from .models import Pictures
from django.forms import ModelForm, TextInput, Textarea


class PicturesForm(ModelForm):
    class Meta:
        model = Pictures
        fields = ['title', 'picture', 'description']

    widgets = {
        'title': TextInput(attrs={
            'placeholder': 'Название картины',
            'class': 'form-control',
        }),
        'picture': TextInput(attrs={
            'placeholder': 'url ссылка на изображение',
            'class': 'form-control',
        }),
        'full_text': Textarea(attrs={
            'placeholder': 'Описание картины',
            'class': 'form-control',
        }),
    }
