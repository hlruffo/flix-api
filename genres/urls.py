from django.urls import path
from .views import GenreCreateListView, GenreRetrieveUpdateDestroyView

urlpatterns = [
    #path('', genre_create_list_view, name='genre-create-list'),
    #path('<int:pk>/', genre_detail_view, name='genre-detail-update-delete'),
    path('genres/',GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-update-delete'),
    
]
