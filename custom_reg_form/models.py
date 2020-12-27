from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    
    phone_number = models.CharField(
        verbose_name="Phone Number",
        max_length=100,
    )
    
    def __str__(self):
        result = '{0.user} {0.phone_number}'
        return result.format(self)
