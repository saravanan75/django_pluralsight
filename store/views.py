from django.views import View
from django.core.exceptions import ViewDoesNotExist
from django.core.paginator import Paginator, PageNotAnInteger
from django.shortcuts import render
from django.contrib import messages
from django.urls import path
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound, request, response

# def error_handler(request, exception=None):
#     return HttpResponseNotFound("<h1>Page Not Found</h1>", status=404)
#
#
# def page_not_found(request):
#     raise ViewDoesNotExist
#
# urlpatterns = [
#     path('404/', page_not_found),
# ]
#
# handler403 = error_handler
from django.views.decorators.gzip import gzip_page
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, TemplateView


def index(request):
    return HttpResponse("Hello there, globomantics e-commerce store front coming here...")


def detail(request):
    return HttpResponse("Hello there, globomantics e-commerce store front detail pages coming here...")


def logout(request):
    try:
        del request.session['customer']
    except KeyError:
        print("Error while logging out")
    return HttpResponse("You're logged out")


@csrf_exempt
@cache_page(900)
@gzip_page
@require_http_methods(["GET"])
def electronics(request):
    items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")

    if request.method == 'GET':
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        name = "Sharu"
        messages.info(request, "Customer Successfully Fetched")
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        if not request.session.has_key('customer'):
            request.session['customer'] = name
            print("Session value set.")
        response = render(request, 'store/list.html', {'items': items})
        if request.COOKIES.get('visits'):
            value = int(request.COOKIES.get('visits'))
            print("Getting Cookie")
            response.set_cookie('visits', value + 1)
        else:
            value = 1
            print("Setting Cookie")
            response.set_cookie('visits', value)
        return response
    elif request.method == 'POST':
        return HttpResponseNotFound("POST method is not allowed")


class ElectronicsView(View):
    def get(self, request):
        items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
        paginator = Paginator(items, 2)
        pages = request.GET.get('page', 1)
        self.process()
        messages.warning(request, "This page will list all the electronics",extra_tags='alert')
        try:
            items = paginator.page(pages)
        except PageNotAnInteger:
            items = paginator.page(1)
        return render(request, 'store/list.html', {'items': items})

    def process(self):
        print("We are processing Electronics")


class ComputersView(ElectronicsView):
    pass


class MobileView():
    pass


class EquipmentView(MobileView, ComputersView):
    pass

class ElectronicsView2(TemplateView):
    template_name = 'store/list.html'
    def get_context_data(self, **kwargs):
        items = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
        context = {'items': items}
        return context


class ElectronicsView3(ListView):
    template_name = 'store/list.html'
    queryset = ("Windows PC", "Apple Mac", "Apple iPhone", "Lenovo", "Samsung", "Google")
    context_object_name = 'items'
    paginate_by = 2
