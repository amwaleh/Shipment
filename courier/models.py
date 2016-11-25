from django.db import models
from django.core.urlresolvers import  reverse
# Create your models here.
class Timemixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

class Customers(Timemixin):
    First_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    Email = models.EmailField(unique=True)
    tel = models.CharField(max_length=12)

    def __str__(self):
        return "{} {}".format(self.First_name, self.last_name)

    def get_absolute_url(self):
        return reverse('courier:view_customer',kwargs={'pk':self.pk})


class Destinations(Timemixin):
    location = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "{}".format(self.location)

class Mailbag(Timemixin):
    destination = models.ForeignKey(Destinations)
    recepient = models.CharField(max_length=64)
    sender = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('courier:detail_mail', kwargs={'pk':self.pk})


    def __str__(self):
        return "Delivery to {} for {} from {} ".format(self.destination,
                                                    self.recepient,
                                                    self.sender)

    def Choices(self):
        return Destinations.objects.all()




