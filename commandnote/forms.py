from django import forms
from .models import Note, Command

class NoteForm(forms.ModelForm):
  class Meta:
    model = Note
    fields = ['sub_category', 'title', 'description', 'reference']

class CommandForm(forms.ModelForm):
  class Meta:
    model = Command
    fields = ['code']