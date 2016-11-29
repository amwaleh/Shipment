from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from courier.models import Customers, Destinations, Mailbag

class TestViews(TestCase):
    fixtures = ['fixture.json']
    def setUp(self):
        self.client = Client()

    def test_landingPage(self):
        response = self.client.get(reverse('courier:index'))
        self.assertEquals(response.status_code,200)


    def test_mail_view(self):
        response = self.client.get(reverse('courier:mail'))
        self.assertEquals(response.status_code, 200)

    def test_list_mail(self):
        response = self.client.get(reverse('courier:list_mail'))
        lenmail = Mailbag.objects.count()
        context = response.context_data
        self.assertEquals(response.status_code, 200)
        self.assertTrue(response.context_data['list_mail'])
        self.assertEquals(len(context['list_mail']), lenmail)

    def test_Customer_view(self):
        response = self.client.get(reverse('courier:customers'))
        self.assertEquals(response.status_code, 200)

    def test_list_customers(self):
        response = self.client.get(reverse('courier:list_customers'))
        self.assertTrue(response.context_data['customer_list'])


    def test_list_Customer_view(self):
        response = self.client.get(reverse('courier:list_customers'))
        self.assertEquals(response.status_code, 200)

    def test_destination_view(self):
        response = self.client.get(reverse('courier:destination'))
        self.assertEquals(response.status_code, 200)

    def test_list_destinations(self):
        response = self.client.get(reverse('courier:list_destinations'))
        self.assertTrue(response.context_data['destination_list'])
