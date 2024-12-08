from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())

def faq(request):
    template = loader.get_template('faq.html')
    return HttpResponse(template.render())