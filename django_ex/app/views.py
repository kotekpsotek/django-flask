# Here I define URL for users
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import ItemNo1

# Create your views here.
def home(request):
    return HttpResponse("Io sonno Michał. Hello world!")

def template(request):
    return render(request, "first.html")

def databse_view(request):
    # Query for all items using Django ORM
    items = ItemNo1.objects.all() # Gives me list with items
    return render(request, "esnext.html", {"items": items})

def json_response(request):
    return JsonResponse({"json_text": "Hello from Json"})