from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.forms import UserChangeForm

app_name = 'housing'
urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^housingsearch/$', views.ListView.as_view(), name='housingsearch'),
    url(r'^housingsearch/$', views.available_filter, name='available'),
    url(r'^housingsearch/$', views.price_filter, name='price'),
    #    url(r'^housingsearch/$', views.ListView.as_view(), name='distance'),
    url(r'^housingsearch/(?P<post_name>.+)/$', views.PostView.as_view(), name='post'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)