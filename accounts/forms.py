from django import forms

from accounts.models import CustomUser, Profile


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=[
            'username',
            'phone',
            'email',
            'password'
        ]


    def save(self, commit = True,**kwargs):
        return CustomUser.objects.create_user(
            username=self.cleaned_data.get('username'),

            email=self.cleaned_data.get('email'),
            phone=self.cleaned_data.get('phone'),
            password=self.cleaned_data.get('password')
        )



class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=[
            'age',
            'avtar',
            'bio'
        ]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=150)
    password=forms.CharField(max_length=150)