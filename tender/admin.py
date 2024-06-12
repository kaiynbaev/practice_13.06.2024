from django.contrib import admin
from .models import Tender, TenderOffer

# Register your models here.

class TenderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'customer', 'contractor', 'price', 'is_active']


class TenderOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'tender', 'user', 'price', 'description', 'is_accepted']


admin.site.register(Tender, TenderAdmin)
admin.site.register(TenderOffer, TenderOfferAdmin)
