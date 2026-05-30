from django import forms
from .models import ErrorNote

class ErrorNoteForm(forms.ModelForm):
  class Meta:
    model = ErrorNote
    fields = ['sub_category','title','error_message','target_file', 'resolution', 'reference' ]