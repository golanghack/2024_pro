from django.shortcuts import render
from django.shortcuts import get_object_or_404
from shop.models import Product
from shop.models import Category


def get_product_list(request: str, category_clug: str = None):
    """The view for product list"""

    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_clug)
        products = products.filter(categories=category)
    template_name = "shop/product/list.html"
    context = {
        "category": category,
        "categories": categories,
        "products": products,
    }
    return render(request, template_name, context)
