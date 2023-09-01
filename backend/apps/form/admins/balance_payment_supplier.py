from django.db import models
from django.forms import TextInput
from .util import *


class BalancePaymentSupplierAdmin(admin.ModelAdmin):
    list_display = ['inquiry', 'supplier', 'amount', 'payment_date', 'currency', 'ex_rate_to_aed', 'payee', 'payeer', 'payment_method']
    search_fields = ['inquiry']
    list_filter = [Inquiry, Supplier, 'currency', 'payeer', 'payment_method']
    autocomplete_fields = ['supplier', 'inquiry']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }