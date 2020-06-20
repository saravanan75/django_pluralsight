# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello there, globomantics e-commerce store front coming here...")


def detail(request):
    return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here...")


def electronics(request):
        return HttpResponse("Hello there, globomantics e-commerce store front Electronics pages coming here...")



