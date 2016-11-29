from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^mail/$', views.CreateMail.as_view(), name='mail'),
    url(r'^mail/(?P<pk>[0-9]+)/$', views.DetailMail.as_view(), name='detail_mail'),
    url(r'^listmail/$', views.ListMail.as_view(), name='list_mail'),
    url(r'^updatemail/(?P<pk>[0-9]+)/$', views.UpdateMail.as_view(), name='update_mail'),
    url(r'^customers/$', views.AddCustomers.as_view(), name='customers'),
    url(r'^listcustomers/$', views.ListCustomers.as_view(), name='list_customers'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.ViewCustomer.as_view(), name='view_customer'),
    url(r'^updatecustomer/(?P<pk>[0-9]+)/$', views.UpdateCustomer.as_view(), name='update_customer'),
    url(r'^destination/$', views.AddDestination.as_view(), name='destination'),
    url(r'^destination/(?P<pk>[0-9]+)/$', views.DetailDestination.as_view(), name='detail_destination'),
    url(r'^listdestination/$', views.ListDestination.as_view(), name='list_destinations'),
    url(r'^updatedestination/(?P<pk>[0-9]+)/$', views.UpdateDestination.as_view(), name='update_destination'),
]