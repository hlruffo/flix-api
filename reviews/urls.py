from django.urls import path
from .views import ReviewListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('reviews/', ReviewListView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-update-delete'),
    ]