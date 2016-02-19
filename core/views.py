from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post

def index(request):
    posts = Post.objects.order_by()[:5]
    
    context_dict = {'posts': posts}
    
    response = render(request, 'core/feed.html', context_dict)
    
    return response

# Create your views here.
