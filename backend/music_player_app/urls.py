# music_player_app/urls.py
# urlpatterns are the URLs that will be used in the app. 
# It is the first file that Django will look for when the app is started
# here you can find the paths of html files implemented in folder 'templates' and the views that will be used in the app
# for each file name, use '/' after the name (e.g.'register/'). It can avoid conflicts with other URLs.

from django.contrib import admin
from django.urls import path, include  # include only for alternative 'accounts/' below
from django.contrib.auth.views import LogoutView
from music_player_app.views import register, user_login, add_song, update_song, index

urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')), # dont´use! just as memory. accoutns here is reduntante for register, login and logout below. Use either this or the 3 below!
    path('', index, name='index'),         # this is the home page #1! (e.g., http://127.0.0.1:8000/ or the domain) It is the first page that will be shown when the app is started
    path('home/', index, name='home'),     # ... also home, but so http://127.0.0.1:8000/home or the domain/home. It is not necessary with path('', index...) before, but it is a good practice to have it as a second option
    path('register/', register, name='register'), 
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'), # it is the only one non-html file. It uses 'LogoutView.as_view' instead of 'user_login' because it is a standard Django view and don't need a hmtl to be rendered, just a redirection to the login page!
    path('add-song/', add_song, name='add_song'),  # Added URL for add_song view
    path('update-song/<int:song_id>/', update_song, name='update_song'),  # Added URL for update_song view
]