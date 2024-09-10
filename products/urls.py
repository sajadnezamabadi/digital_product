from django.urls import path 

from .views import *

urlpatterns = [
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detil"),
    
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("products/<int:product_id>/files", FIleListView.as_view(), name="file-list"),
    path("products/<int:product_id>/files/<int:pk>", FileDetailView.as_view(), name="file-detail")
]
