from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def total_posts() -> int:
    """Return a full count a posts published."""

    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=3):
    """REturn last 10 posts in blog."""
    
    latest_posts = Post.published.order_by('-publish')[:count]
    context = {'latest_posts': latest_posts,}
    return context
