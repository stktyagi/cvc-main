from django.db import models
  

class Portfolio(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    link = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    created_on = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.title
    