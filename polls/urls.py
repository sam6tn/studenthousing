from django.urls import path
from django.http import HttpResponse

from . import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('suggestions/', views.SuggestView.as_view(), name='home'),
    path('suggestions/list', views.ListView.as_view(), name='list'),
]