from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    persons = Person.objects.all()
    context = {
        "persons": persons
    }
    return render(request, "home.html", context)

def contact(request):
    return render(request, "contact.html")