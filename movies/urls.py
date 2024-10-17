from django.urls import path
from .views import MovieListView, MovieRetrieveUpdateDestroyView


urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list-create'),
    path('<int:pk>/', 
         MovieRetrieveUpdateDestroyView.as_view(), 
         name='movie-detail-update-delete'),
]