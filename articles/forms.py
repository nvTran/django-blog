from .models import Comment
from django import forms


from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# Apply summernote to specific fields.
class SomeForm(forms.Form):
    body = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea
    snippet = forms.CharField(widget=SummernoteWidget())
