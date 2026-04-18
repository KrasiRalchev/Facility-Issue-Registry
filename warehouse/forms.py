from django import forms
from common.utils import RequiredFieldsMarkerMixin, FieldsDisabledMixin
from warehouse.models import Product


class ProductFormBase(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at',)

        widgets = {'created_by': forms.DateInput(attrs={'type': 'date'}),
                   'description': forms.Textarea(attrs={'rows': 6, 'cols': 60,
                        'placeholder': 'Insert short issue description and details here...','class': 'form-control'}),
                   'name': forms.TextInput(attrs={'placeholder': 'Product name','class': 'form-control'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control'}),
                   'category': forms.Select(attrs={'class': 'form-control'}),
                   'internal_code': forms.TextInput(attrs={'class': 'form-control'}),
                   'barcode': forms.TextInput(attrs={'class': 'form-control'}),
                   'unit': forms.Select(attrs={'class': 'form-control'}),
                   'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
                   'min_quantity': forms.NumberInput(attrs={'class': 'form-control'}),
                   }

        labels = {'price': 'Price (Euro)',
                  'quantity': 'Available quantity',
                  'min_quantity': 'Minimum quantity',
                  }


class ProductListForm(RequiredFieldsMarkerMixin, ProductFormBase):
    ...


class ProductUpdateForm(RequiredFieldsMarkerMixin, ProductFormBase):
    ...


class ProductDeleteForm(FieldsDisabledMixin, ProductFormBase):
    ...




