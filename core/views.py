from django.shortcuts import render
from django.http import HttpResponse
from core.models import Post
from core.forms import ContactForm, JoinForm
from django.shortcuts import redirect
#class based view imports
from django.views.generic import TemplateView
#ContactForm email imports
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages


def index(request):
    large = Post.objects.filter(post_type='LG', hidden=False).order_by('-date')
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')

    context_dict = {'large_posts': large, 
    				'small_posts': small,
    				'actual_category': 'Feed'}
    
    response = render(request, 'core/feed.html', context_dict)
    return response

def post(request, post_id, post_slug):
    
    context_dict = {}
    
    try:
        post = Post.objects.filter(id=post_id, slug=post_slug)
        context_dict['post'] = post[0]
    except IndexError: #to account for the Post filter not finding anything and the 
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

#Un hash after template, url and form are complete
def contact(request, form_context):
    context_dict = {}
    if form_context == 'join':
        form_class = JoinForm
        context_dict['title'] = 'Join Us'
    else:
        form_class = ContactForm
        context_dict['title'] = 'Contact Us'
    
    if request.method == 'POST':
        form = form_class(data=request.POST)
        
        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name',
                '')
            contact_email = request.POST.get(
                'contact_email',
                '')
            form_content = request.POST.get('content', '')
            
            #Email the profile with the contact info
            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, 'Email Sent')
            
            return render(request, 'core/contact.html')
    
    context_dict['form'] = form_class
        
    response = render(request, 'core/contact.html', context_dict)
    return response

#class FeedView(TemplateView):
#    template_name = 'core/feed.html'
#    
#    def get_context_data(self, **kwargs):
#        context = super(FeedView, self).get_context_data(**kwargs)
#        context['large_posts'] = Post.objects.filter(post_type='LG', hidden=False).order_by('-date')
#        context['small_posts'] = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
#        context['actual_category'] = 'Feed'
#        return context

