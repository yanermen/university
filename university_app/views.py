from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView

from .serializers import UniversitySerializer, SubjectSerializer
from .models import Subject, University


class UniversityCreateAPIView(CreateAPIView):
    """
    Create university with fields name and address
    """
    serializer_class = UniversitySerializer


class SubjectCreateAPIView(CreateAPIView):
    """
    Create subjects for universities
    """
    serializer_class = SubjectSerializer


class DetailUniversityWithSubjectsAPIView(ListAPIView):
    """
    Get list of university with thier subjects
    """
    # serializer_class = UniversitySerializer
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all().filter(university=self.kwargs['pk'])


class ListOfUniversityAPIView(ListAPIView):
    """
    List of all universities which registered
    """
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class ListOfSubjectsAPIView(ListAPIView):
    """
    List of subjects
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DeleteUniversityAPIView(DestroyAPIView):
    """
    Delete special university
    """
    serializer_class = UniversitySerializer

    def get_queryset(self):
        return University.objects.filter(id=self.kwargs['pk'])