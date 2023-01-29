from django.urls import path, include

from . import views

urlpatterns = [

    path('products/<int:pk>/', views.ProductsView.as_view({'get': 'retrieve'})),
    path('products/', views.ProductsView.as_view({'get': 'list'})),
    path('categories/<int:category_id>/products/', views.ProductsView.as_view({'get': 'find_with_category'})),
    path('categories/<int:pk>/', views.CategoriesView.as_view({'get': 'retrieve'})),
    path('categories/', views.CategoriesView.as_view({'get': 'list'})),
]