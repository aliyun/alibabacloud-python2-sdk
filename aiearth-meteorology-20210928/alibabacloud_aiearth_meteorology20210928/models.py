# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GridQueryRequest(TeaModel):
    def __init__(self, element=None, forecast_timestamp=None, latitude=None, longitude=None, page_no=None,
                 page_size=None, product=None, report_timestamp=None):
        self.element = element  # type: str
        self.forecast_timestamp = forecast_timestamp  # type: str
        self.latitude = latitude  # type: float
        self.longitude = longitude  # type: float
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.product = product  # type: str
        self.report_timestamp = report_timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GridQueryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.element is not None:
            result['element'] = self.element
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.product is not None:
            result['product'] = self.product
        if self.report_timestamp is not None:
            result['reportTimestamp'] = self.report_timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('reportTimestamp') is not None:
            self.report_timestamp = m.get('reportTimestamp')
        return self


class GridQueryResponseBodyModuleList(TeaModel):
    def __init__(self, data_type=None, element=None, element_unit=None, forecast_timestamp=None, latitude=None,
                 longitude=None, report_timestamp=None, value=None):
        self.data_type = data_type  # type: str
        self.element = element  # type: str
        self.element_unit = element_unit  # type: str
        self.forecast_timestamp = forecast_timestamp  # type: str
        self.latitude = latitude  # type: float
        self.longitude = longitude  # type: float
        self.report_timestamp = report_timestamp  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GridQueryResponseBodyModuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.element is not None:
            result['element'] = self.element
        if self.element_unit is not None:
            result['elementUnit'] = self.element_unit
        if self.forecast_timestamp is not None:
            result['forecastTimestamp'] = self.forecast_timestamp
        if self.latitude is not None:
            result['latitude'] = self.latitude
        if self.longitude is not None:
            result['longitude'] = self.longitude
        if self.report_timestamp is not None:
            result['reportTimestamp'] = self.report_timestamp
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('element') is not None:
            self.element = m.get('element')
        if m.get('elementUnit') is not None:
            self.element_unit = m.get('elementUnit')
        if m.get('forecastTimestamp') is not None:
            self.forecast_timestamp = m.get('forecastTimestamp')
        if m.get('latitude') is not None:
            self.latitude = m.get('latitude')
        if m.get('longitude') is not None:
            self.longitude = m.get('longitude')
        if m.get('reportTimestamp') is not None:
            self.report_timestamp = m.get('reportTimestamp')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GridQueryResponseBodyModule(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None):
        self.list = list  # type: list[GridQueryResponseBodyModuleList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GridQueryResponseBodyModule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = GridQueryResponseBodyModuleList()
                self.list.append(temp_model.from_map(k))
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GridQueryResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None, success=None):
        self.code = code  # type: long
        self.message = message  # type: str
        self.module = module  # type: GridQueryResponseBodyModule
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super(GridQueryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('module') is not None:
            temp_model = GridQueryResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GridQueryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GridQueryResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GridQueryResponse, self).to_map()
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
            temp_model = GridQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


