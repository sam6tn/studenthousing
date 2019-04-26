from django.contrib import admin

from .models import Post, Review, Profile, Image
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields



class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['info']}),
        (None, {'fields': ['rooms']}),
        (None, {'fields': ['baths']}),
        (None, {'fields': ['address']}),
        (None, {'fields': ['price']}),
        # (None, {'fields': ['rating']}),
        (None, {'fields': ['image_url']}),
        (None, {'fields': ['baths']}),
        (None, {'fields': ['rooms']}),
        (None, {'fields': ['available']}),
        # (None, {'fields': ['google_address']}),
        # (None, {'fields': ['geolocation']}),

        
    ]

    # formfield_overrides = {
    #     map_fields.AddressField: {
    #       'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    # }

    list_display = ('name', 'info', 'address', 'price', 'image_url', 'available')

    list_filter = ['name']

    search_fields = ['name']

    inlines = [ReviewInline,ImageInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
