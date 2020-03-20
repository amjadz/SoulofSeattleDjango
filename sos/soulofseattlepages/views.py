from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactToAddEventForm
from .models import author, userPost, CalenderEvent
from taggit.models import Tag
import datetime
import json


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

    return render(request, 'article.htm', article_info)

def lifestyle(request):
    if request.method == 'GET':
        lifestyle_article = userPost.objects.filter(post_Category='Lifestyle').values() 
        
        lifestyle_articles = {
            "lifestyle_articles": lifestyle_article
        }
    return render(request, 'categories/lifestyle.htm', lifestyle_articles)

def politics(request):
    if request.method == 'GET':

        politics_article = userPost.objects.filter(post_Category='Politics').values()

        politics_articles = {
            "politics_articles": politics_article

        }
    return render(request, 'categories/politics.htm', politics_articles)

def opinion(request):

    if request.method == 'GET':
        
        opinion_article = userPost.objects.filter(post_Category='Opinion').values()

        opinion_articles = {
            "opinion_articles": opinion_article
        }


    return render(request, 'categories/opinion.htm', opinion_articles)

def food(request):
    if request.method == 'GET':
        food_article = userPost.objects.filter(post_Category='Food').values()
        
        food_articles = {
            "food_articles": food_article
        }
    return render(request, 'categories/food.htm', food_articles)

def travel(request):
    if request.method == 'GET':

        travel_article = userPost.objects.filter(post_Category='Travel').values()

        travel_articles = {
            "travel_articles": travel_article
        }
    
    return render(request, 'categories/travel.htm', travel_articles)

def health(request):
    if request.method == 'GET':

        health_article = userPost.objects.filter(post_Category='Health').values()

        health_articles = {
            "health_articles": health_article

        }


    return render(request, 'categories/health.htm', health_articles)

def tech(request):
    if request.method == 'GET':
        tech_article = userPost.objects.filter(post_Category='Tech').values()
        
        tech_articles = {
            "tech_articles": tech_article
        }
    return render(request, 'categories/tech.htm', tech_articles)







def resources(request):
    return render(request, 'resources.htm')

def community(request):
    return render(request, 'community.htm')

def mosquemap(request):
    return render(request, 'mosquemap.htm')

def calender(request):
    events = CalenderEvent.objects.all()
    if request.method == 'GET':
        form = ContactToAddEventForm()
        # event_arr = []

        # for i in events:
        #     event_sub_arr = {}
        #     event_sub_arr['title'] = i.event_name
        #     start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
        #     end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
        #     event_sub_arr['start'] = start_date
        #     event_sub_arr['end'] = end_date
        #     event_arr.append(event_sub_arr)
        # return HttpResponse(json.dumps(event_arr))

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

    # context = {
    #     "events" : events
    # }
    return render(request, 'calender.htm', {'form': form})


