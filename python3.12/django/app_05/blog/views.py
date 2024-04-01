from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from blog.models import Post 

def post_list(request: str):
    """Formation a list for posts.
    
    Get all objects a posts return context, request, dict.
    """
    
    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 3)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
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