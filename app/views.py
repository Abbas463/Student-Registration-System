from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        dob=request.POST['dob']
        gen=request.POST['gender']
        cla=request.POST['class']
        regn=request.POST['reg']
        test=request.POST['test']

        if test > 100:
            return HttpResponse("Test Scores must be less than 100")

        print('name is', name, email, dob, gen, cla, regn, test)
        return render(request, 'index.html')

    return render(request, 'index.html')