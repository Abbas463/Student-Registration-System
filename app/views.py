from django.shortcuts import render, HttpResponse
from .models import Student

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        dob = request.POST['dob']
        gen = request.POST['gender']
        cla = request.POST['class']
        regn = request.POST['reg']
        test = request.POST['test']

        if float(test) > 100:
            return HttpResponse("Test Scores must be less than 100")

        obj = Student()
        obj.name = name
        obj.email = email
        obj.dob = dob
        obj.gen = gen
        obj.stuClass = cla
        obj.reg = regn
        obj.test = test
        obj.save()

        return render(request, "success.html")

    return render(request, "index.html")


def list_stu(request):
    obj = Student.objects.all()
    return render(request, "list.html", {"obj": obj})