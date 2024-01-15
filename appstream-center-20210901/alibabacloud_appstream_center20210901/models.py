# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AccessPageGetAclRequest(TeaModel):
    def __init__(self, access_page_id=None):
        self.access_page_id = access_page_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccessPageGetAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        return self


class AccessPageGetAclResponseBodyData(TeaModel):
    def __init__(self, access_mode=None, access_url=None, effect_time=None, unit=None, url_expire_time=None):
        self.access_mode = access_mode  # type: str
        self.access_url = access_url  # type: str
        self.effect_time = effect_time  # type: int
        self.unit = unit  # type: str
        self.url_expire_time = url_expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccessPageGetAclResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')
        return self


class AccessPageGetAclResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[AccessPageGetAclResponseBodyData]
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AccessPageGetAclResponseBody, self).to_map()
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
                temp_model = AccessPageGetAclResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AccessPageGetAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AccessPageGetAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AccessPageGetAclResponse, self).to_map()
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
            temp_model = AccessPageGetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AccessPageSetAclRequest(TeaModel):
    def __init__(self, access_mode=None, access_page_id=None, access_page_name=None, effect_time=None, unit=None):
        self.access_mode = access_mode  # type: str
        self.access_page_id = access_page_id  # type: str
        self.access_page_name = access_page_name  # type: str
        self.effect_time = effect_time  # type: int
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccessPageSetAclRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class AccessPageSetAclResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccessPageSetAclResponseBody, self).to_map()
        if _map is not None:
            return _map

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


class AccessPageSetAclResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AccessPageSetAclResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AccessPageSetAclResponse, self).to_map()
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
            temp_model = AccessPageSetAclResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApproveOtaTaskRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, biz_region_id=None, ota_type=None, start_time=None, task_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.ota_type = ota_type  # type: str
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveOtaTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ApproveOtaTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApproveOtaTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveOtaTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApproveOtaTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApproveOtaTaskResponse, self).to_map()
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
            temp_model = ApproveOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AskSessionPackagePriceRequest(TeaModel):
    def __init__(self, charge_type=None, max_sessions=None, period=None, period_unit=None, region=None,
                 session_package_type=None, session_spec=None, session_type=None):
        self.charge_type = charge_type  # type: str
        self.max_sessions = max_sessions  # type: int
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.region = region  # type: str
        self.session_package_type = session_package_type  # type: str
        self.session_spec = session_spec  # type: str
        self.session_type = session_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AskSessionPackagePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region is not None:
            result['Region'] = self.region
        if self.session_package_type is not None:
            result['SessionPackageType'] = self.session_package_type
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionPackageType') is not None:
            self.session_package_type = m.get('SessionPackageType')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        return self


class AskSessionPackagePriceResponseBodyDataPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AskSessionPackagePriceResponseBodyDataPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
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
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class AskSessionPackagePriceResponseBodyData(TeaModel):
    def __init__(self, price=None):
        self.price = price  # type: AskSessionPackagePriceResponseBodyDataPrice

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super(AskSessionPackagePriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = AskSessionPackagePriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class AskSessionPackagePriceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[AskSessionPackagePriceResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AskSessionPackagePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AskSessionPackagePriceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AskSessionPackagePriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AskSessionPackagePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AskSessionPackagePriceResponse, self).to_map()
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
            temp_model = AskSessionPackagePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AskSessionPackageRenewPriceRequest(TeaModel):
    def __init__(self, period=None, period_unit=None, session_package_id=None):
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.session_package_id = session_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AskSessionPackageRenewPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        return self


class AskSessionPackageRenewPriceResponseBodyDataPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AskSessionPackageRenewPriceResponseBodyDataPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
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
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class AskSessionPackageRenewPriceResponseBodyData(TeaModel):
    def __init__(self, price=None):
        self.price = price  # type: AskSessionPackageRenewPriceResponseBodyDataPrice

    def validate(self):
        if self.price:
            self.price.validate()

    def to_map(self):
        _map = super(AskSessionPackageRenewPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = AskSessionPackageRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        return self


class AskSessionPackageRenewPriceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: list[AskSessionPackageRenewPriceResponseBodyData]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AskSessionPackageRenewPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = AskSessionPackageRenewPriceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AskSessionPackageRenewPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AskSessionPackageRenewPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AskSessionPackageRenewPriceResponse, self).to_map()
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
            temp_model = AskSessionPackageRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthorizeInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, authorize_user_ids=None, product_type=None,
                 un_authorize_user_ids=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.authorize_user_ids = authorize_user_ids  # type: list[str]
        self.product_type = product_type  # type: str
        self.un_authorize_user_ids = un_authorize_user_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.authorize_user_ids is not None:
            result['AuthorizeUserIds'] = self.authorize_user_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.un_authorize_user_ids is not None:
            result['UnAuthorizeUserIds'] = self.un_authorize_user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AuthorizeUserIds') is not None:
            self.authorize_user_ids = m.get('AuthorizeUserIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('UnAuthorizeUserIds') is not None:
            self.un_authorize_user_ids = m.get('UnAuthorizeUserIds')
        return self


class AuthorizeInstanceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AuthorizeInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AuthorizeInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AuthorizeInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AuthorizeInstanceGroupResponse, self).to_map()
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
            temp_model = AuthorizeInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BuySessionPackageRequest(TeaModel):
    def __init__(self, charge_type=None, max_sessions=None, period=None, period_unit=None, project_id=None,
                 region=None, session_package_name=None, session_package_type=None, session_spec=None, session_type=None):
        self.charge_type = charge_type  # type: str
        self.max_sessions = max_sessions  # type: int
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.project_id = project_id  # type: str
        self.region = region  # type: str
        self.session_package_name = session_package_name  # type: str
        self.session_package_type = session_package_type  # type: str
        self.session_spec = session_spec  # type: str
        self.session_type = session_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuySessionPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region is not None:
            result['Region'] = self.region
        if self.session_package_name is not None:
            result['SessionPackageName'] = self.session_package_name
        if self.session_package_type is not None:
            result['SessionPackageType'] = self.session_package_type
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionPackageName') is not None:
            self.session_package_name = m.get('SessionPackageName')
        if m.get('SessionPackageType') is not None:
            self.session_package_type = m.get('SessionPackageType')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        return self


class BuySessionPackageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, session_package_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.session_package_id = session_package_id  # type: long
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BuySessionPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
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
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BuySessionPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BuySessionPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BuySessionPackageResponse, self).to_map()
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
            temp_model = BuySessionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOtaTaskRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, task_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOtaTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelOtaTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOtaTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelOtaTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelOtaTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelOtaTaskResponse, self).to_map()
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
            temp_model = CancelOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessPageRequest(TeaModel):
    def __init__(self, access_page_name=None, cloud_env_id=None, effect_time=None, project_id=None,
                 project_name=None, unit=None):
        self.access_page_name = access_page_name  # type: str
        self.cloud_env_id = cloud_env_id  # type: str
        self.effect_time = effect_time  # type: int
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.unit = unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.cloud_env_id is not None:
            result['CloudEnvId'] = self.cloud_env_id
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.unit is not None:
            result['Unit'] = self.unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('CloudEnvId') is not None:
            self.cloud_env_id = m.get('CloudEnvId')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        return self


class CreateAccessPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessPageResponseBody, self).to_map()
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


class CreateAccessPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessPageResponse, self).to_map()
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
            temp_model = CreateAccessPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppInstanceGroupRequestNetworkDomainRules(TeaModel):
    def __init__(self, domain=None, policy=None):
        self.domain = domain  # type: str
        self.policy = policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNetworkDomainRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class CreateAppInstanceGroupRequestNetworkRoutes(TeaModel):
    def __init__(self, destination=None, mode=None):
        self.destination = destination  # type: str
        self.mode = mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNetworkRoutes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.destination is not None:
            result['Destination'] = self.destination
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Destination') is not None:
            self.destination = m.get('Destination')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class CreateAppInstanceGroupRequestNetwork(TeaModel):
    def __init__(self, domain_rules=None, ip_expire_minutes=None, routes=None, strategy_type=None):
        self.domain_rules = domain_rules  # type: list[CreateAppInstanceGroupRequestNetworkDomainRules]
        self.ip_expire_minutes = ip_expire_minutes  # type: int
        self.routes = routes  # type: list[CreateAppInstanceGroupRequestNetworkRoutes]
        self.strategy_type = strategy_type  # type: str

    def validate(self):
        if self.domain_rules:
            for k in self.domain_rules:
                if k:
                    k.validate()
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k in self.domain_rules:
                result['DomainRules'].append(k.to_map() if k else None)
        if self.ip_expire_minutes is not None:
            result['IpExpireMinutes'] = self.ip_expire_minutes
        result['Routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['Routes'].append(k.to_map() if k else None)
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k in m.get('DomainRules'):
                temp_model = CreateAppInstanceGroupRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k))
        if m.get('IpExpireMinutes') is not None:
            self.ip_expire_minutes = m.get('IpExpireMinutes')
        self.routes = []
        if m.get('Routes') is not None:
            for k in m.get('Routes'):
                temp_model = CreateAppInstanceGroupRequestNetworkRoutes()
                self.routes.append(temp_model.from_map(k))
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(self, amount=None, end_time=None, start_time=None):
        self.amount = amount  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules(TeaModel):
    def __init__(self, recurrence_type=None, recurrence_values=None, timer_periods=None):
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_values = recurrence_values  # type: list[int]
        self.timer_periods = timer_periods  # type: list[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods]

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class CreateAppInstanceGroupRequestNodePool(TeaModel):
    def __init__(self, max_scaling_amount=None, node_amount=None, node_capacity=None, node_instance_type=None,
                 recurrence_schedules=None, scaling_down_after_idle_minutes=None, scaling_step=None, scaling_usage_threshold=None,
                 strategy_disable_date=None, strategy_enable_date=None, strategy_type=None, warm_up=None):
        self.max_scaling_amount = max_scaling_amount  # type: int
        self.node_amount = node_amount  # type: int
        self.node_capacity = node_capacity  # type: int
        self.node_instance_type = node_instance_type  # type: str
        self.recurrence_schedules = recurrence_schedules  # type: list[CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules]
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.strategy_disable_date = strategy_disable_date  # type: str
        self.strategy_enable_date = strategy_enable_date  # type: str
        self.strategy_type = strategy_type  # type: str
        self.warm_up = warm_up  # type: bool

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = CreateAppInstanceGroupRequestNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class CreateAppInstanceGroupRequestRuntimePolicy(TeaModel):
    def __init__(self, debug_mode=None, session_type=None):
        self.debug_mode = debug_mode  # type: str
        # 会话类型。
        self.session_type = session_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestRuntimePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.debug_mode is not None:
            result['DebugMode'] = self.debug_mode
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DebugMode') is not None:
            self.debug_mode = m.get('DebugMode')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        return self


