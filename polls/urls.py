from django.conf.urls import url

from . import views

app_name = 'housing'
urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^housingsearch/$', views.ListView.as_view(), name='housingsearch'),
    url(r'^housingsearch/(?P<post_id>\d+)/$', views.PostView.as_view(), name='post'),
]