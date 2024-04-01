from django.urls import path, include
from . import views
from .models import Url
urlpatterns = [
    path('',views.index,name='index'),
    path('<str:short_url>',views.detail,name='detail')
]