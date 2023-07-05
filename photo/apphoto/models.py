from django.db import models

# Create your models here.
class Post(models.Model):

    titlename = models.CharField(max_length=100)
    content = models.TextField()
    
    image = models.ImageField(upload_to = 'uploads', blank = True)
    
    
class Author(models.Model):
    POST_TUPE = [('O', "Одиночная фотосессия"), ('G', "Групповая фотосессия"),  ('Т', "Тематическая съёмка"),  ('Б', "Фото без обработки"),  ('О', "Обработка фото"), ('В', "Видеосъёмка")]
    email = models.EmailField(primary_key=True)  
    name = models.CharField(max_length=100) 
    post_type = models.CharField(choices=POST_TUPE, max_length=1, null=True)
    data = models.CharField(max_length=10, unique=True, null=True, default='01/01/24') 
    time = models.CharField(max_length=11, null=True, default='12:00 - 13:00')
    
class QA(models.Model):
    titlename = models.CharField(max_length=100)
    content = models.TextField()
    