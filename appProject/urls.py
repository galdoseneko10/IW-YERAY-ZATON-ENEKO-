from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductosListView.as_view(), name='index'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto'),
    path('producto/create/', views.CreateProductoView.as_view(), name='producto_create'),
 ]
