from io import BytesIO

from django.contrib import admin
from django.db import models
from django.db.models import Q
from django.forms import TextInput
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter, A4
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from .util import InputFilter, CustomAdminDateWidget, Brand

from ..models import Inquiry


class InquiryNumber(InputFilter):
    parameter_name = 'Inquiry Number'
    title = 'Inquiry Number'

    def queryset(self, request, queryset):
        if self.value() is not None:
            inquiry_number = self.value()

            return queryset.filter(
                Q(inquiry_number__icontains=inquiry_number)
            )


class Customer(InputFilter):
    parameter_name = 'customer'
    title = 'customer'

    def queryset(self, request, queryset):
        if self.value() is not None:
            customer = self.value()

            return queryset.filter(
                Q(customer__company__icontains=customer)
            )



class Expert(InputFilter):
    parameter_name = 'Expert'
    title = 'Expert'

    def queryset(self, request, queryset):
        if self.value() is not None:
            expert = self.value()

            return queryset.filter(
                Q(expert__name__icontains=expert)
            )



def get_color(row_number):
    if row_number % 2 == 0:
        return colors.lightgrey
    else:
        return colors.white


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['inquiry_number', 'status', 'inquiry_date', 'to_date', 'co_date', 'po_date', 'customer', 'expert', 'category', 'brand']
    list_filter = [InquiryNumber, Customer, Expert, Brand, 'status', 'inquiry_type', 'assign',  'inquiry_date', 'to_date', 'co_date', 'po_date']
    search_fields = ['inquiry_number', 'status']
    autocomplete_fields = ['customer', 'expert']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.IntegerField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vIntegerField'})},
        models.EmailField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vEmailField'})},
        models.URLField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vURLField'})},
        models.DateField: {'widget': CustomAdminDateWidget},
    }

    @admin.action
    def save_as_pdf(self, request, queryset):
        buffer = BytesIO()
        # Modify this line to set the pagesize to landscape orientation
        doc = SimpleDocTemplate(buffer, pagesize=landscape(A4), topMargin=15, bottomMargin=15)
        elements = []
        bad = ['note', 'brand', 'category', 'product_type']

        header = [field.verbose_name.capitalize() for field in Inquiry._meta.fields if field.name not in bad]
        data = [header]

        for inquiry in queryset:
            row = [str(getattr(inquiry, field.name)) for field in Inquiry._meta.fields if field.name not in bad]
            data.append(row)

        table = Table(data, repeatRows=1)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),  # Adjusted for horizontal layout
            ('FONTSIZE', (0, 1), (-1, -1), 8),  # Adjusted for horizontal layout
            ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])

        # Apply row color based on index (assuming get_color function exists)
        for row_index in range(1, len(data)):
            row_color = get_color(row_index)  # Ensure get_color function is defined
            style.add('BACKGROUND', (0, row_index), (-1, row_index), row_color)

        table.setStyle(style)
        elements.append(table)

        doc.build(elements)

        buffer.seek(0)
        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="inquiries.pdf"'
        return response

    actions = ['save_as_pdf',]
