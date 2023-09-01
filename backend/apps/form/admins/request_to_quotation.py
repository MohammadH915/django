from django.db import models
from django.forms import TextInput
from .util import *


class RequestToQuotationAdmin(admin.ModelAdmin):
    list_display = ['request_number', 'supplier', 'inquiry', 'submission_type', 'sender_company']
    search_fields = ['request_number']
    list_filter = [Inquiry, Supplier, 'submission_type', 'sender_company']
    autocomplete_fields = ['supplier', 'inquiry']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }