from django import forms
from .models import Author, QA
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, IntegerField, ImageField
class QAF(ModelForm):
    titlename = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": " Укажите адрес "}))
    content = forms.CharField(widget=forms.Textarea(attrs={"placeholder": " Место для вашего вопроса "}))
    class Meta:
        model = QA
        fields = ['titlename', 'content']
class ClientForm(forms.Form):
    email = forms.EmailField(label = "gjxnf",widget=forms.EmailInput(attrs={"placeholder": " Укажите адрес "}))
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Как я могу к вам обращаться "})) 
    post_type = forms.ChoiceField(choices=Author.POST_TUPE, label ='Тип съёмки')
    data = forms.CharField(max_length=5, label = 'Дата', widget=forms.TextInput(attrs={"placeholder": " Формат: дд/мм "})) 
    time02 = forms.CharField(max_length=5, label = 'Время(минимум - 1 час)',widget=forms.TextInput(attrs={"placeholder": " Формат:чч:мм "}))
    time = forms.CharField(max_length=5, label = 'Время(минимум - 1 час)',widget=forms.TextInput(attrs={"placeholder": " Формат:чч:мм "}))
    
    
    def clean_time(self):
        email_data = self.cleaned_data['email']
        
        name_data = self.cleaned_data['name']
        data_data = self.cleaned_data['data']
        time02_data = self.cleaned_data['time02']
        time_data = self.cleaned_data['time']
     
        if email_data == name_data:
            raise ValidationError('uncorrect')
       
        if len(time_data)<5:
            raise ValidationError('Проверьте корректность ввода времени записи')
        if len(time02_data)<5:
            raise ValidationError('Указан неверный формат времени')
        if len(data_data)<5:
            raise ValidationError('Указан неверный формат времени')
        if data_data[0]=='3' and data_data[1]=='2' or data_data[0]=='3' and data_data[1]=='3' or data_data[0]=='3' and data_data[1]=='4'or data_data[0]=='3' and data_data[1]=='5'or data_data[0]=='3' and data_data[1]=='6' or data_data[0]=='3' and data_data[1]=='7' or data_data[0]=='3' and data_data[1]=='8' or data_data[0]=='3' and data_data[1]=='9':
            raise ValidationError('Указан неверный формат времени')
        if data_data[3]!='0' and data_data[3]!='1':
            raise ValidationError('Указан неверный формат времени')
        if data_data[0]!='0' and data_data[0]!='1' and data_data[0]!='2' and data_data[0]!='3':
            raise ValidationError('Указан неверный формат времени')
        if data_data[3]=='1' and data_data[4]=='3' or data_data[3]=='1' and data_data[4]=='4' or data_data[3]=='1' and data_data[4]=='5' or data_data[3]=='1' and data_data[4]=='6' or data_data[3]=='1' and data_data[4]=='7'  or data_data[3]=='1' and data_data[4]=='8' or data_data[3]=='1' and data_data[4]=='9':
            raise ValidationError('Указан неверный формат времени')
        if name_data.isalpha() ==False:
            raise ValidationError('Указан неверный формат имени')
        if time_data[0]!='0' and time_data[0]!='1' and time_data[0]!='2':
            raise ValidationError('Указан неверный формат времени')
        if time_data[0]=='2' and time_data[1]=='4' or time_data[0]=='2' and time_data[1]=='5' or time_data[0]=='2' and time_data[1]=='6' or time_data[0]=='2' and time_data[1]=='7' or time_data[0]=='2' and time_data[1]=='8' or time_data[0]=='2' and time_data[1]=='9'  :
            raise ValidationError('Указан неверный формат времени')
        if time02_data[0]=='2' and time02_data[1]=='4' or time02_data[0]=='2' and time02_data[1]=='5' or time02_data[0]=='2' and time02_data[1]=='6' or time02_data[0]=='2' and time02_data[1]=='7' or time02_data[0]=='2' and time02_data[1]=='8' or time02_data[0]=='2' and time02_data[1]=='9'  :
            raise ValidationError('Указан неверный формат времени')
        if time02_data[3]!='0' and  time02_data[3]!='3':
            raise ValidationError('Указан неверный формат времени')
        if time_data[3]!='0' and  time_data[3]!='3':
            raise ValidationError('Указан неверный формат времени')
        if time02_data[4]!='0':
            raise ValidationError('Указан неверный формат времени')
        if time_data[4]!='0':
            raise ValidationError('Указан неверный формат времени')
        if time_data == time02_data:
            raise ValidationError('Указан неверный формат времени')
        if time02_data[0]!='0' and time02_data[0]!='1' and time02_data[0]!='2':
            raise ValidationError('Указан неверный формат времени')
        if '/' not in data_data:
            raise ValidationError('Указан неверный формат времени')
        if ':' not in time02_data:
            raise ValidationError('Указан неверный формат времени')
        if ':' not in time_data:
            raise ValidationError('Указан неверный формат времени')
       
        return time_data
      

 
  