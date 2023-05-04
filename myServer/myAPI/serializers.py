from rest_framework import serializers
from .models import Category, MenuItem
from datetime import datetime
from decimal import Decimal

class CategorySerializer(serializers.ModelSerializer):     
    class Meta:
        model = Category
        fields = '__all__'
        
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, min_value=2)
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField()#CategorySerializer() 
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name='category-detail')
      
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'category', 'featured', 'stock', 'price_after_tax']
        # validators = [
        #      UniqueTogetherValidator(
        #          queryset=MenuItem.objects.all(),
        #          fields=['title', 'price']
        #      ),
        # ]
        depth = 1
        # extra_kwargs = {
        #      'price': {'min_value': 2},
        #      'stock':{'source':'inventory', 'min_value': 0},
        # }
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)        