# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AbortAndRollbackChangeOrderRequest(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortAndRollbackChangeOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortAndRollbackChangeOrderResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortAndRollbackChangeOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortAndRollbackChangeOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: AbortAndRollbackChangeOrderResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AbortAndRollbackChangeOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AbortAndRollbackChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AbortAndRollbackChangeOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbortAndRollbackChangeOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbortAndRollbackChangeOrderResponse, self).to_map()
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
            temp_model = AbortAndRollbackChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AbortChangeOrderRequest(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortChangeOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortChangeOrderResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AbortChangeOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class AbortChangeOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: AbortChangeOrderResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AbortChangeOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AbortChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class AbortChangeOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AbortChangeOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AbortChangeOrderResponse, self).to_map()
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
            temp_model = AbortChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStartApplicationsRequest(TeaModel):
    def __init__(self, app_ids=None, namespace_id=None):
        self.app_ids = app_ids  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class BatchStartApplicationsResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStartApplicationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BatchStartApplicationsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: BatchStartApplicationsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchStartApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BatchStartApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BatchStartApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchStartApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStartApplicationsResponse, self).to_map()
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
            temp_model = BatchStartApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchStopApplicationsRequest(TeaModel):
    def __init__(self, app_ids=None, namespace_id=None):
        self.app_ids = app_ids  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_ids is not None:
            result['AppIds'] = self.app_ids
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppIds') is not None:
            self.app_ids = m.get('AppIds')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class BatchStopApplicationsResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchStopApplicationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BatchStopApplicationsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: BatchStopApplicationsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchStopApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BatchStopApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BatchStopApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchStopApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchStopApplicationsResponse, self).to_map()
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
            temp_model = BatchStopApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindSlbRequest(TeaModel):
    def __init__(self, app_id=None, internet=None, internet_slb_id=None, intranet=None, intranet_slb_id=None):
        self.app_id = app_id  # type: str
        self.internet = internet  # type: str
        self.internet_slb_id = internet_slb_id  # type: str
        self.intranet = intranet  # type: str
        self.intranet_slb_id = intranet_slb_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindSlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.internet is not None:
            result['Internet'] = self.internet
        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id
        if self.intranet is not None:
            result['Intranet'] = self.intranet
        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Internet') is not None:
            self.internet = m.get('Internet')
        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')
        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')
        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')
        return self


class BindSlbResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindSlbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class BindSlbResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: BindSlbResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BindSlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = BindSlbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class BindSlbResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindSlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindSlbResponse, self).to_map()
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
            temp_model = BindSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmPipelineBatchRequest(TeaModel):
    def __init__(self, confirm=None, pipeline_id=None):
        self.confirm = confirm  # type: bool
        self.pipeline_id = pipeline_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmPipelineBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.confirm is not None:
            result['Confirm'] = self.confirm
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Confirm') is not None:
            self.confirm = m.get('Confirm')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ConfirmPipelineBatchResponseBodyData(TeaModel):
    def __init__(self, pipeline_id=None):
        self.pipeline_id = pipeline_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfirmPipelineBatchResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class ConfirmPipelineBatchResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ConfirmPipelineBatchResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ConfirmPipelineBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ConfirmPipelineBatchResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ConfirmPipelineBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfirmPipelineBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfirmPipelineBatchResponse, self).to_map()
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
            temp_model = ConfirmPipelineBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationRequest(TeaModel):
    def __init__(self, acr_assume_role_arn=None, acr_instance_id=None, app_description=None, app_name=None,
                 associate_eip=None, auto_config=None, command=None, command_args=None, config_map_mount_desc=None, cpu=None,
                 custom_host_alias=None, deploy=None, edas_container_version=None, envs=None, image_url=None, jar_start_args=None,
                 jar_start_options=None, jdk=None, kafka_configs=None, kafka_endpoint=None, kafka_instance_id=None,
                 kafka_logfile_config=None, liveness=None, memory=None, mount_desc=None, mount_host=None, namespace_id=None, nas_id=None,
                 open_collect_to_kafka=None, oss_ak_id=None, oss_ak_secret=None, oss_mount_descs=None, package_type=None,
                 package_url=None, package_version=None, php_arms_config_location=None, php_config=None,
                 php_config_location=None, post_start=None, pre_stop=None, programming_language=None, readiness=None, replicas=None,
                 security_group_id=None, sls_configs=None, termination_grace_period_seconds=None, timezone=None, tomcat_config=None,
                 v_switch_id=None, vpc_id=None, war_start_options=None, web_container=None, mse_feature_config=None):
        self.acr_assume_role_arn = acr_assume_role_arn  # type: str
        # ACR 企业版实例 ID
        self.acr_instance_id = acr_instance_id  # type: str
        self.app_description = app_description  # type: str
        self.app_name = app_name  # type: str
        # 是否绑定EIP
        self.associate_eip = associate_eip  # type: bool
        self.auto_config = auto_config  # type: bool
        self.command = command  # type: str
        self.command_args = command_args  # type: str
        self.config_map_mount_desc = config_map_mount_desc  # type: str
        self.cpu = cpu  # type: int
        self.custom_host_alias = custom_host_alias  # type: str
        self.deploy = deploy  # type: bool
        self.edas_container_version = edas_container_version  # type: str
        self.envs = envs  # type: str
        self.image_url = image_url  # type: str
        self.jar_start_args = jar_start_args  # type: str
        self.jar_start_options = jar_start_options  # type: str
        self.jdk = jdk  # type: str
        self.kafka_configs = kafka_configs  # type: str
        self.kafka_endpoint = kafka_endpoint  # type: str
        self.kafka_instance_id = kafka_instance_id  # type: str
        self.kafka_logfile_config = kafka_logfile_config  # type: str
        self.liveness = liveness  # type: str
        self.memory = memory  # type: int
        self.mount_desc = mount_desc  # type: str
        self.mount_host = mount_host  # type: str
        self.namespace_id = namespace_id  # type: str
        self.nas_id = nas_id  # type: str
        self.open_collect_to_kafka = open_collect_to_kafka  # type: bool
        # OSS使用的AKID
        self.oss_ak_id = oss_ak_id  # type: str
        # OSS AKID对应的secret
        self.oss_ak_secret = oss_ak_secret  # type: str
        # OSS挂载描述信息
        self.oss_mount_descs = oss_mount_descs  # type: str
        self.package_type = package_type  # type: str
        self.package_url = package_url  # type: str
        self.package_version = package_version  # type: str
        self.php_arms_config_location = php_arms_config_location  # type: str
        self.php_config = php_config  # type: str
        self.php_config_location = php_config_location  # type: str
        self.post_start = post_start  # type: str
        self.pre_stop = pre_stop  # type: str
        self.programming_language = programming_language  # type: str
        self.readiness = readiness  # type: str
        self.replicas = replicas  # type: int
        self.security_group_id = security_group_id  # type: str
        self.sls_configs = sls_configs  # type: str
        self.termination_grace_period_seconds = termination_grace_period_seconds  # type: int
        self.timezone = timezone  # type: str
        self.tomcat_config = tomcat_config  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.war_start_options = war_start_options  # type: str
        self.web_container = web_container  # type: str
        self.mse_feature_config = mse_feature_config  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.deploy is not None:
            result['Deploy'] = self.deploy
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs
        if self.kafka_endpoint is not None:
            result['KafkaEndpoint'] = self.kafka_endpoint
        if self.kafka_instance_id is not None:
            result['KafkaInstanceId'] = self.kafka_instance_id
        if self.kafka_logfile_config is not None:
            result['KafkaLogfileConfig'] = self.kafka_logfile_config
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.open_collect_to_kafka is not None:
            result['OpenCollectToKafka'] = self.open_collect_to_kafka
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        if self.mse_feature_config is not None:
            result['mseFeatureConfig'] = self.mse_feature_config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')
        if m.get('KafkaEndpoint') is not None:
            self.kafka_endpoint = m.get('KafkaEndpoint')
        if m.get('KafkaInstanceId') is not None:
            self.kafka_instance_id = m.get('KafkaInstanceId')
        if m.get('KafkaLogfileConfig') is not None:
            self.kafka_logfile_config = m.get('KafkaLogfileConfig')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OpenCollectToKafka') is not None:
            self.open_collect_to_kafka = m.get('OpenCollectToKafka')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        if m.get('mseFeatureConfig') is not None:
            self.mse_feature_config = m.get('mseFeatureConfig')
        return self


class CreateApplicationResponseBodyData(TeaModel):
    def __init__(self, app_id=None, change_order_id=None):
        self.app_id = app_id  # type: str
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class CreateApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationResponse, self).to_map()
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
            temp_model = CreateApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateApplicationScalingRuleRequest(TeaModel):
    def __init__(self, app_id=None, min_ready_instance_ratio=None, min_ready_instances=None,
                 scaling_rule_enable=None, scaling_rule_metric=None, scaling_rule_name=None, scaling_rule_timer=None,
                 scaling_rule_type=None):
        self.app_id = app_id  # type: str
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int
        self.scaling_rule_enable = scaling_rule_enable  # type: bool
        self.scaling_rule_metric = scaling_rule_metric  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str
        self.scaling_rule_timer = scaling_rule_timer  # type: str
        self.scaling_rule_type = scaling_rule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationScalingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.scaling_rule_enable is not None:
            result['ScalingRuleEnable'] = self.scaling_rule_enable
        if self.scaling_rule_metric is not None:
            result['ScalingRuleMetric'] = self.scaling_rule_metric
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer
        if self.scaling_rule_type is not None:
            result['ScalingRuleType'] = self.scaling_rule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('ScalingRuleEnable') is not None:
            self.scaling_rule_enable = m.get('ScalingRuleEnable')
        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')
        if m.get('ScalingRuleType') is not None:
            self.scaling_rule_type = m.get('ScalingRuleType')
        return self


class CreateApplicationScalingRuleResponseBodyDataMetricMetrics(TeaModel):
    def __init__(self, metric_target_average_utilization=None, metric_type=None):
        self.metric_target_average_utilization = metric_target_average_utilization  # type: int
        self.metric_type = metric_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponseBodyDataMetricMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class CreateApplicationScalingRuleResponseBodyDataMetric(TeaModel):
    def __init__(self, max_replicas=None, metrics=None, min_replicas=None):
        self.max_replicas = max_replicas  # type: int
        self.metrics = metrics  # type: list[CreateApplicationScalingRuleResponseBodyDataMetricMetrics]
        self.min_replicas = min_replicas  # type: int

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponseBodyDataMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = CreateApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        return self


class CreateApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(self, at_time=None, target_replicas=None):
        self.at_time = at_time  # type: str
        self.target_replicas = target_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponseBodyDataTimerSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class CreateApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(self, begin_date=None, end_date=None, period=None, schedules=None):
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.period = period  # type: str
        self.schedules = schedules  # type: list[CreateApplicationScalingRuleResponseBodyDataTimerSchedules]

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponseBodyDataTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = CreateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class CreateApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(self, app_id=None, create_time=None, last_disable_time=None, metric=None, scale_rule_enabled=None,
                 scale_rule_name=None, scale_rule_type=None, timer=None, update_time=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: long
        self.last_disable_time = last_disable_time  # type: long
        self.metric = metric  # type: CreateApplicationScalingRuleResponseBodyDataMetric
        self.scale_rule_enabled = scale_rule_enabled  # type: bool
        self.scale_rule_name = scale_rule_name  # type: str
        self.scale_rule_type = scale_rule_type  # type: str
        self.timer = timer  # type: CreateApplicationScalingRuleResponseBodyDataTimer
        self.update_time = update_time  # type: long

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateApplicationScalingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, trace_id=None):
        self.data = data  # type: CreateApplicationScalingRuleResponseBodyData
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateApplicationScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateApplicationScalingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateApplicationScalingRuleResponse, self).to_map()
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
            temp_model = CreateApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConfigMapRequest(TeaModel):
    def __init__(self, data=None, description=None, name=None, namespace_id=None):
        self.data = data  # type: str
        self.description = description  # type: str
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConfigMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class CreateConfigMapResponseBodyData(TeaModel):
    def __init__(self, config_map_id=None):
        self.config_map_id = config_map_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateConfigMapResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class CreateConfigMapResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateConfigMapResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateConfigMapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateConfigMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateConfigMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateConfigMapResponse, self).to_map()
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
            temp_model = CreateConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGreyTagRouteRequest(TeaModel):
    def __init__(self, app_id=None, description=None, dubbo_rules=None, name=None, sc_rules=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 规则名称
        self.description = description  # type: str
        # Dubbo规则
        self.dubbo_rules = dubbo_rules  # type: str
        # 规则名称
        self.name = name  # type: str
        # SpringCloud规则
        self.sc_rules = sc_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGreyTagRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.description is not None:
            result['Description'] = self.description
        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules
        if self.name is not None:
            result['Name'] = self.name
        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')
        return self


class CreateGreyTagRouteResponseBodyData(TeaModel):
    def __init__(self, grey_tag_route_id=None):
        self.grey_tag_route_id = grey_tag_route_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGreyTagRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class CreateGreyTagRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateGreyTagRouteResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateGreyTagRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateGreyTagRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGreyTagRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGreyTagRouteResponse, self).to_map()
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
            temp_model = CreateGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIngressRequest(TeaModel):
    def __init__(self, cert_id=None, default_rule=None, description=None, listener_port=None,
                 listener_protocol=None, load_balance_type=None, namespace_id=None, rules=None, slb_id=None):
        self.cert_id = cert_id  # type: str
        self.default_rule = default_rule  # type: str
        self.description = description  # type: str
        self.listener_port = listener_port  # type: int
        self.listener_protocol = listener_protocol  # type: str
        self.load_balance_type = load_balance_type  # type: str
        self.namespace_id = namespace_id  # type: str
        self.rules = rules  # type: str
        self.slb_id = slb_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIngressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.description is not None:
            result['Description'] = self.description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.rules is not None:
            result['Rules'] = self.rules
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        return self


