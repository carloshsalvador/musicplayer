# MUSIC PLAYER APP (part II)

The file README.md is the part I to develop a web application of music player. The readers can there find the context, dependencies, architecture and infrasctructure and how the app was planed.

Here on the other hand is the part II for the specific description of programation's steps with some explanation about the step itself, but not the context.

In this documment is also possible to see the frist version of scripts, especially the .html to start the project. Thus, their are more simple than the cloned version, because they were modified during the development of the project and fixing problems.

# STEPS AS CONTENT

This app was developed basically with 8 steps. 

The steps are the primery keys to organize this document. 

Terefore, the general steps below works as an overview and the content of this document.

## GENERAL STEPS:

1. **Version Control with GitHub**:
	- version control and collaboration.
	- setting gitignore, specially file .env. with environments variables such as keys etc.
2. **File organisation and security**
	- basically: fodlers, files, Python's virtual environment and environmental variables.
	- libraries installed at virutal environments.
	- file .env to procted environmental variables.
3. **Backend with Django and PostgreSQL**
	- start django project and Django REST Framework for creating RESTful APIs.
	- Django's settings.py with DATABASE for PostgresSQL.
4. **Creating Docker's image and volumes for Django and PostgreSQL**:
	- Dockerfile to define the Django image.
	- file .dockerignore to protect env. variables.
5. **Containers Orchestration with Docker Compose**:
	- file `docker-compose.yml` to manage all containers separately: Django and Data Bank (PosterSQL)
6. **Hosting on Back4App**:
	- Deploy backend and database services on Back4App linked to GitHub for systematically deplyments.
7. **Frontend with Tailwind CSS**:
	- developement of user interface. [not implemented yet]
8. **Frontend Development with Vue.js**:
	- more development of the user interface and use of CSS from Tailwind. [not implemented yet]

## DJANGO PROJECT: START