class CreateAppInstanceGroupRequestSecurityPolicy(TeaModel):
    def __init__(self, reset_after_unbind=None, skip_user_auth_check=None):
        self.reset_after_unbind = reset_after_unbind  # type: bool
        self.skip_user_auth_check = skip_user_auth_check  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestSecurityPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reset_after_unbind is not None:
            result['ResetAfterUnbind'] = self.reset_after_unbind
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResetAfterUnbind') is not None:
            self.reset_after_unbind = m.get('ResetAfterUnbind')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        return self


class CreateAppInstanceGroupRequestStoragePolicy(TeaModel):
    def __init__(self, storage_type_list=None):
        self.storage_type_list = storage_type_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestStoragePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')
        return self


class CreateAppInstanceGroupRequestUserInfo(TeaModel):
    def __init__(self, type=None):
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequestUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_name=None, auto_pay=None, auto_renew=None,
                 biz_region_id=None, charge_resource_mode=None, charge_type=None, network=None, node_pool=None, period=None,
                 period_unit=None, pre_open_app_id=None, product_type=None, promotion_id=None, runtime_policy=None,
                 security_policy=None, session_timeout=None, storage_policy=None, user_info=None, users=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.biz_region_id = biz_region_id  # type: str
        self.charge_resource_mode = charge_resource_mode  # type: str
        self.charge_type = charge_type  # type: str
        self.network = network  # type: CreateAppInstanceGroupRequestNetwork
        self.node_pool = node_pool  # type: CreateAppInstanceGroupRequestNodePool
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.pre_open_app_id = pre_open_app_id  # type: str
        self.product_type = product_type  # type: str
        self.promotion_id = promotion_id  # type: str
        self.runtime_policy = runtime_policy  # type: CreateAppInstanceGroupRequestRuntimePolicy
        self.security_policy = security_policy  # type: CreateAppInstanceGroupRequestSecurityPolicy
        self.session_timeout = session_timeout  # type: int
        self.storage_policy = storage_policy  # type: CreateAppInstanceGroupRequestStoragePolicy
        self.user_info = user_info  # type: CreateAppInstanceGroupRequestUserInfo
        self.users = users  # type: list[str]

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.runtime_policy:
            self.runtime_policy.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.runtime_policy is not None:
            result['RuntimePolicy'] = self.runtime_policy.to_map()
        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Network') is not None:
            temp_model = CreateAppInstanceGroupRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = CreateAppInstanceGroupRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RuntimePolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestRuntimePolicy()
            self.runtime_policy = temp_model.from_map(m['RuntimePolicy'])
        if m.get('SecurityPolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            temp_model = CreateAppInstanceGroupRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m['StoragePolicy'])
        if m.get('UserInfo') is not None:
            temp_model = CreateAppInstanceGroupRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupShrinkRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_name=None, auto_pay=None, auto_renew=None,
                 biz_region_id=None, charge_resource_mode=None, charge_type=None, network_shrink=None, node_pool_shrink=None,
                 period=None, period_unit=None, pre_open_app_id=None, product_type=None, promotion_id=None,
                 runtime_policy_shrink=None, security_policy_shrink=None, session_timeout=None, storage_policy_shrink=None,
                 user_info_shrink=None, users=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.auto_renew = auto_renew  # type: bool
        self.biz_region_id = biz_region_id  # type: str
        self.charge_resource_mode = charge_resource_mode  # type: str
        self.charge_type = charge_type  # type: str
        self.network_shrink = network_shrink  # type: str
        self.node_pool_shrink = node_pool_shrink  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.pre_open_app_id = pre_open_app_id  # type: str
        self.product_type = product_type  # type: str
        self.promotion_id = promotion_id  # type: str
        self.runtime_policy_shrink = runtime_policy_shrink  # type: str
        self.security_policy_shrink = security_policy_shrink  # type: str
        self.session_timeout = session_timeout  # type: int
        self.storage_policy_shrink = storage_policy_shrink  # type: str
        self.user_info_shrink = user_info_shrink  # type: str
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.runtime_policy_shrink is not None:
            result['RuntimePolicy'] = self.runtime_policy_shrink
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('RuntimePolicy') is not None:
            self.runtime_policy_shrink = m.get('RuntimePolicy')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class CreateAppInstanceGroupResponseBodyAppInstanceGroupModel(TeaModel):
    def __init__(self, app_instance_group_id=None, node_pool_id=None, order_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.node_pool_id = node_pool_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppInstanceGroupResponseBodyAppInstanceGroupModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, app_instance_group_model=None, request_id=None):
        self.app_instance_group_model = app_instance_group_model  # type: CreateAppInstanceGroupResponseBodyAppInstanceGroupModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_instance_group_model:
            self.app_instance_group_model.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_model is not None:
            result['AppInstanceGroupModel'] = self.app_instance_group_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupModel') is not None:
            temp_model = CreateAppInstanceGroupResponseBodyAppInstanceGroupModel()
            self.app_instance_group_model = temp_model.from_map(m['AppInstanceGroupModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppInstanceGroupResponse, self).to_map()
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
            temp_model = CreateAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateImageFromAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_center_image_name=None, app_instance_group_id=None, product_type=None):
        self.app_center_image_name = app_center_image_name  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageFromAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class CreateImageFromAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, image_id=None, request_id=None):
        self.image_id = image_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateImageFromAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateImageFromAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateImageFromAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateImageFromAppInstanceGroupResponse, self).to_map()
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
            temp_model = CreateImageFromAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, clipboard=None, cloud_env_id=None, content_id=None, description=None, file_transfer=None,
                 frame_rate=None, keep_alive_duration=None, project_name=None, session_resolution_height=None,
                 session_resolution_width=None, session_spec=None, streaming_mode=None, terminal_resolution_adaptation=None):
        self.clipboard = clipboard  # type: int
        self.cloud_env_id = cloud_env_id  # type: str
        self.content_id = content_id  # type: str
        self.description = description  # type: str
        self.file_transfer = file_transfer  # type: int
        self.frame_rate = frame_rate  # type: int
        self.keep_alive_duration = keep_alive_duration  # type: int
        self.project_name = project_name  # type: str
        self.session_resolution_height = session_resolution_height  # type: int
        self.session_resolution_width = session_resolution_width  # type: int
        self.session_spec = session_spec  # type: str
        self.streaming_mode = streaming_mode  # type: str
        self.terminal_resolution_adaptation = terminal_resolution_adaptation  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.cloud_env_id is not None:
            result['CloudEnvId'] = self.cloud_env_id
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.keep_alive_duration is not None:
            result['KeepAliveDuration'] = self.keep_alive_duration
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode
        if self.terminal_resolution_adaptation is not None:
            result['TerminalResolutionAdaptation'] = self.terminal_resolution_adaptation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('CloudEnvId') is not None:
            self.cloud_env_id = m.get('CloudEnvId')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('KeepAliveDuration') is not None:
            self.keep_alive_duration = m.get('KeepAliveDuration')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')
        if m.get('TerminalResolutionAdaptation') is not None:
            self.terminal_resolution_adaptation = m.get('TerminalResolutionAdaptation')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessPageRequest(TeaModel):
    def __init__(self, access_page_id=None):
        self.access_page_id = access_page_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        return self


class DeleteAccessPageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessPageResponseBody, self).to_map()
        if _map is not None:
            return _map

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


class DeleteAccessPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessPageResponse, self).to_map()
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
            temp_model = DeleteAccessPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppInstanceGroupResponse, self).to_map()
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
            temp_model = DeleteAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppInstancesRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_ids=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_ids = app_instance_ids  # type: list[str]
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_ids is not None:
            result['AppInstanceIds'] = self.app_instance_ids
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceIds') is not None:
            self.app_instance_ids = m.get('AppInstanceIds')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class DeleteAppInstancesResponseBodyDeleteAppInstanceModels(TeaModel):
    def __init__(self, app_instance_id=None, code=None, message=None, success=None):
        self.app_instance_id = app_instance_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppInstancesResponseBodyDeleteAppInstanceModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAppInstancesResponseBody(TeaModel):
    def __init__(self, delete_app_instance_models=None, request_id=None):
        self.delete_app_instance_models = delete_app_instance_models  # type: list[DeleteAppInstancesResponseBodyDeleteAppInstanceModels]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.delete_app_instance_models:
            for k in self.delete_app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DeleteAppInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeleteAppInstanceModels'] = []
        if self.delete_app_instance_models is not None:
            for k in self.delete_app_instance_models:
                result['DeleteAppInstanceModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.delete_app_instance_models = []
        if m.get('DeleteAppInstanceModels') is not None:
            for k in m.get('DeleteAppInstanceModels'):
                temp_model = DeleteAppInstancesResponseBodyDeleteAppInstanceModels()
                self.delete_app_instance_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppInstancesResponse, self).to_map()
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
            temp_model = DeleteAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
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


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessPageSessionRequest(TeaModel):
    def __init__(self, access_page_id=None, access_page_token=None, external_user_id=None):
        self.access_page_id = access_page_id  # type: str
        self.access_page_token = access_page_token  # type: str
        self.external_user_id = external_user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessPageSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_token is not None:
            result['AccessPageToken'] = self.access_page_token
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageToken') is not None:
            self.access_page_token = m.get('AccessPageToken')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        return self


class GetAccessPageSessionResponseBodyData(TeaModel):
    def __init__(self, connect_ticket=None, flow_id=None):
        self.connect_ticket = connect_ticket  # type: str
        # flow ID
        self.flow_id = flow_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessPageSessionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connect_ticket is not None:
            result['ConnectTicket'] = self.connect_ticket
        if self.flow_id is not None:
            result['FlowId'] = self.flow_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectTicket') is not None:
            self.connect_ticket = m.get('ConnectTicket')
        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')
        return self


class GetAccessPageSessionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetAccessPageSessionResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetAccessPageSessionResponseBody, self).to_map()
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
            temp_model = GetAccessPageSessionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAccessPageSessionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccessPageSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccessPageSessionResponse, self).to_map()
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
            temp_model = GetAccessPageSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(self, app_icon=None, app_id=None, app_name=None, app_version=None, app_version_name=None):
        self.app_icon = app_icon  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_version = app_version  # type: str
        self.app_version_name = app_version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(self, amount=None, end_time=None, start_time=None):
        self.amount = amount  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(self, recurrence_type=None, recurrence_values=None, timer_periods=None):
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_values = recurrence_values  # type: list[int]
        self.timer_periods = timer_periods  # type: list[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods]

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
    def __init__(self, amount=None, max_scaling_amount=None, node_amount=None, node_capacity=None,
                 node_instance_type=None, node_pool_id=None, node_type_name=None, node_used=None, recurrence_schedules=None,
                 scaling_down_after_idle_minutes=None, scaling_node_amount=None, scaling_node_used=None, scaling_step=None,
                 scaling_usage_threshold=None, strategy_disable_date=None, strategy_enable_date=None, strategy_type=None, warm_up=None):
        self.amount = amount  # type: int
        self.max_scaling_amount = max_scaling_amount  # type: int
        self.node_amount = node_amount  # type: int
        self.node_capacity = node_capacity  # type: int
        self.node_instance_type = node_instance_type  # type: str
        self.node_pool_id = node_pool_id  # type: str
        self.node_type_name = node_type_name  # type: str
        self.node_used = node_used  # type: int
        self.recurrence_schedules = recurrence_schedules  # type: list[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules]
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_node_amount = scaling_node_amount  # type: int
        self.scaling_node_used = scaling_node_used  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.strategy_disable_date = strategy_disable_date  # type: str
        self.strategy_enable_date = strategy_enable_date  # type: str
        self.strategy_type = strategy_type  # type: str
        self.warm_up = warm_up  # type: bool

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        if self.node_used is not None:
            result['NodeUsed'] = self.node_used
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_node_amount is not None:
            result['ScalingNodeAmount'] = self.scaling_node_amount
        if self.scaling_node_used is not None:
            result['ScalingNodeUsed'] = self.scaling_node_used
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingNodeAmount') is not None:
            self.scaling_node_amount = m.get('ScalingNodeAmount')
        if m.get('ScalingNodeUsed') is not None:
            self.scaling_node_used = m.get('ScalingNodeUsed')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
    def __init__(self, new_ota_version=None, ota_version=None, task_id=None):
        self.new_ota_version = new_ota_version  # type: str
        self.ota_version = ota_version  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_ota_version is not None:
            result['NewOtaVersion'] = self.new_ota_version
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewOtaVersion') is not None:
            self.new_ota_version = m.get('NewOtaVersion')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
    def __init__(self, amount=None, app_center_image_id=None, app_center_image_name=None,
                 app_instance_group_id=None, app_instance_group_name=None, app_instance_type=None, app_instance_type_name=None,
                 app_policy_id=None, apps=None, charge_resource_mode=None, charge_type=None, expired_time=None, gmt_create=None,
                 max_amount=None, min_amount=None, node_pool=None, os_type=None, ota_info=None, product_type=None,
                 region_id=None, reserve_amount_ratio=None, reserve_max_amount=None, reserve_min_amount=None,
                 resource_status=None, scaling_down_after_idle_minutes=None, scaling_step=None, scaling_usage_threshold=None,
                 session_timeout=None, skip_user_auth_check=None, spec_id=None, status=None):
        self.amount = amount  # type: int
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_center_image_name = app_center_image_name  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.app_instance_type = app_instance_type  # type: str
        self.app_instance_type_name = app_instance_type_name  # type: str
        self.app_policy_id = app_policy_id  # type: str
        self.apps = apps  # type: list[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps]
        self.charge_resource_mode = charge_resource_mode  # type: str
        self.charge_type = charge_type  # type: str
        self.expired_time = expired_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int
        self.node_pool = node_pool  # type: list[GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool]
        self.os_type = os_type  # type: str
        self.ota_info = ota_info  # type: GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.reserve_amount_ratio = reserve_amount_ratio  # type: str
        self.reserve_max_amount = reserve_max_amount  # type: int
        self.reserve_min_amount = reserve_min_amount  # type: int
        self.resource_status = resource_status  # type: str
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.session_timeout = session_timeout  # type: str
        self.skip_user_auth_check = skip_user_auth_check  # type: bool
        self.spec_id = spec_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBodyAppInstanceGroupModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_center_image_name is not None:
            result['AppCenterImageName'] = self.app_center_image_name
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.app_instance_type_name is not None:
            result['AppInstanceTypeName'] = self.app_instance_type_name
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount
        result['NodePool'] = []
        if self.node_pool is not None:
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserve_amount_ratio is not None:
            result['ReserveAmountRatio'] = self.reserve_amount_ratio
        if self.reserve_max_amount is not None:
            result['ReserveMaxAmount'] = self.reserve_max_amount
        if self.reserve_min_amount is not None:
            result['ReserveMinAmount'] = self.reserve_min_amount
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppCenterImageName') is not None:
            self.app_center_image_name = m.get('AppCenterImageName')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('AppInstanceTypeName') is not None:
            self.app_instance_type_name = m.get('AppInstanceTypeName')
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')
        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')
        self.node_pool = []
        if m.get('NodePool') is not None:
            for k in m.get('NodePool'):
                temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReserveAmountRatio') is not None:
            self.reserve_amount_ratio = m.get('ReserveAmountRatio')
        if m.get('ReserveMaxAmount') is not None:
            self.reserve_max_amount = m.get('ReserveMaxAmount')
        if m.get('ReserveMinAmount') is not None:
            self.reserve_min_amount = m.get('ReserveMinAmount')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, app_instance_group_models=None, request_id=None):
        # AppInstanceGroupModels
        self.app_instance_group_models = app_instance_group_models  # type: GetAppInstanceGroupResponseBodyAppInstanceGroupModels
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_instance_group_models:
            self.app_instance_group_models.validate()

    def to_map(self):
        _map = super(GetAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_models is not None:
            result['AppInstanceGroupModels'] = self.app_instance_group_models.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupModels') is not None:
            temp_model = GetAppInstanceGroupResponseBodyAppInstanceGroupModels()
            self.app_instance_group_models = temp_model.from_map(m['AppInstanceGroupModels'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppInstanceGroupResponse, self).to_map()
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
            temp_model = GetAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnectionTicketRequest(TeaModel):
    def __init__(self, app_id=None, app_instance_group_id_list=None, app_instance_id=None,
                 app_instance_persistent_id=None, app_start_param=None, app_version=None, biz_region_id=None, end_user_id=None,
                 product_type=None, task_id=None):
        self.app_id = app_id  # type: str
        self.app_instance_group_id_list = app_instance_group_id_list  # type: list[str]
        self.app_instance_id = app_instance_id  # type: str
        self.app_instance_persistent_id = app_instance_persistent_id  # type: str
        self.app_start_param = app_start_param  # type: str
        self.app_version = app_version  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.product_type = product_type  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id_list is not None:
            result['AppInstanceGroupIdList'] = self.app_instance_group_id_list
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.app_start_param is not None:
            result['AppStartParam'] = self.app_start_param
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupIdList') is not None:
            self.app_instance_group_id_list = m.get('AppInstanceGroupIdList')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('AppStartParam') is not None:
            self.app_start_param = m.get('AppStartParam')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetConnectionTicketResponseBody(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_id=None, app_instance_persistent_id=None,
                 biz_region_id=None, os_type=None, request_id=None, task_id=None, task_status=None, tenant_id=None, ticket=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_id = app_instance_id  # type: str
        self.app_instance_persistent_id = app_instance_persistent_id  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.os_type = os_type  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: str
        self.tenant_id = tenant_id  # type: long
        self.ticket = ticket  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConnectionTicketResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.ticket is not None:
            result['Ticket'] = self.ticket
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')
        return self


class GetConnectionTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConnectionTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConnectionTicketResponse, self).to_map()
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
            temp_model = GetConnectionTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDebugAppInstanceRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDebugAppInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetDebugAppInstanceResponseBody(TeaModel):
    def __init__(self, app_id=None, app_instance_group_id=None, app_instance_id=None, app_version=None,
                 auth_code=None, request_id=None, user_id=None):
        self.app_id = app_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_id = app_instance_id  # type: str
        self.app_version = app_version  # type: str
        self.auth_code = auth_code  # type: str
        self.request_id = request_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDebugAppInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetDebugAppInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDebugAppInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDebugAppInstanceResponse, self).to_map()
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
            temp_model = GetDebugAppInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOtaTaskByTaskIdRequest(TeaModel):
    def __init__(self, task_id=None):
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOtaTaskByTaskIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetOtaTaskByTaskIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, ota_version=None, release_note=None, request_id=None,
                 task_start_time=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.ota_version = ota_version  # type: str
        self.release_note = release_note  # type: str
        self.request_id = request_id  # type: str
        self.task_start_time = task_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOtaTaskByTaskIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.release_note is not None:
            result['ReleaseNote'] = self.release_note
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('ReleaseNote') is not None:
            self.release_note = m.get('ReleaseNote')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class GetOtaTaskByTaskIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOtaTaskByTaskIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOtaTaskByTaskIdResponse, self).to_map()
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
            temp_model = GetOtaTaskByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectPoliciesRequest(TeaModel):
    def __init__(self, project_id=None):
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectPoliciesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetProjectPoliciesResponseBodyData(TeaModel):
    def __init__(self, clipboard=None, file_transfer=None, frame_rate=None, keep_alive_duration=None,
                 max_hours=None, max_sessions=None, project_id=None, session_resolution_height=None,
                 session_resolution_width=None, session_spec=None, streaming_mode=None, terminal_resolution_adaptation=None):
        self.clipboard = clipboard  # type: int
        self.file_transfer = file_transfer  # type: int
        self.frame_rate = frame_rate  # type: str
        self.keep_alive_duration = keep_alive_duration  # type: int
        self.max_hours = max_hours  # type: int
        self.max_sessions = max_sessions  # type: int
        self.project_id = project_id  # type: str
        self.session_resolution_height = session_resolution_height  # type: int
        self.session_resolution_width = session_resolution_width  # type: int
        self.session_spec = session_spec  # type: str
        self.streaming_mode = streaming_mode  # type: str
        self.terminal_resolution_adaptation = terminal_resolution_adaptation  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectPoliciesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.keep_alive_duration is not None:
            result['KeepAliveDuration'] = self.keep_alive_duration
        if self.max_hours is not None:
            result['MaxHours'] = self.max_hours
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode
        if self.terminal_resolution_adaptation is not None:
            result['TerminalResolutionAdaptation'] = self.terminal_resolution_adaptation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('KeepAliveDuration') is not None:
            self.keep_alive_duration = m.get('KeepAliveDuration')
        if m.get('MaxHours') is not None:
            self.max_hours = m.get('MaxHours')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')
        if m.get('TerminalResolutionAdaptation') is not None:
            self.terminal_resolution_adaptation = m.get('TerminalResolutionAdaptation')
        return self


class GetProjectPoliciesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetProjectPoliciesResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProjectPoliciesResponseBody, self).to_map()
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
            temp_model = GetProjectPoliciesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProjectPoliciesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectPoliciesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectPoliciesResponse, self).to_map()
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
            temp_model = GetProjectPoliciesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePriceRequest(TeaModel):
    def __init__(self, amount=None, app_instance_type=None, biz_region_id=None, charge_type=None,
                 node_instance_type=None, period=None, period_unit=None, product_type=None):
        self.amount = amount  # type: long
        self.app_instance_type = app_instance_type  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.charge_type = charge_type  # type: str
        self.node_instance_type = node_instance_type  # type: str
        self.period = period  # type: long
        self.period_unit = period_unit  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourcePriceResponseBodyPriceListPricePromotions(TeaModel):
    def __init__(self, option_code=None, promotion_desc=None, promotion_id=None, promotion_name=None, selected=None):
        self.option_code = option_code  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceListPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceListPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, promotions=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: str
        self.original_price = original_price  # type: str
        self.promotions = promotions  # type: list[GetResourcePriceResponseBodyPriceListPricePromotions]
        self.trade_price = trade_price  # type: str

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceListPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
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
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceListPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceListRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceListRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceList(TeaModel):
    def __init__(self, price=None, price_type=None, rules=None):
        self.price = price  # type: GetResourcePriceResponseBodyPriceListPrice
        self.price_type = price_type  # type: str
        self.rules = rules  # type: list[GetResourcePriceResponseBodyPriceListRules]

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        if self.price_type is not None:
            result['PriceType'] = self.price_type
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceListPrice()
            self.price = temp_model.from_map(m['Price'])
        if m.get('PriceType') is not None:
            self.price_type = m.get('PriceType')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceListRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBodyPriceModelPricePromotions(TeaModel):
    def __init__(self, option_code=None, promotion_desc=None, promotion_id=None, promotion_name=None, selected=None):
        self.option_code = option_code  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModelPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourcePriceResponseBodyPriceModelPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, promotions=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: str
        self.original_price = original_price  # type: str
        self.promotions = promotions  # type: list[GetResourcePriceResponseBodyPriceModelPricePromotions]
        self.trade_price = trade_price  # type: str

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModelPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
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
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourcePriceResponseBodyPriceModelPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourcePriceResponseBodyPriceModelRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModelRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourcePriceResponseBodyPriceModel(TeaModel):
    def __init__(self, price=None, rules=None):
        self.price = price  # type: GetResourcePriceResponseBodyPriceModelPrice
        self.rules = rules  # type: list[GetResourcePriceResponseBodyPriceModelRules]

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBodyPriceModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModelPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourcePriceResponseBodyPriceModelRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourcePriceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, price_list=None, price_model=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.price_list = price_list  # type: list[GetResourcePriceResponseBodyPriceList]
        self.price_model = price_model  # type: GetResourcePriceResponseBodyPriceModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.price_list:
            for k in self.price_list:
                if k:
                    k.validate()
        if self.price_model:
            self.price_model.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['PriceList'] = []
        if self.price_list is not None:
            for k in self.price_list:
                result['PriceList'].append(k.to_map() if k else None)
        if self.price_model is not None:
            result['PriceModel'] = self.price_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.price_list = []
        if m.get('PriceList') is not None:
            for k in m.get('PriceList'):
                temp_model = GetResourcePriceResponseBodyPriceList()
                self.price_list.append(temp_model.from_map(k))
        if m.get('PriceModel') is not None:
            temp_model = GetResourcePriceResponseBodyPriceModel()
            self.price_model = temp_model.from_map(m['PriceModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourcePriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourcePriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourcePriceResponse, self).to_map()
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
            temp_model = GetResourcePriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceRenewPriceRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, period=None, period_unit=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.period = period  # type: long
        self.period_unit = period_unit  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRenewPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class GetResourceRenewPriceResponseBodyDataPricePromotions(TeaModel):
    def __init__(self, option_code=None, promotion_desc=None, promotion_id=None, promotion_name=None, selected=None):
        self.option_code = option_code  # type: str
        self.promotion_desc = promotion_desc  # type: str
        self.promotion_id = promotion_id  # type: str
        self.promotion_name = promotion_name  # type: str
        self.selected = selected  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyDataPricePromotions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.option_code is not None:
            result['OptionCode'] = self.option_code
        if self.promotion_desc is not None:
            result['PromotionDesc'] = self.promotion_desc
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        if self.promotion_name is not None:
            result['PromotionName'] = self.promotion_name
        if self.selected is not None:
            result['Selected'] = self.selected
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OptionCode') is not None:
            self.option_code = m.get('OptionCode')
        if m.get('PromotionDesc') is not None:
            self.promotion_desc = m.get('PromotionDesc')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        if m.get('PromotionName') is not None:
            self.promotion_name = m.get('PromotionName')
        if m.get('Selected') is not None:
            self.selected = m.get('Selected')
        return self


class GetResourceRenewPriceResponseBodyDataPrice(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, promotions=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: str
        self.original_price = original_price  # type: str
        self.promotions = promotions  # type: list[GetResourceRenewPriceResponseBodyDataPricePromotions]
        self.trade_price = trade_price  # type: str

    def validate(self):
        if self.promotions:
            for k in self.promotions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyDataPrice, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        result['Promotions'] = []
        if self.promotions is not None:
            for k in self.promotions:
                result['Promotions'].append(k.to_map() if k else None)
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
        self.promotions = []
        if m.get('Promotions') is not None:
            for k in m.get('Promotions'):
                temp_model = GetResourceRenewPriceResponseBodyDataPricePromotions()
                self.promotions.append(temp_model.from_map(k))
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class GetResourceRenewPriceResponseBodyDataRules(TeaModel):
    def __init__(self, description=None, rule_id=None):
        self.description = description  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetResourceRenewPriceResponseBodyData(TeaModel):
    def __init__(self, price=None, rules=None):
        self.price = price  # type: GetResourceRenewPriceResponseBodyDataPrice
        self.rules = rules  # type: list[GetResourceRenewPriceResponseBodyDataRules]

    def validate(self):
        if self.price:
            self.price.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.price is not None:
            result['Price'] = self.price.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Price') is not None:
            temp_model = GetResourceRenewPriceResponseBodyDataPrice()
            self.price = temp_model.from_map(m['Price'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = GetResourceRenewPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class GetResourceRenewPriceResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetResourceRenewPriceResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetResourceRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetResourceRenewPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourceRenewPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourceRenewPriceResponse, self).to_map()
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
            temp_model = GetResourceRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessPagesRequest(TeaModel):
    def __init__(self, access_page_id=None, access_page_name=None, page_number=None, page_size=None,
                 project_id=None, sort_type=None):
        self.access_page_id = access_page_id  # type: str
        self.access_page_name = access_page_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.sort_type = sort_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessPagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        return self


class ListAccessPagesResponseBodyData(TeaModel):
    def __init__(self, access_mode=None, access_page_id=None, access_page_name=None, access_page_state=None,
                 access_url=None, content_id=None, content_name=None, effect_time=None, gmt_create=None, project_id=None,
                 project_name=None, unit=None, url_expire_time=None):
        self.access_mode = access_mode  # type: str
        self.access_page_id = access_page_id  # type: str
        self.access_page_name = access_page_name  # type: str
        self.access_page_state = access_page_state  # type: str
        self.access_url = access_url  # type: str
        self.content_id = content_id  # type: str
        self.content_name = content_name  # type: str
        self.effect_time = effect_time  # type: int
        self.gmt_create = gmt_create  # type: str
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.unit = unit  # type: str
        self.url_expire_time = url_expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessPagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_mode is not None:
            result['AccessMode'] = self.access_mode
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_name is not None:
            result['AccessPageName'] = self.access_page_name
        if self.access_page_state is not None:
            result['AccessPageState'] = self.access_page_state
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.unit is not None:
            result['Unit'] = self.unit
        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessMode') is not None:
            self.access_mode = m.get('AccessMode')
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageName') is not None:
            self.access_page_name = m.get('AccessPageName')
        if m.get('AccessPageState') is not None:
            self.access_page_state = m.get('AccessPageState')
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Unit') is not None:
            self.unit = m.get('Unit')
        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')
        return self


class ListAccessPagesResponseBody(TeaModel):
    def __init__(self, code=None, count=None, data=None, message=None, page_number=None, page_size=None,
                 request_id=None, success=None):
        self.code = code  # type: str
        self.count = count  # type: str
        self.data = data  # type: list[ListAccessPagesResponseBodyData]
        self.message = message  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccessPagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAccessPagesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAccessPagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccessPagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccessPagesResponse, self).to_map()
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
            temp_model = ListAccessPagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_id=None, app_instance_group_name=None,
                 biz_region_id=None, node_instance_type=None, page_number=None, page_size=None, product_type=None, status=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.node_instance_type = node_instance_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str
        self.status = status  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps(TeaModel):
    def __init__(self, app_icon=None, app_id=None, app_name=None, app_version=None, app_version_name=None):
        # 应用图标。
        self.app_icon = app_icon  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        # 应用版本。
        self.app_version = app_version  # type: str
        # 应用版本名称。
        self.app_version_name = app_version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_icon is not None:
            result['AppIcon'] = self.app_icon
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIcon') is not None:
            self.app_icon = m.get('AppIcon')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(self, amount=None, end_time=None, start_time=None):
        self.amount = amount  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules(TeaModel):
    def __init__(self, recurrence_type=None, recurrence_values=None, timer_periods=None):
        self.recurrence_type = recurrence_type  # type: str
        self.recurrence_values = recurrence_values  # type: list[int]
        self.timer_periods = timer_periods  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods]

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool(TeaModel):
    def __init__(self, amount=None, max_scaling_amount=None, node_amount=None, node_capacity=None,
                 node_instance_type=None, node_pool_id=None, node_type_name=None, node_used=None, recurrence_schedules=None,
                 scaling_down_after_idle_minutes=None, scaling_node_amount=None, scaling_node_used=None, scaling_step=None,
                 scaling_usage_threshold=None, strategy_disable_date=None, strategy_enable_date=None, strategy_type=None, warm_up=None):
        self.amount = amount  # type: int
        self.max_scaling_amount = max_scaling_amount  # type: int
        self.node_amount = node_amount  # type: int
        self.node_capacity = node_capacity  # type: int
        self.node_instance_type = node_instance_type  # type: str
        self.node_pool_id = node_pool_id  # type: str
        self.node_type_name = node_type_name  # type: str
        self.node_used = node_used  # type: int
        self.recurrence_schedules = recurrence_schedules  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules]
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_node_amount = scaling_node_amount  # type: int
        self.scaling_node_used = scaling_node_used  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.strategy_disable_date = strategy_disable_date  # type: str
        self.strategy_enable_date = strategy_enable_date  # type: str
        self.strategy_type = strategy_type  # type: str
        self.warm_up = warm_up  # type: bool

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        if self.node_used is not None:
            result['NodeUsed'] = self.node_used
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_node_amount is not None:
            result['ScalingNodeAmount'] = self.scaling_node_amount
        if self.scaling_node_used is not None:
            result['ScalingNodeUsed'] = self.scaling_node_used
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        if m.get('NodeUsed') is not None:
            self.node_used = m.get('NodeUsed')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePoolRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingNodeAmount') is not None:
            self.scaling_node_amount = m.get('ScalingNodeAmount')
        if m.get('ScalingNodeUsed') is not None:
            self.scaling_node_used = m.get('ScalingNodeUsed')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo(TeaModel):
    def __init__(self, new_ota_version=None, ota_version=None, task_id=None):
        self.new_ota_version = new_ota_version  # type: str
        self.ota_version = ota_version  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_ota_version is not None:
            result['NewOtaVersion'] = self.new_ota_version
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NewOtaVersion') is not None:
            self.new_ota_version = m.get('NewOtaVersion')
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListAppInstanceGroupResponseBodyAppInstanceGroupModels(TeaModel):
    def __init__(self, amount=None, app_center_image_id=None, app_instance_group_id=None,
                 app_instance_group_name=None, app_instance_type=None, app_policy_id=None, apps=None, charge_resource_mode=None,
                 charge_type=None, expired_time=None, gmt_create=None, max_amount=None, min_amount=None, node_pool=None,
                 os_type=None, ota_info=None, product_type=None, region_id=None, reserve_amount_ratio=None,
                 reserve_max_amount=None, reserve_min_amount=None, resource_status=None, scaling_down_after_idle_minutes=None,
                 scaling_step=None, scaling_usage_threshold=None, session_timeout=None, skip_user_auth_check=None, spec_id=None,
                 status=None):
        self.amount = amount  # type: int
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.app_instance_type = app_instance_type  # type: str
        # 策略ID。
        self.app_policy_id = app_policy_id  # type: str
        self.apps = apps  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps]
        # 售卖模式。
        self.charge_resource_mode = charge_resource_mode  # type: str
        self.charge_type = charge_type  # type: str
        self.expired_time = expired_time  # type: str
        self.gmt_create = gmt_create  # type: str
        self.max_amount = max_amount  # type: int
        self.min_amount = min_amount  # type: int
        self.node_pool = node_pool  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool]
        self.os_type = os_type  # type: str
        self.ota_info = ota_info  # type: ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo
        self.product_type = product_type  # type: str
        self.region_id = region_id  # type: str
        self.reserve_amount_ratio = reserve_amount_ratio  # type: str
        self.reserve_max_amount = reserve_max_amount  # type: int
        self.reserve_min_amount = reserve_min_amount  # type: int
        self.resource_status = resource_status  # type: str
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        self.session_timeout = session_timeout  # type: str
        self.skip_user_auth_check = skip_user_auth_check  # type: bool
        self.spec_id = spec_id  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()
        if self.node_pool:
            for k in self.node_pool:
                if k:
                    k.validate()
        if self.ota_info:
            self.ota_info.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBodyAppInstanceGroupModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.app_instance_type is not None:
            result['AppInstanceType'] = self.app_instance_type
        if self.app_policy_id is not None:
            result['AppPolicyId'] = self.app_policy_id
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.charge_resource_mode is not None:
            result['ChargeResourceMode'] = self.charge_resource_mode
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.max_amount is not None:
            result['MaxAmount'] = self.max_amount
        if self.min_amount is not None:
            result['MinAmount'] = self.min_amount
        result['NodePool'] = []
        if self.node_pool is not None:
            for k in self.node_pool:
                result['NodePool'].append(k.to_map() if k else None)
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.ota_info is not None:
            result['OtaInfo'] = self.ota_info.to_map()
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.reserve_amount_ratio is not None:
            result['ReserveAmountRatio'] = self.reserve_amount_ratio
        if self.reserve_max_amount is not None:
            result['ReserveMaxAmount'] = self.reserve_max_amount
        if self.reserve_min_amount is not None:
            result['ReserveMinAmount'] = self.reserve_min_amount
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('AppInstanceType') is not None:
            self.app_instance_type = m.get('AppInstanceType')
        if m.get('AppPolicyId') is not None:
            self.app_policy_id = m.get('AppPolicyId')
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('ChargeResourceMode') is not None:
            self.charge_resource_mode = m.get('ChargeResourceMode')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('MaxAmount') is not None:
            self.max_amount = m.get('MaxAmount')
        if m.get('MinAmount') is not None:
            self.min_amount = m.get('MinAmount')
        self.node_pool = []
        if m.get('NodePool') is not None:
            for k in m.get('NodePool'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsNodePool()
                self.node_pool.append(temp_model.from_map(k))
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('OtaInfo') is not None:
            temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModelsOtaInfo()
            self.ota_info = temp_model.from_map(m['OtaInfo'])
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReserveAmountRatio') is not None:
            self.reserve_amount_ratio = m.get('ReserveAmountRatio')
        if m.get('ReserveMaxAmount') is not None:
            self.reserve_max_amount = m.get('ReserveMaxAmount')
        if m.get('ReserveMinAmount') is not None:
            self.reserve_min_amount = m.get('ReserveMinAmount')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, app_instance_group_models=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.app_instance_group_models = app_instance_group_models  # type: list[ListAppInstanceGroupResponseBodyAppInstanceGroupModels]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.app_instance_group_models:
            for k in self.app_instance_group_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceGroupModels'] = []
        if self.app_instance_group_models is not None:
            for k in self.app_instance_group_models:
                result['AppInstanceGroupModels'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_instance_group_models = []
        if m.get('AppInstanceGroupModels') is not None:
            for k in m.get('AppInstanceGroupModels'):
                temp_model = ListAppInstanceGroupResponseBodyAppInstanceGroupModels()
                self.app_instance_group_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppInstanceGroupResponse, self).to_map()
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
            temp_model = ListAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInstancesRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_id=None, app_instance_id_list=None,
                 include_deleted=None, page_number=None, page_size=None, status=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_id = app_instance_id  # type: str
        self.app_instance_id_list = app_instance_id_list  # type: list[str]
        self.include_deleted = include_deleted  # type: bool
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_id_list is not None:
            result['AppInstanceIdList'] = self.app_instance_id_list
        if self.include_deleted is not None:
            result['IncludeDeleted'] = self.include_deleted
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstanceIdList') is not None:
            self.app_instance_id_list = m.get('AppInstanceIdList')
        if m.get('IncludeDeleted') is not None:
            self.include_deleted = m.get('IncludeDeleted')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstancesResponseBodyAppInstanceModelsBindInfo(TeaModel):
    def __init__(self, end_user_id=None, usage_duration=None):
        self.end_user_id = end_user_id  # type: str
        self.usage_duration = usage_duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppInstancesResponseBodyAppInstanceModelsBindInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.usage_duration is not None:
            result['UsageDuration'] = self.usage_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('UsageDuration') is not None:
            self.usage_duration = m.get('UsageDuration')
        return self


class ListAppInstancesResponseBodyAppInstanceModels(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_id=None, bind_info=None, gmt_create=None,
                 gmt_modified=None, main_eth_public_ip=None, session_status=None, status=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_id = app_instance_id  # type: str
        self.bind_info = bind_info  # type: ListAppInstancesResponseBodyAppInstanceModelsBindInfo
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.main_eth_public_ip = main_eth_public_ip  # type: str
        self.session_status = session_status  # type: str
        self.status = status  # type: str

    def validate(self):
        if self.bind_info:
            self.bind_info.validate()

    def to_map(self):
        _map = super(ListAppInstancesResponseBodyAppInstanceModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.bind_info is not None:
            result['BindInfo'] = self.bind_info.to_map()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.main_eth_public_ip is not None:
            result['MainEthPublicIp'] = self.main_eth_public_ip
        if self.session_status is not None:
            result['SessionStatus'] = self.session_status
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('BindInfo') is not None:
            temp_model = ListAppInstancesResponseBodyAppInstanceModelsBindInfo()
            self.bind_info = temp_model.from_map(m['BindInfo'])
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('MainEthPublicIp') is not None:
            self.main_eth_public_ip = m.get('MainEthPublicIp')
        if m.get('SessionStatus') is not None:
            self.session_status = m.get('SessionStatus')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppInstancesResponseBody(TeaModel):
    def __init__(self, app_instance_models=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.app_instance_models = app_instance_models  # type: list[ListAppInstancesResponseBodyAppInstanceModels]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.app_instance_models:
            for k in self.app_instance_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInstanceModels'] = []
        if self.app_instance_models is not None:
            for k in self.app_instance_models:
                result['AppInstanceModels'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_instance_models = []
        if m.get('AppInstanceModels') is not None:
            for k in m.get('AppInstanceModels'):
                temp_model = ListAppInstancesResponseBodyAppInstanceModels()
                self.app_instance_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppInstancesResponse, self).to_map()
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
            temp_model = ListAppInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeInstanceTypeRequest(TeaModel):
    def __init__(self, biz_region_id=None, language=None, node_instance_type=None, os_type=None, page_number=None,
                 page_size=None, product_type=None):
        # 资源所属的地域ID。关于支持的地域详情，请参见[使用限制](~~426036~~)。
        self.biz_region_id = biz_region_id  # type: str
        # 语言类型。
        self.language = language  # type: str
        self.node_instance_type = node_instance_type  # type: str
        # 支持的操作系统类型。
        self.os_type = os_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeInstanceTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.language is not None:
            result['Language'] = self.language
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.os_type is not None:
            result['OsType'] = self.os_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels(TeaModel):
    def __init__(self, cpu=None, gpu=None, gpu_memory=None, max_capacity=None, memory=None, node_instance_type=None,
                 node_instance_type_family=None, node_type_name=None):
        self.cpu = cpu  # type: str
        self.gpu = gpu  # type: str
        # 显卡内存大小，单位为MB。
        self.gpu_memory = gpu_memory  # type: long
        # 最大并发会话数，即单个资源可同时连接的会话数。如果同时连接的会话数过多，可能导致应用的使用体验下降。取值范围因资源规格不同而不同。各资源规格对应的取值范围分别是：
        # 
        # - appstreaming.general.4c8g：1\~2；
        # - appstreaming.general.8c16g：1\~4；
        # - appstreaming.vgpu.8c16g.4g：1\~4；
        # - appstreaming.vgpu.8c31g.16g：1\~4；
        # - appstreaming.vgpu.14c93g.12g：1\~6；
        self.max_capacity = max_capacity  # type: int
        self.memory = memory  # type: long
        self.node_instance_type = node_instance_type  # type: str
        self.node_instance_type_family = node_instance_type_family  # type: str
        # 资源规格名称。
        self.node_type_name = node_type_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.gpu is not None:
            result['Gpu'] = self.gpu
        if self.gpu_memory is not None:
            result['GpuMemory'] = self.gpu_memory
        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.node_instance_type is not None:
            result['NodeInstanceType'] = self.node_instance_type
        if self.node_instance_type_family is not None:
            result['NodeInstanceTypeFamily'] = self.node_instance_type_family
        if self.node_type_name is not None:
            result['NodeTypeName'] = self.node_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')
        if m.get('GpuMemory') is not None:
            self.gpu_memory = m.get('GpuMemory')
        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('NodeInstanceType') is not None:
            self.node_instance_type = m.get('NodeInstanceType')
        if m.get('NodeInstanceTypeFamily') is not None:
            self.node_instance_type_family = m.get('NodeInstanceTypeFamily')
        if m.get('NodeTypeName') is not None:
            self.node_type_name = m.get('NodeTypeName')
        return self


class ListNodeInstanceTypeResponseBody(TeaModel):
    def __init__(self, node_instance_type_models=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        self.node_instance_type_models = node_instance_type_models  # type: list[ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.node_instance_type_models:
            for k in self.node_instance_type_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNodeInstanceTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['NodeInstanceTypeModels'] = []
        if self.node_instance_type_models is not None:
            for k in self.node_instance_type_models:
                result['NodeInstanceTypeModels'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.node_instance_type_models = []
        if m.get('NodeInstanceTypeModels') is not None:
            for k in m.get('NodeInstanceTypeModels'):
                temp_model = ListNodeInstanceTypeResponseBodyNodeInstanceTypeModels()
                self.node_instance_type_models.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNodeInstanceTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNodeInstanceTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNodeInstanceTypeResponse, self).to_map()
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
            temp_model = ListNodeInstanceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOtaTaskRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, ota_type=None, page_number=None, page_size=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.ota_type = ota_type  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOtaTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.ota_type is not None:
            result['OtaType'] = self.ota_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('OtaType') is not None:
            self.ota_type = m.get('OtaType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOtaTaskResponseBodyTaskList(TeaModel):
    def __init__(self, ota_version=None, task_display_status=None, task_id=None, task_start_time=None):
        self.ota_version = ota_version  # type: str
        self.task_display_status = task_display_status  # type: str
        self.task_id = task_id  # type: str
        self.task_start_time = task_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOtaTaskResponseBodyTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ota_version is not None:
            result['OtaVersion'] = self.ota_version
        if self.task_display_status is not None:
            result['TaskDisplayStatus'] = self.task_display_status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OtaVersion') is not None:
            self.ota_version = m.get('OtaVersion')
        if m.get('TaskDisplayStatus') is not None:
            self.task_display_status = m.get('TaskDisplayStatus')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        return self


class ListOtaTaskResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, task_list=None, total_count=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.task_list = task_list  # type: list[ListOtaTaskResponseBodyTaskList]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOtaTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = ListOtaTaskResponseBodyTaskList()
                self.task_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOtaTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOtaTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOtaTaskResponse, self).to_map()
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
            temp_model = ListOtaTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, project_name=None, sort_type=None,
                 state_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.sort_type = sort_type  # type: str
        self.state_list = state_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.state_list is not None:
            result['StateList'] = self.state_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('StateList') is not None:
            self.state_list = m.get('StateList')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(self, access_page_id=None, available_hours=None, content_id=None, content_name=None,
                 create_time=None, description=None, in_use_sessions=None, max_hours=None, max_sessions=None, project_id=None,
                 project_name=None, project_state=None, session_spec=None):
        self.access_page_id = access_page_id  # type: list[long]
        self.available_hours = available_hours  # type: int
        self.content_id = content_id  # type: str
        self.content_name = content_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.in_use_sessions = in_use_sessions  # type: long
        self.max_hours = max_hours  # type: long
        self.max_sessions = max_sessions  # type: long
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.project_state = project_state  # type: str
        self.session_spec = session_spec  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListProjectsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.available_hours is not None:
            result['AvailableHours'] = self.available_hours
        if self.content_id is not None:
            result['ContentId'] = self.content_id
        if self.content_name is not None:
            result['ContentName'] = self.content_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.in_use_sessions is not None:
            result['InUseSessions'] = self.in_use_sessions
        if self.max_hours is not None:
            result['MaxHours'] = self.max_hours
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_state is not None:
            result['ProjectState'] = self.project_state
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AvailableHours') is not None:
            self.available_hours = m.get('AvailableHours')
        if m.get('ContentId') is not None:
            self.content_id = m.get('ContentId')
        if m.get('ContentName') is not None:
            self.content_name = m.get('ContentName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InUseSessions') is not None:
            self.in_use_sessions = m.get('InUseSessions')
        if m.get('MaxHours') is not None:
            self.max_hours = m.get('MaxHours')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectState') is not None:
            self.project_state = m.get('ProjectState')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, page_number=None, page_size=None, request_id=None,
                 success=None, total_count=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListProjectsResponseBodyData]
        self.message = message  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListProjectsResponseBody, self).to_map()
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
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListProjectsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListProjectsResponse, self).to_map()
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
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegionModels(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyRegionModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, region_models=None, request_id=None):
        self.region_models = region_models  # type: list[ListRegionsResponseBodyRegionModels]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.region_models:
            for k in self.region_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionModels'] = []
        if self.region_models is not None:
            for k in self.region_models:
                result['RegionModels'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k in m.get('RegionModels'):
                temp_model = ListRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSessionPackagesRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, project_id=None, session_package_id=None,
                 session_package_name=None, sort_type=None, state_list=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.project_id = project_id  # type: str
        self.session_package_id = session_package_id  # type: str
        self.session_package_name = session_package_name  # type: str
        self.sort_type = sort_type  # type: str
        self.state_list = state_list  # type: list[int]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSessionPackagesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.session_package_name is not None:
            result['SessionPackageName'] = self.session_package_name
        if self.sort_type is not None:
            result['SortType'] = self.sort_type
        if self.state_list is not None:
            result['StateList'] = self.state_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('SessionPackageName') is not None:
            self.session_package_name = m.get('SessionPackageName')
        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')
        if m.get('StateList') is not None:
            self.state_list = m.get('StateList')
        return self


class ListSessionPackagesResponseBodyDataInstanceObject(TeaModel):
    def __init__(self, expired_time=None, instance_id=None, instance_type=None, resource_id=None,
                 resource_type=None, start_time=None, total_time=None, used_time=None):
        self.expired_time = expired_time  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_type = instance_type  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.start_time = start_time  # type: str
        self.total_time = total_time  # type: long
        self.used_time = used_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSessionPackagesResponseBodyDataInstanceObject, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_time is not None:
            result['TotalTime'] = self.total_time
        if self.used_time is not None:
            result['UsedTime'] = self.used_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalTime') is not None:
            self.total_time = m.get('TotalTime')
        if m.get('UsedTime') is not None:
            self.used_time = m.get('UsedTime')
        return self


class ListSessionPackagesResponseBodyData(TeaModel):
    def __init__(self, available_hours=None, charge_type=None, delete_status=None, gmt_create=None,
                 gmt_modified_time=None, instance_object=None, max_hours=None, max_sessions=None, project_id=None, project_name=None,
                 region=None, session_package_id=None, session_package_name=None, session_package_type_id=None,
                 session_spec=None, session_usage_rate=None, state=None, user_identification=None):
        self.available_hours = available_hours  # type: long
        self.charge_type = charge_type  # type: str
        self.delete_status = delete_status  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_object = instance_object  # type: ListSessionPackagesResponseBodyDataInstanceObject
        self.max_hours = max_hours  # type: long
        self.max_sessions = max_sessions  # type: long
        self.project_id = project_id  # type: str
        self.project_name = project_name  # type: str
        self.region = region  # type: str
        self.session_package_id = session_package_id  # type: str
        self.session_package_name = session_package_name  # type: str
        self.session_package_type_id = session_package_type_id  # type: str
        self.session_spec = session_spec  # type: str
        self.session_usage_rate = session_usage_rate  # type: long
        self.state = state  # type: int
        self.user_identification = user_identification  # type: long

    def validate(self):
        if self.instance_object:
            self.instance_object.validate()

    def to_map(self):
        _map = super(ListSessionPackagesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_hours is not None:
            result['AvailableHours'] = self.available_hours
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.delete_status is not None:
            result['DeleteStatus'] = self.delete_status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_object is not None:
            result['InstanceObject'] = self.instance_object.to_map()
        if self.max_hours is not None:
            result['MaxHours'] = self.max_hours
        if self.max_sessions is not None:
            result['MaxSessions'] = self.max_sessions
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.region is not None:
            result['Region'] = self.region
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.session_package_name is not None:
            result['SessionPackageName'] = self.session_package_name
        if self.session_package_type_id is not None:
            result['SessionPackageTypeId'] = self.session_package_type_id
        if self.session_spec is not None:
            result['SessionSpec'] = self.session_spec
        if self.session_usage_rate is not None:
            result['SessionUsageRate'] = self.session_usage_rate
        if self.state is not None:
            result['State'] = self.state
        if self.user_identification is not None:
            result['UserIdentification'] = self.user_identification
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableHours') is not None:
            self.available_hours = m.get('AvailableHours')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('DeleteStatus') is not None:
            self.delete_status = m.get('DeleteStatus')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceObject') is not None:
            temp_model = ListSessionPackagesResponseBodyDataInstanceObject()
            self.instance_object = temp_model.from_map(m['InstanceObject'])
        if m.get('MaxHours') is not None:
            self.max_hours = m.get('MaxHours')
        if m.get('MaxSessions') is not None:
            self.max_sessions = m.get('MaxSessions')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('SessionPackageName') is not None:
            self.session_package_name = m.get('SessionPackageName')
        if m.get('SessionPackageTypeId') is not None:
            self.session_package_type_id = m.get('SessionPackageTypeId')
        if m.get('SessionSpec') is not None:
            self.session_spec = m.get('SessionSpec')
        if m.get('SessionUsageRate') is not None:
            self.session_usage_rate = m.get('SessionUsageRate')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UserIdentification') is not None:
            self.user_identification = m.get('UserIdentification')
        return self


class ListSessionPackagesResponseBody(TeaModel):
    def __init__(self, data=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.data = data  # type: list[ListSessionPackagesResponseBodyData]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSessionPackagesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSessionPackagesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSessionPackagesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSessionPackagesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSessionPackagesResponse, self).to_map()
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
            temp_model = ListSessionPackagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTenantConfigResponseBodyTenantConfigModel(TeaModel):
    def __init__(self, app_instance_group_expire_remind=None):
        self.app_instance_group_expire_remind = app_instance_group_expire_remind  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTenantConfigResponseBodyTenantConfigModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ListTenantConfigResponseBody(TeaModel):
    def __init__(self, request_id=None, tenant_config_model=None):
        self.request_id = request_id  # type: str
        self.tenant_config_model = tenant_config_model  # type: ListTenantConfigResponseBodyTenantConfigModel

    def validate(self):
        if self.tenant_config_model:
            self.tenant_config_model.validate()

    def to_map(self):
        _map = super(ListTenantConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tenant_config_model is not None:
            result['TenantConfigModel'] = self.tenant_config_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TenantConfigModel') is not None:
            temp_model = ListTenantConfigResponseBodyTenantConfigModel()
            self.tenant_config_model = temp_model.from_map(m['TenantConfigModel'])
        return self


class ListTenantConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTenantConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTenantConfigResponse, self).to_map()
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
            temp_model = ListTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogOffAllSessionsInAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogOffAllSessionsInAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class LogOffAllSessionsInAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogOffAllSessionsInAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LogOffAllSessionsInAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LogOffAllSessionsInAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LogOffAllSessionsInAppInstanceGroupResponse, self).to_map()
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
            temp_model = LogOffAllSessionsInAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateSessionPackageRequest(TeaModel):
    def __init__(self, dest_project_id=None, session_package_id=None, source_project_id=None):
        self.dest_project_id = dest_project_id  # type: str
        self.session_package_id = session_package_id  # type: str
        self.source_project_id = source_project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateSessionPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dest_project_id is not None:
            result['DestProjectId'] = self.dest_project_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        if self.source_project_id is not None:
            result['SourceProjectId'] = self.source_project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DestProjectId') is not None:
            self.dest_project_id = m.get('DestProjectId')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('SourceProjectId') is not None:
            self.source_project_id = m.get('SourceProjectId')
        return self


class MigrateSessionPackageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MigrateSessionPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

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


class MigrateSessionPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MigrateSessionPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MigrateSessionPackageResponse, self).to_map()
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
            temp_model = MigrateSessionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppInstanceGroupAttributeRequestNetworkDomainRules(TeaModel):
    def __init__(self, domain=None, policy=None):
        self.domain = domain  # type: str
        self.policy = policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequestNetworkDomainRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class ModifyAppInstanceGroupAttributeRequestNetwork(TeaModel):
    def __init__(self, domain_rules=None):
        self.domain_rules = domain_rules  # type: list[ModifyAppInstanceGroupAttributeRequestNetworkDomainRules]

    def validate(self):
        if self.domain_rules:
            for k in self.domain_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequestNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DomainRules'] = []
        if self.domain_rules is not None:
            for k in self.domain_rules:
                result['DomainRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.domain_rules = []
        if m.get('DomainRules') is not None:
            for k in m.get('DomainRules'):
                temp_model = ModifyAppInstanceGroupAttributeRequestNetworkDomainRules()
                self.domain_rules.append(temp_model.from_map(k))
        return self


class ModifyAppInstanceGroupAttributeRequestNodePool(TeaModel):
    def __init__(self, node_capacity=None, node_pool_id=None):
        self.node_capacity = node_capacity  # type: int
        self.node_pool_id = node_pool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequestNodePool, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_id is not None:
            result['NodePoolId'] = self.node_pool_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolId') is not None:
            self.node_pool_id = m.get('NodePoolId')
        return self


class ModifyAppInstanceGroupAttributeRequestSecurityPolicy(TeaModel):
    def __init__(self, reset_after_unbind=None, skip_user_auth_check=None):
        self.reset_after_unbind = reset_after_unbind  # type: bool
        self.skip_user_auth_check = skip_user_auth_check  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequestSecurityPolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reset_after_unbind is not None:
            result['ResetAfterUnbind'] = self.reset_after_unbind
        if self.skip_user_auth_check is not None:
            result['SkipUserAuthCheck'] = self.skip_user_auth_check
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResetAfterUnbind') is not None:
            self.reset_after_unbind = m.get('ResetAfterUnbind')
        if m.get('SkipUserAuthCheck') is not None:
            self.skip_user_auth_check = m.get('SkipUserAuthCheck')
        return self


class ModifyAppInstanceGroupAttributeRequestStoragePolicy(TeaModel):
    def __init__(self, storage_type_list=None):
        self.storage_type_list = storage_type_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequestStoragePolicy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storage_type_list is not None:
            result['StorageTypeList'] = self.storage_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StorageTypeList') is not None:
            self.storage_type_list = m.get('StorageTypeList')
        return self


class ModifyAppInstanceGroupAttributeRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_group_name=None, network=None, node_pool=None,
                 pre_open_app_id=None, pre_open_mode=None, product_type=None, security_policy=None, session_timeout=None,
                 storage_policy=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.network = network  # type: ModifyAppInstanceGroupAttributeRequestNetwork
        self.node_pool = node_pool  # type: ModifyAppInstanceGroupAttributeRequestNodePool
        self.pre_open_app_id = pre_open_app_id  # type: str
        self.pre_open_mode = pre_open_mode  # type: str
        self.product_type = product_type  # type: str
        self.security_policy = security_policy  # type: ModifyAppInstanceGroupAttributeRequestSecurityPolicy
        self.session_timeout = session_timeout  # type: int
        self.storage_policy = storage_policy  # type: ModifyAppInstanceGroupAttributeRequestStoragePolicy

    def validate(self):
        if self.network:
            self.network.validate()
        if self.node_pool:
            self.node_pool.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.storage_policy:
            self.storage_policy.validate()

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.node_pool is not None:
            result['NodePool'] = self.node_pool.to_map()
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy is not None:
            result['StoragePolicy'] = self.storage_policy.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('Network') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('NodePool') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestNodePool()
            self.node_pool = temp_model.from_map(m['NodePool'])
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SecurityPolicy') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m['SecurityPolicy'])
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            temp_model = ModifyAppInstanceGroupAttributeRequestStoragePolicy()
            self.storage_policy = temp_model.from_map(m['StoragePolicy'])
        return self


class ModifyAppInstanceGroupAttributeShrinkRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_group_name=None, network_shrink=None,
                 node_pool_shrink=None, pre_open_app_id=None, pre_open_mode=None, product_type=None, security_policy_shrink=None,
                 session_timeout=None, storage_policy_shrink=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_group_name = app_instance_group_name  # type: str
        self.network_shrink = network_shrink  # type: str
        self.node_pool_shrink = node_pool_shrink  # type: str
        self.pre_open_app_id = pre_open_app_id  # type: str
        self.pre_open_mode = pre_open_mode  # type: str
        self.product_type = product_type  # type: str
        self.security_policy_shrink = security_policy_shrink  # type: str
        self.session_timeout = session_timeout  # type: int
        self.storage_policy_shrink = storage_policy_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_group_name is not None:
            result['AppInstanceGroupName'] = self.app_instance_group_name
        if self.network_shrink is not None:
            result['Network'] = self.network_shrink
        if self.node_pool_shrink is not None:
            result['NodePool'] = self.node_pool_shrink
        if self.pre_open_app_id is not None:
            result['PreOpenAppId'] = self.pre_open_app_id
        if self.pre_open_mode is not None:
            result['PreOpenMode'] = self.pre_open_mode
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.security_policy_shrink is not None:
            result['SecurityPolicy'] = self.security_policy_shrink
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.storage_policy_shrink is not None:
            result['StoragePolicy'] = self.storage_policy_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceGroupName') is not None:
            self.app_instance_group_name = m.get('AppInstanceGroupName')
        if m.get('Network') is not None:
            self.network_shrink = m.get('Network')
        if m.get('NodePool') is not None:
            self.node_pool_shrink = m.get('NodePool')
        if m.get('PreOpenAppId') is not None:
            self.pre_open_app_id = m.get('PreOpenAppId')
        if m.get('PreOpenMode') is not None:
            self.pre_open_mode = m.get('PreOpenMode')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('SecurityPolicy') is not None:
            self.security_policy_shrink = m.get('SecurityPolicy')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('StoragePolicy') is not None:
            self.storage_policy_shrink = m.get('StoragePolicy')
        return self


class ModifyAppInstanceGroupAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppInstanceGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppInstanceGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppInstanceGroupAttributeResponse, self).to_map()
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
            temp_model = ModifyAppInstanceGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods(TeaModel):
    def __init__(self, amount=None, end_time=None, start_time=None):
        # 资源数量。
        self.amount = amount  # type: int
        # 结束时间。格式为HH:mm。
        self.end_time = end_time  # type: str
        # 开始时间。格式为HH:mm。
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules(TeaModel):
    def __init__(self, recurrence_type=None, recurrence_values=None, timer_periods=None):
        # 策略执行周期的类型。必须同时指定`RecurrenceType`和`RecurrenceValues`。
        self.recurrence_type = recurrence_type  # type: str
        # 策略执行周期的数值列表。
        self.recurrence_values = recurrence_values  # type: list[int]
        # 策略执行周期的时间段列表。时间段设置要求：
        # 
        # - 最多可添加3个时间段。
        # - 时间段之间不重叠。
        # - 时间段之间的间隔大于或等于5分钟。
        # - 单个时间段的时长大于或等于15分钟。
        # - 所有时间段累计不跨天。
        self.timer_periods = timer_periods  # type: list[ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods]

    def validate(self):
        if self.timer_periods:
            for k in self.timer_periods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type
        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values
        result['TimerPeriods'] = []
        if self.timer_periods is not None:
            for k in self.timer_periods:
                result['TimerPeriods'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')
        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')
        self.timer_periods = []
        if m.get('TimerPeriods') is not None:
            for k in m.get('TimerPeriods'):
                temp_model = ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedulesTimerPeriods()
                self.timer_periods.append(temp_model.from_map(k))
        return self


class ModifyNodePoolAttributeRequestNodePoolStrategy(TeaModel):
    def __init__(self, max_scaling_amount=None, node_amount=None, recurrence_schedules=None,
                 scaling_down_after_idle_minutes=None, scaling_step=None, scaling_usage_threshold=None, strategy_disable_date=None,
                 strategy_enable_date=None, strategy_type=None, warm_up=None):
        self.max_scaling_amount = max_scaling_amount  # type: int
        # 购买资源的数量。取值范围：1~100。
        # 
        # > 
        # - 若为包年包月资源，则该参数不可修改。
        # - 若为按量付费资源，则当弹性模式（`StrategyType`）为固定数量（`NODE_FIXED`）或自动扩缩容（`NODE_SCALING_BY_USAGE`）时该参数可修改。
        self.node_amount = node_amount  # type: int
        # 策略执行周期列表。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.recurrence_schedules = recurrence_schedules  # type: list[ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules]
        self.scaling_down_after_idle_minutes = scaling_down_after_idle_minutes  # type: int
        self.scaling_step = scaling_step  # type: int
        self.scaling_usage_threshold = scaling_usage_threshold  # type: str
        # 策略失效日期。格式为：yyyy-MM-dd。失效日期与生效日期的间隔必须介于7天到1年之间（含7天和1年）。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.strategy_disable_date = strategy_disable_date  # type: str
        # 策略生效日期。格式为：yyyy-MM-dd。该日期必须大于或等于当前日期。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.strategy_enable_date = strategy_enable_date  # type: str
        self.strategy_type = strategy_type  # type: str
        # 是否开启资源预热策略。`StrategyType`（弹性模式）设为`NODE_SCALING_BY_SCHEDULE`（定时扩缩容）时，该字段必填。
        self.warm_up = warm_up  # type: bool

    def validate(self):
        if self.recurrence_schedules:
            for k in self.recurrence_schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyNodePoolAttributeRequestNodePoolStrategy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_scaling_amount is not None:
            result['MaxScalingAmount'] = self.max_scaling_amount
        if self.node_amount is not None:
            result['NodeAmount'] = self.node_amount
        result['RecurrenceSchedules'] = []
        if self.recurrence_schedules is not None:
            for k in self.recurrence_schedules:
                result['RecurrenceSchedules'].append(k.to_map() if k else None)
        if self.scaling_down_after_idle_minutes is not None:
            result['ScalingDownAfterIdleMinutes'] = self.scaling_down_after_idle_minutes
        if self.scaling_step is not None:
            result['ScalingStep'] = self.scaling_step
        if self.scaling_usage_threshold is not None:
            result['ScalingUsageThreshold'] = self.scaling_usage_threshold
        if self.strategy_disable_date is not None:
            result['StrategyDisableDate'] = self.strategy_disable_date
        if self.strategy_enable_date is not None:
            result['StrategyEnableDate'] = self.strategy_enable_date
        if self.strategy_type is not None:
            result['StrategyType'] = self.strategy_type
        if self.warm_up is not None:
            result['WarmUp'] = self.warm_up
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxScalingAmount') is not None:
            self.max_scaling_amount = m.get('MaxScalingAmount')
        if m.get('NodeAmount') is not None:
            self.node_amount = m.get('NodeAmount')
        self.recurrence_schedules = []
        if m.get('RecurrenceSchedules') is not None:
            for k in m.get('RecurrenceSchedules'):
                temp_model = ModifyNodePoolAttributeRequestNodePoolStrategyRecurrenceSchedules()
                self.recurrence_schedules.append(temp_model.from_map(k))
        if m.get('ScalingDownAfterIdleMinutes') is not None:
            self.scaling_down_after_idle_minutes = m.get('ScalingDownAfterIdleMinutes')
        if m.get('ScalingStep') is not None:
            self.scaling_step = m.get('ScalingStep')
        if m.get('ScalingUsageThreshold') is not None:
            self.scaling_usage_threshold = m.get('ScalingUsageThreshold')
        if m.get('StrategyDisableDate') is not None:
            self.strategy_disable_date = m.get('StrategyDisableDate')
        if m.get('StrategyEnableDate') is not None:
            self.strategy_enable_date = m.get('StrategyEnableDate')
        if m.get('StrategyType') is not None:
            self.strategy_type = m.get('StrategyType')
        if m.get('WarmUp') is not None:
            self.warm_up = m.get('WarmUp')
        return self


class ModifyNodePoolAttributeRequest(TeaModel):
    def __init__(self, biz_region_id=None, node_capacity=None, node_pool_strategy=None, pool_id=None,
                 product_type=None):
        self.biz_region_id = biz_region_id  # type: str
        self.node_capacity = node_capacity  # type: int
        self.node_pool_strategy = node_pool_strategy  # type: ModifyNodePoolAttributeRequestNodePoolStrategy
        self.pool_id = pool_id  # type: str
        # 产品类型。
        self.product_type = product_type  # type: str

    def validate(self):
        if self.node_pool_strategy:
            self.node_pool_strategy.validate()

    def to_map(self):
        _map = super(ModifyNodePoolAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy.to_map()
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            temp_model = ModifyNodePoolAttributeRequestNodePoolStrategy()
            self.node_pool_strategy = temp_model.from_map(m['NodePoolStrategy'])
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeShrinkRequest(TeaModel):
    def __init__(self, biz_region_id=None, node_capacity=None, node_pool_strategy_shrink=None, pool_id=None,
                 product_type=None):
        self.biz_region_id = biz_region_id  # type: str
        self.node_capacity = node_capacity  # type: int
        self.node_pool_strategy_shrink = node_pool_strategy_shrink  # type: str
        self.pool_id = pool_id  # type: str
        # 产品类型。
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodePoolAttributeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.node_capacity is not None:
            result['NodeCapacity'] = self.node_capacity
        if self.node_pool_strategy_shrink is not None:
            result['NodePoolStrategy'] = self.node_pool_strategy_shrink
        if self.pool_id is not None:
            result['PoolId'] = self.pool_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('NodeCapacity') is not None:
            self.node_capacity = m.get('NodeCapacity')
        if m.get('NodePoolStrategy') is not None:
            self.node_pool_strategy_shrink = m.get('NodePoolStrategy')
        if m.get('PoolId') is not None:
            self.pool_id = m.get('PoolId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class ModifyNodePoolAttributeResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyNodePoolAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyNodePoolAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyNodePoolAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyNodePoolAttributeResponse, self).to_map()
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
            temp_model = ModifyNodePoolAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProjectPolicyRequest(TeaModel):
    def __init__(self, clipboard=None, file_transfer=None, frame_rate=None, keep_alive_duration=None,
                 project_id=None, session_resolution_height=None, session_resolution_width=None, streaming_mode=None,
                 terminal_resolution_adaptation=None):
        self.clipboard = clipboard  # type: int
        self.file_transfer = file_transfer  # type: int
        self.frame_rate = frame_rate  # type: int
        self.keep_alive_duration = keep_alive_duration  # type: int
        self.project_id = project_id  # type: str
        self.session_resolution_height = session_resolution_height  # type: int
        self.session_resolution_width = session_resolution_width  # type: int
        self.streaming_mode = streaming_mode  # type: str
        self.terminal_resolution_adaptation = terminal_resolution_adaptation  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProjectPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clipboard is not None:
            result['Clipboard'] = self.clipboard
        if self.file_transfer is not None:
            result['FileTransfer'] = self.file_transfer
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.keep_alive_duration is not None:
            result['KeepAliveDuration'] = self.keep_alive_duration
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.session_resolution_height is not None:
            result['SessionResolutionHeight'] = self.session_resolution_height
        if self.session_resolution_width is not None:
            result['SessionResolutionWidth'] = self.session_resolution_width
        if self.streaming_mode is not None:
            result['StreamingMode'] = self.streaming_mode
        if self.terminal_resolution_adaptation is not None:
            result['TerminalResolutionAdaptation'] = self.terminal_resolution_adaptation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Clipboard') is not None:
            self.clipboard = m.get('Clipboard')
        if m.get('FileTransfer') is not None:
            self.file_transfer = m.get('FileTransfer')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('KeepAliveDuration') is not None:
            self.keep_alive_duration = m.get('KeepAliveDuration')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('SessionResolutionHeight') is not None:
            self.session_resolution_height = m.get('SessionResolutionHeight')
        if m.get('SessionResolutionWidth') is not None:
            self.session_resolution_width = m.get('SessionResolutionWidth')
        if m.get('StreamingMode') is not None:
            self.streaming_mode = m.get('StreamingMode')
        if m.get('TerminalResolutionAdaptation') is not None:
            self.terminal_resolution_adaptation = m.get('TerminalResolutionAdaptation')
        return self


class ModifyProjectPolicyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProjectPolicyResponseBody, self).to_map()
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


class ModifyProjectPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyProjectPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProjectPolicyResponse, self).to_map()
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
            temp_model = ModifyProjectPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTenantConfigRequest(TeaModel):
    def __init__(self, app_instance_group_expire_remind=None):
        self.app_instance_group_expire_remind = app_instance_group_expire_remind  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_expire_remind is not None:
            result['AppInstanceGroupExpireRemind'] = self.app_instance_group_expire_remind
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupExpireRemind') is not None:
            self.app_instance_group_expire_remind = m.get('AppInstanceGroupExpireRemind')
        return self


class ModifyTenantConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyTenantConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyTenantConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyTenantConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyTenantConfigResponse, self).to_map()
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
            temp_model = ModifyTenantConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageListAppInstanceGroupUserRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, page_number=None, page_size=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageListAppInstanceGroupUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class PageListAppInstanceGroupUserResponseBody(TeaModel):
    def __init__(self, request_id=None, users=None):
        self.request_id = request_id  # type: str
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageListAppInstanceGroupUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class PageListAppInstanceGroupUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PageListAppInstanceGroupUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageListAppInstanceGroupUserResponse, self).to_map()
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
            temp_model = PageListAppInstanceGroupUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshAccessUrlRequest(TeaModel):
    def __init__(self, access_page_id=None):
        self.access_page_id = access_page_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshAccessUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        return self


class RefreshAccessUrlResponseBody(TeaModel):
    def __init__(self, access_url=None, code=None, message=None, request_id=None, success=None):
        self.access_url = access_url  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshAccessUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_url is not None:
            result['AccessUrl'] = self.access_url
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
        if m.get('AccessUrl') is not None:
            self.access_url = m.get('AccessUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshAccessUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshAccessUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshAccessUrlResponse, self).to_map()
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
            temp_model = RefreshAccessUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewAppInstanceGroupRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, auto_pay=None, period=None, period_unit=None, product_type=None,
                 promotion_id=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.auto_pay = auto_pay  # type: bool
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.product_type = product_type  # type: str
        self.promotion_id = promotion_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAppInstanceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.promotion_id is not None:
            result['PromotionId'] = self.promotion_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('PromotionId') is not None:
            self.promotion_id = m.get('PromotionId')
        return self


class RenewAppInstanceGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, order_id=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewAppInstanceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RenewAppInstanceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewAppInstanceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewAppInstanceGroupResponse, self).to_map()
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
            temp_model = RenewAppInstanceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewSessionPackageRequest(TeaModel):
    def __init__(self, period=None, period_unit=None, session_package_id=None):
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        self.session_package_id = session_package_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewSessionPackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        return self


class RenewSessionPackageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, session_package_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.session_package_id = session_package_id  # type: long
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewSessionPackageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_package_id is not None:
            result['SessionPackageId'] = self.session_package_id
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
        if m.get('SessionPackageId') is not None:
            self.session_package_id = m.get('SessionPackageId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewSessionPackageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewSessionPackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewSessionPackageResponse, self).to_map()
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
            temp_model = RenewSessionPackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindRequest(TeaModel):
    def __init__(self, app_instance_group_id=None, app_instance_id=None, app_instance_persistent_id=None,
                 end_user_id=None, product_type=None):
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.app_instance_id = app_instance_id  # type: str
        self.app_instance_persistent_id = app_instance_persistent_id  # type: str
        self.end_user_id = end_user_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_instance_persistent_id is not None:
            result['AppInstancePersistentId'] = self.app_instance_persistent_id
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppInstancePersistentId') is not None:
            self.app_instance_persistent_id = m.get('AppInstancePersistentId')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class UnbindResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindResponse, self).to_map()
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
            temp_model = UnbindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAccessPageStateRequest(TeaModel):
    def __init__(self, access_page_id=None, access_page_state=None):
        self.access_page_id = access_page_id  # type: str
        self.access_page_state = access_page_state  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccessPageStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_page_id is not None:
            result['AccessPageId'] = self.access_page_id
        if self.access_page_state is not None:
            result['AccessPageState'] = self.access_page_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessPageId') is not None:
            self.access_page_id = m.get('AccessPageId')
        if m.get('AccessPageState') is not None:
            self.access_page_state = m.get('AccessPageState')
        return self


class UpdateAccessPageStateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAccessPageStateResponseBody, self).to_map()
        if _map is not None:
            return _map

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


class UpdateAccessPageStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAccessPageStateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAccessPageStateResponse, self).to_map()
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
            temp_model = UpdateAccessPageStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppInstanceGroupImageRequest(TeaModel):
    def __init__(self, app_center_image_id=None, app_instance_group_id=None, biz_region_id=None, product_type=None):
        self.app_center_image_id = app_center_image_id  # type: str
        self.app_instance_group_id = app_instance_group_id  # type: str
        self.biz_region_id = biz_region_id  # type: str
        self.product_type = product_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppInstanceGroupImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_center_image_id is not None:
            result['AppCenterImageId'] = self.app_center_image_id
        if self.app_instance_group_id is not None:
            result['AppInstanceGroupId'] = self.app_instance_group_id
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCenterImageId') is not None:
            self.app_center_image_id = m.get('AppCenterImageId')
        if m.get('AppInstanceGroupId') is not None:
            self.app_instance_group_id = m.get('AppInstanceGroupId')
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        return self


class UpdateAppInstanceGroupImageResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppInstanceGroupImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppInstanceGroupImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppInstanceGroupImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppInstanceGroupImageResponse, self).to_map()
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
            temp_model = UpdateAppInstanceGroupImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


