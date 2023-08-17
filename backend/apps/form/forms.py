from django import forms
from .models import *


class DatePicker(forms.DateInput):
    input_type = 'date'


class PositiveIntegerInput(forms.TextInput):
    input_type = 'number'
    min_value = 0
    step = 1


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'deadline': DatePicker(attrs={'class': 'datepicker'}),
            'category': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'inquiry_type': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'status': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
        widgets = {
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'distributor': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'customer_name': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'replacement': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class TechnicalOfferForm(forms.ModelForm):
    class Meta:
        model = TechnicalOffer
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'delivery_term': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'state': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestToQuotation
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'address_type': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class CommercialOfferForm(forms.ModelForm):
    class Meta:
        model = CommercialOffer
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'qty': forms.NumberInput(attrs={'class': 'positive-integer-input', 'min': 0}),
            'state': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        widgets = {
            'purchase_order_date': DatePicker(attrs={'class': 'datepicker'}),
            'ordering_date_to_supplier': DatePicker(attrs={'class': 'datepicker'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'payeer': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'qty': forms.NumberInput(attrs={'class': 'positive-integer-input', 'min': 0}),
            'state': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class ForwarderForm(forms.ModelForm):
    class Meta:
        model = Forwarder
        fields = '__all__'


class ShippingForm(forms.ModelForm):
    class Meta:
        model = Shipping
        fields = '__all__'
        widgets = {
            'route_choices': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'shipper_choices': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'non_dual_use_letter': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'state': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'booking_date': DatePicker(attrs={'class': 'datepicker'}),
        }


class OrderRegistrationForm(forms.ModelForm):
    class Meta:
        model = OrderRegistration
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'expire_date': DatePicker(attrs={'class': 'datepicker'}),
            'bank_confirmation': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'cbi_confirmation': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'payment_method': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class CustomClearanceForm(forms.ModelForm):
    class Meta:
        model = CustomClearance
        fields = '__all__'
        widgets = {
            'custom': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'documents_send_to_bank': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'documents_send_to_custom': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class BankGuaranteeForm(forms.ModelForm):
    class Meta:
        model = BankGuarantee
        fields = '__all__'
        widgets = {
            'date_of_issue': DatePicker(attrs={'class': 'datepicker'}),
            'cheque_date': DatePicker(attrs={'class': 'datepicker'}),
            'name_of_bank': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'type_of_bank_guarantee': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class FinancialReportForeignForm(forms.ModelForm):
    class Meta:
        model = FinancialReportForeign
        fields = '__all__'
        widgets = {
            'customer_payment_date': DatePicker(attrs={'class': 'datepicker'}),
            'date_of_payment': DatePicker(attrs={'class': 'datepicker'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),

        }


class FinancialReportIRRForm(forms.ModelForm):
    class Meta:
        model = FinancialReportIRR
        fields = '__all__'
        widgets = {
            'customer_payment_date': DatePicker(attrs={'class': 'datepicker'}),
            'date_of_payment': DatePicker(attrs={'class': 'datepicker'}),
            'assign': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class AdvancePaymentSupplierForm(forms.ModelForm):
    class Meta:
        model = AdvancePaymentSupplier
        fields = '__all__'
        widgets = {
            'payment_date': DatePicker(attrs={'class': 'datepicker'}),
            'payeer': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'payment_method': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class BalancePaymentSupplierForm(forms.ModelForm):
    class Meta:
        model = BalancePaymentSupplier
        fields = '__all__'
        widgets = {
            'payment_date': DatePicker(attrs={'class': 'datepicker'}),
            'payeer': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'payment_method': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class ForwarderPaymentForm(forms.ModelForm):
    class Meta:
        model = ForwarderPayment
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'payment_method': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'shipping_method': forms.Select(attrs={'style': 'max-height: 150px;'}),
            'currency': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }


class ClosedForm(forms.ModelForm):
    class Meta:
        model = Closed
        fields = '__all__'
        widgets = {
            'date': DatePicker(attrs={'class': 'datepicker'}),
            'closed_reason': forms.Select(attrs={'style': 'max-height: 150px;'}),
        }
