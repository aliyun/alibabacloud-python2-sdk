# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class YxTestApiRequest(TeaModel):
    def __init__(self, f_0=None, f_1=None):
        # param0
        self.f_0 = f_0  # type: int
        # param1
        self.f_1 = f_1  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(YxTestApiRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.f_0 is not None:
            result['f0'] = self.f_0
        if self.f_1 is not None:
            result['f1'] = self.f_1
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('f0') is not None:
            self.f_0 = m.get('f0')
        if m.get('f1') is not None:
            self.f_1 = m.get('f1')
        return self


class YxTestApiResponseBody(TeaModel):
    def __init__(self, sum=None):
        # sum
        self.sum = sum  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(YxTestApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sum is not None:
            result['sum'] = self.sum
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('sum') is not None:
            self.sum = m.get('sum')
        return self


class YxTestApiResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: YxTestApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(YxTestApiResponse, self).to_map()
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
            temp_model = YxTestApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


