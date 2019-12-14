from django import forms
from webapp.models import Gallery

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['images', 'signature', 'author','laike']