# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetAddressDivisionCodeRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressDivisionCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressDivisionCodeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressDivisionCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressDivisionCodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAddressDivisionCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressDivisionCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StructureAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StructureAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class StructureAddressResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StructureAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class StructureAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StructureAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StructureAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractExpressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractExpressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractExpressResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractExpressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractExpressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExtractExpressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExtractExpressResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = ExtractExpressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractNameRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractNameResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractNameResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExtractNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressBlockMappingRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressBlockMappingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressBlockMappingResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressBlockMappingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressBlockMappingResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAddressBlockMappingResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAddressBlockMappingResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAddressBlockMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressSearchRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressSearchResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressSearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressSearchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAddressSearchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAddressSearchResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAddressSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictPOIRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictPOIRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class PredictPOIResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictPOIResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class PredictPOIResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PredictPOIResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PredictPOIResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = PredictPOIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClassifyPOIRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClassifyPOIRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ClassifyPOIResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClassifyPOIResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ClassifyPOIResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ClassifyPOIResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClassifyPOIResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = ClassifyPOIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CorrectAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CorrectAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CorrectAddressResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CorrectAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CorrectAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CorrectAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CorrectAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetZipcodeRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetZipcodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetZipcodeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetZipcodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetZipcodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetZipcodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetZipcodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompleteAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class CompleteAddressResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CompleteAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class CompleteAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CompleteAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CompleteAddressResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = CompleteAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressSimilarityRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressSimilarityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressSimilarityResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressSimilarityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressSimilarityResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAddressSimilarityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAddressSimilarityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressGeocodeRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressGeocodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressGeocodeResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressGeocodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressGeocodeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAddressGeocodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAddressGeocodeResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAddressGeocodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferCoordRequest(TeaModel):
    def __init__(self, service_code=None, text=None, src_coord=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.src_coord = src_coord  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferCoordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.src_coord is not None:
            result['SrcCoord'] = self.src_coord
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('SrcCoord') is not None:
            self.src_coord = m.get('SrcCoord')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class TransferCoordResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferCoordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class TransferCoordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TransferCoordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferCoordResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = TransferCoordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(self, service_code=None, parameters=None):
        self.service_code = service_code  # type: str
        self.parameters = parameters  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        return self


class UpdateProjectShrinkRequest(TeaModel):
    def __init__(self, service_code=None, parameters_shrink=None):
        self.service_code = service_code  # type: str
        self.parameters_shrink = parameters_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateProjectResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateProjectResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractPhoneRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractPhoneRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractPhoneResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractPhoneResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractPhoneResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExtractPhoneResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInputSearchRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInputSearchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetInputSearchResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInputSearchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetInputSearchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInputSearchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInputSearchResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = GetInputSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAddressEvaluateRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressEvaluateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class GetAddressEvaluateResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAddressEvaluateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetAddressEvaluateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAddressEvaluateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAddressEvaluateResponse, self).to_map()
        if _map is not None:
            return _map

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
            temp_model = GetAddressEvaluateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtractAddressRequest(TeaModel):
    def __init__(self, service_code=None, text=None, default_province=None, default_city=None,
                 default_district=None, app_key=None):
        self.service_code = service_code  # type: str
        self.text = text  # type: str
        self.default_province = default_province  # type: str
        self.default_city = default_city  # type: str
        self.default_district = default_district  # type: str
        self.app_key = app_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        if self.text is not None:
            result['Text'] = self.text
        if self.default_province is not None:
            result['DefaultProvince'] = self.default_province
        if self.default_city is not None:
            result['DefaultCity'] = self.default_city
        if self.default_district is not None:
            result['DefaultDistrict'] = self.default_district
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('DefaultProvince') is not None:
            self.default_province = m.get('DefaultProvince')
        if m.get('DefaultCity') is not None:
            self.default_city = m.get('DefaultCity')
        if m.get('DefaultDistrict') is not None:
            self.default_district = m.get('DefaultDistrict')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ExtractAddressResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExtractAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ExtractAddressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExtractAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExtractAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


