from django.contrib import admin
from .models import Author, Post, QA

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(QA)
# Register your models here.
