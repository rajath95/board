from django.shortcuts import HttpResponse
from django.shortcuts import render,render_to_response


def basic(request):
    return HttpResponse("Welcome")

def table(request):
    return render_to_response('index.html',context=None)
