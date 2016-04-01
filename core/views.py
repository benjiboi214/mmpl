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

category_dict = {'NE': 'News',
       			 'EV': 'Events',
       			 'RU': 'Results',
       			 'RO': 'Resources',
       			 'FE': 'Feed'}

def get_topic(request, category=False):
    if category:
        large = Post.objects.filter(post_type='LG', hidden=False, category=category).order_by('-date')
    else:
        large = Post.objects.filter(post_type='LG', hidden=False).order_by('-date')
        category = 'FE'
    small = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
    
    context_dict = {'large_posts': large,
    				'small_posts': small,
    				'actual_category': category_dict[category],}
    
    response = render(request, 'core/feed.html', context_dict)
    return response

def index(request):
    return get_topic(request)

def news(request):
    return get_topic(request, 'NE')
    
def events(request):
	return get_topic(request, 'EV')

def results(request):
    return get_topic(request, 'RU')

def resources(request):
    return get_topic(request, 'RO')
    
def post(request, post_id, post_slug):
    
    context_dict = {}
    try:
        post = Post.objects.filter(id=post_id, slug=post_slug)
        context_dict['post'] = post[0]
    except IndexError: #to account for the Post filter not finding anything and the 
        pass
    
    context_dict['actual_category'] = category_dict[post[0].category]
    
    response = render(request, 'core/post.html', context_dict)
    return response

def get_contact_form(request, form_class, title):
    
    context_dict = {}

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
    context_dict['title'] = title
        
    response = render(request, 'core/contact.html', context_dict)
    return response

def contact(request):
    return get_contact_form(request, ContactForm, 'Contact Us')

def join(request):
    return get_contact_form(request, JoinForm, 'Join Us')

#class FeedView(TemplateView):
#    template_name = 'core/feed.html'
#    
#    def get_context_data(self, **kwargs):
#        context = super(FeedView, self).get_context_data(**kwargs)
#        context['large_posts'] = Post.objects.filter(post_type='LG', hidden=False).order_by('-date')
#        context['small_posts'] = Post.objects.filter(post_type='SM', hidden=False).order_by('-date')
#        context['actual_category'] = 'Feed'
#        return context

