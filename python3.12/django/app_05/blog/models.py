from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    """ 
    
    class Status(models.TextChoices):
        """Status of writable a post."""
        
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=256, help_text='use title for name of blog post')
    slug = models.SlugField(max_length=256)
    body = models.TextField(help_text='Enter a contant of blog post')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                            choices=Status.choices,
                            default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name='blog_posts')
    
    class Meta:
        """Default ordering for posts."""
        
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        """Returns the title of the Post."""
        
        return f'{self.title}'