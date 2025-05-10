from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
import json

from .models import Person
from .forms import PersonModelForm

# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
    persons = Person.objects.all()
    context['persons'] = persons
    context['form'] = PersonModelForm()
    return render(request, "home.html", context)

def contact(request):
    return render(request, "contact.html")

def get_all_persons(request):
    persons_list = []
    persons = Person.objects.all()
    data = serializers.serialize("json", persons) # json like string
    data = json.loads(data)
    for i in data:
        persons_list.append(i["fields"])
    return JsonResponse(data=persons_list, safe=False)


def delete_person(request, id):
    Person.objects.get(id=id).delete()
    return redirect("/")