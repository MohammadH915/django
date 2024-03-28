from .models import *
from django.contrib import admin
from .admins import *
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin


class MyAdminSite(AdminSite):
    def get_app_list(self, request, app_label=None):
        app_dict = self._build_app_dict(request, app_label)

        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        custom_order = {
            'Inquiry': 1,
            'Expert': 2,
            'Customer': 3,
            'Supplier': 4,
            'RequestToQuotation': 5,
            'Quotation': 6,
            'TechnicalOffer': 7,
            'CommercialOffer': 8,
            'PurchaseOrder': 9,
            'Forwarder': 10,
            'Shipping': 11,
            'OrderRegistration': 12,
            'CustomClearance': 13,
            'BankGuarantee': 14,
            'FinancialReportForeign': 15,
            'FinancialReportIRR': 16,
            'AdvancePaymentSupplier': 17,
            'BalancePaymentSupplier': 18,
            'ForwarderPayment': 19,
            'Closed': 20,
        }

        for app in app_list:
            app['models'].sort(key=lambda x: custom_order.get(x['object_name'], 0))

        return app_list


admin_site = MyAdminSite(name='myadmin')

admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin)
admin_site.site_header = "Pantatec"
admin_site.site_title = "Pantatec"
admin_site.index_title = "Pantatec"
admin_site.register(Customer, CustomerAdmin)
admin_site.register(Expert, ExpertAdmin)
admin_site.register(Inquiry, InquiryAdmin)
admin_site.register(Supplier, SupplierAdmin)
admin_site.register(RequestToQuotation, RequestToQuotationAdmin)
admin_site.register(Quotation, QuotationAdmin)
admin_site.register(TechnicalOffer, TechnicalOfferAdmin)
admin_site.register(CommercialOffer, CommercialOfferAdmin)
admin_site.register(PurchaseOrder, PurchaseOrderAdmin)
admin_site.register(Forwarder, ForwarderAdmin)
admin_site.register(Shipping, ShippingAdmin)
admin_site.register(OrderRegistration)
admin_site.register(CustomClearance)
admin_site.register(BankGuarantee)
admin_site.register(FinancialReportForeign)
admin_site.register(FinancialReportIRR)
admin_site.register(AdvancePaymentSupplier, AdvancePaymentSupplierAdmin)
admin_site.register(BalancePaymentSupplier, BalancePaymentSupplierAdmin)
admin_site.register(ForwarderPayment)
admin_site.register(Closed)

