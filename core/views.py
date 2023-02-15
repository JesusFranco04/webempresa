from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

def sample(request):
    return render(request, 'sample.html', {})

def services(request):
    return render(request, 'services.html', {})

def store(request):
    return render(request, 'store.html', {})
# Create your views here.
