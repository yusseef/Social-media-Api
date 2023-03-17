from django.contrib import admin
from .models import *
# Register your models here.

class ImagesAdmin(admin.TabularInline):
    model = Photo
    extra = 3

class LikesAdmin(admin.TabularInline):
    model = Like

class CommentAdmin(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'content']
    inlines = [LikesAdmin, CommentAdmin, ImagesAdmin]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Photo)
