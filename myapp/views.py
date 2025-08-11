from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# it's required to put 'request' param
def home(request):

    # HttpResponse : allow our function to return http response to the user
    return HttpResponse("Hello World!")

