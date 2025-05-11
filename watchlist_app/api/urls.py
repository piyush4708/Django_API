from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import StreamPlatforAv,WatchDetailsAP,WatchListAV
urlpatterns = [
    
    path('Stream_Platform_list/', StreamPlatforAv.as_view(), name='Stream_platform'),
    # path('<int:pk>', StreamPlatforAv.as_view(), name='Stream_Platform_details'),
    path('list/',WatchListAV.as_view(), name='Watch_list'),
    path('<int:pk>', WatchDetailsAP.as_view(), name='WatchDetails_'),
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    
]