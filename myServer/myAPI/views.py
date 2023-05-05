from django.shortcuts import render
from rest_framework import generics, viewsets , status
from rest_framework.response import Response
from .models import MenuItem, Category
from .serializers import CategorySerializer, MenuItemSerializer

# Create your views here.
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   
    
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # ordering_fields=['price','inventory']
    search_fields=['title','category__title']    