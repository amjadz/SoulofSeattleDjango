from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactToAddEventForm
from .models import Article

# Create your views here.

def home(request):
    if request.method == 'GET':
        data = Article.objects.all()

        articles = {
            "articles": data

        }

    return render(request, 'home.htm', articles)

def article(request, article_title):
    return render(request, 'article.htm')

def resources(request):
    return render(request, 'resources.htm')

def mosquemap(request):
    return render(request, 'mosquemap.htm')

def calender(request):
    if request.method == 'GET':
        form = ContactToAddEventForm()
    else:
        form = ContactToAddEventForm(request.POST)
        if form.is_valid():
            event_name = form.cleaned_data['event_name']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(event_name, message, 'amjadzubair931@gmail.com' ,[your_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse("Your email has been sent!")
    return render(request, 'calender.htm', {'form': form})


