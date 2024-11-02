from django.shortcuts import render

def about(request):
    return render(request, 'appu/about.html')

def contact(request):
    return render(request, 'appu/contact.html')

def index(request):
    return render(request, 'appu/index.html')

def propertyAgent(request):
    return render(request, 'appu/property-agent.html')

def propertyList(request):
    return render(request, 'appu/property-list.html')

def propertyType(request):
    return render(request, 'appu/property-type.html')

def testimonials(request):
    return render(request, 'appu/testimonial.html')


def welcome(request):
    return render(request, 'appu/welcome.html')
