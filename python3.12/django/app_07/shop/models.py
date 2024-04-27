from django.db import models

class Category(models.Model):
    """ The Category model.
    
    Attributes:
        name: string of name a stuff.
        slug: string of slug.
        ordering: orderign a stuff.
        indexes: index in db.
        verbose_name: name in table.
        verbose_name_plural: names in table.
    """
    
    name = models.CharField(max_length=250, help_text='name a product')
    slug = models.SlugField(max_length=300, unique=True, blank=False)
    
    class Meta:
        ordering = ['name',]
        indexes = [
            models.Index(fields=['name',]),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self) -> str:
        return self.name 
    
    
