from django.shortcuts import render
from .models import Product
from django.db.models import Q
from .forms import ProductSearchForm


def product_list(request):
    products = Product.objects.order_by("-post_date")

    form = ProductSearchForm(request.GET)

    
    if form.is_valid():

        search = form.cleaned_data["search"]
        category = form.cleaned_data["category"]
        tags = form.cleaned_data["tags"]

        if search:
            products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))

        if category:
            products = products.filter(category=category)

        if tags:
            products = products.filter(tags__in=tags).distinct()

    context = {
                "products": products,
                "form": form
                }
    return render(request, "products/product-list.html", context)


