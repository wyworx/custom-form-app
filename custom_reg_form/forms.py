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
        self.fields['referral_code'].required = False
        

    class Meta(object):
        model = ExtraInfo
        fields = ('referral_code',)
        labels = {'referral_code': _("Referral Code"),}
        help_text = {'referral_code': _("Please enter the public user name of the person who referred you to our website."),}
