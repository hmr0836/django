#from django.http import HttpResponse
from django.shortcuts import render

def hi(request,x,y):
    #w = request.GET.get('w')
    #return HttpResponse('<h1>{}</h1>',format(x / y))
    s = x + y
    return render(request,'hi.html',{'s':s},)

def r(request,x1,y1):

    if x1 > y1:
        x1 , y1 = y1 , x1
        rang1 = range(x1,y1+1)
        rang1 = reversed(rang1)
    else:
        rang1 = range(x1, y1 + 1)

    return render(request,'r.html',{'rang1':rang1},)

def tag_test(request):
    ll = [2,4,6,8,10,12,2,4,6,8,10,12]

    return render(request,'tag_test.html',{'ll':ll},)