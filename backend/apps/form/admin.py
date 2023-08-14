from django.contrib import admin
from .models import Inquiry, Supplier, Quotation, Request

admin.site.register(Inquiry)
admin.site.register(Supplier)
admin.site.register(Quotation)
admin.site.register(Request)