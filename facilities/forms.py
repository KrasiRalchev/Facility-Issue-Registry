from django import forms

from facilities.models import Facility


class FacilityFormBase(forms.ModelForm):
    class Meta:
        model = Facility
        exclude = ['is_active']
        widgets = {
            'installed_on' : forms.DateInput(attrs={'type': 'date'}),
            'description' : forms.Textarea(attrs={'rows': 6})
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


class FacilityCreateForm(FacilityFormBase):
    ...

class FacilityEditForm(FacilityFormBase):
    ...

class FacilityDeleteForm(FacilityFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True



