from django import forms
from mtlpy.shortener.models import Shortcut

class ShortcutForm(forms.ModelForm):
    class Meta:
        model = Shortcut
        fields = ('link',)
