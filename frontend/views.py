from django.shortcuts import render
from frontend.models import Project
from frontend.serializers import ProjectSerializer
from rest_framework import generics

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
