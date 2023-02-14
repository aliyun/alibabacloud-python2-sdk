# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CorrectAddressRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CorrectAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class CorrectAddressResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CorrectAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CorrectAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CorrectAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CorrectAddressResponse, self).to_map()
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
            temp_model = CorrectAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractAddressRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ExtractAddressResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExtractAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtractAddressResponse, self).to_map()
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
            temp_model = ExtractAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractNameRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ExtractNameResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExtractNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtractNameResponse, self).to_map()
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
            temp_model = ExtractNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractPhoneRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractPhoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class ExtractPhoneResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractPhoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExtractPhoneResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExtractPhoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtractPhoneResponse, self).to_map()
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
            temp_model = ExtractPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressDivisionCodeRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressDivisionCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetAddressDivisionCodeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressDivisionCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAddressDivisionCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAddressDivisionCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAddressDivisionCodeResponse, self).to_map()
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
            temp_model = GetAddressDivisionCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressSimilarityRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressSimilarityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetAddressSimilarityResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressSimilarityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAddressSimilarityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAddressSimilarityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAddressSimilarityResponse, self).to_map()
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
            temp_model = GetAddressSimilarityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetZipcodeRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetZipcodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetZipcodeResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetZipcodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetZipcodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetZipcodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetZipcodeResponse, self).to_map()
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
            temp_model = GetZipcodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StructureAddressRequest(TeaModel):
    def __init__(self, app_key=None, default_city=None, default_district=None, default_province=None,
                 service_code=None, text=None):
        self.app_key = app_key  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.default_province = default_province  # type: str
        self.service_code = service_code  # type: str
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StructureAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class StructureAddressResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: str
        # RequestId
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StructureAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StructureAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StructureAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StructureAddressResponse, self).to_map()
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
            temp_model = StructureAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


