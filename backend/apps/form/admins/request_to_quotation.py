from io import BytesIO
from django.db import models
from django.forms import TextInput
from .util import *
from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape, letter, A4
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from ..models import RequestToQuotation
from django.db.models import Q
from django.http import HttpResponse

def get_color(row_number):
    if row_number % 2 == 0:
        return colors.lightgrey
    else:
        return colors.white


class RequestToQuotationAdmin(admin.ModelAdmin):
    list_display = ['supplier', 'inquiry', 'status', 'customer', 'date']
    search_fields = ['request_number']
    list_filter = [Inquiry, Supplier, 'submission_type', 'sender_company']
    autocomplete_fields = ['supplier', 'inquiry']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vDateField'})},
        models.TextField: {'widget': TextInput(attrs={'autocomplete': 'off', 'class': 'vTextField'})},
        models.DateField: {'widget': CustomAdminDateWidget},
    }

    def status(self, obj):
        return obj.inquiry.status

    status.short_description = 'Status'

    def customer(self, obj):
        return obj.inquiry.customer
    customer.short_description = 'Customer'

    @admin.action
    def save_as_pdf(self, request, queryset):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=landscape(A4), topMargin=15, bottomMargin=15)
        elements = []
        bad = ['note']

        #header = [field.verbose_name.capitalize() for field in RequestToQuotation._meta.fields if field.name not in bad]
        header = []
        for field_name in self.list_display:
            if hasattr(self, field_name):
                header.append(getattr(self, field_name).short_description)
            else:
                header.append(field_name.replace('_', ' ').capitalize())

        data = [header]
        for obj in queryset:
            row = []
            for field_name in self.list_display:
                if hasattr(self, field_name):
                    method = getattr(self, field_name)
                    row.append(method(obj))
                else:
                    # Directly get the field value from the model instance
                    value = getattr(obj, field_name, '')
                    row.append(value)
            data.append(row)

        table = Table(data, repeatRows=1)

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 8),  # Adjusted for horizontal layout
            ('FONTSIZE', (0, 1), (-1, -1), 8),  # Adjusted for horizontal layout
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
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


