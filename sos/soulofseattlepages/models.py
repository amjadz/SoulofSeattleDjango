from django.db import models

# Create your models here.

class Article(models.Model):
    article_author = models.CharField(max_length=50)
    article_title = models.CharField(max_length=50, default="Title")
    article_post_time = models.DateTimeField(auto_now_add=True)
    article_content = models.TextField()
