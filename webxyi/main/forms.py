from .models import Aga
from django.forms import ModelForm, TextInput, Textarea


class AgaForm(ModelForm):
    class Meta:
        model = Aga
        fields = ['name', 'age', 'history', 'content', 'invite']

        widgets = {
            "name": TextInput(attrs={
                'class': 'fon',
                'placeholder': 'Имя'
            }),
            "age": TextInput(attrs={
                'class': 'fon',
                'placeholder': 'Возраст'
            }),
            "history": Textarea(attrs={
                'class': 'fon',
                'placeholder': 'История моего персонажа начинается с ...',
                'cols': '40',
                'rows': '10'
            }),
            "content": Textarea(attrs={
                'class': 'fon',
                'placeholder': 'Нет/Да(+ссылка)',
                'cols': '40',
                'rows': '10'
            }),
            "invite": Textarea(attrs={
                'class': 'fon',
                'placeholder': 'Я узнал о сервере ...',
                'cols': '40',
                'rows': '10'
            }),
        }