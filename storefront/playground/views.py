from django.shortcuts import render
from django.http import HttpResponse

"""
Create your views here.
A view processes a request and returns a response. In Django speak, a view is
basically a request handler

"""
def say_hello(request):
    """
    The render() function takes two params:  a Http request, and a template

    which can be an html file that would be rendered as a response on the page.
    """
    return render(request, 'hello.html', {'name': 'Okechukwu'})

def say_hello_root(request):
    
    return HttpResponse('You are at the root page of the playground application \n. Visit playground/hello for a welcome message')