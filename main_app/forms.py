from django import forms
from .models import Person

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type': 'date'}), required=False)