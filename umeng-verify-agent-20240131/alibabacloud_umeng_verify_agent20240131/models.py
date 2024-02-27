# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateRequest(TeaModel):
    def __init__(self, app_name=None, bundle_id=None, pack_name=None, platform=None, scheme_name=None,
                 sign_name=None):
        self.app_name = app_name  # type: str
        self.bundle_id = bundle_id  # type: str
        self.pack_name = pack_name  # type: str
        self.platform = platform  # type: str
        self.scheme_name = scheme_name  # type: str
        self.sign_name = sign_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.bundle_id is not None:
            result['bundleId'] = self.bundle_id
        if self.pack_name is not None:
            result['packName'] = self.pack_name
        if self.platform is not None:
            result['platform'] = self.platform
        if self.scheme_name is not None:
            result['schemeName'] = self.scheme_name
        if self.sign_name is not None:
            result['signName'] = self.sign_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('bundleId') is not None:
            self.bundle_id = m.get('bundleId')
        if m.get('packName') is not None:
            self.pack_name = m.get('packName')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('schemeName') is not None:
            self.scheme_name = m.get('schemeName')
        if m.get('signName') is not None:
            self.sign_name = m.get('signName')
        return self


class CreateResponseBodyData(TeaModel):
    def __init__(self, scheme_code=None):
        self.scheme_code = scheme_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_code is not None:
            result['schemeCode'] = self.scheme_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schemeCode') is not None:
            self.scheme_code = m.get('schemeCode')
        return self


class CreateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
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
            temp_model = CreateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResponse, self).to_map()
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
            temp_model = CreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMobileWithTokenRequest(TeaModel):
    def __init__(self, api_code=None, operator_id=None, os_type=None, scheme_code=None, token=None):
        self.api_code = api_code  # type: int
        self.operator_id = operator_id  # type: int
        self.os_type = os_type  # type: str
        self.scheme_code = scheme_code  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMobileWithTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_code is not None:
            result['apiCode'] = self.api_code
        if self.operator_id is not None:
            result['operatorId'] = self.operator_id
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.scheme_code is not None:
            result['schemeCode'] = self.scheme_code
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('apiCode') is not None:
            self.api_code = m.get('apiCode')
        if m.get('operatorId') is not None:
            self.operator_id = m.get('operatorId')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('schemeCode') is not None:
            self.scheme_code = m.get('schemeCode')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetMobileWithTokenResponseBodyData(TeaModel):
    def __init__(self, mobile=None):
        self.mobile = mobile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMobileWithTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mobile is not None:
            result['mobile'] = self.mobile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('mobile') is not None:
            self.mobile = m.get('mobile')
        return self


class GetMobileWithTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetMobileWithTokenResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMobileWithTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
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
            temp_model = GetMobileWithTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetMobileWithTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMobileWithTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMobileWithTokenResponse, self).to_map()
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
            temp_model = GetMobileWithTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAppInfoBySchemeRequest(TeaModel):
    def __init__(self, scheme_code=None):
        self.scheme_code = scheme_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAppInfoBySchemeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme_code is not None:
            result['schemeCode'] = self.scheme_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('schemeCode') is not None:
            self.scheme_code = m.get('schemeCode')
        return self


class QueryAppInfoBySchemeResponseBodyData(TeaModel):
    def __init__(self, cm_app_id=None, cm_app_key=None, ct_app_id=None, ct_app_key=None, cu_app_id=None,
                 cu_app_key=None, cu_rsa_publick_key=None):
        self.cm_app_id = cm_app_id  # type: str
        self.cm_app_key = cm_app_key  # type: str
        self.ct_app_id = ct_app_id  # type: str
        self.ct_app_key = ct_app_key  # type: str
        self.cu_app_id = cu_app_id  # type: str
        self.cu_app_key = cu_app_key  # type: str
        self.cu_rsa_publick_key = cu_rsa_publick_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAppInfoBySchemeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cm_app_id is not None:
            result['cmAppId'] = self.cm_app_id
        if self.cm_app_key is not None:
            result['cmAppKey'] = self.cm_app_key
        if self.ct_app_id is not None:
            result['ctAppId'] = self.ct_app_id
        if self.ct_app_key is not None:
            result['ctAppKey'] = self.ct_app_key
        if self.cu_app_id is not None:
            result['cuAppId'] = self.cu_app_id
        if self.cu_app_key is not None:
            result['cuAppKey'] = self.cu_app_key
        if self.cu_rsa_publick_key is not None:
            result['cuRsaPublickKey'] = self.cu_rsa_publick_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cmAppId') is not None:
            self.cm_app_id = m.get('cmAppId')
        if m.get('cmAppKey') is not None:
            self.cm_app_key = m.get('cmAppKey')
        if m.get('ctAppId') is not None:
            self.ct_app_id = m.get('ctAppId')
        if m.get('ctAppKey') is not None:
            self.ct_app_key = m.get('ctAppKey')
        if m.get('cuAppId') is not None:
            self.cu_app_id = m.get('cuAppId')
        if m.get('cuAppKey') is not None:
            self.cu_app_key = m.get('cuAppKey')
        if m.get('cuRsaPublickKey') is not None:
            self.cu_rsa_publick_key = m.get('cuRsaPublickKey')
        return self


class QueryAppInfoBySchemeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, msg=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAppInfoBySchemeResponseBodyData
        self.msg = msg  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAppInfoBySchemeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
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
            temp_model = QueryAppInfoBySchemeResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryAppInfoBySchemeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAppInfoBySchemeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAppInfoBySchemeResponse, self).to_map()
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
            temp_model = QueryAppInfoBySchemeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


