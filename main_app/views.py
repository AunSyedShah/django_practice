from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
import json
from django.core.signing import Signer

from .models import Person
from .forms import PersonModelForm


signer = Signer()

# Create your views here.
def home(request):
    context = {}
    if request.method == "POST":
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
    persons = Person.objects.all()
    signed_person = []
    for person in persons:
        person.encrypted_id = signer.sign(person.id)
        signed_person.append(person)
    context['persons'] = signed_person
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
    id = signer.unsign(id)
    Person.objects.get(id=id).delete()
    return redirect("/")


def update_person(request, id):
    person_id = signer.unsign(id)
    person = Person.objects.get(pk=person_id)

    if request.method == "POST":
        form = PersonModelForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PersonModelForm(instance=person)

    return render(request, "update_person.html", {"form": form})