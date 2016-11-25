from django.conf.urls import url , handler404, handler500
from . import views
handler500 ='views.serverrequest'
handler404 = 'views.badrequest'
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='index'),
    url(r'^mail/$', views.CreateMail.as_view(), name='mail'),
    url(r'^mail/(?P<pk>[0-9]+)/$', views.DetailMail.as_view(), name='detail_mail'),
    url(r'^listmail/$', views.ListMail.as_view(), name='list_mail'),
    url(r'^customers/$', views.AddCustomers.as_view(), name='customers'),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.Viewcustomer.as_view(), name='view_customer')
]