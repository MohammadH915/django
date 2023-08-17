from django.contrib import admin
from django.db import models
from django.db.models import Q
from .util import InputFilter
from django.forms import TextInput


class Company(InputFilter):
    parameter_name = 'Company'
    title = 'Company'

    def queryset(self, request, queryset):
        if self.value() is not None:
            company = self.value()

            return queryset.filter(
                Q(company=company)
            )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company', 'address', 'phone_number']
    search_fields = ['company', 'address', 'phone_number']
    list_filter = [Company]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }
