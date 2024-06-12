from django.db import models
from account.models import UserModel

# Create your models here.

class Tender(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    customer = models.ForeignKey(UserModel, related_name='tenders_as_customer', on_delete=models.CASCADE)
    contractor = models.ForeignKey(UserModel, related_name='tenders_as_contractor', null=True, blank=True, on_delete=models.CASCADE)
    offer = models.ManyToManyField(UserModel, related_name='tender_offers', blank=True)  # Поле, хранящее запросы на сделку
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TenderOffer(models.Model):
    tender = models.ForeignKey(Tender, related_name='offers', on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, related_name='offers', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_accepted = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Offer for {self.tender.title} by {self.user.username}"