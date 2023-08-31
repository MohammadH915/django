import random

from django.db import models

assign_choices = (
    ('Manager', 'Manager'),
    ('Technical Team No.1', 'Technical Team No.1'),
    ('Technical Team No.2', 'Technical Team No.2'),
    ('Commercial Team No.1', 'Commercial Team No.1'),
    ('Commercial Team No.2', 'Commercial Team No.2'),
    ('Sales Team No.1', 'Sales Team No.1'),
    ('Sales Team No.2', 'Sales Team No.2'),
    ('Administrative Team No.1', 'Administrative Team No.1'),
)

payeer_choices = [
    ('Walid', 'Walid'),
    ('Cash', 'Cash'),
    ('Lalik', 'Lalik'),
    ('Pineapple', 'Pineapple'),
    ('Pantatec', 'pantatec'),
]

company_choices = [
    ('Pineapple', 'Pineapple'),
    ('Pantatec', 'pantatec'),
    ('Payanik', 'Payanik'),
    ('Other', 'Other'),
]

INQUIRY_TYPES = (
    ('Tender Guarantee', 'Tender Guarantee'),
    ('Payment Guarantee', 'Payment Guarantee'),
    ('Performance Guarantee', 'Performance Guarantee')
)

BANK_NAMES = (
    ('Pasargad', 'Pasargad'),
    ('Meli', 'Meli'),
    ('Mellat', 'Mellat')
)

CURRENCY_CHOICES = (
    ('AED', 'AED'),
    ('EURO', 'EURO'),
    ('USD', 'USD'),
    ('GP', 'GP'),
)

PAYMENT_METHOD = (
    ('Cash', 'Cash'),
    ('ATM', 'ATM'),
    ('Online', 'Online'),
    ('Bank transfer', 'Bank transfer'),
)

Signatory_CHOICES = (
    ('Manager', 'Manager'),
    ('Tec No.1', 'Tec No.1'),
    ('Tec No.2', 'Tec No.2'),
    ('Tec No.3', 'Tec No.3'),
    ('Com No.1', 'Com No.1'),
    ('Com No.2', 'Com No.2'),
    ('Com No.3', 'Com No.3'),
    ('Sales No.2', 'Sales No.2'),
    ('Sales No.3', 'Sales No.3'),
    ('Other', 'Other'),
)

Signatory_CHOICES = (
    ('DDP', 'DDP'),
    ('CPT', 'CPT'),
    ('CFR', 'CFR'),
)


class Customer(models.Model):
    company = models.CharField(max_length=100, primary_key=True)
    address = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=500)
    economical_code = models.CharField(max_length=20)
    national_ID = models.CharField(max_length=500)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company


class Expert(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'customer'], name='unique_expert_per_customer')
        ]

    def __str__(self):
        return self.name


class Inquiry(models.Model):
    inquiry_number = models.CharField(max_length=20, primary_key=True)
    status_choices = (
        ('Inquiry', 'Inquiry'),

        ('Request', 'Request'),

        ('Quotation', 'Quotation'),
        ('Technical offer', 'Technical offer'),
        ('Technical Confirmation', 'Technical Confirmation'),

        ('Technical Revise', 'Technical Revise'),
        ('Commercial offer', 'Commercial offer'),
        ('CO Win', 'CO Win'),

        ('CO Lose', 'CO Lose'),
        ('Close', 'Close'),
        ('Purchase Order', 'Purchase Order'),

        ('Placing the Order', 'Placing the Order'),
        ('Po Lead Time', 'Po Lead Time'),

        ('Shipping', 'Shipping'),
        ('Delivery of Documents', 'Delivery of Documents'),

        ('Custom', 'Custom'),
        ('Custome Clearance', 'Custome Clearance'),
        ('Bank Documents', 'Bank Documents'),

        ('Decline', 'Decline'),
        ('Close', 'Close'),
    )
    status = models.CharField(max_length=50, choices=status_choices)
    inquiry_type_choices = (
        ('Tender', 'Tender'),
        ('Indent', 'Indent'),
    )
    inquiry_type = models.CharField(max_length=10, choices=inquiry_type_choices)
    date = models.DateField()
    deadline = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    email_address = models.EmailField()
    category_choices = (
        ('Mechanic', 'Mechanic'),
        ('Instrument', 'Instrument'),
        ('Electrical', 'Electrical'),
    )
    category = models.CharField(max_length=20, choices=category_choices)
    brand = models.CharField(max_length=100)
    product_choices = (
        ('Spare Part', 'Spare Part'),
        ('Complete Assembly', 'Complete Assembly'),
    )
    product_type = models.CharField(max_length=100, choices=product_choices)
    assign = models.CharField(max_length=30, choices=assign_choices)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.inquiry_number


