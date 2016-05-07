from django.contrib import admin
from django.contrib.auth.models import User
from core.models import Post, Image, File
from django.core.urlresolvers import reverse


class ImageInline(admin.TabularInline):
    readonly_fields = [
        'image_admin'
    ]
    fieldsets = [
        (None, {'fields': ['image_admin', 'title', 'description', 'image']})
    ]
    model = Image
    extra = 1


class FileInline(admin.TabularInline):
    model = File
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline, FileInline
    ]
    readonly_fields = ['author',
                       'date',
                       ]
    fieldsets = [
        (None, {'fields': ['title', 'subtitle', 'body']}),
        # ('Media', {'fields': ['Image', 'File'], 'classes': ['collapse']}),
        ('Details', {'fields': ['category', 'author', 'date'], 'classes': ['collapse']}),
        ('Location', {'fields': ['post_type', 'hidden'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'date', 'post_type', 'hidden')
    list_filter = ('date', 'post_type', 'hidden')
    search_fields = ['title', 'body', ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = User.objects.get(id=request.user.id)
        obj.save()

    def view_on_site(self, obj):
        return 'http://127.0.0.1:8000' + reverse('post',
                                                 kwargs={'post_slug': obj.slug,
                                                         'post_id': obj.id})
