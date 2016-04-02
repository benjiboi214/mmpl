from django.contrib import admin
from django.contrib.auth.models import User
from core.models import Post
from django.core.urlresolvers import reverse

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'date',]
    #exclude = ['author', 'date',]
    fieldsets = [
        (None, {'fields': ['title', 'subtitle', 'body']}),
        ('Media', {'fields': ['image', 'file'],
        			'classes': ['collapse']}),
        ('Details', {'fields': ['category', 'author', 'date'], 
                     'classes': ['collapse']}),
        ('Location', {'fields': ['post_type', 'hidden'],
        			  'classes': ['collapse']}),
    ]
    list_display = ('title', 'date', 'post_type', 'hidden')
    list_filter = ('date', 'post_type', 'hidden')
    search_fields = ['title', 'body',]
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = User.objects.get(id = request.user.id)
        obj.save()
    
    def view_on_site(self, obj):
        return 'http://127.0.0.1:8000' + reverse('post',
        										 kwargs={'post_slug': obj.slug,
        										 		 'post_id': obj.id})


admin.site.register(Post, PostAdmin)