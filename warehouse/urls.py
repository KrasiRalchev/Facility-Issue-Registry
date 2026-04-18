from django.urls import path
from django.views.generic import TemplateView

from warehouse.views import ProductListView, ProductCreateView, ProductEditView, ProductDeleteView

app_name = 'warehouse'


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('create/', ProductCreateView.as_view(), name='product-create'),
    path('edit/<int:pk>/', ProductEditView.as_view(), name='product-edit'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('error/', TemplateView.as_view(template_name='404.html'), name='error'),
]