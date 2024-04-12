# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetOpenStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOpenStatusResponseBody, self).to_map()
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


class GetOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOpenStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOpenStatusResponse, self).to_map()
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
            temp_model = GetOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderInfoRequest(TeaModel):
    def __init__(self, rel_service=None, resource_type=None):
        self.rel_service = rel_service  # type: str
        self.resource_type = resource_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrderInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rel_service is not None:
            result['RelService'] = self.rel_service
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RelService') is not None:
            self.rel_service = m.get('RelService')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetOrderInfoResponseBodyData(TeaModel):
    def __init__(self, biz_type=None, current_concurrency=None, current_days=None, instance_id=None,
                 license_key=None, remark=None, total_days=None):
        self.biz_type = biz_type  # type: str
        self.current_concurrency = current_concurrency  # type: int
        self.current_days = current_days  # type: int
        self.instance_id = instance_id  # type: str
        self.license_key = license_key  # type: str
        self.remark = remark  # type: str
        self.total_days = total_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrderInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.current_concurrency is not None:
            result['currentConcurrency'] = self.current_concurrency
        if self.current_days is not None:
            result['currentDays'] = self.current_days
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.license_key is not None:
            result['licenseKey'] = self.license_key
        if self.remark is not None:
            result['remark'] = self.remark
        if self.total_days is not None:
            result['totalDays'] = self.total_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('currentConcurrency') is not None:
            self.current_concurrency = m.get('currentConcurrency')
        if m.get('currentDays') is not None:
            self.current_days = m.get('currentDays')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('licenseKey') is not None:
            self.license_key = m.get('licenseKey')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        if m.get('totalDays') is not None:
            self.total_days = m.get('totalDays')
        return self


class GetOrderInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetOrderInfoResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOrderInfoResponseBody, self).to_map()
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
                temp_model = GetOrderInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrderInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrderInfoResponse, self).to_map()
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
            temp_model = GetOrderInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrderUsageRequest(TeaModel):
    def __init__(self, license_key=None, rel_service=None, resource_type=None, time_range=None):
        self.license_key = license_key  # type: str
        self.rel_service = rel_service  # type: str
        self.resource_type = resource_type  # type: int
        self.time_range = time_range  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrderUsageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license_key is not None:
            result['LicenseKey'] = self.license_key
        if self.rel_service is not None:
            result['RelService'] = self.rel_service
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.time_range is not None:
            result['TimeRange'] = self.time_range
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LicenseKey') is not None:
            self.license_key = m.get('LicenseKey')
        if m.get('RelService') is not None:
            self.rel_service = m.get('RelService')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TimeRange') is not None:
            self.time_range = m.get('TimeRange')
        return self


class GetOrderUsageResponseBody(TeaModel):
    def __init__(self, data=None, message=None, request_id=None, success=None):
        self.data = data  # type: list[dict[str, any]]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrderUsageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOrderUsageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrderUsageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrderUsageResponse, self).to_map()
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
            temp_model = GetOrderUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