class CreateIngressResponseBodyData(TeaModel):
    def __init__(self, ingress_id=None):
        self.ingress_id = ingress_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateIngressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class CreateIngressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateIngressResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateIngressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateIngressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateIngressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateIngressResponse, self).to_map()
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
            temp_model = CreateIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(self, namespace_description=None, namespace_id=None, namespace_name=None):
        self.namespace_description = namespace_description  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class CreateNamespaceResponseBodyData(TeaModel):
    def __init__(self, namespace_description=None, namespace_id=None, namespace_name=None, region_id=None):
        self.namespace_description = namespace_description  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: CreateNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = CreateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateNamespaceResponse, self).to_map()
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteApplicationResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class DeleteApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationResponse, self).to_map()
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
            temp_model = DeleteApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplicationScalingRuleRequest(TeaModel):
    def __init__(self, app_id=None, scaling_rule_name=None):
        self.app_id = app_id  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationScalingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DeleteApplicationScalingRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_id=None):
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplicationScalingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteApplicationScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplicationScalingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplicationScalingRuleResponse, self).to_map()
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
            temp_model = DeleteApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConfigMapRequest(TeaModel):
    def __init__(self, config_map_id=None):
        self.config_map_id = config_map_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConfigMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DeleteConfigMapResponseBodyData(TeaModel):
    def __init__(self, config_map_id=None):
        self.config_map_id = config_map_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteConfigMapResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DeleteConfigMapResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteConfigMapResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteConfigMapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteConfigMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteConfigMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteConfigMapResponse, self).to_map()
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
            temp_model = DeleteConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGreyTagRouteRequest(TeaModel):
    def __init__(self, grey_tag_route_id=None):
        # 规则ID
        self.grey_tag_route_id = grey_tag_route_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGreyTagRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DeleteGreyTagRouteResponseBodyData(TeaModel):
    def __init__(self, grey_tag_route_id=None):
        self.grey_tag_route_id = grey_tag_route_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGreyTagRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DeleteGreyTagRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteGreyTagRouteResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteGreyTagRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteGreyTagRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGreyTagRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGreyTagRouteResponse, self).to_map()
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
            temp_model = DeleteGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIngressRequest(TeaModel):
    def __init__(self, ingress_id=None):
        self.ingress_id = ingress_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIngressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DeleteIngressResponseBodyData(TeaModel):
    def __init__(self, ingress_id=None):
        self.ingress_id = ingress_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteIngressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DeleteIngressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteIngressResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteIngressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeleteIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteIngressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteIngressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteIngressResponse, self).to_map()
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
            temp_model = DeleteIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(self, namespace_id=None):
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None, trace_id=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNamespaceResponse, self).to_map()
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployApplicationRequest(TeaModel):
    def __init__(self, acr_assume_role_arn=None, acr_instance_id=None, app_id=None, associate_eip=None,
                 auto_enable_application_scaling_rule=None, batch_wait_time=None, change_order_desc=None, command=None, command_args=None,
                 config_map_mount_desc=None, custom_host_alias=None, edas_container_version=None, enable_ahas=None,
                 enable_grey_tag_route=None, envs=None, image_url=None, jar_start_args=None, jar_start_options=None, jdk=None,
                 kafka_configs=None, kafka_endpoint=None, kafka_instance_id=None, kafka_logfile_config=None, liveness=None,
                 min_ready_instance_ratio=None, min_ready_instances=None, mount_desc=None, mount_host=None, mse_feature_config=None,
                 nas_id=None, open_collect_to_kafka=None, oss_ak_id=None, oss_ak_secret=None, oss_mount_descs=None,
                 package_url=None, package_version=None, php_arms_config_location=None, php_config=None,
                 php_config_location=None, post_start=None, pre_stop=None, readiness=None, sls_configs=None,
                 termination_grace_period_seconds=None, timezone=None, tomcat_config=None, update_strategy=None, war_start_options=None,
                 web_container=None):
        self.acr_assume_role_arn = acr_assume_role_arn  # type: str
        # ACR 企业版实例 ID
        self.acr_instance_id = acr_instance_id  # type: str
        self.app_id = app_id  # type: str
        # 是否绑定EIP
        self.associate_eip = associate_eip  # type: bool
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule  # type: bool
        self.batch_wait_time = batch_wait_time  # type: int
        self.change_order_desc = change_order_desc  # type: str
        self.command = command  # type: str
        self.command_args = command_args  # type: str
        self.config_map_mount_desc = config_map_mount_desc  # type: str
        self.custom_host_alias = custom_host_alias  # type: str
        self.edas_container_version = edas_container_version  # type: str
        self.enable_ahas = enable_ahas  # type: str
        # 是否开启发布流量灰度规则
        self.enable_grey_tag_route = enable_grey_tag_route  # type: bool
        self.envs = envs  # type: str
        self.image_url = image_url  # type: str
        self.jar_start_args = jar_start_args  # type: str
        self.jar_start_options = jar_start_options  # type: str
        self.jdk = jdk  # type: str
        self.kafka_configs = kafka_configs  # type: str
        self.kafka_endpoint = kafka_endpoint  # type: str
        self.kafka_instance_id = kafka_instance_id  # type: str
        self.kafka_logfile_config = kafka_logfile_config  # type: str
        self.liveness = liveness  # type: str
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int
        self.mount_desc = mount_desc  # type: str
        self.mount_host = mount_host  # type: str
        self.mse_feature_config = mse_feature_config  # type: str
        self.nas_id = nas_id  # type: str
        self.open_collect_to_kafka = open_collect_to_kafka  # type: bool
        # OSS使用的AKID
        self.oss_ak_id = oss_ak_id  # type: str
        # OSS AKID对应的secret
        self.oss_ak_secret = oss_ak_secret  # type: str
        # OSS挂载描述信息
        self.oss_mount_descs = oss_mount_descs  # type: str
        self.package_url = package_url  # type: str
        self.package_version = package_version  # type: str
        self.php_arms_config_location = php_arms_config_location  # type: str
        self.php_config = php_config  # type: str
        self.php_config_location = php_config_location  # type: str
        self.post_start = post_start  # type: str
        self.pre_stop = pre_stop  # type: str
        self.readiness = readiness  # type: str
        self.sls_configs = sls_configs  # type: str
        self.termination_grace_period_seconds = termination_grace_period_seconds  # type: int
        self.timezone = timezone  # type: str
        self.tomcat_config = tomcat_config  # type: str
        self.update_strategy = update_strategy  # type: str
        self.war_start_options = war_start_options  # type: str
        self.web_container = web_container  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.change_order_desc is not None:
            result['ChangeOrderDesc'] = self.change_order_desc
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas
        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs
        if self.kafka_endpoint is not None:
            result['KafkaEndpoint'] = self.kafka_endpoint
        if self.kafka_instance_id is not None:
            result['KafkaInstanceId'] = self.kafka_instance_id
        if self.kafka_logfile_config is not None:
            result['KafkaLogfileConfig'] = self.kafka_logfile_config
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.mse_feature_config is not None:
            result['MseFeatureConfig'] = self.mse_feature_config
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.open_collect_to_kafka is not None:
            result['OpenCollectToKafka'] = self.open_collect_to_kafka
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('ChangeOrderDesc') is not None:
            self.change_order_desc = m.get('ChangeOrderDesc')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')
        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')
        if m.get('KafkaEndpoint') is not None:
            self.kafka_endpoint = m.get('KafkaEndpoint')
        if m.get('KafkaInstanceId') is not None:
            self.kafka_instance_id = m.get('KafkaInstanceId')
        if m.get('KafkaLogfileConfig') is not None:
            self.kafka_logfile_config = m.get('KafkaLogfileConfig')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('MseFeatureConfig') is not None:
            self.mse_feature_config = m.get('MseFeatureConfig')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OpenCollectToKafka') is not None:
            self.open_collect_to_kafka = m.get('OpenCollectToKafka')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DeployApplicationResponseBodyData(TeaModel):
    def __init__(self, app_id=None, change_order_id=None, is_need_approval=None):
        self.app_id = app_id  # type: str
        self.change_order_id = change_order_id  # type: str
        self.is_need_approval = is_need_approval  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeployApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')
        return self


class DeployApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DeployApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeployApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DeployApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DeployApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeployApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeployApplicationResponse, self).to_map()
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
            temp_model = DeployApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAppServiceDetailRequest(TeaModel):
    def __init__(self, app_id=None, service_group=None, service_name=None, service_type=None, service_version=None):
        # mse 的 appId
        self.app_id = app_id  # type: str
        self.service_group = service_group  # type: str
        self.service_name = service_name  # type: str
        self.service_type = service_type  # type: str
        self.service_version = service_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppServiceDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')
        return self


class DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions(TeaModel):
    def __init__(self, description=None, name=None, type=None):
        self.description = description  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeAppServiceDetailResponseBodyDataMethods(TeaModel):
    def __init__(self, method_controller=None, name=None, name_detail=None, parameter_definitions=None,
                 parameter_details=None, parameter_types=None, paths=None, request_methods=None, return_details=None,
                 return_type=None):
        self.method_controller = method_controller  # type: str
        self.name = name  # type: str
        self.name_detail = name_detail  # type: str
        self.parameter_definitions = parameter_definitions  # type: list[DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions]
        self.parameter_details = parameter_details  # type: list[str]
        self.parameter_types = parameter_types  # type: list[str]
        self.paths = paths  # type: list[str]
        self.request_methods = request_methods  # type: list[str]
        self.return_details = return_details  # type: str
        self.return_type = return_type  # type: str

    def validate(self):
        if self.parameter_definitions:
            for k in self.parameter_definitions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppServiceDetailResponseBodyDataMethods, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_controller is not None:
            result['MethodController'] = self.method_controller
        if self.name is not None:
            result['Name'] = self.name
        if self.name_detail is not None:
            result['NameDetail'] = self.name_detail
        result['ParameterDefinitions'] = []
        if self.parameter_definitions is not None:
            for k in self.parameter_definitions:
                result['ParameterDefinitions'].append(k.to_map() if k else None)
        if self.parameter_details is not None:
            result['ParameterDetails'] = self.parameter_details
        if self.parameter_types is not None:
            result['ParameterTypes'] = self.parameter_types
        if self.paths is not None:
            result['Paths'] = self.paths
        if self.request_methods is not None:
            result['RequestMethods'] = self.request_methods
        if self.return_details is not None:
            result['ReturnDetails'] = self.return_details
        if self.return_type is not None:
            result['ReturnType'] = self.return_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MethodController') is not None:
            self.method_controller = m.get('MethodController')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NameDetail') is not None:
            self.name_detail = m.get('NameDetail')
        self.parameter_definitions = []
        if m.get('ParameterDefinitions') is not None:
            for k in m.get('ParameterDefinitions'):
                temp_model = DescribeAppServiceDetailResponseBodyDataMethodsParameterDefinitions()
                self.parameter_definitions.append(temp_model.from_map(k))
        if m.get('ParameterDetails') is not None:
            self.parameter_details = m.get('ParameterDetails')
        if m.get('ParameterTypes') is not None:
            self.parameter_types = m.get('ParameterTypes')
        if m.get('Paths') is not None:
            self.paths = m.get('Paths')
        if m.get('RequestMethods') is not None:
            self.request_methods = m.get('RequestMethods')
        if m.get('ReturnDetails') is not None:
            self.return_details = m.get('ReturnDetails')
        if m.get('ReturnType') is not None:
            self.return_type = m.get('ReturnType')
        return self


class DescribeAppServiceDetailResponseBodyData(TeaModel):
    def __init__(self, dubbo_application_name=None, edas_app_name=None, group=None, metadata=None, methods=None,
                 service_name=None, service_type=None, spring_application_name=None, version=None):
        self.dubbo_application_name = dubbo_application_name  # type: str
        self.edas_app_name = edas_app_name  # type: str
        self.group = group  # type: str
        self.metadata = metadata  # type: dict[str, any]
        self.methods = methods  # type: list[DescribeAppServiceDetailResponseBodyDataMethods]
        self.service_name = service_name  # type: str
        self.service_type = service_type  # type: str
        self.spring_application_name = spring_application_name  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.methods:
            for k in self.methods:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeAppServiceDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dubbo_application_name is not None:
            result['DubboApplicationName'] = self.dubbo_application_name
        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.metadata is not None:
            result['Metadata'] = self.metadata
        result['Methods'] = []
        if self.methods is not None:
            for k in self.methods:
                result['Methods'].append(k.to_map() if k else None)
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.spring_application_name is not None:
            result['SpringApplicationName'] = self.spring_application_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DubboApplicationName') is not None:
            self.dubbo_application_name = m.get('DubboApplicationName')
        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')
        self.methods = []
        if m.get('Methods') is not None:
            for k in m.get('Methods'):
                temp_model = DescribeAppServiceDetailResponseBodyDataMethods()
                self.methods.append(temp_model.from_map(k))
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('SpringApplicationName') is not None:
            self.spring_application_name = m.get('SpringApplicationName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeAppServiceDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeAppServiceDetailResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeAppServiceDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeAppServiceDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeAppServiceDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeAppServiceDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAppServiceDetailResponse, self).to_map()
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
            temp_model = DescribeAppServiceDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationConfigRequest(TeaModel):
    def __init__(self, app_id=None, version_id=None):
        self.app_id = app_id  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class DescribeApplicationConfigResponseBodyDataConfigMapMountDesc(TeaModel):
    def __init__(self, config_map_id=None, config_map_name=None, key=None, mount_path=None):
        self.config_map_id = config_map_id  # type: long
        self.config_map_name = config_map_name  # type: str
        self.key = key  # type: str
        self.mount_path = mount_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationConfigResponseBodyDataConfigMapMountDesc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name
        if self.key is not None:
            result['Key'] = self.key
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        return self


class DescribeApplicationConfigResponseBodyDataMountDesc(TeaModel):
    def __init__(self, mount_path=None, nas_path=None):
        self.mount_path = mount_path  # type: str
        self.nas_path = nas_path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationConfigResponseBodyDataMountDesc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path
        if self.nas_path is not None:
            result['NasPath'] = self.nas_path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')
        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')
        return self


class DescribeApplicationConfigResponseBodyDataOssMountDescs(TeaModel):
    def __init__(self, bucket_name=None, bucket_path=None, mount_path=None, read_only=None):
        # Bucket名称
        self.bucket_name = bucket_name  # type: str
        # Bucket中Oss Key名称
        self.bucket_path = bucket_path  # type: str
        # 挂载到容器的路径
        self.mount_path = mount_path  # type: str
        # 是否只读
        self.read_only = read_only  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationConfigResponseBodyDataOssMountDescs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        if self.read_only is not None:
            result['readOnly'] = self.read_only
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')
        return self


class DescribeApplicationConfigResponseBodyDataTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationConfigResponseBodyDataTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeApplicationConfigResponseBodyData(TeaModel):
    def __init__(self, acr_assume_role_arn=None, acr_instance_id=None, app_description=None, app_id=None,
                 app_name=None, associate_eip=None, batch_wait_time=None, command=None, command_args=None,
                 config_map_mount_desc=None, cpu=None, custom_host_alias=None, edas_container_version=None, enable_ahas=None,
                 enable_grey_tag_route=None, envs=None, image_url=None, jar_start_args=None, jar_start_options=None, jdk=None,
                 kafka_configs=None, liveness=None, memory=None, min_ready_instance_ratio=None, min_ready_instances=None,
                 mount_desc=None, mount_host=None, mse_application_id=None, mse_feature_config=None, namespace_id=None,
                 nas_id=None, oss_ak_id=None, oss_ak_secret=None, oss_mount_descs=None, package_type=None,
                 package_url=None, package_version=None, php_arms_config_location=None, php_config=None,
                 php_config_location=None, post_start=None, pre_stop=None, programming_language=None, readiness=None, region_id=None,
                 replicas=None, security_group_id=None, sls_configs=None, tags=None, termination_grace_period_seconds=None,
                 timezone=None, tomcat_config=None, update_strategy=None, v_switch_id=None, vpc_id=None,
                 war_start_options=None, web_container=None):
        self.acr_assume_role_arn = acr_assume_role_arn  # type: str
        # ACR 企业版实例 ID
        self.acr_instance_id = acr_instance_id  # type: str
        self.app_description = app_description  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        # 是否绑定EIP
        self.associate_eip = associate_eip  # type: bool
        self.batch_wait_time = batch_wait_time  # type: int
        self.command = command  # type: str
        self.command_args = command_args  # type: str
        self.config_map_mount_desc = config_map_mount_desc  # type: list[DescribeApplicationConfigResponseBodyDataConfigMapMountDesc]
        self.cpu = cpu  # type: int
        self.custom_host_alias = custom_host_alias  # type: str
        self.edas_container_version = edas_container_version  # type: str
        self.enable_ahas = enable_ahas  # type: str
        # 开启流量灰度
        self.enable_grey_tag_route = enable_grey_tag_route  # type: bool
        self.envs = envs  # type: str
        self.image_url = image_url  # type: str
        self.jar_start_args = jar_start_args  # type: str
        self.jar_start_options = jar_start_options  # type: str
        self.jdk = jdk  # type: str
        self.kafka_configs = kafka_configs  # type: str
        self.liveness = liveness  # type: str
        self.memory = memory  # type: int
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int
        self.mount_desc = mount_desc  # type: list[DescribeApplicationConfigResponseBodyDataMountDesc]
        self.mount_host = mount_host  # type: str
        # 对应MSE产品侧应用ID
        self.mse_application_id = mse_application_id  # type: str
        self.mse_feature_config = mse_feature_config  # type: str
        self.namespace_id = namespace_id  # type: str
        self.nas_id = nas_id  # type: str
        # OSS读写的AK
        self.oss_ak_id = oss_ak_id  # type: str
        # OSS读写的secret
        self.oss_ak_secret = oss_ak_secret  # type: str
        # OSS挂载描述信息
        self.oss_mount_descs = oss_mount_descs  # type: list[DescribeApplicationConfigResponseBodyDataOssMountDescs]
        self.package_type = package_type  # type: str
        self.package_url = package_url  # type: str
        self.package_version = package_version  # type: str
        self.php_arms_config_location = php_arms_config_location  # type: str
        self.php_config = php_config  # type: str
        self.php_config_location = php_config_location  # type: str
        self.post_start = post_start  # type: str
        self.pre_stop = pre_stop  # type: str
        self.programming_language = programming_language  # type: str
        self.readiness = readiness  # type: str
        self.region_id = region_id  # type: str
        self.replicas = replicas  # type: int
        self.security_group_id = security_group_id  # type: str
        self.sls_configs = sls_configs  # type: str
        self.tags = tags  # type: list[DescribeApplicationConfigResponseBodyDataTags]
        self.termination_grace_period_seconds = termination_grace_period_seconds  # type: int
        self.timezone = timezone  # type: str
        self.tomcat_config = tomcat_config  # type: str
        self.update_strategy = update_strategy  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.war_start_options = war_start_options  # type: str
        self.web_container = web_container  # type: str

    def validate(self):
        if self.config_map_mount_desc:
            for k in self.config_map_mount_desc:
                if k:
                    k.validate()
        if self.mount_desc:
            for k in self.mount_desc:
                if k:
                    k.validate()
        if self.oss_mount_descs:
            for k in self.oss_mount_descs:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k.to_map() if k else None)
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas
        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs
        if self.liveness is not None:
            result['Liveness'] = self.liveness
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        result['MountDesc'] = []
        if self.mount_desc is not None:
            for k in self.mount_desc:
                result['MountDesc'].append(k.to_map() if k else None)
        if self.mount_host is not None:
            result['MountHost'] = self.mount_host
        if self.mse_application_id is not None:
            result['MseApplicationId'] = self.mse_application_id
        if self.mse_feature_config is not None:
            result['MseFeatureConfig'] = self.mse_feature_config
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.nas_id is not None:
            result['NasId'] = self.nas_id
        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id
        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret
        result['OssMountDescs'] = []
        if self.oss_mount_descs is not None:
            for k in self.oss_mount_descs:
                result['OssMountDescs'].append(k.to_map() if k else None)
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location
        if self.php_config is not None:
            result['PhpConfig'] = self.php_config
        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location
        if self.post_start is not None:
            result['PostStart'] = self.post_start
        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop
        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language
        if self.readiness is not None:
            result['Readiness'] = self.readiness
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds
        if self.timezone is not None:
            result['Timezone'] = self.timezone
        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k in m.get('ConfigMapMountDesc'):
                temp_model = DescribeApplicationConfigResponseBodyDataConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k))
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')
        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')
        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        self.mount_desc = []
        if m.get('MountDesc') is not None:
            for k in m.get('MountDesc'):
                temp_model = DescribeApplicationConfigResponseBodyDataMountDesc()
                self.mount_desc.append(temp_model.from_map(k))
        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')
        if m.get('MseApplicationId') is not None:
            self.mse_application_id = m.get('MseApplicationId')
        if m.get('MseFeatureConfig') is not None:
            self.mse_feature_config = m.get('MseFeatureConfig')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')
        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')
        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')
        self.oss_mount_descs = []
        if m.get('OssMountDescs') is not None:
            for k in m.get('OssMountDescs'):
                temp_model = DescribeApplicationConfigResponseBodyDataOssMountDescs()
                self.oss_mount_descs.append(temp_model.from_map(k))
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')
        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')
        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')
        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')
        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')
        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')
        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeApplicationConfigResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')
        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')
        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeApplicationConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeApplicationConfigResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationConfigResponse, self).to_map()
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
            temp_model = DescribeApplicationConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationGroupsRequest(TeaModel):
    def __init__(self, app_id=None, current_page=None, page_size=None):
        self.app_id = app_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeApplicationGroupsResponseBodyData(TeaModel):
    def __init__(self, edas_container_version=None, group_id=None, group_name=None, group_type=None, image_url=None,
                 jdk=None, package_type=None, package_url=None, package_version=None, replicas=None,
                 running_instances=None, web_container=None):
        self.edas_container_version = edas_container_version  # type: str
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str
        self.group_type = group_type  # type: int
        self.image_url = image_url  # type: str
        self.jdk = jdk  # type: str
        self.package_type = package_type  # type: str
        self.package_url = package_url  # type: str
        self.package_version = package_version  # type: str
        self.replicas = replicas  # type: int
        self.running_instances = running_instances  # type: int
        self.web_container = web_container  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.jdk is not None:
            result['Jdk'] = self.jdk
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.package_url is not None:
            result['PackageUrl'] = self.package_url
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        if self.web_container is not None:
            result['WebContainer'] = self.web_container
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')
        return self


class DescribeApplicationGroupsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeApplicationGroupsResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeApplicationGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationGroupsResponse, self).to_map()
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
            temp_model = DescribeApplicationGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationImageRequest(TeaModel):
    def __init__(self, app_id=None, image_url=None):
        self.app_id = app_id  # type: str
        self.image_url = image_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationImageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class DescribeApplicationImageResponseBodyData(TeaModel):
    def __init__(self, cr_url=None, logo=None, region_id=None, repo_name=None, repo_namespace=None,
                 repo_origin_type=None, repo_tag=None, repo_type=None):
        self.cr_url = cr_url  # type: str
        self.logo = logo  # type: str
        self.region_id = region_id  # type: str
        self.repo_name = repo_name  # type: str
        self.repo_namespace = repo_namespace  # type: str
        self.repo_origin_type = repo_origin_type  # type: str
        self.repo_tag = repo_tag  # type: str
        self.repo_type = repo_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationImageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cr_url is not None:
            result['CrUrl'] = self.cr_url
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace is not None:
            result['RepoNamespace'] = self.repo_namespace
        if self.repo_origin_type is not None:
            result['RepoOriginType'] = self.repo_origin_type
        if self.repo_tag is not None:
            result['RepoTag'] = self.repo_tag
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CrUrl') is not None:
            self.cr_url = m.get('CrUrl')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespace') is not None:
            self.repo_namespace = m.get('RepoNamespace')
        if m.get('RepoOriginType') is not None:
            self.repo_origin_type = m.get('RepoOriginType')
        if m.get('RepoTag') is not None:
            self.repo_tag = m.get('RepoTag')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        return self


class DescribeApplicationImageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeApplicationImageResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationImageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationImageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationImageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationImageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationImageResponse, self).to_map()
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
            temp_model = DescribeApplicationImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationInstancesRequest(TeaModel):
    def __init__(self, app_id=None, current_page=None, group_id=None, page_size=None, reverse=None):
        self.app_id = app_id  # type: str
        self.current_page = current_page  # type: int
        self.group_id = group_id  # type: str
        self.page_size = page_size  # type: int
        self.reverse = reverse  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class DescribeApplicationInstancesResponseBodyDataInstances(TeaModel):
    def __init__(self, create_time_stamp=None, debug_status=None, eip=None, finish_time_stamp=None, group_id=None,
                 image_url=None, instance_container_ip=None, instance_container_restarts=None,
                 instance_container_status=None, instance_health_status=None, instance_id=None, package_version=None, v_switch_id=None):
        self.create_time_stamp = create_time_stamp  # type: long
        self.debug_status = debug_status  # type: bool
        self.eip = eip  # type: str
        self.finish_time_stamp = finish_time_stamp  # type: long
        self.group_id = group_id  # type: str
        self.image_url = image_url  # type: str
        self.instance_container_ip = instance_container_ip  # type: str
        self.instance_container_restarts = instance_container_restarts  # type: long
        self.instance_container_status = instance_container_status  # type: str
        self.instance_health_status = instance_health_status  # type: str
        self.instance_id = instance_id  # type: str
        self.package_version = package_version  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationInstancesResponseBodyDataInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time_stamp is not None:
            result['CreateTimeStamp'] = self.create_time_stamp
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.eip is not None:
            result['Eip'] = self.eip
        if self.finish_time_stamp is not None:
            result['FinishTimeStamp'] = self.finish_time_stamp
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.instance_container_ip is not None:
            result['InstanceContainerIp'] = self.instance_container_ip
        if self.instance_container_restarts is not None:
            result['InstanceContainerRestarts'] = self.instance_container_restarts
        if self.instance_container_status is not None:
            result['InstanceContainerStatus'] = self.instance_container_status
        if self.instance_health_status is not None:
            result['InstanceHealthStatus'] = self.instance_health_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.package_version is not None:
            result['PackageVersion'] = self.package_version
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTimeStamp') is not None:
            self.create_time_stamp = m.get('CreateTimeStamp')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('Eip') is not None:
            self.eip = m.get('Eip')
        if m.get('FinishTimeStamp') is not None:
            self.finish_time_stamp = m.get('FinishTimeStamp')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('InstanceContainerIp') is not None:
            self.instance_container_ip = m.get('InstanceContainerIp')
        if m.get('InstanceContainerRestarts') is not None:
            self.instance_container_restarts = m.get('InstanceContainerRestarts')
        if m.get('InstanceContainerStatus') is not None:
            self.instance_container_status = m.get('InstanceContainerStatus')
        if m.get('InstanceHealthStatus') is not None:
            self.instance_health_status = m.get('InstanceHealthStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class DescribeApplicationInstancesResponseBodyData(TeaModel):
    def __init__(self, current_page=None, instances=None, page_size=None, total_size=None):
        self.current_page = current_page  # type: int
        self.instances = instances  # type: list[DescribeApplicationInstancesResponseBodyDataInstances]
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeApplicationInstancesResponseBodyDataInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeApplicationInstancesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeApplicationInstancesResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationInstancesResponse, self).to_map()
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
            temp_model = DescribeApplicationInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationScalingRuleRequest(TeaModel):
    def __init__(self, app_id=None, scaling_rule_name=None):
        self.app_id = app_id  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetrics(TeaModel):
    def __init__(self, metric_target_average_utilization=None, metric_type=None):
        self.metric_target_average_utilization = metric_target_average_utilization  # type: int
        self.metric_type = metric_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetricMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics(TeaModel):
    def __init__(self, current_value=None, name=None, type=None):
        self.current_value = current_value  # type: long
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics(TeaModel):
    def __init__(self, name=None, next_scale_in_average_utilization=None, next_scale_out_average_utilization=None):
        self.name = name  # type: str
        self.next_scale_in_average_utilization = next_scale_in_average_utilization  # type: int
        self.next_scale_out_average_utilization = next_scale_out_average_utilization  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.next_scale_in_average_utilization is not None:
            result['NextScaleInAverageUtilization'] = self.next_scale_in_average_utilization
        if self.next_scale_out_average_utilization is not None:
            result['NextScaleOutAverageUtilization'] = self.next_scale_out_average_utilization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextScaleInAverageUtilization') is not None:
            self.next_scale_in_average_utilization = m.get('NextScaleInAverageUtilization')
        if m.get('NextScaleOutAverageUtilization') is not None:
            self.next_scale_out_average_utilization = m.get('NextScaleOutAverageUtilization')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus(TeaModel):
    def __init__(self, current_metrics=None, current_replicas=None, desired_replicas=None, last_scale_time=None,
                 next_scale_metrics=None, next_scale_time_period=None):
        self.current_metrics = current_metrics  # type: list[DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics]
        self.current_replicas = current_replicas  # type: long
        self.desired_replicas = desired_replicas  # type: long
        self.last_scale_time = last_scale_time  # type: str
        self.next_scale_metrics = next_scale_metrics  # type: list[DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics]
        self.next_scale_time_period = next_scale_time_period  # type: int

    def validate(self):
        if self.current_metrics:
            for k in self.current_metrics:
                if k:
                    k.validate()
        if self.next_scale_metrics:
            for k in self.next_scale_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k in self.current_metrics:
                result['CurrentMetrics'].append(k.to_map() if k else None)
        if self.current_replicas is not None:
            result['CurrentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['DesiredReplicas'] = self.desired_replicas
        if self.last_scale_time is not None:
            result['LastScaleTime'] = self.last_scale_time
        result['NextScaleMetrics'] = []
        if self.next_scale_metrics is not None:
            for k in self.next_scale_metrics:
                result['NextScaleMetrics'].append(k.to_map() if k else None)
        if self.next_scale_time_period is not None:
            result['NextScaleTimePeriod'] = self.next_scale_time_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k in m.get('CurrentMetrics'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k))
        if m.get('CurrentReplicas') is not None:
            self.current_replicas = m.get('CurrentReplicas')
        if m.get('DesiredReplicas') is not None:
            self.desired_replicas = m.get('DesiredReplicas')
        if m.get('LastScaleTime') is not None:
            self.last_scale_time = m.get('LastScaleTime')
        self.next_scale_metrics = []
        if m.get('NextScaleMetrics') is not None:
            for k in m.get('NextScaleMetrics'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatusNextScaleMetrics()
                self.next_scale_metrics.append(temp_model.from_map(k))
        if m.get('NextScaleTimePeriod') is not None:
            self.next_scale_time_period = m.get('NextScaleTimePeriod')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules(TeaModel):
    def __init__(self, disabled=None, stabilization_window_seconds=None, step=None):
        self.disabled = disabled  # type: bool
        self.stabilization_window_seconds = stabilization_window_seconds  # type: long
        self.step = step  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules(TeaModel):
    def __init__(self, disabled=None, stabilization_window_seconds=None, step=None):
        self.disabled = disabled  # type: bool
        self.stabilization_window_seconds = stabilization_window_seconds  # type: long
        self.step = step  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRuleResponseBodyDataMetric(TeaModel):
    def __init__(self, max_replicas=None, metrics=None, metrics_status=None, min_replicas=None,
                 scale_down_rules=None, scale_up_rules=None):
        self.max_replicas = max_replicas  # type: int
        self.metrics = metrics  # type: list[DescribeApplicationScalingRuleResponseBodyDataMetricMetrics]
        self.metrics_status = metrics_status  # type: DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus
        self.min_replicas = min_replicas  # type: int
        self.scale_down_rules = scale_down_rules  # type: DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules
        self.scale_up_rules = scale_up_rules  # type: DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.metrics_status:
            self.metrics_status.validate()
        if self.scale_down_rules:
            self.scale_down_rules.validate()
        if self.scale_up_rules:
            self.scale_up_rules.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.metrics_status is not None:
            result['MetricsStatus'] = self.metrics_status.to_map()
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.scale_down_rules is not None:
            result['ScaleDownRules'] = self.scale_down_rules.to_map()
        if self.scale_up_rules is not None:
            result['ScaleUpRules'] = self.scale_up_rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MetricsStatus') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricMetricsStatus()
            self.metrics_status = temp_model.from_map(m['MetricsStatus'])
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('ScaleDownRules') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m['ScaleDownRules'])
        if m.get('ScaleUpRules') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetricScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m['ScaleUpRules'])
        return self


class DescribeApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(self, at_time=None, target_replicas=None):
        self.at_time = at_time  # type: str
        self.target_replicas = target_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataTimerSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class DescribeApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(self, begin_date=None, end_date=None, period=None, schedules=None):
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.period = period  # type: str
        self.schedules = schedules  # type: list[DescribeApplicationScalingRuleResponseBodyDataTimerSchedules]

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyDataTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = DescribeApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class DescribeApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(self, app_id=None, create_time=None, last_disable_time=None, metric=None, scale_rule_enabled=None,
                 scale_rule_name=None, scale_rule_type=None, timer=None, update_time=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: long
        self.last_disable_time = last_disable_time  # type: long
        self.metric = metric  # type: DescribeApplicationScalingRuleResponseBodyDataMetric
        self.scale_rule_enabled = scale_rule_enabled  # type: bool
        self.scale_rule_name = scale_rule_name  # type: str
        self.scale_rule_type = scale_rule_type  # type: str
        self.timer = timer  # type: DescribeApplicationScalingRuleResponseBodyDataTimer
        self.update_time = update_time  # type: long

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeApplicationScalingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, trace_id=None):
        self.data = data  # type: DescribeApplicationScalingRuleResponseBodyData
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationScalingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRuleResponse, self).to_map()
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
            temp_model = DescribeApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationScalingRulesRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics(TeaModel):
    def __init__(self, metric_target_average_utilization=None, metric_type=None):
        self.metric_target_average_utilization = metric_target_average_utilization  # type: int
        self.metric_type = metric_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics(TeaModel):
    def __init__(self, current_value=None, name=None, type=None):
        self.current_value = current_value  # type: long
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics(TeaModel):
    def __init__(self, name=None, next_scale_in_average_utilization=None, next_scale_out_average_utilization=None):
        self.name = name  # type: str
        self.next_scale_in_average_utilization = next_scale_in_average_utilization  # type: int
        self.next_scale_out_average_utilization = next_scale_out_average_utilization  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.next_scale_in_average_utilization is not None:
            result['NextScaleInAverageUtilization'] = self.next_scale_in_average_utilization
        if self.next_scale_out_average_utilization is not None:
            result['NextScaleOutAverageUtilization'] = self.next_scale_out_average_utilization
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextScaleInAverageUtilization') is not None:
            self.next_scale_in_average_utilization = m.get('NextScaleInAverageUtilization')
        if m.get('NextScaleOutAverageUtilization') is not None:
            self.next_scale_out_average_utilization = m.get('NextScaleOutAverageUtilization')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus(TeaModel):
    def __init__(self, current_metrics=None, current_replicas=None, desired_replicas=None, last_scale_time=None,
                 max_replicas=None, min_replicas=None, next_scale_metrics=None, next_scale_time_period=None):
        self.current_metrics = current_metrics  # type: list[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics]
        self.current_replicas = current_replicas  # type: long
        self.desired_replicas = desired_replicas  # type: long
        self.last_scale_time = last_scale_time  # type: str
        self.max_replicas = max_replicas  # type: long
        self.min_replicas = min_replicas  # type: long
        self.next_scale_metrics = next_scale_metrics  # type: list[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics]
        self.next_scale_time_period = next_scale_time_period  # type: int

    def validate(self):
        if self.current_metrics:
            for k in self.current_metrics:
                if k:
                    k.validate()
        if self.next_scale_metrics:
            for k in self.next_scale_metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CurrentMetrics'] = []
        if self.current_metrics is not None:
            for k in self.current_metrics:
                result['CurrentMetrics'].append(k.to_map() if k else None)
        if self.current_replicas is not None:
            result['CurrentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['DesiredReplicas'] = self.desired_replicas
        if self.last_scale_time is not None:
            result['LastScaleTime'] = self.last_scale_time
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        result['NextScaleMetrics'] = []
        if self.next_scale_metrics is not None:
            for k in self.next_scale_metrics:
                result['NextScaleMetrics'].append(k.to_map() if k else None)
        if self.next_scale_time_period is not None:
            result['NextScaleTimePeriod'] = self.next_scale_time_period
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.current_metrics = []
        if m.get('CurrentMetrics') is not None:
            for k in m.get('CurrentMetrics'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusCurrentMetrics()
                self.current_metrics.append(temp_model.from_map(k))
        if m.get('CurrentReplicas') is not None:
            self.current_replicas = m.get('CurrentReplicas')
        if m.get('DesiredReplicas') is not None:
            self.desired_replicas = m.get('DesiredReplicas')
        if m.get('LastScaleTime') is not None:
            self.last_scale_time = m.get('LastScaleTime')
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        self.next_scale_metrics = []
        if m.get('NextScaleMetrics') is not None:
            for k in m.get('NextScaleMetrics'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatusNextScaleMetrics()
                self.next_scale_metrics.append(temp_model.from_map(k))
        if m.get('NextScaleTimePeriod') is not None:
            self.next_scale_time_period = m.get('NextScaleTimePeriod')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules(TeaModel):
    def __init__(self, disabled=None, stabilization_window_seconds=None, step=None):
        self.disabled = disabled  # type: bool
        self.stabilization_window_seconds = stabilization_window_seconds  # type: long
        self.step = step  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules(TeaModel):
    def __init__(self, disabled=None, stabilization_window_seconds=None, step=None):
        self.disabled = disabled  # type: bool
        self.stabilization_window_seconds = stabilization_window_seconds  # type: long
        self.step = step  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.stabilization_window_seconds is not None:
            result['StabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.step is not None:
            result['Step'] = self.step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('StabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('StabilizationWindowSeconds')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric(TeaModel):
    def __init__(self, max_replicas=None, metrics=None, metrics_status=None, min_replicas=None,
                 scale_down_rules=None, scale_up_rules=None):
        self.max_replicas = max_replicas  # type: int
        self.metrics = metrics  # type: list[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics]
        self.metrics_status = metrics_status  # type: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus
        self.min_replicas = min_replicas  # type: int
        self.scale_down_rules = scale_down_rules  # type: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules
        self.scale_up_rules = scale_up_rules  # type: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.metrics_status:
            self.metrics_status.validate()
        if self.scale_down_rules:
            self.scale_down_rules.validate()
        if self.scale_up_rules:
            self.scale_up_rules.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.metrics_status is not None:
            result['MetricsStatus'] = self.metrics_status.to_map()
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.scale_down_rules is not None:
            result['ScaleDownRules'] = self.scale_down_rules.to_map()
        if self.scale_up_rules is not None:
            result['ScaleUpRules'] = self.scale_up_rules.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MetricsStatus') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricMetricsStatus()
            self.metrics_status = temp_model.from_map(m['MetricsStatus'])
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('ScaleDownRules') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleDownRules()
            self.scale_down_rules = temp_model.from_map(m['ScaleDownRules'])
        if m.get('ScaleUpRules') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetricScaleUpRules()
            self.scale_up_rules = temp_model.from_map(m['ScaleUpRules'])
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules(TeaModel):
    def __init__(self, at_time=None, max_replicas=None, min_replicas=None, target_replicas=None):
        self.at_time = at_time  # type: str
        self.max_replicas = max_replicas  # type: long
        self.min_replicas = min_replicas  # type: long
        self.target_replicas = target_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer(TeaModel):
    def __init__(self, begin_date=None, end_date=None, period=None, schedules=None):
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.period = period  # type: str
        self.schedules = schedules  # type: list[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules]

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules(TeaModel):
    def __init__(self, app_id=None, create_time=None, last_disable_time=None, metric=None, scale_rule_enabled=None,
                 scale_rule_name=None, scale_rule_type=None, timer=None, update_time=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: long
        self.last_disable_time = last_disable_time  # type: long
        self.metric = metric  # type: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric
        self.scale_rule_enabled = scale_rule_enabled  # type: bool
        self.scale_rule_name = scale_rule_name  # type: str
        self.scale_rule_type = scale_rule_type  # type: str
        self.timer = timer  # type: DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer
        self.update_time = update_time  # type: long

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRulesTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeApplicationScalingRulesResponseBodyData(TeaModel):
    def __init__(self, application_scaling_rules=None, current_page=None, page_size=None, total_size=None):
        self.application_scaling_rules = application_scaling_rules  # type: list[DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.application_scaling_rules:
            for k in self.application_scaling_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApplicationScalingRules'] = []
        if self.application_scaling_rules is not None:
            for k in self.application_scaling_rules:
                result['ApplicationScalingRules'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.application_scaling_rules = []
        if m.get('ApplicationScalingRules') is not None:
            for k in m.get('ApplicationScalingRules'):
                temp_model = DescribeApplicationScalingRulesResponseBodyDataApplicationScalingRules()
                self.application_scaling_rules.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeApplicationScalingRulesResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, trace_id=None):
        self.data = data  # type: DescribeApplicationScalingRulesResponseBodyData
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DescribeApplicationScalingRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationScalingRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationScalingRulesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationScalingRulesResponse, self).to_map()
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
            temp_model = DescribeApplicationScalingRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationSlbsRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationSlbsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationSlbsResponseBodyDataInternet(TeaModel):
    def __init__(self, https_cert_id=None, port=None, protocol=None, target_port=None):
        self.https_cert_id = https_cert_id  # type: str
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.target_port = target_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationSlbsResponseBodyDataInternet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeApplicationSlbsResponseBodyDataIntranet(TeaModel):
    def __init__(self, https_cert_id=None, port=None, protocol=None, target_port=None):
        self.https_cert_id = https_cert_id  # type: str
        self.port = port  # type: int
        self.protocol = protocol  # type: str
        self.target_port = target_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationSlbsResponseBodyDataIntranet, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.target_port is not None:
            result['TargetPort'] = self.target_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')
        return self


class DescribeApplicationSlbsResponseBodyData(TeaModel):
    def __init__(self, internet=None, internet_ip=None, internet_slb_id=None, intranet=None, intranet_ip=None,
                 intranet_slb_id=None):
        self.internet = internet  # type: list[DescribeApplicationSlbsResponseBodyDataInternet]
        self.internet_ip = internet_ip  # type: str
        self.internet_slb_id = internet_slb_id  # type: str
        self.intranet = intranet  # type: list[DescribeApplicationSlbsResponseBodyDataIntranet]
        self.intranet_ip = intranet_ip  # type: str
        self.intranet_slb_id = intranet_slb_id  # type: str

    def validate(self):
        if self.internet:
            for k in self.internet:
                if k:
                    k.validate()
        if self.intranet:
            for k in self.intranet:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeApplicationSlbsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Internet'] = []
        if self.internet is not None:
            for k in self.internet:
                result['Internet'].append(k.to_map() if k else None)
        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip
        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id
        result['Intranet'] = []
        if self.intranet is not None:
            for k in self.intranet:
                result['Intranet'].append(k.to_map() if k else None)
        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip
        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.internet = []
        if m.get('Internet') is not None:
            for k in m.get('Internet'):
                temp_model = DescribeApplicationSlbsResponseBodyDataInternet()
                self.internet.append(temp_model.from_map(k))
        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')
        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')
        self.intranet = []
        if m.get('Intranet') is not None:
            for k in m.get('Intranet'):
                temp_model = DescribeApplicationSlbsResponseBodyDataIntranet()
                self.intranet.append(temp_model.from_map(k))
        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')
        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')
        return self


class DescribeApplicationSlbsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeApplicationSlbsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationSlbsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationSlbsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationSlbsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationSlbsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationSlbsResponse, self).to_map()
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
            temp_model = DescribeApplicationSlbsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeApplicationStatusRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DescribeApplicationStatusResponseBodyData(TeaModel):
    def __init__(self, app_id=None, arms_advanced_enabled=None, arms_apm_info=None, create_time=None,
                 current_status=None, enable_agent=None, file_size_limit=None, last_change_order_id=None,
                 last_change_order_running=None, last_change_order_status=None, running_instances=None, sub_status=None):
        self.app_id = app_id  # type: str
        self.arms_advanced_enabled = arms_advanced_enabled  # type: str
        self.arms_apm_info = arms_apm_info  # type: str
        self.create_time = create_time  # type: str
        self.current_status = current_status  # type: str
        self.enable_agent = enable_agent  # type: bool
        self.file_size_limit = file_size_limit  # type: long
        self.last_change_order_id = last_change_order_id  # type: str
        self.last_change_order_running = last_change_order_running  # type: bool
        self.last_change_order_status = last_change_order_status  # type: str
        self.running_instances = running_instances  # type: int
        self.sub_status = sub_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeApplicationStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.arms_advanced_enabled is not None:
            result['ArmsAdvancedEnabled'] = self.arms_advanced_enabled
        if self.arms_apm_info is not None:
            result['ArmsApmInfo'] = self.arms_apm_info
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_status is not None:
            result['CurrentStatus'] = self.current_status
        if self.enable_agent is not None:
            result['EnableAgent'] = self.enable_agent
        if self.file_size_limit is not None:
            result['FileSizeLimit'] = self.file_size_limit
        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id
        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running
        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ArmsAdvancedEnabled') is not None:
            self.arms_advanced_enabled = m.get('ArmsAdvancedEnabled')
        if m.get('ArmsApmInfo') is not None:
            self.arms_apm_info = m.get('ArmsApmInfo')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentStatus') is not None:
            self.current_status = m.get('CurrentStatus')
        if m.get('EnableAgent') is not None:
            self.enable_agent = m.get('EnableAgent')
        if m.get('FileSizeLimit') is not None:
            self.file_size_limit = m.get('FileSizeLimit')
        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')
        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')
        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        return self


class DescribeApplicationStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeApplicationStatusResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeApplicationStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeApplicationStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeApplicationStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeApplicationStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeApplicationStatusResponse, self).to_map()
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
            temp_model = DescribeApplicationStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeChangeOrderRequest(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChangeOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class DescribeChangeOrderResponseBodyDataPipelines(TeaModel):
    def __init__(self, batch_type=None, parallel_count=None, pipeline_id=None, pipeline_name=None, start_time=None,
                 status=None, update_time=None):
        self.batch_type = batch_type  # type: int
        self.parallel_count = parallel_count  # type: int
        self.pipeline_id = pipeline_id  # type: str
        self.pipeline_name = pipeline_name  # type: str
        self.start_time = start_time  # type: long
        self.status = status  # type: int
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeChangeOrderResponseBodyDataPipelines, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.parallel_count is not None:
            result['ParallelCount'] = self.parallel_count
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ParallelCount') is not None:
            self.parallel_count = m.get('ParallelCount')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeChangeOrderResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, approval_id=None, auto=None, batch_count=None, batch_type=None,
                 batch_wait_time=None, change_order_id=None, co_type=None, co_type_code=None, create_time=None,
                 current_pipeline_id=None, description=None, error_message=None, pipelines=None, status=None, sub_status=None,
                 support_rollback=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.approval_id = approval_id  # type: str
        self.auto = auto  # type: bool
        self.batch_count = batch_count  # type: int
        self.batch_type = batch_type  # type: str
        self.batch_wait_time = batch_wait_time  # type: int
        self.change_order_id = change_order_id  # type: str
        self.co_type = co_type  # type: str
        self.co_type_code = co_type_code  # type: str
        self.create_time = create_time  # type: str
        self.current_pipeline_id = current_pipeline_id  # type: str
        self.description = description  # type: str
        self.error_message = error_message  # type: str
        self.pipelines = pipelines  # type: list[DescribeChangeOrderResponseBodyDataPipelines]
        self.status = status  # type: int
        self.sub_status = sub_status  # type: int
        self.support_rollback = support_rollback  # type: bool

    def validate(self):
        if self.pipelines:
            for k in self.pipelines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeChangeOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.approval_id is not None:
            result['ApprovalId'] = self.approval_id
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.current_pipeline_id is not None:
            result['CurrentPipelineId'] = self.current_pipeline_id
        if self.description is not None:
            result['Description'] = self.description
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        result['Pipelines'] = []
        if self.pipelines is not None:
            for k in self.pipelines:
                result['Pipelines'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_status is not None:
            result['SubStatus'] = self.sub_status
        if self.support_rollback is not None:
            result['SupportRollback'] = self.support_rollback
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ApprovalId') is not None:
            self.approval_id = m.get('ApprovalId')
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CurrentPipelineId') is not None:
            self.current_pipeline_id = m.get('CurrentPipelineId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        self.pipelines = []
        if m.get('Pipelines') is not None:
            for k in m.get('Pipelines'):
                temp_model = DescribeChangeOrderResponseBodyDataPipelines()
                self.pipelines.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubStatus') is not None:
            self.sub_status = m.get('SubStatus')
        if m.get('SupportRollback') is not None:
            self.support_rollback = m.get('SupportRollback')
        return self


class DescribeChangeOrderResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeChangeOrderResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeChangeOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeChangeOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeChangeOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeChangeOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeChangeOrderResponse, self).to_map()
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
            temp_model = DescribeChangeOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentsRequest(TeaModel):
    def __init__(self, app_id=None, type=None):
        self.app_id = app_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeComponentsResponseBodyData(TeaModel):
    def __init__(self, component_description=None, component_key=None, expired=None, type=None):
        self.component_description = component_description  # type: str
        self.component_key = component_key  # type: str
        self.expired = expired  # type: bool
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_description is not None:
            result['ComponentDescription'] = self.component_description
        if self.component_key is not None:
            result['ComponentKey'] = self.component_key
        if self.expired is not None:
            result['Expired'] = self.expired
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentDescription') is not None:
            self.component_description = m.get('ComponentDescription')
        if m.get('ComponentKey') is not None:
            self.component_key = m.get('ComponentKey')
        if m.get('Expired') is not None:
            self.expired = m.get('Expired')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeComponentsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeComponentsResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeComponentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeComponentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentsResponse, self).to_map()
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
            temp_model = DescribeComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigMapRequest(TeaModel):
    def __init__(self, config_map_id=None):
        self.config_map_id = config_map_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class DescribeConfigMapResponseBodyDataRelateApps(TeaModel):
    def __init__(self, app_id=None, app_name=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigMapResponseBodyDataRelateApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class DescribeConfigMapResponseBodyData(TeaModel):
    def __init__(self, config_map_id=None, create_time=None, data=None, description=None, name=None,
                 namespace_id=None, relate_apps=None, update_time=None):
        self.config_map_id = config_map_id  # type: long
        self.create_time = create_time  # type: long
        self.data = data  # type: dict[str, any]
        self.description = description  # type: str
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.relate_apps = relate_apps  # type: list[DescribeConfigMapResponseBodyDataRelateApps]
        self.update_time = update_time  # type: long

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeConfigMapResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = DescribeConfigMapResponseBodyDataRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeConfigMapResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeConfigMapResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeConfigMapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeConfigMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeConfigMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeConfigMapResponse, self).to_map()
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
            temp_model = DescribeConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeConfigurationPriceRequest(TeaModel):
    def __init__(self, cpu=None, memory=None, workload=None):
        self.cpu = cpu  # type: int
        self.memory = memory  # type: int
        self.workload = workload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigurationPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.workload is not None:
            result['Workload'] = self.workload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Workload') is not None:
            self.workload = m.get('Workload')
        return self


class DescribeConfigurationPriceResponseBodyDataBagUsage(TeaModel):
    def __init__(self, cpu=None, mem=None):
        self.cpu = cpu  # type: float
        self.mem = mem  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigurationPriceResponseBodyDataBagUsage, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.mem is not None:
            result['Mem'] = self.mem
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Mem') is not None:
            self.mem = m.get('Mem')
        return self


class DescribeConfigurationPriceResponseBodyDataOrder(TeaModel):
    def __init__(self, discount_amount=None, original_amount=None, rule_ids=None, trade_amount=None):
        self.discount_amount = discount_amount  # type: float
        self.original_amount = original_amount  # type: float
        self.rule_ids = rule_ids  # type: list[str]
        self.trade_amount = trade_amount  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigurationPriceResponseBodyDataOrder, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_amount is not None:
            result['DiscountAmount'] = self.discount_amount
        if self.original_amount is not None:
            result['OriginalAmount'] = self.original_amount
        if self.rule_ids is not None:
            result['RuleIds'] = self.rule_ids
        if self.trade_amount is not None:
            result['TradeAmount'] = self.trade_amount
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiscountAmount') is not None:
            self.discount_amount = m.get('DiscountAmount')
        if m.get('OriginalAmount') is not None:
            self.original_amount = m.get('OriginalAmount')
        if m.get('RuleIds') is not None:
            self.rule_ids = m.get('RuleIds')
        if m.get('TradeAmount') is not None:
            self.trade_amount = m.get('TradeAmount')
        return self


class DescribeConfigurationPriceResponseBodyDataRules(TeaModel):
    def __init__(self, name=None, rule_desc_id=None):
        self.name = name  # type: str
        self.rule_desc_id = rule_desc_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeConfigurationPriceResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.rule_desc_id is not None:
            result['RuleDescId'] = self.rule_desc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RuleDescId') is not None:
            self.rule_desc_id = m.get('RuleDescId')
        return self


class DescribeConfigurationPriceResponseBodyData(TeaModel):
    def __init__(self, bag_usage=None, order=None, rules=None):
        self.bag_usage = bag_usage  # type: DescribeConfigurationPriceResponseBodyDataBagUsage
        self.order = order  # type: DescribeConfigurationPriceResponseBodyDataOrder
        self.rules = rules  # type: list[DescribeConfigurationPriceResponseBodyDataRules]

    def validate(self):
        if self.bag_usage:
            self.bag_usage.validate()
        if self.order:
            self.order.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeConfigurationPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bag_usage is not None:
            result['BagUsage'] = self.bag_usage.to_map()
        if self.order is not None:
            result['Order'] = self.order.to_map()
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BagUsage') is not None:
            temp_model = DescribeConfigurationPriceResponseBodyDataBagUsage()
            self.bag_usage = temp_model.from_map(m['BagUsage'])
        if m.get('Order') is not None:
            temp_model = DescribeConfigurationPriceResponseBodyDataOrder()
            self.order = temp_model.from_map(m['Order'])
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeConfigurationPriceResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeConfigurationPriceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeConfigurationPriceResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeConfigurationPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeConfigurationPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeConfigurationPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeConfigurationPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeConfigurationPriceResponse, self).to_map()
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
            temp_model = DescribeConfigurationPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdasContainersResponseBodyData(TeaModel):
    def __init__(self, disabled=None, edas_container_version=None):
        self.disabled = disabled  # type: bool
        self.edas_container_version = edas_container_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEdasContainersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')
        return self


class DescribeEdasContainersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeEdasContainersResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEdasContainersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeEdasContainersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeEdasContainersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEdasContainersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEdasContainersResponse, self).to_map()
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
            temp_model = DescribeEdasContainersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGreyTagRouteRequest(TeaModel):
    def __init__(self, grey_tag_route_id=None):
        # 规则ID
        self.grey_tag_route_id = grey_tag_route_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGreyTagRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class DescribeGreyTagRouteResponseBodyDataDubboRulesItems(TeaModel):
    def __init__(self, cond=None, expr=None, index=None, name=None, operator=None, type=None, value=None):
        self.cond = cond  # type: str
        self.expr = expr  # type: str
        self.index = index  # type: int
        # abandon
        self.name = name  # type: str
        self.operator = operator  # type: str
        # abandon
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponseBodyDataDubboRulesItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataDubboRules(TeaModel):
    def __init__(self, condition=None, group=None, items=None, method_name=None, service_name=None, version=None):
        self.condition = condition  # type: str
        self.group = group  # type: str
        self.items = items  # type: list[DescribeGreyTagRouteResponseBodyDataDubboRulesItems]
        self.method_name = method_name  # type: str
        self.service_name = service_name  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponseBodyDataDubboRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.group is not None:
            result['group'] = self.group
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('group') is not None:
            self.group = m.get('group')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataDubboRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeGreyTagRouteResponseBodyDataScRulesItems(TeaModel):
    def __init__(self, cond=None, expr=None, index=None, name=None, operator=None, type=None, value=None):
        self.cond = cond  # type: str
        # abandon
        self.expr = expr  # type: str
        # abandon
        self.index = index  # type: int
        self.name = name  # type: str
        self.operator = operator  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponseBodyDataScRulesItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class DescribeGreyTagRouteResponseBodyDataScRules(TeaModel):
    def __init__(self, condition=None, items=None, path=None):
        self.condition = condition  # type: str
        self.items = items  # type: list[DescribeGreyTagRouteResponseBodyDataScRulesItems]
        self.path = path  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponseBodyDataScRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeGreyTagRouteResponseBodyDataScRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class DescribeGreyTagRouteResponseBodyData(TeaModel):
    def __init__(self, app_id=None, create_time=None, description=None, dubbo_rules=None, grey_tag_route_id=None,
                 name=None, sc_rules=None, update_time=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.dubbo_rules = dubbo_rules  # type: list[DescribeGreyTagRouteResponseBodyDataDubboRules]
        self.grey_tag_route_id = grey_tag_route_id  # type: long
        self.name = name  # type: str
        self.sc_rules = sc_rules  # type: list[DescribeGreyTagRouteResponseBodyDataScRules]
        self.update_time = update_time  # type: long

    def validate(self):
        if self.dubbo_rules:
            for k in self.dubbo_rules:
                if k:
                    k.validate()
        if self.sc_rules:
            for k in self.sc_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k in self.dubbo_rules:
                result['DubboRules'].append(k.to_map() if k else None)
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.name is not None:
            result['Name'] = self.name
        result['ScRules'] = []
        if self.sc_rules is not None:
            for k in self.sc_rules:
                result['ScRules'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k in m.get('DubboRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k))
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k in m.get('ScRules'):
                temp_model = DescribeGreyTagRouteResponseBodyDataScRules()
                self.sc_rules.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeGreyTagRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeGreyTagRouteResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeGreyTagRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeGreyTagRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGreyTagRouteResponse, self).to_map()
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
            temp_model = DescribeGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIngressRequest(TeaModel):
    def __init__(self, ingress_id=None):
        self.ingress_id = ingress_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIngressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class DescribeIngressResponseBodyDataDefaultRule(TeaModel):
    def __init__(self, app_id=None, app_name=None, backend_protocol=None, container_port=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.backend_protocol = backend_protocol  # type: str
        self.container_port = container_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIngressResponseBodyDataDefaultRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        return self


class DescribeIngressResponseBodyDataRules(TeaModel):
    def __init__(self, app_id=None, app_name=None, backend_protocol=None, container_port=None, domain=None,
                 path=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.backend_protocol = backend_protocol  # type: str
        self.container_port = container_port  # type: int
        self.domain = domain  # type: str
        self.path = path  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIngressResponseBodyDataRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.backend_protocol is not None:
            result['BackendProtocol'] = self.backend_protocol
        if self.container_port is not None:
            result['ContainerPort'] = self.container_port
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.path is not None:
            result['Path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BackendProtocol') is not None:
            self.backend_protocol = m.get('BackendProtocol')
        if m.get('ContainerPort') is not None:
            self.container_port = m.get('ContainerPort')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Path') is not None:
            self.path = m.get('Path')
        return self


class DescribeIngressResponseBodyData(TeaModel):
    def __init__(self, cert_id=None, default_rule=None, description=None, id=None, listener_port=None,
                 listener_protocol=None, load_balance_type=None, name=None, namespace_id=None, rules=None, slb_id=None, slb_type=None):
        self.cert_id = cert_id  # type: str
        self.default_rule = default_rule  # type: DescribeIngressResponseBodyDataDefaultRule
        self.description = description  # type: str
        self.id = id  # type: long
        self.listener_port = listener_port  # type: int
        self.listener_protocol = listener_protocol  # type: str
        self.load_balance_type = load_balance_type  # type: str
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.rules = rules  # type: list[DescribeIngressResponseBodyDataRules]
        self.slb_id = slb_id  # type: str
        self.slb_type = slb_type  # type: str

    def validate(self):
        if self.default_rule:
            self.default_rule.validate()
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeIngressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DefaultRule') is not None:
            temp_model = DescribeIngressResponseBodyDataDefaultRule()
            self.default_rule = temp_model.from_map(m['DefaultRule'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeIngressResponseBodyDataRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class DescribeIngressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeIngressResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeIngressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeIngressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeIngressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIngressResponse, self).to_map()
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
            temp_model = DescribeIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceLogRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceLogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceLogResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceLogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeInstanceLogResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceLogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceLogResponse, self).to_map()
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
            temp_model = DescribeInstanceLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceSpecificationsResponseBodyData(TeaModel):
    def __init__(self, cpu=None, enable=None, id=None, memory=None, spec_info=None, version=None):
        self.cpu = cpu  # type: int
        self.enable = enable  # type: bool
        self.id = id  # type: int
        self.memory = memory  # type: int
        self.spec_info = spec_info  # type: str
        self.version = version  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceSpecificationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.id is not None:
            result['Id'] = self.id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.spec_info is not None:
            result['SpecInfo'] = self.spec_info
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('SpecInfo') is not None:
            self.spec_info = m.get('SpecInfo')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeInstanceSpecificationsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeInstanceSpecificationsResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecificationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeInstanceSpecificationsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeInstanceSpecificationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceSpecificationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceSpecificationsResponse, self).to_map()
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
            temp_model = DescribeInstanceSpecificationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobStatusRequest(TeaModel):
    def __init__(self, app_id=None, job_id=None):
        self.app_id = app_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobStatusResponseBodyData(TeaModel):
    def __init__(self, active=None, completion_time=None, failed=None, job_id=None, message=None, start_time=None,
                 state=None, succeeded=None):
        self.active = active  # type: long
        self.completion_time = completion_time  # type: long
        self.failed = failed  # type: long
        self.job_id = job_id  # type: str
        self.message = message  # type: str
        self.start_time = start_time  # type: long
        self.state = state  # type: str
        self.succeeded = succeeded  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeJobStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.completion_time is not None:
            result['CompletionTime'] = self.completion_time
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.message is not None:
            result['Message'] = self.message
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.state is not None:
            result['State'] = self.state
        if self.succeeded is not None:
            result['Succeeded'] = self.succeeded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CompletionTime') is not None:
            self.completion_time = m.get('CompletionTime')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Succeeded') is not None:
            self.succeeded = m.get('Succeeded')
        return self


class DescribeJobStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeJobStatusResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeJobStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeJobStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeJobStatusResponse, self).to_map()
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
            temp_model = DescribeJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceRequest(TeaModel):
    def __init__(self, namespace_id=None):
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResponseBodyData(TeaModel):
    def __init__(self, namespace_description=None, namespace_id=None, namespace_name=None, region_id=None):
        self.namespace_description = namespace_description  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNamespaceResponse, self).to_map()
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
            temp_model = DescribeNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceListRequest(TeaModel):
    def __init__(self, contain_custom=None, hybrid_cloud_exclude=None):
        self.contain_custom = contain_custom  # type: bool
        self.hybrid_cloud_exclude = hybrid_cloud_exclude  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contain_custom is not None:
            result['ContainCustom'] = self.contain_custom
        if self.hybrid_cloud_exclude is not None:
            result['HybridCloudExclude'] = self.hybrid_cloud_exclude
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ContainCustom') is not None:
            self.contain_custom = m.get('ContainCustom')
        if m.get('HybridCloudExclude') is not None:
            self.hybrid_cloud_exclude = m.get('HybridCloudExclude')
        return self


class DescribeNamespaceListResponseBodyData(TeaModel):
    def __init__(self, agent_install=None, current=None, custom=None, hybrid_cloud_enable=None, namespace_id=None,
                 namespace_name=None, region_id=None, security_group_id=None, v_switch_id=None, vpc_id=None):
        self.agent_install = agent_install  # type: str
        self.current = current  # type: bool
        self.custom = custom  # type: bool
        self.hybrid_cloud_enable = hybrid_cloud_enable  # type: bool
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.region_id = region_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_install is not None:
            result['AgentInstall'] = self.agent_install
        if self.current is not None:
            result['Current'] = self.current
        if self.custom is not None:
            result['Custom'] = self.custom
        if self.hybrid_cloud_enable is not None:
            result['HybridCloudEnable'] = self.hybrid_cloud_enable
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentInstall') is not None:
            self.agent_install = m.get('AgentInstall')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Custom') is not None:
            self.custom = m.get('Custom')
        if m.get('HybridCloudEnable') is not None:
            self.hybrid_cloud_enable = m.get('HybridCloudEnable')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeNamespaceListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[DescribeNamespaceListResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNamespaceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = DescribeNamespaceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNamespaceListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNamespaceListResponse, self).to_map()
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
            temp_model = DescribeNamespaceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespaceResourcesRequest(TeaModel):
    def __init__(self, namespace_id=None):
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class DescribeNamespaceResourcesResponseBodyData(TeaModel):
    def __init__(self, app_count=None, belong_region=None, description=None, jump_server_app_id=None,
                 jump_server_ip=None, last_change_order_id=None, last_change_order_running=None, last_change_order_status=None,
                 namespace_id=None, namespace_name=None, notification_expired=None, security_group_id=None, tenant_id=None,
                 user_id=None, v_switch_id=None, v_switch_name=None, vpc_id=None, vpc_name=None):
        self.app_count = app_count  # type: long
        self.belong_region = belong_region  # type: str
        self.description = description  # type: str
        self.jump_server_app_id = jump_server_app_id  # type: str
        self.jump_server_ip = jump_server_ip  # type: str
        self.last_change_order_id = last_change_order_id  # type: str
        self.last_change_order_running = last_change_order_running  # type: bool
        self.last_change_order_status = last_change_order_status  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.notification_expired = notification_expired  # type: bool
        self.security_group_id = security_group_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_id = user_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespaceResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_count is not None:
            result['AppCount'] = self.app_count
        if self.belong_region is not None:
            result['BelongRegion'] = self.belong_region
        if self.description is not None:
            result['Description'] = self.description
        if self.jump_server_app_id is not None:
            result['JumpServerAppId'] = self.jump_server_app_id
        if self.jump_server_ip is not None:
            result['JumpServerIp'] = self.jump_server_ip
        if self.last_change_order_id is not None:
            result['LastChangeOrderId'] = self.last_change_order_id
        if self.last_change_order_running is not None:
            result['LastChangeOrderRunning'] = self.last_change_order_running
        if self.last_change_order_status is not None:
            result['LastChangeOrderStatus'] = self.last_change_order_status
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.notification_expired is not None:
            result['NotificationExpired'] = self.notification_expired
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCount') is not None:
            self.app_count = m.get('AppCount')
        if m.get('BelongRegion') is not None:
            self.belong_region = m.get('BelongRegion')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('JumpServerAppId') is not None:
            self.jump_server_app_id = m.get('JumpServerAppId')
        if m.get('JumpServerIp') is not None:
            self.jump_server_ip = m.get('JumpServerIp')
        if m.get('LastChangeOrderId') is not None:
            self.last_change_order_id = m.get('LastChangeOrderId')
        if m.get('LastChangeOrderRunning') is not None:
            self.last_change_order_running = m.get('LastChangeOrderRunning')
        if m.get('LastChangeOrderStatus') is not None:
            self.last_change_order_status = m.get('LastChangeOrderStatus')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NotificationExpired') is not None:
            self.notification_expired = m.get('NotificationExpired')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class DescribeNamespaceResourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeNamespaceResourcesResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeNamespaceResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespaceResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespaceResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNamespaceResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNamespaceResourcesResponse, self).to_map()
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
            temp_model = DescribeNamespaceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNamespacesRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class DescribeNamespacesResponseBodyDataNamespaces(TeaModel):
    def __init__(self, access_key=None, namespace_description=None, namespace_id=None, namespace_name=None,
                 region_id=None, secret_key=None, tenant_id=None):
        self.access_key = access_key  # type: str
        self.namespace_description = namespace_description  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.region_id = region_id  # type: str
        self.secret_key = secret_key  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeNamespacesResponseBodyDataNamespaces, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key is not None:
            result['AccessKey'] = self.access_key
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeNamespacesResponseBodyData(TeaModel):
    def __init__(self, current_page=None, namespaces=None, page_size=None, total_size=None):
        self.current_page = current_page  # type: int
        self.namespaces = namespaces  # type: list[DescribeNamespacesResponseBodyDataNamespaces]
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeNamespacesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = DescribeNamespacesResponseBodyDataNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class DescribeNamespacesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribeNamespacesResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribeNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribeNamespacesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribeNamespacesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeNamespacesResponse, self).to_map()
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
            temp_model = DescribeNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePipelineRequest(TeaModel):
    def __init__(self, pipeline_id=None):
        self.pipeline_id = pipeline_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePipelineRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        return self


class DescribePipelineResponseBodyDataStageListTaskList(TeaModel):
    def __init__(self, error_code=None, error_ignore=None, error_message=None, message=None,
                 show_manual_ignore=None, stage_id=None, status=None, task_id=None, task_name=None):
        self.error_code = error_code  # type: str
        self.error_ignore = error_ignore  # type: int
        self.error_message = error_message  # type: str
        self.message = message  # type: str
        self.show_manual_ignore = show_manual_ignore  # type: bool
        self.stage_id = stage_id  # type: str
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePipelineResponseBodyDataStageListTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_ignore is not None:
            result['ErrorIgnore'] = self.error_ignore
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.show_manual_ignore is not None:
            result['ShowManualIgnore'] = self.show_manual_ignore
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorIgnore') is not None:
            self.error_ignore = m.get('ErrorIgnore')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ShowManualIgnore') is not None:
            self.show_manual_ignore = m.get('ShowManualIgnore')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class DescribePipelineResponseBodyDataStageList(TeaModel):
    def __init__(self, executor_type=None, stage_id=None, stage_name=None, status=None, task_list=None):
        self.executor_type = executor_type  # type: int
        self.stage_id = stage_id  # type: str
        self.stage_name = stage_name  # type: str
        self.status = status  # type: int
        self.task_list = task_list  # type: list[DescribePipelineResponseBodyDataStageListTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePipelineResponseBodyDataStageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.executor_type is not None:
            result['ExecutorType'] = self.executor_type
        if self.stage_id is not None:
            result['StageId'] = self.stage_id
        if self.stage_name is not None:
            result['StageName'] = self.stage_name
        if self.status is not None:
            result['Status'] = self.status
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExecutorType') is not None:
            self.executor_type = m.get('ExecutorType')
        if m.get('StageId') is not None:
            self.stage_id = m.get('StageId')
        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = DescribePipelineResponseBodyDataStageListTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class DescribePipelineResponseBodyData(TeaModel):
    def __init__(self, co_status=None, current_stage_id=None, next_pipeline_id=None, pipeline_id=None,
                 pipeline_name=None, pipeline_status=None, show_batch=None, stage_list=None):
        self.co_status = co_status  # type: str
        self.current_stage_id = current_stage_id  # type: str
        self.next_pipeline_id = next_pipeline_id  # type: str
        self.pipeline_id = pipeline_id  # type: str
        self.pipeline_name = pipeline_name  # type: str
        self.pipeline_status = pipeline_status  # type: int
        self.show_batch = show_batch  # type: bool
        self.stage_list = stage_list  # type: list[DescribePipelineResponseBodyDataStageList]

    def validate(self):
        if self.stage_list:
            for k in self.stage_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePipelineResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.current_stage_id is not None:
            result['CurrentStageId'] = self.current_stage_id
        if self.next_pipeline_id is not None:
            result['NextPipelineId'] = self.next_pipeline_id
        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id
        if self.pipeline_name is not None:
            result['PipelineName'] = self.pipeline_name
        if self.pipeline_status is not None:
            result['PipelineStatus'] = self.pipeline_status
        if self.show_batch is not None:
            result['ShowBatch'] = self.show_batch
        result['StageList'] = []
        if self.stage_list is not None:
            for k in self.stage_list:
                result['StageList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CurrentStageId') is not None:
            self.current_stage_id = m.get('CurrentStageId')
        if m.get('NextPipelineId') is not None:
            self.next_pipeline_id = m.get('NextPipelineId')
        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')
        if m.get('PipelineName') is not None:
            self.pipeline_name = m.get('PipelineName')
        if m.get('PipelineStatus') is not None:
            self.pipeline_status = m.get('PipelineStatus')
        if m.get('ShowBatch') is not None:
            self.show_batch = m.get('ShowBatch')
        self.stage_list = []
        if m.get('StageList') is not None:
            for k in m.get('StageList'):
                temp_model = DescribePipelineResponseBodyDataStageList()
                self.stage_list.append(temp_model.from_map(k))
        return self


class DescribePipelineResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: DescribePipelineResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DescribePipelineResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = DescribePipelineResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DescribePipelineResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePipelineResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePipelineResponse, self).to_map()
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
            temp_model = DescribePipelineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegionsRegionRecommendZones(TeaModel):
    def __init__(self, recommend_zone=None):
        self.recommend_zone = recommend_zone  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegionRecommendZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.recommend_zone is not None:
            result['RecommendZone'] = self.recommend_zone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RecommendZone') is not None:
            self.recommend_zone = m.get('RecommendZone')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, recommend_zones=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.recommend_zones = recommend_zones  # type: DescribeRegionsResponseBodyRegionsRegionRecommendZones
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        if self.recommend_zones:
            self.recommend_zones.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.recommend_zones is not None:
            result['RecommendZones'] = self.recommend_zones.to_map()
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RecommendZones') is not None:
            temp_model = DescribeRegionsResponseBodyRegionsRegionRecommendZones()
            self.recommend_zones = temp_model.from_map(m['RecommendZones'])
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, regions=None, request_id=None):
        self.code = code  # type: int
        self.message = message  # type: str
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
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
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableApplicationScalingRuleRequest(TeaModel):
    def __init__(self, app_id=None, scaling_rule_name=None):
        self.app_id = app_id  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationScalingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class DisableApplicationScalingRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_id=None):
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableApplicationScalingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class DisableApplicationScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableApplicationScalingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableApplicationScalingRuleResponse, self).to_map()
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
            temp_model = DisableApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableApplicationScalingRuleRequest(TeaModel):
    def __init__(self, app_id=None, scaling_rule_name=None):
        self.app_id = app_id  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationScalingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        return self


