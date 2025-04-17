from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.SearchJsonView.as_view(), name='search_json'),
]