from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.forms import TextInput
from .util import InputFilter, CustomAdminDateWidget


class InquiryNumber(InputFilter):
    parameter_name = 'Inquiry Number'
    title = 'Inquiry Number'

    def queryset(self, request, queryset):
        if self.value() is not None:
            inquiry_number = self.value()

            return queryset.filter(
                Q(inquiry_number=inquiry_number)
            )


class Customer(InputFilter):
    parameter_name = 'customer'
    title = 'customer'

    def queryset(self, request, queryset):
        if self.value() is not None:
            customer = self.value()

            return queryset.filter(
                Q(customer=customer)
            )


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['inquiry_number', 'status', 'date', 'deadline', 'customer', 'expert', 'category', 'brand']
    list_filter = [InquiryNumber, Customer, 'status', 'inquiry_type', 'assign', 'date', 'deadline']
    autocomplete_fields = ['customer', 'expert']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
        models.DateField: {'widget': CustomAdminDateWidget},
    }