class Supplier(models.Model):
    company_name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField()
    website = models.URLField()
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    country_of_origin = models.CharField(max_length=50)
    company_type = models.CharField(choices=[('Distributer', 'Distributer'), ('Manufacturer', 'Manufacturer'), ('Trading Company', 'Trading Company')], max_length=50)
    brand_no_1 = models.CharField(max_length=100, blank=True)
    brand_no_2 = models.CharField(max_length=100, null=True, blank=True)
    brand_no_3 = models.CharField(max_length=100, null=True, blank=True)
    brand_no_4 = models.CharField(max_length=100, null=True, blank=True)
    brand_no_5 = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class RequestToQuotation(models.Model):
    request_number = models.CharField(max_length=10, primary_key=True, unique=True, editable=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, to_field='company_name')
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number')
    submission_type = models.CharField(max_length=50, choices=[
        ('Email', 'Email'),
        ('WebSite', 'WebSite'),
    ])
    address = models.CharField(null=True, blank=True, max_length=200)
    phone_number = models.CharField(null=True, blank=True, max_length=20)
    sender_company = models.CharField(max_length=50, choices=company_choices)
    date = models.DateField()
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        if self.inquiry and self.inquiry.status == 'Inquiry':
            self.inquiry.status = 'Request'  # Change the address_type to 'Request'
            self.inquiry.save()

    def save(self, *args, **kwargs):
        if not self.request_number:
            # Generate a random request number
            self.request_number = ''.join(random.choices('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=10))

        self.update_inquiry_status()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.inquiry.inquiry_number + " - " + self.supplier.company_name + " - " + self.request_number


class Quotation(models.Model):
    quotation_number = models.CharField(primary_key=True, max_length=50)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, to_field='company_name')
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number')
    request_id = models.ForeignKey(RequestToQuotation, on_delete=models.CASCADE, to_field='request_number')
    date = models.DateField()
    brand = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=50)
    delivery_time = models.CharField(max_length=100, null=True, blank=True)
    delivery_term = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    validity = models.CharField(max_length=100)
    replacement = models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    assign = models.CharField(max_length=30, choices=assign_choices)
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        if self.inquiry and self.inquiry.status == 'Request':
            self.inquiry.status = 'Quotation'  # Change the address_type to 'Request'
            # You might want to add more logic here to update other fields
            self.inquiry.save()

    def save(self, *args, **kwargs):
        self.update_inquiry_status()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.quotation_number


class TechnicalOffer(models.Model):
    technical_number = models.CharField(primary_key=True, max_length=100)
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number')
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    manufacture = models.CharField(max_length=200)
    delivery_term = models.CharField(max_length=50, choices=[
        ('DDP', 'DDP'),
        ('CPT', 'CPT'),
        ('CFR', 'CFR'),
    ])
    assign = models.CharField(max_length=30, choices=assign_choices)
    signatory = models.CharField(max_length=30, choices=Signatory_CHOICES)
    state = models.CharField(max_length=50, choices=[
        ('Offer', 'Offer'),
        ('Revise', 'Revise'),
        ('Pending to Commercial', 'Pending to Commercial'),
        ('Hold', 'Hold'),
    ], default='Offer')
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        if self.inquiry:
            if self.state == 'offer':
                self.inquiry.status = 'Technical offer'  # Change the address_type to 'Request'
            if self.state == 'Confirmation':
                self.inquiry.status = 'Technical Confirmation'  # Change the address_type to 'Request'
            if self.state == 'Revise':
                self.inquiry.status = 'Technical Revise'  # Change the address_type to 'Request'

            self.inquiry.save()

    def save(self, *args, **kwargs):
        self.update_inquiry_status()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.technical_number


