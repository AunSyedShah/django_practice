from django.shortcuts import render
from .models import Person

# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        contactName = request.POST['contactName']
        contactNumber = request.POST['contactNumber']
        Person.objects.create(name=contactName, contactNumber=contactNumber)
    persons = Person.objects.all()
    context['persons'] = persons
    return render(request, "home.html", context)

def contact(request):
    return render(request, "contact.html")