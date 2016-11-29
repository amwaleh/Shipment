from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from .models import Mailbag, Customers, Destinations

class DestinationBase(SuccessMessageMixin):
    model = Destinations
    fields = '__all__'
    template_name = 'index.html'
    success_message = "%(location)s was successfully committed"

class Mailbag(SuccessMessageMixin):
    model = Mailbag
    fields = "__all__"
    template_name = "index.html"
    success_message = " %(sender)s mail was successfully added"

class Customer(SuccessMessageMixin):
    model = Customers
    fields = "__all__"
    template_name = "index.html"
    success_message = " %(first_name)s  successfully added"


class Home (TemplateView):
    template_name = "index.html"


class CreateMail (Mailbag,CreateView):
    pass

class DetailMail(Mailbag,DetailView):
    context_object_name = 'detail_mail'

class ListMail(Mailbag, ListView):
    context_object_name = 'list_mail'
    paginate_by = 6

class UpdateMail(Mailbag,UpdateView):
    pass


class AddCustomers(Customer,CreateView):
    pass


class ViewCustomer(Customer, DetailView):
    context_object_name = "customer_detail"


class ListCustomers(Customer,ListView):
    context_object_name = "customer_list"
    paginate_by = 6


class UpdateCustomer(Customer, UpdateView):
    pass


class DetailDestination(DestinationBase,DetailView):
    context_object_name = 'destination_detail'


class AddDestination(DestinationBase,CreateView):
    template_name = 'index.html'


class ListDestination(DestinationBase,ListView):
    paginate_by = 6
    context_object_name = "destination_list"


class UpdateDestination(DestinationBase,UpdateView):
    pass
