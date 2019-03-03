from django.conf.urls import url

from . import views


app_name = 'housing'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^search/$', views.SuggestView.as_view(), name='home'),
    url(r'^search/results/$', views.ListView.as_view(), name='list'),
]