Following [Djang's recomendation](https://docs.djangoproject.com/en/5.1/intro/tutorial01/), it is important to avoid naming projects after built-in Python or Django components. In particular, this means names like django (which will conflict with Django itself) or test (which conflicts with a built-in Python package). 

So, start the project with proper [name](https://docs.djangoproject.com/en/5.1/intro/tutorial01/#creating-a-project), such as **backend**, on the terminal at root **musicplayer/**:

```django-admin startproject backend```

Some files are created automatically. Now, the project's folder has new file struture and organisation:

```
musicplayer/
	backend/
		manage.py
		mysite/
			__init__.py
			settings.py
			urls.py
			asgi.py
			wsgi.py
```

The inner backend/ directory is the Python package for the project. Its name is the Python package name to use to import anything inside it (*e.g.*, mysite.urls).

The files descriptions and their useful tools:

- **manage.py**

	This script configures the Django environment by setting the environment variable DJANGO_SETTINGS_MODULE. In this case, the line os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings') specifies that Django should use the settings module located in backend/settings.py.

	The manage.py script imports the execute_from_command_line function from the django.core.management module, which is the main command that Django uses to execute any of its subcommands (such as runserver, migrate, makemigrations, createsuperuser, among others). When running a shell command like ```python manage.py runserver```, Django uses this manage.py script to configure the appropriate environment and then calls the function execute_from_command_line(sys.argv). This command processes the command-line arguments (sys.argv) and performs the corresponding task.
	Some of the most commonly used commands with manage.py include:
	1. ```python manage.py runserver``` # Starts Django’s development server.
	2. ```python manage.py makemigrations``` # Creates new migrations based on the changes made to Django models.
	3. ```python manage.py migrate``` # Applies all pending database migrations.
	4. ```python manage.py createsuperuser``` # Creates a [superuser](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#module-django.contrib.admin) for accessing the admin panel.
	5. ```python manage.py startapp <app_name>``` # Creates a new Django application within the project.

- **mysite/__init__.py**

	An empty file that tells Python that this directory should be considered a Python package.

- **mysite/settings.py**

	Settings/configuration for this Django project. Django settings will tell you all about how settings work.

- **mysite/urls.py**

	The URL declarations for this Django project; a “table of contents” of your Django-powered site.

- **mysite/asgi.py** and **mysite/wsgi.py**
	
	An entry-point for ASGI-compatible web servers to serve your project.
	
The **settings.py** was created in this step and need modification. However, set the modifaction only after creating the app (step below), to avoid extra works afterwards (*e.g.,* change names of folders). This step of modification you find below on the best sequence ((Remember, it works as recipt and the sequence matter... like cooking :-)).

Now the environment – a “project” – is set up and we can are set to start doing work.

Don't forget to commit it! Remember the first 12 Factors?!... see README.md again. I help you:

**useful**: git commit -m"starting django project with 'django-admin startproject backend'. This add . 6 new files: 1 on the root of new backend folder and 5 inside the new backend subfolder with the same name"

### APPs

This are the steps about the [app](https://docs.djangoproject.com/en/5.1/intro/tutorial01/#creating-the-polls-app) itself.

Each application in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so we can focus on writing code rather than creating directories.

So, at the terminal, at project root, the next commands are:
1. ```cd backend```
2. ```python manage.py startapp api```
3. ```python manage.py startapp music_player_app```

**useful**: git commit -m"2 apps created with 'python manage.py start app ...' (api and music_player). this stepe create tow folder with 8 files each, total of 16 new files"

#### project's scripts

##### project/project/settings.py

Based on the names of new app's directories, add and update the variables on settings.py:

INSTALLED_APPS = [ 
    "django.contrib.admin", 
    "django.contrib.auth", 
    "django.contrib.contenttypes", 
    "django.contrib.sessions", 
    "django.contrib.messages", 
    "django.contrib.staticfiles", 
    "music_player_app", 
    "api", 
    "rest_framework" 
]

**useful**: git commit -m "setting  the file backend/settings.py with INSTALLED_APPS=[..,music_player, api, rest_framework] variable."


#### apps' script modification

This step basically sets the Classes and Models on .py files used for each app. It is a cascate of settings: it starts with **models.py** implementation for each apps' Classes and Models and then implement them afterwards on different files.

##### models.py

###### APP: api
```
# api/models.py
from django.db import models

class Song(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=100)
	categorie = models.CharField(max_length=100, null=True, default=None)
	artist = models.CharField(max_length=100)
	audio_file = models.FileField(upload_to='audio/')
	audio_img = models.FileField(upload_to='audio_img/')

	def __str__(self):
		return self.title
```

**useful**: git commit -m "setting api/models.py with code to define a Django model named 'Song'(a Python's class) with fields for id, title, category, artist,rning the song title."

###### APP: music_player_app

```
# music_player_app/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
	groups = models.ManyToManyField(
		'auth.Group',
		related_name='customuser_set',
		related_query_name='user'
	)
	user_permissions = models.ManyToManyField(
		'auth.Permission',
		related_name='customuser_set',
		related_query_name='user'
	)

```

**useful**: git commit -m "similar to commit before, but settings to music_player_app/models.py :code defines a custom Django user model named 'CustomUser' that extends the AbstractUser model, adding fields for groups and user permissions, allowing users to be associated with multiple groups and permissions"

##### project/app/views.py

**useful**: git commit -m "settings api/views.py requires also new library djangorestframework (modulo rest_framework used on this script). requirements.txt was thus also updated"


**useful**: git commit -m "setting views.py for music_player_app. For testing I did also python manage.py migrate and python mandage runserver; this create more files automaticlly such as the subfoler api/__pycach__ and api/migrations as well as in music_player_app."

obs: Be aware that music_player_app/views.py uses folder name music_player_app.... if it is not right name, change it!

#### api/serializers.py

api/serializers.py has the code to define a Django Rest Framework serializer, “SongSerializer,” using the model “Song” and including all fields for serialization. 

This file doesn't exist yet. It has been not automatically created as the other with 'startapp'. Thus, the file need to be created on the folder api and fill it up with the following code:
```
from rest_framework import serializers
from .models import Song
 
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
```


**useful**: git commit -m "create and set a new file for api/serializers.py with code to define a Django Rest Framework serializer, 'SongSerializer', using the model 'Song' and including all fields for serialization. This information was also updated on Readme."

##### music_player_app/forms.py

music_palyer_app/forms.py : below code defines a registration form (“RegistrationForm”) and a login form (“LoginForm”) for a custom user model, extending default Django forms for user creation and authentication.

```
# music_player_app/forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
	class Meta:
		model = CustomUser
		fields = ['username', 'password']
```


**useful**: git commit -m "create and set a new file for music_palyer_app/forms.py with code to define a registration form ('RegistrationForm') and a login form ('LoginForm') for a custom user model, extending default Django forms for user creation and authentication.This information was also updated on Readme."

#### urls.py

The urls.py files in both the api and music_player_app directories are used to define specific URL patterns for each app. The api/urls.py manages routes related to the Song model for CRUD operations, while music_player_app/urls.py handles user authentication routes and core app functionalities like home, adding, and updating songs. Having these separated allows for modular and organized code, making the project easier to maintain and extend. For this reason, each project has specific routes and urls.py are automatically created neither with startproject nor startapp, in contrast to other scripts. 

##### api/urls.py

api/urls.py : below code sets up Django URL patterns for song listing/creation and song detail using “SongListCreateView” and “SongDetailView” views, respectively.

The SongListCreateView and SongDetailView classes are using the Django REST Framework's generic views (generics.ListCreateAPIView and generics.RetrieveUpdateDestroyAPIView), which are suitable for basic CRUD operations.

##### api/urls.py

api/urls.py : below code sets up Django URL patterns for song listing/creation, song detail, and adding songs from Spotify using “SongListCreateView”, “SongDetailView”, and “AddSongFromSpotifyView” views, respectively.

The SongListCreateView and SongDetailView classes are using the Django REST Framework's generic views (generics.ListCreateAPIView and generics.RetrieveUpdateDestroyAPIView), which are suitable for basic CRUD operations.


```
# api/urls.py
from django.urls import path
from .views import SongListCreateView, SongDetailView, AddSongFromSpotifyView 

urlpatterns = [
	path('songs/', SongListCreateView.as_view(), name='song-list-create'), # '/' can avoid conflicts with other URLs, the same for all other URLs, here and other files (e.g., music_player_app/urls.py)
	path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
    path('add-song-from-spotify/', AddSongFromSpotifyView.as_view(), name='add-song-from-spotify'),
]
```

**useful**: git commit -m "create and set a new file for api/urls.py with code to set up Django URL patterns for song listing/creation and song detail using 'SongListCreateView' and 'SongDetailView' views, respectively. This information was also updated on Readme."

##### music_player_app/urls.py

music_player_app/urls.py : below code defines Django URL patterns for user authentication, registration, login, logout, and views for the home page, updating a song, and adding a song in the music player app. It includes paths for default authentication views, custom registration and login views, and specific URLs for app features.

```
# music_player_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from music_player_app.views import register, user_login
from music_player_app.views import index, UpdateSong, AddSong
 
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('home', index, name='home'),
    path('UpdateSong/<int:pk>', UpdateSong, name='UpdateSong'),
    path('AddSong', AddSong, name='AddSong'),
]
```

**useful**: git commit -m "create and set a new file for music_player_app/urls.py with code to define Django URL patterns for user authentication, registration, login, logout, and views for the home page, updating a song, and adding a song in the music player app. It includes paths for default authentication views, custom registration and login views, and specific URLs for app features. This information was also updated on Readme."

##  Graphical User Interface (GUI)

Here starts a new and important component. It involves adding a new folder **templates** at the root level of the project directory, on the same level as other existing folders: api, backend and musicplayer. However, some cautions are required by setting up th templates in Django:
- organize the HTML templates properly to ensure clarity and avoid conflicts.
- create a templates folder on the project root backend and named it as **templates**.
- create a subfolder named after the app already created before. In this moment only **templates/music_player_app** is enougth. All the following HTML files are prepared for the User interface,*i.e.* the music_player_app concern. The same folders names keep templates organized and avoids naming conflicts between different apps.
- add HTML Files to **templates/music_player_app**. The conent of each html is bellow. Here is only the list:
    1. AddSong.html
    2. index.html
    3. login.html
    4. register.html
    5. UpdateSong.html
This structure allows Django to easily locate and render the correct templates by functions like ```render()``` in **views.py**.

**useful**: git commit -m "create a new folder on the projects root with a subfolder, the 'templates/music_player_app', to host the html files for the GUI in regards to to music_player_app created earlier. The html files were also added but empety."

### AddSong.html

This HTML file provides a form for adding new songs to the music player. It uses Bootstrap for styling and JavaScript for form validation and handling the submission to a Django API endpoint. The form includes fields for the song title, artist, category, audio file, and album image.

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Add Song</title>

	<!-- Bootstrap CSS -->
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
		integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
		crossorigin="anonymous" />
</head>
<body>
	<div class="container mt-5">
	<h2>Add Song</h2>

	<form id="songForm">
		<div class="form-group">
		<label for="title">Title:</label>
		<input type="text" class="form-control" id="title" name="title" required />
		<div class="invalid-feedback">Title is required.</div>
		</div>

		<div class="form-group">
		<label for="artist">Artist:</label>
		<input type="text" class="form-control" id="artist" name="artist" required />
		<div class="invalid-feedback">Artist is required.</div>
		</div>
		<div class="form-group">
		<label for="categorie">Categorie:</label>
		<input type="text" class="form-control" id="categorie" name="categorie" required />
		<div class="invalid-feedback">Categorie is required.</div>
		</div>

		<div class="form-group">
		<label for="audio_file">Audio File:</label>
		<input type="file" class="form-control-file" id="audio_file" name="audio_file"
				accept="audio/*" required />
		<div class="invalid-feedback">Audio file is required.</div>
		</div>
		<div class="form-group">
		<label for="audio_img">Audio Img:</label>
		<input type="file" class="form-control-file" id="audio_img" name="audio_img" required />
		<div class="invalid-feedback">Audio Img is required.</div>
		</div>

		<button type="button" class="btn btn-primary" onclick="postData()">Submit</button>
	</form>
	</div>

	<!-- Bootstrap JS and dependencies -->
	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
			integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
			crossorigin="anonymous"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
			integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
			crossorigin="anonymous"></script>
	<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
			integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
			crossorigin="anonymous"></script>

	<script>
	function postData() {
		// Validate the form
		if (validateForm()) {
		let title = document.getElementById('title').value
		let artist = document.getElementById('artist').value
		let categorie = document.getElementById('categorie').value
		let audio_file = document.getElementById('audio_file').files[0]
		let audio_img = document.getElementById('audio_img').files[0]
	
		const formData = new FormData()
		formData.append('title', title)
		formData.append('artist', artist)
		formData.append('categorie', categorie)
		formData.append('audio_file', audio_file)
		formData.append('audio_img', audio_img)
	
		fetch('http://127.0.0.1:8000/api/songs/', {
			method: 'POST',
			headers: {
			'X-CSRFToken': getCookie('csrftoken')
			},
			body: formData
		})
			.then((response) => response.json())
			.then((result) => {
			console.log('Success:', result)
			// Refresh the page after successful submission
			location.reload()
			})
			.catch((error) => {
			// Handle errors as needed
			console.error('Error:', error)
			})
		}
	}
	
	function validateForm() {
		const title = document.getElementById('title').value
		const artist = document.getElementById('artist').value
		const categorie = document.getElementById('categorie').value
		const audio_file = document.getElementById('audio_file').files[0]
		const audio_img = document.getElementById('audio_img').files[0]
		const invalidFeedbacks = document.querySelectorAll('.invalid-feedback')
		invalidFeedbacks.forEach((element) => {
		element.style.display = 'none'
		})
	
		let isValid = true
	
		if (!title.trim()) {
		document.getElementById('title').nextElementSibling.style.display = 'block'
		isValid = false
		}
		if (!categorie.trim()) {
		document.getElementById('categorie').nextElementSibling.style.display = 'block'
		isValid = false
		}
	
		if (!artist.trim()) {
		document.getElementById('artist').nextElementSibling.style.display = 'block'
		isValid = false
		}
	
		if (!audio_file) {
		document.getElementById('audio_file').nextElementSibling.style.display = 'block'
		isValid = false
		}
		if (!audio_img) {
		document.getElementById('audio_img').nextElementSibling.style.display = 'block'
		isValid = false
		}
	
		return isValid
	}
	
	// Function to get CSRF token from cookies
	function getCookie(name) {
		var cookieValue = null
		if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';')
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim()
			if (cookie.substring(0, name.length + 1) === name + '=') {
			cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
			break
			}
		}
		}
		return cookieValue
	}
	</script>
