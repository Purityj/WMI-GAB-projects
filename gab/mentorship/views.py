from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mentorship/home.html')

def about(request):
    return render(request, 'mentorship/about.html')

def mentor(request):
    return render(request, 'mentorship/mentor.html')

def mentee(request):
    return render(request, 'mentorship/mentee.html')
