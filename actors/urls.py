from django.urls import path
from .views import ActorCreateListView, ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('',ActorCreateListView.as_view(), name='actor-create-list'),
    path('<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-update-delete'),
    
]