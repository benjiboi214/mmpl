from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post

def index(request):
    large = Post.objects.filter(post_type='LG', hidden=False)
    small = Post.objects.filter(post_type='SM', hidden=False)
    
    large_posts = large.order_by('-date')
    small_posts = small.order_by('-date')
    
    context_dict = {'large_posts': large_posts, 
    				'small_posts': small_posts,}
    
    response = render(request, 'core/feed.html', context_dict)
    
    return response

def post(request, post_name_slug):
    
    context_dict = {}
    
    try:
        post = Post.objects.get(slug=post_name_slug)
        context_dict['post'] = post
    except Post.DoesNotExist:
        pass
    
    response = render(request, 'core/post.html', context_dict)
    
    return response
