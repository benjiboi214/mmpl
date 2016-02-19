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
    author = models.ForeignKey(User, verbose_name='Author')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    category = models.CharField(max_length=2,
    							choices=CATEGORY_CHOICES,
    							default='NE',
    							verbose_name='Category')
    title = models.CharField(max_length=128, verbose_name='Title')
    body = models.TextField(verbose_name='Content')
    feature = models.BooleanField(default=True, verbose_name='Featured')
    large = models.BooleanField(default=True, verbose_name='Large Post')
    #image = 
    #files = 
        
    def __unicode__(self):
        return self.title
