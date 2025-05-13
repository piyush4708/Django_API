from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import StreamPlatforAV,WatchDetailsAV,WatchListAV,StreamPlatformDetailAV
urlpatterns = [
    
    path('stream/', StreamPlatforAV.as_view(), name='stream-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='Stream-detail'),
    path('list/',WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='movie-Detail'),
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    
]