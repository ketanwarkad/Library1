from django.http import HttpResponse

def func1(request):
    return HttpResponse("In func1")