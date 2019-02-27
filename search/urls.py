from django.urls import path
from django.http import HttpResponse

from . import views


app_name = 'housing'
urlpatterns = [

    path('search/', views.SuggestView.as_view(), name='home'),
    path('search/results/', views.ListView.as_view(), name='list'),
    ]