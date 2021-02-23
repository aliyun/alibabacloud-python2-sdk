# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class RpcNoDefaultErrorCodeApiRequest(TeaModel):
    def __init__(self, success=None, code=None, message=None, http_status_code=None):
        self.success = TeaConverter.to_unicode(success)  # type: unicode
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.message = TeaConverter.to_unicode(message)  # type: unicode
        self.http_status_code = TeaConverter.to_unicode(http_status_code)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        return self


class RpcNoDefaultErrorCodeApiResponseBody(TeaModel):
    def __init__(self, code=None, success=None):
        self.code = TeaConverter.to_unicode(code)  # type: unicode
        self.success = TeaConverter.to_unicode(success)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RpcNoDefaultErrorCodeApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RpcNoDefaultErrorCodeApiResponseBody

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
            temp_model = RpcNoDefaultErrorCodeApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