class CommercialOffer(models.Model):
    CommercialOffer_number = models.CharField(max_length=100)
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    manufacture = models.CharField(max_length=100)
    delivery_term = models.CharField(max_length=100)
    delivery_time = models.CharField(max_length=100)
    validity = models.CharField(max_length=100)
    total_amount = models.FloatField()
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    term_of_payment = models.CharField(max_length=100)
    signatory = models.CharField(max_length=30, choices=Signatory_CHOICES)
    assign = models.CharField(max_length=30, choices=assign_choices)
    state = models.CharField(max_length=50, choices=[
        ('Offer', 'Offer'),
        ('Win', 'Win'),
        ('Lose', 'Lose'),
        ('Re-Tender', 'Re-Tender'),
        ('Hold', 'Hold'),
    ], default='Offer')
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        if self.inquiry:
            if self.state == 'offer':
                self.inquiry.status = 'Commercial offer'  # Change the address_type to 'Request'
            if self.state == 'win':
                self.inquiry.status = 'CO Win'  # Change the address_type to 'Request'
            if self.state == 'lose':
                self.inquiry.status = 'CO Lose'  # Change the address_type to 'Request'

            self.inquiry.save()

    def save(self, *args, **kwargs):
        self.update_inquiry_status()

        super().save(*args, **kwargs)


class PurchaseOrder(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE)
    purchase_order_number = models.CharField(max_length=50, primary_key=True)
    purchase_order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE)
    manufacture = models.CharField(max_length=100)
    qty = models.PositiveIntegerField()
    purchase_order_value = models.FloatField()
    delivery_time = models.CharField(max_length=100)
    delivery_term = models.CharField(max_length=100)
    term_of_payment = models.CharField(max_length=100)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    brand = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, to_field='company_name')
    ordering_date_to_supplier = models.DateField()
    supplier_delivery_term = models.CharField(max_length=100)
    supplier_term_of_payment = models.CharField(max_length=100)
    payeer = models.CharField(max_length=50, choices=payeer_choices)
    duration_of_contract = models.CharField(max_length=100, null=True, blank=True)
    prepayment = models.FloatField()
    bank_guarantee_number = models.CharField(max_length=50)
    assign = models.CharField(max_length=30, choices=assign_choices)

    state = models.CharField(max_length=50, choices=[
        ('Ordering', 'Ordering'),
        ('Placing the Order', 'Placing the Order'),
        ('Po Lead Time', 'Po Lead Time'),
    ], default='Ordering')
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        if self.inquiry:
            if self.state == 'Ordering':
                self.inquiry.status = 'Purchase Order'  # Change the address_type to 'Request'
            if self.state == 'Placing the Order':
                self.inquiry.status = 'Placing the Order'  # Change the address_type to 'Request'
            if self.state == 'Po Lead Time':
                self.inquiry.status = 'Po Lead Time'  # Change the address_type to 'Request'

    def save(self, *args, **kwargs):
        self.update_inquiry_status()

        super().save(*args, **kwargs)


class Forwarder(models.Model):
    company_name = models.CharField(max_length=100, primary_key=True)
    tel = models.CharField(max_length=20)
    email = models.EmailField()
    contact_person_1 = models.CharField(max_length=100)
    contact_person_2 = models.CharField(max_length=100, null=True, blank=True)
    contact_person_3 = models.CharField(max_length=100, null=True, blank=True)
    contact_person_4 = models.CharField(max_length=100, null=True, blank=True)
    mob_number_1 = models.CharField(max_length=20)
    mob_number_2 = models.CharField(max_length=20, null=True, blank=True)
    mob_number_3 = models.CharField(max_length=20, null=True, blank=True)
    mob_number_4 = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField()
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class Shipping(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, primary_key=True)
    forwarder_name = models.ForeignKey(Forwarder, on_delete=models.CASCADE, to_field='company_name')
    consignee = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    delivery_term = models.CharField(max_length=100)
    route_choices = [
        ('Transit', 'Transit'),
        ('Sea Freight', 'Sea Freight'),
        ('Air Freight', 'Air Freight'),
    ]
    route = models.CharField(max_length=100, choices=route_choices)
    booking_date = models.DateField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimension = models.CharField(max_length=100)
    packing = models.CharField(max_length=100)
    non_dual_use_letter = models.BooleanField(choices=[(True, 'Needed'), (False, 'NO')])
    tracking_number = models.CharField(max_length=100)
    ups_label = models.CharField(max_length=100)
    bill_of_lading_no = models.CharField(max_length=100)
    shipper_choices = [
        ('NRA', 'NRA'),
        ('MOSKOT', 'MOSKOT'),
        ('LALIK', 'LALIK'),
    ]
    shipper = models.CharField(max_length=100, choices=shipper_choices)
    clause_transit = models.CharField(max_length=100)
    custom = models.CharField(max_length=100)
    freight_charge = models.DecimalField(max_digits=10, decimal_places=2)
    term_of_payment_to_forwarder = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100)
    assign = models.CharField(max_length=30, choices=assign_choices)
    state = models.CharField(max_length=50, choices=[
        ('In Progres', 'In Progres'),
        ('Delivery of Documents', 'Delivery of Documents'),
        ('Custom', 'Custom'),
    ], default='In Progres')
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        if self.state == 'In Progres':
            self.inquiry.status = 'Shipping'
        if self.state == 'Delivery of Documents':
            self.inquiry.status = 'Delivery of Documents'
        if self.state == 'Custom':
            self.inquiry.status = 'Custom'

        self.inquiry.save()

    def save(self, *args, **kwargs):
        self.update_inquiry_status()

        super().save(*args, **kwargs)


class OrderRegistration(models.Model):
    registration_number = models.CharField(max_length=20, primary_key=True)
    file_number = models.CharField(max_length=100)
    proforma_invoice_number = models.CharField(max_length=100)
    date = models.DateField()
    expire_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    inquiries = models.ManyToManyField(Inquiry, related_name='order_registrations')

    hs_code_1 = models.CharField(max_length=100)
    hs_code_2 = models.CharField(max_length=100, null=True, blank=True)
    hs_code_3 = models.CharField(max_length=100, null=True, blank=True)
    hs_code_4 = models.CharField(max_length=100, null=True, blank=True)
    hs_code_5 = models.CharField(max_length=100, null=True, blank=True)
    bank_confirmation = models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], max_length=20)
    cbi_confirmation = models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], max_length=20)
    payment_method = models.CharField(max_length=100, choices=PAYMENT_METHOD)
    shipper = models.CharField(max_length=100)
    exchange_office = models.CharField(max_length=100)
    payeer = models.CharField(max_length=100, choices=payeer_choices, null=True, blank=True)
    payment_tools_number = models.CharField(max_length=100, null=True, blank=True)
    assign = models.CharField(max_length=100, choices=assign_choices, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Order Registration {self.registration_number}"


class CustomClearance(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number')
    custom_choices = [
        ('IKA', 'IKA'),
        ('Tehran', 'Tehran'),
        ('Payam', 'Payam'),
        ('Sahlan', 'Sahlan'),
        ('Shahid Rajaee', 'Shahid Rajaee'),
        ('Bahonar', 'Bahonar'),
    ]
    custom = models.CharField(max_length=20, choices=custom_choices)
    contractor = models.CharField(max_length=100)
    order_registration_number = models.CharField(max_length=50)
    invoice_number = models.CharField(max_length=50)
    packing_number = models.CharField(max_length=50)
    amount = models.FloatField()
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    hs_code = models.CharField(max_length=20)
    cottage_number = models.CharField(max_length=20)
    documents_send_to_bank = models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], max_length=20)
    documents_send_to_custom = models.BooleanField(choices=[(True, 'YES'), (False, 'NO')], max_length=20)
    bank_expert = models.CharField(null=True, blank=True, max_length=100)
    shipper = models.CharField(max_length=100)
    custom_duty = models.FloatField(null=True, blank=True)
    custom_vat = models.FloatField(null=True, blank=True)
    contractor_cost = models.FloatField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        self.inquiry.status = 'Custome Clearance'
        self.inquiry.save()

    def save(self, *args, **kwargs):
        self.update_inquiry_status()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Inquiry Number: {self.inquiry}, Custom: {self.custom}"


