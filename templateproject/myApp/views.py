from django.shortcuts import render

# Create your views here.


def view1(request):
    return render(request, 'myApp/one.html')
