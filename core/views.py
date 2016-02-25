from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post

def index(request):
    large = Post.objects.filter(post_type='LG', hidden=False).order_by('-date')
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')

    context_dict = {'large_posts': large, 
    				'small_posts': small,}
    
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

def news(request):
    large = Post.objects.filter(post_type='LG', hidden=False, category='NE').order_by('-date')
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
    
    context_dict = {'large_posts': large,
    				'small_posts': small,
    				'actual_category': 'News',}
    
    response = render(request, 'core/feed.html', context_dict)
    return response

def events(request):
    large = Post.objects.filter(post_type='LG', hidden=False, category='EV').order_by('-date')
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
    
    context_dict = {'large_posts': large,
    				'small_posts': small,
    				'actual_category': 'Events',}
    
    response = render(request, 'core/feed.html', context_dict)
    return response

def results(request):
    large = Post.objects.filter(post_type='LG', hidden=False, category='RU').order_by('-date')
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
    
    context_dict = {'large_posts': large,
    				'small_posts': small,
    				'actual_category': 'Results',}
    
    response = render(request, 'core/feed.html', context_dict)
    return response

def resources(request):
    large = Post.objects.filter(post_type='LG', hidden=False, category='RO').order_by('-date')
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
    
    context_dict = {'large_posts': large,
    				'small_posts': small,
    				'actual_category': 'Resources',}
    
    response = render(request, 'core/feed.html', context_dict)
    return response
