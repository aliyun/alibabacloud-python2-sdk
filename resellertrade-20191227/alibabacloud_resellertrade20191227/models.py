# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateCouponTemplateRequestCurrency(TeaModel):
    def __init__(self, currency_code=None, default_fraction_digits=None, numeric_code=None):
        self.currency_code = currency_code  # type: str
        self.default_fraction_digits = default_fraction_digits  # type: int
        self.numeric_code = numeric_code  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCouponTemplateRequestCurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        if self.default_fraction_digits is not None:
            result['DefaultFractionDigits'] = self.default_fraction_digits
        if self.numeric_code is not None:
            result['NumericCode'] = self.numeric_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        if m.get('DefaultFractionDigits') is not None:
            self.default_fraction_digits = m.get('DefaultFractionDigits')
        if m.get('NumericCode') is not None:
            self.numeric_code = m.get('NumericCode')
        return self


class CreateCouponTemplateRequest(TeaModel):
    def __init__(self, activity_site=None, bid=None, certain_money=None, client_type=None, commodity_type=None,
                 control_type=None, coupon_amount=None, coupon_end_time=None, coupon_fixed_type=None, coupon_start_time=None,
                 coupon_type=None, currency=None, description=None, discount_rate=None, end_time=None, extends_map=None,
                 from_app=None, item_code_set=None, market=None, market_type=None, max_release=None, message_id=None,
                 name=None, operator=None, order_type_set=None, per_limit_num=None, promotion_id=None, reason=None,
                 relative_second=None, request_id=None, selection_id_set=None, seller_id=None, site=None, sp_id=None,
                 start_time=None, type=None, universal_type=None, upper_limit=None, usage_count=None, use_scene=None,
                 user_pk_amount=None, validity_type=None):
        self.activity_site = activity_site  # type: int
        self.bid = bid  # type: long
        self.certain_money = certain_money  # type: float
        self.client_type = client_type  # type: str
        self.commodity_type = commodity_type  # type: str
        self.control_type = control_type  # type: str
        self.coupon_amount = coupon_amount  # type: float
        self.coupon_end_time = coupon_end_time  # type: str
        self.coupon_fixed_type = coupon_fixed_type  # type: str
        self.coupon_start_time = coupon_start_time  # type: str
        self.coupon_type = coupon_type  # type: str
        self.currency = currency  # type: CreateCouponTemplateRequestCurrency
        self.description = description  # type: str
        self.discount_rate = discount_rate  # type: float
        self.end_time = end_time  # type: str
        self.extends_map = extends_map  # type: dict[str, str]
        self.from_app = from_app  # type: str
        self.item_code_set = item_code_set  # type: list[str]
        self.market = market  # type: str
        self.market_type = market_type  # type: long
        self.max_release = max_release  # type: float
        self.message_id = message_id  # type: str
        self.name = name  # type: str
        self.operator = operator  # type: str
        self.order_type_set = order_type_set  # type: list[str]
        self.per_limit_num = per_limit_num  # type: int
        self.promotion_id = promotion_id  # type: long
        self.reason = reason  # type: str
        self.relative_second = relative_second  # type: int
        self.request_id = request_id  # type: str
        self.selection_id_set = selection_id_set  # type: list[str]
        self.seller_id = seller_id  # type: long
        self.site = site  # type: str
        self.sp_id = sp_id  # type: long
        self.start_time = start_time  # type: str
        self.type = type  # type: str
        self.universal_type = universal_type  # type: str
        self.upper_limit = upper_limit  # type: float
        self.usage_count = usage_count  # type: int
        self.use_scene = use_scene  # type: str
        self.user_pk_amount = user_pk_amount  # type: str
        self.validity_type = validity_type  # type: str

    def validate(self):
        if self.currency:
            self.currency.validate()

    def to_map(self):
        _map = super(CreateCouponTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_site is not None:
            result['ActivitySite'] = self.activity_site
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.certain_money is not None:
            result['CertainMoney'] = self.certain_money
        if self.client_type is not None:
            result['ClientType'] = self.client_type
        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.coupon_amount is not None:
            result['CouponAmount'] = self.coupon_amount
        if self.coupon_end_time is not None:
            result['CouponEndTime'] = self.coupon_end_time
        if self.coupon_fixed_type is not None:
            result['CouponFixedType'] = self.coupon_fixed_type
        if self.coupon_start_time is not None:
            result['CouponStartTime'] = self.coupon_start_time
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.currency is not None:
            result['Currency'] = self.currency.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.discount_rate is not None:
            result['DiscountRate'] = self.discount_rate
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extends_map is not None:
            result['ExtendsMap'] = self.extends_map
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.item_code_set is not None:
            result['ItemCodeSet'] = self.item_code_set
        if self.market is not None:
            result['Market'] = self.market
        if self.market_type is not None:
            result['MarketType'] = self.market_type
        if self.max_release is not None:
            result['MaxRelease'] = self.max_release
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.name is not None:
            result['Name'] = self.name
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.order_type_set is not None:
            result['OrderTypeSet'] = self.order_type_set
        if self.per_limit_num is not None:
            result['PerLimitNum'] = self.per_limit_num
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.relative_second is not None:
            result['RelativeSecond'] = self.relative_second
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.selection_id_set is not None:
            result['SelectionIdSet'] = self.selection_id_set
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.site is not None:
            result['Site'] = self.site
        if self.sp_id is not None:
            result['SpId'] = self.sp_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        if self.universal_type is not None:
            result['UniversalType'] = self.universal_type
        if self.upper_limit is not None:
            result['UpperLimit'] = self.upper_limit
        if self.usage_count is not None:
            result['UsageCount'] = self.usage_count
        if self.use_scene is not None:
            result['UseScene'] = self.use_scene
        if self.user_pk_amount is not None:
            result['UserPkAmount'] = self.user_pk_amount
        if self.validity_type is not None:
            result['ValidityType'] = self.validity_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivitySite') is not None:
            self.activity_site = m.get('ActivitySite')
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('CertainMoney') is not None:
            self.certain_money = m.get('CertainMoney')
        if m.get('ClientType') is not None:
            self.client_type = m.get('ClientType')
        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('CouponAmount') is not None:
            self.coupon_amount = m.get('CouponAmount')
        if m.get('CouponEndTime') is not None:
            self.coupon_end_time = m.get('CouponEndTime')
        if m.get('CouponFixedType') is not None:
            self.coupon_fixed_type = m.get('CouponFixedType')
        if m.get('CouponStartTime') is not None:
            self.coupon_start_time = m.get('CouponStartTime')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('Currency') is not None:
            temp_model = CreateCouponTemplateRequestCurrency()
            self.currency = temp_model.from_map(m['Currency'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiscountRate') is not None:
            self.discount_rate = m.get('DiscountRate')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendsMap') is not None:
            self.extends_map = m.get('ExtendsMap')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('ItemCodeSet') is not None:
            self.item_code_set = m.get('ItemCodeSet')
        if m.get('Market') is not None:
            self.market = m.get('Market')
        if m.get('MarketType') is not None:
            self.market_type = m.get('MarketType')
        if m.get('MaxRelease') is not None:
            self.max_release = m.get('MaxRelease')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('OrderTypeSet') is not None:
            self.order_type_set = m.get('OrderTypeSet')
        if m.get('PerLimitNum') is not None:
            self.per_limit_num = m.get('PerLimitNum')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('RelativeSecond') is not None:
            self.relative_second = m.get('RelativeSecond')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SelectionIdSet') is not None:
            self.selection_id_set = m.get('SelectionIdSet')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('SpId') is not None:
            self.sp_id = m.get('SpId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UniversalType') is not None:
            self.universal_type = m.get('UniversalType')
        if m.get('UpperLimit') is not None:
            self.upper_limit = m.get('UpperLimit')
        if m.get('UsageCount') is not None:
            self.usage_count = m.get('UsageCount')
        if m.get('UseScene') is not None:
            self.use_scene = m.get('UseScene')
        if m.get('UserPkAmount') is not None:
            self.user_pk_amount = m.get('UserPkAmount')
        if m.get('ValidityType') is not None:
            self.validity_type = m.get('ValidityType')
        return self


class CreateCouponTemplateResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        # result data
        self.data = data  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCouponTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateCouponTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCouponTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCouponTemplateResponse, self).to_map()
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
            temp_model = CreateCouponTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DiscardCouponListRequest(TeaModel):
    def __init__(self, coupon_list=None):
        self.coupon_list = coupon_list  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DiscardCouponListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.coupon_list is not None:
            result['CouponList'] = self.coupon_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CouponList') is not None:
            self.coupon_list = m.get('CouponList')
        return self


class DiscardCouponListResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        # result data
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DiscardCouponListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DiscardCouponListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DiscardCouponListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DiscardCouponListResponse, self).to_map()
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
            temp_model = DiscardCouponListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCouponPageRequest(TeaModel):
    def __init__(self, from_app=None, page_no=None, page_size=None, request_id=None, seller_id=None,
                 template_id=None, uids=None):
        self.from_app = from_app  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.seller_id = seller_id  # type: long
        self.template_id = template_id  # type: long
        self.uids = uids  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCouponPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.uids is not None:
            result['Uids'] = self.uids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Uids') is not None:
            self.uids = m.get('Uids')
        return self


class GetCouponPageResponseBodyDataCurrency(TeaModel):
    def __init__(self, currency_code=None):
        self.currency_code = currency_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCouponPageResponseBodyDataCurrency, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')
        return self


class GetCouponPageResponseBodyData(TeaModel):
    def __init__(self, amount=None, certain_money=None, coupon_id=None, coupon_type=None, currency=None,
                 description=None, discount_rate=None, end_time=None, frozen_amount=None, frozen_count=None, promotion_id=None,
                 seller_id=None, start_time=None, status=None, template_id=None, universal_type=None, upper_limit=None,
                 usage_count=None, used_amount=None, used_count=None, user_id=None):
        self.amount = amount  # type: float
        self.certain_money = certain_money  # type: float
        self.coupon_id = coupon_id  # type: long
        self.coupon_type = coupon_type  # type: str
        self.currency = currency  # type: GetCouponPageResponseBodyDataCurrency
        self.description = description  # type: str
        self.discount_rate = discount_rate  # type: float
        self.end_time = end_time  # type: str
        self.frozen_amount = frozen_amount  # type: float
        self.frozen_count = frozen_count  # type: int
        self.promotion_id = promotion_id  # type: long
        self.seller_id = seller_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.template_id = template_id  # type: long
        self.universal_type = universal_type  # type: str
        self.upper_limit = upper_limit  # type: float
        self.usage_count = usage_count  # type: int
        self.used_amount = used_amount  # type: float
        self.used_count = used_count  # type: int
        self.user_id = user_id  # type: long

    def validate(self):
        if self.currency:
            self.currency.validate()

    def to_map(self):
        _map = super(GetCouponPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.certain_money is not None:
            result['CertainMoney'] = self.certain_money
        if self.coupon_id is not None:
            result['CouponId'] = self.coupon_id
        if self.coupon_type is not None:
            result['CouponType'] = self.coupon_type
        if self.currency is not None:
            result['Currency'] = self.currency.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.discount_rate is not None:
            result['DiscountRate'] = self.discount_rate
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.frozen_amount is not None:
            result['FrozenAmount'] = self.frozen_amount
        if self.frozen_count is not None:
            result['FrozenCount'] = self.frozen_count
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.universal_type is not None:
            result['UniversalType'] = self.universal_type
        if self.upper_limit is not None:
            result['UpperLimit'] = self.upper_limit
        if self.usage_count is not None:
            result['UsageCount'] = self.usage_count
        if self.used_amount is not None:
            result['UsedAmount'] = self.used_amount
        if self.used_count is not None:
            result['UsedCount'] = self.used_count
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('CertainMoney') is not None:
            self.certain_money = m.get('CertainMoney')
        if m.get('CouponId') is not None:
            self.coupon_id = m.get('CouponId')
        if m.get('CouponType') is not None:
            self.coupon_type = m.get('CouponType')
        if m.get('Currency') is not None:
            temp_model = GetCouponPageResponseBodyDataCurrency()
            self.currency = temp_model.from_map(m['Currency'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiscountRate') is not None:
            self.discount_rate = m.get('DiscountRate')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FrozenAmount') is not None:
            self.frozen_amount = m.get('FrozenAmount')
        if m.get('FrozenCount') is not None:
            self.frozen_count = m.get('FrozenCount')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('UniversalType') is not None:
            self.universal_type = m.get('UniversalType')
        if m.get('UpperLimit') is not None:
            self.upper_limit = m.get('UpperLimit')
        if m.get('UsageCount') is not None:
            self.usage_count = m.get('UsageCount')
        if m.get('UsedAmount') is not None:
            self.used_amount = m.get('UsedAmount')
        if m.get('UsedCount') is not None:
            self.used_count = m.get('UsedCount')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetCouponPageResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, count=None, data=None, message=None, request_id=None,
                 success=None, total_count=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.count = count  # type: int
        self.data = data  # type: list[GetCouponPageResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCouponPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
        if self.count is not None:
            result['Count'] = self.count
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetCouponPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetCouponPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCouponPageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCouponPageResponse, self).to_map()
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
            temp_model = GetCouponPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomerListRequest(TeaModel):
    def __init__(self, page_no=None, page_size=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomerListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetCustomerListResponseBodyData(TeaModel):
    def __init__(self, total_size=None, uid_list=None):
        self.total_size = total_size  # type: int
        self.uid_list = uid_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCustomerListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        if self.uid_list is not None:
            result['UidList'] = self.uid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
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
        _map = super(GetCustomerListResponseBody, self).to_map()
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCustomerListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCustomerListResponse, self).to_map()
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
            temp_model = GetCustomerListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRelationRequest(TeaModel):
    def __init__(self, relation_time=None, uid=None):
        self.relation_time = relation_time  # type: long
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_time is not None:
            result['RelationTime'] = self.relation_time
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelationTime') is not None:
            self.relation_time = m.get('RelationTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetRelationResponseBodyDataResellerProductModeDO(TeaModel):
    def __init__(self, class_=None, is_service=None, product_code=None, product_name=None):
        self.class_ = class_  # type: str
        self.is_service = is_service  # type: long
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRelationResponseBodyDataResellerProductModeDO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.is_service is not None:
            result['IsService'] = self.is_service
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('IsService') is not None:
            self.is_service = m.get('IsService')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class GetRelationResponseBodyDataResellerProductRuleDO(TeaModel):
    def __init__(self, class_=None, commodity_route=None, multi_order=None, pay_mode=None):
        self.class_ = class_  # type: str
        self.commodity_route = commodity_route  # type: bool
        self.multi_order = multi_order  # type: bool
        self.pay_mode = pay_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRelationResponseBodyDataResellerProductRuleDO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.commodity_route is not None:
            result['CommodityRoute'] = self.commodity_route
        if self.multi_order is not None:
            result['MultiOrder'] = self.multi_order
        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('CommodityRoute') is not None:
            self.commodity_route = m.get('CommodityRoute')
        if m.get('MultiOrder') is not None:
            self.multi_order = m.get('MultiOrder')
        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')
        return self


class GetRelationResponseBodyData(TeaModel):
    def __init__(self, can_login_official=None, class_=None, end_time=None, reseller_product_mode_do=None,
                 reseller_product_rule_do=None, reseller_uid=None, start_time=None, status=None, top_reseller=None, uid=None, user_type=None):
        self.can_login_official = can_login_official  # type: bool
        self.class_ = class_  # type: str
        self.end_time = end_time  # type: long
        self.reseller_product_mode_do = reseller_product_mode_do  # type: GetRelationResponseBodyDataResellerProductModeDO
        self.reseller_product_rule_do = reseller_product_rule_do  # type: GetRelationResponseBodyDataResellerProductRuleDO
        self.reseller_uid = reseller_uid  # type: long
        self.start_time = start_time  # type: long
        self.status = status  # type: str
        self.top_reseller = top_reseller  # type: bool
        self.uid = uid  # type: long
        self.user_type = user_type  # type: str

    def validate(self):
        if self.reseller_product_mode_do:
            self.reseller_product_mode_do.validate()
        if self.reseller_product_rule_do:
            self.reseller_product_rule_do.validate()

    def to_map(self):
        _map = super(GetRelationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_login_official is not None:
            result['CanLoginOfficial'] = self.can_login_official
        if self.class_ is not None:
            result['Class'] = self.class_
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.reseller_product_mode_do is not None:
            result['ResellerProductModeDO'] = self.reseller_product_mode_do.to_map()
        if self.reseller_product_rule_do is not None:
            result['ResellerProductRuleDO'] = self.reseller_product_rule_do.to_map()
        if self.reseller_uid is not None:
            result['ResellerUid'] = self.reseller_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.top_reseller is not None:
            result['TopReseller'] = self.top_reseller
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanLoginOfficial') is not None:
            self.can_login_official = m.get('CanLoginOfficial')
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ResellerProductModeDO') is not None:
            temp_model = GetRelationResponseBodyDataResellerProductModeDO()
            self.reseller_product_mode_do = temp_model.from_map(m['ResellerProductModeDO'])
        if m.get('ResellerProductRuleDO') is not None:
            temp_model = GetRelationResponseBodyDataResellerProductRuleDO()
            self.reseller_product_rule_do = temp_model.from_map(m['ResellerProductRuleDO'])
        if m.get('ResellerUid') is not None:
            self.reseller_uid = m.get('ResellerUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TopReseller') is not None:
            self.top_reseller = m.get('TopReseller')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class GetRelationResponseBody(TeaModel):
    def __init__(self, class_=None, code=None, data=None, message=None, request_id=None, success=None):
        self.class_ = class_  # type: str
        self.code = code  # type: str
        self.data = data  # type: GetRelationResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.class_ is not None:
            result['Class'] = self.class_
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
        if m.get('Class') is not None:
            self.class_ = m.get('Class')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRelationResponse, self).to_map()
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
            temp_model = GetRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResellerPayOrderRequest(TeaModel):
    def __init__(self, order_id=None, uid=None):
        self.order_id = order_id  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResellerPayOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class GetResellerPayOrderResponseBodyData(TeaModel):
    def __init__(self, buyer_id=None, order_id=None, order_status=None, pay_amount=None):
        self.buyer_id = buyer_id  # type: str
        self.order_id = order_id  # type: str
        self.order_status = order_status  # type: str
        self.pay_amount = pay_amount  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResellerPayOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.pay_amount is not None:
            result['PayAmount'] = self.pay_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PayAmount') is not None:
            self.pay_amount = m.get('PayAmount')
        return self


class GetResellerPayOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetResellerPayOrderResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResellerPayOrderResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetResellerPayOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetResellerPayOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResellerPayOrderResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResellerPayOrderResponse, self).to_map()
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
            temp_model = GetResellerPayOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LabelPartnerUserRequest(TeaModel):
    def __init__(self, user_pk=None, user_tag=None):
        self.user_pk = user_pk  # type: long
        self.user_tag = user_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LabelPartnerUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_pk is not None:
            result['UserPK'] = self.user_pk
        if self.user_tag is not None:
            result['UserTag'] = self.user_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPK') is not None:
            self.user_pk = m.get('UserPK')
        if m.get('UserTag') is not None:
            self.user_tag = m.get('UserTag')
        return self


class LabelPartnerUserResponseBodyData(TeaModel):
    def __init__(self, user_pk=None, user_tag=None):
        self.user_pk = user_pk  # type: long
        self.user_tag = user_tag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LabelPartnerUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_pk is not None:
            result['UserPK'] = self.user_pk
        if self.user_tag is not None:
            result['UserTag'] = self.user_tag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserPK') is not None:
            self.user_pk = m.get('UserPK')
        if m.get('UserTag') is not None:
            self.user_tag = m.get('UserTag')
        return self


class LabelPartnerUserResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: LabelPartnerUserResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(LabelPartnerUserResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = LabelPartnerUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LabelPartnerUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LabelPartnerUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LabelPartnerUserResponse, self).to_map()
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
            temp_model = LabelPartnerUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateResourceRequest(TeaModel):
    def __init__(self, action_code=None, content=None):
        self.action_code = action_code  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class MigrateResourceResponseBodyData(TeaModel):
    def __init__(self, content=None, proc_envir=None):
        self.content = content  # type: str
        self.proc_envir = proc_envir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.proc_envir is not None:
            result['ProcEnvir'] = self.proc_envir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProcEnvir') is not None:
            self.proc_envir = m.get('ProcEnvir')
        return self


class MigrateResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: MigrateResourceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MigrateResourceResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = MigrateResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MigrateResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MigrateResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MigrateResourceResponse, self).to_map()
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
            temp_model = MigrateResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OfflineActivityRequest(TeaModel):
    def __init__(self, activity_list=None, biz_id=None, token=None):
        self.activity_list = activity_list  # type: list[long]
        self.biz_id = biz_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineActivityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_list is not None:
            result['ActivityList'] = self.activity_list
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityList') is not None:
            self.activity_list = m.get('ActivityList')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class OfflineActivityResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.data = data  # type: list[long]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OfflineActivityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OfflineActivityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OfflineActivityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OfflineActivityResponse, self).to_map()
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
            temp_model = OfflineActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PayResultCallbackRequest(TeaModel):
    def __init__(self, order_id=None, pay_status=None, pay_time=None, uid=None):
        self.order_id = order_id  # type: str
        self.pay_status = pay_status  # type: str
        self.pay_time = pay_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PayResultCallbackRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.pay_status is not None:
            result['PayStatus'] = self.pay_status
        if self.pay_time is not None:
            result['PayTime'] = self.pay_time
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PayStatus') is not None:
            self.pay_status = m.get('PayStatus')
        if m.get('PayTime') is not None:
            self.pay_time = m.get('PayTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class PayResultCallbackResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PayResultCallbackResponseBody, self).to_map()
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


class PayResultCallbackResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PayResultCallbackResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PayResultCallbackResponse, self).to_map()
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
            temp_model = PayResultCallbackResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublicActivityRequest(TeaModel):
    def __init__(self, activity_list=None, biz_id=None, snap_type=None, token=None):
        self.activity_list = activity_list  # type: list[long]
        self.biz_id = biz_id  # type: str
        self.snap_type = snap_type  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublicActivityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_list is not None:
            result['ActivityList'] = self.activity_list
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.snap_type is not None:
            result['SnapType'] = self.snap_type
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityList') is not None:
            self.activity_list = m.get('ActivityList')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SnapType') is not None:
            self.snap_type = m.get('SnapType')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class PublicActivityResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.data = data  # type: list[long]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(PublicActivityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublicActivityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PublicActivityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PublicActivityResponse, self).to_map()
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
            temp_model = PublicActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryActivityRequest(TeaModel):
    def __init__(self, activity_id=None, biz_id=None, snap_type=None):
        self.activity_id = activity_id  # type: long
        self.biz_id = biz_id  # type: str
        self.snap_type = snap_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryActivityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.snap_type is not None:
            result['SnapType'] = self.snap_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('SnapType') is not None:
            self.snap_type = m.get('SnapType')
        return self


class QueryActivityResponseBodyData(TeaModel):
    def __init__(self, activity_id=None, activity_name=None, black_list=None, commodity_code_list=None,
                 description=None, end_time=None, ext_map=None, promotion_description=None, promotion_value=None,
                 region_list=None, seller_id_list=None, start_time=None, status=None, test_account_list=None, white_list=None):
        self.activity_id = activity_id  # type: long
        self.activity_name = activity_name  # type: str
        self.black_list = black_list  # type: list[long]
        self.commodity_code_list = commodity_code_list  # type: list[str]
        self.description = description  # type: str
        self.end_time = end_time  # type: str
        self.ext_map = ext_map  # type: dict[str, str]
        self.promotion_description = promotion_description  # type: str
        self.promotion_value = promotion_value  # type: float
        self.region_list = region_list  # type: list[str]
        self.seller_id_list = seller_id_list  # type: list[long]
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.test_account_list = test_account_list  # type: list[long]
        self.white_list = white_list  # type: list[long]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryActivityResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.black_list is not None:
            result['BlackList'] = self.black_list
        if self.commodity_code_list is not None:
            result['CommodityCodeList'] = self.commodity_code_list
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.ext_map is not None:
            result['ExtMap'] = self.ext_map
        if self.promotion_description is not None:
            result['PromotionDescription'] = self.promotion_description
        if self.promotion_value is not None:
            result['PromotionValue'] = self.promotion_value
        if self.region_list is not None:
            result['RegionList'] = self.region_list
        if self.seller_id_list is not None:
            result['SellerIdList'] = self.seller_id_list
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.test_account_list is not None:
            result['TestAccountList'] = self.test_account_list
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('BlackList') is not None:
            self.black_list = m.get('BlackList')
        if m.get('CommodityCodeList') is not None:
            self.commodity_code_list = m.get('CommodityCodeList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtMap') is not None:
            self.ext_map = m.get('ExtMap')
        if m.get('PromotionDescription') is not None:
            self.promotion_description = m.get('PromotionDescription')
        if m.get('PromotionValue') is not None:
            self.promotion_value = m.get('PromotionValue')
        if m.get('RegionList') is not None:
            self.region_list = m.get('RegionList')
        if m.get('SellerIdList') is not None:
            self.seller_id_list = m.get('SellerIdList')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TestAccountList') is not None:
            self.test_account_list = m.get('TestAccountList')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class QueryActivityResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.data = data  # type: QueryActivityResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryActivityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            temp_model = QueryActivityResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryActivityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryActivityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryActivityResponse, self).to_map()
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
            temp_model = QueryActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEcoRelationRequest(TeaModel):
    def __init__(self, relation_time=None, uid=None):
        self.relation_time = relation_time  # type: str
        self.uid = uid  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEcoRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relation_time is not None:
            result['RelationTime'] = self.relation_time
        if self.uid is not None:
            result['Uid'] = self.uid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelationTime') is not None:
            self.relation_time = m.get('RelationTime')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        return self


class QueryEcoRelationResponseBodyDataResellerProductModeDO(TeaModel):
    def __init__(self, is_service=None, product_code=None, product_name=None):
        self.is_service = is_service  # type: int
        self.product_code = product_code  # type: str
        self.product_name = product_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEcoRelationResponseBodyDataResellerProductModeDO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_service is not None:
            result['IsService'] = self.is_service
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsService') is not None:
            self.is_service = m.get('IsService')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class QueryEcoRelationResponseBodyDataResellerProductRuleDO(TeaModel):
    def __init__(self, commodity_route=None, multi_order=None, pay_mode=None):
        self.commodity_route = commodity_route  # type: bool
        self.multi_order = multi_order  # type: bool
        self.pay_mode = pay_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEcoRelationResponseBodyDataResellerProductRuleDO, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_route is not None:
            result['CommodityRoute'] = self.commodity_route
        if self.multi_order is not None:
            result['MultiOrder'] = self.multi_order
        if self.pay_mode is not None:
            result['PayMode'] = self.pay_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityRoute') is not None:
            self.commodity_route = m.get('CommodityRoute')
        if m.get('MultiOrder') is not None:
            self.multi_order = m.get('MultiOrder')
        if m.get('PayMode') is not None:
            self.pay_mode = m.get('PayMode')
        return self


class QueryEcoRelationResponseBodyData(TeaModel):
    def __init__(self, can_login_official=None, end_time=None, is_top_reseller=None, reseller_product_mode_do=None,
                 reseller_product_rule_do=None, reseller_uid=None, start_time=None, status=None, uid=None, user_type=None):
        self.can_login_official = can_login_official  # type: bool
        self.end_time = end_time  # type: str
        self.is_top_reseller = is_top_reseller  # type: bool
        self.reseller_product_mode_do = reseller_product_mode_do  # type: QueryEcoRelationResponseBodyDataResellerProductModeDO
        self.reseller_product_rule_do = reseller_product_rule_do  # type: QueryEcoRelationResponseBodyDataResellerProductRuleDO
        self.reseller_uid = reseller_uid  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.uid = uid  # type: long
        self.user_type = user_type  # type: str

    def validate(self):
        if self.reseller_product_mode_do:
            self.reseller_product_mode_do.validate()
        if self.reseller_product_rule_do:
            self.reseller_product_rule_do.validate()

    def to_map(self):
        _map = super(QueryEcoRelationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_login_official is not None:
            result['CanLoginOfficial'] = self.can_login_official
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.is_top_reseller is not None:
            result['IsTopReseller'] = self.is_top_reseller
        if self.reseller_product_mode_do is not None:
            result['ResellerProductModeDO'] = self.reseller_product_mode_do.to_map()
        if self.reseller_product_rule_do is not None:
            result['ResellerProductRuleDO'] = self.reseller_product_rule_do.to_map()
        if self.reseller_uid is not None:
            result['ResellerUid'] = self.reseller_uid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CanLoginOfficial') is not None:
            self.can_login_official = m.get('CanLoginOfficial')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IsTopReseller') is not None:
            self.is_top_reseller = m.get('IsTopReseller')
        if m.get('ResellerProductModeDO') is not None:
            temp_model = QueryEcoRelationResponseBodyDataResellerProductModeDO()
            self.reseller_product_mode_do = temp_model.from_map(m['ResellerProductModeDO'])
        if m.get('ResellerProductRuleDO') is not None:
            temp_model = QueryEcoRelationResponseBodyDataResellerProductRuleDO()
            self.reseller_product_rule_do = temp_model.from_map(m['ResellerProductRuleDO'])
        if m.get('ResellerUid') is not None:
            self.reseller_uid = m.get('ResellerUid')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class QueryEcoRelationResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.data = data  # type: QueryEcoRelationResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryEcoRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            temp_model = QueryEcoRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEcoRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEcoRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEcoRelationResponse, self).to_map()
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
            temp_model = QueryEcoRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveActivityRequestFusionPromotionParamListModuleInfoParamList(TeaModel):
    def __init__(self, component_code=None, item_code=None, module_id=None, module_key=None, module_name=None,
                 module_value_list=None, price_plan_id=None):
        self.component_code = component_code  # type: str
        self.item_code = item_code  # type: str
        self.module_id = module_id  # type: long
        self.module_key = module_key  # type: str
        self.module_name = module_name  # type: str
        self.module_value_list = module_value_list  # type: list[str]
        self.price_plan_id = price_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveActivityRequestFusionPromotionParamListModuleInfoParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['componentCode'] = self.component_code
        if self.item_code is not None:
            result['itemCode'] = self.item_code
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_key is not None:
            result['moduleKey'] = self.module_key
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_value_list is not None:
            result['moduleValueList'] = self.module_value_list
        if self.price_plan_id is not None:
            result['pricePlanId'] = self.price_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentCode') is not None:
            self.component_code = m.get('componentCode')
        if m.get('itemCode') is not None:
            self.item_code = m.get('itemCode')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleKey') is not None:
            self.module_key = m.get('moduleKey')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleValueList') is not None:
            self.module_value_list = m.get('moduleValueList')
        if m.get('pricePlanId') is not None:
            self.price_plan_id = m.get('pricePlanId')
        return self


class SaveActivityRequestFusionPromotionParamList(TeaModel):
    def __init__(self, commodity_code_list=None, promotion_value=None, restricted_region_list=None,
                 module_info_param_list=None):
        self.commodity_code_list = commodity_code_list  # type: list[str]
        self.promotion_value = promotion_value  # type: float
        self.restricted_region_list = restricted_region_list  # type: list[str]
        self.module_info_param_list = module_info_param_list  # type: list[SaveActivityRequestFusionPromotionParamListModuleInfoParamList]

    def validate(self):
        if self.module_info_param_list:
            for k in self.module_info_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveActivityRequestFusionPromotionParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code_list is not None:
            result['CommodityCodeList'] = self.commodity_code_list
        if self.promotion_value is not None:
            result['PromotionValue'] = self.promotion_value
        if self.restricted_region_list is not None:
            result['RestrictedRegionList'] = self.restricted_region_list
        result['moduleInfoParamList'] = []
        if self.module_info_param_list is not None:
            for k in self.module_info_param_list:
                result['moduleInfoParamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCodeList') is not None:
            self.commodity_code_list = m.get('CommodityCodeList')
        if m.get('PromotionValue') is not None:
            self.promotion_value = m.get('PromotionValue')
        if m.get('RestrictedRegionList') is not None:
            self.restricted_region_list = m.get('RestrictedRegionList')
        self.module_info_param_list = []
        if m.get('moduleInfoParamList') is not None:
            for k in m.get('moduleInfoParamList'):
                temp_model = SaveActivityRequestFusionPromotionParamListModuleInfoParamList()
                self.module_info_param_list.append(temp_model.from_map(k))
        return self


class SaveActivityRequest(TeaModel):
    def __init__(self, activity_name=None, biz_id=None, black_uid_list=None, description=None, end_time=None,
                 extend_map=None, fusion_promotion_param_list=None, publish_tag=None, start_time=None,
                 test_account_uid_list=None, token=None, white_uid_list=None):
        self.activity_name = activity_name  # type: str
        self.biz_id = biz_id  # type: str
        self.black_uid_list = black_uid_list  # type: list[long]
        self.description = description  # type: str
        self.end_time = end_time  # type: str
        self.extend_map = extend_map  # type: dict[str, any]
        self.fusion_promotion_param_list = fusion_promotion_param_list  # type: list[SaveActivityRequestFusionPromotionParamList]
        self.publish_tag = publish_tag  # type: str
        self.start_time = start_time  # type: str
        self.test_account_uid_list = test_account_uid_list  # type: list[long]
        self.token = token  # type: str
        self.white_uid_list = white_uid_list  # type: list[long]

    def validate(self):
        if self.fusion_promotion_param_list:
            for k in self.fusion_promotion_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveActivityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.black_uid_list is not None:
            result['BlackUidList'] = self.black_uid_list
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extend_map is not None:
            result['ExtendMap'] = self.extend_map
        result['FusionPromotionParamList'] = []
        if self.fusion_promotion_param_list is not None:
            for k in self.fusion_promotion_param_list:
                result['FusionPromotionParamList'].append(k.to_map() if k else None)
        if self.publish_tag is not None:
            result['PublishTag'] = self.publish_tag
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.test_account_uid_list is not None:
            result['TestAccountUidList'] = self.test_account_uid_list
        if self.token is not None:
            result['Token'] = self.token
        if self.white_uid_list is not None:
            result['WhiteUidList'] = self.white_uid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BlackUidList') is not None:
            self.black_uid_list = m.get('BlackUidList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendMap') is not None:
            self.extend_map = m.get('ExtendMap')
        self.fusion_promotion_param_list = []
        if m.get('FusionPromotionParamList') is not None:
            for k in m.get('FusionPromotionParamList'):
                temp_model = SaveActivityRequestFusionPromotionParamList()
                self.fusion_promotion_param_list.append(temp_model.from_map(k))
        if m.get('PublishTag') is not None:
            self.publish_tag = m.get('PublishTag')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TestAccountUidList') is not None:
            self.test_account_uid_list = m.get('TestAccountUidList')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('WhiteUidList') is not None:
            self.white_uid_list = m.get('WhiteUidList')
        return self


class SaveActivityShrinkRequestFusionPromotionParamListModuleInfoParamList(TeaModel):
    def __init__(self, component_code=None, item_code=None, module_id=None, module_key=None, module_name=None,
                 module_value_list=None, price_plan_id=None):
        self.component_code = component_code  # type: str
        self.item_code = item_code  # type: str
        self.module_id = module_id  # type: long
        self.module_key = module_key  # type: str
        self.module_name = module_name  # type: str
        self.module_value_list = module_value_list  # type: list[str]
        self.price_plan_id = price_plan_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveActivityShrinkRequestFusionPromotionParamListModuleInfoParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['componentCode'] = self.component_code
        if self.item_code is not None:
            result['itemCode'] = self.item_code
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_key is not None:
            result['moduleKey'] = self.module_key
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_value_list is not None:
            result['moduleValueList'] = self.module_value_list
        if self.price_plan_id is not None:
            result['pricePlanId'] = self.price_plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('componentCode') is not None:
            self.component_code = m.get('componentCode')
        if m.get('itemCode') is not None:
            self.item_code = m.get('itemCode')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleKey') is not None:
            self.module_key = m.get('moduleKey')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleValueList') is not None:
            self.module_value_list = m.get('moduleValueList')
        if m.get('pricePlanId') is not None:
            self.price_plan_id = m.get('pricePlanId')
        return self


class SaveActivityShrinkRequestFusionPromotionParamList(TeaModel):
    def __init__(self, commodity_code_list=None, promotion_value=None, restricted_region_list=None,
                 module_info_param_list=None):
        self.commodity_code_list = commodity_code_list  # type: list[str]
        self.promotion_value = promotion_value  # type: float
        self.restricted_region_list = restricted_region_list  # type: list[str]
        self.module_info_param_list = module_info_param_list  # type: list[SaveActivityShrinkRequestFusionPromotionParamListModuleInfoParamList]

    def validate(self):
        if self.module_info_param_list:
            for k in self.module_info_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveActivityShrinkRequestFusionPromotionParamList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code_list is not None:
            result['CommodityCodeList'] = self.commodity_code_list
        if self.promotion_value is not None:
            result['PromotionValue'] = self.promotion_value
        if self.restricted_region_list is not None:
            result['RestrictedRegionList'] = self.restricted_region_list
        result['moduleInfoParamList'] = []
        if self.module_info_param_list is not None:
            for k in self.module_info_param_list:
                result['moduleInfoParamList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommodityCodeList') is not None:
            self.commodity_code_list = m.get('CommodityCodeList')
        if m.get('PromotionValue') is not None:
            self.promotion_value = m.get('PromotionValue')
        if m.get('RestrictedRegionList') is not None:
            self.restricted_region_list = m.get('RestrictedRegionList')
        self.module_info_param_list = []
        if m.get('moduleInfoParamList') is not None:
            for k in m.get('moduleInfoParamList'):
                temp_model = SaveActivityShrinkRequestFusionPromotionParamListModuleInfoParamList()
                self.module_info_param_list.append(temp_model.from_map(k))
        return self


class SaveActivityShrinkRequest(TeaModel):
    def __init__(self, activity_name=None, biz_id=None, black_uid_list=None, description=None, end_time=None,
                 extend_map_shrink=None, fusion_promotion_param_list=None, publish_tag=None, start_time=None,
                 test_account_uid_list=None, token=None, white_uid_list=None):
        self.activity_name = activity_name  # type: str
        self.biz_id = biz_id  # type: str
        self.black_uid_list = black_uid_list  # type: list[long]
        self.description = description  # type: str
        self.end_time = end_time  # type: str
        self.extend_map_shrink = extend_map_shrink  # type: str
        self.fusion_promotion_param_list = fusion_promotion_param_list  # type: list[SaveActivityShrinkRequestFusionPromotionParamList]
        self.publish_tag = publish_tag  # type: str
        self.start_time = start_time  # type: str
        self.test_account_uid_list = test_account_uid_list  # type: list[long]
        self.token = token  # type: str
        self.white_uid_list = white_uid_list  # type: list[long]

    def validate(self):
        if self.fusion_promotion_param_list:
            for k in self.fusion_promotion_param_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveActivityShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.black_uid_list is not None:
            result['BlackUidList'] = self.black_uid_list
        if self.description is not None:
            result['Description'] = self.description
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.extend_map_shrink is not None:
            result['ExtendMap'] = self.extend_map_shrink
        result['FusionPromotionParamList'] = []
        if self.fusion_promotion_param_list is not None:
            for k in self.fusion_promotion_param_list:
                result['FusionPromotionParamList'].append(k.to_map() if k else None)
        if self.publish_tag is not None:
            result['PublishTag'] = self.publish_tag
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.test_account_uid_list is not None:
            result['TestAccountUidList'] = self.test_account_uid_list
        if self.token is not None:
            result['Token'] = self.token
        if self.white_uid_list is not None:
            result['WhiteUidList'] = self.white_uid_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BlackUidList') is not None:
            self.black_uid_list = m.get('BlackUidList')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExtendMap') is not None:
            self.extend_map_shrink = m.get('ExtendMap')
        self.fusion_promotion_param_list = []
        if m.get('FusionPromotionParamList') is not None:
            for k in m.get('FusionPromotionParamList'):
                temp_model = SaveActivityShrinkRequestFusionPromotionParamList()
                self.fusion_promotion_param_list.append(temp_model.from_map(k))
        if m.get('PublishTag') is not None:
            self.publish_tag = m.get('PublishTag')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TestAccountUidList') is not None:
            self.test_account_uid_list = m.get('TestAccountUidList')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('WhiteUidList') is not None:
            self.white_uid_list = m.get('WhiteUidList')
        return self


class SaveActivityResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.data = data  # type: list[long]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveActivityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
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
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveActivityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveActivityResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveActivityResponse, self).to_map()
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
            temp_model = SaveActivityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCouponRequestUserAmountModelList(TeaModel):
    def __init__(self, amount=None, uid=None, user_id=None, youhui_id=None):
        self.amount = amount  # type: float
        self.uid = uid  # type: long
        self.user_id = user_id  # type: long
        self.youhui_id = youhui_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCouponRequestUserAmountModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.youhui_id is not None:
            result['YouhuiId'] = self.youhui_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('YouhuiId') is not None:
            self.youhui_id = m.get('YouhuiId')
        return self


class SendCouponRequest(TeaModel):
    def __init__(self, bid=None, from_app=None, operator=None, request_id=None, seller_id=None, template_id=None,
                 user_amount_model_list=None):
        self.bid = bid  # type: long
        self.from_app = from_app  # type: str
        self.operator = operator  # type: str
        self.request_id = request_id  # type: str
        self.seller_id = seller_id  # type: long
        self.template_id = template_id  # type: long
        self.user_amount_model_list = user_amount_model_list  # type: list[SendCouponRequestUserAmountModelList]

    def validate(self):
        if self.user_amount_model_list:
            for k in self.user_amount_model_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendCouponRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.from_app is not None:
            result['FromApp'] = self.from_app
        if self.operator is not None:
            result['Operator'] = self.operator
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.seller_id is not None:
            result['SellerId'] = self.seller_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['UserAmountModelList'] = []
        if self.user_amount_model_list is not None:
            for k in self.user_amount_model_list:
                result['UserAmountModelList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('FromApp') is not None:
            self.from_app = m.get('FromApp')
        if m.get('Operator') is not None:
            self.operator = m.get('Operator')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SellerId') is not None:
            self.seller_id = m.get('SellerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.user_amount_model_list = []
        if m.get('UserAmountModelList') is not None:
            for k in m.get('UserAmountModelList'):
                temp_model = SendCouponRequestUserAmountModelList()
                self.user_amount_model_list.append(temp_model.from_map(k))
        return self


class SendCouponResponseBodyData(TeaModel):
    def __init__(self, amount=None, uid=None, user_id=None, youhui_id=None):
        self.amount = amount  # type: float
        self.uid = uid  # type: long
        self.user_id = user_id  # type: long
        self.youhui_id = youhui_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCouponResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.uid is not None:
            result['Uid'] = self.uid
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.youhui_id is not None:
            result['YouhuiId'] = self.youhui_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('YouhuiId') is not None:
            self.youhui_id = m.get('YouhuiId')
        return self


class SendCouponResponseBody(TeaModel):
    def __init__(self, code=None, context_map=None, count=None, data=None, message=None, request_id=None,
                 success=None, total_count=None):
        self.code = code  # type: str
        self.context_map = context_map  # type: dict[str, any]
        self.count = count  # type: int
        self.data = data  # type: list[SendCouponResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SendCouponResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.context_map is not None:
            result['ContextMap'] = self.context_map
        if self.count is not None:
            result['Count'] = self.count
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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ContextMap') is not None:
            self.context_map = m.get('ContextMap')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SendCouponResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class SendCouponResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCouponResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCouponResponse, self).to_map()
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
            temp_model = SendCouponResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferResourceRequest(TeaModel):
    def __init__(self, action_code=None, content=None):
        self.action_code = action_code  # type: str
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class TransferResourceResponseBodyData(TeaModel):
    def __init__(self, content=None, proc_env=None):
        self.content = content  # type: str
        self.proc_env = proc_env  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferResourceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.proc_env is not None:
            result['ProcEnv'] = self.proc_env
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ProcEnv') is not None:
            self.proc_env = m.get('ProcEnv')
        return self


class TransferResourceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: TransferResourceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TransferResourceResponseBody, self).to_map()
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
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = TransferResourceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferResourceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferResourceResponse, self).to_map()
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
            temp_model = TransferResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


