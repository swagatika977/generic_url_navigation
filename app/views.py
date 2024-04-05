from django.shortcuts import render

# Create your views here.
def football(request):
    return render(request,'football.html')

def vollyball(request):
    return render(request,'vollyball.html')
