from django import forms

from issues.models import Issue


class IssueFormBase(forms.ModelForm):
    class Meta:
        model = Issue
        exclude = ['is_critical', 'resolved_at']

        widgets = {
           'created_at' : forms.DateInput(attrs={'type': 'date'}),
            'description' : forms.Textarea(attrs={'rows': 6, 'cols': 60,
                'placeholder': ' Insert issue description and details here...'}),
        }

        labels = {
            'title': 'Issue Title',
            'description': 'Description',
        }

        help_texts = {
            'location': 'e.g.: Terminal 2 / roof',
        }

class IssueFormCreate(IssueFormBase):
    ...

class IssueFormEdit(IssueFormBase):
    ...

class IssueFormDelete(IssueFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

