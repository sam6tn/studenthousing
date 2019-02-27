from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    numbers = [1,2,3,4]
    name = "Corban"


    args = {'myName': name, 'numbers': numbers}

    return render(request, 'home/login.html', args)