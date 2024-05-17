from django.forms import ModelForm
from .models import Photo
from django import forms


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'category', 'image', 'description']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})
