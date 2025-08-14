from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# it's required to put 'request' param
def home(request):

    # HttpResponse : 
        # allow our function to return http response to the user
        # serves as our Template, it return html in simple form
        # can't return html file
    #return HttpResponse('<h1>Hello</h1>')

    # render :
        # allows our View function to return http response to the user
        # 
    return render(request, 'myapp/home.html', {})

def my_page(request):
    return render(request, 'myapp/my-page.html', {})