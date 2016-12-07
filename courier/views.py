from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from .models import Mailbag, Customers, Destinations
from django.db.models import Q

class DestinationBase(SuccessMessageMixin):
    model = Destinations
    fields = '__all__'
    template_name = 'content.html'
    success_message = "%(location)s was successfully committed"

class MailbagBase(SuccessMessageMixin):
    model = Mailbag
    fields = "__all__"
    template_name = "content.html"
    success_message = " %(sender)s mail was successfully added"

class Customer(SuccessMessageMixin):
    model = Customers
    fields = "__all__"
    template_name = "content.html"
    success_message = " %(first_name)s  successfully added"


class Home (TemplateView):
    template_name = "content.html"


class CreateMail (MailbagBase, CreateView):
    pass

class DetailMail(MailbagBase, DetailView):
    context_object_name = 'detail_mail'

class ListMail(MailbagBase, ListView):
    context_object_name = 'list_mail'
    paginate_by = 6

class UpdateMail(MailbagBase, UpdateView):
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
    template_name = 'content.html'


class ListDestination(DestinationBase,ListView):
    paginate_by = 6
    context_object_name = "destination_list"


class UpdateDestination(DestinationBase,UpdateView):
    pass

class Search(ListMail):

    def get_queryset(self):
        term = self.request.GET.get('search')
        queryset = Mailbag.objects.filter(
                                          Q(sender__first_name__icontains=term) |
                                          Q(sender__tel__icontains=term)|
                                          Q(sender__last_name__icontains=term)|
                                          Q(recipient__icontains=term)|
                                          Q(description__icontains=term)|
                                          Q(destination__location__icontains=term)|
                                          Q(destination__location__search=term)
                                            ).order_by('-modified')
        if not queryset:
            messages.error(self.request, 'No result found for \'{}\''.format(term))


        return queryset
