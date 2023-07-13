# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetDeviceInfoRequest(TeaModel):
    def __init__(self, device_id=None, ds=None, factory_id=None):
        self.device_id = device_id  # type: str
        self.ds = ds  # type: str
        self.factory_id = factory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.ds is not None:
            result['ds'] = self.ds
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('ds') is not None:
            self.ds = m.get('ds')
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        return self


class GetDeviceInfoResponseBodyDataRecordList(TeaModel):
    def __init__(self, identifier=None, param_name=None, statistics_date=None, type=None, unit=None, value=None):
        self.identifier = identifier  # type: str
        self.param_name = param_name  # type: str
        self.statistics_date = statistics_date  # type: str
        self.type = type  # type: str
        self.unit = unit  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceInfoResponseBodyDataRecordList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.param_name is not None:
            result['paramName'] = self.param_name
        if self.statistics_date is not None:
            result['statisticsDate'] = self.statistics_date
        if self.type is not None:
            result['type'] = self.type
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('paramName') is not None:
            self.param_name = m.get('paramName')
        if m.get('statisticsDate') is not None:
            self.statistics_date = m.get('statisticsDate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetDeviceInfoResponseBodyData(TeaModel):
    def __init__(self, device_id=None, device_name=None, first_type_name=None, record_list=None,
                 second_type_name=None):
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.first_type_name = first_type_name  # type: str
        self.record_list = record_list  # type: list[GetDeviceInfoResponseBodyDataRecordList]
        self.second_type_name = second_type_name  # type: str

    def validate(self):
        if self.record_list:
            for k in self.record_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDeviceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name
        result['recordList'] = []
        if self.record_list is not None:
            for k in self.record_list:
                result['recordList'].append(k.to_map() if k else None)
        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')
        self.record_list = []
        if m.get('recordList') is not None:
            for k in m.get('recordList'):
                temp_model = GetDeviceInfoResponseBodyDataRecordList()
                self.record_list.append(temp_model.from_map(k))
        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')
        return self


class GetDeviceInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetDeviceInfoResponseBodyData
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceInfoResponse, self).to_map()
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
            temp_model = GetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceListRequest(TeaModel):
    def __init__(self, factory_id=None):
        self.factory_id = factory_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        return self


class GetDeviceListResponseBodyDataDeviceListInfo(TeaModel):
    def __init__(self, const_kva=None, ct=None, magnification=None, pressure=None, pt=None):
        self.const_kva = const_kva  # type: int
        self.ct = ct  # type: int
        self.magnification = magnification  # type: int
        self.pressure = pressure  # type: int
        self.pt = pt  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceListResponseBodyDataDeviceListInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.const_kva is not None:
            result['constKva'] = self.const_kva
        if self.ct is not None:
            result['ct'] = self.ct
        if self.magnification is not None:
            result['magnification'] = self.magnification
        if self.pressure is not None:
            result['pressure'] = self.pressure
        if self.pt is not None:
            result['pt'] = self.pt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('constKva') is not None:
            self.const_kva = m.get('constKva')
        if m.get('ct') is not None:
            self.ct = m.get('ct')
        if m.get('magnification') is not None:
            self.magnification = m.get('magnification')
        if m.get('pressure') is not None:
            self.pressure = m.get('pressure')
        if m.get('pt') is not None:
            self.pt = m.get('pt')
        return self


class GetDeviceListResponseBodyDataDeviceList(TeaModel):
    def __init__(self, device_id=None, device_name=None, first_type_name=None, info=None, parent_device=None,
                 second_type_name=None):
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.first_type_name = first_type_name  # type: str
        self.info = info  # type: GetDeviceListResponseBodyDataDeviceListInfo
        self.parent_device = parent_device  # type: str
        self.second_type_name = second_type_name  # type: str

    def validate(self):
        if self.info:
            self.info.validate()

    def to_map(self):
        _map = super(GetDeviceListResponseBodyDataDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.device_name is not None:
            result['deviceName'] = self.device_name
        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name
        if self.info is not None:
            result['info'] = self.info.to_map()
        if self.parent_device is not None:
            result['parentDevice'] = self.parent_device
        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')
        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')
        if m.get('info') is not None:
            temp_model = GetDeviceListResponseBodyDataDeviceListInfo()
            self.info = temp_model.from_map(m['info'])
        if m.get('parentDevice') is not None:
            self.parent_device = m.get('parentDevice')
        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')
        return self


class GetDeviceListResponseBodyData(TeaModel):
    def __init__(self, code=None, device_list=None, factory_id=None, http_code=None, success=None):
        self.code = code  # type: str
        self.device_list = device_list  # type: list[GetDeviceListResponseBodyDataDeviceList]
        self.factory_id = factory_id  # type: str
        self.http_code = http_code  # type: int
        self.success = success  # type: bool

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDeviceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['deviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['deviceList'].append(k.to_map() if k else None)
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.device_list = []
        if m.get('deviceList') is not None:
            for k in m.get('deviceList'):
                temp_model = GetDeviceListResponseBodyDataDeviceList()
                self.device_list.append(temp_model.from_map(k))
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetDeviceListResponseBodyData
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeviceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDeviceListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetDeviceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceListResponse, self).to_map()
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
            temp_model = GetDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOrgAndFactoryResponseBodyDataFactoryList(TeaModel):
    def __init__(self, factory_id=None, factory_name=None):
        self.factory_id = factory_id  # type: str
        self.factory_name = factory_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOrgAndFactoryResponseBodyDataFactoryList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.factory_id is not None:
            result['factoryId'] = self.factory_id
        if self.factory_name is not None:
            result['factoryName'] = self.factory_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')
        if m.get('factoryName') is not None:
            self.factory_name = m.get('factoryName')
        return self


class GetOrgAndFactoryResponseBodyData(TeaModel):
    def __init__(self, aliyun_pk=None, factory_list=None, organization_id=None, organization_name=None):
        self.aliyun_pk = aliyun_pk  # type: str
        self.factory_list = factory_list  # type: list[GetOrgAndFactoryResponseBodyDataFactoryList]
        self.organization_id = organization_id  # type: str
        self.organization_name = organization_name  # type: str

    def validate(self):
        if self.factory_list:
            for k in self.factory_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOrgAndFactoryResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliyun_pk is not None:
            result['aliyunPk'] = self.aliyun_pk
        result['factoryList'] = []
        if self.factory_list is not None:
            for k in self.factory_list:
                result['factoryList'].append(k.to_map() if k else None)
        if self.organization_id is not None:
            result['organizationId'] = self.organization_id
        if self.organization_name is not None:
            result['organizationName'] = self.organization_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('aliyunPk') is not None:
            self.aliyun_pk = m.get('aliyunPk')
        self.factory_list = []
        if m.get('factoryList') is not None:
            for k in m.get('factoryList'):
                temp_model = GetOrgAndFactoryResponseBodyDataFactoryList()
                self.factory_list.append(temp_model.from_map(k))
        if m.get('organizationId') is not None:
            self.organization_id = m.get('organizationId')
        if m.get('organizationName') is not None:
            self.organization_name = m.get('organizationName')
        return self


class GetOrgAndFactoryResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_code=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetOrgAndFactoryResponseBodyData]
        self.http_code = http_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetOrgAndFactoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_code is not None:
            result['httpCode'] = self.http_code
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetOrgAndFactoryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetOrgAndFactoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOrgAndFactoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOrgAndFactoryResponse, self).to_map()
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
            temp_model = GetOrgAndFactoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