</body>
</html>

```

### index.html

This file implements the main music player interface. It displays a list of songs, allows for playback, deletion, and updating of songs. It also includes a search bar to find songs using the Saavn API, as well as a logout button.

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Music Player</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
	<style>
	body {
		font-family: 'Arial', sans-serif;
		text-align: center;
		margin: 50px;
	}
	#audioPlayer {
		width: 100%;
		max-width: 400px;
		margin: 20px auto;
	}
	#playlist {
		list-style: none;
		padding: 0;
	}
	#playlist li {
		margin: 5px;
		cursor: pointer;
		transition: transform 0.3s ease-in-out;
		display: flex;
		justify-content: space-between;
		align-items: center;
	}
	#playlist li:hover {
		transform: scale(1.1);
	}
	</style>
</head>
<body>
	<div class="container">
	<div class="player">
		<img style="width:250px; height:250px;"
			src="https://th.bing.com/th/id/OIP.bLCU8HwL546JIVk9vLV3NAHaHa?rs=1&pid=ImgDetMain"
			alt id="audioPlayerimg" />
		<br />
		<audio id="audioPlayer" class="w-100" controls>Your browser does not support the audio element.</audio>
	</div>
	<label for="Search">Search Song:</label>
	<input type="text" id="Search" placeholder="Enter song name" />
	<button onclick="SearchSongs()">Search</button>
	<ul id="playlist" class="list-group"></ul>
	<button type="button" class="btn btn-primary mt-3" data-toggle="modal" data-target="#addSongModal"
			onclick="AddSong()">Add Song</button>
	<button type="button" class="btnlogout btn btn-danger mt-3" data-toggle="modal"
			data-target="#addSongModal" onclick="Logout()">Logout</button>
	</div>
	<script>
	
document.addEventListener('DOMContentLoaded', function () {
fetchSongs();
});

const audioPlayer = document.getElementById('audioPlayer');
const audioPlayerimg = document.getElementById('audioPlayerimg');
const playlist = document.getElementById('playlist');

function fetchSongs() {
fetch('/api/songs/')
	.then(response => response.json())
	.then(songs => {
		songs.forEach(song => {
			playlist.innerHTML += `<li class="list-group-item" onclick="playSong('${song.audio_file}','${song.audio_img}')">
			<span>${song.title} - ${song.artist}-${song.categorie}</span>
			<div>
				<button class="btn btn-info btn-sm" onclick="UpdateSong(${song.id})">Update</button>
				<button class="btn btn-danger btn-sm" onclick="deleteSong(${song.id})">Delete</button>
			</div></li>`;
		});
	})
	.catch(error => console.error('Error fetching data:', error));
}

function playSong(songSrc, songimg) {
console.log(songSrc);
console.log(songimg);
document.querySelectorAll('#playlist li').forEach((item) => {
	item.style.transform = 'scale(1)';
});
event.target.style.transform = 'scale(1.2)';
audioPlayer.src = songSrc;
console.log(audioPlayerimg);
audioPlayerimg.src = songimg;
audioPlayer.play();
}

function deleteSong(songId) {
if (confirm('Are you sure you want to delete this song?')) {
	fetch(`/api/songs/${songId}/`, {
		method: 'DELETE',
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': '{{ csrf_token }}',
		},
	})
		.then(response => {
			if (response.ok) {
				location.reload();
			} else {
				alert('Failed to delete the song. Please try again.');
			}
		})
		.catch(error => {
			console.error('Error:', error);
		});
}
}

function AddSong() {
window.location.href = `/AddSong`;
}

function UpdateSong(itemId) {
window.location.href = `/UpdateSong/${itemId}`;
}

function Logout(itemId) {
window.location.href = `/logout/`;
}
function SearchSongs() {
const SearchSong = document.getElementById('Search').value.toLowerCase();
// Saavn API endpoint for searching songs
const saavnSearchUrl = 'https://saavn.me/search/songs';

// Query parameters for the search
const params = {
	query: SearchSong,
};

// Request headers
const headers = {
	'Content-Type': 'application/json',
};

// Make the GET request to search for songs
fetch(`${saavnSearchUrl}?${new URLSearchParams(params)}`, {
	method: 'GET',
	headers: headers,
})
	.then(response => response.json())
	.then(songData => {
		playlist.innerHTML = '';
		for (const song of songData.data.results) {
			const songName = song.name;
			const artistName = song.primaryArtists;
			const highestQualityDownloadUrl = song.downloadUrl.find(downloadUrl => downloadUrl.quality === '320kbps');
			const image150x150 = song.image.find(image => image.quality === '150x150');
			const lowestQualityImage = song.image.find(image => image.quality === '50x50');
			playlist.innerHTML += `<li class="list-group-item" onclick="playSong('${highestQualityDownloadUrl.link}','${image150x150.link}')"><span>
			<img src="${lowestQualityImage.link}">
			${songName} by ${artistName}</span>
			</li>`;
		}
	})
	.catch(error => console.error('Error:', error));

}
	</script>
</body>
</html>

```

