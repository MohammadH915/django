from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse

from ..models import *


def get_field_choices(model, field_name):
    return model._meta.get_field(field_name).choices


def generic_search_view(request, model, template_name, name, search_view):
    filter_fields = model._meta.fields
    search_url = reverse(search_view)  # Change 'generic_search' to the actual URL name

    if request.method == 'GET':
        query_params = request.GET
        items = model.objects.all()

        for field_name, value in query_params.items():
            if value:
                if hasattr(model, field_name.replace("filter_", "")):
                    kwargs = {field_name.replace("filter_", "") + '__icontains': value}
                    if field_name.replace("filter_", "") == 'inquiry':
                        kwargs = {field_name.replace("filter_", "") + '__inquiry_number__icontains': value}
                    if field_name.replace("filter_", "") == 'customer':
                        kwargs = {field_name.replace("filter_", "") + '__company__icontains': value}
                    if field_name.replace("filter_", "") == 'expert':
                        kwargs = {field_name.replace("filter_", "") + '__name__icontains': value}
                    if field_name.replace("filter_", "") == 'supplier':
                        kwargs = {field_name.replace("filter_", "") + '__company_name__icontains': value}
                    if field_name.replace("filter_", "") == 'forwarder_name':
                        kwargs = {field_name.replace("filter_", "") + '__company_name__icontains': value}
                    if field_name.replace("filter_", "") == 'purchase_order':
                        kwargs = {field_name.replace("filter_", "") + '__purchase_order_number__icontains': value}
                    items = items.filter(**kwargs)
                elif field_name.replace("filter_", "") in ["date_start", "deadline_start"]:
                    try:
                        date_start = datetime.strptime(value, '%Y-%m-%d')
                        items = items.filter(**{field_name.replace("filter_", "") + '__gte': date_start})
                    except ValueError:
                        pass
                elif field_name.replace("filter_", "") in ["date_end", "deadline_end"]:
                    try:
                        date_end = datetime.strptime(value, '%Y-%m-%d')
                        items = items.filter(**{field_name.replace("filter_", "") + '__lte': date_end})
                    except ValueError:
                        pass

        model_fields = model._meta.get_fields()

        items_list = [
            {field.name: getattr(item, field.name) for field in model_fields if hasattr(item, field.name)}
            for item in items
        ]
        paginator = Paginator(items_list, 10)  # 10 items per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'page_obj': page_obj,
            'filter_fields': filter_fields,
            'choices': {field.name: get_field_choices(model, field.name) for field in filter_fields if
                        hasattr(field, 'choices')},
            'search_url': search_url,
            'name': name
        }
        return render(request, template_name, context)

    context = {
        'items': model.objects.all(),
        'filter_fields': filter_fields,
        'choices': {field.name: get_field_choices(model, field.name) for field in filter_fields if
                    hasattr(field, 'choices')},
        'search_url': search_url,
        'name': name
    }
    return render(request, template_name, context)


def inquiry_search(request):
    return generic_search_view(request, Inquiry, 'find.html', 'inquiries', 'inquiry_search')


def supplier_search(request):
    return generic_search_view(request, Supplier, 'find.html', 'suppliers', 'supplier_search')


def quotation_search(request):
    return generic_search_view(request, Quotation, 'find.html', 'quotations', 'quotation_search')


def technicalOffer_search(request):
    return generic_search_view(request, TechnicalOffer, 'find.html', 'technical Offers', 'technicalOffer_search')


def request_search(request):
    return generic_search_view(request, Request, 'find.html', 'requests', 'request_search')


def commercialOffer_search(request):
    return generic_search_view(request, CommercialOffer, 'find.html', 'technical offers', 'commercialOffer_search')


def purchaseOrder_search(request):
    return generic_search_view(request, PurchaseOrder, 'find.html', 'purchease orders', 'purchaseOrder_search')


def forwarder_search(request):
    return generic_search_view(request, Forwarder, 'find.html', 'forwarders', 'forwarder_search')


def shipping_search(request):
    return generic_search_view(request, Shipping, 'find.html', 'shipping', 'shipping_search')


def orderRegistration_search(request):
    return generic_search_view(request, OrderRegistration, 'find.html', 'order registrations',
                               'orderRegistration_search')


def customClearance_search(request):
    return generic_search_view(request, CustomClearance, 'find.html', 'custom clearances', 'customClearance_search')


def customer_search(request):
    return generic_search_view(request, Customer, 'find.html', 'customer', 'customer_search')


def expert_search(request):
    return generic_search_view(request, Expert, 'find.html', 'expert', 'expert_search')


def bankGuarantee_search(request):
    return generic_search_view(request, BankGuarantee, 'find.html', 'bank guarantees', 'bankGuarantee_search')


def financialReportForeign_search(request):
    return generic_search_view(request, FinancialReportForeign, 'find.html', 'financial reports (foreign)',
                               'financialReportForeign_search')


def financialReportIRR_search(request):
    return generic_search_view(request, FinancialReportIRR, 'find.html', 'financial reports (IRR)',
                               'financialReportIRR_search')


def advancePaymentSupplier_search(request):
    return generic_search_view(request, AdvancePaymentSupplier, 'find.html', 'advance payment suppliers',
                               'advancePaymentSupplier_search')


def balancePaymentSupplier_search(request):
    return generic_search_view(request, BalancePaymentSupplier, 'find.html', 'balance payment suppliers',
                               'balancePaymentSupplier_search')


def forwarderPayment_search(request):
    return generic_search_view(request, ForwarderPayment, 'find.html', 'forwarder payments', 'forwarderPayment_search')


def closed_search(request):
    return generic_search_view(request, Closed, 'find.html', 'closed forms', 'closed_search')
