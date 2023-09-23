from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    image = forms.ImageField(label='Фото')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('image',)
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'image']

from django import forms

class MessageForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='Отправитель')
