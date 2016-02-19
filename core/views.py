from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post

def index(request):
    large = Post.objects.filter(large=True, feature=False)
    small = Post.objects.filter(large=False, feature=False)
    
    large_posts = large.order_by('-date')
    small_posts = small.order_by('-date')
    
    context_dict = {'large_posts': large_posts, 'small_posts': small_posts}
    
    response = render(request, 'core/feed.html', context_dict)
    
    return response

# Create your views here.
