from django.contrib import admin

from .models import Post, Review, Profile

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['info']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['price']}),
        (None, {'fields': ['rating']}),
        (None, {'fields': ['image_url']}),
        (None, {'fields': ['available']}),
    ]
    list_display = ('name', 'info', 'address', 'price', 'rating', 'image_url', 'available')

    list_filter = ['name']

    search_fields = ['name']

    inlines = [ReviewInline]


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

admin.site.register(Profile)
