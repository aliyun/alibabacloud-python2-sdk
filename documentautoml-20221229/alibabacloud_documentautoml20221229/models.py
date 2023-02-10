# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class PredictClassifierModelRequest(TeaModel):
    def __init__(self, auto_prediction=None, classifier_id=None, content=None):
        self.auto_prediction = auto_prediction  # type: bool
        self.classifier_id = classifier_id  # type: long
        self.content = content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictClassifierModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_prediction is not None:
            result['AutoPrediction'] = self.auto_prediction
        if self.classifier_id is not None:
            result['ClassifierId'] = self.classifier_id
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoPrediction') is not None:
            self.auto_prediction = m.get('AutoPrediction')
        if m.get('ClassifierId') is not None:
            self.classifier_id = m.get('ClassifierId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class PredictClassifierModelResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictClassifierModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictClassifierModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PredictClassifierModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PredictClassifierModelResponse, self).to_map()
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
            temp_model = PredictClassifierModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictModelRequest(TeaModel):
    def __init__(self, binary_to_text=None, content=None, model_id=None, model_version=None):
        self.binary_to_text = binary_to_text  # type: bool
        self.content = content  # type: str
        self.model_id = model_id  # type: long
        self.model_version = model_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.binary_to_text is not None:
            result['BinaryToText'] = self.binary_to_text
        if self.content is not None:
            result['Content'] = self.content
        if self.model_id is not None:
            result['ModelId'] = self.model_id
        if self.model_version is not None:
            result['ModelVersion'] = self.model_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BinaryToText') is not None:
            self.binary_to_text = m.get('BinaryToText')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')
        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')
        return self


class PredictModelResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PredictModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PredictModelResponse, self).to_map()
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
            temp_model = PredictModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictTemplateModelRequest(TeaModel):
    def __init__(self, content=None, task_id=None):
        self.content = content  # type: str
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictTemplateModelRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PredictTemplateModelResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PredictTemplateModelResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PredictTemplateModelResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PredictTemplateModelResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PredictTemplateModelResponse, self).to_map()
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
            temp_model = PredictTemplateModelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


