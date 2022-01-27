from .models import Portfolio
from django.forms import ModelForm, TextInput
import datetime
class StudiesForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'ac_advisor', 'originality']
        widgets = {
            'title': TextInput(attrs={
                'class':'form-control',
                'placeholder':'Название работы'
            }),
            'ac_advisor': TextInput(attrs={
                'class':'form-control',
                'placeholder':"Научный руководитель"
            }),
            'originality': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Уникальность"
            }),
        }
