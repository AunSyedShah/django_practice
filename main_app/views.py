from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

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

def get_all_persons(request):
    persons = Person.objects.all()
    persons_json = serializers.serialize('json', persons)
    return JsonResponse(data=persons_json, safe=False)