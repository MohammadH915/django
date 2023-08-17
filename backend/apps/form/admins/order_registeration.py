from django.contrib import admin

from ..models import OrderRegistration


class InquiryInline(admin.TabularInline):
    model = OrderRegistration.inquiries.through
    extra = 1


class OrderRegistrationAdmin(admin.ModelAdmin):
    inlines = [InquiryInline]
