from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactToAddEventForm
from .models import Post

# Create your views here.

def home(request):
    if request.method == 'GET':
        queryset = Post.objects.filter(status=1).order_by('-created_on')

        articles = {
            "articles": queryset

        }

    return render(request, 'home.htm', articles)

def article(request, slug):
    article = Post.objects.filter(slug=slug).values()

    article_info = {
        "object": article
    }

    return render(request, 'article.htm', article_info)

def resources(request):
    return render(request, 'resources.htm')

def community(request):
    return render(request, 'community.htm')

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
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']
            event_date = form.cleaned_data['event_date'] 
            message = form.cleaned_data['message']

            email_message = message + " " + ("start time: " + start_time) + " " + ("end time:" + end_time) + " " + str(event_date) 
            
            try:
                send_mail(event_name, email_message, 'amjadzubair931@gmail.com' ,[your_email], html_message=None)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse("Your email has been sent!")
    return render(request, 'calender.htm', {'form': form})


