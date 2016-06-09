from django import template
from core.models import Post

register = template.Library()

@register.inclusion_tag('core/jumbotron.html')
def get_jumbotron():

    jumbotron = Post.objects.filter(post_type='FE').order_by('-date')[:1]

    return {'jumbotron': jumbotron}
