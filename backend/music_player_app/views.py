# Create your views here.
# music_player_app/views.py

from django.shortcuts import render, redirect, get_object_or_404  # Added get_object_or_404 for update view
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm
from api.models import Song  # import class from api.model! if only .models, the import will be from the same folder (music_player_app.models)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# Add song view
@login_required
def add_song(request):
    if request.method == 'POST':
        title = request.POST['title']
        artist = request.POST['artist']
        categorie = request.POST['categorie']
        song = Song(title=title, artist=artist, categorie=categorie)
        song.save()
        return redirect('/')
    return render(request, 'music_player_app/AddSong.html') # Render AddSong.html template

# Update song view
@login_required
def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.title = request.POST['title']
        song.artist = request.POST['artist']
        song.categorie = request.POST['categorie']
        song.save()
        return redirect('/')
    return render(request, 'music_player_app/UpdateSong.html', {'song': song}) # Render UpdateSong.html template with song context

# Render index.html template
def index(request):
    return render(request, 'music_player_app/index.html')