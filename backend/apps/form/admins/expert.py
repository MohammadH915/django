from django.contrib import admin
from django.db import models
from django.db.models import Q
from .util import InputFilter
from django.forms import TextInput
from .inquiry import Customer


class Name(InputFilter):
    parameter_name = 'Name'
    title = 'Name'

    def queryset(self, request, queryset):
        if self.value() is not None:
            name = self.value()

            return queryset.filter(
                Q(name=name)
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


class ExpertAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'customer']
    search_fields = ['name', 'email', 'customer']
    list_filter = [Name, Email, Customer]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
    }
