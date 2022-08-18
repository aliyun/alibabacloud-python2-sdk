# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class DataRateLimitTestResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataRateLimitTestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DataRateLimitTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DataRateLimitTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DataRateLimitTestResponse, self).to_map()
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
            temp_model = DataRateLimitTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NormalRpcHsfApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NormalRpcHsfApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NormalRpcHsfApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NormalRpcHsfApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NormalRpcHsfApiResponse, self).to_map()
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
            temp_model = NormalRpcHsfApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NormalRpcHttpApiResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NormalRpcHttpApiResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NormalRpcHttpApiResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NormalRpcHttpApiResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NormalRpcHttpApiResponse, self).to_map()
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
            temp_model = NormalRpcHttpApiResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RpcDataUploadRequest(TeaModel):
    def __init__(self, large_param=None, query_1=None, query_2=None):
        self.large_param = large_param  # type: str
        self.query_1 = query_1  # type: str
        self.query_2 = query_2  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RpcDataUploadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.large_param is not None:
            result['largeParam'] = self.large_param
        if self.query_1 is not None:
            result['query1'] = self.query_1
        if self.query_2 is not None:
            result['query2'] = self.query_2
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('largeParam') is not None:
            self.large_param = m.get('largeParam')
        if m.get('query1') is not None:
            self.query_1 = m.get('query1')
        if m.get('query2') is not None:
            self.query_2 = m.get('query2')
        return self


class RpcDataUploadResponseBody(TeaModel):
    def __init__(self, request_id=None, headers=None, params=None, speed=None, total_bytes=None, total_time=None,
                 url=None):
        self.request_id = request_id  # type: str
        self.headers = headers  # type: dict[str, any]
        self.params = params  # type: dict[str, any]
        self.speed = speed  # type: str
        self.total_bytes = total_bytes  # type: long
        self.total_time = total_time  # type: long
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RpcDataUploadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.headers is not None:
            result['headers'] = self.headers
        if self.params is not None:
            result['params'] = self.params
        if self.speed is not None:
            result['speed'] = self.speed
        if self.total_bytes is not None:
            result['totalBytes'] = self.total_bytes
        if self.total_time is not None:
            result['totalTime'] = self.total_time
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('speed') is not None:
            self.speed = m.get('speed')
        if m.get('totalBytes') is not None:
            self.total_bytes = m.get('totalBytes')
        if m.get('totalTime') is not None:
            self.total_time = m.get('totalTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class RpcDataUploadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RpcDataUploadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RpcDataUploadResponse, self).to_map()
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
            temp_model = RpcDataUploadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RpcDataUploadAndDownloadRequest(TeaModel):
    def __init__(self, query_1=None):
        self.query_1 = query_1  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RpcDataUploadAndDownloadRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_1 is not None:
            result['query1'] = self.query_1
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('query1') is not None:
            self.query_1 = m.get('query1')
        return self


class RpcDataUploadAndDownloadResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RpcDataUploadAndDownloadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RpcDataUploadAndDownloadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RpcDataUploadAndDownloadResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RpcDataUploadAndDownloadResponse, self).to_map()
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
            temp_model = RpcDataUploadAndDownloadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RpcDataUploadTestResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RpcDataUploadTestResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RpcDataUploadTestResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RpcDataUploadTestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RpcDataUploadTestResponse, self).to_map()
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
            temp_model = RpcDataUploadTestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


