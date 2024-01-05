# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ActualDeductResourceCmd(TeaModel):
    def __init__(self, cost=None, extra_info=None, idempotent_id=None, task_id=None):
        self.cost = cost  # type: long
        self.extra_info = extra_info  # type: str
        self.idempotent_id = idempotent_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActualDeductResourceCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost is not None:
            result['cost'] = self.cost
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ActualDeductResourceResult(TeaModel):
    def __init__(self, error_message=None, errorcode=None, request_id=None, success=None):
        self.error_message = error_message  # type: str
        self.errorcode = errorcode  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActualDeductResourceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.errorcode is not None:
            result['errorcode'] = self.errorcode
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorcode') is not None:
            self.errorcode = m.get('errorcode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DirectDeductResourceCmd(TeaModel):
    def __init__(self, account_id=None, cost=None, extra_info=None, idempotent_id=None, resource_type=None,
                 sub_account_id=None, token=None):
        self.account_id = account_id  # type: str
        self.cost = cost  # type: long
        self.extra_info = extra_info  # type: str
        self.idempotent_id = idempotent_id  # type: str
        self.resource_type = resource_type  # type: long
        self.sub_account_id = sub_account_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DirectDeductResourceCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.cost is not None:
            result['cost'] = self.cost
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class DirectDeductResourceResult(TeaModel):
    def __init__(self, error_message=None, errorcode=None, request_id=None, success=None):
        self.error_message = error_message  # type: str
        self.errorcode = errorcode  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DirectDeductResourceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.errorcode is not None:
            result['errorcode'] = self.errorcode
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorcode') is not None:
            self.errorcode = m.get('errorcode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ExpectDeductResourceCmd(TeaModel):
    def __init__(self, account_id=None, cost=None, extra_info=None, idempotent_id=None, resource_type=None,
                 sub_account_id=None, token=None):
        self.account_id = account_id  # type: str
        self.cost = cost  # type: long
        self.extra_info = extra_info  # type: str
        self.idempotent_id = idempotent_id  # type: str
        self.resource_type = resource_type  # type: long
        self.sub_account_id = sub_account_id  # type: str
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExpectDeductResourceCmd, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.cost is not None:
            result['cost'] = self.cost
        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info
        if self.idempotent_id is not None:
            result['idempotentId'] = self.idempotent_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_account_id is not None:
            result['subAccountId'] = self.sub_account_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('cost') is not None:
            self.cost = m.get('cost')
        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')
        if m.get('idempotentId') is not None:
            self.idempotent_id = m.get('idempotentId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subAccountId') is not None:
            self.sub_account_id = m.get('subAccountId')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class ExpectDeductResourceResult(TeaModel):
    def __init__(self, error_message=None, errorcode=None, request_id=None, success=None, task_id=None):
        self.error_message = error_message  # type: str
        self.errorcode = errorcode  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExpectDeductResourceResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.errorcode is not None:
            result['errorcode'] = self.errorcode
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('errorcode') is not None:
            self.errorcode = m.get('errorcode')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ActualDeductResourceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: ActualDeductResourceCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActualDeductResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ActualDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ActualDeductResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ActualDeductResourceResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActualDeductResourceResponse, self).to_map()
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
            temp_model = ActualDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class DirectDeductResourceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: DirectDeductResourceCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DirectDeductResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = DirectDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class DirectDeductResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DirectDeductResourceResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DirectDeductResourceResponse, self).to_map()
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
            temp_model = DirectDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpectDeductResourceRequest(TeaModel):
    def __init__(self, body=None):
        self.body = body  # type: ExpectDeductResourceCmd

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExpectDeductResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = ExpectDeductResourceCmd()
            self.body = temp_model.from_map(m['body'])
        return self


class ExpectDeductResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExpectDeductResourceResult

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExpectDeductResourceResponse, self).to_map()
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
            temp_model = ExpectDeductResourceResult()
            self.body = temp_model.from_map(m['body'])
        return self


