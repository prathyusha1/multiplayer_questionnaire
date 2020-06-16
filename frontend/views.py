from django.shortcuts import render


def index(request):
    print("**in index");
    return render(request, 'frontend/index.html')