### login.html

This HTML document creates a login form for users to authenticate themselves. It’s styled with Bootstrap and contains fields for username and password, along with a link for user registration.

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Login</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container">
	<div class="row">
	<div class="col-md-6 offset-md-3">
		<h2 class="mt-4 mb-4">Login</h2>
		<form method="post" class="mb-4">
		{% csrf_token %}
		{{ form.as_p }}
		<button type="submit" class="btn btn-primary">Login</button>
		</form>
		<p>Don't have an account? <a href="{% url 'register' %}" class="btn btn-link">Register here</a>.</p>
	</div>
	</div>
</div>
</body>
</html>

```

### register.html

Similar to login.html, this file provides a registration form for new users to create an account. It includes fields for username, password, and password confirmation, and it’s also styled using Bootstrap.

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Register</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
</head>
<body>
	<div class="container">
	<div class="row">
		<div class="col-md-6 offset-md-3">
		<h2 class="mt-4 mb-4">Register</h2>
		<form method="post" class="mb-4">
			{% csrf_token %}
			{{ form.as_p }}
			<button type="submit" class="btn btn-primary">Register</button>
		</form>
		<p>Already have an account? <a href="{% url 'login' %}" class="btn btn-link">Login here</a>.</p>
		</div>
	</div>
	</div>
</body>
</html>

```

