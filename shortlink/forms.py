from django import forms
from .models import ShortLink
from django.core.validators import validate_slug


class ShortLinkForm(forms.ModelForm):

    class Meta:
        link = forms.CharField(label='Длинная ссылка:',
                                    widget=forms.TextInput(attrs={'placeholder': 'Введите ссылку'}))
        word = forms.CharField(label='Сокращенная ссылка:', validators=[validate_slug],
                                     widget=forms.TextInput(attrs={'placeholder': 'Введите слово сокращение'}))
        model = ShortLink
        fields = ['link', 'word']

