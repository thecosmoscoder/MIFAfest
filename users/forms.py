from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser  

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        models = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'country')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        models = CustomUser
        fields = UserChangeForm.Meta.fields