class BankGuarantee(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    name_of_bank = models.CharField(max_length=100, choices=BANK_NAMES)
    bank_guarantee_number = models.CharField(max_length=50)
    beneficiary = models.CharField(max_length=200)
    guarantee_amount = models.DecimalField(max_digits=15, decimal_places=2)
    cheque_number = models.CharField(max_length=50)
    cheque_date = models.DateField()
    date_of_issue = models.DateField()
    validity = models.DateField()
    type_of_bank_guarantee = models.CharField(max_length=50, choices=INQUIRY_TYPES)
    assign = models.CharField(max_length=100, choices=assign_choices, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_of_bank} - {self.bank_guarantee_number}"


class FinancialReportForeign(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, to_field='purchase_order_number')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')

    customer_payment_date = models.DateField()
    amount_received = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    date_of_payment = models.DateField()
    bank_charge_walid = models.CharField(max_length=50)
    bank_fee_customer = models.DecimalField(max_digits=15, decimal_places=2)
    term_of_payment = models.CharField(max_length=50)
    cheque_no = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    tracking_number = models.CharField(max_length=50)
    contact_value = models.DecimalField(max_digits=15, decimal_places=2)
    buying_value = models.DecimalField(max_digits=15, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=15, decimal_places=2)
    commission = models.DecimalField(max_digits=15, decimal_places=2)
    extra_charge = models.DecimalField(max_digits=15, decimal_places=2)
    benefit = models.DecimalField(max_digits=15, decimal_places=2)
    assign = models.CharField(max_length=50, choices=assign_choices)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.purchase_order_number


class FinancialReportIRR(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, to_field='purchase_order_number')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    customer_payment_date = models.DateField()
    amount_received = models.DecimalField(max_digits=15, decimal_places=2)
    registration_number = models.CharField(max_length=50)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
    bank_information = models.TextField()
    account_number = models.CharField(max_length=50)
    term_of_payment = models.CharField(max_length=50)
    cheque_no = models.CharField(max_length=50)
    bank_of_customer = models.CharField(max_length=100)
    date_of_payment = models.DateField()
    invoice_number = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=50)
    contact_value = models.DecimalField(max_digits=15, decimal_places=2)
    buying_value = models.DecimalField(max_digits=15, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=15, decimal_places=2)
    custom_clearance_cost = models.DecimalField(max_digits=15, decimal_places=2)
    customs_broker_salary = models.CharField(max_length=100)
    commission = models.DecimalField(max_digits=15, decimal_places=2)
    registration_order_cost = models.DecimalField(max_digits=15, decimal_places=2)
    extra_charge = models.DecimalField(max_digits=15, decimal_places=2)
    benefit = models.DecimalField(max_digits=15, decimal_places=2)
    assign = models.CharField(max_length=50, choices=assign_choices)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.purchase_order_number


class AdvancePaymentSupplier(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, to_field='company_name')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    ex_rate_to_aed = models.DecimalField(max_digits=10, decimal_places=4)
    payee = models.CharField(max_length=100)
    payeer = models.CharField(max_length=100, choices=payeer_choices, null=True, blank=True)
    beneficiary = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    origin_bank = models.CharField(max_length=100, null=True, blank=True)
    tracing_number = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.inquiry)


class BalancePaymentSupplier(models.Model):
    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, to_field='company_name')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    ex_rate_to_aed = models.DecimalField(max_digits=10, decimal_places=4)
    payee = models.CharField(max_length=100)
    payeer = models.CharField(max_length=100, choices=payeer_choices, null=True, blank=True)
    beneficiary = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    origin_bank = models.CharField(max_length=100, null=True, blank=True)
    tracing_number = models.CharField(max_length=50, null=True, blank=True)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.inquiry)


class ForwarderPayment(models.Model):
    SHIPPING_METHOD_CHOICES = (
        ('Ship', 'Ship'),
        ('Air', 'Air'),
        ('Truck', 'Truck'),
    )

    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    forwarder_name = models.ForeignKey(Forwarder, on_delete=models.CASCADE, to_field='company_name')
    shipping_method = models.CharField(max_length=10, choices=SHIPPING_METHOD_CHOICES)
    date = models.DateField()
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    ex_rate_to_aed = models.DecimalField(max_digits=10, decimal_places=4)
    ex_rate_to_rials = models.DecimalField(max_digits=10, decimal_places=4)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    contact_person = models.CharField(null=True, blank=True, max_length=100)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.inquiry)


class Closed(models.Model):
    INQUIRY_CHOICES = (
        ('Lost', 'Lost'),
        ('Decline', 'Decline'),
        ('Supplier Reject', 'Supplier Reject'),
        ('Canceled by Customer', 'Canceled by Customer'),
        ('End User Destination', 'End User Destination'),
        ('Other', 'Other'),
    )

    inquiry = models.OneToOneField(Inquiry, on_delete=models.CASCADE, to_field='inquiry_number',
                                   primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, to_field='company')
    date = models.DateField()
    closed_reason = models.CharField(max_length=50, choices=INQUIRY_CHOICES)
    note = models.TextField(null=True, blank=True)

    def update_inquiry_status(self):
        self.inquiry.status = 'Close'  # Change the address_type to 'Request'
        self.inquiry.save()

    def save(self, *args, **kwargs):
        self.update_inquiry_status()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.inquiry)
