from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


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


class Contact(models.Model):
    """Model for Contact profile.

    Attributes:
            user_from: An user from.
            user_to: An user to.
            created: Date a formation net.
    """

    user_from = models.ForeignKey(
        "auth.User", related_name="related_from_set", on_delete=models.CASCADE
    )
    user_to = models.ForeignKey(
        "auth.User", related_name="related_to_set", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
        ]

    ordering = [
        "-created",
    ]

    def __str__(self):
        return f"{self.user_from} follow {self.user_to}"


# dinamicaly added filed in User model
user_model = get_user_model()
user_model.add_to_class(
    "following",
    models.ManyToManyField(
        "self", through=Contact, related_name="followers", symmetrical=False
    ),
)
