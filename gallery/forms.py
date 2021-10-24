from .models import Pictures
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class PicturesForm(ModelForm):
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Описание картины',
            'class': 'form-control'
        }
        )
    )

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
        }
