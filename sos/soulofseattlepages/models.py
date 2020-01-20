from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200, unique=True)
    author_biography = models.TextField(default="N/A")
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    upload_image = models.ImageField(default="default.png", blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title