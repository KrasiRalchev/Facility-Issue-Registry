from django import forms
from common.utils import RequiredFieldsMarkerMixin, FieldsDisabledMixin
from issues.models import Issue


class IssueFormBase(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['facility', 'location', 'description', 'priority', 'issue_image', 'tags']

        widgets = {
            'facility': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'created_at' : forms.DateInput(attrs={'type': 'date'}),
            'description' : forms.Textarea(attrs={'rows': 6, 'cols': 60,
                 'placeholder': ' Insert issue description and details here...', 'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
        }

        labels = {
            'title': 'Issue Title',
            'description': 'Description',
            'tags': "Special requirements",
        }

        help_texts = {
            'location': 'e.g.: Terminal 2 / roof',
        }

class IssueFormCreate(RequiredFieldsMarkerMixin, IssueFormBase):
    ...

class IssueFormEdit(RequiredFieldsMarkerMixin, IssueFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['facility'].disabled = True

class IssueFormDelete(FieldsDisabledMixin, IssueFormBase):
   ...

