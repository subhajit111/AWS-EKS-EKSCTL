from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    return HttpResponse('Hello World')

# here we are using render which returns a HttpResponse.
def adding_template(request):
    return render(request, 'hello.html')
