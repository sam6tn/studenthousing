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
        (None, {'fields': ['baths']}),
        (None, {'fields': ['rooms']}),
        (None, {'fields': ['available']}),
    ]
    list_display = ('name', 'info', 'address', 'price', 'rating', 'image_url', 'baths', 'rooms', 'available',)

    list_filter = ['name']

    search_fields = ['name']

    inlines = [ReviewInline]

admin.site.register(Post, PostAdmin)

admin.site.register(Profile)
