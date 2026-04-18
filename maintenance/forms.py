from django import forms

from common.utils import RequiredFieldsMarkerMixin
from maintenance.models import MaintenanceAction


class MaintenanceCreateForm(RequiredFieldsMarkerMixin, forms.ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = ['performer', 'performer_name', 'requires_parts']
        labels = {'performer_name': 'Performer name / company name',
                          'cost': 'Cost in €',
                          'requires_parts': 'Necessary parts',
                          'performer': 'Type of service:',
                 }
        widgets = {'performer': forms.Select(attrs={'class': 'form-control'}),
                   'performer_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'requires_parts': forms.Select(attrs={'class': 'form-control'}),
                   }


class MaintenanceResolveForm(forms.ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = ['performer', 'performer_name', 'cost', 'action_description', 'resolved_on']

        widgets = {
            'resolved_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'action_description': forms.Textarea(attrs={'rows': 5, 'cols': 50,
            'placeholder': 'Describe the measures taken here... ',  'class': 'form-control'}),
            'performer': forms.TextInput(attrs={'class': 'form-control'}),
            'performer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {'cost': 'Cost in Euro',}
        help_texts = {'cost': 'Insert total cost after performance!'}


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['performer'].disabled = True
        self.fields['performer_name'].disabled = True









