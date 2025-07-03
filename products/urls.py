from django.urls import path
from .views import *

urlpatterns = [
    path('watch/', watch_list, name='watch'),
    path('watch/<int:pk>/', watch_detail, name='watch-detail'),
    path('create/', create_watch, name='create-watch')

]