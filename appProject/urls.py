from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductosListView.as_view(), name='productos'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto'),
    path('producto/create/', views.CreateProductoView.as_view(), name='producto_create'),
    path('productos/delete/<int:producto_id>/', views.delete_producto, name='producto_delete'),
    path('productos/edit/<int:producto_id>/', views.edit_producto, name='producto_edit'),
    path('pedidos/', views.PedidosListView.as_view(), name='pedidos'),
    path('pedido/<int:pk>/', views.PedidoDetailView.as_view(), name='pedido'),
    path('pedido/create/', views.CreatePedidosView.as_view(), name='pedido_create'),
    path('clientes/', views.ClientesListView.as_view(), name='clientes'),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente'),
    path('cliente/create/', views.CreateClienteView.as_view(), name='cliente_create'),
    path('clientes/delete/<int:cliente_id>/', views.delete_cliente, name='cliente_delete'),
    path('clientes/edit/<int:cliente_id>/', views.edit_cliente, name='cliente_edit'),
    path('componentes/', views.ComponentesListView.as_view(), name='componentes'),
    path('componente/<int:pk>/', views.ComponenteDetailView.as_view(), name='componente'),
    path('componente/create/', views.CreateComponenteView.as_view(), name='componente_create'),
    path('componentes/delete/<int:componente_id>/', views.delete_componente, name='componente_delete'),
    path('componentes/edit/<int:componente_id>/', views.edit_componente, name='componente_edit'),
]
