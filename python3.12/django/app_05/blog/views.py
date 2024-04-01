from django.shortcuts import render, get_object_or_404
from blog.models import Post 

def post_list(request: str):
    """Formation a list for posts.
    
    Get all objects a posts return context, request, dict.
    """
    
    posts = Post.published.all()
    temp = 'blog/post/list.html'
    context = {'posts': posts,}
    return render(request, temp, context) 

def post_detail(request: str, year: int, month: int, day: int, post: str):
    """Get detail information about a post with id."""
    
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED,
                             slug=post, 
                             publish__year=year,
                             publish__month=month, 
                             publish__day=day,)
    temp = 'blog/post/detail.html'
    context = {'post': post,}
    return render(request, temp, context)