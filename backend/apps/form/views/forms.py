from django.shortcuts import render, redirect
from ..forms import *


def base_form_view(request, form_class, form_name):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Replace 'success_url_name' with the URL name for the success page
    else:
        form = form_class()
    return render(request, 'form.html', {'form': form, 'name': form_name})


def inquiry_form_view(request):
    return base_form_view(request, InquiryForm, 'Inquiry')


def supplier_form_view(request):
    return base_form_view(request, SupplierForm, 'Supplier')


def quotation_form_view(request):
    return base_form_view(request, QuotationForm, 'Quotation')


def technicalOffer_form_view(request):
    return base_form_view(request, TechnicalOfferForm, 'Technical Offer')


def request_form_view(request):
    return base_form_view(request, RequestForm, 'Request')


def commercialOffer_form_view(request):
    return base_form_view(request, CommercialOfferForm, 'Commercial Offer')


def purchaseOrder_form_view(request):
    return base_form_view(request, PurchaseOrderForm, 'Purchase Order')


def forwarder_form_view(request):
    return base_form_view(request, ForwarderForm, 'Forwarder')


def shipping_form_view(request):
    return base_form_view(request, ShippingForm, 'Shipping')


def orderRegistration_form_view(request):
    return base_form_view(request, OrderRegistrationForm, 'Order Registration')


def customClearance_form_view(request):
    return base_form_view(request, CustomClearanceForm, 'Custom Clearance')


def customer_form_view(request):
    return base_form_view(request, CustomerForm, 'Customer')


def expert_form_view(request):
    return base_form_view(request, ExpertForm, 'Expert')


def bankGuarantee_form_view(request):
    return base_form_view(request, BankGuaranteeForm, 'BankGuarantee')


def financialReportForeign_form_view(request):
    return base_form_view(request, FinancialReportForeignForm, 'FinancialReportForeign')


def financialReportIRR_form_view(request):
    return base_form_view(request, FinancialReportIRRForm, 'FinancialReportIRR')


def advancePaymentSupplier_form_view(request):
    return base_form_view(request, AdvancePaymentSupplierForm, 'AdvancePaymentSupplier')


def balancePaymentSupplier_form_view(request):
    return base_form_view(request, BalancePaymentSupplierForm, 'BalancePaymentSupplier')


def forwarderPayment_form_view(request):
    return base_form_view(request, ForwarderPaymentForm, 'ForwarderPayment')


def closed_form_view(request):
    return base_form_view(request, ClosedForm, 'ClosedForm')
