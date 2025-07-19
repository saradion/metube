from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class creator(models.Model):
    image = models.ImageField(upload_to='craetor/')
    name = models.CharField(max_length=250)
    description = models.TextField()
    contact = models.URLField()
    def __str__(self):
        return self.name


class video_table(models.Model):
    category_choices = (
        ('category1', '1'),
        ('category2', '2'),
        ('category3', '3'),
        ('category4', '4'),
        ('category5', '5'),
        ('category6', '6'),
    )
    category = models.CharField(max_length=50, choices=category_choices)
    video_file = models.FileField(upload_to='videos/')
    title = models.CharField(max_length=250)
    description = models.TextField()
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    creator = models.ForeignKey(creator, on_delete=models.CASCADE, default=' ')

    def __str__(self):
        return self.title



class top_video(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    top_video_file = models.FileField(upload_to='videos/')
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    creator = models.ForeignKey(creator, on_delete=models.CASCADE, default='')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(top_video, self).save(*args, **kwargs)
    def __str__(self):
        return self.title
    
    @property
    def file_id(self):
        return self.top_video_file.id

    
class maincontent(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Footer(models.Model):
    poster = models.ImageField(upload_to='footer/')
    social_media_links = models.JSONField() 

    def __str__(self):
        return "Footer Content"
    

class search_bar(models.Model):
    title = models.CharField(max_length=100, default= None)

    def __str__(self):
        return self.query
    

class ads(models.Model):
    name = models.CharField(max_length=200, default='sponsor')
    image = models.ImageField(upload_to='ads/', default=None)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "ads content"


class news(models.Model):
    poster = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=250)
    news_text= models.TextField()
    source = models.URLField()

    def __str__(self):
        return self.title


class post(models.Model):
    poster = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=250)
    post_text= models.TextField()

    def __str__(self):
        return self.title
