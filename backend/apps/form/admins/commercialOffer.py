from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.forms import TextInput
from .util import InputFilter, CustomAdminDateWidget
from .inquiry import Customer


class CommercialOfferNumber(InputFilter):
    parameter_name = 'Commercial Offer Number'
    title = 'Commercial Offer Number'

    def queryset(self, request, queryset):
        if self.value() is not None:
            CommercialOffer_number = self.value()

            return queryset.filter(
                Q(CommercialOffer_number=CommercialOffer_number)
            )


class Inquiry(InputFilter):
    parameter_name = 'Inquiry'
    title = 'Inquiry'

    def queryset(self, request, queryset):
        if self.value() is not None:
            inquiry = self.value()

            return queryset.filter(
                Q(inquiry=inquiry)
            )


class Expert(InputFilter):
    parameter_name = 'Expert'
    title = 'Expert'

    def queryset(self, request, queryset):
        if self.value() is not None:
            expert = self.value()

            return queryset.filter(
                Q(expert=expert)
            )


class CommercialOfferAdmin(admin.ModelAdmin):
    list_display = ['CommercialOffer_number', 'inquiry', 'date', 'customer', 'expert']
    list_filter = [CommercialOfferNumber, Customer, Inquiry, 'date', Expert]
    autocomplete_fields = ['customer', 'expert', 'inquiry']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.EmailField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vEmailField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
        models.DateField: {'widget': CustomAdminDateWidget},
    }
