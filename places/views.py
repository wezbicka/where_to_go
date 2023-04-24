from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def show_main_page(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
