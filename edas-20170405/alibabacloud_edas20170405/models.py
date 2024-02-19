# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class EdasProduceRequest(TeaModel):
    def __init__(self, data=None, source_flag=None):
        self.data = data  # type: str
        self.source_flag = source_flag  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EdasProduceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.source_flag is not None:
            result['sourceFlag'] = self.source_flag
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('sourceFlag') is not None:
            self.source_flag = m.get('sourceFlag')
        return self


class EdasProduceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, success=None, synchro=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.success = success  # type: bool
        self.synchro = synchro  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EdasProduceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.success is not None:
            result['success'] = self.success
        if self.synchro is not None:
            result['synchro'] = self.synchro
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('synchro') is not None:
            self.synchro = m.get('synchro')
        return self


class EdasProduceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EdasProduceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EdasProduceResponse, self).to_map()
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
            temp_model = EdasProduceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


