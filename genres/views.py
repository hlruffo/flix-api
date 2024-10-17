from .models import Genre
from .serializers import GenreSerializer
from rest_framework import generics


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Create your views here.
# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
    
#     elif request.method == 'POST':        
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, 
#                             status=201) 

# @csrf_exempt
# def genre_detail_view(request, pk):
#     genre = get_object_or_404(Genre, pk=pk)
    
#     if request.method == 'GET':
#         return JsonResponse({'id': genre.id, 'name': genre.name}, status=200)
    
#     elif request.method == 'PUT':
#         data = json.loads(request.body.decode('utf-8'))
#         genre.name = data['name']
#         genre.save()
#         return JsonResponse({'id': genre.id, 'name': genre.name})
#     else:
#         genre.delete();       
#         return JsonResponse({'message': 'Genre deleted'}, status=204)
    
