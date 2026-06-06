from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Tag, Category
from django.urls import reverse
from django.views import generic


def product_list(request):
    products = Product.objects.order_by("-post_date")
    context = {"products": products}
    print(request)
    print("HELLOOO")
    return render(request, "products/product-list.html", context)


