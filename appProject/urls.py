from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductosListView.as_view(), name='index'),
    path('producto/<int:producto_id>', views.ProductoDetailView.as_view(), name='producto')
 ]
