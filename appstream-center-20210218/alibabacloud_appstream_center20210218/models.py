# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetAuthCodeRequest(TeaModel):
    def __init__(self, end_user_id=None, external_user_id=None, policy=None):
        self.end_user_id = end_user_id  # type: str
        self.external_user_id = external_user_id  # type: str
        self.policy = policy  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id
        if self.policy is not None:
            result['Policy'] = self.policy
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        return self


class GetAuthCodeResponseBodyAuthModel(TeaModel):
    def __init__(self, auth_code=None, end_user_id=None, expire_time=None):
        self.auth_code = auth_code  # type: str
        self.end_user_id = end_user_id  # type: str
        self.expire_time = expire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAuthCodeResponseBodyAuthModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class GetAuthCodeResponseBody(TeaModel):
    def __init__(self, auth_model=None, request_id=None):
        self.auth_model = auth_model  # type: GetAuthCodeResponseBodyAuthModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.auth_model:
            self.auth_model.validate()

    def to_map(self):
        _map = super(GetAuthCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_model is not None:
            result['AuthModel'] = self.auth_model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthModel') is not None:
            temp_model = GetAuthCodeResponseBodyAuthModel()
            self.auth_model = temp_model.from_map(m['AuthModel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAuthCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAuthCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAuthCodeResponse, self).to_map()
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
            temp_model = GetAuthCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


