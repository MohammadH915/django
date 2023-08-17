from django.contrib import admin
from django.db import models
from django.db.models import Q
from .util import InputFilter
from django.forms import TextInput


class CompanyName(InputFilter):
    parameter_name = 'Company Name'
    title = 'Company Name'

    def queryset(self, request, queryset):
        if self.value() is not None:
            company_name = self.value()

            return queryset.filter(
                Q(company_name=company_name)
            )


class Email(InputFilter):
    parameter_name = 'email'
    title = 'email'

    def queryset(self, request, queryset):
        if self.value() is not None:
            email = self.value()

            return queryset.filter(
                Q(email=email)
            )


class Website(InputFilter):
    parameter_name = 'Website'
    title = 'Website'

    def queryset(self, request, queryset):
        if self.value() is not None:
            website = self.value()

            return queryset.filter(
                Q(website=website)
            )


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email', 'website', 'contact_person', 'company_type']
    search_fields = ['company_name', 'email', 'website', 'contact_person', 'company_type']
    list_filter = [CompanyName, Email, Website, 'company_type']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }
