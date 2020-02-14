from django.contrib import admin
from .models import author, userPost

# Register your models here.

class userAdminPost(admin.ModelAdmin):
    list_display = ('post_Title', 'post_Slug', 'post_Status', 'post_CreatedOn')
    list_filter = ("post_Status")
    search_fields = ['post_Title', 'post_Content']
    prepopulated_fields = {'post_Slug': ('post_Title')}

class userAuthorAdminPost(admin.ModelAdmin):
    list_display = ('author_firstName', 'author_lastName')

admin.site.register(author)
admin.site.register(userPost)

