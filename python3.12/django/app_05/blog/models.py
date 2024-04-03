from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    """Custom manager for published post."""

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    """ 
    The Post class model.

    Attributes:
        title: string for title of a post in blog.
        slug: string for a represent the url post of a blog.
        body: string (option a text) for a contant in blog post.
        __str__: string presention a class Post.
        publish: The date of publish post.
        created: The date of create post.
        updated: The date of update post.
        status: The status for post.
        author: The user as an author for a post.
        objects: The default manager for models Post data.
        published: The custom manager for work with posts.
    """

    class Status(models.TextChoices):
        """Status of writable a post."""

        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(
        max_length=256, help_text="use title for name of blog post"
    )
    slug = models.SlugField(max_length=256, unique_for_date="publish")
    body = models.TextField(help_text="Enter a contant of blog post")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        """Default ordering for posts."""

        ordering = ["-publish"]
        indexes = [models.Index(fields=["-publish"])]

    def __str__(self):
        """Returns the title of the Post."""

        return f"{self.title}"

    def get_absolute_url(self):
        """Find url from resources"""

        return reverse(
            "blog:post_detail",
            args=[self.publish.year, self.publish.month, self.publish.day, self.slug],
        )

class Comment(models.Model):
    """Comments model for comments of users to posts.
    
    Attributes:
            post: The related post for comments.
            name: The name a string of comments.
            email: The email for user send a comments to post.
            body: The text for comments to post from user.
            created: The date was create a comment for post.
            updated: The date was updated a comment for post.
            active: The boolean flag for status of comments.
    """
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created',]
        indexes = [models.Index(fields=['created']),]
        
    def __str__(self) -> str:
        return f'Comment by {self.name} on {self.post}'