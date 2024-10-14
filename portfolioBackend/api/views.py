from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render

from .models import Project, Experience
from .serializers import ProjectSerializer, ExperienceSerializer


@api_view(['GET'])
def home(request):
    return Response('Vid Pesko')


# Get all projects
class ProjectList(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        search_param = self.request.query_params.get("highlighted", None)

        if search_param:
            # Example filtering (adjust as per your model fields)
            queryset = queryset.filter(highlighted=True)

        return queryset


class ExperienceList(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer