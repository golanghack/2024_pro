from django.db import models
from django.conf import settings


class Profile(models.Model):
    """Profile model for user account.

    Attributes:
            user: A default user model.
            date_of_birth: date field a birth day of user.
            photo: A photo for user account.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True)

    def __str__(self) -> str:
        return f"Profile of {self.user.username}"
