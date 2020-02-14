from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactToAddEventForm
from .models import author, userPost
from taggit.models import Tag


#Create your views here.

def home(request):
    if request.method == 'GET':
        queryset = userPost.objects.filter(post_Status=1).order_by('-post_CreatedOn')

        articles = {
            "articles": queryset
        }
    return render(request, 'home.htm', articles)

def article(request, post_Slug):
    article = userPost.objects.filter(post_Slug=post_Slug).values()
    related_articles = userPost.objects.get(post_Slug=post_Slug)

    article_info = {
        "article": article,
        "related_articles" : related_articles.tags.similar_objects(),  # Instance of Post is article
    }

    return render(request, 'article.htm')

def lifestyle(request):
   # if request.method == 'GET':

        #lifestyle_article = Post.objects.filter(category='lifestyle').values()

        #lifestyle_articles = {
            #"lifestyle_articles": lifestyle_article
        #}

    return render(request, 'categories/lifestyle.htm')

def politics(request):
    return render(request, 'categories/politics.htm')

def opinion(request):
    return render(request, 'categories/opinion.htm')

def food(request):
    return render(request, 'categories/food.htm')

def travel(request):
    return render(request, 'categories/travel.htm')

def health(request):
    return render(request, 'categories/health.htm')

def tech(request):
    return render(request, 'categories/tech.htm')







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


