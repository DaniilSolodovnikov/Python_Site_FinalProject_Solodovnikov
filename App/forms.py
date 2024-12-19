from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from App.models import Ad


class RentalAdForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    price = forms.DecimalField(label='Price', max_digits=6, decimal_places=2)
    image = forms.ImageField(label='Image')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'image', 'description']

