from rest_framework import serializers
from .models import Product, Tag, Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'post_date', 'price', 'description', 'category', 'tags']