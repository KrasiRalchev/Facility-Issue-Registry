from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from warehouse.forms import ProductListForm, ProductUpdateForm, ProductDeleteForm
from warehouse.models import Product


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'warehouse/product_list.html'

    def get_queryset(self):
        category = self.request.GET.get('category')
        q = self.request.GET.get('q')
        if category:
            return Product.objects.filter(category__name__iexact=category)
        elif q:
            return Product.objects.filter(name__istartswith=q)
        return Product.objects.all()


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model = Product
    form_class = ProductListForm
    template_name = 'warehouse/product_create.html'
    success_url = reverse_lazy('warehouse:product-list')

    permission_required = 'product.add_product'


class ProductEditView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductUpdateForm
    template_name = 'warehouse/product_edit.html'
    success_url = reverse_lazy('warehouse:product-list')

    permission_required = 'product.change_product'
    error_url = 'warehouse:error'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'warehouse/product_delete.html'
    success_url = reverse_lazy('warehouse:product-list')

    permission_required = 'product.delete_product'
    error_url = 'warehouse:error'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductDeleteForm(instance=self.object)
        return context