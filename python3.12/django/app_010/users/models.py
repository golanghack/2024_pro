from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class LowerCaseEmailField(models.EmailField):
    """
    Email model for user
    """

    def get_prep_value(self, value):
        """Get prepolation email from user and lower"""

        if value:
            return str(value).lower()
        return None


class User(AbstractUser):
    """
    User model
    """

    # email
    email = LowerCaseEmailField(_('email address'), unique=True)
    # fields 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('pk',)
