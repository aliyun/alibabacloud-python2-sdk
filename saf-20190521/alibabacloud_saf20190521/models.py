# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ExecuteExtendServiceRequest(TeaModel):
    def __init__(self, region=None, service=None, service_parameters=None):
        self.region = region  # type: str
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteExtendServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ExecuteExtendServiceResponseBodyData(TeaModel):
    def __init__(self, invoke_result=None):
        self.invoke_result = invoke_result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteExtendServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_result is not None:
            result['InvokeResult'] = self.invoke_result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvokeResult') is not None:
            self.invoke_result = m.get('InvokeResult')
        return self


class ExecuteExtendServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ExecuteExtendServiceResponseBodyData
        self.http_status_code = http_status_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExecuteExtendServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ExecuteExtendServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecuteExtendServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteExtendServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteExtendServiceResponse, self).to_map()
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
            temp_model = ExecuteExtendServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteRequestRequest(TeaModel):
    def __init__(self, service=None, service_parameters=None):
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ExecuteRequestResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequestResponseBody, self).to_map()
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


class ExecuteRequestResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteRequestResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteRequestResponse, self).to_map()
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
            temp_model = ExecuteRequestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteRequestMLRequest(TeaModel):
    def __init__(self, lang=None, service=None, service_parameters=None):
        self.lang = lang  # type: str
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequestMLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ExecuteRequestMLResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequestMLResponseBody, self).to_map()
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


class ExecuteRequestMLResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteRequestMLResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteRequestMLResponse, self).to_map()
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
            temp_model = ExecuteRequestMLResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteRequestSGRequest(TeaModel):
    def __init__(self, lang=None, service=None, service_parameters=None):
        self.lang = lang  # type: str
        self.service = service  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequestSGRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.service is not None:
            result['Service'] = self.service
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('Service') is not None:
            self.service = m.get('Service')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class ExecuteRequestSGResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: int
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteRequestSGResponseBody, self).to_map()
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


class ExecuteRequestSGResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteRequestSGResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteRequestSGResponse, self).to_map()
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
            temp_model = ExecuteRequestSGResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestDecisionRequest(TeaModel):
    def __init__(self, event_code=None, service_parameters=None):
        self.event_code = event_code  # type: str
        self.service_parameters = service_parameters  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestDecisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_code is not None:
            result['EventCode'] = self.event_code
        if self.service_parameters is not None:
            result['ServiceParameters'] = self.service_parameters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')
        if m.get('ServiceParameters') is not None:
            self.service_parameters = m.get('ServiceParameters')
        return self


class RequestDecisionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: long
        self.data = data  # type: dict[str, any]
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestDecisionResponseBody, self).to_map()
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


class RequestDecisionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RequestDecisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestDecisionResponse, self).to_map()
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
            temp_model = RequestDecisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


