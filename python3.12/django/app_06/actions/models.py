from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    """Action model for users action.

    user: An user created action.
    verb: A verb for declare action for user.
    created: A date for action.
    target_ct: ContentType for model Image.
    target_id: ContentType id for target_ct.
    target: Generic Foreign Key.
    """

    user = models.ForeignKey(
        "auth.User", related_name="actions", on_delete=models.CASCADE
    )
    verb = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="target_obj",
        on_delete=models.CASCADE,
    )
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_ct", "target_id")

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
            models.Index(fields=["target_ct", "target_id"]),
        ]
        ordering = [
            "-created",
        ]
