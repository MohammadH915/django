from .models import *
from django.contrib import admin
from .admins import *

admin.site.site_header = "Pantatec"
admin.site.site_title = "Pantatec"
admin.site.index_title = "Pantatec"
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(RequestToQuotation)
admin.site.register(Quotation)
admin.site.register(TechnicalOffer)
admin.site.register(CommercialOffer)
admin.site.register(PurchaseOrder)
admin.site.register(Forwarder)
admin.site.register(Shipping)
admin.site.register(OrderRegistration)
admin.site.register(CustomClearance)
admin.site.register(BankGuarantee)
admin.site.register(FinancialReportForeign)
admin.site.register(FinancialReportIRR)
admin.site.register(AdvancePaymentSupplier)
admin.site.register(BalancePaymentSupplier)
admin.site.register(ForwarderPayment)
admin.site.register(Closed)