### UpdateSong.html

This file contains a form for updating existing songs in the music player. It retrieves song data via an API call, populates the form with the existing data, and allows users to modify and submit updates.

```
<!-- music_player_app/templates/music_player_app/update_form.html -->

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<title>Update Song</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" />
</head>
<body>
	<div class="container mt-5">
	<h2>Update Song</h2>
	<form id="updateForm">
		<div class="form-group">
		<label for="title">Title</label>
		<input type="text" class="form-control" id="title" name="title" required />
		<label for="artist">Artist</label>
		<input type="text" class="form-control" id="artist" name="artist" required />
		<label for="categorie">Categorie</label>
		<input type="text" class="form-control" id="categorie" name="categorie" required />
		<label for="audio_file">Audio File</label>
		<input type="file" class="form-control-file" id="audio_file" name="audio_file" accept="audio/*" required />
		<label for="audio_img">Audio Img</label>
		<input type="file" class="form-control-file" id="audio_img" name="audio_img" required />
		</div>
		<!-- Add other form fields as needed -->

		<button type="submit" class="btn btn-primary">Update</button>
	</form>
	</div>

	<script>
	document.addEventListener('DOMContentLoaded', function () {
		// Fetch song data and fill the form fields
		const url = window.location.pathname.split('/')
		let songId = url[2]
		fetch(`/api/songs/${songId}/`)
		.then((response) => response.json())
		.then((data) => {
			document.getElementById('title').value = data.title
			document.getElementById('artist').value = data.artist
			document.getElementById('categorie').value = data.categorie
			document.getElementById('audio_file').value = ''
			document.getElementById('audio_img').value = ''
		})
		.catch((error) => console.error('Error fetching song data:', error))
	
		// Submit form with API call
		document.getElementById('updateForm').addEventListener('submit', function (event) {
		event.preventDefault()
	
		// Get form data
		const formData = new FormData(this)
	
		// Make API call to update song
		fetch(`/api/songs/${songId}/`, {
			method: 'PUT',
			headers: {
			'X-CSRFToken': getCookie('csrftoken') // Ensure to include CSRF token
			},
			body: formData
		})
			.then((response) => response.json())
			.then((data) => {
			alert('Song updated successfully!')
			window.location.href = '/home' // Redirect to the song list page
			})
			.catch((error) => console.error('Error updating song:', error))
		})
	})
	
	// Function to get CSRF token from cookies
	function getCookie(name) {
		var cookieValue = null
		if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';')
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim()
			if (cookie.substring(0, name.length + 1) === name + '=') {
			cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
			break
			}
		}
		}
		return cookieValue
	}
	</script>
</body>
</html>

```

### git commit it!!

**useful**: git commit -m "all files html empty created on the stept (git commit) before were now filled up with code. All of them belongs to GUI associated to the Django's music_player_app"

## admin.py

Here is the last step before deploying the Django's app!

The **admin.py** files for both the **api** and **music_player_app** apps play a crucial role in managing the data models through the Django admin interface. They are responsible for registering models with Django's admin site, providing a user-friendly interface for performing CRUD operations on these models. This is directly related to the database, as each model represents a table in the database, and CRUD operations modify the data stored in these tables.
| **App Folder**          | **Models Registered in admin.py**             |
|-------------------------|-----------------------------------------------|
| `api/admin.py`          | `Song`, `SongAdmin`                                        |
| `music_player_app/admin.py` | `CustomUser`, `UserAdmin`                               |


Additionally, by setting up these models in the admin, it prepares the backend to integrate with RESTful APIs, which use HTTP methods to perform CRUD operations programmatically. [Migrations](https://docs.djangoproject.com/en/5.1/topics/migrations/#module-django.db.migrations) in Django are essential for managing and evolving the database schema based on changes to models. The ```makemigrations``` command creates migration files that track these changes, while ```migrate``` applies them to the database, ensuring consistency. This process is crucial for aligning the backend with RESTful APIs and allows the Django admin (**admin.py**) to manage data accurately according to the latest model definitions. For this reason it is important to run the both commands before deploing Django.

Finally, this setup ensures that data can be managed both via the Django admin interface and through API calls, facilitating a flexible and comprehensive approach to data management in the application.

### api/admin.py

Here the models of api app are registred.

```
### api/admin.py
from django.contrib import admin
from .models import Song
 
class SongAdmin(admin.ModelAdmin):
    list_display = ('id','title','categorie', 'artist', )
    search_fields = ('title', 'artist')
 
admin.site.register(Song, SongAdmin)
```

### music_player_app/admin.py

Here the app of music_player_app app are registred.

```
# music_player_app/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
 
admin.site.register(CustomUser, UserAdmin)
```

**useful**: git commit -m "create and update the admin.py files at api and music_player_app folder each. They are the last step before migration and deploy Django app"

# Database

After all implementation above, 2 important step was done in regards to data bank: implementation of Spotify search and PostgreSQL. See the file backend/spotify.py with comments there. The PostgreSQL was implement basically on seetings.py using the Djangos' APIs, but also keeping the default SQLite for the development modus (DEBUG=True) for quick and easier tests.


# Deployment checklist

Before deploying the Django project, review the settings in regards to security, performance, and operations ([doc](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/)).

Frist, [run check deploy](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/#run-manage-py-check-deploy):

```python manage.py check --deploy```

Check and protect the environmental variables by setting the files [**backend/settings.py** and **.env**](https://docs.djangoproject.com/en/5.1/topics/settings/#django-settings). (dont' forget set .env on .gitingore and .dockerignore as well). Because a settings file contains sensitive information, such as the database password, you should make every attempt to limit access to it. For example, change its file permissions so that only you and your web server’s user can read it. This is especially important in a shared-hosting environment ([see Django's doc.](https://docs.djangoproject.com/en/5.1/topics/settings/#security)).

The **.env** file makes more sense in the context of git and container. Thus, it is important to set **.env** on their ignore files:
```
echo .env > .gitignore
echo .env > .dockerignore
``` 

### backend/settings.py ([doc](https://docs.djangoproject.com/en/5.1/topics/settings/#django-settings))

### .env

.env has all environmental variables such the secret key.

For the Django´s secrete key, make on stronge one with some tools such as:

```
python -c "from django.core.management.utils import get_random_secret_key; import pyperclip; secret_key = get_random_secret_key(); pyperclip.copy(secret_key); print('Secret key copied to clipboard:', secret_key)"
```
This command copys the key to the clipboar direct, but need the pythons' library `pyperclip` installed.

### dependecies

Update **requirements.txt**.

```pip freeze > requirements.txt```

# Migration & Deploy

Again, just in case, it is a matter of security: [run check deploy](https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/#run-manage-py-check-deploy):

```
python manage.py check --deploy
```

Finally, run the Migration's commands and deploy Django. This is enought, but check others commands at [Djangos' doc](https://docs.djangoproject.com/en/5.1/topics/migrations/#module-django.db.migrations)) for other possibilities before deploying.

```python manage.py makemigrations```
```python manage.py migrate```
```python manage.py runserver```

Now that the server’s running, visit http://127.0.0.1:8000/ on the web browser ([Django's doc.](https://docs.djangoproject.com/en/5.1/intro/tutorial01/#the-development-server)).

# **Docker**

Until here there is only one dockerfile to buil the docker image and wouldn't be necessary to use the **docker-compose.yml** now, but it is interesting for build the image due to the files structure such **.env** and **.dockerignore** at the main root, out of the backend directory instead. This procedure make also easier to set tags for the containers' name by setting then inside the docker-compose.yml instead of in each ```docker build --tag...```. 

Only **requirements.txt** is interesting to keep simple copy inside the directories to avoid more setting paths inside the Dockerfiles. For this reason start this step by copying it to respective directories with (in WSL2 and Mac):

```cp requirements.txt ./backend/requirements.txt```

Now, builing the images and run containers:

```docker-compose build ```

```docker-compose up ``` 

Or run ```docker-compose up -d``` on detached mode to keep the terminal free, *i.e.* ruining in background. In this case, 2 commands are useful: `docker-compose ps` to check the containers are runing and `docker-compose down` to stop them.

Just in case of enventual problem to remove and rebuild images, containers and volums after tests (e.g., after changing Dockerfile, or environmental variables on .env):

```docker-compose down -v```

```docker-compose up --build```

Kinds of possible problems during the creation of containers with docker-compose is the delay between Django and PostSQL, and them the connection fail between them, a matter of syncronization. This project has faced this problem and the solution was to set the function wait-for-it developed by [Vishna Bob](https://github.com/vishnubob/wait-for-it). The function has been implemtend in bash file, which was donwloaded and save on Django's directory (backend):

```curl -o backend/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh```

```chmod +x backend/wait-for-it.sh```