from django.urls import path
from blog.views import post_detail
from blog.views import post_list
from blog.views import post_share
from blog.views import post_comment

app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"
    ),
    path("<int:post_id>/share/", post_share, name="post_share"),
    path("<int:post_id>/comment/", post_comment, name="post_comment"),
    path("tag/<slug:tag_slug>/", post_list, name="post_list_by_tag"),
]
