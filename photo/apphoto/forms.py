from django import forms
from .models import Author, QA
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, IntegerField, ImageField

class ClientForm(forms.Form):
    email = forms.EmailField(label = 'Email')
    name = forms.CharField(max_length=1000, label = 'ФИО') 
    post_type = forms.ChoiceField(choices=Author.POST_TUPE, label ='Тип съёмки')
    data = forms.CharField(max_length=10, label = 'Дата') 
    time = forms.CharField(max_length=11, label = 'Время(минимум - 1 час)')
    
    def clean_time(self):
        email_data = self.cleaned_data['email']
        
        name_data = self.cleaned_data['name']
        time_data = self.cleaned_data['time']
     
        
        
        
        
        if email_data == name_data:
            raise ValidationError('uncorrect')
      
        if len(time_data)<11:
            raise ValidationError('uncorrect len')
       
       
       
            
            
        
        return time_data
      
class QAF(ModelForm):
    class Meta:
        model = QA
        fields = ['titlename', 'content']
    
 
  