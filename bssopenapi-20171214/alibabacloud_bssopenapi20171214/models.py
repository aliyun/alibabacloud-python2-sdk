# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AllocateCostUnitResourceRequestResourceInstanceList(TeaModel):
    def __init__(self, apportion_code=None, commodity_code=None, resource_id=None, resource_user_id=None):
        self.apportion_code = apportion_code  # type: str
        self.commodity_code = commodity_code  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_user_id = resource_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')
        return self


class AllocateCostUnitResourceRequest(TeaModel):
    def __init__(self, from_unit_user_id=None, from_unit_id=None, to_unit_user_id=None, to_unit_id=None,
                 resource_instance_list=None):
        self.from_unit_user_id = from_unit_user_id  # type: long
        self.from_unit_id = from_unit_id  # type: long
        self.to_unit_user_id = to_unit_user_id  # type: long
        self.to_unit_id = to_unit_id  # type: long
        self.resource_instance_list = resource_instance_list  # type: list[AllocateCostUnitResourceRequestResourceInstanceList]

    def validate(self):
        if self.resource_instance_list:
            for k in self.resource_instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.from_unit_user_id is not None:
            result['FromUnitUserId'] = self.from_unit_user_id
        if self.from_unit_id is not None:
            result['FromUnitId'] = self.from_unit_id
        if self.to_unit_user_id is not None:
            result['ToUnitUserId'] = self.to_unit_user_id
        if self.to_unit_id is not None:
            result['ToUnitId'] = self.to_unit_id
        result['ResourceInstanceList'] = []
        if self.resource_instance_list is not None:
            for k in self.resource_instance_list:
                result['ResourceInstanceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromUnitUserId') is not None:
            self.from_unit_user_id = m.get('FromUnitUserId')
        if m.get('FromUnitId') is not None:
            self.from_unit_id = m.get('FromUnitId')
        if m.get('ToUnitUserId') is not None:
            self.to_unit_user_id = m.get('ToUnitUserId')
        if m.get('ToUnitId') is not None:
            self.to_unit_id = m.get('ToUnitId')
        self.resource_instance_list = []
        if m.get('ResourceInstanceList') is not None:
            for k in m.get('ResourceInstanceList'):
                temp_model = AllocateCostUnitResourceRequestResourceInstanceList()
                self.resource_instance_list.append(temp_model.from_map(k))
        return self


class AllocateCostUnitResourceResponseBodyData(TeaModel):
    def __init__(self, is_success=None, to_unit_id=None, to_unit_user_id=None):
        self.is_success = is_success  # type: bool
        self.to_unit_id = to_unit_id  # type: long
        self.to_unit_user_id = to_unit_user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.to_unit_id is not None:
            result['ToUnitId'] = self.to_unit_id
        if self.to_unit_user_id is not None:
            result['ToUnitUserId'] = self.to_unit_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ToUnitId') is not None:
            self.to_unit_id = m.get('ToUnitId')
        if m.get('ToUnitUserId') is not None:
            self.to_unit_user_id = m.get('ToUnitUserId')
        return self


class AllocateCostUnitResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: AllocateCostUnitResourceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = AllocateCostUnitResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AllocateCostUnitResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AllocateCostUnitResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AllocateCostUnitResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyInvoiceRequest(TeaModel):
    def __init__(self, invoice_amount=None, owner_id=None, customer_id=None, address_id=None, invoicing_type=None,
                 process_way=None, apply_user_nick=None, invoice_by_amount=None, selected_ids=None):
        self.invoice_amount = invoice_amount  # type: long
        self.owner_id = owner_id  # type: long
        self.customer_id = customer_id  # type: long
        self.address_id = address_id  # type: long
        self.invoicing_type = invoicing_type  # type: int
        self.process_way = process_way  # type: int
        self.apply_user_nick = apply_user_nick  # type: str
        self.invoice_by_amount = invoice_by_amount  # type: bool
        self.selected_ids = selected_ids  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.invoice_amount is not None:
            result['InvoiceAmount'] = self.invoice_amount
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id
        if self.address_id is not None:
            result['AddressId'] = self.address_id
        if self.invoicing_type is not None:
            result['InvoicingType'] = self.invoicing_type
        if self.process_way is not None:
            result['ProcessWay'] = self.process_way
        if self.apply_user_nick is not None:
            result['ApplyUserNick'] = self.apply_user_nick
        if self.invoice_by_amount is not None:
            result['InvoiceByAmount'] = self.invoice_by_amount
        if self.selected_ids is not None:
            result['SelectedIds'] = self.selected_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvoiceAmount') is not None:
            self.invoice_amount = m.get('InvoiceAmount')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')
        if m.get('AddressId') is not None:
            self.address_id = m.get('AddressId')
        if m.get('InvoicingType') is not None:
            self.invoicing_type = m.get('InvoicingType')
        if m.get('ProcessWay') is not None:
            self.process_way = m.get('ProcessWay')
        if m.get('ApplyUserNick') is not None:
            self.apply_user_nick = m.get('ApplyUserNick')
        if m.get('InvoiceByAmount') is not None:
            self.invoice_by_amount = m.get('InvoiceByAmount')
        if m.get('SelectedIds') is not None:
            self.selected_ids = m.get('SelectedIds')
        return self


class ApplyInvoiceResponseBodyData(TeaModel):
    def __init__(self, invoice_apply_id=None):
        self.invoice_apply_id = invoice_apply_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.invoice_apply_id is not None:
            result['InvoiceApplyId'] = self.invoice_apply_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvoiceApplyId') is not None:
            self.invoice_apply_id = m.get('InvoiceApplyId')
        return self


class ApplyInvoiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ApplyInvoiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ApplyInvoiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ApplyInvoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyInvoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ApplyInvoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRequest(TeaModel):
    def __init__(self, order_id=None, owner_id=None):
        self.order_id = order_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class CancelOrderResponseBodyData(TeaModel):
    def __init__(self, host_id=None):
        self.host_id = host_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        return self


class CancelOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CancelOrderResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CancelOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResellerConsumeAmountRequest(TeaModel):
    def __init__(self, owner_id=None, adjust_type=None, amount=None, currency=None, business_type=None, source=None,
                 out_biz_id=None, extend_map=None):
        self.owner_id = owner_id  # type: long
        self.adjust_type = adjust_type  # type: str
        self.amount = amount  # type: str
        self.currency = currency  # type: str
        self.business_type = business_type  # type: str
        self.source = source  # type: str
        self.out_biz_id = out_biz_id  # type: str
        self.extend_map = extend_map  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.adjust_type is not None:
            result['AdjustType'] = self.adjust_type
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.source is not None:
            result['Source'] = self.source
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        if self.extend_map is not None:
            result['ExtendMap'] = self.extend_map
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AdjustType') is not None:
            self.adjust_type = m.get('AdjustType')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        if m.get('ExtendMap') is not None:
            self.extend_map = m.get('ExtendMap')
        return self


class ChangeResellerConsumeAmountResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class ChangeResellerConsumeAmountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ChangeResellerConsumeAmountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ChangeResellerConsumeAmountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConvertChargeTypeRequest(TeaModel):
    def __init__(self, owner_id=None, product_type=None, subscription_type=None, period=None, product_code=None,
                 instance_id=None):
        self.owner_id = owner_id  # type: long
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.period = period  # type: int
        self.product_code = product_code  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.period is not None:
            result['Period'] = self.period
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ConvertChargeTypeResponseBodyData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ConvertChargeTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ConvertChargeTypeResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ConvertChargeTypeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ConvertChargeTypeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConvertChargeTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConvertChargeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAgAccountRequest(TeaModel):
    def __init__(self, login_email=None, account_attr=None, enterprise_name=None, first_name=None, last_name=None,
                 nation_code=None, province_name=None, city_name=None, postcode=None):
        self.login_email = login_email  # type: str
        self.account_attr = account_attr  # type: str
        self.enterprise_name = enterprise_name  # type: str
        self.first_name = first_name  # type: str
        self.last_name = last_name  # type: str
        self.nation_code = nation_code  # type: str
        self.province_name = province_name  # type: str
        self.city_name = city_name  # type: str
        self.postcode = postcode  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email
        if self.account_attr is not None:
            result['AccountAttr'] = self.account_attr
        if self.enterprise_name is not None:
            result['EnterpriseName'] = self.enterprise_name
        if self.first_name is not None:
            result['FirstName'] = self.first_name
        if self.last_name is not None:
            result['LastName'] = self.last_name
        if self.nation_code is not None:
            result['NationCode'] = self.nation_code
        if self.province_name is not None:
            result['ProvinceName'] = self.province_name
        if self.city_name is not None:
            result['CityName'] = self.city_name
        if self.postcode is not None:
            result['Postcode'] = self.postcode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')
        if m.get('AccountAttr') is not None:
            self.account_attr = m.get('AccountAttr')
        if m.get('EnterpriseName') is not None:
            self.enterprise_name = m.get('EnterpriseName')
        if m.get('FirstName') is not None:
            self.first_name = m.get('FirstName')
        if m.get('LastName') is not None:
            self.last_name = m.get('LastName')
        if m.get('NationCode') is not None:
            self.nation_code = m.get('NationCode')
        if m.get('ProvinceName') is not None:
            self.province_name = m.get('ProvinceName')
        if m.get('CityName') is not None:
            self.city_name = m.get('CityName')
        if m.get('Postcode') is not None:
            self.postcode = m.get('Postcode')
        return self


class CreateAgAccountResponseBodyAgRelationDto(TeaModel):
    def __init__(self, mpk=None, pk=None, ram_admin_role_name=None, type=None):
        self.mpk = mpk  # type: str
        self.pk = pk  # type: str
        self.ram_admin_role_name = ram_admin_role_name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.ram_admin_role_name is not None:
            result['RamAdminRoleName'] = self.ram_admin_role_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('RamAdminRoleName') is not None:
            self.ram_admin_role_name = m.get('RamAdminRoleName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAgAccountResponseBody(TeaModel):
    def __init__(self, ag_relation_dto=None, code=None, message=None, request_id=None, success=None):
        self.ag_relation_dto = ag_relation_dto  # type: CreateAgAccountResponseBodyAgRelationDto
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.ag_relation_dto:
            self.ag_relation_dto.validate()

    def to_map(self):
        result = dict()
        if self.ag_relation_dto is not None:
            result['AgRelationDto'] = self.ag_relation_dto.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgRelationDto') is not None:
            temp_model = CreateAgAccountResponseBodyAgRelationDto()
            self.ag_relation_dto = temp_model.from_map(m['AgRelationDto'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateAgAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAgAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAgAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCostUnitRequestUnitEntityList(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_name=None):
        self.owner_uid = owner_uid  # type: long
        self.parent_unit_id = parent_unit_id  # type: long
        self.unit_name = unit_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class CreateCostUnitRequest(TeaModel):
    def __init__(self, unit_entity_list=None):
        self.unit_entity_list = unit_entity_list  # type: list[CreateCostUnitRequestUnitEntityList]

    def validate(self):
        if self.unit_entity_list:
            for k in self.unit_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k in self.unit_entity_list:
                result['UnitEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.unit_entity_list = []
        if m.get('UnitEntityList') is not None:
            for k in m.get('UnitEntityList'):
                temp_model = CreateCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k))
        return self


class CreateCostUnitResponseBodyDataCostUnitDtoList(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_id=None, unit_name=None):
        self.owner_uid = owner_uid  # type: long
        self.parent_unit_id = parent_unit_id  # type: long
        self.unit_id = unit_id  # type: long
        self.unit_name = unit_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class CreateCostUnitResponseBodyData(TeaModel):
    def __init__(self, cost_unit_dto_list=None):
        self.cost_unit_dto_list = cost_unit_dto_list  # type: list[CreateCostUnitResponseBodyDataCostUnitDtoList]

    def validate(self):
        if self.cost_unit_dto_list:
            for k in self.cost_unit_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cost_unit_dto_list = []
        if m.get('CostUnitDtoList') is not None:
            for k in m.get('CostUnitDtoList'):
                temp_model = CreateCostUnitResponseBodyDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k))
        return self


class CreateCostUnitResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateCostUnitResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CreateCostUnitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCostUnitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCostUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestParameter(TeaModel):
    def __init__(self, code=None, value=None):
        self.code = code  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, product_code=None, owner_id=None, product_type=None, subscription_type=None, period=None,
                 renewal_status=None, renew_period=None, client_token=None, parameter=None):
        self.product_code = product_code  # type: str
        self.owner_id = owner_id  # type: long
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.period = period  # type: int
        self.renewal_status = renewal_status  # type: str
        self.renew_period = renew_period  # type: int
        self.client_token = client_token  # type: str
        self.parameter = parameter  # type: list[CreateInstanceRequestParameter]

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.period is not None:
            result['Period'] = self.period
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = CreateInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class CreateInstanceResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateInstanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CreateInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResellerUserQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, amount=None, currency=None, out_biz_id=None):
        self.owner_id = owner_id  # type: long
        self.amount = amount  # type: str
        self.currency = currency  # type: str
        self.out_biz_id = out_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        return self


class CreateResellerUserQuotaResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class CreateResellerUserQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateResellerUserQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateResellerUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourcePackageRequest(TeaModel):
    def __init__(self, owner_id=None, product_code=None, package_type=None, effective_date=None, specification=None,
                 duration=None, pricing_cycle=None):
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.package_type = package_type  # type: str
        self.effective_date = effective_date  # type: str
        self.specification = specification  # type: str
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class CreateResourcePackageResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateResourcePackageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, order_id=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateResourcePackageResponseBodyData
        self.message = message  # type: str
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
            temp_model = CreateResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCostUnitRequest(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None):
        self.owner_uid = owner_uid  # type: long
        self.unit_id = unit_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        return self


class DeleteCostUnitResponseBodyData(TeaModel):
    def __init__(self, is_success=None, owner_uid=None, unit_id=None):
        self.is_success = is_success  # type: bool
        self.owner_uid = owner_uid  # type: long
        self.unit_id = unit_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        return self


class DeleteCostUnitResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteCostUnitResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DeleteCostUnitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCostUnitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteCostUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeResourcePackageProductRequest(TeaModel):
    def __init__(self, product_code=None):
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties(TeaModel):
    def __init__(self, property=None):
        self.property = property  # type: list[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty]

    def validate(self):
        if self.property:
            for k in self.property:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Property'] = []
        if self.property is not None:
            for k in self.property:
                result['Property'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.property = []
        if m.get('Property') is not None:
            for k in m.get('Property'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypePropertiesProperty()
                self.property.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration(TeaModel):
    def __init__(self, name=None, unit=None, value=None):
        self.name = name  # type: str
        self.unit = unit  # type: str
        self.value = value  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations(TeaModel):
    def __init__(self, available_duration=None):
        self.available_duration = available_duration  # type: list[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration]

    def validate(self):
        if self.available_duration:
            for k in self.available_duration:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AvailableDuration'] = []
        if self.available_duration is not None:
            for k in self.available_duration:
                result['AvailableDuration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_duration = []
        if m.get('AvailableDuration') is not None:
            for k in m.get('AvailableDuration'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurationsAvailableDuration()
                self.available_duration.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification(TeaModel):
    def __init__(self, available_durations=None, name=None, value=None):
        self.available_durations = available_durations  # type: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        if self.available_durations:
            self.available_durations.validate()

    def to_map(self):
        result = dict()
        if self.available_durations is not None:
            result['AvailableDurations'] = self.available_durations.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableDurations') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecificationAvailableDurations()
            self.available_durations = temp_model.from_map(m['AvailableDurations'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications(TeaModel):
    def __init__(self, specification=None):
        self.specification = specification  # type: list[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification]

    def validate(self):
        if self.specification:
            for k in self.specification:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Specification'] = []
        if self.specification is not None:
            for k in self.specification:
                result['Specification'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.specification = []
        if m.get('Specification') is not None:
            for k in m.get('Specification'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecificationsSpecification()
                self.specification.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType(TeaModel):
    def __init__(self, code=None, name=None, properties=None, specifications=None):
        self.code = code  # type: str
        self.name = name  # type: str
        self.properties = properties  # type: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties
        self.specifications = specifications  # type: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications

    def validate(self):
        if self.properties:
            self.properties.validate()
        if self.specifications:
            self.specifications.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.properties is not None:
            result['Properties'] = self.properties.to_map()
        if self.specifications is not None:
            result['Specifications'] = self.specifications.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Properties') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeProperties()
            self.properties = temp_model.from_map(m['Properties'])
        if m.get('Specifications') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageTypeSpecifications()
            self.specifications = temp_model.from_map(m['Specifications'])
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes(TeaModel):
    def __init__(self, package_type=None):
        self.package_type = package_type  # type: list[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType]

    def validate(self):
        if self.package_type:
            for k in self.package_type:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PackageType'] = []
        if self.package_type is not None:
            for k in self.package_type:
                result['PackageType'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.package_type = []
        if m.get('PackageType') is not None:
            for k in m.get('PackageType'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypesPackageType()
                self.package_type.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage(TeaModel):
    def __init__(self, name=None, package_types=None, product_code=None, product_type=None):
        self.name = name  # type: str
        self.package_types = package_types  # type: DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        if self.package_types:
            self.package_types.validate()

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.package_types is not None:
            result['PackageTypes'] = self.package_types.to_map()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PackageTypes') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackagePackageTypes()
            self.package_types = temp_model.from_map(m['PackageTypes'])
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DescribeResourcePackageProductResponseBodyDataResourcePackages(TeaModel):
    def __init__(self, resource_package=None):
        self.resource_package = resource_package  # type: list[DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage]

    def validate(self):
        if self.resource_package:
            for k in self.resource_package:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ResourcePackage'] = []
        if self.resource_package is not None:
            for k in self.resource_package:
                result['ResourcePackage'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.resource_package = []
        if m.get('ResourcePackage') is not None:
            for k in m.get('ResourcePackage'):
                temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackagesResourcePackage()
                self.resource_package.append(temp_model.from_map(k))
        return self


class DescribeResourcePackageProductResponseBodyData(TeaModel):
    def __init__(self, resource_packages=None):
        self.resource_packages = resource_packages  # type: DescribeResourcePackageProductResponseBodyDataResourcePackages

    def validate(self):
        if self.resource_packages:
            self.resource_packages.validate()

    def to_map(self):
        result = dict()
        if self.resource_packages is not None:
            result['ResourcePackages'] = self.resource_packages.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourcePackages') is not None:
            temp_model = DescribeResourcePackageProductResponseBodyDataResourcePackages()
            self.resource_packages = temp_model.from_map(m['ResourcePackages'])
        return self


class DescribeResourcePackageProductResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, order_id=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeResourcePackageProductResponseBodyData
        self.message = message  # type: str
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
            temp_model = DescribeResourcePackageProductResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeResourcePackageProductResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeResourcePackageProductResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeResourcePackageProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSplitItemBillRequestTagFilter(TeaModel):
    def __init__(self, tag_values=None, tag_key=None):
        self.tag_values = tag_values  # type: list[str]
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class DescribeSplitItemBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 owner_id=None, next_token=None, max_results=None, bill_owner_id=None, instance_id=None, split_item_id=None,
                 tag_filter=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.owner_id = owner_id  # type: long
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.bill_owner_id = bill_owner_id  # type: long
        self.instance_id = instance_id  # type: str
        self.split_item_id = split_item_id  # type: str
        self.tag_filter = tag_filter  # type: list[DescribeSplitItemBillRequestTagFilter]

    def validate(self):
        if self.tag_filter:
            for k in self.tag_filter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id
        result['TagFilter'] = []
        if self.tag_filter is not None:
            for k in self.tag_filter:
                result['TagFilter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')
        self.tag_filter = []
        if m.get('TagFilter') is not None:
            for k in m.get('TagFilter'):
                temp_model = DescribeSplitItemBillRequestTagFilter()
                self.tag_filter.append(temp_model.from_map(k))
        return self


class DescribeSplitItemBillResponseBodyDataItems(TeaModel):
    def __init__(self, billing_date=None, instance_config=None, internet_ip=None, split_item_id=None, item=None,
                 split_account_id=None, tag=None, instance_id=None, currency=None, deducted_by_cash_coupons=None,
                 subscription_type=None, instance_spec=None, billing_item=None, deducted_by_coupons=None, region=None,
                 outstanding_amount=None, cost_unit=None, list_price_unit=None, resource_group=None, pip_code=None, pretax_amount=None,
                 service_period_unit=None, product_name=None, commodity_code=None, split_product_detail=None, nick_name=None,
                 product_detail=None, usage=None, intranet_ip=None, owner_id=None, split_commodity_code=None,
                 deducted_by_prepaid_card=None, usage_unit=None, payment_amount=None, invoice_discount=None,
                 deducted_by_resource_package=None, product_type=None, split_billing_cycle=None, service_period=None, split_item_name=None,
                 zone=None, list_price=None, pretax_gross_amount=None, split_account_name=None, product_code=None,
                 billing_type=None):
        self.billing_date = billing_date  # type: str
        self.instance_config = instance_config  # type: str
        self.internet_ip = internet_ip  # type: str
        self.split_item_id = split_item_id  # type: str
        self.item = item  # type: str
        self.split_account_id = split_account_id  # type: str
        self.tag = tag  # type: str
        self.instance_id = instance_id  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.subscription_type = subscription_type  # type: str
        self.instance_spec = instance_spec  # type: str
        self.billing_item = billing_item  # type: str
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.region = region  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.cost_unit = cost_unit  # type: str
        self.list_price_unit = list_price_unit  # type: str
        self.resource_group = resource_group  # type: str
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.service_period_unit = service_period_unit  # type: str
        self.product_name = product_name  # type: str
        self.commodity_code = commodity_code  # type: str
        self.split_product_detail = split_product_detail  # type: str
        self.nick_name = nick_name  # type: str
        self.product_detail = product_detail  # type: str
        self.usage = usage  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.owner_id = owner_id  # type: str
        self.split_commodity_code = split_commodity_code  # type: str
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.usage_unit = usage_unit  # type: str
        self.payment_amount = payment_amount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.deducted_by_resource_package = deducted_by_resource_package  # type: str
        self.product_type = product_type  # type: str
        self.split_billing_cycle = split_billing_cycle  # type: str
        self.service_period = service_period  # type: str
        self.split_item_name = split_item_name  # type: str
        self.zone = zone  # type: str
        self.list_price = list_price  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.split_account_name = split_account_name  # type: str
        self.product_code = product_code  # type: str
        self.billing_type = billing_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id
        if self.item is not None:
            result['Item'] = self.item
        if self.split_account_id is not None:
            result['SplitAccountID'] = self.split_account_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.region is not None:
            result['Region'] = self.region
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.split_product_detail is not None:
            result['SplitProductDetail'] = self.split_product_detail
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.split_commodity_code is not None:
            result['SplitCommodityCode'] = self.split_commodity_code
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.split_billing_cycle is not None:
            result['SplitBillingCycle'] = self.split_billing_cycle
        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period
        if self.split_item_name is not None:
            result['SplitItemName'] = self.split_item_name
        if self.zone is not None:
            result['Zone'] = self.zone
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.split_account_name is not None:
            result['SplitAccountName'] = self.split_account_name
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('SplitAccountID') is not None:
            self.split_account_id = m.get('SplitAccountID')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('SplitProductDetail') is not None:
            self.split_product_detail = m.get('SplitProductDetail')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('SplitCommodityCode') is not None:
            self.split_commodity_code = m.get('SplitCommodityCode')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SplitBillingCycle') is not None:
            self.split_billing_cycle = m.get('SplitBillingCycle')
        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')
        if m.get('SplitItemName') is not None:
            self.split_item_name = m.get('SplitItemName')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('SplitAccountName') is not None:
            self.split_account_name = m.get('SplitAccountName')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        return self


class DescribeSplitItemBillResponseBodyData(TeaModel):
    def __init__(self, items=None, next_token=None, billing_cycle=None, max_results=None, account_id=None,
                 total_count=None, account_name=None):
        self.items = items  # type: list[DescribeSplitItemBillResponseBodyDataItems]
        self.next_token = next_token  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.max_results = max_results  # type: int
        self.account_id = account_id  # type: str
        self.total_count = total_count  # type: int
        self.account_name = account_name  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = DescribeSplitItemBillResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        return self


class DescribeSplitItemBillResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: DescribeSplitItemBillResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeSplitItemBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeSplitItemBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeSplitItemBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSplitItemBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableBillGenerationRequest(TeaModel):
    def __init__(self, product_code=None, owner_id=None):
        self.product_code = product_code  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class EnableBillGenerationResponseBodyData(TeaModel):
    def __init__(self, boolean=None):
        self.boolean = boolean  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.boolean is not None:
            result['Boolean'] = self.boolean
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Boolean') is not None:
            self.boolean = m.get('Boolean')
        return self


class EnableBillGenerationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: EnableBillGenerationResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = EnableBillGenerationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableBillGenerationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableBillGenerationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableBillGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerAccountInfoRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetCustomerAccountInfoResponseBodyData(TeaModel):
    def __init__(self, account_type=None, credit_limit_status=None, hosting_status=None, is_certified=None,
                 login_email=None, mpk=None):
        self.account_type = account_type  # type: str
        self.credit_limit_status = credit_limit_status  # type: str
        self.hosting_status = hosting_status  # type: str
        self.is_certified = is_certified  # type: bool
        self.login_email = login_email  # type: str
        self.mpk = mpk  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.credit_limit_status is not None:
            result['CreditLimitStatus'] = self.credit_limit_status
        if self.hosting_status is not None:
            result['HostingStatus'] = self.hosting_status
        if self.is_certified is not None:
            result['IsCertified'] = self.is_certified
        if self.login_email is not None:
            result['LoginEmail'] = self.login_email
        if self.mpk is not None:
            result['Mpk'] = self.mpk
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('CreditLimitStatus') is not None:
            self.credit_limit_status = m.get('CreditLimitStatus')
        if m.get('HostingStatus') is not None:
            self.hosting_status = m.get('HostingStatus')
        if m.get('IsCertified') is not None:
            self.is_certified = m.get('IsCertified')
        if m.get('LoginEmail') is not None:
            self.login_email = m.get('LoginEmail')
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')
        return self


class GetCustomerAccountInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCustomerAccountInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetCustomerAccountInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomerAccountInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCustomerAccountInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCustomerAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerListResponseBodyData(TeaModel):
    def __init__(self, uid_list=None):
        self.uid_list = uid_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uid_list is not None:
            result['UidList'] = self.uid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UidList') is not None:
            self.uid_list = m.get('UidList')
        return self


class GetCustomerListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetCustomerListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetCustomerListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomerListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCustomerListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetCustomerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderDetailRequest(TeaModel):
    def __init__(self, order_id=None, owner_id=None):
        self.order_id = order_id  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class GetOrderDetailResponseBodyDataOrderListOrder(TeaModel):
    def __init__(self, after_tax_amount=None, config=None, create_time=None, currency=None, instance_ids=None,
                 operator=None, order_id=None, order_sub_type=None, order_type=None, original_config=None,
                 payment_currency=None, payment_status=None, payment_time=None, pretax_amount=None, pretax_amount_local=None,
                 pretax_gross_amount=None, product_code=None, product_type=None, quantity=None, region=None, related_order_id=None,
                 sub_order_id=None, subscription_type=None, tax=None, usage_end_time=None, usage_start_time=None):
        self.after_tax_amount = after_tax_amount  # type: str
        self.config = config  # type: str
        self.create_time = create_time  # type: str
        self.currency = currency  # type: str
        self.instance_ids = instance_ids  # type: str
        self.operator = operator  # type: str
        self.order_id = order_id  # type: str
        self.order_sub_type = order_sub_type  # type: str
        self.order_type = order_type  # type: str
        self.original_config = original_config  # type: str
        self.payment_currency = payment_currency  # type: str
        self.payment_status = payment_status  # type: str
        self.payment_time = payment_time  # type: str
        self.pretax_amount = pretax_amount  # type: str
        self.pretax_amount_local = pretax_amount_local  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.quantity = quantity  # type: str
        self.region = region  # type: str
        self.related_order_id = related_order_id  # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: str
        self.usage_end_time = usage_end_time  # type: str
        self.usage_start_time = usage_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_sub_type is not None:
            result['OrderSubType'] = self.order_sub_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.original_config is not None:
            result['OriginalConfig'] = self.original_config
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.region is not None:
            result['Region'] = self.region
        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderSubType') is not None:
            self.order_sub_type = m.get('OrderSubType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OriginalConfig') is not None:
            self.original_config = m.get('OriginalConfig')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        return self


class GetOrderDetailResponseBodyDataOrderList(TeaModel):
    def __init__(self, order=None):
        self.order = order  # type: list[GetOrderDetailResponseBodyDataOrderListOrder]

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k in m.get('Order'):
                temp_model = GetOrderDetailResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        return self


class GetOrderDetailResponseBodyData(TeaModel):
    def __init__(self, host_name=None, order_list=None, page_num=None, page_size=None, total_count=None):
        self.host_name = host_name  # type: str
        self.order_list = order_list  # type: GetOrderDetailResponseBodyDataOrderList
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OrderList') is not None:
            temp_model = GetOrderDetailResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetOrderDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetOrderDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetOrderDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOrderDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetOrderDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPayAsYouGoPriceRequestModuleList(TeaModel):
    def __init__(self, config=None, module_code=None, price_type=None):
        self.config = config  # type: str
        self.module_code = module_code  # type: str
        self.price_type = price_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        return self


class GetPayAsYouGoPriceRequest(TeaModel):
    def __init__(self, owner_id=None, product_code=None, product_type=None, subscription_type=None, region=None,
                 module_list=None):
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.region = region  # type: str
        self.module_list = module_list  # type: list[GetPayAsYouGoPriceRequestModuleList]

    def validate(self):
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.region is not None:
            result['Region'] = self.region
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        self.module_list = []
        if m.get('ModuleList') is not None:
            for k in m.get('ModuleList'):
                temp_model = GetPayAsYouGoPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k))
        return self


class GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail(TeaModel):
    def __init__(self, cost_after_discount=None, invoice_discount=None, module_code=None, original_cost=None,
                 unit_price=None):
        self.cost_after_discount = cost_after_discount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.module_code = module_code  # type: str
        self.original_cost = original_cost  # type: float
        self.unit_price = unit_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_after_discount is not None:
            result['CostAfterDiscount'] = self.cost_after_discount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostAfterDiscount') is not None:
            self.cost_after_discount = m.get('CostAfterDiscount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetPayAsYouGoPriceResponseBodyDataModuleDetails(TeaModel):
    def __init__(self, module_detail=None):
        self.module_detail = module_detail  # type: list[GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail]

    def validate(self):
        if self.module_detail:
            for k in self.module_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k in self.module_detail:
                result['ModuleDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.module_detail = []
        if m.get('ModuleDetail') is not None:
            for k in m.get('ModuleDetail'):
                temp_model = GetPayAsYouGoPriceResponseBodyDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k))
        return self


class GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail(TeaModel):
    def __init__(self, promotion_desc=None, promotion_id=None, promotion_name=None):
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: long
        self.promotion_name = promotion_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        return self


class GetPayAsYouGoPriceResponseBodyDataPromotionDetails(TeaModel):
    def __init__(self, promotion_detail=None):
        self.promotion_detail = promotion_detail  # type: list[GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail]

    def validate(self):
        if self.promotion_detail:
            for k in self.promotion_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k in self.promotion_detail:
                result['PromotionDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.promotion_detail = []
        if m.get('PromotionDetail') is not None:
            for k in m.get('PromotionDetail'):
                temp_model = GetPayAsYouGoPriceResponseBodyDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k))
        return self


class GetPayAsYouGoPriceResponseBodyData(TeaModel):
    def __init__(self, currency=None, module_details=None, promotion_details=None):
        self.currency = currency  # type: str
        self.module_details = module_details  # type: GetPayAsYouGoPriceResponseBodyDataModuleDetails
        self.promotion_details = promotion_details  # type: GetPayAsYouGoPriceResponseBodyDataPromotionDetails

    def validate(self):
        if self.module_details:
            self.module_details.validate()
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()
        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('ModuleDetails') is not None:
            temp_model = GetPayAsYouGoPriceResponseBodyDataModuleDetails()
            self.module_details = temp_model.from_map(m['ModuleDetails'])
        if m.get('PromotionDetails') is not None:
            temp_model = GetPayAsYouGoPriceResponseBodyDataPromotionDetails()
            self.promotion_details = temp_model.from_map(m['PromotionDetails'])
        return self


class GetPayAsYouGoPriceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetPayAsYouGoPriceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetPayAsYouGoPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPayAsYouGoPriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetPayAsYouGoPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetPayAsYouGoPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePackagePriceRequest(TeaModel):
    def __init__(self, owner_id=None, product_code=None, package_type=None, effective_date=None, specification=None,
                 duration=None, pricing_cycle=None, order_type=None, instance_id=None):
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.package_type = package_type  # type: str
        self.effective_date = effective_date  # type: str
        self.specification = specification  # type: str
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str
        self.order_type = order_type  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetResourcePackagePriceResponseBodyDataPromotionsPromotion(TeaModel):
    def __init__(self, id=None, name=None):
        self.id = id  # type: long
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetResourcePackagePriceResponseBodyDataPromotions(TeaModel):
    def __init__(self, promotion=None):
        self.promotion = promotion  # type: list[GetResourcePackagePriceResponseBodyDataPromotionsPromotion]

    def validate(self):
        if self.promotion:
            for k in self.promotion:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Promotion'] = []
        if self.promotion is not None:
            for k in self.promotion:
                result['Promotion'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.promotion = []
        if m.get('Promotion') is not None:
            for k in m.get('Promotion'):
                temp_model = GetResourcePackagePriceResponseBodyDataPromotionsPromotion()
                self.promotion.append(temp_model.from_map(k))
        return self


class GetResourcePackagePriceResponseBodyData(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, promotions=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.promotions = promotions  # type: GetResourcePackagePriceResponseBodyDataPromotions
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.promotions:
            self.promotions.validate()

    def to_map(self):
        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.promotions is not None:
            result['Promotions'] = self.promotions.to_map()
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('Promotions') is not None:
            temp_model = GetResourcePackagePriceResponseBodyDataPromotions()
            self.promotions = temp_model.from_map(m['Promotions'])
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePackagePriceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetResourcePackagePriceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetResourcePackagePriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResourcePackagePriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetResourcePackagePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetResourcePackagePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubscriptionPriceRequestModuleList(TeaModel):
    def __init__(self, config=None, module_code=None, module_status=None, tag=None):
        self.config = config  # type: str
        self.module_code = module_code  # type: str
        self.module_status = module_status  # type: int
        self.tag = tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.module_status is not None:
            result['ModuleStatus'] = self.module_status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('ModuleStatus') is not None:
            self.module_status = m.get('ModuleStatus')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetSubscriptionPriceRequest(TeaModel):
    def __init__(self, service_period_unit=None, subscription_type=None, owner_id=None, product_code=None,
                 order_type=None, service_period_quantity=None, product_type=None, region=None, instance_id=None,
                 quantity=None, module_list=None):
        self.service_period_unit = service_period_unit  # type: str
        self.subscription_type = subscription_type  # type: str
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.order_type = order_type  # type: str
        self.service_period_quantity = service_period_quantity  # type: int
        self.product_type = product_type  # type: str
        self.region = region  # type: str
        self.instance_id = instance_id  # type: str
        self.quantity = quantity  # type: int
        self.module_list = module_list  # type: list[GetSubscriptionPriceRequestModuleList]

    def validate(self):
        if self.module_list:
            for k in self.module_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.service_period_quantity is not None:
            result['ServicePeriodQuantity'] = self.service_period_quantity
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        result['ModuleList'] = []
        if self.module_list is not None:
            for k in self.module_list:
                result['ModuleList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('ServicePeriodQuantity') is not None:
            self.service_period_quantity = m.get('ServicePeriodQuantity')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        self.module_list = []
        if m.get('ModuleList') is not None:
            for k in m.get('ModuleList'):
                temp_model = GetSubscriptionPriceRequestModuleList()
                self.module_list.append(temp_model.from_map(k))
        return self


class GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail(TeaModel):
    def __init__(self, cost_after_discount=None, invoice_discount=None, module_code=None, original_cost=None,
                 unit_price=None):
        self.cost_after_discount = cost_after_discount  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.module_code = module_code  # type: str
        self.original_cost = original_cost  # type: float
        self.unit_price = unit_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_after_discount is not None:
            result['CostAfterDiscount'] = self.cost_after_discount
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.module_code is not None:
            result['ModuleCode'] = self.module_code
        if self.original_cost is not None:
            result['OriginalCost'] = self.original_cost
        if self.unit_price is not None:
            result['UnitPrice'] = self.unit_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostAfterDiscount') is not None:
            self.cost_after_discount = m.get('CostAfterDiscount')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')
        if m.get('OriginalCost') is not None:
            self.original_cost = m.get('OriginalCost')
        if m.get('UnitPrice') is not None:
            self.unit_price = m.get('UnitPrice')
        return self


class GetSubscriptionPriceResponseBodyDataModuleDetails(TeaModel):
    def __init__(self, module_detail=None):
        self.module_detail = module_detail  # type: list[GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail]

    def validate(self):
        if self.module_detail:
            for k in self.module_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ModuleDetail'] = []
        if self.module_detail is not None:
            for k in self.module_detail:
                result['ModuleDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.module_detail = []
        if m.get('ModuleDetail') is not None:
            for k in m.get('ModuleDetail'):
                temp_model = GetSubscriptionPriceResponseBodyDataModuleDetailsModuleDetail()
                self.module_detail.append(temp_model.from_map(k))
        return self


class GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail(TeaModel):
    def __init__(self, promotion_desc=None, promotion_id=None, promotion_name=None):
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: long
        self.promotion_name = promotion_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        return self


class GetSubscriptionPriceResponseBodyDataPromotionDetails(TeaModel):
    def __init__(self, promotion_detail=None):
        self.promotion_detail = promotion_detail  # type: list[GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail]

    def validate(self):
        if self.promotion_detail:
            for k in self.promotion_detail:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PromotionDetail'] = []
        if self.promotion_detail is not None:
            for k in self.promotion_detail:
                result['PromotionDetail'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.promotion_detail = []
        if m.get('PromotionDetail') is not None:
            for k in m.get('PromotionDetail'):
                temp_model = GetSubscriptionPriceResponseBodyDataPromotionDetailsPromotionDetail()
                self.promotion_detail.append(temp_model.from_map(k))
        return self


class GetSubscriptionPriceResponseBodyData(TeaModel):
    def __init__(self, currency=None, discount_price=None, module_details=None, original_price=None,
                 promotion_details=None, quantity=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.module_details = module_details  # type: GetSubscriptionPriceResponseBodyDataModuleDetails
        self.original_price = original_price  # type: float
        self.promotion_details = promotion_details  # type: GetSubscriptionPriceResponseBodyDataPromotionDetails
        self.quantity = quantity  # type: int
        self.trade_price = trade_price  # type: float

    def validate(self):
        if self.module_details:
            self.module_details.validate()
        if self.promotion_details:
            self.promotion_details.validate()

    def to_map(self):
        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.module_details is not None:
            result['ModuleDetails'] = self.module_details.to_map()
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.promotion_details is not None:
            result['PromotionDetails'] = self.promotion_details.to_map()
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('ModuleDetails') is not None:
            temp_model = GetSubscriptionPriceResponseBodyDataModuleDetails()
            self.module_details = temp_model.from_map(m['ModuleDetails'])
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('PromotionDetails') is not None:
            temp_model = GetSubscriptionPriceResponseBodyDataPromotionDetails()
            self.promotion_details = temp_model.from_map(m['PromotionDetails'])
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetSubscriptionPriceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetSubscriptionPriceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetSubscriptionPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubscriptionPriceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSubscriptionPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetSubscriptionPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyCostUnitRequestUnitEntityList(TeaModel):
    def __init__(self, new_unit_name=None, owner_uid=None, unit_id=None):
        self.new_unit_name = new_unit_name  # type: str
        self.owner_uid = owner_uid  # type: long
        self.unit_id = unit_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.new_unit_name is not None:
            result['NewUnitName'] = self.new_unit_name
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewUnitName') is not None:
            self.new_unit_name = m.get('NewUnitName')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        return self


class ModifyCostUnitRequest(TeaModel):
    def __init__(self, unit_entity_list=None):
        self.unit_entity_list = unit_entity_list  # type: list[ModifyCostUnitRequestUnitEntityList]

    def validate(self):
        if self.unit_entity_list:
            for k in self.unit_entity_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['UnitEntityList'] = []
        if self.unit_entity_list is not None:
            for k in self.unit_entity_list:
                result['UnitEntityList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.unit_entity_list = []
        if m.get('UnitEntityList') is not None:
            for k in m.get('UnitEntityList'):
                temp_model = ModifyCostUnitRequestUnitEntityList()
                self.unit_entity_list.append(temp_model.from_map(k))
        return self


class ModifyCostUnitResponseBodyData(TeaModel):
    def __init__(self, is_success=None, owner_uid=None, unit_id=None):
        self.is_success = is_success  # type: bool
        self.owner_uid = owner_uid  # type: long
        self.unit_id = unit_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        return self


class ModifyCostUnitResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ModifyCostUnitResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
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
                temp_model = ModifyCostUnitResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyCostUnitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyCostUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRequestParameter(TeaModel):
    def __init__(self, code=None, value=None):
        self.code = code  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(self, product_code=None, owner_id=None, product_type=None, subscription_type=None,
                 modify_type=None, instance_id=None, client_token=None, parameter=None):
        self.product_code = product_code  # type: str
        self.owner_id = owner_id  # type: long
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.modify_type = modify_type  # type: str
        self.instance_id = instance_id  # type: str
        self.client_token = client_token  # type: str
        self.parameter = parameter  # type: list[ModifyInstanceRequestParameter]

    def validate(self):
        if self.parameter:
            for k in self.parameter:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        result['Parameter'] = []
        if self.parameter is not None:
            for k in self.parameter:
                result['Parameter'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        self.parameter = []
        if m.get('Parameter') is not None:
            for k in m.get('Parameter'):
                temp_model = ModifyInstanceRequestParameter()
                self.parameter.append(temp_model.from_map(k))
        return self


class ModifyInstanceResponseBodyData(TeaModel):
    def __init__(self, host_id=None, order_id=None):
        self.host_id = host_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ModifyInstanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ModifyInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountBalanceResponseBodyData(TeaModel):
    def __init__(self, available_amount=None, available_cash_amount=None, credit_amount=None, currency=None,
                 mybank_credit_amount=None):
        self.available_amount = available_amount  # type: str
        self.available_cash_amount = available_cash_amount  # type: str
        self.credit_amount = credit_amount  # type: str
        self.currency = currency  # type: str
        self.mybank_credit_amount = mybank_credit_amount  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.available_amount is not None:
            result['AvailableAmount'] = self.available_amount
        if self.available_cash_amount is not None:
            result['AvailableCashAmount'] = self.available_cash_amount
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.mybank_credit_amount is not None:
            result['MybankCreditAmount'] = self.mybank_credit_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableAmount') is not None:
            self.available_amount = m.get('AvailableAmount')
        if m.get('AvailableCashAmount') is not None:
            self.available_cash_amount = m.get('AvailableCashAmount')
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('MybankCreditAmount') is not None:
            self.mybank_credit_amount = m.get('MybankCreditAmount')
        return self


class QueryAccountBalanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAccountBalanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAccountBalanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAccountBalanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAccountBalanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAccountBalanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, page_num=None, page_size=None, owner_id=None, is_group_by_product=None,
                 product_code=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.owner_id = owner_id  # type: long
        self.is_group_by_product = is_group_by_product  # type: bool
        self.product_code = product_code  # type: str
        self.bill_owner_id = bill_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.is_group_by_product is not None:
            result['IsGroupByProduct'] = self.is_group_by_product
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('IsGroupByProduct') is not None:
            self.is_group_by_product = m.get('IsGroupByProduct')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryAccountBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, cost_unit=None, currency=None, deducted_by_cash_coupons=None, deducted_by_coupons=None,
                 deducted_by_prepaid_card=None, invoice_discount=None, outstanding_amount=None, owner_id=None, owner_name=None,
                 payment_amount=None, pip_code=None, pretax_amount=None, pretax_gross_amount=None, product_code=None,
                 product_name=None, subscription_type=None):
        self.cost_unit = cost_unit  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.owner_id = owner_id  # type: str
        self.owner_name = owner_name  # type: str
        self.payment_amount = payment_amount  # type: float
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryAccountBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryAccountBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryAccountBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryAccountBillResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, billing_cycle=None, items=None, page_num=None,
                 page_size=None, total_count=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QueryAccountBillResponseBodyDataItems
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryAccountBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAccountBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAccountBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAccountBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAccountBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAccountBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAccountBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountTransactionDetailsRequest(TeaModel):
    def __init__(self, transaction_number=None, record_id=None, transaction_channel_sn=None,
                 create_time_start=None, create_time_end=None, transaction_type=None, transaction_channel=None, next_token=None,
                 max_results=None):
        self.transaction_number = transaction_number  # type: str
        self.record_id = record_id  # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.create_time_start = create_time_start  # type: str
        self.create_time_end = create_time_end  # type: str
        self.transaction_type = transaction_type  # type: str
        self.transaction_channel = transaction_channel  # type: str
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        return self


class QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList(TeaModel):
    def __init__(self, amount=None, balance=None, billing_cycle=None, fund_type=None, record_id=None, remarks=None,
                 transaction_account=None, transaction_channel=None, transaction_channel_sn=None, transaction_flow=None,
                 transaction_number=None, transaction_time=None, transaction_type=None):
        self.amount = amount  # type: str
        self.balance = balance  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.fund_type = fund_type  # type: str
        self.record_id = record_id  # type: str
        self.remarks = remarks  # type: str
        self.transaction_account = transaction_account  # type: str
        self.transaction_channel = transaction_channel  # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.transaction_flow = transaction_flow  # type: str
        self.transaction_number = transaction_number  # type: str
        self.transaction_time = transaction_time  # type: str
        self.transaction_type = transaction_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.transaction_flow is not None:
            result['TransactionFlow'] = self.transaction_flow
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('TransactionFlow') is not None:
            self.transaction_flow = m.get('TransactionFlow')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        return self


class QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList(TeaModel):
    def __init__(self, account_transactions_list=None):
        self.account_transactions_list = account_transactions_list  # type: list[QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList]

    def validate(self):
        if self.account_transactions_list:
            for k in self.account_transactions_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k in self.account_transactions_list:
                result['AccountTransactionsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account_transactions_list = []
        if m.get('AccountTransactionsList') is not None:
            for k in m.get('AccountTransactionsList'):
                temp_model = QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k))
        return self


class QueryAccountTransactionDetailsResponseBodyData(TeaModel):
    def __init__(self, account_name=None, account_transactions_list=None, max_results=None, next_token=None,
                 total_count=None):
        self.account_name = account_name  # type: str
        self.account_transactions_list = account_transactions_list  # type: QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountTransactionsList') is not None:
            temp_model = QueryAccountTransactionDetailsResponseBodyDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(m['AccountTransactionsList'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAccountTransactionDetailsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAccountTransactionDetailsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAccountTransactionDetailsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAccountTransactionDetailsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAccountTransactionDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAccountTransactionDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAccountTransactionsRequest(TeaModel):
    def __init__(self, transaction_number=None, record_id=None, transaction_channel_sn=None,
                 create_time_start=None, create_time_end=None, page_num=None, page_size=None):
        self.transaction_number = transaction_number  # type: str
        self.record_id = record_id  # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.create_time_start = create_time_start  # type: str
        self.create_time_end = create_time_end  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList(TeaModel):
    def __init__(self, amount=None, balance=None, billing_cycle=None, fund_type=None, record_id=None, remarks=None,
                 transaction_account=None, transaction_channel=None, transaction_channel_sn=None, transaction_flow=None,
                 transaction_number=None, transaction_time=None, transaction_type=None):
        self.amount = amount  # type: str
        self.balance = balance  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.fund_type = fund_type  # type: str
        self.record_id = record_id  # type: str
        self.remarks = remarks  # type: str
        self.transaction_account = transaction_account  # type: str
        self.transaction_channel = transaction_channel  # type: str
        self.transaction_channel_sn = transaction_channel_sn  # type: str
        self.transaction_flow = transaction_flow  # type: str
        self.transaction_number = transaction_number  # type: str
        self.transaction_time = transaction_time  # type: str
        self.transaction_type = transaction_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.fund_type is not None:
            result['FundType'] = self.fund_type
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.remarks is not None:
            result['Remarks'] = self.remarks
        if self.transaction_account is not None:
            result['TransactionAccount'] = self.transaction_account
        if self.transaction_channel is not None:
            result['TransactionChannel'] = self.transaction_channel
        if self.transaction_channel_sn is not None:
            result['TransactionChannelSN'] = self.transaction_channel_sn
        if self.transaction_flow is not None:
            result['TransactionFlow'] = self.transaction_flow
        if self.transaction_number is not None:
            result['TransactionNumber'] = self.transaction_number
        if self.transaction_time is not None:
            result['TransactionTime'] = self.transaction_time
        if self.transaction_type is not None:
            result['TransactionType'] = self.transaction_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('FundType') is not None:
            self.fund_type = m.get('FundType')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')
        if m.get('TransactionAccount') is not None:
            self.transaction_account = m.get('TransactionAccount')
        if m.get('TransactionChannel') is not None:
            self.transaction_channel = m.get('TransactionChannel')
        if m.get('TransactionChannelSN') is not None:
            self.transaction_channel_sn = m.get('TransactionChannelSN')
        if m.get('TransactionFlow') is not None:
            self.transaction_flow = m.get('TransactionFlow')
        if m.get('TransactionNumber') is not None:
            self.transaction_number = m.get('TransactionNumber')
        if m.get('TransactionTime') is not None:
            self.transaction_time = m.get('TransactionTime')
        if m.get('TransactionType') is not None:
            self.transaction_type = m.get('TransactionType')
        return self


class QueryAccountTransactionsResponseBodyDataAccountTransactionsList(TeaModel):
    def __init__(self, account_transactions_list=None):
        self.account_transactions_list = account_transactions_list  # type: list[QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList]

    def validate(self):
        if self.account_transactions_list:
            for k in self.account_transactions_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['AccountTransactionsList'] = []
        if self.account_transactions_list is not None:
            for k in self.account_transactions_list:
                result['AccountTransactionsList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.account_transactions_list = []
        if m.get('AccountTransactionsList') is not None:
            for k in m.get('AccountTransactionsList'):
                temp_model = QueryAccountTransactionsResponseBodyDataAccountTransactionsListAccountTransactionsList()
                self.account_transactions_list.append(temp_model.from_map(k))
        return self


class QueryAccountTransactionsResponseBodyData(TeaModel):
    def __init__(self, account_name=None, account_transactions_list=None, page_num=None, page_size=None,
                 total_count=None):
        self.account_name = account_name  # type: str
        self.account_transactions_list = account_transactions_list  # type: QueryAccountTransactionsResponseBodyDataAccountTransactionsList
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.account_transactions_list:
            self.account_transactions_list.validate()

    def to_map(self):
        result = dict()
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.account_transactions_list is not None:
            result['AccountTransactionsList'] = self.account_transactions_list.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('AccountTransactionsList') is not None:
            temp_model = QueryAccountTransactionsResponseBodyDataAccountTransactionsList()
            self.account_transactions_list = temp_model.from_map(m['AccountTransactionsList'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAccountTransactionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAccountTransactionsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAccountTransactionsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAccountTransactionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAccountTransactionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAccountTransactionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvailableInstancesRequest(TeaModel):
    def __init__(self, region=None, owner_id=None, page_num=None, page_size=None, product_code=None,
                 product_type=None, subscription_type=None, instance_ids=None, end_time_start=None, end_time_end=None,
                 create_time_start=None, create_time_end=None, renew_status=None):
        self.region = region  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.instance_ids = instance_ids  # type: str
        self.end_time_start = end_time_start  # type: str
        self.end_time_end = end_time_end  # type: str
        self.create_time_start = create_time_start  # type: str
        self.create_time_end = create_time_end  # type: str
        self.renew_status = renew_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids
        if self.end_time_start is not None:
            result['EndTimeStart'] = self.end_time_start
        if self.end_time_end is not None:
            result['EndTimeEnd'] = self.end_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')
        if m.get('EndTimeStart') is not None:
            self.end_time_start = m.get('EndTimeStart')
        if m.get('EndTimeEnd') is not None:
            self.end_time_end = m.get('EndTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        return self


class QueryAvailableInstancesResponseBodyDataInstanceList(TeaModel):
    def __init__(self, create_time=None, end_time=None, expected_release_time=None, instance_id=None, owner_id=None,
                 product_code=None, product_type=None, region=None, release_time=None, renew_status=None, renewal_duration=None,
                 renewal_duration_unit=None, seller=None, seller_id=None, status=None, stop_time=None, sub_status=None,
                 subscription_type=None):
        self.create_time = create_time  # type: str
        self.end_time = end_time  # type: str
        self.expected_release_time = expected_release_time  # type: str
        self.instance_id = instance_id  # type: str
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.region = region  # type: str
        self.release_time = release_time  # type: str
        self.renew_status = renew_status  # type: str
        self.renewal_duration = renewal_duration  # type: int
        self.renewal_duration_unit = renewal_duration_unit  # type: str
        self.seller = seller  # type: str
        self.seller_id = seller_id  # type: long
        self.status = status  # type: str
        self.stop_time = stop_time  # type: str
        self.sub_status = sub_status  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.expected_release_time is not None:
            result['ExpectedReleaseTime'] = self.expected_release_time
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.renew_status is not None:
            result['RenewStatus'] = self.renew_status
        if self.renewal_duration is not None:
            result['RenewalDuration'] = self.renewal_duration
        if self.renewal_duration_unit is not None:
            result['RenewalDurationUnit'] = self.renewal_duration_unit
        if self.seller is not None:
            result['Seller'] = self.seller
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.status is not None:
            result['Status'] = self.status
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExpectedReleaseTime') is not None:
            self.expected_release_time = m.get('ExpectedReleaseTime')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('RenewStatus') is not None:
            self.renew_status = m.get('RenewStatus')
        if m.get('RenewalDuration') is not None:
            self.renewal_duration = m.get('RenewalDuration')
        if m.get('RenewalDurationUnit') is not None:
            self.renewal_duration_unit = m.get('RenewalDurationUnit')
        if m.get('Seller') is not None:
            self.seller = m.get('Seller')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryAvailableInstancesResponseBodyData(TeaModel):
    def __init__(self, instance_list=None, page_num=None, page_size=None, total_count=None):
        self.instance_list = instance_list  # type: list[QueryAvailableInstancesResponseBodyDataInstanceList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instance_list:
            for k in self.instance_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['InstanceList'] = []
        if self.instance_list is not None:
            for k in self.instance_list:
                result['InstanceList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instance_list = []
        if m.get('InstanceList') is not None:
            for k in m.get('InstanceList'):
                temp_model = QueryAvailableInstancesResponseBodyDataInstanceList()
                self.instance_list.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryAvailableInstancesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAvailableInstancesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAvailableInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvailableInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAvailableInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryAvailableInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, type=None, product_code=None, product_type=None, subscription_type=None,
                 is_hide_zero_charge=None, is_display_local_currency=None, owner_id=None, page_num=None, page_size=None,
                 bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.type = type  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool
        self.is_display_local_currency = is_display_local_currency  # type: bool
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.bill_owner_id = bill_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.type is not None:
            result['Type'] = self.type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        if self.is_display_local_currency is not None:
            result['IsDisplayLocalCurrency'] = self.is_display_local_currency
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        if m.get('IsDisplayLocalCurrency') is not None:
            self.is_display_local_currency = m.get('IsDisplayLocalCurrency')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, after_tax_amount=None, commodity_code=None, currency=None, deducted_by_cash_coupons=None,
                 deducted_by_coupons=None, deducted_by_prepaid_card=None, invoice_discount=None, item=None, outstanding_amount=None,
                 owner_id=None, payment_amount=None, payment_currency=None, payment_time=None, payment_transaction_id=None,
                 pip_code=None, pretax_amount=None, pretax_amount_local=None, pretax_gross_amount=None, product_code=None,
                 product_detail=None, product_name=None, product_type=None, record_id=None, round_down_discount=None, status=None,
                 sub_order_id=None, subscription_type=None, tax=None, usage_end_time=None, usage_start_time=None):
        self.after_tax_amount = after_tax_amount  # type: float
        self.commodity_code = commodity_code  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.item = item  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.owner_id = owner_id  # type: str
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.payment_time = payment_time  # type: str
        self.payment_transaction_id = payment_transaction_id  # type: str
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_detail = product_detail  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.record_id = record_id  # type: str
        self.round_down_discount = round_down_discount  # type: str
        self.status = status  # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: float
        self.usage_end_time = usage_end_time  # type: str
        self.usage_start_time = usage_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.item is not None:
            result['Item'] = self.item
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.payment_transaction_id is not None:
            result['PaymentTransactionID'] = self.payment_transaction_id
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PaymentTransactionID') is not None:
            self.payment_transaction_id = m.get('PaymentTransactionID')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        return self


class QueryBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBillResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, billing_cycle=None, items=None, page_num=None,
                 page_size=None, total_count=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QueryBillResponseBodyDataItems
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBillOverviewRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.bill_owner_id = bill_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryBillOverviewResponseBodyDataItemsItem(TeaModel):
    def __init__(self, after_tax_amount=None, commodity_code=None, currency=None, deducted_by_cash_coupons=None,
                 deducted_by_coupons=None, deducted_by_prepaid_card=None, invoice_discount=None, item=None, outstanding_amount=None,
                 payment_amount=None, payment_currency=None, pip_code=None, pretax_amount=None, pretax_amount_local=None,
                 pretax_gross_amount=None, product_code=None, product_detail=None, product_name=None, product_type=None,
                 round_down_discount=None, subscription_type=None, tax=None):
        self.after_tax_amount = after_tax_amount  # type: float
        self.commodity_code = commodity_code  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.item = item  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_detail = product_detail  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.round_down_discount = round_down_discount  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.item is not None:
            result['Item'] = self.item
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        return self


class QueryBillOverviewResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryBillOverviewResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBillOverviewResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBillOverviewResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, billing_cycle=None, items=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QueryBillOverviewResponseBodyDataItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryBillOverviewResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryBillOverviewResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryBillOverviewResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryBillOverviewResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBillOverviewResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryBillOverviewResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBillOverviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryBillToOSSSubscriptionResponseBodyDataItemsItem(TeaModel):
    def __init__(self, bucket_owner_id=None, subscribe_bucket=None, subscribe_language=None, subscribe_time=None,
                 subscribe_type=None):
        self.bucket_owner_id = bucket_owner_id  # type: long
        self.subscribe_bucket = subscribe_bucket  # type: str
        self.subscribe_language = subscribe_language  # type: str
        self.subscribe_time = subscribe_time  # type: str
        self.subscribe_type = subscribe_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id
        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket
        if self.subscribe_language is not None:
            result['SubscribeLanguage'] = self.subscribe_language
        if self.subscribe_time is not None:
            result['SubscribeTime'] = self.subscribe_time
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')
        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')
        if m.get('SubscribeLanguage') is not None:
            self.subscribe_language = m.get('SubscribeLanguage')
        if m.get('SubscribeTime') is not None:
            self.subscribe_time = m.get('SubscribeTime')
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        return self


class QueryBillToOSSSubscriptionResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryBillToOSSSubscriptionResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryBillToOSSSubscriptionResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryBillToOSSSubscriptionResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, items=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.items = items  # type: QueryBillToOSSSubscriptionResponseBodyDataItems

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.items is not None:
            result['Items'] = self.items.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('Items') is not None:
            temp_model = QueryBillToOSSSubscriptionResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        return self


class QueryBillToOSSSubscriptionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryBillToOSSSubscriptionResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryBillToOSSSubscriptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryBillToOSSSubscriptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryBillToOSSSubscriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryBillToOSSSubscriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCashCouponsRequest(TeaModel):
    def __init__(self, expiry_time_end=None, expiry_time_start=None, effective_or_not=None):
        self.expiry_time_end = expiry_time_end  # type: str
        self.expiry_time_start = expiry_time_start  # type: str
        self.effective_or_not = effective_or_not  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')
        return self


class QueryCashCouponsResponseBodyDataCashCoupon(TeaModel):
    def __init__(self, applicable_products=None, applicable_scenarios=None, balance=None, cash_coupon_id=None,
                 cash_coupon_no=None, effective_time=None, expiry_time=None, granted_time=None, nominal_value=None, status=None):
        self.applicable_products = applicable_products  # type: str
        self.applicable_scenarios = applicable_scenarios  # type: str
        self.balance = balance  # type: str
        self.cash_coupon_id = cash_coupon_id  # type: long
        self.cash_coupon_no = cash_coupon_no  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.granted_time = granted_time  # type: str
        self.nominal_value = nominal_value  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products
        if self.applicable_scenarios is not None:
            result['ApplicableScenarios'] = self.applicable_scenarios
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.cash_coupon_id is not None:
            result['CashCouponId'] = self.cash_coupon_id
        if self.cash_coupon_no is not None:
            result['CashCouponNo'] = self.cash_coupon_no
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')
        if m.get('ApplicableScenarios') is not None:
            self.applicable_scenarios = m.get('ApplicableScenarios')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('CashCouponId') is not None:
            self.cash_coupon_id = m.get('CashCouponId')
        if m.get('CashCouponNo') is not None:
            self.cash_coupon_no = m.get('CashCouponNo')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryCashCouponsResponseBodyData(TeaModel):
    def __init__(self, cash_coupon=None):
        self.cash_coupon = cash_coupon  # type: list[QueryCashCouponsResponseBodyDataCashCoupon]

    def validate(self):
        if self.cash_coupon:
            for k in self.cash_coupon:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CashCoupon'] = []
        if self.cash_coupon is not None:
            for k in self.cash_coupon:
                result['CashCoupon'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cash_coupon = []
        if m.get('CashCoupon') is not None:
            for k in m.get('CashCoupon'):
                temp_model = QueryCashCouponsResponseBodyDataCashCoupon()
                self.cash_coupon.append(temp_model.from_map(k))
        return self


class QueryCashCouponsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCashCouponsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryCashCouponsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCashCouponsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCashCouponsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCashCouponsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostUnitRequest(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, page_num=None, page_size=None):
        self.owner_uid = owner_uid  # type: long
        self.parent_unit_id = parent_unit_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCostUnitResponseBodyDataCostUnitDtoList(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_id=None, unit_name=None):
        self.owner_uid = owner_uid  # type: long
        self.parent_unit_id = parent_unit_id  # type: long
        self.unit_id = unit_id  # type: long
        self.unit_name = unit_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class QueryCostUnitResponseBodyData(TeaModel):
    def __init__(self, cost_unit_dto_list=None, page_num=None, page_size=None, total_count=None):
        self.cost_unit_dto_list = cost_unit_dto_list  # type: list[QueryCostUnitResponseBodyDataCostUnitDtoList]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cost_unit_dto_list:
            for k in self.cost_unit_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CostUnitDtoList'] = []
        if self.cost_unit_dto_list is not None:
            for k in self.cost_unit_dto_list:
                result['CostUnitDtoList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.cost_unit_dto_list = []
        if m.get('CostUnitDtoList') is not None:
            for k in m.get('CostUnitDtoList'):
                temp_model = QueryCostUnitResponseBodyDataCostUnitDtoList()
                self.cost_unit_dto_list.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCostUnitResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCostUnitResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryCostUnitResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCostUnitResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCostUnitResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCostUnitResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCostUnitResourceRequest(TeaModel):
    def __init__(self, owner_uid=None, unit_id=None, page_num=None, page_size=None):
        self.owner_uid = owner_uid  # type: long
        self.unit_id = unit_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCostUnitResourceResponseBodyDataCostUnit(TeaModel):
    def __init__(self, owner_uid=None, parent_unit_id=None, unit_id=None, unit_name=None):
        self.owner_uid = owner_uid  # type: long
        self.parent_unit_id = parent_unit_id  # type: long
        self.unit_id = unit_id  # type: long
        self.unit_name = unit_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_uid is not None:
            result['OwnerUid'] = self.owner_uid
        if self.parent_unit_id is not None:
            result['ParentUnitId'] = self.parent_unit_id
        if self.unit_id is not None:
            result['UnitId'] = self.unit_id
        if self.unit_name is not None:
            result['UnitName'] = self.unit_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerUid') is not None:
            self.owner_uid = m.get('OwnerUid')
        if m.get('ParentUnitId') is not None:
            self.parent_unit_id = m.get('ParentUnitId')
        if m.get('UnitId') is not None:
            self.unit_id = m.get('UnitId')
        if m.get('UnitName') is not None:
            self.unit_name = m.get('UnitName')
        return self


class QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo(TeaModel):
    def __init__(self, resource_count=None, resource_group_count=None, sub_unit_count=None,
                 total_resource_count=None, total_resource_group_count=None, total_user_count=None, user_count=None):
        self.resource_count = resource_count  # type: long
        self.resource_group_count = resource_group_count  # type: long
        self.sub_unit_count = sub_unit_count  # type: long
        self.total_resource_count = total_resource_count  # type: long
        self.total_resource_group_count = total_resource_group_count  # type: long
        self.total_user_count = total_user_count  # type: long
        self.user_count = user_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count
        if self.resource_group_count is not None:
            result['ResourceGroupCount'] = self.resource_group_count
        if self.sub_unit_count is not None:
            result['SubUnitCount'] = self.sub_unit_count
        if self.total_resource_count is not None:
            result['TotalResourceCount'] = self.total_resource_count
        if self.total_resource_group_count is not None:
            result['TotalResourceGroupCount'] = self.total_resource_group_count
        if self.total_user_count is not None:
            result['TotalUserCount'] = self.total_user_count
        if self.user_count is not None:
            result['UserCount'] = self.user_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')
        if m.get('ResourceGroupCount') is not None:
            self.resource_group_count = m.get('ResourceGroupCount')
        if m.get('SubUnitCount') is not None:
            self.sub_unit_count = m.get('SubUnitCount')
        if m.get('TotalResourceCount') is not None:
            self.total_resource_count = m.get('TotalResourceCount')
        if m.get('TotalResourceGroupCount') is not None:
            self.total_resource_group_count = m.get('TotalResourceGroupCount')
        if m.get('TotalUserCount') is not None:
            self.total_user_count = m.get('TotalUserCount')
        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')
        return self


class QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList(TeaModel):
    def __init__(self, apportion_code=None, apportion_name=None, commodity_code=None, commodity_name=None,
                 related_resources=None, resource_group=None, resource_id=None, resource_nick=None, resource_status=None,
                 resource_tag=None, resource_type=None, resource_user_id=None, resource_user_name=None):
        self.apportion_code = apportion_code  # type: str
        self.apportion_name = apportion_name  # type: str
        self.commodity_code = commodity_code  # type: str
        self.commodity_name = commodity_name  # type: str
        self.related_resources = related_resources  # type: str
        self.resource_group = resource_group  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_nick = resource_nick  # type: str
        self.resource_status = resource_status  # type: str
        self.resource_tag = resource_tag  # type: str
        self.resource_type = resource_type  # type: str
        self.resource_user_id = resource_user_id  # type: long
        self.resource_user_name = resource_user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.apportion_code is not None:
            result['ApportionCode'] = self.apportion_code
        if self.apportion_name is not None:
            result['ApportionName'] = self.apportion_name
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name
        if self.related_resources is not None:
            result['RelatedResources'] = self.related_resources
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_nick is not None:
            result['ResourceNick'] = self.resource_nick
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_tag is not None:
            result['ResourceTag'] = self.resource_tag
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_user_id is not None:
            result['ResourceUserId'] = self.resource_user_id
        if self.resource_user_name is not None:
            result['ResourceUserName'] = self.resource_user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApportionCode') is not None:
            self.apportion_code = m.get('ApportionCode')
        if m.get('ApportionName') is not None:
            self.apportion_name = m.get('ApportionName')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')
        if m.get('RelatedResources') is not None:
            self.related_resources = m.get('RelatedResources')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceNick') is not None:
            self.resource_nick = m.get('ResourceNick')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceTag') is not None:
            self.resource_tag = m.get('ResourceTag')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceUserId') is not None:
            self.resource_user_id = m.get('ResourceUserId')
        if m.get('ResourceUserName') is not None:
            self.resource_user_name = m.get('ResourceUserName')
        return self


class QueryCostUnitResourceResponseBodyData(TeaModel):
    def __init__(self, cost_unit=None, cost_unit_statis_info=None, page_num=None, page_size=None,
                 resource_instance_dto_list=None, total_count=None):
        self.cost_unit = cost_unit  # type: QueryCostUnitResourceResponseBodyDataCostUnit
        self.cost_unit_statis_info = cost_unit_statis_info  # type: QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.resource_instance_dto_list = resource_instance_dto_list  # type: list[QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.cost_unit:
            self.cost_unit.validate()
        if self.cost_unit_statis_info:
            self.cost_unit_statis_info.validate()
        if self.resource_instance_dto_list:
            for k in self.resource_instance_dto_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit.to_map()
        if self.cost_unit_statis_info is not None:
            result['CostUnitStatisInfo'] = self.cost_unit_statis_info.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ResourceInstanceDtoList'] = []
        if self.resource_instance_dto_list is not None:
            for k in self.resource_instance_dto_list:
                result['ResourceInstanceDtoList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CostUnit') is not None:
            temp_model = QueryCostUnitResourceResponseBodyDataCostUnit()
            self.cost_unit = temp_model.from_map(m['CostUnit'])
        if m.get('CostUnitStatisInfo') is not None:
            temp_model = QueryCostUnitResourceResponseBodyDataCostUnitStatisInfo()
            self.cost_unit_statis_info = temp_model.from_map(m['CostUnitStatisInfo'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.resource_instance_dto_list = []
        if m.get('ResourceInstanceDtoList') is not None:
            for k in m.get('ResourceInstanceDtoList'):
                temp_model = QueryCostUnitResourceResponseBodyDataResourceInstanceDtoList()
                self.resource_instance_dto_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryCostUnitResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCostUnitResourceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryCostUnitResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCostUnitResourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCostUnitResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCostUnitResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCustomerAddressListRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress(TeaModel):
    def __init__(self, addressee=None, biz_type=None, city=None, county=None, delivery_address=None, id=None,
                 phone=None, postal_code=None, province=None, street=None, user_id=None, user_nick=None):
        self.addressee = addressee  # type: str
        self.biz_type = biz_type  # type: str
        self.city = city  # type: str
        self.county = county  # type: str
        self.delivery_address = delivery_address  # type: str
        self.id = id  # type: long
        self.phone = phone  # type: str
        self.postal_code = postal_code  # type: str
        self.province = province  # type: str
        self.street = street  # type: str
        self.user_id = user_id  # type: long
        self.user_nick = user_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.addressee is not None:
            result['Addressee'] = self.addressee
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.city is not None:
            result['City'] = self.city
        if self.county is not None:
            result['County'] = self.county
        if self.delivery_address is not None:
            result['DeliveryAddress'] = self.delivery_address
        if self.id is not None:
            result['Id'] = self.id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.postal_code is not None:
            result['PostalCode'] = self.postal_code
        if self.province is not None:
            result['Province'] = self.province
        if self.street is not None:
            result['Street'] = self.street
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Addressee') is not None:
            self.addressee = m.get('Addressee')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('City') is not None:
            self.city = m.get('City')
        if m.get('County') is not None:
            self.county = m.get('County')
        if m.get('DeliveryAddress') is not None:
            self.delivery_address = m.get('DeliveryAddress')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('PostalCode') is not None:
            self.postal_code = m.get('PostalCode')
        if m.get('Province') is not None:
            self.province = m.get('Province')
        if m.get('Street') is not None:
            self.street = m.get('Street')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList(TeaModel):
    def __init__(self, customer_invoice_address=None):
        self.customer_invoice_address = customer_invoice_address  # type: list[QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress]

    def validate(self):
        if self.customer_invoice_address:
            for k in self.customer_invoice_address:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CustomerInvoiceAddress'] = []
        if self.customer_invoice_address is not None:
            for k in self.customer_invoice_address:
                result['CustomerInvoiceAddress'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.customer_invoice_address = []
        if m.get('CustomerInvoiceAddress') is not None:
            for k in m.get('CustomerInvoiceAddress'):
                temp_model = QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressListCustomerInvoiceAddress()
                self.customer_invoice_address.append(temp_model.from_map(k))
        return self


class QueryCustomerAddressListResponseBodyData(TeaModel):
    def __init__(self, customer_invoice_address_list=None):
        self.customer_invoice_address_list = customer_invoice_address_list  # type: QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList

    def validate(self):
        if self.customer_invoice_address_list:
            self.customer_invoice_address_list.validate()

    def to_map(self):
        result = dict()
        if self.customer_invoice_address_list is not None:
            result['CustomerInvoiceAddressList'] = self.customer_invoice_address_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerInvoiceAddressList') is not None:
            temp_model = QueryCustomerAddressListResponseBodyDataCustomerInvoiceAddressList()
            self.customer_invoice_address_list = temp_model.from_map(m['CustomerInvoiceAddressList'])
        return self


class QueryCustomerAddressListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCustomerAddressListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryCustomerAddressListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCustomerAddressListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCustomerAddressListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryCustomerAddressListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEvaluateListRequest(TeaModel):
    def __init__(self, type=None, out_biz_id=None, owner_id=None, page_num=None, page_size=None, start_amount=None,
                 end_amount=None, start_biz_time=None, end_biz_time=None, sort_type=None, start_search_time=None,
                 end_search_time=None, bill_cycle=None, biz_type_list=None):
        self.type = type  # type: int
        self.out_biz_id = out_biz_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.start_amount = start_amount  # type: long
        self.end_amount = end_amount  # type: long
        self.start_biz_time = start_biz_time  # type: str
        self.end_biz_time = end_biz_time  # type: str
        self.sort_type = sort_type  # type: int
        self.start_search_time = start_search_time  # type: str
        self.end_search_time = end_search_time  # type: str
        self.bill_cycle = bill_cycle  # type: str
        self.biz_type_list = biz_type_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.start_amount is not None:
            result['StartAmount'] = self.start_amount
        if self.end_amount is not None:
            result['EndAmount'] = self.end_amount
        if self.start_biz_time is not None:
            result['StartBizTime'] = self.start_biz_time
        if self.end_biz_time is not None:
            result['EndBizTime'] = self.end_biz_time
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.start_search_time is not None:
            result['StartSearchTime'] = self.start_search_time
        if self.end_search_time is not None:
            result['EndSearchTime'] = self.end_search_time
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.biz_type_list is not None:
            result['BizTypeList'] = self.biz_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StartAmount') is not None:
            self.start_amount = m.get('StartAmount')
        if m.get('EndAmount') is not None:
            self.end_amount = m.get('EndAmount')
        if m.get('StartBizTime') is not None:
            self.start_biz_time = m.get('StartBizTime')
        if m.get('EndBizTime') is not None:
            self.end_biz_time = m.get('EndBizTime')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('StartSearchTime') is not None:
            self.start_search_time = m.get('StartSearchTime')
        if m.get('EndSearchTime') is not None:
            self.end_search_time = m.get('EndSearchTime')
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('BizTypeList') is not None:
            self.biz_type_list = m.get('BizTypeList')
        return self


class QueryEvaluateListResponseBodyDataEvaluateListEvaluate(TeaModel):
    def __init__(self, bill_cycle=None, bill_id=None, biz_time=None, biz_type=None, can_invoice_amount=None,
                 gmt_create=None, gmt_modified=None, id=None, invoiced_amount=None, item_id=None, name=None,
                 offset_accept_amount=None, offset_cost_amount=None, op_id=None, original_amount=None, out_biz_id=None,
                 present_amount=None, status=None, type=None, user_id=None, user_nick=None):
        self.bill_cycle = bill_cycle  # type: str
        self.bill_id = bill_id  # type: long
        self.biz_time = biz_time  # type: str
        self.biz_type = biz_type  # type: str
        self.can_invoice_amount = can_invoice_amount  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.invoiced_amount = invoiced_amount  # type: long
        self.item_id = item_id  # type: long
        self.name = name  # type: str
        self.offset_accept_amount = offset_accept_amount  # type: long
        self.offset_cost_amount = offset_cost_amount  # type: long
        self.op_id = op_id  # type: str
        self.original_amount = original_amount  # type: long
        self.out_biz_id = out_biz_id  # type: str
        self.present_amount = present_amount  # type: long
        self.status = status  # type: int
        self.type = type  # type: int
        self.user_id = user_id  # type: long
        self.user_nick = user_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.bill_cycle is not None:
            result['BillCycle'] = self.bill_cycle
        if self.bill_id is not None:
            result['BillId'] = self.bill_id
        if self.biz_time is not None:
            result['BizTime'] = self.biz_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.can_invoice_amount is not None:
            result['CanInvoiceAmount'] = self.can_invoice_amount
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.invoiced_amount is not None:
            result['InvoicedAmount'] = self.invoiced_amount
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.name is not None:
            result['Name'] = self.name
        if self.offset_accept_amount is not None:
            result['OffsetAcceptAmount'] = self.offset_accept_amount
        if self.offset_cost_amount is not None:
            result['OffsetCostAmount'] = self.offset_cost_amount
        if self.op_id is not None:
            result['OpId'] = self.op_id
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        if self.present_amount is not None:
            result['PresentAmount'] = self.present_amount
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillCycle') is not None:
            self.bill_cycle = m.get('BillCycle')
        if m.get('BillId') is not None:
            self.bill_id = m.get('BillId')
        if m.get('BizTime') is not None:
            self.biz_time = m.get('BizTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CanInvoiceAmount') is not None:
            self.can_invoice_amount = m.get('CanInvoiceAmount')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InvoicedAmount') is not None:
            self.invoiced_amount = m.get('InvoicedAmount')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OffsetAcceptAmount') is not None:
            self.offset_accept_amount = m.get('OffsetAcceptAmount')
        if m.get('OffsetCostAmount') is not None:
            self.offset_cost_amount = m.get('OffsetCostAmount')
        if m.get('OpId') is not None:
            self.op_id = m.get('OpId')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        if m.get('PresentAmount') is not None:
            self.present_amount = m.get('PresentAmount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class QueryEvaluateListResponseBodyDataEvaluateList(TeaModel):
    def __init__(self, evaluate=None):
        self.evaluate = evaluate  # type: list[QueryEvaluateListResponseBodyDataEvaluateListEvaluate]

    def validate(self):
        if self.evaluate:
            for k in self.evaluate:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Evaluate'] = []
        if self.evaluate is not None:
            for k in self.evaluate:
                result['Evaluate'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.evaluate = []
        if m.get('Evaluate') is not None:
            for k in m.get('Evaluate'):
                temp_model = QueryEvaluateListResponseBodyDataEvaluateListEvaluate()
                self.evaluate.append(temp_model.from_map(k))
        return self


class QueryEvaluateListResponseBodyData(TeaModel):
    def __init__(self, evaluate_list=None, host_id=None, page_num=None, page_size=None, total_count=None,
                 total_invoice_amount=None, total_un_applied_invoice_amount=None):
        self.evaluate_list = evaluate_list  # type: QueryEvaluateListResponseBodyDataEvaluateList
        self.host_id = host_id  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_invoice_amount = total_invoice_amount  # type: long
        self.total_un_applied_invoice_amount = total_un_applied_invoice_amount  # type: long

    def validate(self):
        if self.evaluate_list:
            self.evaluate_list.validate()

    def to_map(self):
        result = dict()
        if self.evaluate_list is not None:
            result['EvaluateList'] = self.evaluate_list.to_map()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_invoice_amount is not None:
            result['TotalInvoiceAmount'] = self.total_invoice_amount
        if self.total_un_applied_invoice_amount is not None:
            result['TotalUnAppliedInvoiceAmount'] = self.total_un_applied_invoice_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EvaluateList') is not None:
            temp_model = QueryEvaluateListResponseBodyDataEvaluateList()
            self.evaluate_list = temp_model.from_map(m['EvaluateList'])
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalInvoiceAmount') is not None:
            self.total_invoice_amount = m.get('TotalInvoiceAmount')
        if m.get('TotalUnAppliedInvoiceAmount') is not None:
            self.total_un_applied_invoice_amount = m.get('TotalUnAppliedInvoiceAmount')
        return self


class QueryEvaluateListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryEvaluateListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryEvaluateListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEvaluateListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryEvaluateListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryEvaluateListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFinancialAccountInfoRequest(TeaModel):
    def __init__(self, user_id=None):
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFinancialAccountInfoResponseBodyData(TeaModel):
    def __init__(self, member_nick_name=None, is_financial_account=None, member_group_name=None, user_name=None,
                 account_type=None, member_group_id=None):
        self.member_nick_name = member_nick_name  # type: str
        self.is_financial_account = is_financial_account  # type: bool
        self.member_group_name = member_group_name  # type: str
        self.user_name = user_name  # type: str
        self.account_type = account_type  # type: str
        self.member_group_id = member_group_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.member_nick_name is not None:
            result['MemberNickName'] = self.member_nick_name
        if self.is_financial_account is not None:
            result['IsFinancialAccount'] = self.is_financial_account
        if self.member_group_name is not None:
            result['MemberGroupName'] = self.member_group_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.member_group_id is not None:
            result['MemberGroupId'] = self.member_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MemberNickName') is not None:
            self.member_nick_name = m.get('MemberNickName')
        if m.get('IsFinancialAccount') is not None:
            self.is_financial_account = m.get('IsFinancialAccount')
        if m.get('MemberGroupName') is not None:
            self.member_group_name = m.get('MemberGroupName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('MemberGroupId') is not None:
            self.member_group_id = m.get('MemberGroupId')
        return self


class QueryFinancialAccountInfoResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryFinancialAccountInfoResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryFinancialAccountInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFinancialAccountInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryFinancialAccountInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryFinancialAccountInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 owner_id=None, is_billing_item=None, page_num=None, page_size=None, is_hide_zero_charge=None,
                 billing_date=None, granularity=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.owner_id = owner_id  # type: long
        self.is_billing_item = is_billing_item  # type: bool
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool
        self.billing_date = billing_date  # type: str
        self.granularity = granularity  # type: str
        self.bill_owner_id = bill_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.is_billing_item is not None:
            result['IsBillingItem'] = self.is_billing_item
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.granularity is not None:
            result['Granularity'] = self.granularity
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('IsBillingItem') is not None:
            self.is_billing_item = m.get('IsBillingItem')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QueryInstanceBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, billing_date=None, billing_item=None, billing_type=None, commodity_code=None, cost_unit=None,
                 currency=None, deducted_by_cash_coupons=None, deducted_by_coupons=None, deducted_by_prepaid_card=None,
                 deducted_by_resource_package=None, instance_config=None, instance_id=None, instance_spec=None, internet_ip=None,
                 intranet_ip=None, invoice_discount=None, item=None, list_price=None, list_price_unit=None, nick_name=None,
                 outstanding_amount=None, owner_id=None, payment_amount=None, pip_code=None, pretax_amount=None,
                 pretax_gross_amount=None, product_code=None, product_detail=None, product_name=None, product_type=None, region=None,
                 resource_group=None, service_period=None, service_period_unit=None, subscription_type=None, tag=None, usage=None,
                 usage_unit=None, zone=None):
        self.billing_date = billing_date  # type: str
        self.billing_item = billing_item  # type: str
        self.billing_type = billing_type  # type: str
        self.commodity_code = commodity_code  # type: str
        self.cost_unit = cost_unit  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.deducted_by_resource_package = deducted_by_resource_package  # type: str
        self.instance_config = instance_config  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_spec = instance_spec  # type: str
        self.internet_ip = internet_ip  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.invoice_discount = invoice_discount  # type: float
        self.item = item  # type: str
        self.list_price = list_price  # type: str
        self.list_price_unit = list_price_unit  # type: str
        self.nick_name = nick_name  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.owner_id = owner_id  # type: str
        self.payment_amount = payment_amount  # type: float
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_detail = product_detail  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.region = region  # type: str
        self.resource_group = resource_group  # type: str
        self.service_period = service_period  # type: str
        self.service_period_unit = service_period_unit  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tag = tag  # type: str
        self.usage = usage  # type: str
        self.usage_unit = usage_unit  # type: str
        self.zone = zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.item is not None:
            result['Item'] = self.item
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period
        if self.service_period_unit is not None:
            result['ServicePeriodUnit'] = self.service_period_unit
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')
        if m.get('ServicePeriodUnit') is not None:
            self.service_period_unit = m.get('ServicePeriodUnit')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class QueryInstanceBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryInstanceBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryInstanceBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryInstanceBillResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, billing_cycle=None, items=None, page_num=None,
                 page_size=None, total_count=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QueryInstanceBillResponseBodyDataItems
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryInstanceBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryInstanceBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryInstanceBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryInstanceBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInstanceBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryInstanceBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryInstanceBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceByTagRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryInstanceByTagRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[QueryInstanceByTagRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = QueryInstanceByTagRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class QueryInstanceByTagResponseBodyTagResourceTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class QueryInstanceByTagResponseBodyTagResource(TeaModel):
    def __init__(self, resource_type=None, tag=None, resource_id=None):
        self.resource_type = resource_type  # type: str
        self.tag = tag  # type: list[QueryInstanceByTagResponseBodyTagResourceTag]
        self.resource_id = resource_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = QueryInstanceByTagResponseBodyTagResourceTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class QueryInstanceByTagResponseBody(TeaModel):
    def __init__(self, message=None, next_token=None, request_id=None, tag_resource=None, code=None, success=None):
        self.message = message  # type: str
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.tag_resource = tag_resource  # type: list[QueryInstanceByTagResponseBodyTagResource]
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = QueryInstanceByTagResponseBodyTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInstanceByTagResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryInstanceByTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryInstanceByTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceGaapCostRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, billing_cycle=None, product_code=None, product_type=None,
                 subscription_type=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryInstanceGaapCostResponseBodyDataModulesModule(TeaModel):
    def __init__(self, accounting_unit=None, bill_type=None, billing_cycle=None, currency=None,
                 deducted_by_cash_coupons=None, deducted_by_coupons=None, deducted_by_prepaid_card=None,
                 gaap_deducted_by_cash_coupons=None, gaap_deducted_by_coupons=None, gaap_deducted_by_prepaid_card=None,
                 gaap_payment_amount=None, gaap_pretax_amount=None, gaap_pretax_amount_local=None, gaap_pretax_gross_amount=None,
                 gaap_pricing_discount=None, instance_id=None, month_gaap_deducted_by_cash_coupons=None,
                 month_gaap_deducted_by_coupons=None, month_gaap_deducted_by_prepaid_card=None, month_gaap_payment_amount=None,
                 month_gaap_pretax_amount=None, month_gaap_pretax_amount_local=None, month_gaap_pretax_gross_amount=None,
                 month_gaap_pricing_discount=None, order_id=None, order_type=None, owner_id=None, pay_time=None, payer_account=None,
                 payment_amount=None, payment_currency=None, pretax_amount=None, pretax_amount_local=None,
                 pretax_gross_amount=None, pricing_discount=None, product_code=None, product_type=None, region=None,
                 resource_group=None, sub_order_id=None, subscription_type=None, tag=None,
                 unallocated_deducted_by_cash_coupons=None, unallocated_deducted_by_coupons=None, unallocated_deducted_by_prepaid_card=None,
                 unallocated_payment_amount=None, unallocated_pretax_amount=None, unallocated_pretax_amount_local=None,
                 unallocated_pretax_gross_amount=None, unallocated_pricing_discount=None, usage_end_date=None, usage_start_date=None):
        self.accounting_unit = accounting_unit  # type: str
        self.bill_type = bill_type  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: str
        self.deducted_by_coupons = deducted_by_coupons  # type: str
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: str
        self.gaap_deducted_by_cash_coupons = gaap_deducted_by_cash_coupons  # type: str
        self.gaap_deducted_by_coupons = gaap_deducted_by_coupons  # type: str
        self.gaap_deducted_by_prepaid_card = gaap_deducted_by_prepaid_card  # type: str
        self.gaap_payment_amount = gaap_payment_amount  # type: str
        self.gaap_pretax_amount = gaap_pretax_amount  # type: str
        self.gaap_pretax_amount_local = gaap_pretax_amount_local  # type: str
        self.gaap_pretax_gross_amount = gaap_pretax_gross_amount  # type: str
        self.gaap_pricing_discount = gaap_pricing_discount  # type: str
        self.instance_id = instance_id  # type: str
        self.month_gaap_deducted_by_cash_coupons = month_gaap_deducted_by_cash_coupons  # type: str
        self.month_gaap_deducted_by_coupons = month_gaap_deducted_by_coupons  # type: str
        self.month_gaap_deducted_by_prepaid_card = month_gaap_deducted_by_prepaid_card  # type: str
        self.month_gaap_payment_amount = month_gaap_payment_amount  # type: str
        self.month_gaap_pretax_amount = month_gaap_pretax_amount  # type: str
        self.month_gaap_pretax_amount_local = month_gaap_pretax_amount_local  # type: str
        self.month_gaap_pretax_gross_amount = month_gaap_pretax_gross_amount  # type: str
        self.month_gaap_pricing_discount = month_gaap_pricing_discount  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: str
        self.owner_id = owner_id  # type: str
        self.pay_time = pay_time  # type: str
        self.payer_account = payer_account  # type: str
        self.payment_amount = payment_amount  # type: str
        self.payment_currency = payment_currency  # type: str
        self.pretax_amount = pretax_amount  # type: str
        self.pretax_amount_local = pretax_amount_local  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: str
        self.pricing_discount = pricing_discount  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.region = region  # type: str
        self.resource_group = resource_group  # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tag = tag  # type: str
        self.unallocated_deducted_by_cash_coupons = unallocated_deducted_by_cash_coupons  # type: str
        self.unallocated_deducted_by_coupons = unallocated_deducted_by_coupons  # type: str
        self.unallocated_deducted_by_prepaid_card = unallocated_deducted_by_prepaid_card  # type: str
        self.unallocated_payment_amount = unallocated_payment_amount  # type: str
        self.unallocated_pretax_amount = unallocated_pretax_amount  # type: str
        self.unallocated_pretax_amount_local = unallocated_pretax_amount_local  # type: str
        self.unallocated_pretax_gross_amount = unallocated_pretax_gross_amount  # type: str
        self.unallocated_pricing_discount = unallocated_pricing_discount  # type: str
        self.usage_end_date = usage_end_date  # type: str
        self.usage_start_date = usage_start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.accounting_unit is not None:
            result['AccountingUnit'] = self.accounting_unit
        if self.bill_type is not None:
            result['BillType'] = self.bill_type
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.gaap_deducted_by_cash_coupons is not None:
            result['GaapDeductedByCashCoupons'] = self.gaap_deducted_by_cash_coupons
        if self.gaap_deducted_by_coupons is not None:
            result['GaapDeductedByCoupons'] = self.gaap_deducted_by_coupons
        if self.gaap_deducted_by_prepaid_card is not None:
            result['GaapDeductedByPrepaidCard'] = self.gaap_deducted_by_prepaid_card
        if self.gaap_payment_amount is not None:
            result['GaapPaymentAmount'] = self.gaap_payment_amount
        if self.gaap_pretax_amount is not None:
            result['GaapPretaxAmount'] = self.gaap_pretax_amount
        if self.gaap_pretax_amount_local is not None:
            result['GaapPretaxAmountLocal'] = self.gaap_pretax_amount_local
        if self.gaap_pretax_gross_amount is not None:
            result['GaapPretaxGrossAmount'] = self.gaap_pretax_gross_amount
        if self.gaap_pricing_discount is not None:
            result['GaapPricingDiscount'] = self.gaap_pricing_discount
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.month_gaap_deducted_by_cash_coupons is not None:
            result['MonthGaapDeductedByCashCoupons'] = self.month_gaap_deducted_by_cash_coupons
        if self.month_gaap_deducted_by_coupons is not None:
            result['MonthGaapDeductedByCoupons'] = self.month_gaap_deducted_by_coupons
        if self.month_gaap_deducted_by_prepaid_card is not None:
            result['MonthGaapDeductedByPrepaidCard'] = self.month_gaap_deducted_by_prepaid_card
        if self.month_gaap_payment_amount is not None:
            result['MonthGaapPaymentAmount'] = self.month_gaap_payment_amount
        if self.month_gaap_pretax_amount is not None:
            result['MonthGaapPretaxAmount'] = self.month_gaap_pretax_amount
        if self.month_gaap_pretax_amount_local is not None:
            result['MonthGaapPretaxAmountLocal'] = self.month_gaap_pretax_amount_local
        if self.month_gaap_pretax_gross_amount is not None:
            result['MonthGaapPretaxGrossAmount'] = self.month_gaap_pretax_gross_amount
        if self.month_gaap_pricing_discount is not None:
            result['MonthGaapPricingDiscount'] = self.month_gaap_pricing_discount
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.pricing_discount is not None:
            result['PricingDiscount'] = self.pricing_discount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.unallocated_deducted_by_cash_coupons is not None:
            result['UnallocatedDeductedByCashCoupons'] = self.unallocated_deducted_by_cash_coupons
        if self.unallocated_deducted_by_coupons is not None:
            result['UnallocatedDeductedByCoupons'] = self.unallocated_deducted_by_coupons
        if self.unallocated_deducted_by_prepaid_card is not None:
            result['UnallocatedDeductedByPrepaidCard'] = self.unallocated_deducted_by_prepaid_card
        if self.unallocated_payment_amount is not None:
            result['UnallocatedPaymentAmount'] = self.unallocated_payment_amount
        if self.unallocated_pretax_amount is not None:
            result['UnallocatedPretaxAmount'] = self.unallocated_pretax_amount
        if self.unallocated_pretax_amount_local is not None:
            result['UnallocatedPretaxAmountLocal'] = self.unallocated_pretax_amount_local
        if self.unallocated_pretax_gross_amount is not None:
            result['UnallocatedPretaxGrossAmount'] = self.unallocated_pretax_gross_amount
        if self.unallocated_pricing_discount is not None:
            result['UnallocatedPricingDiscount'] = self.unallocated_pricing_discount
        if self.usage_end_date is not None:
            result['UsageEndDate'] = self.usage_end_date
        if self.usage_start_date is not None:
            result['UsageStartDate'] = self.usage_start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountingUnit') is not None:
            self.accounting_unit = m.get('AccountingUnit')
        if m.get('BillType') is not None:
            self.bill_type = m.get('BillType')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('GaapDeductedByCashCoupons') is not None:
            self.gaap_deducted_by_cash_coupons = m.get('GaapDeductedByCashCoupons')
        if m.get('GaapDeductedByCoupons') is not None:
            self.gaap_deducted_by_coupons = m.get('GaapDeductedByCoupons')
        if m.get('GaapDeductedByPrepaidCard') is not None:
            self.gaap_deducted_by_prepaid_card = m.get('GaapDeductedByPrepaidCard')
        if m.get('GaapPaymentAmount') is not None:
            self.gaap_payment_amount = m.get('GaapPaymentAmount')
        if m.get('GaapPretaxAmount') is not None:
            self.gaap_pretax_amount = m.get('GaapPretaxAmount')
        if m.get('GaapPretaxAmountLocal') is not None:
            self.gaap_pretax_amount_local = m.get('GaapPretaxAmountLocal')
        if m.get('GaapPretaxGrossAmount') is not None:
            self.gaap_pretax_gross_amount = m.get('GaapPretaxGrossAmount')
        if m.get('GaapPricingDiscount') is not None:
            self.gaap_pricing_discount = m.get('GaapPricingDiscount')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('MonthGaapDeductedByCashCoupons') is not None:
            self.month_gaap_deducted_by_cash_coupons = m.get('MonthGaapDeductedByCashCoupons')
        if m.get('MonthGaapDeductedByCoupons') is not None:
            self.month_gaap_deducted_by_coupons = m.get('MonthGaapDeductedByCoupons')
        if m.get('MonthGaapDeductedByPrepaidCard') is not None:
            self.month_gaap_deducted_by_prepaid_card = m.get('MonthGaapDeductedByPrepaidCard')
        if m.get('MonthGaapPaymentAmount') is not None:
            self.month_gaap_payment_amount = m.get('MonthGaapPaymentAmount')
        if m.get('MonthGaapPretaxAmount') is not None:
            self.month_gaap_pretax_amount = m.get('MonthGaapPretaxAmount')
        if m.get('MonthGaapPretaxAmountLocal') is not None:
            self.month_gaap_pretax_amount_local = m.get('MonthGaapPretaxAmountLocal')
        if m.get('MonthGaapPretaxGrossAmount') is not None:
            self.month_gaap_pretax_gross_amount = m.get('MonthGaapPretaxGrossAmount')
        if m.get('MonthGaapPricingDiscount') is not None:
            self.month_gaap_pricing_discount = m.get('MonthGaapPricingDiscount')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('PricingDiscount') is not None:
            self.pricing_discount = m.get('PricingDiscount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('UnallocatedDeductedByCashCoupons') is not None:
            self.unallocated_deducted_by_cash_coupons = m.get('UnallocatedDeductedByCashCoupons')
        if m.get('UnallocatedDeductedByCoupons') is not None:
            self.unallocated_deducted_by_coupons = m.get('UnallocatedDeductedByCoupons')
        if m.get('UnallocatedDeductedByPrepaidCard') is not None:
            self.unallocated_deducted_by_prepaid_card = m.get('UnallocatedDeductedByPrepaidCard')
        if m.get('UnallocatedPaymentAmount') is not None:
            self.unallocated_payment_amount = m.get('UnallocatedPaymentAmount')
        if m.get('UnallocatedPretaxAmount') is not None:
            self.unallocated_pretax_amount = m.get('UnallocatedPretaxAmount')
        if m.get('UnallocatedPretaxAmountLocal') is not None:
            self.unallocated_pretax_amount_local = m.get('UnallocatedPretaxAmountLocal')
        if m.get('UnallocatedPretaxGrossAmount') is not None:
            self.unallocated_pretax_gross_amount = m.get('UnallocatedPretaxGrossAmount')
        if m.get('UnallocatedPricingDiscount') is not None:
            self.unallocated_pricing_discount = m.get('UnallocatedPricingDiscount')
        if m.get('UsageEndDate') is not None:
            self.usage_end_date = m.get('UsageEndDate')
        if m.get('UsageStartDate') is not None:
            self.usage_start_date = m.get('UsageStartDate')
        return self


class QueryInstanceGaapCostResponseBodyDataModules(TeaModel):
    def __init__(self, module=None):
        self.module = module  # type: list[QueryInstanceGaapCostResponseBodyDataModulesModule]

    def validate(self):
        if self.module:
            for k in self.module:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Module'] = []
        if self.module is not None:
            for k in self.module:
                result['Module'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.module = []
        if m.get('Module') is not None:
            for k in m.get('Module'):
                temp_model = QueryInstanceGaapCostResponseBodyDataModulesModule()
                self.module.append(temp_model.from_map(k))
        return self


class QueryInstanceGaapCostResponseBodyData(TeaModel):
    def __init__(self, host_id=None, modules=None, page_num=None, page_size=None, total_count=None):
        self.host_id = host_id  # type: str
        self.modules = modules  # type: QueryInstanceGaapCostResponseBodyDataModules
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.modules:
            self.modules.validate()

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.modules is not None:
            result['Modules'] = self.modules.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Modules') is not None:
            temp_model = QueryInstanceGaapCostResponseBodyDataModules()
            self.modules = temp_model.from_map(m['Modules'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryInstanceGaapCostResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryInstanceGaapCostResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryInstanceGaapCostResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInstanceGaapCostResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryInstanceGaapCostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryInstanceGaapCostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInvoicingCustomerListRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice(TeaModel):
    def __init__(self, adjust_type=None, bank=None, bank_no=None, customer_type=None, default_remark=None,
                 end_cycle=None, gmt_create=None, id=None, invoice_title=None, issue_type=None,
                 operating_license_address=None, operating_license_phone=None, register_no=None, start_cycle=None, status=None,
                 taxation_license=None, taxpayer_type=None, title_change_instructions=None, type=None, user_id=None, user_nick=None):
        self.adjust_type = adjust_type  # type: long
        self.bank = bank  # type: str
        self.bank_no = bank_no  # type: str
        self.customer_type = customer_type  # type: long
        self.default_remark = default_remark  # type: str
        self.end_cycle = end_cycle  # type: long
        self.gmt_create = gmt_create  # type: str
        self.id = id  # type: long
        self.invoice_title = invoice_title  # type: str
        self.issue_type = issue_type  # type: long
        self.operating_license_address = operating_license_address  # type: str
        self.operating_license_phone = operating_license_phone  # type: str
        self.register_no = register_no  # type: str
        self.start_cycle = start_cycle  # type: long
        self.status = status  # type: long
        self.taxation_license = taxation_license  # type: str
        self.taxpayer_type = taxpayer_type  # type: long
        self.title_change_instructions = title_change_instructions  # type: str
        self.type = type  # type: long
        self.user_id = user_id  # type: long
        self.user_nick = user_nick  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.adjust_type is not None:
            result['AdjustType'] = self.adjust_type
        if self.bank is not None:
            result['Bank'] = self.bank
        if self.bank_no is not None:
            result['BankNo'] = self.bank_no
        if self.customer_type is not None:
            result['CustomerType'] = self.customer_type
        if self.default_remark is not None:
            result['DefaultRemark'] = self.default_remark
        if self.end_cycle is not None:
            result['EndCycle'] = self.end_cycle
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.invoice_title is not None:
            result['InvoiceTitle'] = self.invoice_title
        if self.issue_type is not None:
            result['IssueType'] = self.issue_type
        if self.operating_license_address is not None:
            result['OperatingLicenseAddress'] = self.operating_license_address
        if self.operating_license_phone is not None:
            result['OperatingLicensePhone'] = self.operating_license_phone
        if self.register_no is not None:
            result['RegisterNo'] = self.register_no
        if self.start_cycle is not None:
            result['StartCycle'] = self.start_cycle
        if self.status is not None:
            result['Status'] = self.status
        if self.taxation_license is not None:
            result['TaxationLicense'] = self.taxation_license
        if self.taxpayer_type is not None:
            result['TaxpayerType'] = self.taxpayer_type
        if self.title_change_instructions is not None:
            result['TitleChangeInstructions'] = self.title_change_instructions
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdjustType') is not None:
            self.adjust_type = m.get('AdjustType')
        if m.get('Bank') is not None:
            self.bank = m.get('Bank')
        if m.get('BankNo') is not None:
            self.bank_no = m.get('BankNo')
        if m.get('CustomerType') is not None:
            self.customer_type = m.get('CustomerType')
        if m.get('DefaultRemark') is not None:
            self.default_remark = m.get('DefaultRemark')
        if m.get('EndCycle') is not None:
            self.end_cycle = m.get('EndCycle')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InvoiceTitle') is not None:
            self.invoice_title = m.get('InvoiceTitle')
        if m.get('IssueType') is not None:
            self.issue_type = m.get('IssueType')
        if m.get('OperatingLicenseAddress') is not None:
            self.operating_license_address = m.get('OperatingLicenseAddress')
        if m.get('OperatingLicensePhone') is not None:
            self.operating_license_phone = m.get('OperatingLicensePhone')
        if m.get('RegisterNo') is not None:
            self.register_no = m.get('RegisterNo')
        if m.get('StartCycle') is not None:
            self.start_cycle = m.get('StartCycle')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaxationLicense') is not None:
            self.taxation_license = m.get('TaxationLicense')
        if m.get('TaxpayerType') is not None:
            self.taxpayer_type = m.get('TaxpayerType')
        if m.get('TitleChangeInstructions') is not None:
            self.title_change_instructions = m.get('TitleChangeInstructions')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        return self


class QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList(TeaModel):
    def __init__(self, customer_invoice=None):
        self.customer_invoice = customer_invoice  # type: list[QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice]

    def validate(self):
        if self.customer_invoice:
            for k in self.customer_invoice:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['CustomerInvoice'] = []
        if self.customer_invoice is not None:
            for k in self.customer_invoice:
                result['CustomerInvoice'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.customer_invoice = []
        if m.get('CustomerInvoice') is not None:
            for k in m.get('CustomerInvoice'):
                temp_model = QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceListCustomerInvoice()
                self.customer_invoice.append(temp_model.from_map(k))
        return self


class QueryInvoicingCustomerListResponseBodyData(TeaModel):
    def __init__(self, customer_invoice_list=None):
        self.customer_invoice_list = customer_invoice_list  # type: QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList

    def validate(self):
        if self.customer_invoice_list:
            self.customer_invoice_list.validate()

    def to_map(self):
        result = dict()
        if self.customer_invoice_list is not None:
            result['CustomerInvoiceList'] = self.customer_invoice_list.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerInvoiceList') is not None:
            temp_model = QueryInvoicingCustomerListResponseBodyDataCustomerInvoiceList()
            self.customer_invoice_list = temp_model.from_map(m['CustomerInvoiceList'])
        return self


class QueryInvoicingCustomerListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryInvoicingCustomerListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryInvoicingCustomerListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryInvoicingCustomerListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryInvoicingCustomerListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryInvoicingCustomerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyBillRequest(TeaModel):
    def __init__(self, billing_cycle=None):
        self.billing_cycle = billing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        return self


class QueryMonthlyBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, after_tax_amount=None, currency=None, deducted_by_cash_coupons=None,
                 deducted_by_coupons=None, deducted_by_prepaid_card=None, invoice_discount=None, item=None, outstanding_amount=None,
                 payment_amount=None, payment_currency=None, pretax_amount=None, pretax_amount_local=None,
                 pretax_gross_amount=None, product_code=None, product_type=None, solution_code=None, solution_name=None,
                 subscription_type=None, tax=None):
        self.after_tax_amount = after_tax_amount  # type: float
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.item = item  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.solution_code = solution_code  # type: str
        self.solution_name = solution_name  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.item is not None:
            result['Item'] = self.item
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.solution_code is not None:
            result['SolutionCode'] = self.solution_code
        if self.solution_name is not None:
            result['SolutionName'] = self.solution_name
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SolutionCode') is not None:
            self.solution_code = m.get('SolutionCode')
        if m.get('SolutionName') is not None:
            self.solution_name = m.get('SolutionName')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        return self


class QueryMonthlyBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryMonthlyBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryMonthlyBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryMonthlyBillResponseBodyData(TeaModel):
    def __init__(self, billing_cycle=None, items=None, new_invoice_amount=None, outstanding_amount=None,
                 total_outstanding_amount=None):
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QueryMonthlyBillResponseBodyDataItems
        self.new_invoice_amount = new_invoice_amount  # type: float
        self.outstanding_amount = outstanding_amount  # type: float
        self.total_outstanding_amount = total_outstanding_amount  # type: float

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.new_invoice_amount is not None:
            result['NewInvoiceAmount'] = self.new_invoice_amount
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.total_outstanding_amount is not None:
            result['TotalOutstandingAmount'] = self.total_outstanding_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryMonthlyBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('NewInvoiceAmount') is not None:
            self.new_invoice_amount = m.get('NewInvoiceAmount')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('TotalOutstandingAmount') is not None:
            self.total_outstanding_amount = m.get('TotalOutstandingAmount')
        return self


class QueryMonthlyBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryMonthlyBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryMonthlyBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonthlyBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMonthlyBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonthlyBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthlyInstanceConsumptionRequest(TeaModel):
    def __init__(self, product_code=None, owner_id=None, page_num=None, page_size=None, billing_cycle=None,
                 product_type=None, subscription_type=None):
        self.product_code = product_code  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryMonthlyInstanceConsumptionResponseBodyDataItemsItem(TeaModel):
    def __init__(self, after_tax_amount=None, currency=None, discount_amount=None, instance_id=None, owner_id=None,
                 payer_account=None, payment_currency=None, pretax_amount=None, pretax_amount_local=None,
                 pretax_gross_amount=None, product_code=None, product_type=None, region=None, resource_group=None,
                 subscription_type=None, tag=None, tax=None):
        self.after_tax_amount = after_tax_amount  # type: float
        self.currency = currency  # type: str
        self.discount_amount = discount_amount  # type: float
        self.instance_id = instance_id  # type: str
        self.owner_id = owner_id  # type: str
        self.payer_account = payer_account  # type: str
        self.payment_currency = payment_currency  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.region = region  # type: str
        self.resource_group = resource_group  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tag = tag  # type: str
        self.tax = tax  # type: float

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.tax is not None:
            result['Tax'] = self.tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        return self


class QueryMonthlyInstanceConsumptionResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QueryMonthlyInstanceConsumptionResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QueryMonthlyInstanceConsumptionResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QueryMonthlyInstanceConsumptionResponseBodyData(TeaModel):
    def __init__(self, billing_cycle=None, items=None, page_num=None, page_size=None, total_count=None):
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QueryMonthlyInstanceConsumptionResponseBodyDataItems
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QueryMonthlyInstanceConsumptionResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryMonthlyInstanceConsumptionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryMonthlyInstanceConsumptionResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryMonthlyInstanceConsumptionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonthlyInstanceConsumptionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMonthlyInstanceConsumptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryMonthlyInstanceConsumptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrdersRequest(TeaModel):
    def __init__(self, create_time_end=None, page_num=None, page_size=None, product_code=None, product_type=None,
                 subscription_type=None, order_type=None, payment_status=None, create_time_start=None, owner_id=None):
        self.create_time_end = create_time_end  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.order_type = order_type  # type: str
        self.payment_status = payment_status  # type: str
        self.create_time_start = create_time_start  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class QueryOrdersResponseBodyDataOrderListOrder(TeaModel):
    def __init__(self, after_tax_amount=None, create_time=None, currency=None, order_id=None, order_type=None,
                 payment_currency=None, payment_status=None, payment_time=None, pretax_amount=None, pretax_amount_local=None,
                 pretax_gross_amount=None, product_code=None, product_type=None, related_order_id=None, subscription_type=None,
                 tax=None):
        self.after_tax_amount = after_tax_amount  # type: str
        self.create_time = create_time  # type: str
        self.currency = currency  # type: str
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: str
        self.payment_currency = payment_currency  # type: str
        self.payment_status = payment_status  # type: str
        self.payment_time = payment_time  # type: str
        self.pretax_amount = pretax_amount  # type: str
        self.pretax_amount_local = pretax_amount_local  # type: str
        self.pretax_gross_amount = pretax_gross_amount  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.related_order_id = related_order_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_status is not None:
            result['PaymentStatus'] = self.payment_status
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.related_order_id is not None:
            result['RelatedOrderId'] = self.related_order_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentStatus') is not None:
            self.payment_status = m.get('PaymentStatus')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RelatedOrderId') is not None:
            self.related_order_id = m.get('RelatedOrderId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        return self


class QueryOrdersResponseBodyDataOrderList(TeaModel):
    def __init__(self, order=None):
        self.order = order  # type: list[QueryOrdersResponseBodyDataOrderListOrder]

    def validate(self):
        if self.order:
            for k in self.order:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Order'] = []
        if self.order is not None:
            for k in self.order:
                result['Order'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.order = []
        if m.get('Order') is not None:
            for k in m.get('Order'):
                temp_model = QueryOrdersResponseBodyDataOrderListOrder()
                self.order.append(temp_model.from_map(k))
        return self


class QueryOrdersResponseBodyData(TeaModel):
    def __init__(self, host_name=None, order_list=None, page_num=None, page_size=None, total_count=None):
        self.host_name = host_name  # type: str
        self.order_list = order_list  # type: QueryOrdersResponseBodyDataOrderList
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.order_list:
            self.order_list.validate()

    def to_map(self):
        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.order_list is not None:
            result['OrderList'] = self.order_list.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('OrderList') is not None:
            temp_model = QueryOrdersResponseBodyDataOrderList()
            self.order_list = temp_model.from_map(m['OrderList'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryOrdersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryOrdersResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryOrdersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPermissionListRequest(TeaModel):
    def __init__(self, relation_id=None):
        self.relation_id = relation_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class QueryPermissionListResponseBodyDataPermissionList(TeaModel):
    def __init__(self, end_time=None, start_time=None, permission_code=None, permission_name=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.permission_code = permission_code  # type: str
        self.permission_name = permission_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.permission_code is not None:
            result['PermissionCode'] = self.permission_code
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('PermissionCode') is not None:
            self.permission_code = m.get('PermissionCode')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        return self


class QueryPermissionListResponseBodyData(TeaModel):
    def __init__(self, end_time=None, relation_type=None, start_time=None, permission_list=None, state=None,
                 master_id=None, member_id=None, setup_time=None):
        self.end_time = end_time  # type: str
        self.relation_type = relation_type  # type: str
        self.start_time = start_time  # type: str
        self.permission_list = permission_list  # type: list[QueryPermissionListResponseBodyDataPermissionList]
        self.state = state  # type: str
        self.master_id = master_id  # type: long
        self.member_id = member_id  # type: long
        self.setup_time = setup_time  # type: str

    def validate(self):
        if self.permission_list:
            for k in self.permission_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        result['PermissionList'] = []
        if self.permission_list is not None:
            for k in self.permission_list:
                result['PermissionList'].append(k.to_map() if k else None)
        if self.state is not None:
            result['State'] = self.state
        if self.master_id is not None:
            result['MasterId'] = self.master_id
        if self.member_id is not None:
            result['MemberId'] = self.member_id
        if self.setup_time is not None:
            result['SetupTime'] = self.setup_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        self.permission_list = []
        if m.get('PermissionList') is not None:
            for k in m.get('PermissionList'):
                temp_model = QueryPermissionListResponseBodyDataPermissionList()
                self.permission_list.append(temp_model.from_map(k))
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('MasterId') is not None:
            self.master_id = m.get('MasterId')
        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')
        if m.get('SetupTime') is not None:
            self.setup_time = m.get('SetupTime')
        return self


class QueryPermissionListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryPermissionListResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryPermissionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPermissionListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryPermissionListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPermissionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPrepaidCardsRequest(TeaModel):
    def __init__(self, expiry_time_end=None, expiry_time_start=None, effective_or_not=None):
        self.expiry_time_end = expiry_time_end  # type: str
        self.expiry_time_start = expiry_time_start  # type: str
        self.effective_or_not = effective_or_not  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')
        return self


class QueryPrepaidCardsResponseBodyDataPrepaidCard(TeaModel):
    def __init__(self, applicable_products=None, applicable_scenarios=None, balance=None, effective_time=None,
                 expiry_time=None, granted_time=None, nominal_value=None, prepaid_card_id=None, prepaid_card_no=None,
                 status=None):
        self.applicable_products = applicable_products  # type: str
        self.applicable_scenarios = applicable_scenarios  # type: str
        self.balance = balance  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.granted_time = granted_time  # type: str
        self.nominal_value = nominal_value  # type: str
        self.prepaid_card_id = prepaid_card_id  # type: long
        self.prepaid_card_no = prepaid_card_no  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products
        if self.applicable_scenarios is not None:
            result['ApplicableScenarios'] = self.applicable_scenarios
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value
        if self.prepaid_card_id is not None:
            result['PrepaidCardId'] = self.prepaid_card_id
        if self.prepaid_card_no is not None:
            result['PrepaidCardNo'] = self.prepaid_card_no
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')
        if m.get('ApplicableScenarios') is not None:
            self.applicable_scenarios = m.get('ApplicableScenarios')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')
        if m.get('PrepaidCardId') is not None:
            self.prepaid_card_id = m.get('PrepaidCardId')
        if m.get('PrepaidCardNo') is not None:
            self.prepaid_card_no = m.get('PrepaidCardNo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryPrepaidCardsResponseBodyData(TeaModel):
    def __init__(self, prepaid_card=None):
        self.prepaid_card = prepaid_card  # type: list[QueryPrepaidCardsResponseBodyDataPrepaidCard]

    def validate(self):
        if self.prepaid_card:
            for k in self.prepaid_card:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['PrepaidCard'] = []
        if self.prepaid_card is not None:
            for k in self.prepaid_card:
                result['PrepaidCard'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.prepaid_card = []
        if m.get('PrepaidCard') is not None:
            for k in m.get('PrepaidCard'):
                temp_model = QueryPrepaidCardsResponseBodyDataPrepaidCard()
                self.prepaid_card.append(temp_model.from_map(k))
        return self


class QueryPrepaidCardsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPrepaidCardsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryPrepaidCardsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPrepaidCardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryPrepaidCardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryPrepaidCardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryProductListRequest(TeaModel):
    def __init__(self, query_total_count=None, page_num=None, page_size=None):
        self.query_total_count = query_total_count  # type: bool
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.query_total_count is not None:
            result['QueryTotalCount'] = self.query_total_count
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueryTotalCount') is not None:
            self.query_total_count = m.get('QueryTotalCount')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryProductListResponseBodyDataProductListProduct(TeaModel):
    def __init__(self, product_code=None, product_name=None, product_type=None, subscription_type=None):
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        return self


class QueryProductListResponseBodyDataProductList(TeaModel):
    def __init__(self, product=None):
        self.product = product  # type: list[QueryProductListResponseBodyDataProductListProduct]

    def validate(self):
        if self.product:
            for k in self.product:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Product'] = []
        if self.product is not None:
            for k in self.product:
                result['Product'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.product = []
        if m.get('Product') is not None:
            for k in m.get('Product'):
                temp_model = QueryProductListResponseBodyDataProductListProduct()
                self.product.append(temp_model.from_map(k))
        return self


class QueryProductListResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, product_list=None, total_count=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.product_list = product_list  # type: QueryProductListResponseBodyDataProductList
        self.total_count = total_count  # type: int

    def validate(self):
        if self.product_list:
            self.product_list.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_list is not None:
            result['ProductList'] = self.product_list.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductList') is not None:
            temp_model = QueryProductListResponseBodyDataProductList()
            self.product_list = temp_model.from_map(m['ProductList'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryProductListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryProductListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryProductListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryProductListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryProductListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryProductListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRedeemRequest(TeaModel):
    def __init__(self, expiry_time_start=None, expiry_time_end=None, effective_or_not=None, page_num=None,
                 page_size=None):
        self.expiry_time_start = expiry_time_start  # type: str
        self.expiry_time_end = expiry_time_end  # type: str
        self.effective_or_not = effective_or_not  # type: bool
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.expiry_time_start is not None:
            result['ExpiryTimeStart'] = self.expiry_time_start
        if self.expiry_time_end is not None:
            result['ExpiryTimeEnd'] = self.expiry_time_end
        if self.effective_or_not is not None:
            result['EffectiveOrNot'] = self.effective_or_not
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiryTimeStart') is not None:
            self.expiry_time_start = m.get('ExpiryTimeStart')
        if m.get('ExpiryTimeEnd') is not None:
            self.expiry_time_end = m.get('ExpiryTimeEnd')
        if m.get('EffectiveOrNot') is not None:
            self.effective_or_not = m.get('EffectiveOrNot')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRedeemResponseBodyDataRedeemRedeem(TeaModel):
    def __init__(self, applicable_products=None, balance=None, effective_time=None, expiry_time=None,
                 granted_time=None, nominal_value=None, redeem_id=None, redeem_no=None, specification=None, status=None):
        self.applicable_products = applicable_products  # type: str
        self.balance = balance  # type: str
        self.effective_time = effective_time  # type: str
        self.expiry_time = expiry_time  # type: str
        self.granted_time = granted_time  # type: str
        self.nominal_value = nominal_value  # type: str
        self.redeem_id = redeem_id  # type: str
        self.redeem_no = redeem_no  # type: str
        self.specification = specification  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.applicable_products is not None:
            result['ApplicableProducts'] = self.applicable_products
        if self.balance is not None:
            result['Balance'] = self.balance
        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time
        if self.granted_time is not None:
            result['GrantedTime'] = self.granted_time
        if self.nominal_value is not None:
            result['NominalValue'] = self.nominal_value
        if self.redeem_id is not None:
            result['RedeemId'] = self.redeem_id
        if self.redeem_no is not None:
            result['RedeemNo'] = self.redeem_no
        if self.specification is not None:
            result['Specification'] = self.specification
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplicableProducts') is not None:
            self.applicable_products = m.get('ApplicableProducts')
        if m.get('Balance') is not None:
            self.balance = m.get('Balance')
        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')
        if m.get('GrantedTime') is not None:
            self.granted_time = m.get('GrantedTime')
        if m.get('NominalValue') is not None:
            self.nominal_value = m.get('NominalValue')
        if m.get('RedeemId') is not None:
            self.redeem_id = m.get('RedeemId')
        if m.get('RedeemNo') is not None:
            self.redeem_no = m.get('RedeemNo')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryRedeemResponseBodyDataRedeem(TeaModel):
    def __init__(self, redeem=None):
        self.redeem = redeem  # type: list[QueryRedeemResponseBodyDataRedeemRedeem]

    def validate(self):
        if self.redeem:
            for k in self.redeem:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Redeem'] = []
        if self.redeem is not None:
            for k in self.redeem:
                result['Redeem'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.redeem = []
        if m.get('Redeem') is not None:
            for k in m.get('Redeem'):
                temp_model = QueryRedeemResponseBodyDataRedeemRedeem()
                self.redeem.append(temp_model.from_map(k))
        return self


class QueryRedeemResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, redeem=None, total_count=None):
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.redeem = redeem  # type: QueryRedeemResponseBodyDataRedeem
        self.total_count = total_count  # type: long

    def validate(self):
        if self.redeem:
            self.redeem.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.redeem is not None:
            result['Redeem'] = self.redeem.to_map()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Redeem') is not None:
            temp_model = QueryRedeemResponseBodyDataRedeem()
            self.redeem = temp_model.from_map(m['Redeem'])
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryRedeemResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRedeemResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryRedeemResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRedeemResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRedeemResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRedeemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRelationListRequest(TeaModel):
    def __init__(self, user_id=None, page_num=None, page_size=None, status_list=None):
        self.user_id = user_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.status_list = status_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class QueryRelationListResponseBodyDataFinancialRelationInfoList(TeaModel):
    def __init__(self, end_time=None, relation_type=None, account_nick_name=None, start_time=None, state=None,
                 account_id=None, setup_time=None, account_type=None, account_name=None, relation_id=None):
        self.end_time = end_time  # type: str
        self.relation_type = relation_type  # type: str
        self.account_nick_name = account_nick_name  # type: str
        self.start_time = start_time  # type: str
        self.state = state  # type: str
        self.account_id = account_id  # type: long
        self.setup_time = setup_time  # type: str
        self.account_type = account_type  # type: str
        self.account_name = account_name  # type: str
        self.relation_id = relation_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type
        if self.account_nick_name is not None:
            result['AccountNickName'] = self.account_nick_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.setup_time is not None:
            result['SetupTime'] = self.setup_time
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.relation_id is not None:
            result['RelationId'] = self.relation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')
        if m.get('AccountNickName') is not None:
            self.account_nick_name = m.get('AccountNickName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('SetupTime') is not None:
            self.setup_time = m.get('SetupTime')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('RelationId') is not None:
            self.relation_id = m.get('RelationId')
        return self


class QueryRelationListResponseBodyData(TeaModel):
    def __init__(self, page_num=None, page_size=None, total_count=None, financial_relation_info_list=None):
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.financial_relation_info_list = financial_relation_info_list  # type: list[QueryRelationListResponseBodyDataFinancialRelationInfoList]

    def validate(self):
        if self.financial_relation_info_list:
            for k in self.financial_relation_info_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['FinancialRelationInfoList'] = []
        if self.financial_relation_info_list is not None:
            for k in self.financial_relation_info_list:
                result['FinancialRelationInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.financial_relation_info_list = []
        if m.get('FinancialRelationInfoList') is not None:
            for k in m.get('FinancialRelationInfoList'):
                temp_model = QueryRelationListResponseBodyDataFinancialRelationInfoList()
                self.financial_relation_info_list.append(temp_model.from_map(k))
        return self


class QueryRelationListResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryRelationListResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryRelationListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRelationListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRelationListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRelationListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResellerAvailableQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, item_codes=None):
        self.owner_id = owner_id  # type: long
        self.item_codes = item_codes  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.item_codes is not None:
            result['ItemCodes'] = self.item_codes
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ItemCodes') is not None:
            self.item_codes = m.get('ItemCodes')
        return self


class QueryResellerAvailableQuotaResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class QueryResellerAvailableQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryResellerAvailableQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryResellerAvailableQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRIUtilizationDetailRequest(TeaModel):
    def __init__(self, riinstance_id=None, instance_spec=None, ricommodity_code=None, deducted_instance_id=None,
                 start_time=None, end_time=None, page_num=None, page_size=None):
        self.riinstance_id = riinstance_id  # type: str
        self.instance_spec = instance_spec  # type: str
        self.ricommodity_code = ricommodity_code  # type: str
        self.deducted_instance_id = deducted_instance_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.riinstance_id is not None:
            result['RIInstanceId'] = self.riinstance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.ricommodity_code is not None:
            result['RICommodityCode'] = self.ricommodity_code
        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RIInstanceId') is not None:
            self.riinstance_id = m.get('RIInstanceId')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('RICommodityCode') is not None:
            self.ricommodity_code = m.get('RICommodityCode')
        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRIUtilizationDetailResponseBodyDataDetailListDetailList(TeaModel):
    def __init__(self, deduct_date=None, deduct_factor_total=None, deduct_hours=None, deduct_quantity=None,
                 deducted_commodity_code=None, deducted_instance_id=None, deducted_product_detail=None, instance_spec=None,
                 riinstance_id=None):
        self.deduct_date = deduct_date  # type: str
        self.deduct_factor_total = deduct_factor_total  # type: float
        self.deduct_hours = deduct_hours  # type: str
        self.deduct_quantity = deduct_quantity  # type: float
        self.deducted_commodity_code = deducted_commodity_code  # type: str
        self.deducted_instance_id = deducted_instance_id  # type: str
        self.deducted_product_detail = deducted_product_detail  # type: str
        self.instance_spec = instance_spec  # type: str
        self.riinstance_id = riinstance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.deduct_date is not None:
            result['DeductDate'] = self.deduct_date
        if self.deduct_factor_total is not None:
            result['DeductFactorTotal'] = self.deduct_factor_total
        if self.deduct_hours is not None:
            result['DeductHours'] = self.deduct_hours
        if self.deduct_quantity is not None:
            result['DeductQuantity'] = self.deduct_quantity
        if self.deducted_commodity_code is not None:
            result['DeductedCommodityCode'] = self.deducted_commodity_code
        if self.deducted_instance_id is not None:
            result['DeductedInstanceId'] = self.deducted_instance_id
        if self.deducted_product_detail is not None:
            result['DeductedProductDetail'] = self.deducted_product_detail
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.riinstance_id is not None:
            result['RIInstanceId'] = self.riinstance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeductDate') is not None:
            self.deduct_date = m.get('DeductDate')
        if m.get('DeductFactorTotal') is not None:
            self.deduct_factor_total = m.get('DeductFactorTotal')
        if m.get('DeductHours') is not None:
            self.deduct_hours = m.get('DeductHours')
        if m.get('DeductQuantity') is not None:
            self.deduct_quantity = m.get('DeductQuantity')
        if m.get('DeductedCommodityCode') is not None:
            self.deducted_commodity_code = m.get('DeductedCommodityCode')
        if m.get('DeductedInstanceId') is not None:
            self.deducted_instance_id = m.get('DeductedInstanceId')
        if m.get('DeductedProductDetail') is not None:
            self.deducted_product_detail = m.get('DeductedProductDetail')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('RIInstanceId') is not None:
            self.riinstance_id = m.get('RIInstanceId')
        return self


class QueryRIUtilizationDetailResponseBodyDataDetailList(TeaModel):
    def __init__(self, detail_list=None):
        self.detail_list = detail_list  # type: list[QueryRIUtilizationDetailResponseBodyDataDetailListDetailList]

    def validate(self):
        if self.detail_list:
            for k in self.detail_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['DetailList'] = []
        if self.detail_list is not None:
            for k in self.detail_list:
                result['DetailList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.detail_list = []
        if m.get('DetailList') is not None:
            for k in m.get('DetailList'):
                temp_model = QueryRIUtilizationDetailResponseBodyDataDetailListDetailList()
                self.detail_list.append(temp_model.from_map(k))
        return self


class QueryRIUtilizationDetailResponseBodyData(TeaModel):
    def __init__(self, detail_list=None, page_num=None, page_size=None, total_count=None):
        self.detail_list = detail_list  # type: QueryRIUtilizationDetailResponseBodyDataDetailList
        self.page_num = page_num  # type: long
        self.page_size = page_size  # type: long
        self.total_count = total_count  # type: long

    def validate(self):
        if self.detail_list:
            self.detail_list.validate()

    def to_map(self):
        result = dict()
        if self.detail_list is not None:
            result['DetailList'] = self.detail_list.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DetailList') is not None:
            temp_model = QueryRIUtilizationDetailResponseBodyDataDetailList()
            self.detail_list = temp_model.from_map(m['DetailList'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryRIUtilizationDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRIUtilizationDetailResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryRIUtilizationDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRIUtilizationDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRIUtilizationDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryRIUtilizationDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySavingsPlansDeductLogRequest(TeaModel):
    def __init__(self, instance_type=None, page_size=None, locale=None, page_num=None, instance_id=None,
                 start_time=None, end_time=None):
        self.instance_type = instance_type  # type: str
        self.page_size = page_size  # type: int
        self.locale = locale  # type: str
        self.page_num = page_num  # type: int
        self.instance_id = instance_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QuerySavingsPlansDeductLogResponseBodyDataItems(TeaModel):
    def __init__(self, end_time=None, start_time=None, savings_type=None, user_id=None, discount_rate=None,
                 bill_module=None, instance_id=None, deduct_instance_id=None, deduct_commodity=None, deduct_rate=None,
                 deduct_fee=None):
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.savings_type = savings_type  # type: str
        self.user_id = user_id  # type: long
        self.discount_rate = discount_rate  # type: str
        self.bill_module = bill_module  # type: str
        self.instance_id = instance_id  # type: str
        self.deduct_instance_id = deduct_instance_id  # type: str
        self.deduct_commodity = deduct_commodity  # type: str
        self.deduct_rate = deduct_rate  # type: str
        self.deduct_fee = deduct_fee  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.savings_type is not None:
            result['SavingsType'] = self.savings_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.discount_rate is not None:
            result['DiscountRate'] = self.discount_rate
        if self.bill_module is not None:
            result['BillModule'] = self.bill_module
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.deduct_instance_id is not None:
            result['DeductInstanceId'] = self.deduct_instance_id
        if self.deduct_commodity is not None:
            result['DeductCommodity'] = self.deduct_commodity
        if self.deduct_rate is not None:
            result['DeductRate'] = self.deduct_rate
        if self.deduct_fee is not None:
            result['DeductFee'] = self.deduct_fee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('SavingsType') is not None:
            self.savings_type = m.get('SavingsType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DiscountRate') is not None:
            self.discount_rate = m.get('DiscountRate')
        if m.get('BillModule') is not None:
            self.bill_module = m.get('BillModule')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DeductInstanceId') is not None:
            self.deduct_instance_id = m.get('DeductInstanceId')
        if m.get('DeductCommodity') is not None:
            self.deduct_commodity = m.get('DeductCommodity')
        if m.get('DeductRate') is not None:
            self.deduct_rate = m.get('DeductRate')
        if m.get('DeductFee') is not None:
            self.deduct_fee = m.get('DeductFee')
        return self


class QuerySavingsPlansDeductLogResponseBodyData(TeaModel):
    def __init__(self, items=None, page_num=None, page_size=None, total_count=None):
        self.items = items  # type: list[QuerySavingsPlansDeductLogResponseBodyDataItems]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QuerySavingsPlansDeductLogResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySavingsPlansDeductLogResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QuerySavingsPlansDeductLogResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QuerySavingsPlansDeductLogResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySavingsPlansDeductLogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySavingsPlansDeductLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySavingsPlansDeductLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySavingsPlansInstanceRequest(TeaModel):
    def __init__(self, page_size=None, locale=None, page_num=None, instance_id=None, start_time=None, end_time=None):
        self.page_size = page_size  # type: int
        self.locale = locale  # type: str
        self.page_num = page_num  # type: int
        self.instance_id = instance_id  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.locale is not None:
            result['Locale'] = self.locale
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Locale') is not None:
            self.locale = m.get('Locale')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QuerySavingsPlansInstanceResponseBodyDataItems(TeaModel):
    def __init__(self, status=None, share=None, savings_type=None, prepay_fee=None, utilization=None,
                 instance_id=None, currency=None, end_time=None, start_time=None, instance_family=None, region=None,
                 total_save=None, pool_value=None, pay_mode=None):
        self.status = status  # type: str
        self.share = share  # type: bool
        self.savings_type = savings_type  # type: str
        self.prepay_fee = prepay_fee  # type: str
        self.utilization = utilization  # type: str
        self.instance_id = instance_id  # type: str
        self.currency = currency  # type: str
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str
        self.instance_family = instance_family  # type: str
        self.region = region  # type: str
        self.total_save = total_save  # type: str
        self.pool_value = pool_value  # type: str
        self.pay_mode = pay_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.share is not None:
            result['Share'] = self.share
        if self.savings_type is not None:
            result['SavingsType'] = self.savings_type
        if self.prepay_fee is not None:
            result['PrepayFee'] = self.prepay_fee
        if self.utilization is not None:
            result['Utilization'] = self.utilization
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.instance_family is not None:
            result['InstanceFamily'] = self.instance_family
        if self.region is not None:
            result['Region'] = self.region
        if self.total_save is not None:
            result['TotalSave'] = self.total_save
        if self.pool_value is not None:
            result['PoolValue'] = self.pool_value
        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Share') is not None:
            self.share = m.get('Share')
        if m.get('SavingsType') is not None:
            self.savings_type = m.get('SavingsType')
        if m.get('PrepayFee') is not None:
            self.prepay_fee = m.get('PrepayFee')
        if m.get('Utilization') is not None:
            self.utilization = m.get('Utilization')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('InstanceFamily') is not None:
            self.instance_family = m.get('InstanceFamily')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('TotalSave') is not None:
            self.total_save = m.get('TotalSave')
        if m.get('PoolValue') is not None:
            self.pool_value = m.get('PoolValue')
        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')
        return self


class QuerySavingsPlansInstanceResponseBodyData(TeaModel):
    def __init__(self, items=None, page_num=None, page_size=None, total_count=None):
        self.items = items  # type: list[QuerySavingsPlansInstanceResponseBodyDataItems]
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Items'] = []
        if self.items is not None:
            for k in self.items:
                result['Items'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k in m.get('Items'):
                temp_model = QuerySavingsPlansInstanceResponseBodyDataItems()
                self.items.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySavingsPlansInstanceResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QuerySavingsPlansInstanceResponseBodyData
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QuerySavingsPlansInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySavingsPlansInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySavingsPlansInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySavingsPlansInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySettleBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, type=None, product_code=None, product_type=None, subscription_type=None,
                 is_hide_zero_charge=None, is_display_local_currency=None, owner_id=None, next_token=None, max_results=None,
                 bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.type = type  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool
        self.is_display_local_currency = is_display_local_currency  # type: bool
        self.owner_id = owner_id  # type: long
        self.next_token = next_token  # type: str
        self.max_results = max_results  # type: int
        self.bill_owner_id = bill_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.type is not None:
            result['Type'] = self.type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        if self.is_display_local_currency is not None:
            result['IsDisplayLocalCurrency'] = self.is_display_local_currency
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        if m.get('IsDisplayLocalCurrency') is not None:
            self.is_display_local_currency = m.get('IsDisplayLocalCurrency')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QuerySettleBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, after_tax_amount=None, commodity_code=None, currency=None, deducted_by_cash_coupons=None,
                 deducted_by_coupons=None, deducted_by_prepaid_card=None, invoice_discount=None, item=None, outstanding_amount=None,
                 owner_id=None, payment_amount=None, payment_currency=None, payment_time=None, payment_transaction_id=None,
                 pip_code=None, pretax_amount=None, pretax_amount_local=None, pretax_gross_amount=None, product_code=None,
                 product_detail=None, product_name=None, product_type=None, record_id=None, round_down_discount=None, status=None,
                 sub_order_id=None, subscription_type=None, tax=None, usage_end_time=None, usage_start_time=None):
        self.after_tax_amount = after_tax_amount  # type: float
        self.commodity_code = commodity_code  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.invoice_discount = invoice_discount  # type: float
        self.item = item  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.owner_id = owner_id  # type: str
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.payment_time = payment_time  # type: str
        self.payment_transaction_id = payment_transaction_id  # type: str
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_detail = product_detail  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.record_id = record_id  # type: str
        self.round_down_discount = round_down_discount  # type: str
        self.status = status  # type: str
        self.sub_order_id = sub_order_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: float
        self.usage_end_time = usage_end_time  # type: str
        self.usage_start_time = usage_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.item is not None:
            result['Item'] = self.item
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.payment_transaction_id is not None:
            result['PaymentTransactionID'] = self.payment_transaction_id
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.round_down_discount is not None:
            result['RoundDownDiscount'] = self.round_down_discount
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_order_id is not None:
            result['SubOrderId'] = self.sub_order_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PaymentTransactionID') is not None:
            self.payment_transaction_id = m.get('PaymentTransactionID')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('RoundDownDiscount') is not None:
            self.round_down_discount = m.get('RoundDownDiscount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubOrderId') is not None:
            self.sub_order_id = m.get('SubOrderId')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        return self


class QuerySettleBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QuerySettleBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QuerySettleBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QuerySettleBillResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, billing_cycle=None, items=None, max_results=None,
                 next_token=None, total_count=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QuerySettleBillResponseBodyDataItems
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QuerySettleBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySettleBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QuerySettleBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QuerySettleBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySettleBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySettleBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySettleBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySettlementBillRequest(TeaModel):
    def __init__(self, page_size=None, owner_id=None, page_num=None, billing_cycle=None, start_time=None,
                 end_time=None, type=None, product_code=None, product_type=None, subscription_type=None,
                 is_hide_zero_charge=None):
        self.page_size = page_size  # type: int
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.billing_cycle = billing_cycle  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.type = type  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.is_hide_zero_charge = is_hide_zero_charge  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.is_hide_zero_charge is not None:
            result['IsHideZeroCharge'] = self.is_hide_zero_charge
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('IsHideZeroCharge') is not None:
            self.is_hide_zero_charge = m.get('IsHideZeroCharge')
        return self


class QuerySettlementBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, account_discount=None, after_tax_amount=None, bill_id=None, charge_discount=None,
                 cleared_time=None, config=None, create_time=None, currency=None, deducted_by_cash_coupons=None,
                 deducted_by_coupons=None, deducted_by_prepaid_card=None, invoice_no=None, item=None, linked_customer_order_id=None,
                 mybank_payment_amount=None, order_id=None, order_type=None, original_order_id=None, outstanding_amount=None,
                 owner_id=None, payer_account=None, payment_amount=None, payment_currency=None, payment_time=None,
                 pretax_amount=None, pretax_amount_local=None, pretax_gross_amount=None, previous_billing_cycle_balance=None,
                 product_code=None, product_type=None, promotion=None, quantity=None, record_id=None, region=None, seller=None,
                 solution_id=None, solution_name=None, status=None, suborder_id=None, subscription_type=None, tax=None,
                 usage_end_time=None, usage_start_time=None):
        self.account_discount = account_discount  # type: float
        self.after_tax_amount = after_tax_amount  # type: float
        self.bill_id = bill_id  # type: str
        self.charge_discount = charge_discount  # type: float
        self.cleared_time = cleared_time  # type: str
        self.config = config  # type: str
        self.create_time = create_time  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.invoice_no = invoice_no  # type: str
        self.item = item  # type: str
        self.linked_customer_order_id = linked_customer_order_id  # type: str
        self.mybank_payment_amount = mybank_payment_amount  # type: float
        self.order_id = order_id  # type: str
        self.order_type = order_type  # type: str
        self.original_order_id = original_order_id  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.owner_id = owner_id  # type: str
        self.payer_account = payer_account  # type: str
        self.payment_amount = payment_amount  # type: float
        self.payment_currency = payment_currency  # type: str
        self.payment_time = payment_time  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_amount_local = pretax_amount_local  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.previous_billing_cycle_balance = previous_billing_cycle_balance  # type: float
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.promotion = promotion  # type: str
        self.quantity = quantity  # type: str
        self.record_id = record_id  # type: str
        self.region = region  # type: str
        self.seller = seller  # type: str
        self.solution_id = solution_id  # type: str
        self.solution_name = solution_name  # type: str
        self.status = status  # type: str
        self.suborder_id = suborder_id  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tax = tax  # type: float
        self.usage_end_time = usage_end_time  # type: str
        self.usage_start_time = usage_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.account_discount is not None:
            result['AccountDiscount'] = self.account_discount
        if self.after_tax_amount is not None:
            result['AfterTaxAmount'] = self.after_tax_amount
        if self.bill_id is not None:
            result['BillID'] = self.bill_id
        if self.charge_discount is not None:
            result['ChargeDiscount'] = self.charge_discount
        if self.cleared_time is not None:
            result['ClearedTime'] = self.cleared_time
        if self.config is not None:
            result['Config'] = self.config
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.invoice_no is not None:
            result['InvoiceNo'] = self.invoice_no
        if self.item is not None:
            result['Item'] = self.item
        if self.linked_customer_order_id is not None:
            result['LinkedCustomerOrderID'] = self.linked_customer_order_id
        if self.mybank_payment_amount is not None:
            result['MybankPaymentAmount'] = self.mybank_payment_amount
        if self.order_id is not None:
            result['OrderID'] = self.order_id
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.original_order_id is not None:
            result['OriginalOrderID'] = self.original_order_id
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.payer_account is not None:
            result['PayerAccount'] = self.payer_account
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.payment_currency is not None:
            result['PaymentCurrency'] = self.payment_currency
        if self.payment_time is not None:
            result['PaymentTime'] = self.payment_time
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_amount_local is not None:
            result['PretaxAmountLocal'] = self.pretax_amount_local
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.previous_billing_cycle_balance is not None:
            result['PreviousBillingCycleBalance'] = self.previous_billing_cycle_balance
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion is not None:
            result['Promotion'] = self.promotion
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.record_id is not None:
            result['RecordID'] = self.record_id
        if self.region is not None:
            result['Region'] = self.region
        if self.seller is not None:
            result['Seller'] = self.seller
        if self.solution_id is not None:
            result['SolutionID'] = self.solution_id
        if self.solution_name is not None:
            result['SolutionName'] = self.solution_name
        if self.status is not None:
            result['Status'] = self.status
        if self.suborder_id is not None:
            result['SuborderID'] = self.suborder_id
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tax is not None:
            result['Tax'] = self.tax
        if self.usage_end_time is not None:
            result['UsageEndTime'] = self.usage_end_time
        if self.usage_start_time is not None:
            result['UsageStartTime'] = self.usage_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountDiscount') is not None:
            self.account_discount = m.get('AccountDiscount')
        if m.get('AfterTaxAmount') is not None:
            self.after_tax_amount = m.get('AfterTaxAmount')
        if m.get('BillID') is not None:
            self.bill_id = m.get('BillID')
        if m.get('ChargeDiscount') is not None:
            self.charge_discount = m.get('ChargeDiscount')
        if m.get('ClearedTime') is not None:
            self.cleared_time = m.get('ClearedTime')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('InvoiceNo') is not None:
            self.invoice_no = m.get('InvoiceNo')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('LinkedCustomerOrderID') is not None:
            self.linked_customer_order_id = m.get('LinkedCustomerOrderID')
        if m.get('MybankPaymentAmount') is not None:
            self.mybank_payment_amount = m.get('MybankPaymentAmount')
        if m.get('OrderID') is not None:
            self.order_id = m.get('OrderID')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('OriginalOrderID') is not None:
            self.original_order_id = m.get('OriginalOrderID')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PayerAccount') is not None:
            self.payer_account = m.get('PayerAccount')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PaymentCurrency') is not None:
            self.payment_currency = m.get('PaymentCurrency')
        if m.get('PaymentTime') is not None:
            self.payment_time = m.get('PaymentTime')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxAmountLocal') is not None:
            self.pretax_amount_local = m.get('PretaxAmountLocal')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('PreviousBillingCycleBalance') is not None:
            self.previous_billing_cycle_balance = m.get('PreviousBillingCycleBalance')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Promotion') is not None:
            self.promotion = m.get('Promotion')
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('RecordID') is not None:
            self.record_id = m.get('RecordID')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Seller') is not None:
            self.seller = m.get('Seller')
        if m.get('SolutionID') is not None:
            self.solution_id = m.get('SolutionID')
        if m.get('SolutionName') is not None:
            self.solution_name = m.get('SolutionName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuborderID') is not None:
            self.suborder_id = m.get('SuborderID')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tax') is not None:
            self.tax = m.get('Tax')
        if m.get('UsageEndTime') is not None:
            self.usage_end_time = m.get('UsageEndTime')
        if m.get('UsageStartTime') is not None:
            self.usage_start_time = m.get('UsageStartTime')
        return self


class QuerySettlementBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QuerySettlementBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QuerySettlementBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QuerySettlementBillResponseBodyData(TeaModel):
    def __init__(self, billing_cycle=None, items=None, page_num=None, page_size=None, total_count=None):
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QuerySettlementBillResponseBodyDataItems
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QuerySettlementBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySettlementBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QuerySettlementBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QuerySettlementBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySettlementBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySettlementBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySettlementBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySplitItemBillRequest(TeaModel):
    def __init__(self, billing_cycle=None, product_code=None, product_type=None, subscription_type=None,
                 owner_id=None, page_num=None, page_size=None, bill_owner_id=None):
        self.billing_cycle = billing_cycle  # type: str
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.owner_id = owner_id  # type: long
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.bill_owner_id = bill_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.bill_owner_id is not None:
            result['BillOwnerId'] = self.bill_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('BillOwnerId') is not None:
            self.bill_owner_id = m.get('BillOwnerId')
        return self


class QuerySplitItemBillResponseBodyDataItemsItem(TeaModel):
    def __init__(self, billing_date=None, billing_item=None, billing_type=None, commodity_code=None, cost_unit=None,
                 currency=None, deducted_by_cash_coupons=None, deducted_by_coupons=None, deducted_by_prepaid_card=None,
                 deducted_by_resource_package=None, instance_config=None, instance_id=None, instance_spec=None, internet_ip=None,
                 intranet_ip=None, invoice_discount=None, item=None, list_price=None, list_price_unit=None, nick_name=None,
                 outstanding_amount=None, owner_id=None, payment_amount=None, pip_code=None, pretax_amount=None,
                 pretax_gross_amount=None, product_code=None, product_detail=None, product_name=None, product_type=None, region=None,
                 resource_group=None, service_period=None, split_item_id=None, split_item_name=None, subscription_type=None,
                 tag=None, usage=None, usage_unit=None, zone=None):
        self.billing_date = billing_date  # type: str
        self.billing_item = billing_item  # type: str
        self.billing_type = billing_type  # type: str
        self.commodity_code = commodity_code  # type: str
        self.cost_unit = cost_unit  # type: str
        self.currency = currency  # type: str
        self.deducted_by_cash_coupons = deducted_by_cash_coupons  # type: float
        self.deducted_by_coupons = deducted_by_coupons  # type: float
        self.deducted_by_prepaid_card = deducted_by_prepaid_card  # type: float
        self.deducted_by_resource_package = deducted_by_resource_package  # type: str
        self.instance_config = instance_config  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_spec = instance_spec  # type: str
        self.internet_ip = internet_ip  # type: str
        self.intranet_ip = intranet_ip  # type: str
        self.invoice_discount = invoice_discount  # type: float
        self.item = item  # type: str
        self.list_price = list_price  # type: str
        self.list_price_unit = list_price_unit  # type: str
        self.nick_name = nick_name  # type: str
        self.outstanding_amount = outstanding_amount  # type: float
        self.owner_id = owner_id  # type: str
        self.payment_amount = payment_amount  # type: float
        self.pip_code = pip_code  # type: str
        self.pretax_amount = pretax_amount  # type: float
        self.pretax_gross_amount = pretax_gross_amount  # type: float
        self.product_code = product_code  # type: str
        self.product_detail = product_detail  # type: str
        self.product_name = product_name  # type: str
        self.product_type = product_type  # type: str
        self.region = region  # type: str
        self.resource_group = resource_group  # type: str
        self.service_period = service_period  # type: str
        self.split_item_id = split_item_id  # type: str
        self.split_item_name = split_item_name  # type: str
        self.subscription_type = subscription_type  # type: str
        self.tag = tag  # type: str
        self.usage = usage  # type: str
        self.usage_unit = usage_unit  # type: str
        self.zone = zone  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.billing_date is not None:
            result['BillingDate'] = self.billing_date
        if self.billing_item is not None:
            result['BillingItem'] = self.billing_item
        if self.billing_type is not None:
            result['BillingType'] = self.billing_type
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.cost_unit is not None:
            result['CostUnit'] = self.cost_unit
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.deducted_by_cash_coupons is not None:
            result['DeductedByCashCoupons'] = self.deducted_by_cash_coupons
        if self.deducted_by_coupons is not None:
            result['DeductedByCoupons'] = self.deducted_by_coupons
        if self.deducted_by_prepaid_card is not None:
            result['DeductedByPrepaidCard'] = self.deducted_by_prepaid_card
        if self.deducted_by_resource_package is not None:
            result['DeductedByResourcePackage'] = self.deducted_by_resource_package
        if self.instance_config is not None:
            result['InstanceConfig'] = self.instance_config
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id
        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec
        if self.internet_ip is not None:
            result['InternetIP'] = self.internet_ip
        if self.intranet_ip is not None:
            result['IntranetIP'] = self.intranet_ip
        if self.invoice_discount is not None:
            result['InvoiceDiscount'] = self.invoice_discount
        if self.item is not None:
            result['Item'] = self.item
        if self.list_price is not None:
            result['ListPrice'] = self.list_price
        if self.list_price_unit is not None:
            result['ListPriceUnit'] = self.list_price_unit
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.outstanding_amount is not None:
            result['OutstandingAmount'] = self.outstanding_amount
        if self.owner_id is not None:
            result['OwnerID'] = self.owner_id
        if self.payment_amount is not None:
            result['PaymentAmount'] = self.payment_amount
        if self.pip_code is not None:
            result['PipCode'] = self.pip_code
        if self.pretax_amount is not None:
            result['PretaxAmount'] = self.pretax_amount
        if self.pretax_gross_amount is not None:
            result['PretaxGrossAmount'] = self.pretax_gross_amount
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.service_period is not None:
            result['ServicePeriod'] = self.service_period
        if self.split_item_id is not None:
            result['SplitItemID'] = self.split_item_id
        if self.split_item_name is not None:
            result['SplitItemName'] = self.split_item_name
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.usage is not None:
            result['Usage'] = self.usage
        if self.usage_unit is not None:
            result['UsageUnit'] = self.usage_unit
        if self.zone is not None:
            result['Zone'] = self.zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BillingDate') is not None:
            self.billing_date = m.get('BillingDate')
        if m.get('BillingItem') is not None:
            self.billing_item = m.get('BillingItem')
        if m.get('BillingType') is not None:
            self.billing_type = m.get('BillingType')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('CostUnit') is not None:
            self.cost_unit = m.get('CostUnit')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DeductedByCashCoupons') is not None:
            self.deducted_by_cash_coupons = m.get('DeductedByCashCoupons')
        if m.get('DeductedByCoupons') is not None:
            self.deducted_by_coupons = m.get('DeductedByCoupons')
        if m.get('DeductedByPrepaidCard') is not None:
            self.deducted_by_prepaid_card = m.get('DeductedByPrepaidCard')
        if m.get('DeductedByResourcePackage') is not None:
            self.deducted_by_resource_package = m.get('DeductedByResourcePackage')
        if m.get('InstanceConfig') is not None:
            self.instance_config = m.get('InstanceConfig')
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')
        if m.get('InstanceSpec') is not None:
            self.instance_spec = m.get('InstanceSpec')
        if m.get('InternetIP') is not None:
            self.internet_ip = m.get('InternetIP')
        if m.get('IntranetIP') is not None:
            self.intranet_ip = m.get('IntranetIP')
        if m.get('InvoiceDiscount') is not None:
            self.invoice_discount = m.get('InvoiceDiscount')
        if m.get('Item') is not None:
            self.item = m.get('Item')
        if m.get('ListPrice') is not None:
            self.list_price = m.get('ListPrice')
        if m.get('ListPriceUnit') is not None:
            self.list_price_unit = m.get('ListPriceUnit')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OutstandingAmount') is not None:
            self.outstanding_amount = m.get('OutstandingAmount')
        if m.get('OwnerID') is not None:
            self.owner_id = m.get('OwnerID')
        if m.get('PaymentAmount') is not None:
            self.payment_amount = m.get('PaymentAmount')
        if m.get('PipCode') is not None:
            self.pip_code = m.get('PipCode')
        if m.get('PretaxAmount') is not None:
            self.pretax_amount = m.get('PretaxAmount')
        if m.get('PretaxGrossAmount') is not None:
            self.pretax_gross_amount = m.get('PretaxGrossAmount')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductDetail') is not None:
            self.product_detail = m.get('ProductDetail')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('ServicePeriod') is not None:
            self.service_period = m.get('ServicePeriod')
        if m.get('SplitItemID') is not None:
            self.split_item_id = m.get('SplitItemID')
        if m.get('SplitItemName') is not None:
            self.split_item_name = m.get('SplitItemName')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Usage') is not None:
            self.usage = m.get('Usage')
        if m.get('UsageUnit') is not None:
            self.usage_unit = m.get('UsageUnit')
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')
        return self


class QuerySplitItemBillResponseBodyDataItems(TeaModel):
    def __init__(self, item=None):
        self.item = item  # type: list[QuerySplitItemBillResponseBodyDataItemsItem]

    def validate(self):
        if self.item:
            for k in self.item:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Item'] = []
        if self.item is not None:
            for k in self.item:
                result['Item'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k in m.get('Item'):
                temp_model = QuerySplitItemBillResponseBodyDataItemsItem()
                self.item.append(temp_model.from_map(k))
        return self


class QuerySplitItemBillResponseBodyData(TeaModel):
    def __init__(self, account_id=None, account_name=None, billing_cycle=None, items=None, page_num=None,
                 page_size=None, total_count=None):
        self.account_id = account_id  # type: str
        self.account_name = account_name  # type: str
        self.billing_cycle = billing_cycle  # type: str
        self.items = items  # type: QuerySplitItemBillResponseBodyDataItems
        self.page_num = page_num  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        if self.account_id is not None:
            result['AccountID'] = self.account_id
        if self.account_name is not None:
            result['AccountName'] = self.account_name
        if self.billing_cycle is not None:
            result['BillingCycle'] = self.billing_cycle
        if self.items is not None:
            result['Items'] = self.items.to_map()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccountID') is not None:
            self.account_id = m.get('AccountID')
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')
        if m.get('BillingCycle') is not None:
            self.billing_cycle = m.get('BillingCycle')
        if m.get('Items') is not None:
            temp_model = QuerySplitItemBillResponseBodyDataItems()
            self.items = temp_model.from_map(m['Items'])
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QuerySplitItemBillResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QuerySplitItemBillResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QuerySplitItemBillResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySplitItemBillResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySplitItemBillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QuerySplitItemBillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserOmsDataRequest(TeaModel):
    def __init__(self, owner_id=None, table=None, data_type=None, start_time=None, end_time=None, marker=None,
                 page_size=None):
        self.owner_id = owner_id  # type: long
        self.table = table  # type: str
        self.data_type = data_type  # type: str
        self.start_time = start_time  # type: str
        self.end_time = end_time  # type: str
        self.marker = marker  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.table is not None:
            result['Table'] = self.table
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Table') is not None:
            self.table = m.get('Table')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryUserOmsDataResponseBodyData(TeaModel):
    def __init__(self, host_id=None, marker=None, oms_data=None):
        self.host_id = host_id  # type: str
        self.marker = marker  # type: str
        self.oms_data = oms_data  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.oms_data is not None:
            result['OmsData'] = self.oms_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('OmsData') is not None:
            self.oms_data = m.get('OmsData')
        return self


class QueryUserOmsDataResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryUserOmsDataResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryUserOmsDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserOmsDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUserOmsDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryUserOmsDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, product_code=None, instance_id=None, renew_period=None, client_token=None, product_type=None,
                 owner_id=None):
        self.product_code = product_code  # type: str
        self.instance_id = instance_id  # type: str
        self.renew_period = renew_period  # type: int
        self.client_token = client_token  # type: str
        self.product_type = product_type  # type: str
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.renew_period is not None:
            result['RenewPeriod'] = self.renew_period
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RenewPeriod') is not None:
            self.renew_period = m.get('RenewPeriod')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: RenewInstanceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewResourcePackageRequest(TeaModel):
    def __init__(self, owner_id=None, instance_id=None, effective_date=None, duration=None, pricing_cycle=None):
        self.owner_id = owner_id  # type: long
        self.instance_id = instance_id  # type: str
        self.effective_date = effective_date  # type: str
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewResourcePackageResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class RenewResourcePackageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, order_id=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: RenewResourcePackageResponseBodyData
        self.message = message  # type: str
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
            temp_model = RenewResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RenewResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenewResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveUserCreditRequest(TeaModel):
    def __init__(self, avoid_expiration=None, avoid_prepaid_notification=None, description=None,
                 avoid_notification=None, credit_value=None, avoid_prepaid_expiration=None, operator=None, credit_type=None):
        self.avoid_expiration = avoid_expiration  # type: bool
        self.avoid_prepaid_notification = avoid_prepaid_notification  # type: bool
        self.description = description  # type: str
        self.avoid_notification = avoid_notification  # type: bool
        self.credit_value = credit_value  # type: str
        self.avoid_prepaid_expiration = avoid_prepaid_expiration  # type: bool
        self.operator = operator  # type: str
        self.credit_type = credit_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.avoid_expiration is not None:
            result['AvoidExpiration'] = self.avoid_expiration
        if self.avoid_prepaid_notification is not None:
            result['AvoidPrepaidNotification'] = self.avoid_prepaid_notification
        if self.description is not None:
            result['Description'] = self.description
        if self.avoid_notification is not None:
            result['AvoidNotification'] = self.avoid_notification
        if self.credit_value is not None:
            result['CreditValue'] = self.credit_value
        if self.avoid_prepaid_expiration is not None:
            result['AvoidPrepaidExpiration'] = self.avoid_prepaid_expiration
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.credit_type is not None:
            result['CreditType'] = self.credit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvoidExpiration') is not None:
            self.avoid_expiration = m.get('AvoidExpiration')
        if m.get('AvoidPrepaidNotification') is not None:
            self.avoid_prepaid_notification = m.get('AvoidPrepaidNotification')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('AvoidNotification') is not None:
            self.avoid_notification = m.get('AvoidNotification')
        if m.get('CreditValue') is not None:
            self.credit_value = m.get('CreditValue')
        if m.get('AvoidPrepaidExpiration') is not None:
            self.avoid_prepaid_expiration = m.get('AvoidPrepaidExpiration')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('CreditType') is not None:
            self.credit_type = m.get('CreditType')
        return self


class SaveUserCreditResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveUserCreditResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SaveUserCreditResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveUserCreditResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetCreditLabelActionRequest(TeaModel):
    def __init__(self, action_type=None, uid=None, clear_cycle=None, credit_amount=None, currency_code=None,
                 daily_cycle=None, description=None, is_need_add_settle_label=None, is_need_adjust_credit_account=None,
                 is_need_save_notify_rule=None, is_need_set_credit_amount=None, need_notice=None, new_create_mode=None, operator=None,
                 request_id=None, site_code=None, source=None):
        self.action_type = action_type  # type: str
        self.uid = uid  # type: str
        self.clear_cycle = clear_cycle  # type: str
        self.credit_amount = credit_amount  # type: str
        self.currency_code = currency_code  # type: str
        self.daily_cycle = daily_cycle  # type: str
        self.description = description  # type: str
        self.is_need_add_settle_label = is_need_add_settle_label  # type: str
        self.is_need_adjust_credit_account = is_need_adjust_credit_account  # type: str
        self.is_need_save_notify_rule = is_need_save_notify_rule  # type: str
        self.is_need_set_credit_amount = is_need_set_credit_amount  # type: str
        self.need_notice = need_notice  # type: bool
        self.new_create_mode = new_create_mode  # type: bool
        self.operator = operator  # type: str
        self.request_id = request_id  # type: str
        self.site_code = site_code  # type: str
        self.source = source  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.clear_cycle is not None:
            result['ClearCycle'] = self.clear_cycle
        if self.credit_amount is not None:
            result['CreditAmount'] = self.credit_amount
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.daily_cycle is not None:
            result['DailyCycle'] = self.daily_cycle
        if self.description is not None:
            result['Description'] = self.description
        if self.is_need_add_settle_label is not None:
            result['IsNeedAddSettleLabel'] = self.is_need_add_settle_label
        if self.is_need_adjust_credit_account is not None:
            result['IsNeedAdjustCreditAccount'] = self.is_need_adjust_credit_account
        if self.is_need_save_notify_rule is not None:
            result['IsNeedSaveNotifyRule'] = self.is_need_save_notify_rule
        if self.is_need_set_credit_amount is not None:
            result['IsNeedSetCreditAmount'] = self.is_need_set_credit_amount
        if self.need_notice is not None:
            result['NeedNotice'] = self.need_notice
        if self.new_create_mode is not None:
            result['NewCreateMode'] = self.new_create_mode
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.site_code is not None:
            result['SiteCode'] = self.site_code
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('ClearCycle') is not None:
            self.clear_cycle = m.get('ClearCycle')
        if m.get('CreditAmount') is not None:
            self.credit_amount = m.get('CreditAmount')
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('DailyCycle') is not None:
            self.daily_cycle = m.get('DailyCycle')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsNeedAddSettleLabel') is not None:
            self.is_need_add_settle_label = m.get('IsNeedAddSettleLabel')
        if m.get('IsNeedAdjustCreditAccount') is not None:
            self.is_need_adjust_credit_account = m.get('IsNeedAdjustCreditAccount')
        if m.get('IsNeedSaveNotifyRule') is not None:
            self.is_need_save_notify_rule = m.get('IsNeedSaveNotifyRule')
        if m.get('IsNeedSetCreditAmount') is not None:
            self.is_need_set_credit_amount = m.get('IsNeedSetCreditAmount')
        if m.get('NeedNotice') is not None:
            self.need_notice = m.get('NeedNotice')
        if m.get('NewCreateMode') is not None:
            self.new_create_mode = m.get('NewCreateMode')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SiteCode') is not None:
            self.site_code = m.get('SiteCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class SetCreditLabelActionResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: bool
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetCreditLabelActionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetCreditLabelActionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetCreditLabelActionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetRenewalRequest(TeaModel):
    def __init__(self, renewal_period=None, instance_ids=None, owner_id=None, product_code=None, product_type=None,
                 subscription_type=None, renewal_period_unit=None, renewal_status=None):
        self.renewal_period = renewal_period  # type: int
        self.instance_ids = instance_ids  # type: str
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.product_type = product_type  # type: str
        self.subscription_type = subscription_type  # type: str
        self.renewal_period_unit = renewal_period_unit  # type: str
        self.renewal_status = renewal_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.renewal_period is not None:
            result['RenewalPeriod'] = self.renewal_period
        if self.instance_ids is not None:
            result['InstanceIDs'] = self.instance_ids
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.subscription_type is not None:
            result['SubscriptionType'] = self.subscription_type
        if self.renewal_period_unit is not None:
            result['RenewalPeriodUnit'] = self.renewal_period_unit
        if self.renewal_status is not None:
            result['RenewalStatus'] = self.renewal_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenewalPeriod') is not None:
            self.renewal_period = m.get('RenewalPeriod')
        if m.get('InstanceIDs') is not None:
            self.instance_ids = m.get('InstanceIDs')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SubscriptionType') is not None:
            self.subscription_type = m.get('SubscriptionType')
        if m.get('RenewalPeriodUnit') is not None:
            self.renewal_period_unit = m.get('RenewalPeriodUnit')
        if m.get('RenewalStatus') is not None:
            self.renewal_status = m.get('RenewalStatus')
        return self


class SetRenewalResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetRenewalResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetRenewalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetRenewalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetResellerUserAlarmThresholdRequest(TeaModel):
    def __init__(self, owner_id=None, alarm_type=None, alarm_thresholds=None):
        self.owner_id = owner_id  # type: long
        self.alarm_type = alarm_type  # type: str
        self.alarm_thresholds = alarm_thresholds  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.alarm_type is not None:
            result['AlarmType'] = self.alarm_type
        if self.alarm_thresholds is not None:
            result['AlarmThresholds'] = self.alarm_thresholds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('AlarmType') is not None:
            self.alarm_type = m.get('AlarmType')
        if m.get('AlarmThresholds') is not None:
            self.alarm_thresholds = m.get('AlarmThresholds')
        return self


class SetResellerUserAlarmThresholdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class SetResellerUserAlarmThresholdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetResellerUserAlarmThresholdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetResellerUserAlarmThresholdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetResellerUserQuotaRequest(TeaModel):
    def __init__(self, owner_id=None, amount=None, currency=None, out_biz_id=None):
        self.owner_id = owner_id  # type: long
        self.amount = amount  # type: str
        self.currency = currency  # type: str
        self.out_biz_id = out_biz_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.out_biz_id is not None:
            result['OutBizId'] = self.out_biz_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('OutBizId') is not None:
            self.out_biz_id = m.get('OutBizId')
        return self


class SetResellerUserQuotaResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class SetResellerUserQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetResellerUserQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetResellerUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetResellerUserStatusRequest(TeaModel):
    def __init__(self, owner_id=None, status=None, business_type=None):
        self.owner_id = owner_id  # type: str
        self.status = status  # type: str
        self.business_type = business_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        return self


class SetResellerUserStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
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


class SetResellerUserStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetResellerUserStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SetResellerUserStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubscribeBillToOSSRequest(TeaModel):
    def __init__(self, subscribe_bucket=None, subscribe_type=None, mult_account_rel_subscribe=None,
                 bucket_owner_id=None):
        self.subscribe_bucket = subscribe_bucket  # type: str
        self.subscribe_type = subscribe_type  # type: str
        self.mult_account_rel_subscribe = mult_account_rel_subscribe  # type: str
        self.bucket_owner_id = bucket_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_bucket is not None:
            result['SubscribeBucket'] = self.subscribe_bucket
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        if self.mult_account_rel_subscribe is not None:
            result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        if self.bucket_owner_id is not None:
            result['BucketOwnerId'] = self.bucket_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubscribeBucket') is not None:
            self.subscribe_bucket = m.get('SubscribeBucket')
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        if m.get('MultAccountRelSubscribe') is not None:
            self.mult_account_rel_subscribe = m.get('MultAccountRelSubscribe')
        if m.get('BucketOwnerId') is not None:
            self.bucket_owner_id = m.get('BucketOwnerId')
        return self


class SubscribeBillToOSSResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubscribeBillToOSSResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubscribeBillToOSSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubscribeBillToOSSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, resource_id=None, tag=None):
        self.resource_type = resource_type  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: bool
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnsubscribeBillToOSSRequest(TeaModel):
    def __init__(self, subscribe_type=None, mult_account_rel_subscribe=None):
        self.subscribe_type = subscribe_type  # type: str
        self.mult_account_rel_subscribe = mult_account_rel_subscribe  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.subscribe_type is not None:
            result['SubscribeType'] = self.subscribe_type
        if self.mult_account_rel_subscribe is not None:
            result['MultAccountRelSubscribe'] = self.mult_account_rel_subscribe
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SubscribeType') is not None:
            self.subscribe_type = m.get('SubscribeType')
        if m.get('MultAccountRelSubscribe') is not None:
            self.mult_account_rel_subscribe = m.get('MultAccountRelSubscribe')
        return self


class UnsubscribeBillToOSSResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnsubscribeBillToOSSResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnsubscribeBillToOSSResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnsubscribeBillToOSSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, resource_type=None, all=None, resource_id=None, tag_key=None):
        self.resource_type = resource_type  # type: str
        self.all = all  # type: bool
        self.resource_id = resource_id  # type: list[str]
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, data=None, code=None, success=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: bool
        self.code = code  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeResourcePackageRequest(TeaModel):
    def __init__(self, owner_id=None, instance_id=None, effective_date=None, specification=None):
        self.owner_id = owner_id  # type: long
        self.instance_id = instance_id  # type: str
        self.effective_date = effective_date  # type: str
        self.specification = specification  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.effective_date is not None:
            result['EffectiveDate'] = self.effective_date
        if self.specification is not None:
            result['Specification'] = self.specification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EffectiveDate') is not None:
            self.effective_date = m.get('EffectiveDate')
        if m.get('Specification') is not None:
            self.specification = m.get('Specification')
        return self


class UpgradeResourcePackageResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, order_id=None):
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class UpgradeResourcePackageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, order_id=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UpgradeResourcePackageResponseBodyData
        self.message = message  # type: str
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
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
            temp_model = UpgradeResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpgradeResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


