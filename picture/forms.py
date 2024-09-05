from django import forms
from .models import Picture


class NewPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields=['category','name','description','image',]
    def __init__(self, *args, **kwargs):
        super(NewPictureForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class EditPictureForm(forms.ModelForm):
    class Meta:
        model=Picture
        fields=['name','description','image',]
    def __init__(self, *args, **kwargs):
        super(EditPictureForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
