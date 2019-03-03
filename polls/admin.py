from django.contrib import admin
#change
from .models import Question, Choice, Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['info']}),
        (None, {'fields': ['rating']}),
    ]
    list_display = ('name', 'info', 'rating')

    list_filter = ['rating']

    search_fields = ['name']

admin.site.register(Post, PostAdmin)

