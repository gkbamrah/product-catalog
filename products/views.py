from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Category, Product
from django.db.models import Q
from .serializers import CategorySerializer, ProductSerializer


@api_view(["GET", "POST"])
def product_list_api(request):
    
    if request.method == "GET":
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
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)