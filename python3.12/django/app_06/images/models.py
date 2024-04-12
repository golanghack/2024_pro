from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    """Image model

    Attributes:
            title: A string of title for image.
            slug: A slug formation for image.
            user: An user with image.
            url: An url for downloaded image.
            image: An image file for downloaded in file system.
            description: A description for image.
            created: An image created date.
            indexes: An indexes for image in db.
            ordering: An order for sort.
            users_like: An user liked images many_to_many field.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="images_created",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=3000)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    users_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="images_liked", blank=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["-created"]),
        ]
        ordering = [
            "-created",
        ]

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        """Customisation a save function from models."""

        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
