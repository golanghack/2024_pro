from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag
def total_posts() -> int:
    """Return a full count a posts published."""

    return Post.published.count()
