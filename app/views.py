from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method=='POST':
        name=request.POST['name']
        print('name is', name)
        return render(request, 'index.html')

    return render(request, 'index.html')