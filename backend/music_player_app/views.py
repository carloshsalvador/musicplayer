# Create your views here.
# music_player_app/views.py

from django.shortcuts import render, redirect, get_object_or_404  # Added get_object_or_404 for update view
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm, LoginForm
from api.models import Song  # import class from api.model! if only .models, the import will be from the same folder (music_player_app.models)
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('index')  # Redirect to the home page after registration
        else:
            return render(request, 'music_player_app/register.html', {'form': form})  # Render the registration form with errors
    else:
        form = RegistrationForm()
        return render(request, 'music_player_app/register.html', {'form': form})  # Render the empty registration form

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
        song = Song(title=title, artist=artist, categorie=categorie, user=request.user) # 'user' here was implmented later to ensure that each user has different/personalised access to the same data bank
        song.save()
        return redirect('/')
    return render(request, 'music_player_app/AddSong.html') # Render AddSong.html template

# Update song view
@login_required
def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id, user=request.user) # 'user' here was implmented later to ensure that each user has different/personalised access to the same data bank
    if request.method == 'POST':
        song.title = request.POST['title']
        song.artist = request.POST['artist']
        song.categorie = request.POST['categorie']
        song.save()
        return redirect('/')
    return render(request, 'music_player_app/UpdateSong.html', {'song': song}) # Render UpdateSong.html template with song context

# Render index.html template
@login_required
def index(request):
    songs = Song.objects.filter(user=request.user)  # at data bank, filter songs by the logged-in user
    return render(request, 'music_player_app/index.html', {'songs': songs})