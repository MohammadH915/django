from django.db import models
from django.forms import TextInput
from .util import *


class CompanyName(InputFilter):
    parameter_name = 'CompanyName'
    title = 'CompanyName'

    def queryset(self, request, queryset):
        if self.value() is not None:
            CompanyName = self.value()

            return queryset.filter(
                Q(company_name__icontains=CompanyName)
            )


class ForwarderAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'tel', 'email']
    search_fields = ['company_name']
    list_filter = [CompanyName, Email]

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
    }