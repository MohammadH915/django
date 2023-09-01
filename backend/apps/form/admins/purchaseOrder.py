from django.db import models
from django.forms import TextInput
from .util import *


class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ['purchase_order_number', 'inquiry', 'purchase_order_date', 'state', 'customer', 'expert', 'supplier', 'manufacture', 'currency', 'payeer', 'assign']
    search_fields = ['purchase_order_number']
    list_filter = [Inquiry, Customer, Expert, Supplier, 'currency', 'payeer', 'assign', 'state']
    autocomplete_fields = ['inquiry', 'customer', 'expert', 'supplier']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }