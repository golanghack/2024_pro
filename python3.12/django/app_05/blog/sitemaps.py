from django.contrib.sitemaps import Sitemap
from blog.models import Post

class PostSitemap(Sitemap):
    """Create sitemap for post."""
    
    # change a post in time
    changefreq = 'weekly'
    # relevations
    priority = 0.9
    
    def items(self):
        """Return posts for sitemap."""
        
        return Post.published.all()
    
    def lastmod(self, obj):
        """Last modifycation"""
        
        return obj.updated