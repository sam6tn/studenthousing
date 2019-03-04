from django.contrib import admin
#change
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['info']}),
        (None, {'fields': ['rating']}),
    ]
    list_display = ('name', 'info', 'rating')

    list_filter = ['rating']

    search_fields = ['name']
"""

class PostInline(admin.TabularInline):
    model = Post


class LocationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['location_name']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['owner']}),
        (None, {'fields': ['rooms']}),
        (None, {'fields': ['bathrooms']}),

    ]
    inlines = [PostInline]

    list_display = ('location_name', 'address', 'owner')

    search_fields = ['location_name']

admin.site.register(Location, LocationAdmin)
"""
admin.site.register(Post, PostAdmin)
