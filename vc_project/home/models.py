from django.db import models
from ckeditor.fields import RichTextField

class Home(models.Model):
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    image_url_section_one = models.URLField(max_length=1024, null=True, blank=True)
    image_section_one = models.ImageField(null=True, blank=True, upload_to='media/')
    content_section_one = RichTextField(blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    icon = models.CharField(max_length=200, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image_section_one = models.ImageField(null=True, blank=True, upload_to='media/')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

