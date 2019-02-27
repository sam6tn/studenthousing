from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView


app_name = 'home'
urlpatterns = [
    url('home/', views.home),
    url(r'^login/$', LoginView, {'template_name': 'home/login.html'})
]