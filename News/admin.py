from django.contrib import admin
from .models import Author, Post
# Register your models here.

admin.site.register(Author)
admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'news_type', 'time_in', 'category', 'heading')
    list_filter = ('category', 'author')