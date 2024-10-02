from django.urls import path

from .views import index,home_page


urlpatterns = [
    path('', index, name='index'),
    path('home',home_page, name='home')
]