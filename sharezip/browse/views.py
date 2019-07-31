from django.shortcuts import render
from hosting.models import Room

# Create your views here.
def home(request):
    return render(request,'home.html')

def base (request):
    return render(request,'base.html')

def condition(request):
    return render(request, 'condition.html')

def result(request):
    rooms=Room.objects.all()
    return render(request, 'result.html', {'rooms':rooms})