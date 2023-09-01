from django.db import models
from django.forms import TextInput
from .util import *


class TechnicalOfferAdmin(admin.ModelAdmin):
    list_display = ['technical_number', 'inquiry', 'date', 'customer', 'expert', 'manufacture', 'delivery_term',
                    'assign', 'signatory', 'state']
    search_fields = ['technical_number', 'manufacture']
    list_filter = [Inquiry, Customer, Expert, 'date', 'delivery_term', 'assign', 'signatory', 'state']
    autocomplete_fields = ['customer', 'expert', 'inquiry']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }
