from django import forms
from .models import Person
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'


    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control w-25', 'placeholder':"Shabi Naqvi"}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}), required=False)


class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'