class EnableApplicationScalingRuleResponseBody(TeaModel):
    def __init__(self, request_id=None, trace_id=None):
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableApplicationScalingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class EnableApplicationScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableApplicationScalingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableApplicationScalingRuleResponse, self).to_map()
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
            temp_model = EnableApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecJobRequest(TeaModel):
    def __init__(self, app_id=None, command=None, command_args=None, envs=None, event_id=None, jar_start_args=None,
                 jar_start_options=None, war_start_options=None):
        self.app_id = app_id  # type: str
        self.command = command  # type: str
        self.command_args = command_args  # type: str
        self.envs = envs  # type: str
        self.event_id = event_id  # type: str
        self.jar_start_args = jar_start_args  # type: str
        self.jar_start_options = jar_start_options  # type: str
        self.war_start_options = war_start_options  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.command is not None:
            result['Command'] = self.command
        if self.command_args is not None:
            result['CommandArgs'] = self.command_args
        if self.envs is not None:
            result['Envs'] = self.envs
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args
        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options
        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')
        if m.get('Envs') is not None:
            self.envs = m.get('Envs')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')
        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')
        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')
        return self


class ExecJobResponseBodyData(TeaModel):
    def __init__(self, code=None, data=None, msg=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.msg = msg  # type: str
        self.success = success  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExecJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ExecJobResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExecJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ExecJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ExecJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExecJobResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecJobResponse, self).to_map()
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
            temp_model = ExecJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppEventsRequest(TeaModel):
    def __init__(self, app_id=None, current_page=None, event_type=None, namespace=None, object_kind=None,
                 object_name=None, page_size=None, reason=None):
        self.app_id = app_id  # type: str
        self.current_page = current_page  # type: int
        self.event_type = event_type  # type: str
        self.namespace = namespace  # type: str
        self.object_kind = object_kind  # type: str
        self.object_name = object_name  # type: str
        self.page_size = page_size  # type: int
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListAppEventsResponseBodyDataAppEventEntity(TeaModel):
    def __init__(self, event_type=None, first_timestamp=None, last_timestamp=None, message=None, object_kind=None,
                 object_name=None, reason=None):
        self.event_type = event_type  # type: str
        self.first_timestamp = first_timestamp  # type: str
        self.last_timestamp = last_timestamp  # type: str
        self.message = message  # type: str
        self.object_kind = object_kind  # type: str
        self.object_name = object_name  # type: str
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppEventsResponseBodyDataAppEventEntity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.message is not None:
            result['Message'] = self.message
        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind
        if self.object_name is not None:
            result['ObjectName'] = self.object_name
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')
        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListAppEventsResponseBodyData(TeaModel):
    def __init__(self, app_event_entity=None, current_page=None, page_size=None, total_size=None):
        self.app_event_entity = app_event_entity  # type: list[ListAppEventsResponseBodyDataAppEventEntity]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.app_event_entity:
            for k in self.app_event_entity:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppEventEntity'] = []
        if self.app_event_entity is not None:
            for k in self.app_event_entity:
                result['AppEventEntity'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_event_entity = []
        if m.get('AppEventEntity') is not None:
            for k in m.get('AppEventEntity'):
                temp_model = ListAppEventsResponseBodyDataAppEventEntity()
                self.app_event_entity.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAppEventsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListAppEventsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListAppEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = ListAppEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppEventsResponse, self).to_map()
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
            temp_model = ListAppEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppServicesPageRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, service_type=None):
        self.app_id = app_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.service_type = service_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppServicesPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        return self


