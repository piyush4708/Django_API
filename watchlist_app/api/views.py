from rest_framework import status
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList,StreamingPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer


class StreamPlatforAV(APIView):
    def get(self,request):
        platform =  StreamingPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform,many=True,context={'request': request})
        return Response(serializer.data)
    def post(self,request):
        serializer = StreamPlatformSerializer(data = request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
class StreamPlatformDetailAV(APIView):
    def get(self,request,pk):
        try:
            platform = StreamingPlatform.objects.get(pk =pk)
        except platform.DoesNotExist:
            return Response({"error":"Platform not Found"}, status= status.HTTP_400_BAD_REQUEST)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    def put(self,request,pk):
        platform = StreamingPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform,data = request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
    def delete(self,response,pk):
        platform = StreamingPlatform.objects.get(pk =pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchDetailsAV(APIView):
    def get(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"error": 'Movie Not Found'}, status= status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
        # movie =  Movie.objects.get(pk=pk)
        # serializer = MovieSerializer(movie.data)
        
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
        
    def delete(self,response,pk):
        movie = WatchList.objects.get(pk =pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie,many= True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"error": 'Movie Not Found'}, status= status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie,data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
        
#         return Response(serializer.errors)
    
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         # serializer = MovieSerializer(movie, data =request.data)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
        
