from django import forms
from .models import QuestFeedBack, AuthModel


class QuestFeedBackForm(forms.ModelForm):
    class Meta:
        model = QuestFeedBack
        fields = '__all__'
        labels = {
            'name': 'Ваше имя',
            'surname': 'Ваша фамилия',
        }
        widgets = {
            'para': forms.RadioSelect()
        }


class AuthForm(forms.ModelForm):
    class Meta:
        model = AuthModel
        fields = '__all__'
        labels = {
            'field': 'Введите сверхсекретный пароль'
        }
