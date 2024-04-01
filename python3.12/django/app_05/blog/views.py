from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.mail import send_mail
from blog.models import Post
from blog.forms import EmailPostForm
from decouple import Config, RepositoryEnv
config = Config(RepositoryEnv(".env"))


def post_list(request: str):
    """Formation a list for posts.
    
    Get all objects a posts return context, request, dict.
    """

    posts_list = Post.published.all()
    paginator = Paginator(posts_list, 2)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
    temp = "blog/post/list.html"
    context = {"posts": posts}
    return render(request, temp, context)


def post_detail(request: str, year: int, month: int, day: int, post: str):
    """Get detail information about a post with id."""

    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    temp = "blog/post/detail.html"
    context = {"post": post}
    return render(request, temp, context)


def post_share(request: str, post_id: int):
    """Return a post for id"""

    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    # flag of sending 
    flag = False 
    # condition
    if request.method == "POST":
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # success
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f'{cd['name']} recomended for you ' f'{post.title}'
            message = f'Read {post.title} at {post_url}\n\n' f'{cd['name']} comments -> {cd['comments']}'
            send_mail(subject, message, f"{config('EMAIL_HOST_USER')}", [cd['to']])
            flag = True
    form = EmailPostForm()
    temp = "blog/post/share.html"
    context = {"post": post, "form": form, 'sent': flag,}
    return render(request, temp, context)
