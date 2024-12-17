from django.db import models
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    # add author later

    def __str__(self):
        return self.title
    

    def snippet(self):
        return self.body[:150] + "..."
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Automatically create a URL-safe slug
        super().save(*args, **kwargs)