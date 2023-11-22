from django.shortcuts import render
from django.http import HttpResponse
from . models import table1
from . models import team
# Create your views here.
def demo(request):
    obj2 = team.objects.all()
    object1 = table1.objects.all()
    # name = "INDIA"
    return render(request, 'index.html',{'result':object1,'Team':obj2})#,{'obj':name})
# def addition(request):
#     return render(request,'addition.html')
# def result(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res = x+y
#     return render(request,'result.html',{'result':res})

# def about(request):
#     return render(request,'addition.html')
# def contact(request):
#     return HttpResponse("THIS IS THE CONTACT PAGE")