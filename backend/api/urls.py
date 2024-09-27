# api/urls.py
from django.urls import path
from .views import SongListCreateView, SongDetailView, AddSongFromSpotifyView 


urlpatterns = [
	path('songs/', SongListCreateView.as_view(), name='song-list-create'), # '/' can avoid conflicts with other URLs, the same for all other URLs, here and other files (e.g., music_player_app/urls.py)
	path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
    path('add-song-from-spotify/', AddSongFromSpotifyView.as_view(), name='add-song-from-spotify'),
]
