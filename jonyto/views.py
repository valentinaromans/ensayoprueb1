from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jony(request):
    html = """
    <h1>Hola jonyto, esta es la primera página</h1>
    """

    return HttpResponse(html)



def vale(request):
    html = """
    <h1 style="color=blue">Hola valita, esta es la segunda página</h1>
    """
    return HttpResponse(html)
