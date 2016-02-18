from django.contrib import admin
from django.contrib.auth.models import User
from core.models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['author', 'date',]
    #exclude = ['author', 'date',]
    fieldsets = [
        (None, {'fields': ['title', 'body']}),
        ('Details', {'fields': ['category', 'author', 'date', 'feature'], 
                     'classes': ['collapse']}),
    ]
    list_display = ('title', 'date', 'feature',)
    list_filter = ('date',)
    search_fields = ['title', 'body',]
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = User.objects.get(id = request.user.id)
        obj.save()


admin.site.register(Post, PostAdmin)