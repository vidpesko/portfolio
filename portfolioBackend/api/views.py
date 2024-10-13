from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render


@api_view(['GET'])
def home(request):
    return Response('Vid Pesko')


# Get all projects

# Get highlighted projects
