from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class author(models.Model):
   author_firstName = models.CharField(max_length = 30)
   author_lastName = models.CharField(max_length = 30)
   author_biography = models.CharField(max_length = 255)

   def __str__(self):
       return self.author_firstName + " " + self.author_lastName
class userPost(models.Model):
   author = models.ForeignKey(author, on_delete = models.CASCADE)
   post_Title = models.CharField(max_length = 255, unique = True)
   post_Slug = models.CharField(max_length = 255, unique = True)
   post_Content = models.TextField()
   post_CreatedOn = models.DateTimeField(auto_now_add = True)
   post_UploadImage = models.ImageField(default = "default.png", blank = True)
   post_Status = models.IntegerField(choices = STATUS, default = 0)
   post_Tags = TaggableManager()
   post_Category = models.CharField(max_length = 200)

   class Meta:
       ordering = ['-post_CreatedOn']

   def __str__(self):
       return self.post_Title


  