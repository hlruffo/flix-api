from django.urls import path
from .views import ReviewListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list-create'),
    path('<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-update-delete'),
    ]