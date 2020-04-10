from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductosListView.as_view(), name='index'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto'),
    path('producto/create/', views.CreateProductoView.as_view(), name='producto_create'),
    path('pedidos/', views.PedidosListView.as_view(), name='pedidos'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido'),
    path('pedido/create/', views.CreatePedidosView.as_view(), name='pedido_create'),
 ]
