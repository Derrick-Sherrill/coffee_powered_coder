from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'tutorials/index.html')

def python_home(request):
    return render(request, 'tutorials/python.html')
