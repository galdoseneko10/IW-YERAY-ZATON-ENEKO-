from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductosListView.as_view(), name='productos'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto'),
    path('producto/create/', views.CreateProductoView.as_view(), name='producto_create'),
    path('productos/delete/<int:producto_id>/', views.delete, name='producto_delete'),
    path('pedidos/', views.PedidosListView.as_view(), name='pedidos'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido'),
    path('pedido/create/', views.CreatePedidosView.as_view(), name='pedido_create'),
    path('clientes/', views.ClientesListView.as_view(), name='clientes'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),
    path('cliente/create/', views.CreateClienteView.as_view(), name='cliente_create'),
 ]
