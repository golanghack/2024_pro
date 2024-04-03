from django.contrib import admin
from blog.models import Post
from blog.models import Comments


@admin.register(Post)
class PostAdminInterface(admin.ModelAdmin):
    """Inteface for administration a Post"""

    list_display = ["title", "slug", "author", "publish", "status"]
    list_filter = ["status", "created", "publish", "author"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    """Administration of admin model"""
    
    list_display = ['name', 'email', 'post', 'created', 'active',]
    list_filter = ['active', 'created', 'updated',]
    search_fields = ['name', 'email', 'body',]
    