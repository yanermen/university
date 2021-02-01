from django.urls import path
from .views import UniversityCreateAPIView, SubjectCreateAPIView, DetailUniversityWithSubjectsAPIView, ListOfUniversityAPIView, ListOfSubjectsAPIView, DeleteUniversityAPIView

urlpatterns = [
    path('university/', UniversityCreateAPIView.as_view(), name='add_university'),
    path('subject/', SubjectCreateAPIView.as_view(), name='add_subject'),
    path('university/<int:pk>/', DetailUniversityWithSubjectsAPIView.as_view(), name='detail_university'),
    path('universities/', ListOfUniversityAPIView.as_view(), name='list_of_universities'),
    path('subjects/', ListOfSubjectsAPIView.as_view(), name='list_of_subjects'),
    path('delete-university/<int:pk>/', DeleteUniversityAPIView.as_view(), name='delete_university'),
]