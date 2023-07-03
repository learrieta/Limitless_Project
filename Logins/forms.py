from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile


class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    age = forms.CharField(max_length=20)
    bio = forms.CharField(max_length=19900)
    height = forms.FloatField()  # Height in meters
    weight = forms.FloatField()  # Weight in kilograms
    monthly_goals1 = forms.CharField( max_length=1000)
    monthly_goals2 = forms.CharField( max_length=1000)
    monthly_goals3 = forms.CharField( max_length=1000)
    sleep_goals = forms.CharField( max_length=40)
    water_goals = forms.CharField( max_length=1000)

    class Meta:
        model = User
        fields = ('name', 'username', 'email','age', 'bio','height','weight','monthly_goals1','monthly_goals2','monthly_goals3','sleep_goals','water_goals', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        name_parts = self.cleaned_data['name'].split()
        user.first_name = name_parts[0]
        user.last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""
        user.email = self.cleaned_data['email']
        user.bio = self.cleaned_data['bio']
        user.height = self.cleaned_data['height']
        user.weight = self.cleaned_data['weight']
        user.monthly_goals1 = self.cleaned_data['monthly_goals1']
        user.monthly_goals2 = self.cleaned_data['monthly_goals2']
        user.monthly_goals3 = self.cleaned_data['monthly_goals3']
        user.sleep_goals = self.cleaned_data['sleep_goals']
        user.water_goals = self.cleaned_data['water_goals']
        if commit:
            user.save()  # save the user first
        return user


class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    bio = forms.CharField(max_length=19900)
    age = forms.CharField(max_length=20)
    height = forms.FloatField()  # Height in meters
    weight = forms.FloatField()  # Weight in kilograms
    monthly_goals1 = forms.CharField( max_length=1000)
    monthly_goals2 = forms.CharField( max_length=1000)
    monthly_goals3 = forms.CharField( max_length=1000)
    sleep_goals = forms.CharField( max_length=40)
    water_goals = forms.CharField( max_length=1000)
    class Meta:
        model = UserProfile
        fields = ('name',  'email','age','bio','height','weight','monthly_goals1','monthly_goals2','monthly_goals3','sleep_goals','water_goals')
