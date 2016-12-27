# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile

from machina.conf import settings as machina_settings
from machina.core.db.models import get_model

Attachment = get_model('forum_attachments', 'Attachment')


class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file', 'comment', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['file'].widget.attrs['accept'] = 'audio/*,video/*,image/*'

    def clean_file(self):
        f = self.cleaned_data.get('file', None)
        if not isinstance(f, (InMemoryUploadedFile, TemporaryUploadedFile)):
            return f
        if f.content_type.split('/')[0] not in ['image', 'video', 'audio']:
            raise forms.ValidationError(_(u'File type is not supported'))
        return f


class BaseAttachmentFormset(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.post = kwargs.pop('post', None)
        super(BaseAttachmentFormset, self).__init__(*args, **kwargs)

    def save(self, commit=True, **kwargs):
        if self.post:
            for form in self.forms:
                form.instance.post = self.post
        super(BaseAttachmentFormset, self).save(commit)


AttachmentFormset = modelformset_factory(
    Attachment, AttachmentForm,
    formset=BaseAttachmentFormset,
    can_delete=True, extra=1,
    max_num=machina_settings.ATTACHMENT_MAX_FILES_PER_POST,
    validate_max=True)
