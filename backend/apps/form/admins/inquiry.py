from io import BytesIO

from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.forms import TextInput
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate

from .util import InputFilter, CustomAdminDateWidget
from django_object_actions import DjangoObjectActions, action

from ..models import Inquiry


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


def get_color(row_number):
    if row_number % 2 == 0:
        return colors.lightgrey
    else:
        return colors.white

class InquiryAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ['inquiry_number', 'status', 'date', 'deadline', 'customer', 'expert', 'category', 'brand']
    list_filter = [InquiryNumber, Customer, 'status', 'inquiry_type', 'assign', 'date', 'deadline']
    search_fields = ['inquiry_number', 'status']
    autocomplete_fields = ['customer', 'expert']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.EmailField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vEmailField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
        models.DateField: {'widget': CustomAdminDateWidget},
    }

    @action(
        label="Save As pdf",  # optional
        description="Save As pdf"  # optional
    )
    def save_as_pdf(self, request, queryset):
        inquiry_number_filter = request.GET.get('Inquiry Number')
        customer_filter = request.GET.get('customer')

        # Apply filters to the queryset
        filtered_queryset = queryset
        if inquiry_number_filter:
            filtered_queryset = filtered_queryset.filter(Q(inquiry_number=inquiry_number_filter))
        if customer_filter:
            filtered_queryset = filtered_queryset.filter(Q(customer=customer_filter))

        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
        elements = []

        header = [field.verbose_name.capitalize() for field in Inquiry._meta.fields]
        data = [header]

        for inquiry in filtered_queryset:
            row = [str(getattr(inquiry, field.name)) for field in inquiry._meta.fields]
            data.append(row)

        table = Table(data)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, (0.3, 0.3, 0.3)),
        ])

        # Apply row color based on index
        for row_index in range(1, len(data)):
            row_color = get_color(row_index)
            style.add('BACKGROUND', (0, row_index), (-1, row_index), row_color)

        table.setStyle(style)
        elements.append(table)

        doc.build(elements)

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="inquiries.pdf"'
        return response


    changelist_actions = ('save_as_pdf',)
