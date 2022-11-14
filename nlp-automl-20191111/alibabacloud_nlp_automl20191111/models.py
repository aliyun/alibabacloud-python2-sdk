# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateAsyncPredictRequest(TeaModel):
    def __init__(self, content=None, detail_tag=None, fetch_content=None, file_content=None, file_type=None,
                 file_url=None, model_id=None, model_version=None, service_name=None, service_version=None, top_k=None):
        self.content = content  # type: str
        self.detail_tag = detail_tag  # type: str
        self.fetch_content = fetch_content  # type: str
        self.file_content = file_content  # type: str
        self.file_type = file_type  # type: str
        self.file_url = file_url  # type: str
        self.model_id = model_id  # type: int
        self.model_version = model_version  # type: str
        self.service_name = service_name  # type: str
        self.service_version = service_version  # type: str
        self.top_k = top_k  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAsyncPredictRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.detail_tag is not None:
            result['DetailTag'] = self.detail_tag
        if self.fetch_content is not None:
            result['FetchContent'] = self.fetch_content
        if self.file_content is not None:
            result['FileContent'] = self.file_content
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        if self.top_k is not None:
            result['TopK'] = self.top_k
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DetailTag') is not None:
            self.detail_tag = m.get('DetailTag')
        if m.get('FetchContent') is not None:
            self.fetch_content = m.get('FetchContent')
        if m.get('FileContent') is not None:
            self.file_content = m.get('FileContent')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        return self


class CreateAsyncPredictResponseBody(TeaModel):
    def __init__(self, async_predict_id=None, request_id=None):
        self.async_predict_id = async_predict_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAsyncPredictResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAsyncPredictResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAsyncPredictResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAsyncPredictResponse, self).to_map()
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
            temp_model = CreateAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAsyncPredictRequest(TeaModel):
    def __init__(self, async_predict_id=None):
        self.async_predict_id = async_predict_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncPredictRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        return self


class GetAsyncPredictResponseBody(TeaModel):
    def __init__(self, async_predict_id=None, content=None, request_id=None, status=None):
        self.async_predict_id = async_predict_id  # type: int
        self.content = content  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAsyncPredictResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_predict_id is not None:
            result['AsyncPredictId'] = self.async_predict_id
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AsyncPredictId') is not None:
            self.async_predict_id = m.get('AsyncPredictId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAsyncPredictResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAsyncPredictResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAsyncPredictResponse, self).to_map()
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
            temp_model = GetAsyncPredictResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPredictResultRequest(TeaModel):
    def __init__(self, content=None, detail_tag=None, model_id=None, model_version=None, top_k=None):
        self.content = content  # type: str
        self.detail_tag = detail_tag  # type: str
        self.model_id = model_id  # type: int
        self.model_version = model_version  # type: str
        self.top_k = top_k  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPredictResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.detail_tag is not None:
            result['DetailTag'] = self.detail_tag
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        if self.top_k is not None:
            result['TopK'] = self.top_k
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DetailTag') is not None:
            self.detail_tag = m.get('DetailTag')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')
        return self


class GetPredictResultResponseBody(TeaModel):
    def __init__(self, content=None, request_id=None):
        self.content = content  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPredictResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPredictResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPredictResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPredictResultResponse, self).to_map()
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
            temp_model = GetPredictResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunPreTrainServiceRequest(TeaModel):
    def __init__(self, predict_content=None, service_name=None, service_version=None):
        self.predict_content = predict_content  # type: str
        self.service_name = service_name  # type: str
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunPreTrainServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predict_content is not None:
            result['PredictContent'] = self.predict_content
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredictContent') is not None:
            self.predict_content = m.get('PredictContent')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class RunPreTrainServiceResponseBody(TeaModel):
    def __init__(self, predict_result=None, request_id=None):
        self.predict_result = predict_result  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunPreTrainServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predict_result is not None:
            result['PredictResult'] = self.predict_result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PredictResult') is not None:
            self.predict_result = m.get('PredictResult')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunPreTrainServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RunPreTrainServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunPreTrainServiceResponse, self).to_map()
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
            temp_model = RunPreTrainServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


