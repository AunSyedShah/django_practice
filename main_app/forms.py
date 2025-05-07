from django.forms import ModelForm
from .models import Person

class PersonModelForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'