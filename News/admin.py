from django.contrib import admin
from .models import Author, Post, Category
from modeltranslation.admin import TranslationAdmin

admin.site.register(Author)
admin.site.register(Post)


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'news_type',
                    'time_in', 'category', 'heading')
    list_filter = ('category', 'author')


class CategoryAdmin(TranslationAdmin):
    model = Category


admin.site.register(Category)
