# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApplyArInvoiceWithSourceRequestAddressCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceRequestAddressCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequestAddress(TeaModel):
    def __init__(self, address_id=None, app_code=None, city=None, country=None, creator=None, customer=None,
                 detailed_address=None, district=None, encrypt_props=None, fixed_number=None, full_address=None, is_default=None,
                 is_effective=None, language=None, mobile_number=None, province=None, recipient_name=None, related_id=None,
                 related_system=None, sign=None, street=None, uuid=None, zip_code=None):
        self.address_id = address_id  # type: str
        self.app_code = app_code  # type: str
        self.city = city  # type: str
        self.country = country  # type: str
        self.creator = creator  # type: str
        self.customer = customer  # type: ApplyArInvoiceWithSourceRequestAddressCustomer
        self.detailed_address = detailed_address  # type: str
        self.district = district  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.fixed_number = fixed_number  # type: str
        self.full_address = full_address  # type: str
        self.is_default = is_default  # type: bool
        self.is_effective = is_effective  # type: bool
        self.language = language  # type: str
        self.mobile_number = mobile_number  # type: str
        self.province = province  # type: str
        self.recipient_name = recipient_name  # type: str
        self.related_id = related_id  # type: str
        self.related_system = related_system  # type: str
        self.sign = sign  # type: str
        self.street = street  # type: str
        self.uuid = uuid  # type: str
        self.zip_code = zip_code  # type: str

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceRequestAddress, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.city is not None:
            result['City'] = self.city
        if self.country is not None:
            result['Country'] = self.country
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.detailed_address is not None:
            result['DetailedAddress'] = self.detailed_address
        if self.district is not None:
            result['District'] = self.district
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.fixed_number is not None:
            result['FixedNumber'] = self.fixed_number
        if self.full_address is not None:
            result['FullAddress'] = self.full_address
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.is_effective is not None:
            result['IsEffective'] = self.is_effective
        if self.language is not None:
            result['Language'] = self.language
        if self.mobile_number is not None:
            result['MobileNumber'] = self.mobile_number
        if self.province is not None:
            result['Province'] = self.province
        if self.recipient_name is not None:
            result['RecipientName'] = self.recipient_name
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.related_system is not None:
            result['RelatedSystem'] = self.related_system
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.street is not None:
            result['Street'] = self.street
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.zip_code is not None:
            result['ZipCode'] = self.zip_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Customer') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestAddressCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('DetailedAddress') is not None:
            self.detailed_address = m.get('DetailedAddress')
        if m.get('District') is not None:
            self.district = m.get('District')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('FixedNumber') is not None:
            self.fixed_number = m.get('FixedNumber')
        if m.get('FullAddress') is not None:
            self.full_address = m.get('FullAddress')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('IsEffective') is not None:
            self.is_effective = m.get('IsEffective')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MobileNumber') is not None:
            self.mobile_number = m.get('MobileNumber')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('RecipientName') is not None:
            self.recipient_name = m.get('RecipientName')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RelatedSystem') is not None:
            self.related_system = m.get('RelatedSystem')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Street') is not None:
            self.street = m.get('Street')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('ZipCode') is not None:
            self.zip_code = m.get('ZipCode')
        return self


class ApplyArInvoiceWithSourceRequestCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceRequestCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequestSourceListCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceRequestSourceListCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequestSourceList(TeaModel):
    def __init__(self, amount=None, app_code=None, bill_amount=None, bill_domain=None, bill_no=None, bill_type=None,
                 blue_source_id=None, can_merge=None, cargo_name=None, category=None, company_name=None, currency_code=None,
                 customer=None, discount_amount=None, discount_tax_amount=None, encrypt_props=None,
                 excluding_tax_amount=None, excluding_tax_discount_amount=None, excluding_tax_red_amount=None,
                 excluding_tax_remain_amount=None, gmt_bill=None, gmt_bill_end=None, gmt_bill_start=None, gmt_build=None, is_apply=None,
                 language=None, major_bill_no=None, model=None, ou_code=None, parent_category=None, product_domain=None,
                 product_id=None, product_name=None, quantity=None, quantity_unit=None, red_amount=None, related_id=None,
                 remain_amount=None, revenue_type=None, service_name=None, sign=None, site_id=None, source_id=None,
                 tax_amount=None, tax_rate=None, unit_price=None, uuid=None):
        self.amount = amount  # type: float
        self.app_code = app_code  # type: str
        self.bill_amount = bill_amount  # type: float
        self.bill_domain = bill_domain  # type: str
        self.bill_no = bill_no  # type: str
        self.bill_type = bill_type  # type: str
        self.blue_source_id = blue_source_id  # type: long
        self.can_merge = can_merge  # type: bool
        self.cargo_name = cargo_name  # type: str
        self.category = category  # type: str
        self.company_name = company_name  # type: str
        self.currency_code = currency_code  # type: str
        self.customer = customer  # type: ApplyArInvoiceWithSourceRequestSourceListCustomer
        self.discount_amount = discount_amount  # type: float
        self.discount_tax_amount = discount_tax_amount  # type: float
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.excluding_tax_amount = excluding_tax_amount  # type: float
        self.excluding_tax_discount_amount = excluding_tax_discount_amount  # type: float
        self.excluding_tax_red_amount = excluding_tax_red_amount  # type: float
        self.excluding_tax_remain_amount = excluding_tax_remain_amount  # type: float
        self.gmt_bill = gmt_bill  # type: str
        self.gmt_bill_end = gmt_bill_end  # type: str
        self.gmt_bill_start = gmt_bill_start  # type: str
        self.gmt_build = gmt_build  # type: str
        self.is_apply = is_apply  # type: str
        self.language = language  # type: str
        self.major_bill_no = major_bill_no  # type: str
        self.model = model  # type: str
        self.ou_code = ou_code  # type: str
        self.parent_category = parent_category  # type: str
        self.product_domain = product_domain  # type: str
        self.product_id = product_id  # type: str
        self.product_name = product_name  # type: str
        self.quantity = quantity  # type: float
        self.quantity_unit = quantity_unit  # type: str
        self.red_amount = red_amount  # type: float
        self.related_id = related_id  # type: str
        self.remain_amount = remain_amount  # type: float
        self.revenue_type = revenue_type  # type: str
        self.service_name = service_name  # type: str
        self.sign = sign  # type: str
        self.site_id = site_id  # type: str
        self.source_id = source_id  # type: long
        self.tax_amount = tax_amount  # type: float
        self.tax_rate = tax_rate  # type: float
        self.unit_price = unit_price  # type: float
        self.uuid = uuid  # type: str

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceRequestSourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.bill_amount is not None:
            result['BillAmount'] = self.bill_amount
        if self.bill_domain is not None:
            result['BillDomain'] = self.bill_domain
        if self.bill_no is not None:
            result['BillNo'] = self.bill_no
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.blue_source_id is not None:
            result['BlueSourceId'] = self.blue_source_id
        if self.can_merge is not None:
            result['CanMerge'] = self.can_merge
        if self.cargo_name is not None:
            result['CargoName'] = self.cargo_name
        if self.category is not None:
            result['Category'] = self.category
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.discount_tax_amount is not None:
            result['DiscountTaxAmount'] = self.discount_tax_amount
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_discount_amount is not None:
            result['ExcludingTaxDiscountAmount'] = self.excluding_tax_discount_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.gmt_bill is not None:
            result['GmtBill'] = self.gmt_bill
        if self.gmt_bill_end is not None:
            result['GmtBillEnd'] = self.gmt_bill_end
        if self.gmt_bill_start is not None:
            result['GmtBillStart'] = self.gmt_bill_start
        if self.gmt_build is not None:
            result['GmtBuild'] = self.gmt_build
        if self.is_apply is not None:
            result['IsApply'] = self.is_apply
        if self.language is not None:
            result['Language'] = self.language
        if self.major_bill_no is not None:
            result['MajorBillNo'] = self.major_bill_no
        if self.model is not None:
            result['Model'] = self.model
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.product_domain is not None:
            result['ProductDomain'] = self.product_domain
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.quantity_unit is not None:
            result['QuantityUnit'] = self.quantity_unit
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.revenue_type is not None:
            result['RevenueType'] = self.revenue_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BillAmount') is not None:
            self.bill_amount = m.get('BillAmount')
        if m.get('BillDomain') is not None:
            self.bill_domain = m.get('BillDomain')
        if m.get('BillNo') is not None:
            self.bill_no = m.get('BillNo')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BlueSourceId') is not None:
            self.blue_source_id = m.get('BlueSourceId')
        if m.get('CanMerge') is not None:
            self.can_merge = m.get('CanMerge')
        if m.get('CargoName') is not None:
            self.cargo_name = m.get('CargoName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestSourceListCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('DiscountTaxAmount') is not None:
            self.discount_tax_amount = m.get('DiscountTaxAmount')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxDiscountAmount') is not None:
            self.excluding_tax_discount_amount = m.get('ExcludingTaxDiscountAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('GmtBill') is not None:
            self.gmt_bill = m.get('GmtBill')
        if m.get('GmtBillEnd') is not None:
            self.gmt_bill_end = m.get('GmtBillEnd')
        if m.get('GmtBillStart') is not None:
            self.gmt_bill_start = m.get('GmtBillStart')
        if m.get('GmtBuild') is not None:
            self.gmt_build = m.get('GmtBuild')
        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MajorBillNo') is not None:
            self.major_bill_no = m.get('MajorBillNo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ProductDomain') is not None:
            self.product_domain = m.get('ProductDomain')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('QuantityUnit') is not None:
            self.quantity_unit = m.get('QuantityUnit')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('RevenueType') is not None:
            self.revenue_type = m.get('RevenueType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceRequest(TeaModel):
    def __init__(self, address=None, amount=None, app_code=None, applier=None, apply_date=None, currency_code=None,
                 customer=None, encrypt_props=None, excluding_tax_amount=None, input_type=None, invoice_type=None,
                 is_merged=None, language=None, material_type=None, memo=None, ou_code=None, purchaser_bank_info=None,
                 purchaser_contact_info=None, purchaser_name=None, purchaser_tax_no=None, request_no=None, sign=None, site_id=None,
                 source_list=None, tax_amount=None, uuid=None):
        self.address = address  # type: ApplyArInvoiceWithSourceRequestAddress
        self.amount = amount  # type: float
        self.app_code = app_code  # type: str
        self.applier = applier  # type: str
        self.apply_date = apply_date  # type: str
        self.currency_code = currency_code  # type: str
        self.customer = customer  # type: ApplyArInvoiceWithSourceRequestCustomer
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.excluding_tax_amount = excluding_tax_amount  # type: float
        self.input_type = input_type  # type: str
        self.invoice_type = invoice_type  # type: str
        self.is_merged = is_merged  # type: bool
        self.language = language  # type: str
        self.material_type = material_type  # type: str
        self.memo = memo  # type: str
        self.ou_code = ou_code  # type: str
        self.purchaser_bank_info = purchaser_bank_info  # type: str
        self.purchaser_contact_info = purchaser_contact_info  # type: str
        self.purchaser_name = purchaser_name  # type: str
        self.purchaser_tax_no = purchaser_tax_no  # type: str
        self.request_no = request_no  # type: str
        self.sign = sign  # type: str
        self.site_id = site_id  # type: str
        self.source_list = source_list  # type: list[ApplyArInvoiceWithSourceRequestSourceList]
        self.tax_amount = tax_amount  # type: float
        self.uuid = uuid  # type: str

    def validate(self):
        if self.address:
            self.address.validate()
        if self.customer:
            self.customer.validate()
        if self.source_list:
            for k in self.source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address.to_map()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.applier is not None:
            result['Applier'] = self.applier
        if self.apply_date is not None:
            result['ApplyDate'] = self.apply_date
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.input_type is not None:
            result['InputType'] = self.input_type
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_merged is not None:
            result['IsMerged'] = self.is_merged
        if self.language is not None:
            result['Language'] = self.language
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.purchaser_bank_info is not None:
            result['PurchaserBankInfo'] = self.purchaser_bank_info
        if self.purchaser_contact_info is not None:
            result['PurchaserContactInfo'] = self.purchaser_contact_info
        if self.purchaser_name is not None:
            result['PurchaserName'] = self.purchaser_name
        if self.purchaser_tax_no is not None:
            result['PurchaserTaxNo'] = self.purchaser_tax_no
        if self.request_no is not None:
            result['RequestNo'] = self.request_no
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        result['SourceList'] = []
        if self.source_list is not None:
            for k in self.source_list:
                result['SourceList'].append(k.to_map() if k else None)
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestAddress()
            self.address = temp_model.from_map(m['Address'])
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Applier') is not None:
            self.applier = m.get('Applier')
        if m.get('ApplyDate') is not None:
            self.apply_date = m.get('ApplyDate')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = ApplyArInvoiceWithSourceRequestCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsMerged') is not None:
            self.is_merged = m.get('IsMerged')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('PurchaserBankInfo') is not None:
            self.purchaser_bank_info = m.get('PurchaserBankInfo')
        if m.get('PurchaserContactInfo') is not None:
            self.purchaser_contact_info = m.get('PurchaserContactInfo')
        if m.get('PurchaserName') is not None:
            self.purchaser_name = m.get('PurchaserName')
        if m.get('PurchaserTaxNo') is not None:
            self.purchaser_tax_no = m.get('PurchaserTaxNo')
        if m.get('RequestNo') is not None:
            self.request_no = m.get('RequestNo')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        self.source_list = []
        if m.get('SourceList') is not None:
            for k in m.get('SourceList'):
                temp_model = ApplyArInvoiceWithSourceRequestSourceList()
                self.source_list.append(temp_model.from_map(k))
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ApplyArInvoiceWithSourceResponseBodyReturnValue(TeaModel):
    def __init__(self, encrypt_props=None, outer_system_encrypt_str=None, outer_system_sign_str=None, sign=None):
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.outer_system_encrypt_str = outer_system_encrypt_str  # type: str
        self.outer_system_sign_str = outer_system_sign_str  # type: str
        self.sign = sign  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceResponseBodyReturnValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.outer_system_encrypt_str is not None:
            result['OuterSystemEncryptStr'] = self.outer_system_encrypt_str
        if self.outer_system_sign_str is not None:
            result['OuterSystemSignStr'] = self.outer_system_sign_str
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('OuterSystemEncryptStr') is not None:
            self.outer_system_encrypt_str = m.get('OuterSystemEncryptStr')
        if m.get('OuterSystemSignStr') is not None:
            self.outer_system_sign_str = m.get('OuterSystemSignStr')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class ApplyArInvoiceWithSourceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, is_success=None, return_value=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.return_value = return_value  # type: ApplyArInvoiceWithSourceResponseBodyReturnValue

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = ApplyArInvoiceWithSourceResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class ApplyArInvoiceWithSourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyArInvoiceWithSourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyArInvoiceWithSourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyArInvoiceWithSourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyBlackInfoExportRequest(TeaModel):
    def __init__(self, bill_id=None, black_type=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.black_type = black_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyBlackInfoExportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ApplyBlackInfoExportResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyBlackInfoExportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyBlackInfoExportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyBlackInfoExportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyBlackInfoExportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyBlackInfoExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyCallRecordExportRequest(TeaModel):
    def __init__(self, bill_id=None, call_date=None, call_id=None, owner_id=None, phone_no_a=None, phone_no_b=None,
                 prod_code=None, res_type=None, resource_owner_account=None, resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.call_date = call_date  # type: str
        self.call_id = call_id  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyCallRecordExportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ApplyCallRecordExportResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyCallRecordExportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyCallRecordExportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyCallRecordExportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyCallRecordExportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyCallRecordExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyGroupNumberExportRequest(TeaModel):
    def __init__(self, group_id=None, owner_id=None, pool_key=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.group_id = group_id  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyGroupNumberExportRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ApplyGroupNumberExportResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyGroupNumberExportResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyGroupNumberExportResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyGroupNumberExportResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyGroupNumberExportResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyGroupNumberExportResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyRingToneRequest(TeaModel):
    def __init__(self, bill_id=None, id=None, owner_id=None, play_type=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.play_type = play_type  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyRingToneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_type is not None:
            result['PlayType'] = self.play_type
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ApplyRingToneResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyRingToneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ApplyRingToneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyRingToneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyRingToneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchOccupySecretResRequestBatchOccupyList(TeaModel):
    def __init__(self, count=None, order_detail_id=None, order_id=None, partner_key=None, res_type=None,
                 secret_no_type=None):
        self.count = count  # type: int
        self.order_detail_id = order_detail_id  # type: long
        self.order_id = order_id  # type: long
        self.partner_key = partner_key  # type: str
        self.res_type = res_type  # type: long
        self.secret_no_type = secret_no_type  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchOccupySecretResRequestBatchOccupyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.order_detail_id is not None:
            result['OrderDetailId'] = self.order_detail_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.secret_no_type is not None:
            result['SecretNoType'] = self.secret_no_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('OrderDetailId') is not None:
            self.order_detail_id = m.get('OrderDetailId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('SecretNoType') is not None:
            self.secret_no_type = m.get('SecretNoType')
        return self


class BatchOccupySecretResRequest(TeaModel):
    def __init__(self, batch_occupy_list=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.batch_occupy_list = batch_occupy_list  # type: list[BatchOccupySecretResRequestBatchOccupyList]
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        if self.batch_occupy_list:
            for k in self.batch_occupy_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchOccupySecretResRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BatchOccupyList'] = []
        if self.batch_occupy_list is not None:
            for k in self.batch_occupy_list:
                result['BatchOccupyList'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.batch_occupy_list = []
        if m.get('BatchOccupyList') is not None:
            for k in m.get('BatchOccupyList'):
                temp_model = BatchOccupySecretResRequestBatchOccupyList()
                self.batch_occupy_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BatchOccupySecretResShrinkRequest(TeaModel):
    def __init__(self, batch_occupy_list_shrink=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.batch_occupy_list_shrink = batch_occupy_list_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchOccupySecretResShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_occupy_list_shrink is not None:
            result['BatchOccupyList'] = self.batch_occupy_list_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchOccupyList') is not None:
            self.batch_occupy_list_shrink = m.get('BatchOccupyList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BatchOccupySecretResResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchOccupySecretResResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchOccupySecretResResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchOccupySecretResResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchOccupySecretResResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchOccupySecretResResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindResourceRequest(TeaModel):
    def __init__(self, asr_model_id=None, asr_status=None, axn_extension_b=None, bill_id=None, exp_time=None,
                 is_record=None, owner_id=None, phone_no_a=None, phone_no_b=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, secret_no=None):
        self.asr_model_id = asr_model_id  # type: str
        self.asr_status = asr_status  # type: bool
        self.axn_extension_b = axn_extension_b  # type: str
        self.bill_id = bill_id  # type: str
        self.exp_time = exp_time  # type: str
        self.is_record = is_record  # type: bool
        self.owner_id = owner_id  # type: long
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.asr_status is not None:
            result['AsrStatus'] = self.asr_status
        if self.axn_extension_b is not None:
            result['AxnExtensionB'] = self.axn_extension_b
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.exp_time is not None:
            result['ExpTime'] = self.exp_time
        if self.is_record is not None:
            result['IsRecord'] = self.is_record
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('AsrStatus') is not None:
            self.asr_status = m.get('AsrStatus')
        if m.get('AxnExtensionB') is not None:
            self.axn_extension_b = m.get('AxnExtensionB')
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('ExpTime') is not None:
            self.exp_time = m.get('ExpTime')
        if m.get('IsRecord') is not None:
            self.is_record = m.get('IsRecord')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class BindResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class BindResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BlackOperateRequest(TeaModel):
    def __init__(self, bill_id=None, black_map=None, black_type=None, operate_type=None, owner_id=None,
                 prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.black_map = black_map  # type: str
        self.black_type = black_type  # type: str
        self.operate_type = operate_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BlackOperateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.black_map is not None:
            result['BlackMap'] = self.black_map
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.operate_type is not None:
            result['OperateType'] = self.operate_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BlackMap') is not None:
            self.black_map = m.get('BlackMap')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('OperateType') is not None:
            self.operate_type = m.get('OperateType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class BlackOperateResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BlackOperateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class BlackOperateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BlackOperateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BlackOperateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BlackOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCertifyInfoRequest(TeaModel):
    def __init__(self, owner_id=None, phone_no=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.phone_no = phone_no  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertifyInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateCertifyInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCertifyInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateCertifyInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCertifyInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCertifyInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateCertifyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateContactsRequest(TeaModel):
    def __init__(self, bill_id=None, name=None, owner_id=None, phone_number=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateContactsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateContactsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupDetailRequest(TeaModel):
    def __init__(self, group_id=None, number_list=None, owner_id=None, pool_key=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.group_id = group_id  # type: str
        self.number_list = number_list  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateGroupDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupInfoRequest(TeaModel):
    def __init__(self, name=None, number_list=None, owner_id=None, pool_key=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.name = name  # type: str
        self.number_list = number_list  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateGroupInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateGroupInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGroupInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLogicalDeleteRequest(TeaModel):
    def __init__(self, bid=None, country=None, gmt_wakeup=None, hid=None, interrupt=None, invoker=None, message=None,
                 pk=None, prod_code=None, success=None, task_extra_data=None, task_identifier=None):
        self.bid = bid  # type: str
        self.country = country  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.message = message  # type: str
        self.pk = pk  # type: str
        self.prod_code = prod_code  # type: str
        self.success = success  # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogicalDeleteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreateLogicalDeleteResponseBody(TeaModel):
    def __init__(self, bid=None, country=None, gmt_wakeup=None, hid=None, interrupt=None, invoker=None, message=None,
                 pk=None, success=None, task_extra_data=None, task_identifier=None):
        self.bid = bid  # type: str
        self.country = country  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.message = message  # type: str
        self.pk = pk  # type: str
        self.success = success  # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLogicalDeleteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreateLogicalDeleteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLogicalDeleteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLogicalDeleteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateLogicalDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMessageCallbackRequest(TeaModel):
    def __init__(self, biz_type=None, callback_url=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.callback_url = callback_url  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMessageCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMessageCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMessageCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMessageCallbackResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMessageQueueRequest(TeaModel):
    def __init__(self, bill_ids=None, biz_type=None, owner_id=None, prod_code=None, queue_name=None,
                 queue_title=None, resource_owner_account=None, resource_owner_id=None):
        self.bill_ids = bill_ids  # type: str
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.queue_name = queue_name  # type: str
        self.queue_title = queue_title  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMessageQueueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_ids is not None:
            result['BillIds'] = self.bill_ids
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.queue_name is not None:
            result['QueueName'] = self.queue_name
        if self.queue_title is not None:
            result['QueueTitle'] = self.queue_title
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillIds') is not None:
            self.bill_ids = m.get('BillIds')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')
        if m.get('QueueTitle') is not None:
            self.queue_title = m.get('QueueTitle')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateMessageQueueResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMessageQueueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateMessageQueueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMessageQueueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMessageQueueResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMessageQueueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePhysicalDeleteRequest(TeaModel):
    def __init__(self, bid=None, country=None, gmt_wakeup=None, hid=None, interrupt=None, invoker=None, message=None,
                 pk=None, prod_code=None, success=None, task_extra_data=None, task_identifier=None):
        self.bid = bid  # type: str
        self.country = country  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.message = message  # type: str
        self.pk = pk  # type: str
        self.prod_code = prod_code  # type: str
        self.success = success  # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePhysicalDeleteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreatePhysicalDeleteResponseBody(TeaModel):
    def __init__(self, bid=None, country=None, gmt_wakeup=None, hid=None, interrupt=None, invoker=None, message=None,
                 pk=None, success=None, task_extra_data=None, task_identifier=None):
        self.bid = bid  # type: str
        self.country = country  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.message = message  # type: str
        self.pk = pk  # type: str
        self.success = success  # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePhysicalDeleteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        return self


class CreatePhysicalDeleteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePhysicalDeleteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePhysicalDeleteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePhysicalDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePoolInfoRequest(TeaModel):
    def __init__(self, owner_id=None, pool_name=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.pool_name = pool_name  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePoolInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreatePoolInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePoolInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreatePoolInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePoolInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePoolInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePoolInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, prod_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.prod_id = prod_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.prod_id is not None:
            result['ProdId'] = self.prod_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProductResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateProductResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProductResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRingToneRequest(TeaModel):
    def __init__(self, bill_id=None, file_key=None, owner_id=None, play_type=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None, ring_name=None, tts=None):
        self.bill_id = bill_id  # type: str
        self.file_key = file_key  # type: str
        self.owner_id = owner_id  # type: long
        self.play_type = play_type  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.ring_name = ring_name  # type: str
        self.tts = tts  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRingToneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_type is not None:
            result['PlayType'] = self.play_type
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.ring_name is not None:
            result['RingName'] = self.ring_name
        if self.tts is not None:
            result['Tts'] = self.tts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('RingName') is not None:
            self.ring_name = m.get('RingName')
        if m.get('Tts') is not None:
            self.tts = m.get('Tts')
        return self


class CreateRingToneResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRingToneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateRingToneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRingToneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRingToneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSubsTrialRequest(TeaModel):
    def __init__(self, owner_id=None, phone_a=None, phone_b=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.phone_a = phone_a  # type: str
        self.phone_b = phone_b  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubsTrialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_a is not None:
            result['PhoneA'] = self.phone_a
        if self.phone_b is not None:
            result['PhoneB'] = self.phone_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneA') is not None:
            self.phone_a = m.get('PhoneA')
        if m.get('PhoneB') is not None:
            self.phone_b = m.get('PhoneB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class CreateSubsTrialResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSubsTrialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateSubsTrialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSubsTrialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSubsTrialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSubsTrialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTransferRecordRequest(TeaModel):
    def __init__(self, city=None, number_list=None, origin_bill_id=None, origin_name=None, owner_id=None,
                 prod_code=None, resource_owner_account=None, resource_owner_id=None, target_bill_id=None, target_name=None,
                 total=None, transfer_type=None):
        self.city = city  # type: str
        self.number_list = number_list  # type: str
        self.origin_bill_id = origin_bill_id  # type: str
        self.origin_name = origin_name  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.target_bill_id = target_bill_id  # type: str
        self.target_name = target_name  # type: str
        self.total = total  # type: int
        self.transfer_type = transfer_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransferRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.origin_bill_id is not None:
            result['OriginBillId'] = self.origin_bill_id
        if self.origin_name is not None:
            result['OriginName'] = self.origin_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.target_bill_id is not None:
            result['TargetBillId'] = self.target_bill_id
        if self.target_name is not None:
            result['TargetName'] = self.target_name
        if self.total is not None:
            result['Total'] = self.total
        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('OriginBillId') is not None:
            self.origin_bill_id = m.get('OriginBillId')
        if m.get('OriginName') is not None:
            self.origin_name = m.get('OriginName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TargetBillId') is not None:
            self.target_bill_id = m.get('TargetBillId')
        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')
        return self


class CreateTransferRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransferRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class CreateTransferRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransferRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransferRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTransferRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCertifyInfoRequest(TeaModel):
    def __init__(self, certify_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.certify_id = certify_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCertifyInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_id is not None:
            result['CertifyId'] = self.certify_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyId') is not None:
            self.certify_id = m.get('CertifyId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteCertifyInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCertifyInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteCertifyInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCertifyInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCertifyInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCertifyInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteContactsRequest(TeaModel):
    def __init__(self, bill_id=None, id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.id = id  # type: long
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteContactsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteContactsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupDetailRequest(TeaModel):
    def __init__(self, group_id=None, id_list=None, owner_id=None, pool_key=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.group_id = group_id  # type: str
        self.id_list = id_list  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id_list is not None:
            result['IdList'] = self.id_list
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteGroupDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMessageCallbackRequest(TeaModel):
    def __init__(self, biz_type=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteMessageCallbackResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMessageCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteMessageCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMessageCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMessageCallbackResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMessageCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRingToneRequest(TeaModel):
    def __init__(self, bill_id=None, id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRingToneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteRingToneResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRingToneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteRingToneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRingToneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRingToneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadCompleteRequest(TeaModel):
    def __init__(self, biz_type=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadCompleteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DownloadCompleteResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadCompleteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DownloadCompleteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DownloadCompleteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DownloadCompleteResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DownloadCompleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportResRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, res_bind_status=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_bind_status = res_bind_status  # type: int
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportResRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_bind_status is not None:
            result['ResBindStatus'] = self.res_bind_status
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResBindStatus') is not None:
            self.res_bind_status = m.get('ResBindStatus')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ExportResResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportResResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ExportResResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportResResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportResResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExportResResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEinvoicePdfDataRequestCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEinvoicePdfDataRequestCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEinvoicePdfDataRequest(TeaModel):
    def __init__(self, app_code=None, customer=None, encrypt_props=None, invoice_code=None, invoice_no=None,
                 language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer = customer  # type: GetEinvoicePdfDataRequestCustomer
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.invoice_code = invoice_code  # type: str
        self.invoice_no = invoice_no  # type: str
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super(GetEinvoicePdfDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Customer') is not None:
            temp_model = GetEinvoicePdfDataRequestCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEinvoicePdfDataResponseBodyReturnValue(TeaModel):
    def __init__(self, app_code=None, einvoice_data=None, encrypt_props=None, invoice_code=None, invoice_no=None,
                 language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.einvoice_data = einvoice_data  # type: list[int]
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.invoice_code = invoice_code  # type: str
        self.invoice_no = invoice_no  # type: str
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEinvoicePdfDataResponseBodyReturnValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.einvoice_data is not None:
            result['EInvoiceData'] = self.einvoice_data
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('EInvoiceData') is not None:
            self.einvoice_data = m.get('EInvoiceData')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetEinvoicePdfDataResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, is_success=None, return_value=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.return_value = return_value  # type: GetEinvoicePdfDataResponseBodyReturnValue

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super(GetEinvoicePdfDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = GetEinvoicePdfDataResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class GetEinvoicePdfDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetEinvoicePdfDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEinvoicePdfDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetEinvoicePdfDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSecretAsrInfoRequest(TeaModel):
    def __init__(self, call_id=None, call_time=None, pool_key=None, prod_code=None):
        self.call_id = call_id  # type: str
        self.call_time = call_time  # type: str
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretAsrInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class GetSecretAsrInfoResponseBodyData(TeaModel):
    def __init__(self, channel=None, text=None):
        self.channel = channel  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSecretAsrInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetSecretAsrInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetSecretAsrInfoResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSecretAsrInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetSecretAsrInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetSecretAsrInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSecretAsrInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSecretAsrInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSecretAsrInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserResourceTagStatusRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None,
                 resource_type=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.resource_type = resource_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResourceTagStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetUserResourceTagStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResourceTagStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserResourceTagStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserResourceTagStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResourceTagStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUserResourceTagStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsrLanguageModelsRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsrLanguageModelsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListAsrLanguageModelsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsrLanguageModelsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAsrLanguageModelsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAsrLanguageModelsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAsrLanguageModelsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAsrLanguageModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockResourceRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class LockResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class LockResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LockResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OccupySecretResRequest(TeaModel):
    def __init__(self, city=None, is_display_pool=None, no_like=None, order_detail_id=None, order_id=None,
                 owner_id=None, partner_key=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None, secret_no_type=None, total_count=None, secret_no=None):
        self.city = city  # type: str
        self.is_display_pool = is_display_pool  # type: bool
        self.no_like = no_like  # type: str
        self.order_detail_id = order_detail_id  # type: long
        self.order_id = order_id  # type: long
        self.owner_id = owner_id  # type: long
        self.partner_key = partner_key  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no_type = secret_no_type  # type: int
        self.total_count = total_count  # type: int
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OccupySecretResRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.no_like is not None:
            result['NoLike'] = self.no_like
        if self.order_detail_id is not None:
            result['OrderDetailId'] = self.order_detail_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.partner_key is not None:
            result['PartnerKey'] = self.partner_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no_type is not None:
            result['SecretNoType'] = self.secret_no_type
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.secret_no is not None:
            result['secretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('NoLike') is not None:
            self.no_like = m.get('NoLike')
        if m.get('OrderDetailId') is not None:
            self.order_detail_id = m.get('OrderDetailId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PartnerKey') is not None:
            self.partner_key = m.get('PartnerKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNoType') is not None:
            self.secret_no_type = m.get('SecretNoType')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('secretNo') is not None:
            self.secret_no = m.get('secretNo')
        return self


class OccupySecretResResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OccupySecretResResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OccupySecretResResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OccupySecretResResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OccupySecretResResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OccupySecretResResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OrderSucceededCallbackRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None,
                 data=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderSucceededCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class OrderSucceededCallbackResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None, synchro=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.synchro = synchro  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OrderSucceededCallbackResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.synchro is not None:
            result['Synchro'] = self.synchro
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')
        return self


class OrderSucceededCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OrderSucceededCallbackResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OrderSucceededCallbackResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OrderSucceededCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PoolConfigRequest(TeaModel):
    def __init__(self, bill_id=None, callback_type=None, frozen_day=None, need_all_call_records=None,
                 open_sms_white=None, owner_id=None, pool_warning_limit=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None, select_xmode=None, smart_sms_whitelist=None, sms_channel=None):
        self.bill_id = bill_id  # type: str
        self.callback_type = callback_type  # type: int
        self.frozen_day = frozen_day  # type: int
        self.need_all_call_records = need_all_call_records  # type: bool
        self.open_sms_white = open_sms_white  # type: bool
        self.owner_id = owner_id  # type: long
        self.pool_warning_limit = pool_warning_limit  # type: int
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.select_xmode = select_xmode  # type: str
        self.smart_sms_whitelist = smart_sms_whitelist  # type: str
        self.sms_channel = sms_channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PoolConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type
        if self.frozen_day is not None:
            result['FrozenDay'] = self.frozen_day
        if self.need_all_call_records is not None:
            result['NeedAllCallRecords'] = self.need_all_call_records
        if self.open_sms_white is not None:
            result['OpenSmsWhite'] = self.open_sms_white
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_warning_limit is not None:
            result['PoolWarningLimit'] = self.pool_warning_limit
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.select_xmode is not None:
            result['SelectXMode'] = self.select_xmode
        if self.smart_sms_whitelist is not None:
            result['SmartSmsWhitelist'] = self.smart_sms_whitelist
        if self.sms_channel is not None:
            result['SmsChannel'] = self.sms_channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')
        if m.get('FrozenDay') is not None:
            self.frozen_day = m.get('FrozenDay')
        if m.get('NeedAllCallRecords') is not None:
            self.need_all_call_records = m.get('NeedAllCallRecords')
        if m.get('OpenSmsWhite') is not None:
            self.open_sms_white = m.get('OpenSmsWhite')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolWarningLimit') is not None:
            self.pool_warning_limit = m.get('PoolWarningLimit')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SelectXMode') is not None:
            self.select_xmode = m.get('SelectXMode')
        if m.get('SmartSmsWhitelist') is not None:
            self.smart_sms_whitelist = m.get('SmartSmsWhitelist')
        if m.get('SmsChannel') is not None:
            self.sms_channel = m.get('SmsChannel')
        return self


class PoolConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PoolConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PoolConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PoolConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PoolConfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PoolConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PurchaseResourcesRequest(TeaModel):
    def __init__(self, bill_id=None, buy_number=None, is_display_pool=None, no_like=None, owner_id=None,
                 prod_code=None, region_name=None, res_type=None, resource_owner_account=None, resource_owner_id=None,
                 spec_id=None, usage_scenarios=None):
        self.bill_id = bill_id  # type: str
        self.buy_number = buy_number  # type: int
        self.is_display_pool = is_display_pool  # type: bool
        self.no_like = no_like  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.region_name = region_name  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.spec_id = spec_id  # type: long
        self.usage_scenarios = usage_scenarios  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurchaseResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.buy_number is not None:
            result['BuyNumber'] = self.buy_number
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.no_like is not None:
            result['NoLike'] = self.no_like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.usage_scenarios is not None:
            result['UsageScenarios'] = self.usage_scenarios
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BuyNumber') is not None:
            self.buy_number = m.get('BuyNumber')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('NoLike') is not None:
            self.no_like = m.get('NoLike')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('UsageScenarios') is not None:
            self.usage_scenarios = m.get('UsageScenarios')
        return self


class PurchaseResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PurchaseResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class PurchaseResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PurchaseResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PurchaseResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PurchaseResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBindingDetailsRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, page_no=None, page_size=None, phone_no_a=None, phone_no_b=None,
                 prod_code=None, res_type=None, resource_owner_account=None, resource_owner_id=None, secret_no=None,
                 sub_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str
        self.sub_id = sub_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBindingDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        if self.sub_id is not None:
            result['SubId'] = self.sub_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')
        return self


class QueryBindingDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBindingDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBindingDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBindingDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBindingDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBindingDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBlackListRequest(TeaModel):
    def __init__(self, bill_id=None, black_prefix=None, black_type=None, owner_id=None, page_no=None, page_size=None,
                 prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.black_prefix = black_prefix  # type: str
        self.black_type = black_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBlackListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.black_prefix is not None:
            result['BlackPrefix'] = self.black_prefix
        if self.black_type is not None:
            result['BlackType'] = self.black_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BlackPrefix') is not None:
            self.black_prefix = m.get('BlackPrefix')
        if m.get('BlackType') is not None:
            self.black_type = m.get('BlackType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryBlackListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBlackListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryBlackListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBlackListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBlackListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBlackListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyPageInitDataRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyPageInitDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryBuyPageInitDataResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyPageInitDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyPageInitDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBuyPageInitDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBuyPageInitDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyPageInitDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyPageResCountRequest(TeaModel):
    def __init__(self, city=None, like=None, owner_id=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, spec_id=None):
        self.city = city  # type: str
        self.like = like  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.spec_id = spec_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyPageResCountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['City'] = self.city
        if self.like is not None:
            result['Like'] = self.like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryBuyPageResCountResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyPageResCountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyPageResCountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBuyPageResCountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBuyPageResCountResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyPageResCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyPageResInfoRequest(TeaModel):
    def __init__(self, like=None, owner_id=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None, spec_id=None):
        self.like = like  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.spec_id = spec_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyPageResInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.like is not None:
            result['Like'] = self.like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryBuyPageResInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyPageResInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyPageResInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBuyPageResInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBuyPageResInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyPageResInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBuyResInfoRequest(TeaModel):
    def __init__(self, like=None, owner_id=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None, spec_id=None):
        self.like = like  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.spec_id = spec_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyResInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.like is not None:
            result['Like'] = self.like
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Like') is not None:
            self.like = m.get('Like')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        return self


class QueryBuyResInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryBuyResInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryBuyResInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryBuyResInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryBuyResInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryBuyResInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallRecordingListRequest(TeaModel):
    def __init__(self, bill_id=None, call_date=None, call_id=None, owner_id=None, page_no=None, page_size=None,
                 phone_no_a=None, phone_no_b=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.call_date = call_date  # type: str
        self.call_id = call_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.phone_no_a = phone_no_a  # type: str
        self.phone_no_b = phone_no_b  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallRecordingListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_no_a is not None:
            result['PhoneNoA'] = self.phone_no_a
        if self.phone_no_b is not None:
            result['PhoneNoB'] = self.phone_no_b
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNoA') is not None:
            self.phone_no_a = m.get('PhoneNoA')
        if m.get('PhoneNoB') is not None:
            self.phone_no_b = m.get('PhoneNoB')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QueryCallRecordingListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallRecordingListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryCallRecordingListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCallRecordingListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCallRecordingListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCallRecordingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCertifyInfoListRequest(TeaModel):
    def __init__(self, certify_status=None, owner_id=None, page_no=None, page_size=None, phone_no=None,
                 prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.certify_status = certify_status  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.phone_no = phone_no  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCertifyInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_status is not None:
            result['CertifyStatus'] = self.certify_status
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_no is not None:
            result['PhoneNo'] = self.phone_no
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyStatus') is not None:
            self.certify_status = m.get('CertifyStatus')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneNo') is not None:
            self.phone_no = m.get('PhoneNo')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCertifyInfoListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCertifyInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryCertifyInfoListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCertifyInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCertifyInfoListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCertifyInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCertifyOverviewInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCertifyOverviewInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCertifyOverviewInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCertifyOverviewInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryCertifyOverviewInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCertifyOverviewInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCertifyOverviewInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCertifyOverviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryContactsListRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryContactsListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryContactsListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryContactsListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryContactsListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryContactsListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryContactsListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryContactsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCustInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryCustInfoResponseBodyData(TeaModel):
    def __init__(self, certify_type=None, contact_phone=None, cust_id=None, cust_name=None, is_dayu_customer=None,
                 os_status=None, partner_id=None, user_tag=None, user_tag_2=None):
        self.certify_type = certify_type  # type: int
        self.contact_phone = contact_phone  # type: str
        self.cust_id = cust_id  # type: long
        self.cust_name = cust_name  # type: str
        self.is_dayu_customer = is_dayu_customer  # type: bool
        self.os_status = os_status  # type: int
        self.partner_id = partner_id  # type: long
        self.user_tag = user_tag  # type: long
        self.user_tag_2 = user_tag_2  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCustInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certify_type is not None:
            result['CertifyType'] = self.certify_type
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.cust_id is not None:
            result['CustId'] = self.cust_id
        if self.cust_name is not None:
            result['CustName'] = self.cust_name
        if self.is_dayu_customer is not None:
            result['IsDayuCustomer'] = self.is_dayu_customer
        if self.os_status is not None:
            result['OsStatus'] = self.os_status
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.user_tag is not None:
            result['UserTag'] = self.user_tag
        if self.user_tag_2 is not None:
            result['UserTag2'] = self.user_tag_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertifyType') is not None:
            self.certify_type = m.get('CertifyType')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('CustId') is not None:
            self.cust_id = m.get('CustId')
        if m.get('CustName') is not None:
            self.cust_name = m.get('CustName')
        if m.get('IsDayuCustomer') is not None:
            self.is_dayu_customer = m.get('IsDayuCustomer')
        if m.get('OsStatus') is not None:
            self.os_status = m.get('OsStatus')
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('UserTag') is not None:
            self.user_tag = m.get('UserTag')
        if m.get('UserTag2') is not None:
            self.user_tag_2 = m.get('UserTag2')
        return self


class QueryCustInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: QueryCustInfoResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCustInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = QueryCustInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCustInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCustInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCustInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryCustInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDownloadUrlRequest(TeaModel):
    def __init__(self, biz_type=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryDownloadUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDownloadUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDownloadUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEffectiveInvoiceListByBillNosRequest(TeaModel):
    def __init__(self, app_code=None, bill_no=None, encrypt_props=None, language=None, major_bill_no=None,
                 ou_code=None, related_system=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.bill_no = bill_no  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.major_bill_no = major_bill_no  # type: str
        self.ou_code = ou_code  # type: str
        self.related_system = related_system  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEffectiveInvoiceListByBillNosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.bill_no is not None:
            result['BillNo'] = self.bill_no
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.major_bill_no is not None:
            result['MajorBillNo'] = self.major_bill_no
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.related_system is not None:
            result['RelatedSystem'] = self.related_system
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BillNo') is not None:
            self.bill_no = m.get('BillNo')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MajorBillNo') is not None:
            self.major_bill_no = m.get('MajorBillNo')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('RelatedSystem') is not None:
            self.related_system = m.get('RelatedSystem')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList(TeaModel):
    def __init__(self, ali_company=None, ali_id=None, amount=None, app_code=None, build_amount=None, category=None,
                 encrypt_props=None, invoice_no=None, invoice_status=None, invoice_title=None, language=None, order_item_no=None,
                 parent_contract_no=None, sign=None, site=None, tax_regisger_no=None, uuid=None):
        self.ali_company = ali_company  # type: str
        self.ali_id = ali_id  # type: long
        self.amount = amount  # type: float
        self.app_code = app_code  # type: str
        self.build_amount = build_amount  # type: float
        self.category = category  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.invoice_no = invoice_no  # type: str
        self.invoice_status = invoice_status  # type: str
        self.invoice_title = invoice_title  # type: str
        self.language = language  # type: str
        self.order_item_no = order_item_no  # type: str
        self.parent_contract_no = parent_contract_no  # type: str
        self.sign = sign  # type: str
        self.site = site  # type: str
        self.tax_regisger_no = tax_regisger_no  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_company is not None:
            result['AliCompany'] = self.ali_company
        if self.ali_id is not None:
            result['AliId'] = self.ali_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.build_amount is not None:
            result['BuildAmount'] = self.build_amount
        if self.category is not None:
            result['Category'] = self.category
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_status is not None:
            result['InvoiceStatus'] = self.invoice_status
        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title
        if self.language is not None:
            result['Language'] = self.language
        if self.order_item_no is not None:
            result['OrderItemNo'] = self.order_item_no
        if self.parent_contract_no is not None:
            result['ParentContractNo'] = self.parent_contract_no
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site is not None:
            result['Site'] = self.site
        if self.tax_regisger_no is not None:
            result['TaxRegisgerNo'] = self.tax_regisger_no
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliCompany') is not None:
            self.ali_company = m.get('AliCompany')
        if m.get('AliId') is not None:
            self.ali_id = m.get('AliId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BuildAmount') is not None:
            self.build_amount = m.get('BuildAmount')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceStatus') is not None:
            self.invoice_status = m.get('InvoiceStatus')
        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OrderItemNo') is not None:
            self.order_item_no = m.get('OrderItemNo')
        if m.get('ParentContractNo') is not None:
            self.parent_contract_no = m.get('ParentContractNo')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('TaxRegisgerNo') is not None:
            self.tax_regisger_no = m.get('TaxRegisgerNo')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue(TeaModel):
    def __init__(self, encrypt_props=None, list=None, sign=None):
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.list = list  # type: list[QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList]
        self.sign = sign  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEffectiveInvoiceListByBillNosResponseBodyReturnValueList()
                self.list.append(temp_model.from_map(k))
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class QueryEffectiveInvoiceListByBillNosResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, is_success=None, return_value=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.return_value = return_value  # type: QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super(QueryEffectiveInvoiceListByBillNosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = QueryEffectiveInvoiceListByBillNosResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class QueryEffectiveInvoiceListByBillNosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEffectiveInvoiceListByBillNosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEffectiveInvoiceListByBillNosResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryEffectiveInvoiceListByBillNosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryExportResUrlRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None, task_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryExportResUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryExportResUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryExportResUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryExportResUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryExportResUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryExportResUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryExportResUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupDetailListRequest(TeaModel):
    def __init__(self, group_id=None, number=None, owner_id=None, page_no=None, page_size=None, pool_key=None,
                 prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.group_id = group_id  # type: str
        self.number = number  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGroupDetailListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.number is not None:
            result['Number'] = self.number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryGroupDetailListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGroupDetailListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryGroupDetailListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryGroupDetailListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGroupDetailListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryGroupDetailListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGroupInfoListRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None, pool_key=None, prod_code=None, query_key=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.query_key = query_key  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGroupInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.query_key is not None:
            result['QueryKey'] = self.query_key
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('QueryKey') is not None:
            self.query_key = m.get('QueryKey')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryGroupInfoListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGroupInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryGroupInfoListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryGroupInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGroupInfoListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryGroupInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvoiceInfoByRequestNoRequest(TeaModel):
    def __init__(self, app_code=None, encrypt_props=None, language=None, related_system=None, request_no=None,
                 sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.related_system = related_system  # type: str
        self.request_no = request_no  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.related_system is not None:
            result['RelatedSystem'] = self.related_system
        if self.request_no is not None:
            result['RequestNo'] = self.request_no
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RelatedSystem') is not None:
            self.related_system = m.get('RelatedSystem')
        if m.get('RequestNo') is not None:
            self.request_no = m.get('RequestNo')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList(TeaModel):
    def __init__(self, amount=None, app_code=None, bill_amount=None, bill_domain=None, bill_no=None, bill_type=None,
                 blue_source_id=None, can_merge=None, cargo_name=None, category=None, company_name=None, currency_code=None,
                 customer=None, discount_amount=None, discount_tax_amount=None, encrypt_props=None,
                 excluding_tax_amount=None, excluding_tax_discount_amount=None, excluding_tax_red_amount=None,
                 excluding_tax_remain_amount=None, gmt_bill=None, gmt_bill_end=None, gmt_bill_start=None, gmt_build=None, is_apply=None,
                 language=None, major_bill_no=None, model=None, ou_code=None, parent_category=None, product_domain=None,
                 product_id=None, product_name=None, quantity=None, quantity_unit=None, red_amount=None, related_id=None,
                 remain_amount=None, revenue_type=None, service_name=None, sign=None, site_id=None, source_id=None,
                 tax_amount=None, tax_rate=None, unit_price=None, uuid=None):
        self.amount = amount  # type: float
        self.app_code = app_code  # type: str
        self.bill_amount = bill_amount  # type: float
        self.bill_domain = bill_domain  # type: str
        self.bill_no = bill_no  # type: str
        self.bill_type = bill_type  # type: str
        self.blue_source_id = blue_source_id  # type: long
        self.can_merge = can_merge  # type: bool
        self.cargo_name = cargo_name  # type: str
        self.category = category  # type: str
        self.company_name = company_name  # type: str
        self.currency_code = currency_code  # type: str
        self.customer = customer  # type: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer
        self.discount_amount = discount_amount  # type: float
        self.discount_tax_amount = discount_tax_amount  # type: float
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.excluding_tax_amount = excluding_tax_amount  # type: float
        self.excluding_tax_discount_amount = excluding_tax_discount_amount  # type: float
        self.excluding_tax_red_amount = excluding_tax_red_amount  # type: float
        self.excluding_tax_remain_amount = excluding_tax_remain_amount  # type: float
        self.gmt_bill = gmt_bill  # type: str
        self.gmt_bill_end = gmt_bill_end  # type: str
        self.gmt_bill_start = gmt_bill_start  # type: str
        self.gmt_build = gmt_build  # type: str
        self.is_apply = is_apply  # type: str
        self.language = language  # type: str
        self.major_bill_no = major_bill_no  # type: str
        self.model = model  # type: str
        self.ou_code = ou_code  # type: str
        self.parent_category = parent_category  # type: str
        self.product_domain = product_domain  # type: str
        self.product_id = product_id  # type: str
        self.product_name = product_name  # type: str
        self.quantity = quantity  # type: float
        self.quantity_unit = quantity_unit  # type: str
        self.red_amount = red_amount  # type: float
        self.related_id = related_id  # type: str
        self.remain_amount = remain_amount  # type: float
        self.revenue_type = revenue_type  # type: str
        self.service_name = service_name  # type: str
        self.sign = sign  # type: str
        self.site_id = site_id  # type: str
        self.source_id = source_id  # type: long
        self.tax_amount = tax_amount  # type: float
        self.tax_rate = tax_rate  # type: float
        self.unit_price = unit_price  # type: float
        self.uuid = uuid  # type: str

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.bill_amount is not None:
            result['BillAmount'] = self.bill_amount
        if self.bill_domain is not None:
            result['BillDomain'] = self.bill_domain
        if self.bill_no is not None:
            result['BillNo'] = self.bill_no
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.blue_source_id is not None:
            result['BlueSourceId'] = self.blue_source_id
        if self.can_merge is not None:
            result['CanMerge'] = self.can_merge
        if self.cargo_name is not None:
            result['CargoName'] = self.cargo_name
        if self.category is not None:
            result['Category'] = self.category
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.discount_tax_amount is not None:
            result['DiscountTaxAmount'] = self.discount_tax_amount
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_discount_amount is not None:
            result['ExcludingTaxDiscountAmount'] = self.excluding_tax_discount_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.gmt_bill is not None:
            result['GmtBill'] = self.gmt_bill
        if self.gmt_bill_end is not None:
            result['GmtBillEnd'] = self.gmt_bill_end
        if self.gmt_bill_start is not None:
            result['GmtBillStart'] = self.gmt_bill_start
        if self.gmt_build is not None:
            result['GmtBuild'] = self.gmt_build
        if self.is_apply is not None:
            result['IsApply'] = self.is_apply
        if self.language is not None:
            result['Language'] = self.language
        if self.major_bill_no is not None:
            result['MajorBillNo'] = self.major_bill_no
        if self.model is not None:
            result['Model'] = self.model
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.parent_category is not None:
            result['ParentCategory'] = self.parent_category
        if self.product_domain is not None:
            result['ProductDomain'] = self.product_domain
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.quantity_unit is not None:
            result['QuantityUnit'] = self.quantity_unit
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.revenue_type is not None:
            result['RevenueType'] = self.revenue_type
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.source_id is not None:
            result['SourceId'] = self.source_id
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('BillAmount') is not None:
            self.bill_amount = m.get('BillAmount')
        if m.get('BillDomain') is not None:
            self.bill_domain = m.get('BillDomain')
        if m.get('BillNo') is not None:
            self.bill_no = m.get('BillNo')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BlueSourceId') is not None:
            self.blue_source_id = m.get('BlueSourceId')
        if m.get('CanMerge') is not None:
            self.can_merge = m.get('CanMerge')
        if m.get('CargoName') is not None:
            self.cargo_name = m.get('CargoName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceListCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('DiscountTaxAmount') is not None:
            self.discount_tax_amount = m.get('DiscountTaxAmount')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxDiscountAmount') is not None:
            self.excluding_tax_discount_amount = m.get('ExcludingTaxDiscountAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('GmtBill') is not None:
            self.gmt_bill = m.get('GmtBill')
        if m.get('GmtBillEnd') is not None:
            self.gmt_bill_end = m.get('GmtBillEnd')
        if m.get('GmtBillStart') is not None:
            self.gmt_bill_start = m.get('GmtBillStart')
        if m.get('GmtBuild') is not None:
            self.gmt_build = m.get('GmtBuild')
        if m.get('IsApply') is not None:
            self.is_apply = m.get('IsApply')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('MajorBillNo') is not None:
            self.major_bill_no = m.get('MajorBillNo')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('ParentCategory') is not None:
            self.parent_category = m.get('ParentCategory')
        if m.get('ProductDomain') is not None:
            self.product_domain = m.get('ProductDomain')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('QuantityUnit') is not None:
            self.quantity_unit = m.get('QuantityUnit')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('RevenueType') is not None:
            self.revenue_type = m.get('RevenueType')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList(TeaModel):
    def __init__(self, amount=None, app_code=None, cargo_name=None, discount_amount=None, discount_tax_amount=None,
                 encrypt_props=None, excluding_tax_amount=None, excluding_tax_discount_amount=None,
                 excluding_tax_red_amount=None, excluding_tax_remain_amount=None, excluding_tax_unit_price=None, invoice_detail_id=None,
                 language=None, model=None, quantity=None, quantity_unit=None, red_amount=None, related_id=None,
                 remain_amount=None, sign=None, source_list=None, tax_amount=None, tax_rate=None, unit_price=None, uuid=None):
        self.amount = amount  # type: float
        self.app_code = app_code  # type: str
        self.cargo_name = cargo_name  # type: str
        self.discount_amount = discount_amount  # type: float
        self.discount_tax_amount = discount_tax_amount  # type: float
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.excluding_tax_amount = excluding_tax_amount  # type: float
        self.excluding_tax_discount_amount = excluding_tax_discount_amount  # type: float
        self.excluding_tax_red_amount = excluding_tax_red_amount  # type: float
        self.excluding_tax_remain_amount = excluding_tax_remain_amount  # type: float
        self.excluding_tax_unit_price = excluding_tax_unit_price  # type: float
        self.invoice_detail_id = invoice_detail_id  # type: long
        self.language = language  # type: str
        self.model = model  # type: str
        self.quantity = quantity  # type: float
        self.quantity_unit = quantity_unit  # type: str
        self.red_amount = red_amount  # type: float
        self.related_id = related_id  # type: str
        self.remain_amount = remain_amount  # type: float
        self.sign = sign  # type: str
        self.source_list = source_list  # type: list[QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList]
        self.tax_amount = tax_amount  # type: float
        self.tax_rate = tax_rate  # type: float
        self.unit_price = unit_price  # type: float
        self.uuid = uuid  # type: str

    def validate(self):
        if self.source_list:
            for k in self.source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.cargo_name is not None:
            result['CargoName'] = self.cargo_name
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.discount_tax_amount is not None:
            result['DiscountTaxAmount'] = self.discount_tax_amount
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_discount_amount is not None:
            result['ExcludingTaxDiscountAmount'] = self.excluding_tax_discount_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.excluding_tax_unit_price is not None:
            result['ExcludingTaxUnitPrice'] = self.excluding_tax_unit_price
        if self.invoice_detail_id is not None:
            result['InvoiceDetailId'] = self.invoice_detail_id
        if self.language is not None:
            result['Language'] = self.language
        if self.model is not None:
            result['Model'] = self.model
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.quantity_unit is not None:
            result['QuantityUnit'] = self.quantity_unit
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.sign is not None:
            result['Sign'] = self.sign
        result['SourceList'] = []
        if self.source_list is not None:
            for k in self.source_list:
                result['SourceList'].append(k.to_map() if k else None)
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.tax_rate is not None:
            result['TaxRate'] = self.tax_rate
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CargoName') is not None:
            self.cargo_name = m.get('CargoName')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('DiscountTaxAmount') is not None:
            self.discount_tax_amount = m.get('DiscountTaxAmount')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxDiscountAmount') is not None:
            self.excluding_tax_discount_amount = m.get('ExcludingTaxDiscountAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('ExcludingTaxUnitPrice') is not None:
            self.excluding_tax_unit_price = m.get('ExcludingTaxUnitPrice')
        if m.get('InvoiceDetailId') is not None:
            self.invoice_detail_id = m.get('InvoiceDetailId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('QuantityUnit') is not None:
            self.quantity_unit = m.get('QuantityUnit')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        self.source_list = []
        if m.get('SourceList') is not None:
            for k in m.get('SourceList'):
                temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailListSourceList()
                self.source_list.append(temp_model.from_map(k))
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('TaxRate') is not None:
            self.tax_rate = m.get('TaxRate')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer(TeaModel):
    def __init__(self, app_code=None, customer_id=None, customer_site=None, customer_system=None,
                 encrypt_props=None, language=None, sign=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer_id = customer_id  # type: str
        self.customer_site = customer_site  # type: str
        self.customer_system = customer_system  # type: str
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.language = language  # type: str
        self.sign = sign  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.customer_site is not None:
            result['CustomerSite'] = self.customer_site
        if self.customer_system is not None:
            result['CustomerSystem'] = self.customer_system
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.language is not None:
            result['Language'] = self.language
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('CustomerSite') is not None:
            self.customer_site = m.get('CustomerSite')
        if m.get('CustomerSystem') is not None:
            self.customer_system = m.get('CustomerSystem')
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo(TeaModel):
    def __init__(self, app_code=None, customer=None, encrypt_props=None, gmt_send=None, invoice_code=None,
                 invoice_date=None, invoice_id=None, invoice_no=None, invoice_nos=None, language=None, logistics_companies=None,
                 related_id=None, sender=None, sign=None, timestamp=None, tracking_number=None, uuid=None):
        self.app_code = app_code  # type: str
        self.customer = customer  # type: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.gmt_send = gmt_send  # type: str
        self.invoice_code = invoice_code  # type: str
        self.invoice_date = invoice_date  # type: str
        self.invoice_id = invoice_id  # type: long
        self.invoice_no = invoice_no  # type: str
        self.invoice_nos = invoice_nos  # type: str
        self.language = language  # type: str
        self.logistics_companies = logistics_companies  # type: str
        self.related_id = related_id  # type: str
        self.sender = sender  # type: str
        self.sign = sign  # type: str
        self.timestamp = timestamp  # type: long
        self.tracking_number = tracking_number  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.customer:
            self.customer.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.gmt_send is not None:
            result['GmtSend'] = self.gmt_send
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_nos is not None:
            result['InvoiceNos'] = self.invoice_nos
        if self.language is not None:
            result['Language'] = self.language
        if self.logistics_companies is not None:
            result['LogisticsCompanies'] = self.logistics_companies
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.sender is not None:
            result['Sender'] = self.sender
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.tracking_number is not None:
            result['TrackingNumber'] = self.tracking_number
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('Customer') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfoCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('GmtSend') is not None:
            self.gmt_send = m.get('GmtSend')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceNos') is not None:
            self.invoice_nos = m.get('InvoiceNos')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LogisticsCompanies') is not None:
            self.logistics_companies = m.get('LogisticsCompanies')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('Sender') is not None:
            self.sender = m.get('Sender')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('TrackingNumber') is not None:
            self.tracking_number = m.get('TrackingNumber')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValueList(TeaModel):
    def __init__(self, amount=None, app_code=None, currency_code=None, customer=None, detail_list=None,
                 encrypt_props=None, excluding_tax_amount=None, excluding_tax_red_amount=None, excluding_tax_remain_amount=None,
                 invoice_code=None, invoice_date=None, invoice_id=None, invoice_no=None, invoice_status=None, invoice_type=None,
                 is_red=None, is_reissue=None, language=None, link_invoice_code=None, link_invoice_no=None,
                 logistics_info=None, material_type=None, memo=None, ou_code=None, purchaser_bank_info=None,
                 purchaser_contact_info=None, purchaser_name=None, purchaser_tax_no=None, red_amount=None, related_id=None,
                 remain_amount=None, sign=None, site_id=None, tax_amount=None, uuid=None):
        self.amount = amount  # type: float
        self.app_code = app_code  # type: str
        self.currency_code = currency_code  # type: str
        self.customer = customer  # type: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer
        self.detail_list = detail_list  # type: list[QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList]
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.excluding_tax_amount = excluding_tax_amount  # type: float
        self.excluding_tax_red_amount = excluding_tax_red_amount  # type: float
        self.excluding_tax_remain_amount = excluding_tax_remain_amount  # type: float
        self.invoice_code = invoice_code  # type: str
        self.invoice_date = invoice_date  # type: str
        self.invoice_id = invoice_id  # type: long
        self.invoice_no = invoice_no  # type: str
        self.invoice_status = invoice_status  # type: str
        self.invoice_type = invoice_type  # type: str
        self.is_red = is_red  # type: bool
        self.is_reissue = is_reissue  # type: bool
        self.language = language  # type: str
        self.link_invoice_code = link_invoice_code  # type: str
        self.link_invoice_no = link_invoice_no  # type: str
        self.logistics_info = logistics_info  # type: QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo
        self.material_type = material_type  # type: str
        self.memo = memo  # type: str
        self.ou_code = ou_code  # type: str
        self.purchaser_bank_info = purchaser_bank_info  # type: str
        self.purchaser_contact_info = purchaser_contact_info  # type: str
        self.purchaser_name = purchaser_name  # type: str
        self.purchaser_tax_no = purchaser_tax_no  # type: str
        self.red_amount = red_amount  # type: float
        self.related_id = related_id  # type: str
        self.remain_amount = remain_amount  # type: float
        self.sign = sign  # type: str
        self.site_id = site_id  # type: str
        self.tax_amount = tax_amount  # type: float
        self.uuid = uuid  # type: str

    def validate(self):
        if self.customer:
            self.customer.validate()
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()
        if self.logistics_info:
            self.logistics_info.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValueList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.customer is not None:
            result['Customer'] = self.customer.to_map()
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        if self.excluding_tax_amount is not None:
            result['ExcludingTaxAmount'] = self.excluding_tax_amount
        if self.excluding_tax_red_amount is not None:
            result['ExcludingTaxRedAmount'] = self.excluding_tax_red_amount
        if self.excluding_tax_remain_amount is not None:
            result['ExcludingTaxRemainAmount'] = self.excluding_tax_remain_amount
        if self.invoice_code is not None:
            result['InvoiceCode'] = self.invoice_code
        if self.invoice_date is not None:
            result['InvoiceDate'] = self.invoice_date
        if self.invoice_id is not None:
            result['InvoiceId'] = self.invoice_id
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.invoice_status is not None:
            result['InvoiceStatus'] = self.invoice_status
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.is_red is not None:
            result['IsRed'] = self.is_red
        if self.is_reissue is not None:
            result['IsReissue'] = self.is_reissue
        if self.language is not None:
            result['Language'] = self.language
        if self.link_invoice_code is not None:
            result['LinkInvoiceCode'] = self.link_invoice_code
        if self.link_invoice_no is not None:
            result['LinkInvoiceNo'] = self.link_invoice_no
        if self.logistics_info is not None:
            result['LogisticsInfo'] = self.logistics_info.to_map()
        if self.material_type is not None:
            result['MaterialType'] = self.material_type
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.ou_code is not None:
            result['OuCode'] = self.ou_code
        if self.purchaser_bank_info is not None:
            result['PurchaserBankInfo'] = self.purchaser_bank_info
        if self.purchaser_contact_info is not None:
            result['PurchaserContactInfo'] = self.purchaser_contact_info
        if self.purchaser_name is not None:
            result['PurchaserName'] = self.purchaser_name
        if self.purchaser_tax_no is not None:
            result['PurchaserTaxNo'] = self.purchaser_tax_no
        if self.red_amount is not None:
            result['RedAmount'] = self.red_amount
        if self.related_id is not None:
            result['RelatedId'] = self.related_id
        if self.remain_amount is not None:
            result['RemainAmount'] = self.remain_amount
        if self.sign is not None:
            result['Sign'] = self.sign
        if self.site_id is not None:
            result['SiteId'] = self.site_id
        if self.tax_amount is not None:
            result['TaxAmount'] = self.tax_amount
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('Customer') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListCustomer()
            self.customer = temp_model.from_map(m['Customer'])
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k in m.get('DetailList'):
                temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        if m.get('ExcludingTaxAmount') is not None:
            self.excluding_tax_amount = m.get('ExcludingTaxAmount')
        if m.get('ExcludingTaxRedAmount') is not None:
            self.excluding_tax_red_amount = m.get('ExcludingTaxRedAmount')
        if m.get('ExcludingTaxRemainAmount') is not None:
            self.excluding_tax_remain_amount = m.get('ExcludingTaxRemainAmount')
        if m.get('InvoiceCode') is not None:
            self.invoice_code = m.get('InvoiceCode')
        if m.get('InvoiceDate') is not None:
            self.invoice_date = m.get('InvoiceDate')
        if m.get('InvoiceId') is not None:
            self.invoice_id = m.get('InvoiceId')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('InvoiceStatus') is not None:
            self.invoice_status = m.get('InvoiceStatus')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('IsRed') is not None:
            self.is_red = m.get('IsRed')
        if m.get('IsReissue') is not None:
            self.is_reissue = m.get('IsReissue')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LinkInvoiceCode') is not None:
            self.link_invoice_code = m.get('LinkInvoiceCode')
        if m.get('LinkInvoiceNo') is not None:
            self.link_invoice_no = m.get('LinkInvoiceNo')
        if m.get('LogisticsInfo') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueListLogisticsInfo()
            self.logistics_info = temp_model.from_map(m['LogisticsInfo'])
        if m.get('MaterialType') is not None:
            self.material_type = m.get('MaterialType')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('OuCode') is not None:
            self.ou_code = m.get('OuCode')
        if m.get('PurchaserBankInfo') is not None:
            self.purchaser_bank_info = m.get('PurchaserBankInfo')
        if m.get('PurchaserContactInfo') is not None:
            self.purchaser_contact_info = m.get('PurchaserContactInfo')
        if m.get('PurchaserName') is not None:
            self.purchaser_name = m.get('PurchaserName')
        if m.get('PurchaserTaxNo') is not None:
            self.purchaser_tax_no = m.get('PurchaserTaxNo')
        if m.get('RedAmount') is not None:
            self.red_amount = m.get('RedAmount')
        if m.get('RelatedId') is not None:
            self.related_id = m.get('RelatedId')
        if m.get('RemainAmount') is not None:
            self.remain_amount = m.get('RemainAmount')
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')
        if m.get('TaxAmount') is not None:
            self.tax_amount = m.get('TaxAmount')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class QueryInvoiceInfoByRequestNoResponseBodyReturnValue(TeaModel):
    def __init__(self, encrypt_props=None, list=None, sign=None):
        self.encrypt_props = encrypt_props  # type: dict[str, str]
        self.list = list  # type: list[QueryInvoiceInfoByRequestNoResponseBodyReturnValueList]
        self.sign = sign  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBodyReturnValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypt_props is not None:
            result['EncryptProps'] = self.encrypt_props
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.sign is not None:
            result['Sign'] = self.sign
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EncryptProps') is not None:
            self.encrypt_props = m.get('EncryptProps')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValueList()
                self.list.append(temp_model.from_map(k))
        if m.get('Sign') is not None:
            self.sign = m.get('Sign')
        return self


class QueryInvoiceInfoByRequestNoResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, is_success=None, return_value=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.return_value = return_value  # type: QueryInvoiceInfoByRequestNoResponseBodyReturnValue

    def validate(self):
        if self.return_value:
            self.return_value.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.return_value is not None:
            result['ReturnValue'] = self.return_value.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ReturnValue') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBodyReturnValue()
            self.return_value = temp_model.from_map(m['ReturnValue'])
        return self


class QueryInvoiceInfoByRequestNoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryInvoiceInfoByRequestNoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryInvoiceInfoByRequestNoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryInvoiceInfoByRequestNoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageCallbackInfoRequest(TeaModel):
    def __init__(self, biz_type=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMessageCallbackInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryMessageCallbackInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMessageCallbackInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMessageCallbackInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMessageCallbackInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMessageCallbackInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMessageCallbackInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMessageQueueListRequest(TeaModel):
    def __init__(self, biz_type=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMessageQueueListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryMessageQueueListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMessageQueueListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMessageQueueListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMessageQueueListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMessageQueueListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMessageQueueListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyBillInfoRequest(TeaModel):
    def __init__(self, bill_cycle=None, item_id=None, item_name=None, owner_id=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None, subject_item_id=None):
        self.bill_cycle = bill_cycle  # type: str
        self.item_id = item_id  # type: str
        self.item_name = item_name  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.subject_item_id = subject_item_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonthlyBillInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.item_name is not None:
            result['ItemName'] = self.item_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.subject_item_id is not None:
            result['SubjectItemId'] = self.subject_item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ItemName') is not None:
            self.item_name = m.get('ItemName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubjectItemId') is not None:
            self.subject_item_id = m.get('SubjectItemId')
        return self


class QueryMonthlyBillInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonthlyBillInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMonthlyBillInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMonthlyBillInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonthlyBillInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMonthlyBillInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyStatisticsInfoRequest(TeaModel):
    def __init__(self, bill_id=None, end_date=None, owner_id=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, start_date=None):
        self.bill_id = bill_id  # type: str
        self.end_date = end_date  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonthlyStatisticsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryMonthlyStatisticsInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonthlyStatisticsInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryMonthlyStatisticsInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMonthlyStatisticsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonthlyStatisticsInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMonthlyStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNoBuyTasksRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, page_no=None, page_size=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNoBuyTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryNoBuyTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None, message=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNoBuyTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class QueryNoBuyTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryNoBuyTasksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryNoBuyTasksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryNoBuyTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNoDistributeRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNoDistributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryNoDistributeResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryNoDistributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryNoDistributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryNoDistributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryNoDistributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryNoDistributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOpenStatusRequest(TeaModel):
    def __init__(self, bus_offer=None, owner_id=None, prod_code=None, prod_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bus_offer = bus_offer  # type: long
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.prod_id = prod_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOpenStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bus_offer is not None:
            result['BusOffer'] = self.bus_offer
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.prod_id is not None:
            result['ProdId'] = self.prod_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusOffer') is not None:
            self.bus_offer = m.get('BusOffer')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryOpenStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryOpenStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryOpenStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryOpenStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPackageDetailRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None, status=None):
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPackageDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPackageDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPackageDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPackageDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPackageDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPackageDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPackageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPackageListRequest(TeaModel):
    def __init__(self, bill_cycle=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_cycle = bill_cycle  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPackageListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPackageListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPackageListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPackageListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPackageListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPackageListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPackageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPackageStatisticsRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPackageStatisticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPackageStatisticsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPackageStatisticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPackageStatisticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPackageStatisticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPackageStatisticsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPackageStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolCityListRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolCityListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolCityListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolCityListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolCityListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPoolCityListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPoolCityListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolCityListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolInfoListRequest(TeaModel):
    def __init__(self, is_fuzzy_query=None, owner_id=None, page_no=None, page_size=None, pool_name=None,
                 prod_code=None, res_type=None, resource_owner_account=None, resource_owner_id=None, search_param=None):
        self.is_fuzzy_query = is_fuzzy_query  # type: bool
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.pool_name = pool_name  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.search_param = search_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_fuzzy_query is not None:
            result['IsFuzzyQuery'] = self.is_fuzzy_query
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.search_param is not None:
            result['SearchParam'] = self.search_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsFuzzyQuery') is not None:
            self.is_fuzzy_query = m.get('IsFuzzyQuery')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SearchParam') is not None:
            self.search_param = m.get('SearchParam')
        return self


class QueryPoolInfoListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolInfoListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPoolInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPoolInfoListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolMonthlyBillInfoRequest(TeaModel):
    def __init__(self, bill_cycle=None, bill_id=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_cycle = bill_cycle  # type: str
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolMonthlyBillInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolMonthlyBillInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolMonthlyBillInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryPoolMonthlyBillInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPoolMonthlyBillInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPoolMonthlyBillInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolMonthlyBillInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolStatisticsInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolStatisticsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolStatisticsInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolStatisticsInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolStatisticsInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPoolStatisticsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPoolStatisticsInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPoolSummaryInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolSummaryInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPoolSummaryInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPoolSummaryInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPoolSummaryInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPoolSummaryInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPoolSummaryInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPoolSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedInfoRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPurchasedInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryPurchasedInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPurchasedInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPurchasedInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPurchasedInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPurchasedInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPurchasedInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPurchasedResListRequest(TeaModel):
    def __init__(self, bill_id=None, city=None, is_display_pool=None, owner_id=None, page_no=None, page_size=None,
                 prod_code=None, res_bind_status=None, res_type=None, resource_owner_account=None, resource_owner_id=None,
                 secret_no=None):
        self.bill_id = bill_id  # type: str
        self.city = city  # type: str
        self.is_display_pool = is_display_pool  # type: bool
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.res_bind_status = res_bind_status  # type: int
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPurchasedResListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.city is not None:
            result['City'] = self.city
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_bind_status is not None:
            result['ResBindStatus'] = self.res_bind_status
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResBindStatus') is not None:
            self.res_bind_status = m.get('ResBindStatus')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class QueryPurchasedResListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPurchasedResListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryPurchasedResListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPurchasedResListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPurchasedResListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryPurchasedResListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryQRCodeInfoRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, secret_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_number = secret_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryQRCodeInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_number is not None:
            result['SecretNumber'] = self.secret_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNumber') is not None:
            self.secret_number = m.get('SecretNumber')
        return self


class QueryQRCodeInfoResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None, token=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryQRCodeInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class QueryQRCodeInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryQRCodeInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryQRCodeInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryQRCodeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordingUrlRequest(TeaModel):
    def __init__(self, bill_id=None, call_date=None, call_id=None, owner_id=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.call_date = call_date  # type: str
        self.call_id = call_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordingUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.call_date is not None:
            result['CallDate'] = self.call_date
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('CallDate') is not None:
            self.call_date = m.get('CallDate')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRecordingUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordingUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryRecordingUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordingUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordingUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRecordingUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResSummaryInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryResSummaryInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryResSummaryInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryResSummaryInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryResSummaryInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryResSummaryInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryResSummaryInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryResSummaryInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRingToneUrlRequest(TeaModel):
    def __init__(self, bill_id=None, file_key=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.file_key = file_key  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRingToneUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRingToneUrlResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRingToneUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryRingToneUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRingToneUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRingToneUrlResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRingToneUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRingTonesRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, page_no=None, page_size=None, play_type=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.play_type = play_type  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRingTonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.play_type is not None:
            result['PlayType'] = self.play_type
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlayType') is not None:
            self.play_type = m.get('PlayType')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRingTonesResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRingTonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryRingTonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRingTonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRingTonesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryRingTonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySimplePoolInfoListRequest(TeaModel):
    def __init__(self, owner_id=None, pool_name=None, prod_code=None, res_type=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.pool_name = pool_name  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySimplePoolInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QuerySimplePoolInfoListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySimplePoolInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QuerySimplePoolInfoListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySimplePoolInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySimplePoolInfoListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySimplePoolInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStatisticsInfoRequest(TeaModel):
    def __init__(self, bill_id=None, end_date=None, owner_id=None, page_no=None, page_size=None, prod_code=None,
                 res_type=None, resource_owner_account=None, resource_owner_id=None, start_date=None):
        self.bill_id = bill_id  # type: str
        self.end_date = end_date  # type: str
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_date = start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStatisticsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_date is not None:
            result['StartDate'] = self.start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')
        return self


class QueryStatisticsInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStatisticsInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryStatisticsInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStatisticsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStatisticsInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTagOpenStatusRequest(TeaModel):
    def __init__(self, attribute_key=None, biz_type=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, sub_attribute_key=None):
        self.attribute_key = attribute_key  # type: str
        self.biz_type = biz_type  # type: int
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.sub_attribute_key = sub_attribute_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTagOpenStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attribute_key is not None:
            result['AttributeKey'] = self.attribute_key
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.sub_attribute_key is not None:
            result['SubAttributeKey'] = self.sub_attribute_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttributeKey') is not None:
            self.attribute_key = m.get('AttributeKey')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SubAttributeKey') is not None:
            self.sub_attribute_key = m.get('SubAttributeKey')
        return self


class QueryTagOpenStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTagOpenStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTagOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTagOpenStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTagOpenStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTagOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferDetailsRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None, prod_code=None, record_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.record_id = record_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTransferDetailsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryTransferDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTransferDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTransferDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferRecordRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, record_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.record_id = record_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTransferRecordResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryTransferRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTransferRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTransferRecordResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTransferRecordsRequest(TeaModel):
    def __init__(self, owner_id=None, page_no=None, page_size=None, prod_code=None, record_id=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.prod_code = prod_code  # type: str
        self.record_id = record_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryTransferRecordsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTransferRecordsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryTransferRecordsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTransferRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTransferRecordsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTransferRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserDeleteStatusRequest(TeaModel):
    def __init__(self, bid=None, country=None, gmt_wakeup=None, hid=None, interrupt=None, invoker=None, level=None,
                 message=None, pk=None, prod_code=None, prompt=None, success=None, task_extra_data=None,
                 task_identifier=None, url=None):
        self.bid = bid  # type: str
        self.country = country  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.level = level  # type: long
        self.message = message  # type: str
        self.pk = pk  # type: str
        self.prod_code = prod_code  # type: str
        self.prompt = prompt  # type: str
        self.success = success  # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserDeleteStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryUserDeleteStatusResponseBody(TeaModel):
    def __init__(self, bid=None, country=None, gmt_wakeup=None, hid=None, interrupt=None, invoker=None, level=None,
                 message=None, pk=None, prompt=None, success=None, task_extra_data=None, task_identifier=None, url=None):
        self.bid = bid  # type: str
        self.country = country  # type: str
        self.gmt_wakeup = gmt_wakeup  # type: str
        self.hid = hid  # type: long
        self.interrupt = interrupt  # type: bool
        self.invoker = invoker  # type: str
        self.level = level  # type: long
        self.message = message  # type: str
        self.pk = pk  # type: str
        self.prompt = prompt  # type: str
        self.success = success  # type: bool
        self.task_extra_data = task_extra_data  # type: str
        self.task_identifier = task_identifier  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserDeleteStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryUserDeleteStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUserDeleteStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserDeleteStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUserDeleteStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryUserInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryUserInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUserInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserResPoolInfoRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserResPoolInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryUserResPoolInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUserResPoolInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryUserResPoolInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUserResPoolInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUserResPoolInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryUserResPoolInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVirtualOperationShowRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVirtualOperationShowRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryVirtualOperationShowResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVirtualOperationShowResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVirtualOperationShowResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryVirtualOperationShowResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVirtualOperationShowResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryVirtualOperationShowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWarningListRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWarningListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryWarningListResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWarningListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class QueryWarningListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryWarningListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWarningListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWarningListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWaybillOrderInfoRequest(TeaModel):
    def __init__(self, outer_order_code=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.outer_order_code = outer_order_code  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWaybillOrderInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryWaybillOrderInfoResponseBodyData(TeaModel):
    def __init__(self, aliyunprice=None, appoint_got_end_time=None, appoint_got_start_time=None, biz_type=None,
                 city=None, cp_code=None, got_code=None, last_logistic_detail=None, logistics_gmt_modified=None,
                 logistics_status=None, logistics_status_desc=None, mail_no=None, outer_order_code=None):
        self.aliyunprice = aliyunprice  # type: str
        self.appoint_got_end_time = appoint_got_end_time  # type: str
        self.appoint_got_start_time = appoint_got_start_time  # type: str
        self.biz_type = biz_type  # type: int
        self.city = city  # type: str
        self.cp_code = cp_code  # type: str
        self.got_code = got_code  # type: str
        self.last_logistic_detail = last_logistic_detail  # type: str
        self.logistics_gmt_modified = logistics_gmt_modified  # type: str
        self.logistics_status = logistics_status  # type: str
        self.logistics_status_desc = logistics_status_desc  # type: str
        self.mail_no = mail_no  # type: str
        self.outer_order_code = outer_order_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWaybillOrderInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyunprice is not None:
            result['Aliyunprice'] = self.aliyunprice
        if self.appoint_got_end_time is not None:
            result['AppointGotEndTime'] = self.appoint_got_end_time
        if self.appoint_got_start_time is not None:
            result['AppointGotStartTime'] = self.appoint_got_start_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.city is not None:
            result['City'] = self.city
        if self.cp_code is not None:
            result['CpCode'] = self.cp_code
        if self.got_code is not None:
            result['GotCode'] = self.got_code
        if self.last_logistic_detail is not None:
            result['LastLogisticDetail'] = self.last_logistic_detail
        if self.logistics_gmt_modified is not None:
            result['LogisticsGmtModified'] = self.logistics_gmt_modified
        if self.logistics_status is not None:
            result['LogisticsStatus'] = self.logistics_status
        if self.logistics_status_desc is not None:
            result['LogisticsStatusDesc'] = self.logistics_status_desc
        if self.mail_no is not None:
            result['MailNo'] = self.mail_no
        if self.outer_order_code is not None:
            result['OuterOrderCode'] = self.outer_order_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Aliyunprice') is not None:
            self.aliyunprice = m.get('Aliyunprice')
        if m.get('AppointGotEndTime') is not None:
            self.appoint_got_end_time = m.get('AppointGotEndTime')
        if m.get('AppointGotStartTime') is not None:
            self.appoint_got_start_time = m.get('AppointGotStartTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('CpCode') is not None:
            self.cp_code = m.get('CpCode')
        if m.get('GotCode') is not None:
            self.got_code = m.get('GotCode')
        if m.get('LastLogisticDetail') is not None:
            self.last_logistic_detail = m.get('LastLogisticDetail')
        if m.get('LogisticsGmtModified') is not None:
            self.logistics_gmt_modified = m.get('LogisticsGmtModified')
        if m.get('LogisticsStatus') is not None:
            self.logistics_status = m.get('LogisticsStatus')
        if m.get('LogisticsStatusDesc') is not None:
            self.logistics_status_desc = m.get('LogisticsStatusDesc')
        if m.get('MailNo') is not None:
            self.mail_no = m.get('MailNo')
        if m.get('OuterOrderCode') is not None:
            self.outer_order_code = m.get('OuterOrderCode')
        return self


class QueryWaybillOrderInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: QueryWaybillOrderInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryWaybillOrderInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryWaybillOrderInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryWaybillOrderInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryWaybillOrderInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWaybillOrderInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWaybillOrderInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryWaybillOrderStatisticsInfoRequest(TeaModel):
    def __init__(self, end_time=None, granularity=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None):
        self.end_time = end_time  # type: str
        self.granularity = granularity  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWaybillOrderStatisticsInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryWaybillOrderStatisticsInfoResponseBodyData(TeaModel):
    def __init__(self, aliyunprice_amount=None, cancel_count=None, gmt_create=None, got_count=None,
                 order_total=None):
        self.aliyunprice_amount = aliyunprice_amount  # type: float
        self.cancel_count = cancel_count  # type: int
        self.gmt_create = gmt_create  # type: str
        self.got_count = got_count  # type: int
        self.order_total = order_total  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryWaybillOrderStatisticsInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyunprice_amount is not None:
            result['AliyunpriceAmount'] = self.aliyunprice_amount
        if self.cancel_count is not None:
            result['CancelCount'] = self.cancel_count
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.got_count is not None:
            result['GotCount'] = self.got_count
        if self.order_total is not None:
            result['OrderTotal'] = self.order_total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliyunpriceAmount') is not None:
            self.aliyunprice_amount = m.get('AliyunpriceAmount')
        if m.get('CancelCount') is not None:
            self.cancel_count = m.get('CancelCount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GotCount') is not None:
            self.got_count = m.get('GotCount')
        if m.get('OrderTotal') is not None:
            self.order_total = m.get('OrderTotal')
        return self


class QueryWaybillOrderStatisticsInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[QueryWaybillOrderStatisticsInfoResponseBodyData]
        self.http_status_code = http_status_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryWaybillOrderStatisticsInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = QueryWaybillOrderStatisticsInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryWaybillOrderStatisticsInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryWaybillOrderStatisticsInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryWaybillOrderStatisticsInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryWaybillOrderStatisticsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseResourceRequest(TeaModel):
    def __init__(self, bill_id=None, is_display_pool=None, owner_id=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.is_display_pool = is_display_pool  # type: bool
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.is_display_pool is not None:
            result['IsDisplayPool'] = self.is_display_pool
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('IsDisplayPool') is not None:
            self.is_display_pool = m.get('IsDisplayPool')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class ReleaseResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ReleaseResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReleaseResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TestTtsRingToneRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None, tts=None, voice_speed=None, voice_style=None, voice_type=None, voice_volume=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.tts = tts  # type: str
        self.voice_speed = voice_speed  # type: str
        self.voice_style = voice_style  # type: str
        self.voice_type = voice_type  # type: str
        self.voice_volume = voice_volume  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestTtsRingToneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.tts is not None:
            result['Tts'] = self.tts
        if self.voice_speed is not None:
            result['VoiceSpeed'] = self.voice_speed
        if self.voice_style is not None:
            result['VoiceStyle'] = self.voice_style
        if self.voice_type is not None:
            result['VoiceType'] = self.voice_type
        if self.voice_volume is not None:
            result['VoiceVolume'] = self.voice_volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Tts') is not None:
            self.tts = m.get('Tts')
        if m.get('VoiceSpeed') is not None:
            self.voice_speed = m.get('VoiceSpeed')
        if m.get('VoiceStyle') is not None:
            self.voice_style = m.get('VoiceStyle')
        if m.get('VoiceType') is not None:
            self.voice_type = m.get('VoiceType')
        if m.get('VoiceVolume') is not None:
            self.voice_volume = m.get('VoiceVolume')
        return self


class TestTtsRingToneResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TestTtsRingToneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class TestTtsRingToneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TestTtsRingToneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TestTtsRingToneResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TestTtsRingToneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindResourceRequest(TeaModel):
    def __init__(self, bill_id=None, bind_ids=None, owner_id=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.bind_ids = bind_ids  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.bind_ids is not None:
            result['BindIds'] = self.bind_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BindIds') is not None:
            self.bind_ids = m.get('BindIds')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnbindResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UnbindResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockResourceRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, resource_owner_account=None,
                 resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UnlockResourceResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UnlockResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockResourceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnlockResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContactsRequest(TeaModel):
    def __init__(self, bill_id=None, id=None, name=None, owner_id=None, phone_number=None, prod_code=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.id = id  # type: long
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContactsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateContactsResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateContactsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateContactsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateContactsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateContactsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateContactsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupDetailRequest(TeaModel):
    def __init__(self, group_id=None, id=None, owner_id=None, pool_key=None, prod_code=None, remark=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.group_id = group_id  # type: str
        self.id = id  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.id is not None:
            result['Id'] = self.id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateGroupDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateGroupDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGroupDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupDetailResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupInfoRequest(TeaModel):
    def __init__(self, id=None, name=None, owner_id=None, pool_key=None, prod_code=None, remark=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.id = id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_key = pool_key  # type: str
        self.prod_code = prod_code  # type: str
        self.remark = remark  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_key is not None:
            result['PoolKey'] = self.pool_key
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolKey') is not None:
            self.pool_key = m.get('PoolKey')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateGroupInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGroupInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateGroupInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGroupInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGroupInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePoolNameRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, pool_name=None, prod_code=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.pool_name = pool_name  # type: str
        self.prod_code = prod_code  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePoolNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.pool_name is not None:
            result['PoolName'] = self.pool_name
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PoolName') is not None:
            self.pool_name = m.get('PoolName')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdatePoolNameResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePoolNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdatePoolNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePoolNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePoolNameResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePoolNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResRemarkRequest(TeaModel):
    def __init__(self, bill_id=None, owner_id=None, prod_code=None, remark=None, res_type=None,
                 resource_owner_account=None, resource_owner_id=None, secret_no=None):
        self.bill_id = bill_id  # type: str
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.remark = remark  # type: str
        self.res_type = res_type  # type: int
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.secret_no = secret_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResRemarkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.res_type is not None:
            result['ResType'] = self.res_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.secret_no is not None:
            result['SecretNo'] = self.secret_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ResType') is not None:
            self.res_type = m.get('ResType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SecretNo') is not None:
            self.secret_no = m.get('SecretNo')
        return self


class UpdateResRemarkResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResRemarkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class UpdateResRemarkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResRemarkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResRemarkResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResRemarkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateOrderRequest(TeaModel):
    def __init__(self, owner_id=None, prod_code=None, resource_owner_account=None, resource_owner_id=None,
                 data=None):
        self.owner_id = owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class ValidateOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ValidateOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ValidateOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ValidateOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ValidateOrderResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


