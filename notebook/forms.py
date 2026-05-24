from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['sub_category', 'title', 'command', 'description','reference']