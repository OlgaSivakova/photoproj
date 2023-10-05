from django.shortcuts import render, HttpResponse, redirect
from .models import Author, QA
from.forms import ClientForm, QAF

# Create your views here.
def home(request):
    return render(request, 'home.html')
def slider(request):
    return render(request, 'slider.html')
def sucsess(request):
    return render(request, 'sucsess.html')
def qa(request):
    return render(request, 'qa.html')
def me(request):
    return render(request, 'me.html')
def new(request):
    return render(request, 'new.html')
def thank(request):
    return render(request, 'thank.html')
def post(request):
    try:
        posts = Post.objects.all()
    except:
        posts = False
    return render(request, 'post.html', {'posts':posts})
def client(request):
    error = ''
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            author = Author()
            author.name = form.cleaned_data['name']
            author.email = form.cleaned_data['email']
            author.data = form.cleaned_data['data']
            author.time = form.cleaned_data['time']
            author.time02 = form.cleaned_data['time02']
            author.post_type = form.cleaned_data['post_type']
            
            author.save()
            return redirect('sucsess')
        else:
            error = form.errors
    else:
        form = ClientForm()
    return render(request, 'add.html', {'form':form,'error': error})

def QA(request):
    error = ''
    if request.method == "POST":
        forms = QAF(request.POST)
        if forms.is_valid():
                forms.save()
                return redirect('home')
        else:
            error = 'Проверьте корректность ввода данных'
    else:
        forms = QAF()
    return render(request, 'qa.html', {'forms':forms, 'error': error})


