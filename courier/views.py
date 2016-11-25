from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, DetailView
from .models import Mailbag, Customers
from django.shortcuts import render_to_response
from django.template import RequestContext


def badrequest(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def serverrequest(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

class Home (TemplateView):
    template_name = "index.html"

class CreateMail (CreateView):
    model = Mailbag
    fields = "__all__"
    template_name = "index.html"
    context_object_name = "context"


class ListMail(ListView):
    model = Mailbag
    fields = '__all__'
    template_name = "index.html"
    context_object_name = 'list_mail'


class DetailMail(DetailView):
    model= Mailbag
    fields = '__all__'
    template_name = 'index.html'
    context_object_name = 'detail_mail'

class AddCustomers(CreateView):
    model = Customers
    fields = "__all__"
    template_name = "index.html"

class Viewcustomer(DetailView):
    model = Customers
    template_name = "index.html"
    context_object_name = "customer_detail"

