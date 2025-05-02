# from django.shortcuts import render
# from watchlist_app.models import Movies
# from django.http import JsonResponse
# # Create your views here.

# def movie_list(request):
#     movies =Movies.objects.all()
#     # print(movies.values())
#     data = {
#         'movies': list(movies.values())
#     }
    
#     return JsonResponse(data)
    
    
# def movie_details(request,pk):
#     movie = Movies.objects.get(pk=pk)
#     # print(movie.name)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active
#     }
    
#     return JsonResponse(data)


