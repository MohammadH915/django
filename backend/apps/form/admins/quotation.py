from django.db import models
from django.forms import TextInput
from .util import *


class QuotationAdmin(admin.ModelAdmin):
    list_display = ['quotation_number', 'inquiry', 'supplier', 'request_id', 'date', 'brand', 'customer', 'assign']
    search_fields = ['quotation_number']
    list_filter = [Inquiry, Supplier, Customer, RequestId, Brand, 'currency', 'replacement', 'assign']
    autocomplete_fields = ['supplier', 'inquiry', 'request_id', 'customer']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }