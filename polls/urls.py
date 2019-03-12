from django.conf.urls import url

from . import views

app_name = 'housing'
urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^search/$', views.SearchView.as_view(), name='home'),
    url(r'^search/results/$', views.ListView.as_view(), name='list'),
]