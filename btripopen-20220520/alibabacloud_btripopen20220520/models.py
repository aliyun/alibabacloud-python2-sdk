# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AccessTokenRequest(TeaModel):
    def __init__(self, app_key=None, app_secret=None):
        # 应用的appKey
        self.app_key = app_key  # type: str
        # 应用的appSecret
        self.app_secret = app_secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccessTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['app_key'] = self.app_key
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('app_key') is not None:
            self.app_key = m.get('app_key')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        return self


class AccessTokenResponseBodyData(TeaModel):
    def __init__(self, expire=None, token=None):
        # 过期时间，单位ms
        self.expire = expire  # type: long
        # 令牌
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AccessTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire is not None:
            result['expire'] = self.expire
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class AccessTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, trace_id=None):
        # 错误码
        self.code = code  # type: str
        self.data = data  # type: AccessTokenResponseBodyData
        # 错误信息
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AccessTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.trace_id is not None:
            result['traceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AccessTokenResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('traceId') is not None:
            self.trace_id = m.get('traceId')
        return self


class AccessTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AccessTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AccessTokenResponse, self).to_map()
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
            temp_model = AccessTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


