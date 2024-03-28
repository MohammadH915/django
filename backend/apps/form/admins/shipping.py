from django.db import models
from django.forms import TextInput
from .util import *


class ShippingAdmin(admin.ModelAdmin):
    list_display = ['inquiry', 'forwarder_name', 'consignee', 'country_of_origin', 'delivery_term', 'route', 'booking_date']
    search_fields = ['inquiry_number']
    list_filter = [Inquiry, 'forwarder_name', 'consignee']
    autocomplete_fields = ['inquiry', 'forwarder_name']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }
