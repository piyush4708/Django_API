from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import MoviesDetailsAP,MovieAP
urlpatterns = [
    
    path('list/', MovieAP.as_view(), name='movie_list'),
    path('<int:pk>', MoviesDetailsAP.as_view(), name='movie_details'),
    # path('list/', movie_list, name='movie_list'),
    # path('<int:pk>', movie_details, name='movie_details'),
    
]