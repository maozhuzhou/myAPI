from django.urls import path
from . import views

urlpatterns = [
    # path('welcome/',views.welcome),
    # path('secret/',views.secret),
    # path('api-token-auth/',obtain_auth_token),
    # path('categories/', views.CategoryView.as_view()),
    # path('categories/<int:pk>',views.category_detail, name='category-detail'),
    path('categories/', views.CategoryView.as_view({'get':'list','post':'create'})),
    path('categories/<int:pk>/', views.CategoryView.as_view({'get':'retrieve','delete':'destroy','update':'partial_update'})),
    path('menu-items/', views.MenuItemsViewSet.as_view({'get':'list','post':'create'})),
    path('menu-items/<int:pk>/', views.MenuItemsViewSet.as_view({'get':'retrieve','update':'partial_update','delete':'destroy'})),
    
]