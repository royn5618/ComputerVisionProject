from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cvprojects(request):
    return render(request, 'cvprojects.html')
