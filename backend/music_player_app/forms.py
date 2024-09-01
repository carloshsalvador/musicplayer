# music_player_app/forms.py
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    pass  # meta class is not necessary when using AuthenticationForm (Django´s standard form for login)

## only for reference in the case of a custom form for login. Kept for memory:
# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']
