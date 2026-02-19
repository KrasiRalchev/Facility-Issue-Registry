from django import forms
from maintenance.models import MaintenanceAction


class MaintenanceCreateForm(forms.ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = ['performer', 'delivery_request',]


class MaintenanceResolveForm(forms.ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = ['performer', 'performer_name', 'delivery_request', 'cost', 'action_description', 'resolved_on']
        labels = {'performer_name': 'Performer name / company name', 'cost': 'Cost in €',}

        widgets = {
            'resolved_on': forms.DateInput(attrs={'type': 'date'}),
            'action_description': forms.Textarea(attrs={'rows': 5, 'cols': 50,
            'placeholder': 'Describe the measures taken here... '}),
            'cost': forms.NumberInput(attrs={'type': 'number',}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_request'].disabled = True
        self.fields['performer'].disabled = True









