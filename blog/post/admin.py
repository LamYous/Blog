from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmine(admin.ModelAdmin):
    list_display = ('title', 'created_at',)
    
admin.site.register(Post, PostAdmine)

admin.site.register(Comment)