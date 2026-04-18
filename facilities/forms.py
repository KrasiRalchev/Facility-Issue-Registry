from django import forms
from common.utils import RequiredFieldsMarkerMixin, FieldsDisabledMixin
from facilities.models import Facility


class FacilityFormBase(forms.ModelForm):
    class Meta:
        model = Facility
        exclude = ['is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'cost_center': forms.TextInput(attrs={'class': 'form-control'}),
            'cc_manager': forms.TextInput(attrs={'class': 'form-control'}),
            'inventory_number': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 6,
                    'placeholder': 'ect.: Insert technical data or other information here...',
                    'class': 'form-control'}),
            'installed_on' : forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            }

        labels = {
            'name': 'Facility Name',
            'facility_type': 'Facility Type',
            'cost_center': 'Cc number'
        }
        help_texts = {
            'location': 'e.g.: Terminal 2 / roof'
        }

        error_messages = {
            'name': {
                'required': 'The name should clearly describe the facility'
            }
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('The name should be at least 3 characters long')
        return name


class FacilityCreateForm(RequiredFieldsMarkerMixin, FacilityFormBase):
    ...


class FacilityEditForm(RequiredFieldsMarkerMixin, FacilityFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].disabled = True


class FacilityDeleteForm(FieldsDisabledMixin, FacilityFormBase):
    ...



