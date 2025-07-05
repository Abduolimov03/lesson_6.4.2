from django.urls import path
from .views import *

urlpatterns = [
    # path('watch/', watch_list, name='watch'),
    path('watch/', WatchList.as_view(), name='watch'),
    # path('watch/<int:pk>/', watch_detail, name='watch-detail'),
    path('watch/<int:pk>/', WatchDetail.as_view(), name='watch-detail'),

    path('create/', WatchCreate.as_view(), name='create-watch'),
    path('update/<int:pk>', WatchUpdate.as_view(), name='update-watch'),
    path('del/<int:pk>', WatchDelete.as_view(), name='del-watch')
]