from django.contrib import admin
from django.contrib.admin.widgets import AdminDateWidget
from django.db.models import Q


class InputFilter(admin.SimpleListFilter):
    template = 'input_filter.html'

    def lookups(self, request, model_admin):
        # Dummy, required to show the filter.
        return ((),)

    def choices(self, changelist):
        all_choice = next(super().choices(changelist))
        all_choice['query_parts'] = (
            (k, v)
            for k, v in changelist.get_filters_params().items()
            if k != self.parameter_name
        )
        yield all_choice


class CustomAdminDateWidget(AdminDateWidget):
    def __init__(self, attrs=None, format=None):
        if attrs is None:
            attrs = {}
        attrs.update({'autocomplete': 'off', 'class': 'vDateField'})
        super().__init__(attrs=attrs, format=format)


class Customer(InputFilter):
    parameter_name = 'customer'
    title = 'customer'

    def queryset(self, request, queryset):
        if self.value() is not None:
            customer = self.value()

            return queryset.filter(
                Q(customer__icontains=customer)
            )


class Expert(InputFilter):
    parameter_name = 'Expert'
    title = 'Expert'

    def queryset(self, request, queryset):
        if self.value() is not None:
            expert = self.value()

            return queryset.filter(
                Q(expert__icontains=expert)
            )


class Inquiry(InputFilter):
    parameter_name = 'Inquiry'
    title = 'Inquiry'

    def queryset(self, request, queryset):
        if self.value() is not None:
            inquiry = self.value()
            return queryset.filter(
                Q(inquiry__inquiry_number__icontains=inquiry)
            )


class CompanyName(InputFilter):
    parameter_name = 'Company Name'
    title = 'Company Name'

    def queryset(self, request, queryset):
        if self.value() is not None:
            company_name = self.value()

            return queryset.filter(
                Q(company_name__icontains=company_name)
            )


class Email(InputFilter):
    parameter_name = 'email'
    title = 'email'

    def queryset(self, request, queryset):
        if self.value() is not None:
            email = self.value()

            return queryset.filter(
                Q(email__icontains=email)
            )


class Website(InputFilter):
    parameter_name = 'Website'
    title = 'Website'

    def queryset(self, request, queryset):
        if self.value() is not None:
            website = self.value()

            return queryset.filter(
                Q(website__icontains=website)
            )


class Supplier(InputFilter):
    parameter_name = 'Supplier'
    title = 'Supplier'

    def queryset(self, request, queryset):
        if self.value() is not None:
            supplier = self.value()

            return queryset.filter(
                Q(supplier__icontains=supplier)
            )


class RequestId(InputFilter):
    parameter_name = 'Request Id'
    title = 'RequestId'

    def queryset(self, request, queryset):
        if self.value() is not None:
            RequestId = self.value()

            return queryset.filter(
                Q(request_id__icontains=RequestId)
            )


class Brand(InputFilter):
    parameter_name = 'Brand'
    title = 'Brand'

    def queryset(self, request, queryset):
        if self.value() is not None:
            brand = self.value()

            return queryset.filter(
                Q(brand__icontains=brand)
            )
