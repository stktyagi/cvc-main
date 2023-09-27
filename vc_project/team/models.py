from django.db import models
from ckeditor.fields import RichTextField

class Team(models.Model):
    name = models.CharField(max_length = 200, null=True, blank=True)
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique=True)
    country = models.CharField(max_length = 200, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    linkedin = models.URLField(max_length = 200, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    created_on = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
