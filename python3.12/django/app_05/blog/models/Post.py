from django.db import models

class Post(models.Model):
    """ 
    The Post class model.

    Attributes:
        title: string for title of a post in blog.
        slug: string for a represent the url post of a blog.
        body: string (option a text) for a contant in blog post.
        __str__: string presention a class Post.
    """ 

    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    body = models.TextField()

    def __str__(self):
        return self.title

    
