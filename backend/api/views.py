# Create your views here.
# api/views.py
# The SongListCreateView and SongDetailView classes are using the Django REST Framework's generic views (generics.ListCreateAPIView and generics.RetrieveUpdateDestroyAPIView), which are suitable for basic CRUD operations.
# The AddSongFromSpotifyView class is a custom view that uses the APIView class from the Django REST Framework. This view handles the logic for adding songs from Spotify search results.

from django.shortcuts import render
from rest_framework import generics
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .spotify import search_spotify

class SongListCreateView(generics.ListCreateAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class AddSongFromSpotifyView(APIView):
    def post(self, request):
        query = request.data.get('query')
        if query:
            results = search_spotify(query)
            if results and results['tracks']['items']:
                for item in results['tracks']['items']:
                    song = Song(
                        title=item['name'],
                        artist=item['artists'][0]['name'],
                        album=item['album']['name'],                    # Ensure this field is available, when calling the funktion searchSpotify() at index.htm
                        duration=item['duration_ms'] // 1000,           # Convert duration from milliseconds to seconds [the same as above regards to the searchSpotify() function]
                        spotify_id=item['id'],                          # Ensure this field is available [the same as above regards to the searchSpotify() function]
                        audio_file=item['preview_url'],                 # Ensure this field is available [the same as above regards to the searchSpotify() function]
                        audio_img=item['album']['images'][0]['url']     # Ensure this field is available [the same as above regards to the searchSpotify() function]
                    )
                    song.save()
                return Response({"message": "Songs added successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)