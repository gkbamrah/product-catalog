from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Product
from django.db.models import Q
from .forms import ProductSearchForm
from .serializers import ProductSerializer


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

@api_view(["GET"])
def product_list_api(request):
    products = Product.objects.order_by("-post_date")
    
    search = request.GET.get("search")
    category = request.GET.get("category")
    tags = request.GET.getlist("tags")
    
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))

    if category:
        products = products.filter(category=category)

    if tags:
        products = products.filter(tags__in=tags).distinct()
        
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)