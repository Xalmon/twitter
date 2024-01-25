from django.contrib import admin
from .models import Tweet, Comments


# Register your models here.


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['text', 'last_update']
    list_per_page = 10
    search_fields = ['text']
    list_display_links = ['text']


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'commented_on', 'id']
    list_per_page = 10
    search_fields = ['comment']
    list_display_links = ['comment']
