from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = (
        ('NE', 'News'),
        ('EV', 'Events'),
        ('RU', 'Results'),
        ('RO', 'Resources'),
    )
    POST_TYPE_CHOICES = (
        ('LG', 'Large'),
        ('SM', 'Small'),
        ('FE', 'Feature')
    )
    
    #Detail fields
    author = models.ForeignKey(User, verbose_name='Author')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    category = models.CharField(max_length=2,
    							choices=CATEGORY_CHOICES,
    							default='NE',
    							verbose_name='Category')
    
    #Content fields
    title = models.CharField(max_length=128, verbose_name='Title')
    body = models.TextField(verbose_name='Content')
    #image = 
    #files = 
    
    #Location detail fields
    post_type = models.CharField(max_length=2,
    							 choices=POST_TYPE_CHOICES,
    							 default='LG',
    							 verbose_name='Post Type')
    hidden = models.BooleanField(default=False, verbose_name='Hidden')
        
    def __unicode__(self):
        return self.title
