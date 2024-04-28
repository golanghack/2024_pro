from django.db import models
from django.urls import reverse


class Category(models.Model):
    """The Category model.

    Attributes:
        name: string of name a stuff.
        slug: string of slug.
        ordering: orderign a stuff.
        indexes: index in db.
        verbose_name: name in table.
        verbose_name_plural: names in table.
        get_absolute_url: a standart function for absolute urls.
    """

    name = models.CharField(max_length=250, help_text="name a product")
    slug = models.SlugField(max_length=300, unique=True, blank=False)

    class Meta:
        ordering = [
            "name",
        ]
        indexes = [
            models.Index(
                fields=[
                    "name",
                ]
            ),
        ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """Product model.
    Attributes:
        category: string a category name as foreign key.
        name: string a name.
        slug: string a slug.
        image: image file for product.
        description: desc for prodict.
        price: decimal type for price a product.
        created: a date created a product.
        updated: a date updated a product.
        ordering: ordeing a products.
        indexes: indexes for products.
        available: boolean for exist a product.
        get_absolute_url: a standart function for get absolute urls.
    """

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200, help_text="name a product")
    slug = models.SlugField(max_length=300, blank=False)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "name",
        ]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
