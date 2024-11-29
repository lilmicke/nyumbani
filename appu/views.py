from msilib.schema import Property

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import PropertyForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def about(request):
    return render(request, 'appu/about.html')

def contact(request):
    return render(request, 'appu/contact.html')

def index(request):
    return render(request, 'appu/index.html')

def propertyAgent(request):
    return render(request, 'appu/property-agent.html')

# appu/views.py

from .models import Property  # Import the Property model

def propertyList(request):
    properties = Property.objects.all()
    return render(request, 'appu/property-list.html', {'properties': properties})


def propertyType(request):
    return render(request, 'appu/property-type.html')

def testimonials(request):
    return render(request, 'appu/testimonial.html')

def welcome(request):
    return render(request, 'appu/welcome.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'appu/login.html')

def add_property(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, "appu/addproperty.html", {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'appu/signup.html', {'form': form})

def apartments(request):
    return render(request, 'appu/apartments.html')

def building(request):
    return render(request, 'appu/building.html')

def garage(request):
    return render(request, 'appu/garage.html')

def home(request):
    return render(request, 'appu/nyumbani.html')

def office(request):
    return render(request, 'appu/office.html')

def townhouse(request):
    return render(request, 'appu/townhouse.html')

def villas(request):
    return render(request, 'appu/villas.html')

def shop(request):
    return render(request, 'appu/shop.html')