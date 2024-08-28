# Create your views here.
# api/views.py

import rest_framework
import djangorestframework

print(rest_framework.__version__)

import sys
print(sys.path)

from django.shortcuts import render
from rest_framework import generics
from .models import Song
from .serializers import SongSerializer

class SongListCreateView(generics.ListCreateAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

