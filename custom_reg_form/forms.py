from .models import ExtraInfo
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
import logging


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True

    class Meta(object):
        model = ExtraInfo
        fields = ('phone_number',)
        labels = {'phone_number': _("Phone number"),}
        help_text = {'phone_number': _("Please enter your phone number"),}
