from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField


# расширяю UserCreationForm для добавления поля email при регистрации
class CustomUserForm(UserCreationForm):
    email = EmailField(required=True, help_text="Required.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']