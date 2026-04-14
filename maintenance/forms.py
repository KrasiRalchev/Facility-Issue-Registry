from django import forms
from maintenance.models import MaintenanceAction


class MaintenanceCreateForm(forms.ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = ['performer', 'performer_name', 'requires_parts']
        labels = {'performer_name': 'Performer name / company name',
                          'cost': 'Cost in €',
                          'requires_parts': 'Necessary parts',
                          }

class MaintenanceResolveForm(forms.ModelForm):
    class Meta:
        model = MaintenanceAction
        fields = ['performer', 'performer_name', 'delivery_request', 'cost', 'action_description', 'resolved_on']

        widgets = {
            'resolved_on': forms.DateInput(attrs={'type': 'date'}),
            'action_description': forms.Textarea(attrs={'rows': 5, 'cols': 50,
            'placeholder': 'Describe the measures taken here... '}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['delivery_request'].disabled = True
        self.fields['performer'].disabled = True









