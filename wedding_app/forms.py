from django import forms
from .models import QuestFeedBack


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