class ListAppServicesPageResponseBodyDataResult(TeaModel):
    def __init__(self, edas_app_id=None, edas_app_name=None, group=None, instance_num=None, service_name=None,
                 version=None):
        self.edas_app_id = edas_app_id  # type: str
        self.edas_app_name = edas_app_name  # type: str
        self.group = group  # type: str
        self.instance_num = instance_num  # type: long
        self.service_name = service_name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppServicesPageResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edas_app_id is not None:
            result['EdasAppId'] = self.edas_app_id
        if self.edas_app_name is not None:
            result['EdasAppName'] = self.edas_app_name
        if self.group is not None:
            result['Group'] = self.group
        if self.instance_num is not None:
            result['InstanceNum'] = self.instance_num
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EdasAppId') is not None:
            self.edas_app_id = m.get('EdasAppId')
        if m.get('EdasAppName') is not None:
            self.edas_app_name = m.get('EdasAppName')
        if m.get('Group') is not None:
            self.group = m.get('Group')
        if m.get('InstanceNum') is not None:
            self.instance_num = m.get('InstanceNum')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListAppServicesPageResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_number=None, page_size=None, result=None, total_size=None):
        self.current_page = current_page  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.result = result  # type: list[ListAppServicesPageResponseBodyDataResult]
        self.total_size = total_size  # type: str

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppServicesPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAppServicesPageResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAppServicesPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListAppServicesPageResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppServicesPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppServicesPageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListAppServicesPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppServicesPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppServicesPageResponse, self).to_map()
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
            temp_model = ListAppServicesPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppVersionsRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListAppVersionsResponseBodyData(TeaModel):
    def __init__(self, build_package_url=None, create_time=None, id=None, type=None, war_url=None):
        self.build_package_url = build_package_url  # type: str
        self.create_time = create_time  # type: str
        self.id = id  # type: str
        self.type = type  # type: str
        self.war_url = war_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_package_url is not None:
            result['BuildPackageUrl'] = self.build_package_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.type is not None:
            result['Type'] = self.type
        if self.war_url is not None:
            result['WarUrl'] = self.war_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildPackageUrl') is not None:
            self.build_package_url = m.get('BuildPackageUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')
        return self


class ListAppVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListAppVersionsResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAppVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppVersionsResponse, self).to_map()
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
            temp_model = ListAppVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplicationsRequest(TeaModel):
    def __init__(self, app_name=None, current_page=None, field_type=None, field_value=None, namespace_id=None,
                 order_by=None, page_size=None, reverse=None, tags=None):
        self.app_name = app_name  # type: str
        self.current_page = current_page  # type: int
        self.field_type = field_type  # type: str
        self.field_value = field_value  # type: str
        self.namespace_id = namespace_id  # type: str
        self.order_by = order_by  # type: str
        self.page_size = page_size  # type: int
        self.reverse = reverse  # type: bool
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.field_type is not None:
            result['FieldType'] = self.field_type
        if self.field_value is not None:
            result['FieldValue'] = self.field_value
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('FieldType') is not None:
            self.field_type = m.get('FieldType')
        if m.get('FieldValue') is not None:
            self.field_value = m.get('FieldValue')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListApplicationsResponseBodyDataApplicationsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplicationsResponseBodyDataApplicationsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListApplicationsResponseBodyDataApplications(TeaModel):
    def __init__(self, app_deleting_status=None, app_description=None, app_id=None, app_name=None, instances=None,
                 namespace_id=None, region_id=None, running_instances=None, tags=None):
        self.app_deleting_status = app_deleting_status  # type: bool
        self.app_description = app_description  # type: str
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.instances = instances  # type: int
        self.namespace_id = namespace_id  # type: str
        self.region_id = region_id  # type: str
        self.running_instances = running_instances  # type: int
        self.tags = tags  # type: list[ListApplicationsResponseBodyDataApplicationsTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBodyDataApplications, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_deleting_status is not None:
            result['AppDeletingStatus'] = self.app_deleting_status
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.instances is not None:
            result['Instances'] = self.instances
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppDeletingStatus') is not None:
            self.app_deleting_status = m.get('AppDeletingStatus')
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Instances') is not None:
            self.instances = m.get('Instances')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListApplicationsResponseBodyDataApplicationsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListApplicationsResponseBodyData(TeaModel):
    def __init__(self, applications=None, current_page=None, page_size=None, total_size=None):
        self.applications = applications  # type: list[ListApplicationsResponseBodyDataApplications]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.applications:
            for k in self.applications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Applications'] = []
        if self.applications is not None:
            for k in self.applications:
                result['Applications'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k in m.get('Applications'):
                temp_model = ListApplicationsResponseBodyDataApplications()
                self.applications.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListApplicationsResponseBody(TeaModel):
    def __init__(self, code=None, current_page=None, data=None, error_code=None, message=None, page_size=None,
                 request_id=None, success=None, total_size=None):
        self.code = code  # type: str
        self.current_page = current_page  # type: int
        self.data = data  # type: ListApplicationsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total_size = total_size  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListApplicationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Data') is not None:
            temp_model = ListApplicationsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListApplicationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplicationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplicationsResponse, self).to_map()
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
            temp_model = ListApplicationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChangeOrdersRequest(TeaModel):
    def __init__(self, app_id=None, co_status=None, co_type=None, current_page=None, key=None, page_size=None):
        self.app_id = app_id  # type: str
        self.co_status = co_status  # type: str
        self.co_type = co_type  # type: str
        self.current_page = current_page  # type: int
        self.key = key  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChangeOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key is not None:
            result['Key'] = self.key
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChangeOrdersResponseBodyDataChangeOrderList(TeaModel):
    def __init__(self, app_id=None, batch_count=None, batch_type=None, change_order_id=None, co_type=None,
                 co_type_code=None, create_time=None, create_user_id=None, description=None, finish_time=None, group_id=None,
                 source=None, status=None, user_id=None):
        self.app_id = app_id  # type: str
        self.batch_count = batch_count  # type: int
        self.batch_type = batch_type  # type: str
        self.change_order_id = change_order_id  # type: str
        self.co_type = co_type  # type: str
        self.co_type_code = co_type_code  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.description = description  # type: str
        self.finish_time = finish_time  # type: str
        self.group_id = group_id  # type: str
        self.source = source  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListChangeOrdersResponseBodyDataChangeOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.description is not None:
            result['Description'] = self.description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListChangeOrdersResponseBodyData(TeaModel):
    def __init__(self, change_order_list=None, current_page=None, page_size=None, total_size=None):
        self.change_order_list = change_order_list  # type: list[ListChangeOrdersResponseBodyDataChangeOrderList]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.change_order_list:
            for k in self.change_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListChangeOrdersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k in self.change_order_list:
                result['ChangeOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k in m.get('ChangeOrderList'):
                temp_model = ListChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListChangeOrdersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListChangeOrdersResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListChangeOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListChangeOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListChangeOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListChangeOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListChangeOrdersResponse, self).to_map()
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
            temp_model = ListChangeOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConsumedServicesRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConsumedServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListConsumedServicesResponseBodyData(TeaModel):
    def __init__(self, app_id=None, group_2ip=None, groups=None, ips=None, name=None, type=None, version=None):
        self.app_id = app_id  # type: str
        self.group_2ip = group_2ip  # type: str
        self.groups = groups  # type: list[str]
        self.ips = ips  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListConsumedServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListConsumedServicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListConsumedServicesResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListConsumedServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListConsumedServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListConsumedServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListConsumedServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListConsumedServicesResponse, self).to_map()
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
            temp_model = ListConsumedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGreyTagRouteRequest(TeaModel):
    def __init__(self, app_id=None):
        # 应用ID
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGreyTagRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListGreyTagRouteResponseBodyDataResultDubboRulesItems(TeaModel):
    def __init__(self, cond=None, expr=None, index=None, name=None, operator=None, type=None, value=None):
        self.cond = cond  # type: str
        self.expr = expr  # type: str
        self.index = index  # type: int
        # abandon
        self.name = name  # type: str
        self.operator = operator  # type: str
        # abandon
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBodyDataResultDubboRulesItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultDubboRules(TeaModel):
    def __init__(self, condition=None, group=None, items=None, method_name=None, service_name=None, version=None):
        self.condition = condition  # type: str
        self.group = group  # type: str
        self.items = items  # type: list[ListGreyTagRouteResponseBodyDataResultDubboRulesItems]
        self.method_name = method_name  # type: str
        self.service_name = service_name  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBodyDataResultDubboRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.group is not None:
            result['group'] = self.group
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.method_name is not None:
            result['methodName'] = self.method_name
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('group') is not None:
            self.group = m.get('group')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultDubboRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListGreyTagRouteResponseBodyDataResultScRulesItems(TeaModel):
    def __init__(self, cond=None, expr=None, index=None, name=None, operator=None, type=None, value=None):
        self.cond = cond  # type: str
        self.expr = expr  # type: str
        # abandon
        self.index = index  # type: int
        self.name = name  # type: str
        self.operator = operator  # type: str
        self.type = type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBodyDataResultScRulesItems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cond is not None:
            result['cond'] = self.cond
        if self.expr is not None:
            result['expr'] = self.expr
        if self.index is not None:
            result['index'] = self.index
        if self.name is not None:
            result['name'] = self.name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListGreyTagRouteResponseBodyDataResultScRules(TeaModel):
    def __init__(self, condition=None, items=None, path=None):
        self.condition = condition  # type: str
        self.items = items  # type: list[ListGreyTagRouteResponseBodyDataResultScRulesItems]
        self.path = path  # type: str

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBodyDataResultScRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListGreyTagRouteResponseBodyDataResultScRulesItems()
                self.items.append(temp_model.from_map(k))
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ListGreyTagRouteResponseBodyDataResult(TeaModel):
    def __init__(self, create_time=None, description=None, dubbo_rules=None, grey_tag_route_id=None, name=None,
                 sc_rules=None, update_time=None):
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.dubbo_rules = dubbo_rules  # type: list[ListGreyTagRouteResponseBodyDataResultDubboRules]
        self.grey_tag_route_id = grey_tag_route_id  # type: long
        self.name = name  # type: str
        self.sc_rules = sc_rules  # type: list[ListGreyTagRouteResponseBodyDataResultScRules]
        self.update_time = update_time  # type: long

    def validate(self):
        if self.dubbo_rules:
            for k in self.dubbo_rules:
                if k:
                    k.validate()
        if self.sc_rules:
            for k in self.sc_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBodyDataResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        result['DubboRules'] = []
        if self.dubbo_rules is not None:
            for k in self.dubbo_rules:
                result['DubboRules'].append(k.to_map() if k else None)
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.name is not None:
            result['Name'] = self.name
        result['ScRules'] = []
        if self.sc_rules is not None:
            for k in self.sc_rules:
                result['ScRules'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.dubbo_rules = []
        if m.get('DubboRules') is not None:
            for k in m.get('DubboRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultDubboRules()
                self.dubbo_rules.append(temp_model.from_map(k))
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sc_rules = []
        if m.get('ScRules') is not None:
            for k in m.get('ScRules'):
                temp_model = ListGreyTagRouteResponseBodyDataResultScRules()
                self.sc_rules.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGreyTagRouteResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_size=None, result=None, total_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.result = result  # type: list[ListGreyTagRouteResponseBodyDataResult]
        self.total_size = total_size  # type: long

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListGreyTagRouteResponseBodyDataResult()
                self.result.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListGreyTagRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListGreyTagRouteResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListGreyTagRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListGreyTagRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGreyTagRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGreyTagRouteResponse, self).to_map()
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
            temp_model = ListGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIngressesRequest(TeaModel):
    def __init__(self, app_id=None, namespace_id=None):
        self.app_id = app_id  # type: str
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIngressesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListIngressesResponseBodyDataIngressList(TeaModel):
    def __init__(self, cert_id=None, description=None, id=None, listener_port=None, listener_protocol=None,
                 load_balance_type=None, name=None, namespace_id=None, slb_id=None, slb_type=None):
        self.cert_id = cert_id  # type: str
        self.description = description  # type: str
        self.id = id  # type: long
        self.listener_port = listener_port  # type: str
        self.listener_protocol = listener_protocol  # type: str
        self.load_balance_type = load_balance_type  # type: str
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.slb_id = slb_id  # type: str
        self.slb_type = slb_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIngressesResponseBodyDataIngressList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.description is not None:
            result['Description'] = self.description
        if self.id is not None:
            result['Id'] = self.id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.slb_id is not None:
            result['SlbId'] = self.slb_id
        if self.slb_type is not None:
            result['SlbType'] = self.slb_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')
        if m.get('SlbType') is not None:
            self.slb_type = m.get('SlbType')
        return self


class ListIngressesResponseBodyData(TeaModel):
    def __init__(self, ingress_list=None):
        self.ingress_list = ingress_list  # type: list[ListIngressesResponseBodyDataIngressList]

    def validate(self):
        if self.ingress_list:
            for k in self.ingress_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIngressesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IngressList'] = []
        if self.ingress_list is not None:
            for k in self.ingress_list:
                result['IngressList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ingress_list = []
        if m.get('IngressList') is not None:
            for k in m.get('IngressList'):
                temp_model = ListIngressesResponseBodyDataIngressList()
                self.ingress_list.append(temp_model.from_map(k))
        return self


class ListIngressesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListIngressesResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListIngressesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListIngressesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListIngressesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIngressesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIngressesResponse, self).to_map()
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
            temp_model = ListIngressesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLogConfigsRequest(TeaModel):
    def __init__(self, app_id=None, current_page=None, page_size=None):
        self.app_id = app_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListLogConfigsResponseBodyDataLogConfigs(TeaModel):
    def __init__(self, config_name=None, create_time=None, log_dir=None, log_type=None, region_id=None,
                 sls_log_store=None, sls_project=None, store_type=None):
        self.config_name = config_name  # type: str
        self.create_time = create_time  # type: str
        self.log_dir = log_dir  # type: str
        self.log_type = log_type  # type: str
        self.region_id = region_id  # type: str
        self.sls_log_store = sls_log_store  # type: str
        self.sls_project = sls_project  # type: str
        self.store_type = store_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLogConfigsResponseBodyDataLogConfigs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_name is not None:
            result['ConfigName'] = self.config_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log_dir is not None:
            result['LogDir'] = self.log_dir
        if self.log_type is not None:
            result['LogType'] = self.log_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sls_log_store is not None:
            result['SlsLogStore'] = self.sls_log_store
        if self.sls_project is not None:
            result['SlsProject'] = self.sls_project
        if self.store_type is not None:
            result['StoreType'] = self.store_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LogDir') is not None:
            self.log_dir = m.get('LogDir')
        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SlsLogStore') is not None:
            self.sls_log_store = m.get('SlsLogStore')
        if m.get('SlsProject') is not None:
            self.sls_project = m.get('SlsProject')
        if m.get('StoreType') is not None:
            self.store_type = m.get('StoreType')
        return self


class ListLogConfigsResponseBodyData(TeaModel):
    def __init__(self, current_page=None, log_configs=None, page_size=None, total_size=None):
        self.current_page = current_page  # type: int
        self.log_configs = log_configs  # type: list[ListLogConfigsResponseBodyDataLogConfigs]
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.log_configs:
            for k in self.log_configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLogConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['LogConfigs'] = []
        if self.log_configs is not None:
            for k in self.log_configs:
                result['LogConfigs'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.log_configs = []
        if m.get('LogConfigs') is not None:
            for k in m.get('LogConfigs'):
                temp_model = ListLogConfigsResponseBodyDataLogConfigs()
                self.log_configs.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListLogConfigsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListLogConfigsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListLogConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListLogConfigsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListLogConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLogConfigsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLogConfigsResponse, self).to_map()
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
            temp_model = ListLogConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespaceChangeOrdersRequest(TeaModel):
    def __init__(self, co_status=None, co_type=None, current_page=None, key=None, namespace_id=None, page_size=None):
        self.co_status = co_status  # type: str
        self.co_type = co_type  # type: str
        self.current_page = current_page  # type: int
        self.key = key  # type: str
        self.namespace_id = namespace_id  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespaceChangeOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.co_status is not None:
            result['CoStatus'] = self.co_status
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.key is not None:
            result['Key'] = self.key
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CoStatus') is not None:
            self.co_status = m.get('CoStatus')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNamespaceChangeOrdersResponseBodyDataChangeOrderList(TeaModel):
    def __init__(self, batch_count=None, batch_type=None, change_order_id=None, co_type=None, co_type_code=None,
                 create_time=None, create_user_id=None, description=None, finish_time=None, group_id=None, namespace_id=None,
                 pipelines=None, source=None, status=None, user_id=None):
        self.batch_count = batch_count  # type: int
        self.batch_type = batch_type  # type: str
        self.change_order_id = change_order_id  # type: str
        self.co_type = co_type  # type: str
        self.co_type_code = co_type_code  # type: str
        self.create_time = create_time  # type: str
        self.create_user_id = create_user_id  # type: str
        self.description = description  # type: str
        self.finish_time = finish_time  # type: str
        self.group_id = group_id  # type: str
        self.namespace_id = namespace_id  # type: str
        self.pipelines = pipelines  # type: str
        self.source = source  # type: str
        self.status = status  # type: int
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespaceChangeOrdersResponseBodyDataChangeOrderList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_count is not None:
            result['BatchCount'] = self.batch_count
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.co_type is not None:
            result['CoType'] = self.co_type
        if self.co_type_code is not None:
            result['CoTypeCode'] = self.co_type_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id
        if self.description is not None:
            result['Description'] = self.description
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.pipelines is not None:
            result['Pipelines'] = self.pipelines
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchCount') is not None:
            self.batch_count = m.get('BatchCount')
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('CoType') is not None:
            self.co_type = m.get('CoType')
        if m.get('CoTypeCode') is not None:
            self.co_type_code = m.get('CoTypeCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('Pipelines') is not None:
            self.pipelines = m.get('Pipelines')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListNamespaceChangeOrdersResponseBodyData(TeaModel):
    def __init__(self, change_order_list=None, current_page=None, page_size=None, total_size=None):
        self.change_order_list = change_order_list  # type: list[ListNamespaceChangeOrdersResponseBodyDataChangeOrderList]
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: int

    def validate(self):
        if self.change_order_list:
            for k in self.change_order_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNamespaceChangeOrdersResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChangeOrderList'] = []
        if self.change_order_list is not None:
            for k in self.change_order_list:
                result['ChangeOrderList'].append(k.to_map() if k else None)
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.change_order_list = []
        if m.get('ChangeOrderList') is not None:
            for k in m.get('ChangeOrderList'):
                temp_model = ListNamespaceChangeOrdersResponseBodyDataChangeOrderList()
                self.change_order_list.append(temp_model.from_map(k))
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListNamespaceChangeOrdersResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListNamespaceChangeOrdersResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNamespaceChangeOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListNamespaceChangeOrdersResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListNamespaceChangeOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNamespaceChangeOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNamespaceChangeOrdersResponse, self).to_map()
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
            temp_model = ListNamespaceChangeOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespacedConfigMapsRequest(TeaModel):
    def __init__(self, namespace_id=None):
        self.namespace_id = namespace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespacedConfigMapsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps(TeaModel):
    def __init__(self, app_id=None, app_name=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ListNamespacedConfigMapsResponseBodyDataConfigMaps(TeaModel):
    def __init__(self, config_map_id=None, create_time=None, data=None, description=None, name=None,
                 namespace_id=None, relate_apps=None, update_time=None):
        self.config_map_id = config_map_id  # type: long
        self.create_time = create_time  # type: long
        self.data = data  # type: dict[str, any]
        self.description = description  # type: str
        self.name = name  # type: str
        self.namespace_id = namespace_id  # type: str
        self.relate_apps = relate_apps  # type: list[ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps]
        self.update_time = update_time  # type: long

    def validate(self):
        if self.relate_apps:
            for k in self.relate_apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNamespacedConfigMapsResponseBodyDataConfigMaps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        result['RelateApps'] = []
        if self.relate_apps is not None:
            for k in self.relate_apps:
                result['RelateApps'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        self.relate_apps = []
        if m.get('RelateApps') is not None:
            for k in m.get('RelateApps'):
                temp_model = ListNamespacedConfigMapsResponseBodyDataConfigMapsRelateApps()
                self.relate_apps.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListNamespacedConfigMapsResponseBodyData(TeaModel):
    def __init__(self, config_maps=None):
        self.config_maps = config_maps  # type: list[ListNamespacedConfigMapsResponseBodyDataConfigMaps]

    def validate(self):
        if self.config_maps:
            for k in self.config_maps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNamespacedConfigMapsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConfigMaps'] = []
        if self.config_maps is not None:
            for k in self.config_maps:
                result['ConfigMaps'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.config_maps = []
        if m.get('ConfigMaps') is not None:
            for k in m.get('ConfigMaps'):
                temp_model = ListNamespacedConfigMapsResponseBodyDataConfigMaps()
                self.config_maps.append(temp_model.from_map(k))
        return self


class ListNamespacedConfigMapsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListNamespacedConfigMapsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListNamespacedConfigMapsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListNamespacedConfigMapsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListNamespacedConfigMapsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNamespacedConfigMapsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNamespacedConfigMapsResponse, self).to_map()
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
            temp_model = ListNamespacedConfigMapsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPublishedServicesRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishedServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class ListPublishedServicesResponseBodyData(TeaModel):
    def __init__(self, app_id=None, group_2ip=None, groups=None, ips=None, name=None, type=None, version=None):
        self.app_id = app_id  # type: str
        self.group_2ip = group_2ip  # type: str
        self.groups = groups  # type: list[str]
        self.ips = ips  # type: list[str]
        self.name = name  # type: str
        self.type = type  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPublishedServicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.group_2ip is not None:
            result['Group2Ip'] = self.group_2ip
        if self.groups is not None:
            result['Groups'] = self.groups
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Group2Ip') is not None:
            self.group_2ip = m.get('Group2Ip')
        if m.get('Groups') is not None:
            self.groups = m.get('Groups')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListPublishedServicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListPublishedServicesResponseBodyData]
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPublishedServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPublishedServicesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListPublishedServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPublishedServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPublishedServicesResponse, self).to_map()
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
            temp_model = ListPublishedServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_ids=None, resource_type=None, tags=None):
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_ids = resource_ids  # type: str
        self.resource_type = resource_type  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class ListTagResourcesResponseBodyDataTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyDataTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyData(TeaModel):
    def __init__(self, next_token=None, tag_resources=None):
        self.next_token = next_token  # type: str
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyDataTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyDataTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ListTagResourcesResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ListTagResourcesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenSaeServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenSaeServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenSaeServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenSaeServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenSaeServiceResponse, self).to_map()
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
            temp_model = OpenSaeServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryResourceStaticsRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryResourceStaticsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class QueryResourceStaticsResponseBodyDataRealTimeRes(TeaModel):
    def __init__(self, cpu=None, memory=None):
        self.cpu = cpu  # type: float
        self.memory = memory  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryResourceStaticsResponseBodyDataRealTimeRes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class QueryResourceStaticsResponseBodyDataSummary(TeaModel):
    def __init__(self, cpu=None, memory=None):
        self.cpu = cpu  # type: float
        self.memory = memory  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryResourceStaticsResponseBodyDataSummary, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class QueryResourceStaticsResponseBodyData(TeaModel):
    def __init__(self, real_time_res=None, summary=None):
        self.real_time_res = real_time_res  # type: QueryResourceStaticsResponseBodyDataRealTimeRes
        self.summary = summary  # type: QueryResourceStaticsResponseBodyDataSummary

    def validate(self):
        if self.real_time_res:
            self.real_time_res.validate()
        if self.summary:
            self.summary.validate()

    def to_map(self):
        _map = super(QueryResourceStaticsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.real_time_res is not None:
            result['RealTimeRes'] = self.real_time_res.to_map()
        if self.summary is not None:
            result['Summary'] = self.summary.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RealTimeRes') is not None:
            temp_model = QueryResourceStaticsResponseBodyDataRealTimeRes()
            self.real_time_res = temp_model.from_map(m['RealTimeRes'])
        if m.get('Summary') is not None:
            temp_model = QueryResourceStaticsResponseBodyDataSummary()
            self.summary = temp_model.from_map(m['Summary'])
        return self


class QueryResourceStaticsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: QueryResourceStaticsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryResourceStaticsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryResourceStaticsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class QueryResourceStaticsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryResourceStaticsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryResourceStaticsResponse, self).to_map()
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
            temp_model = QueryResourceStaticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReduceApplicationCapacityByInstanceIdsRequest(TeaModel):
    def __init__(self, app_id=None, instance_ids=None):
        self.app_id = app_id  # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReduceApplicationCapacityByInstanceIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class ReduceApplicationCapacityByInstanceIdsResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReduceApplicationCapacityByInstanceIdsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class ReduceApplicationCapacityByInstanceIdsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: ReduceApplicationCapacityByInstanceIdsResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ReduceApplicationCapacityByInstanceIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReduceApplicationCapacityByInstanceIdsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class ReduceApplicationCapacityByInstanceIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReduceApplicationCapacityByInstanceIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReduceApplicationCapacityByInstanceIdsResponse, self).to_map()
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
            temp_model = ReduceApplicationCapacityByInstanceIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationRequest(TeaModel):
    def __init__(self, app_id=None, auto_enable_application_scaling_rule=None, min_ready_instance_ratio=None,
                 min_ready_instances=None, replicas=None):
        self.app_id = app_id  # type: str
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule  # type: bool
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int
        self.replicas = replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RescaleApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.replicas is not None:
            result['Replicas'] = self.replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')
        return self


class RescaleApplicationResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RescaleApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RescaleApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: RescaleApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RescaleApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
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
            temp_model = RescaleApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RescaleApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RescaleApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RescaleApplicationResponse, self).to_map()
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
            temp_model = RescaleApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RescaleApplicationVerticallyRequest(TeaModel):
    def __init__(self, app_id=None, cpu=None, memory=None):
        self.app_id = app_id  # type: str
        self.cpu = cpu  # type: str
        self.memory = memory  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RescaleApplicationVerticallyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.cpu is not None:
            result['Cpu'] = self.cpu
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class RescaleApplicationVerticallyResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RescaleApplicationVerticallyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RescaleApplicationVerticallyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: RescaleApplicationVerticallyResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RescaleApplicationVerticallyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RescaleApplicationVerticallyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RescaleApplicationVerticallyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RescaleApplicationVerticallyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RescaleApplicationVerticallyResponse, self).to_map()
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
            temp_model = RescaleApplicationVerticallyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartApplicationRequest(TeaModel):
    def __init__(self, app_id=None, min_ready_instance_ratio=None, min_ready_instances=None):
        self.app_id = app_id  # type: str
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        return self


class RestartApplicationResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RestartApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: RestartApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RestartApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RestartApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RestartApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartApplicationResponse, self).to_map()
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
            temp_model = RestartApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestartInstancesRequest(TeaModel):
    def __init__(self, app_id=None, instance_ids=None):
        self.app_id = app_id  # type: str
        self.instance_ids = instance_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class RestartInstancesResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RestartInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class RestartInstancesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: RestartInstancesResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RestartInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RestartInstancesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RestartInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RestartInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RestartInstancesResponse, self).to_map()
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
            temp_model = RestartInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackApplicationRequest(TeaModel):
    def __init__(self, app_id=None, auto_enable_application_scaling_rule=None, batch_wait_time=None,
                 min_ready_instance_ratio=None, min_ready_instances=None, update_strategy=None, version_id=None):
        self.app_id = app_id  # type: str
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule  # type: str
        self.batch_wait_time = batch_wait_time  # type: int
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int
        self.update_strategy = update_strategy  # type: str
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule
        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')
        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RollbackApplicationResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None, is_need_approval=None):
        self.change_order_id = change_order_id  # type: str
        self.is_need_approval = is_need_approval  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RollbackApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        if self.is_need_approval is not None:
            result['IsNeedApproval'] = self.is_need_approval
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        if m.get('IsNeedApproval') is not None:
            self.is_need_approval = m.get('IsNeedApproval')
        return self


class RollbackApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: RollbackApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RollbackApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = RollbackApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RollbackApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RollbackApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RollbackApplicationResponse, self).to_map()
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
            temp_model = RollbackApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StartApplicationResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class StartApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: StartApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StartApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StartApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartApplicationResponse, self).to_map()
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
            temp_model = StartApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopApplicationRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopApplicationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class StopApplicationResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopApplicationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class StopApplicationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: StopApplicationResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StopApplicationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StopApplicationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class StopApplicationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopApplicationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopApplicationResponse, self).to_map()
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
            temp_model = StopApplicationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_ids=None, resource_type=None, tags=None):
        self.region_id = region_id  # type: str
        self.resource_ids = resource_ids  # type: str
        self.resource_type = resource_type  # type: str
        self.tags = tags  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tags is not None:
            result['Tags'] = self.tags
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindSlbRequest(TeaModel):
    def __init__(self, app_id=None, internet=None, intranet=None):
        self.app_id = app_id  # type: str
        self.internet = internet  # type: bool
        self.intranet = intranet  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindSlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.internet is not None:
            result['Internet'] = self.internet
        if self.intranet is not None:
            result['Intranet'] = self.intranet
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Internet') is not None:
            self.internet = m.get('Internet')
        if m.get('Intranet') is not None:
            self.intranet = m.get('Intranet')
        return self


class UnbindSlbResponseBodyData(TeaModel):
    def __init__(self, change_order_id=None):
        self.change_order_id = change_order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindSlbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.change_order_id is not None:
            result['ChangeOrderId'] = self.change_order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChangeOrderId') is not None:
            self.change_order_id = m.get('ChangeOrderId')
        return self


class UnbindSlbResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: UnbindSlbResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UnbindSlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UnbindSlbResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UnbindSlbResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindSlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindSlbResponse, self).to_map()
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
            temp_model = UnbindSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, delete_all=None, region_id=None, resource_ids=None, resource_type=None, tag_keys=None):
        self.delete_all = delete_all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_ids = resource_ids  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_keys = tag_keys  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delete_all is not None:
            result['DeleteAll'] = self.delete_all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeleteAll') is not None:
            self.delete_all = m.get('DeleteAll')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppSecurityGroupRequest(TeaModel):
    def __init__(self, app_id=None, security_group_id=None):
        self.app_id = app_id  # type: str
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppSecurityGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class UpdateAppSecurityGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None, trace_id=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateAppSecurityGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateAppSecurityGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateAppSecurityGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateAppSecurityGroupResponse, self).to_map()
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
            temp_model = UpdateAppSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationDescriptionRequest(TeaModel):
    def __init__(self, app_description=None, app_id=None):
        self.app_description = app_description  # type: str
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationDescriptionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_description is not None:
            result['AppDescription'] = self.app_description
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class UpdateApplicationDescriptionResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None, trace_id=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationDescriptionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationDescriptionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationDescriptionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationDescriptionResponse, self).to_map()
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
            temp_model = UpdateApplicationDescriptionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationScalingRuleRequest(TeaModel):
    def __init__(self, app_id=None, min_ready_instance_ratio=None, min_ready_instances=None,
                 scaling_rule_metric=None, scaling_rule_name=None, scaling_rule_timer=None):
        self.app_id = app_id  # type: str
        self.min_ready_instance_ratio = min_ready_instance_ratio  # type: int
        self.min_ready_instances = min_ready_instances  # type: int
        self.scaling_rule_metric = scaling_rule_metric  # type: str
        self.scaling_rule_name = scaling_rule_name  # type: str
        self.scaling_rule_timer = scaling_rule_timer  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio
        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances
        if self.scaling_rule_metric is not None:
            result['ScalingRuleMetric'] = self.scaling_rule_metric
        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name
        if self.scaling_rule_timer is not None:
            result['ScalingRuleTimer'] = self.scaling_rule_timer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')
        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')
        if m.get('ScalingRuleMetric') is not None:
            self.scaling_rule_metric = m.get('ScalingRuleMetric')
        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')
        if m.get('ScalingRuleTimer') is not None:
            self.scaling_rule_timer = m.get('ScalingRuleTimer')
        return self


class UpdateApplicationScalingRuleResponseBodyDataMetricMetrics(TeaModel):
    def __init__(self, metric_target_average_utilization=None, metric_type=None):
        self.metric_target_average_utilization = metric_target_average_utilization  # type: int
        self.metric_type = metric_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponseBodyDataMetricMetrics, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric_target_average_utilization is not None:
            result['MetricTargetAverageUtilization'] = self.metric_target_average_utilization
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MetricTargetAverageUtilization') is not None:
            self.metric_target_average_utilization = m.get('MetricTargetAverageUtilization')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        return self


class UpdateApplicationScalingRuleResponseBodyDataMetric(TeaModel):
    def __init__(self, max_replicas=None, metrics=None, min_replicas=None):
        self.max_replicas = max_replicas  # type: int
        self.metrics = metrics  # type: list[UpdateApplicationScalingRuleResponseBodyDataMetricMetrics]
        self.min_replicas = min_replicas  # type: int

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponseBodyDataMetric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_replicas is not None:
            result['MaxReplicas'] = self.max_replicas
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.min_replicas is not None:
            result['MinReplicas'] = self.min_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxReplicas') is not None:
            self.max_replicas = m.get('MaxReplicas')
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = UpdateApplicationScalingRuleResponseBodyDataMetricMetrics()
                self.metrics.append(temp_model.from_map(k))
        if m.get('MinReplicas') is not None:
            self.min_replicas = m.get('MinReplicas')
        return self


class UpdateApplicationScalingRuleResponseBodyDataTimerSchedules(TeaModel):
    def __init__(self, at_time=None, target_replicas=None):
        self.at_time = at_time  # type: str
        self.target_replicas = target_replicas  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponseBodyDataTimerSchedules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.at_time is not None:
            result['AtTime'] = self.at_time
        if self.target_replicas is not None:
            result['TargetReplicas'] = self.target_replicas
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AtTime') is not None:
            self.at_time = m.get('AtTime')
        if m.get('TargetReplicas') is not None:
            self.target_replicas = m.get('TargetReplicas')
        return self


class UpdateApplicationScalingRuleResponseBodyDataTimer(TeaModel):
    def __init__(self, begin_date=None, end_date=None, period=None, schedules=None):
        self.begin_date = begin_date  # type: str
        self.end_date = end_date  # type: str
        self.period = period  # type: str
        self.schedules = schedules  # type: list[UpdateApplicationScalingRuleResponseBodyDataTimerSchedules]

    def validate(self):
        if self.schedules:
            for k in self.schedules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponseBodyDataTimer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_date is not None:
            result['BeginDate'] = self.begin_date
        if self.end_date is not None:
            result['EndDate'] = self.end_date
        if self.period is not None:
            result['Period'] = self.period
        result['Schedules'] = []
        if self.schedules is not None:
            for k in self.schedules:
                result['Schedules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginDate') is not None:
            self.begin_date = m.get('BeginDate')
        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        self.schedules = []
        if m.get('Schedules') is not None:
            for k in m.get('Schedules'):
                temp_model = UpdateApplicationScalingRuleResponseBodyDataTimerSchedules()
                self.schedules.append(temp_model.from_map(k))
        return self


class UpdateApplicationScalingRuleResponseBodyData(TeaModel):
    def __init__(self, app_id=None, create_time=None, last_disable_time=None, metric=None, scale_rule_enabled=None,
                 scale_rule_name=None, scale_rule_type=None, timer=None, update_time=None):
        self.app_id = app_id  # type: str
        self.create_time = create_time  # type: long
        self.last_disable_time = last_disable_time  # type: long
        self.metric = metric  # type: UpdateApplicationScalingRuleResponseBodyDataMetric
        self.scale_rule_enabled = scale_rule_enabled  # type: bool
        self.scale_rule_name = scale_rule_name  # type: str
        self.scale_rule_type = scale_rule_type  # type: str
        self.timer = timer  # type: UpdateApplicationScalingRuleResponseBodyDataTimer
        self.update_time = update_time  # type: long

    def validate(self):
        if self.metric:
            self.metric.validate()
        if self.timer:
            self.timer.validate()

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_disable_time is not None:
            result['LastDisableTime'] = self.last_disable_time
        if self.metric is not None:
            result['Metric'] = self.metric.to_map()
        if self.scale_rule_enabled is not None:
            result['ScaleRuleEnabled'] = self.scale_rule_enabled
        if self.scale_rule_name is not None:
            result['ScaleRuleName'] = self.scale_rule_name
        if self.scale_rule_type is not None:
            result['ScaleRuleType'] = self.scale_rule_type
        if self.timer is not None:
            result['Timer'] = self.timer.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastDisableTime') is not None:
            self.last_disable_time = m.get('LastDisableTime')
        if m.get('Metric') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyDataMetric()
            self.metric = temp_model.from_map(m['Metric'])
        if m.get('ScaleRuleEnabled') is not None:
            self.scale_rule_enabled = m.get('ScaleRuleEnabled')
        if m.get('ScaleRuleName') is not None:
            self.scale_rule_name = m.get('ScaleRuleName')
        if m.get('ScaleRuleType') is not None:
            self.scale_rule_type = m.get('ScaleRuleType')
        if m.get('Timer') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyDataTimer()
            self.timer = temp_model.from_map(m['Timer'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateApplicationScalingRuleResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, trace_id=None):
        self.data = data  # type: UpdateApplicationScalingRuleResponseBodyData
        self.request_id = request_id  # type: str
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateApplicationScalingRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationScalingRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationScalingRuleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationScalingRuleResponse, self).to_map()
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
            temp_model = UpdateApplicationScalingRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateApplicationVswitchesRequest(TeaModel):
    def __init__(self, app_id=None, v_switch_id=None):
        self.app_id = app_id  # type: str
        self.v_switch_id = v_switch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationVswitchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        return self


class UpdateApplicationVswitchesResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None, trace_id=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateApplicationVswitchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateApplicationVswitchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateApplicationVswitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateApplicationVswitchesResponse, self).to_map()
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
            temp_model = UpdateApplicationVswitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConfigMapRequest(TeaModel):
    def __init__(self, config_map_id=None, data=None, description=None):
        self.config_map_id = config_map_id  # type: long
        self.data = data  # type: str
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConfigMapRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        if self.data is not None:
            result['Data'] = self.data
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateConfigMapResponseBodyData(TeaModel):
    def __init__(self, config_map_id=None):
        self.config_map_id = config_map_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateConfigMapResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')
        return self


class UpdateConfigMapResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateConfigMapResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateConfigMapResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateConfigMapResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateConfigMapResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateConfigMapResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateConfigMapResponse, self).to_map()
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
            temp_model = UpdateConfigMapResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGreyTagRouteRequest(TeaModel):
    def __init__(self, description=None, dubbo_rules=None, grey_tag_route_id=None, sc_rules=None):
        # 规则名称
        self.description = description  # type: str
        # Dubbo规则
        self.dubbo_rules = dubbo_rules  # type: str
        # 规则ID
        self.grey_tag_route_id = grey_tag_route_id  # type: long
        # SpringCloud规则
        self.sc_rules = sc_rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGreyTagRouteRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.dubbo_rules is not None:
            result['DubboRules'] = self.dubbo_rules
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        if self.sc_rules is not None:
            result['ScRules'] = self.sc_rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DubboRules') is not None:
            self.dubbo_rules = m.get('DubboRules')
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        if m.get('ScRules') is not None:
            self.sc_rules = m.get('ScRules')
        return self


class UpdateGreyTagRouteResponseBodyData(TeaModel):
    def __init__(self, grey_tag_route_id=None):
        self.grey_tag_route_id = grey_tag_route_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGreyTagRouteResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grey_tag_route_id is not None:
            result['GreyTagRouteId'] = self.grey_tag_route_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GreyTagRouteId') is not None:
            self.grey_tag_route_id = m.get('GreyTagRouteId')
        return self


class UpdateGreyTagRouteResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateGreyTagRouteResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateGreyTagRouteResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateGreyTagRouteResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateGreyTagRouteResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGreyTagRouteResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGreyTagRouteResponse, self).to_map()
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
            temp_model = UpdateGreyTagRouteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIngressRequest(TeaModel):
    def __init__(self, cert_id=None, default_rule=None, description=None, ingress_id=None, listener_port=None,
                 listener_protocol=None, load_balance_type=None, rules=None):
        self.cert_id = cert_id  # type: str
        self.default_rule = default_rule  # type: str
        self.description = description  # type: str
        self.ingress_id = ingress_id  # type: long
        self.listener_port = listener_port  # type: str
        self.listener_protocol = listener_protocol  # type: str
        self.load_balance_type = load_balance_type  # type: str
        self.rules = rules  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIngressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_id is not None:
            result['CertId'] = self.cert_id
        if self.default_rule is not None:
            result['DefaultRule'] = self.default_rule
        if self.description is not None:
            result['Description'] = self.description
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balance_type is not None:
            result['LoadBalanceType'] = self.load_balance_type
        if self.rules is not None:
            result['Rules'] = self.rules
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')
        if m.get('DefaultRule') is not None:
            self.default_rule = m.get('DefaultRule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalanceType') is not None:
            self.load_balance_type = m.get('LoadBalanceType')
        if m.get('Rules') is not None:
            self.rules = m.get('Rules')
        return self


class UpdateIngressResponseBodyData(TeaModel):
    def __init__(self, ingress_id=None):
        self.ingress_id = ingress_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIngressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ingress_id is not None:
            result['IngressId'] = self.ingress_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IngressId') is not None:
            self.ingress_id = m.get('IngressId')
        return self


class UpdateIngressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateIngressResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateIngressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateIngressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateIngressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateIngressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIngressResponse, self).to_map()
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
            temp_model = UpdateIngressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(self, namespace_description=None, namespace_id=None, namespace_name=None):
        self.namespace_description = namespace_description  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNamespaceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateNamespaceResponseBodyData(TeaModel):
    def __init__(self, namespace_description=None, namespace_id=None, namespace_name=None, region_id=None):
        self.namespace_description = namespace_description  # type: str
        self.namespace_id = namespace_id  # type: str
        self.namespace_name = namespace_name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNamespaceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_description is not None:
            result['NamespaceDescription'] = self.namespace_description
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceDescription') is not None:
            self.namespace_description = m.get('NamespaceDescription')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateNamespaceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_code=None, message=None, request_id=None, success=None,
                 trace_id=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateNamespaceResponseBodyData
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateNamespaceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = UpdateNamespaceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNamespaceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNamespaceResponse, self).to_map()
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
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceVpcRequest(TeaModel):
    def __init__(self, namespace_id=None, vpc_id=None):
        self.namespace_id = namespace_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNamespaceVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateNamespaceVpcResponseBody(TeaModel):
    def __init__(self, code=None, error_code=None, message=None, request_id=None, success=None, trace_id=None):
        self.code = code  # type: str
        self.error_code = error_code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.trace_id = trace_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNamespaceVpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class UpdateNamespaceVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNamespaceVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNamespaceVpcResponse, self).to_map()
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
            temp_model = UpdateNamespaceVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


