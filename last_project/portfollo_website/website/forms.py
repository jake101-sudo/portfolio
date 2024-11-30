from django import forms
from django.forms import ModelForm
from .models import Contact, Comment
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creat contact form
# forms for the user to imput data that saves to the model 
 
class ContectForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('email', 'name', 'message')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    # Custom password validation
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        # Minimum password length check
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']