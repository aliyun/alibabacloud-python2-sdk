# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelAsyncTaskRequest(TeaModel):
    def __init__(self, agent_key=None, task_id=None):
        self.agent_key = agent_key  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelAsyncTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelAsyncTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelAsyncTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelAsyncTaskResponse, self).to_map()
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
            temp_model = CancelAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearIntervenesRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearIntervenesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ClearIntervenesResponseBodyData(TeaModel):
    def __init__(self, fail_id_list=None, task_id=None):
        self.fail_id_list = fail_id_list  # type: list[str]
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearIntervenesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ClearIntervenesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ClearIntervenesResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ClearIntervenesResponseBody, self).to_map()
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
            temp_model = ClearIntervenesResponseBodyData()
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


class ClearIntervenesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClearIntervenesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearIntervenesResponse, self).to_map()
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
            temp_model = ClearIntervenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGeneratedContentRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, content_domain=None, content_text=None, keywords=None,
                 prompt=None, task_id=None, title=None, uuid=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.content_domain = content_domain  # type: str
        self.content_text = content_text  # type: str
        self.keywords = keywords  # type: list[str]
        self.prompt = prompt  # type: str
        self.task_id = task_id  # type: str
        self.title = title  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGeneratedContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CreateGeneratedContentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, content_domain=None, content_text=None, keywords_shrink=None,
                 prompt=None, task_id=None, title=None, uuid=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.content_domain = content_domain  # type: str
        self.content_text = content_text  # type: str
        self.keywords_shrink = keywords_shrink  # type: str
        self.prompt = prompt  # type: str
        self.task_id = task_id  # type: str
        self.title = title  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGeneratedContentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CreateGeneratedContentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGeneratedContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGeneratedContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGeneratedContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGeneratedContentResponse, self).to_map()
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
            temp_model = CreateGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class CreateTokenResponseBodyData(TeaModel):
    def __init__(self, expired_time=None, token=None):
        self.expired_time = expired_time  # type: long
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateTokenResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateTokenResponseBody, self).to_map()
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
            temp_model = CreateTokenResponseBodyData()
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


class CreateTokenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTokenResponse, self).to_map()
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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGeneratedContentRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGeneratedContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteGeneratedContentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGeneratedContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGeneratedContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGeneratedContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGeneratedContentResponse, self).to_map()
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
            temp_model = DeleteGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInterveneRuleRequest(TeaModel):
    def __init__(self, agent_key=None, rule_id=None):
        self.agent_key = agent_key  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInterveneRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteInterveneRuleResponseBodyData(TeaModel):
    def __init__(self, fail_id_list=None, task_id=None):
        self.fail_id_list = fail_id_list  # type: list[str]
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInterveneRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteInterveneRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteInterveneRuleResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteInterveneRuleResponseBody, self).to_map()
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
            temp_model = DeleteInterveneRuleResponseBodyData()
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


class DeleteInterveneRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInterveneRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInterveneRuleResponse, self).to_map()
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
            temp_model = DeleteInterveneRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaterialByIdRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaterialByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteMaterialByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMaterialByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMaterialByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMaterialByIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMaterialByIdResponse, self).to_map()
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
            temp_model = DeleteMaterialByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportGeneratedContentRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportGeneratedContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ExportGeneratedContentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportGeneratedContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportGeneratedContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportGeneratedContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportGeneratedContentResponse, self).to_map()
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
            temp_model = ExportGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportIntervenesRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportIntervenesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ExportIntervenesResponseBodyData(TeaModel):
    def __init__(self, file_url=None):
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExportIntervenesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ExportIntervenesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ExportIntervenesResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ExportIntervenesResponseBody, self).to_map()
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
            temp_model = ExportIntervenesResponseBodyData()
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


class ExportIntervenesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ExportIntervenesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExportIntervenesResponse, self).to_map()
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
            temp_model = ExportIntervenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackDialogueRequest(TeaModel):
    def __init__(self, agent_key=None, customer_response=None, good_text=None, modified_response=None, rating=None,
                 rating_tags=None, session_id=None, task_id=None):
        self.agent_key = agent_key  # type: str
        self.customer_response = customer_response  # type: str
        self.good_text = good_text  # type: str
        self.modified_response = modified_response  # type: str
        self.rating = rating  # type: str
        self.rating_tags = rating_tags  # type: list[str]
        self.session_id = session_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackDialogueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.customer_response is not None:
            result['CustomerResponse'] = self.customer_response
        if self.good_text is not None:
            result['GoodText'] = self.good_text
        if self.modified_response is not None:
            result['ModifiedResponse'] = self.modified_response
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.rating_tags is not None:
            result['RatingTags'] = self.rating_tags
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomerResponse') is not None:
            self.customer_response = m.get('CustomerResponse')
        if m.get('GoodText') is not None:
            self.good_text = m.get('GoodText')
        if m.get('ModifiedResponse') is not None:
            self.modified_response = m.get('ModifiedResponse')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('RatingTags') is not None:
            self.rating_tags = m.get('RatingTags')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FeedbackDialogueShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, customer_response=None, good_text=None, modified_response=None, rating=None,
                 rating_tags_shrink=None, session_id=None, task_id=None):
        self.agent_key = agent_key  # type: str
        self.customer_response = customer_response  # type: str
        self.good_text = good_text  # type: str
        self.modified_response = modified_response  # type: str
        self.rating = rating  # type: str
        self.rating_tags_shrink = rating_tags_shrink  # type: str
        self.session_id = session_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackDialogueShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.customer_response is not None:
            result['CustomerResponse'] = self.customer_response
        if self.good_text is not None:
            result['GoodText'] = self.good_text
        if self.modified_response is not None:
            result['ModifiedResponse'] = self.modified_response
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.rating_tags_shrink is not None:
            result['RatingTags'] = self.rating_tags_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomerResponse') is not None:
            self.customer_response = m.get('CustomerResponse')
        if m.get('GoodText') is not None:
            self.good_text = m.get('GoodText')
        if m.get('ModifiedResponse') is not None:
            self.modified_response = m.get('ModifiedResponse')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('RatingTags') is not None:
            self.rating_tags_shrink = m.get('RatingTags')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FeedbackDialogueResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(FeedbackDialogueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FeedbackDialogueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FeedbackDialogueResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FeedbackDialogueResponse, self).to_map()
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
            temp_model = FeedbackDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchImageTaskRequest(TeaModel):
    def __init__(self, agent_key=None, article_task_id=None, task_id_list=None):
        self.agent_key = agent_key  # type: str
        self.article_task_id = article_task_id  # type: str
        self.task_id_list = task_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchImageTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        if self.task_id_list is not None:
            result['TaskIdList'] = self.task_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        if m.get('TaskIdList') is not None:
            self.task_id_list = m.get('TaskIdList')
        return self


class FetchImageTaskShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, article_task_id=None, task_id_list_shrink=None):
        self.agent_key = agent_key  # type: str
        self.article_task_id = article_task_id  # type: str
        self.task_id_list_shrink = task_id_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchImageTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        if self.task_id_list_shrink is not None:
            result['TaskIdList'] = self.task_id_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        if m.get('TaskIdList') is not None:
            self.task_id_list_shrink = m.get('TaskIdList')
        return self


class FetchImageTaskResponseBodyDataTaskInfoListImageList(TeaModel):
    def __init__(self, code=None, message=None, url=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FetchImageTaskResponseBodyDataTaskInfoListImageList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class FetchImageTaskResponseBodyDataTaskInfoList(TeaModel):
    def __init__(self, id=None, image_list=None, task_id=None, task_status=None):
        self.id = id  # type: long
        self.image_list = image_list  # type: list[FetchImageTaskResponseBodyDataTaskInfoListImageList]
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: str

    def validate(self):
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FetchImageTaskResponseBodyDataTaskInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = FetchImageTaskResponseBodyDataTaskInfoListImageList()
                self.image_list.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class FetchImageTaskResponseBodyData(TeaModel):
    def __init__(self, task_info_list=None):
        self.task_info_list = task_info_list  # type: list[FetchImageTaskResponseBodyDataTaskInfoList]

    def validate(self):
        if self.task_info_list:
            for k in self.task_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FetchImageTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskInfoList'] = []
        if self.task_info_list is not None:
            for k in self.task_info_list:
                result['TaskInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_info_list = []
        if m.get('TaskInfoList') is not None:
            for k in m.get('TaskInfoList'):
                temp_model = FetchImageTaskResponseBodyDataTaskInfoList()
                self.task_info_list.append(temp_model.from_map(k))
        return self


class FetchImageTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: FetchImageTaskResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(FetchImageTaskResponseBody, self).to_map()
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
            temp_model = FetchImageTaskResponseBodyData()
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


class FetchImageTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FetchImageTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FetchImageTaskResponse, self).to_map()
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
            temp_model = FetchImageTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateFileUrlByKeyRequest(TeaModel):
    def __init__(self, agent_key=None, file_key=None, file_name=None):
        self.agent_key = agent_key  # type: str
        self.file_key = file_key  # type: str
        self.file_name = file_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateFileUrlByKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GenerateFileUrlByKeyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateFileUrlByKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateFileUrlByKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateFileUrlByKeyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateFileUrlByKeyResponse, self).to_map()
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
            temp_model = GenerateFileUrlByKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateImageTaskRequestParagraphList(TeaModel):
    def __init__(self, content=None, id=None, task_id=None, task_status=None):
        self.content = content  # type: str
        self.id = id  # type: long
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageTaskRequestParagraphList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GenerateImageTaskRequest(TeaModel):
    def __init__(self, agent_key=None, article_task_id=None, paragraph_list=None, size=None, style=None):
        self.agent_key = agent_key  # type: str
        self.article_task_id = article_task_id  # type: str
        self.paragraph_list = paragraph_list  # type: list[GenerateImageTaskRequestParagraphList]
        self.size = size  # type: str
        self.style = style  # type: str

    def validate(self):
        if self.paragraph_list:
            for k in self.paragraph_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateImageTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        result['ParagraphList'] = []
        if self.paragraph_list is not None:
            for k in self.paragraph_list:
                result['ParagraphList'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.style is not None:
            result['Style'] = self.style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        self.paragraph_list = []
        if m.get('ParagraphList') is not None:
            for k in m.get('ParagraphList'):
                temp_model = GenerateImageTaskRequestParagraphList()
                self.paragraph_list.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        return self


class GenerateImageTaskShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, article_task_id=None, paragraph_list_shrink=None, size=None, style=None):
        self.agent_key = agent_key  # type: str
        self.article_task_id = article_task_id  # type: str
        self.paragraph_list_shrink = paragraph_list_shrink  # type: str
        self.size = size  # type: str
        self.style = style  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        if self.paragraph_list_shrink is not None:
            result['ParagraphList'] = self.paragraph_list_shrink
        if self.size is not None:
            result['Size'] = self.size
        if self.style is not None:
            result['Style'] = self.style
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        if m.get('ParagraphList') is not None:
            self.paragraph_list_shrink = m.get('ParagraphList')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        return self


class GenerateImageTaskResponseBodyDataTaskList(TeaModel):
    def __init__(self, content=None, id=None, task_id=None, task_status=None):
        self.content = content  # type: str
        self.id = id  # type: long
        self.task_id = task_id  # type: str
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateImageTaskResponseBodyDataTaskList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GenerateImageTaskResponseBodyData(TeaModel):
    def __init__(self, task_list=None):
        self.task_list = task_list  # type: list[GenerateImageTaskResponseBodyDataTaskList]

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateImageTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = GenerateImageTaskResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class GenerateImageTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GenerateImageTaskResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateImageTaskResponseBody, self).to_map()
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
            temp_model = GenerateImageTaskResponseBodyData()
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


class GenerateImageTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateImageTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateImageTaskResponse, self).to_map()
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
            temp_model = GenerateImageTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadConfigRequest(TeaModel):
    def __init__(self, agent_key=None, file_name=None, parent_dir=None):
        self.agent_key = agent_key  # type: str
        self.file_name = file_name  # type: str
        self.parent_dir = parent_dir  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.parent_dir is not None:
            result['ParentDir'] = self.parent_dir
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ParentDir') is not None:
            self.parent_dir = m.get('ParentDir')
        return self


class GenerateUploadConfigResponseBodyData(TeaModel):
    def __init__(self, file_key=None, form_datas=None, post_url=None):
        self.file_key = file_key  # type: str
        self.form_datas = form_datas  # type: dict[str, any]
        self.post_url = post_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateUploadConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.form_datas is not None:
            result['FormDatas'] = self.form_datas
        if self.post_url is not None:
            result['PostUrl'] = self.post_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FormDatas') is not None:
            self.form_datas = m.get('FormDatas')
        if m.get('PostUrl') is not None:
            self.post_url = m.get('PostUrl')
        return self


class GenerateUploadConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GenerateUploadConfigResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GenerateUploadConfigResponseBody, self).to_map()
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
            temp_model = GenerateUploadConfigResponseBodyData()
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


class GenerateUploadConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateUploadConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateUploadConfigResponse, self).to_map()
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
            temp_model = GenerateUploadConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateViewPointRequestReferenceData(TeaModel):
    def __init__(self, mini_doc=None):
        self.mini_doc = mini_doc  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateViewPointRequestReferenceData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')
        return self


class GenerateViewPointRequest(TeaModel):
    def __init__(self, agent_key=None, reference_data=None):
        self.agent_key = agent_key  # type: str
        self.reference_data = reference_data  # type: GenerateViewPointRequestReferenceData

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        _map = super(GenerateViewPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ReferenceData') is not None:
            temp_model = GenerateViewPointRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        return self


class GenerateViewPointShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, reference_data_shrink=None):
        self.agent_key = agent_key  # type: str
        self.reference_data_shrink = reference_data_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateViewPointShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        return self


class GenerateViewPointResponseBodyData(TeaModel):
    def __init__(self, point=None):
        self.point = point  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GenerateViewPointResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class GenerateViewPointResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[GenerateViewPointResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GenerateViewPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GenerateViewPointResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateViewPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GenerateViewPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GenerateViewPointResponse, self).to_map()
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
            temp_model = GenerateViewPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceOrderConfigRequest(TeaModel):
    def __init__(self, agent_key=None, product_code=None):
        self.agent_key = agent_key  # type: str
        self.product_code = product_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceOrderConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList(TeaModel):
    def __init__(self, code=None, name=None, number=None, type=None):
        self.code = code  # type: str
        self.name = name  # type: str
        self.number = number  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDataSourceOrderConfigResponseBodyData(TeaModel):
    def __init__(self, user_config_data_source_list=None):
        self.user_config_data_source_list = user_config_data_source_list  # type: list[GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList]

    def validate(self):
        if self.user_config_data_source_list:
            for k in self.user_config_data_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetDataSourceOrderConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserConfigDataSourceList'] = []
        if self.user_config_data_source_list is not None:
            for k in self.user_config_data_source_list:
                result['UserConfigDataSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.user_config_data_source_list = []
        if m.get('UserConfigDataSourceList') is not None:
            for k in m.get('UserConfigDataSourceList'):
                temp_model = GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList()
                self.user_config_data_source_list.append(temp_model.from_map(k))
        return self


class GetDataSourceOrderConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetDataSourceOrderConfigResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDataSourceOrderConfigResponseBody, self).to_map()
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
            temp_model = GetDataSourceOrderConfigResponseBodyData()
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


class GetDataSourceOrderConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDataSourceOrderConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDataSourceOrderConfigResponse, self).to_map()
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
            temp_model = GetDataSourceOrderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGeneratedContentRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGeneratedContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetGeneratedContentResponseBodyData(TeaModel):
    def __init__(self, content=None, content_domain=None, content_text=None, create_time=None, create_user=None,
                 device_id=None, id=None, keyword_list=None, keywords=None, prompt=None, task_id=None, title=None,
                 update_time=None, update_user=None, uuid=None):
        self.content = content  # type: str
        self.content_domain = content_domain  # type: str
        self.content_text = content_text  # type: str
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.device_id = device_id  # type: str
        self.id = id  # type: long
        self.keyword_list = keyword_list  # type: list[str]
        self.keywords = keywords  # type: str
        self.prompt = prompt  # type: str
        self.task_id = task_id  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGeneratedContentResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword_list is not None:
            result['KeywordList'] = self.keyword_list
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeywordList') is not None:
            self.keyword_list = m.get('KeywordList')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetGeneratedContentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetGeneratedContentResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetGeneratedContentResponseBody, self).to_map()
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
            temp_model = GetGeneratedContentResponseBodyData()
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


class GetGeneratedContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGeneratedContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGeneratedContentResponse, self).to_map()
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
            temp_model = GetGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneGlobalReplyRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneGlobalReplyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class GetInterveneGlobalReplyResponseBodyDataReplyMessagList(TeaModel):
    def __init__(self, message=None, reply_type=None):
        self.message = message  # type: str
        self.reply_type = reply_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneGlobalReplyResponseBodyDataReplyMessagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reply_type is not None:
            result['ReplyType'] = self.reply_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReplyType') is not None:
            self.reply_type = m.get('ReplyType')
        return self


class GetInterveneGlobalReplyResponseBodyData(TeaModel):
    def __init__(self, reply_messag_list=None):
        self.reply_messag_list = reply_messag_list  # type: list[GetInterveneGlobalReplyResponseBodyDataReplyMessagList]

    def validate(self):
        if self.reply_messag_list:
            for k in self.reply_messag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInterveneGlobalReplyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplyMessagList'] = []
        if self.reply_messag_list is not None:
            for k in self.reply_messag_list:
                result['ReplyMessagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.reply_messag_list = []
        if m.get('ReplyMessagList') is not None:
            for k in m.get('ReplyMessagList'):
                temp_model = GetInterveneGlobalReplyResponseBodyDataReplyMessagList()
                self.reply_messag_list.append(temp_model.from_map(k))
        return self


class GetInterveneGlobalReplyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetInterveneGlobalReplyResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInterveneGlobalReplyResponseBody, self).to_map()
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
            temp_model = GetInterveneGlobalReplyResponseBodyData()
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


class GetInterveneGlobalReplyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInterveneGlobalReplyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInterveneGlobalReplyResponse, self).to_map()
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
            temp_model = GetInterveneGlobalReplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneImportTaskInfoRequest(TeaModel):
    def __init__(self, agent_key=None, task_id=None):
        self.agent_key = agent_key  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneImportTaskInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetInterveneImportTaskInfoResponseBodyDataStatus(TeaModel):
    def __init__(self, msg=None, percentage=None, status=None, task_id=None, task_name=None):
        self.msg = msg  # type: str
        self.percentage = percentage  # type: int
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneImportTaskInfoResponseBodyDataStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetInterveneImportTaskInfoResponseBodyData(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: GetInterveneImportTaskInfoResponseBodyDataStatus

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(GetInterveneImportTaskInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = GetInterveneImportTaskInfoResponseBodyDataStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class GetInterveneImportTaskInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetInterveneImportTaskInfoResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInterveneImportTaskInfoResponseBody, self).to_map()
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
            temp_model = GetInterveneImportTaskInfoResponseBodyData()
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


class GetInterveneImportTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInterveneImportTaskInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInterveneImportTaskInfoResponse, self).to_map()
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
            temp_model = GetInterveneImportTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneRuleDetailRequest(TeaModel):
    def __init__(self, agent_key=None, rule_id=None):
        self.agent_key = agent_key  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneRuleDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig(TeaModel):
    def __init__(self, answer_type=None, message=None, namespace=None):
        self.answer_type = answer_type  # type: int
        self.message = message  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig(TeaModel):
    def __init__(self, effect_type=None, end_time=None, start_time=None):
        self.effect_type = effect_type  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail(TeaModel):
    def __init__(self, answer_config=None, effect_config=None, intervene_type=None, namespace_list=None,
                 rule_id=None, rule_name=None):
        self.answer_config = answer_config  # type: list[GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig]
        self.effect_config = effect_config  # type: GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig
        self.intervene_type = intervene_type  # type: int
        self.namespace_list = namespace_list  # type: list[str]
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.answer_config:
            for k in self.answer_config:
                if k:
                    k.validate()
        if self.effect_config:
            self.effect_config.validate()

    def to_map(self):
        _map = super(GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k in self.answer_config:
                result['AnswerConfig'].append(k.to_map() if k else None)
        if self.effect_config is not None:
            result['EffectConfig'] = self.effect_config.to_map()
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k in m.get('AnswerConfig'):
                temp_model = GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig()
                self.answer_config.append(temp_model.from_map(k))
        if m.get('EffectConfig') is not None:
            temp_model = GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig()
            self.effect_config = temp_model.from_map(m['EffectConfig'])
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetInterveneRuleDetailResponseBodyData(TeaModel):
    def __init__(self, intervene_rule_detail=None):
        self.intervene_rule_detail = intervene_rule_detail  # type: GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail

    def validate(self):
        if self.intervene_rule_detail:
            self.intervene_rule_detail.validate()

    def to_map(self):
        _map = super(GetInterveneRuleDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intervene_rule_detail is not None:
            result['InterveneRuleDetail'] = self.intervene_rule_detail.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InterveneRuleDetail') is not None:
            temp_model = GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail()
            self.intervene_rule_detail = temp_model.from_map(m['InterveneRuleDetail'])
        return self


class GetInterveneRuleDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetInterveneRuleDetailResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInterveneRuleDetailResponseBody, self).to_map()
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
            temp_model = GetInterveneRuleDetailResponseBodyData()
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


class GetInterveneRuleDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInterveneRuleDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInterveneRuleDetailResponse, self).to_map()
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
            temp_model = GetInterveneRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneTemplateFileUrlRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneTemplateFileUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class GetInterveneTemplateFileUrlResponseBodyData(TeaModel):
    def __init__(self, file_url=None):
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInterveneTemplateFileUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetInterveneTemplateFileUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetInterveneTemplateFileUrlResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetInterveneTemplateFileUrlResponseBody, self).to_map()
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
            temp_model = GetInterveneTemplateFileUrlResponseBodyData()
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


class GetInterveneTemplateFileUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInterveneTemplateFileUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInterveneTemplateFileUrlResponse, self).to_map()
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
            temp_model = GetInterveneTemplateFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMaterialByIdRequest(TeaModel):
    def __init__(self, agent_key=None, id=None):
        self.agent_key = agent_key  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMaterialByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMaterialByIdResponseBodyData(TeaModel):
    def __init__(self, author=None, create_time=None, create_user=None, doc_keywords=None, doc_type=None,
                 external_url=None, html_content=None, id=None, pub_time=None, public_url=None, share_attr=None, src_from=None,
                 summary=None, text_content=None, thumbnail_in_base_64=None, title=None, update_time=None, update_user=None,
                 url=None):
        self.author = author  # type: str
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.doc_keywords = doc_keywords  # type: list[str]
        self.doc_type = doc_type  # type: str
        self.external_url = external_url  # type: str
        self.html_content = html_content  # type: str
        self.id = id  # type: long
        self.pub_time = pub_time  # type: str
        self.public_url = public_url  # type: str
        self.share_attr = share_attr  # type: int
        self.src_from = src_from  # type: str
        self.summary = summary  # type: str
        self.text_content = text_content  # type: str
        self.thumbnail_in_base_64 = thumbnail_in_base_64  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMaterialByIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.thumbnail_in_base_64 is not None:
            result['ThumbnailInBase64'] = self.thumbnail_in_base_64
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('ThumbnailInBase64') is not None:
            self.thumbnail_in_base_64 = m.get('ThumbnailInBase64')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMaterialByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetMaterialByIdResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetMaterialByIdResponseBody, self).to_map()
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
            temp_model = GetMaterialByIdResponseBodyData()
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


class GetMaterialByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMaterialByIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMaterialByIdResponse, self).to_map()
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
            temp_model = GetMaterialByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPropertiesRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class GetPropertiesResponseBodyDataConsoleConfig(TeaModel):
    def __init__(self, tip_content=None, title=None):
        self.tip_content = tip_content  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataConsoleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tip_content is not None:
            result['TipContent'] = self.tip_content
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TipContent') is not None:
            self.tip_content = m.get('TipContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles(TeaModel):
    def __init__(self, select=None, stared=None, title=None, url=None):
        self.select = select  # type: bool
        self.stared = stared  # type: bool
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        if self.stared is not None:
            result['Stared'] = self.stared
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('Stared') is not None:
            self.stared = m.get('Stared')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples(TeaModel):
    def __init__(self, articles=None, prompt=None, text=None):
        self.articles = articles  # type: list[GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles]
        self.prompt = prompt  # type: str
        self.text = text  # type: str

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources(TeaModel):
    def __init__(self, code=None, dataset_name=None, name=None):
        self.code = code  # type: str
        self.dataset_name = dataset_name  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfig(TeaModel):
    def __init__(self, product_description=None, search_samples=None, search_sources=None):
        self.product_description = product_description  # type: str
        self.search_samples = search_samples  # type: list[GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples]
        self.search_sources = search_sources  # type: list[GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources]

    def validate(self):
        if self.search_samples:
            for k in self.search_samples:
                if k:
                    k.validate()
        if self.search_sources:
            for k in self.search_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataIntelligentSearchConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        result['SearchSamples'] = []
        if self.search_samples is not None:
            for k in self.search_samples:
                result['SearchSamples'].append(k.to_map() if k else None)
        result['SearchSources'] = []
        if self.search_sources is not None:
            for k in self.search_sources:
                result['SearchSources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        self.search_samples = []
        if m.get('SearchSamples') is not None:
            for k in m.get('SearchSamples'):
                temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples()
                self.search_samples.append(temp_model.from_map(k))
        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k in m.get('SearchSources'):
                temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources()
                self.search_sources.append(temp_model.from_map(k))
        return self


class GetPropertiesResponseBodyDataSearchSources(TeaModel):
    def __init__(self, label=None, value=None):
        self.label = label  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataSearchSources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPropertiesResponseBodyDataUserInfo(TeaModel):
    def __init__(self, agent_id=None, tenant_id=None, user_id=None, username=None):
        self.agent_id = agent_id  # type: str
        self.tenant_id = tenant_id  # type: str
        self.user_id = user_id  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataUserInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetPropertiesResponseBodyDataWanxiangImageSizeConfig(TeaModel):
    def __init__(self, name=None, value=None):
        self.name = name  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataWanxiangImageSizeConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPropertiesResponseBodyDataWanxiangImageStyleConfig(TeaModel):
    def __init__(self, name=None, pic=None, value=None):
        self.name = name  # type: str
        self.pic = pic  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPropertiesResponseBodyDataWanxiangImageStyleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPropertiesResponseBodyData(TeaModel):
    def __init__(self, chat_config=None, console_config=None, general_config_map=None,
                 intelligent_search_config=None, search_sources=None, slr_authorized=None, user_info=None, wanxiang_image_size_config=None,
                 wanxiang_image_style_config=None):
        self.chat_config = chat_config  # type: dict[str, any]
        self.console_config = console_config  # type: GetPropertiesResponseBodyDataConsoleConfig
        self.general_config_map = general_config_map  # type: dict[str, any]
        self.intelligent_search_config = intelligent_search_config  # type: GetPropertiesResponseBodyDataIntelligentSearchConfig
        self.search_sources = search_sources  # type: list[GetPropertiesResponseBodyDataSearchSources]
        self.slr_authorized = slr_authorized  # type: bool
        self.user_info = user_info  # type: GetPropertiesResponseBodyDataUserInfo
        self.wanxiang_image_size_config = wanxiang_image_size_config  # type: list[GetPropertiesResponseBodyDataWanxiangImageSizeConfig]
        self.wanxiang_image_style_config = wanxiang_image_style_config  # type: list[GetPropertiesResponseBodyDataWanxiangImageStyleConfig]

    def validate(self):
        if self.console_config:
            self.console_config.validate()
        if self.intelligent_search_config:
            self.intelligent_search_config.validate()
        if self.search_sources:
            for k in self.search_sources:
                if k:
                    k.validate()
        if self.user_info:
            self.user_info.validate()
        if self.wanxiang_image_size_config:
            for k in self.wanxiang_image_size_config:
                if k:
                    k.validate()
        if self.wanxiang_image_style_config:
            for k in self.wanxiang_image_style_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetPropertiesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config
        if self.console_config is not None:
            result['ConsoleConfig'] = self.console_config.to_map()
        if self.general_config_map is not None:
            result['GeneralConfigMap'] = self.general_config_map
        if self.intelligent_search_config is not None:
            result['IntelligentSearchConfig'] = self.intelligent_search_config.to_map()
        result['SearchSources'] = []
        if self.search_sources is not None:
            for k in self.search_sources:
                result['SearchSources'].append(k.to_map() if k else None)
        if self.slr_authorized is not None:
            result['SlrAuthorized'] = self.slr_authorized
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        result['WanxiangImageSizeConfig'] = []
        if self.wanxiang_image_size_config is not None:
            for k in self.wanxiang_image_size_config:
                result['WanxiangImageSizeConfig'].append(k.to_map() if k else None)
        result['WanxiangImageStyleConfig'] = []
        if self.wanxiang_image_style_config is not None:
            for k in self.wanxiang_image_style_config:
                result['WanxiangImageStyleConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChatConfig') is not None:
            self.chat_config = m.get('ChatConfig')
        if m.get('ConsoleConfig') is not None:
            temp_model = GetPropertiesResponseBodyDataConsoleConfig()
            self.console_config = temp_model.from_map(m['ConsoleConfig'])
        if m.get('GeneralConfigMap') is not None:
            self.general_config_map = m.get('GeneralConfigMap')
        if m.get('IntelligentSearchConfig') is not None:
            temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfig()
            self.intelligent_search_config = temp_model.from_map(m['IntelligentSearchConfig'])
        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k in m.get('SearchSources'):
                temp_model = GetPropertiesResponseBodyDataSearchSources()
                self.search_sources.append(temp_model.from_map(k))
        if m.get('SlrAuthorized') is not None:
            self.slr_authorized = m.get('SlrAuthorized')
        if m.get('UserInfo') is not None:
            temp_model = GetPropertiesResponseBodyDataUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        self.wanxiang_image_size_config = []
        if m.get('WanxiangImageSizeConfig') is not None:
            for k in m.get('WanxiangImageSizeConfig'):
                temp_model = GetPropertiesResponseBodyDataWanxiangImageSizeConfig()
                self.wanxiang_image_size_config.append(temp_model.from_map(k))
        self.wanxiang_image_style_config = []
        if m.get('WanxiangImageStyleConfig') is not None:
            for k in m.get('WanxiangImageStyleConfig'):
                temp_model = GetPropertiesResponseBodyDataWanxiangImageStyleConfig()
                self.wanxiang_image_style_config.append(temp_model.from_map(k))
        return self


class GetPropertiesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetPropertiesResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPropertiesResponseBody, self).to_map()
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
            temp_model = GetPropertiesResponseBodyData()
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


class GetPropertiesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPropertiesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPropertiesResponse, self).to_map()
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
            temp_model = GetPropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportInterveneFileRequest(TeaModel):
    def __init__(self, agent_key=None, doc_name=None, file_key=None, file_url=None):
        self.agent_key = agent_key  # type: str
        self.doc_name = doc_name  # type: str
        self.file_key = file_key  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportInterveneFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ImportInterveneFileResponseBodyData(TeaModel):
    def __init__(self, fail_id_list=None, task_id=None):
        self.fail_id_list = fail_id_list  # type: list[str]
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportInterveneFileResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ImportInterveneFileResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ImportInterveneFileResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImportInterveneFileResponseBody, self).to_map()
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
            temp_model = ImportInterveneFileResponseBodyData()
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


class ImportInterveneFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportInterveneFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportInterveneFileResponse, self).to_map()
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
            temp_model = ImportInterveneFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportInterveneFileAsyncRequest(TeaModel):
    def __init__(self, agent_key=None, doc_name=None, file_key=None, file_url=None):
        self.agent_key = agent_key  # type: str
        self.doc_name = doc_name  # type: str
        self.file_key = file_key  # type: str
        self.file_url = file_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportInterveneFileAsyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ImportInterveneFileAsyncResponseBodyData(TeaModel):
    def __init__(self, fail_id_list=None, task_id=None):
        self.fail_id_list = fail_id_list  # type: list[str]
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ImportInterveneFileAsyncResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ImportInterveneFileAsyncResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ImportInterveneFileAsyncResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ImportInterveneFileAsyncResponseBody, self).to_map()
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
            temp_model = ImportInterveneFileAsyncResponseBodyData()
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


class ImportInterveneFileAsyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ImportInterveneFileAsyncResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ImportInterveneFileAsyncResponse, self).to_map()
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
            temp_model = ImportInterveneFileAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertInterveneGlobalReplyRequestReplyMessagList(TeaModel):
    def __init__(self, message=None, reply_type=None):
        self.message = message  # type: str
        self.reply_type = reply_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneGlobalReplyRequestReplyMessagList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reply_type is not None:
            result['ReplyType'] = self.reply_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReplyType') is not None:
            self.reply_type = m.get('ReplyType')
        return self


class InsertInterveneGlobalReplyRequest(TeaModel):
    def __init__(self, agent_key=None, reply_messag_list=None):
        self.agent_key = agent_key  # type: str
        self.reply_messag_list = reply_messag_list  # type: list[InsertInterveneGlobalReplyRequestReplyMessagList]

    def validate(self):
        if self.reply_messag_list:
            for k in self.reply_messag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InsertInterveneGlobalReplyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        result['ReplyMessagList'] = []
        if self.reply_messag_list is not None:
            for k in self.reply_messag_list:
                result['ReplyMessagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        self.reply_messag_list = []
        if m.get('ReplyMessagList') is not None:
            for k in m.get('ReplyMessagList'):
                temp_model = InsertInterveneGlobalReplyRequestReplyMessagList()
                self.reply_messag_list.append(temp_model.from_map(k))
        return self


class InsertInterveneGlobalReplyShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, reply_messag_list_shrink=None):
        self.agent_key = agent_key  # type: str
        self.reply_messag_list_shrink = reply_messag_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneGlobalReplyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.reply_messag_list_shrink is not None:
            result['ReplyMessagList'] = self.reply_messag_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ReplyMessagList') is not None:
            self.reply_messag_list_shrink = m.get('ReplyMessagList')
        return self


class InsertInterveneGlobalReplyResponseBodyData(TeaModel):
    def __init__(self, fail_id_list=None, task_id=None):
        self.fail_id_list = fail_id_list  # type: list[str]
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneGlobalReplyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InsertInterveneGlobalReplyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InsertInterveneGlobalReplyResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InsertInterveneGlobalReplyResponseBody, self).to_map()
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
            temp_model = InsertInterveneGlobalReplyResponseBodyData()
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


class InsertInterveneGlobalReplyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertInterveneGlobalReplyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertInterveneGlobalReplyResponse, self).to_map()
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
            temp_model = InsertInterveneGlobalReplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig(TeaModel):
    def __init__(self, answer_type=None, message=None, namespace=None):
        self.answer_type = answer_type  # type: int
        self.message = message  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class InsertInterveneRuleRequestInterveneRuleConfigEffectConfig(TeaModel):
    def __init__(self, effect_type=None, end_time=None, start_time=None):
        self.effect_type = effect_type  # type: int
        self.end_time = end_time  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneRuleRequestInterveneRuleConfigEffectConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList(TeaModel):
    def __init__(self, id=None, operation_type=None, query=None):
        # id
        self.id = id  # type: str
        self.operation_type = operation_type  # type: int
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class InsertInterveneRuleRequestInterveneRuleConfig(TeaModel):
    def __init__(self, answer_config=None, effect_config=None, intervene_config_list=None, intervene_type=None,
                 namespace_list=None, rule_id=None, rule_name=None):
        self.answer_config = answer_config  # type: list[InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig]
        self.effect_config = effect_config  # type: InsertInterveneRuleRequestInterveneRuleConfigEffectConfig
        self.intervene_config_list = intervene_config_list  # type: list[InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList]
        self.intervene_type = intervene_type  # type: int
        self.namespace_list = namespace_list  # type: list[str]
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.answer_config:
            for k in self.answer_config:
                if k:
                    k.validate()
        if self.effect_config:
            self.effect_config.validate()
        if self.intervene_config_list:
            for k in self.intervene_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(InsertInterveneRuleRequestInterveneRuleConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k in self.answer_config:
                result['AnswerConfig'].append(k.to_map() if k else None)
        if self.effect_config is not None:
            result['EffectConfig'] = self.effect_config.to_map()
        result['InterveneConfigList'] = []
        if self.intervene_config_list is not None:
            for k in self.intervene_config_list:
                result['InterveneConfigList'].append(k.to_map() if k else None)
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k in m.get('AnswerConfig'):
                temp_model = InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig()
                self.answer_config.append(temp_model.from_map(k))
        if m.get('EffectConfig') is not None:
            temp_model = InsertInterveneRuleRequestInterveneRuleConfigEffectConfig()
            self.effect_config = temp_model.from_map(m['EffectConfig'])
        self.intervene_config_list = []
        if m.get('InterveneConfigList') is not None:
            for k in m.get('InterveneConfigList'):
                temp_model = InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList()
                self.intervene_config_list.append(temp_model.from_map(k))
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class InsertInterveneRuleRequest(TeaModel):
    def __init__(self, agent_key=None, intervene_rule_config=None):
        self.agent_key = agent_key  # type: str
        self.intervene_rule_config = intervene_rule_config  # type: InsertInterveneRuleRequestInterveneRuleConfig

    def validate(self):
        if self.intervene_rule_config:
            self.intervene_rule_config.validate()

    def to_map(self):
        _map = super(InsertInterveneRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intervene_rule_config is not None:
            result['InterveneRuleConfig'] = self.intervene_rule_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InterveneRuleConfig') is not None:
            temp_model = InsertInterveneRuleRequestInterveneRuleConfig()
            self.intervene_rule_config = temp_model.from_map(m['InterveneRuleConfig'])
        return self


class InsertInterveneRuleShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, intervene_rule_config_shrink=None):
        self.agent_key = agent_key  # type: str
        self.intervene_rule_config_shrink = intervene_rule_config_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneRuleShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intervene_rule_config_shrink is not None:
            result['InterveneRuleConfig'] = self.intervene_rule_config_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InterveneRuleConfig') is not None:
            self.intervene_rule_config_shrink = m.get('InterveneRuleConfig')
        return self


class InsertInterveneRuleResponseBodyData(TeaModel):
    def __init__(self, rule_id=None):
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(InsertInterveneRuleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class InsertInterveneRuleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: InsertInterveneRuleResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(InsertInterveneRuleResponseBody, self).to_map()
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
            temp_model = InsertInterveneRuleResponseBodyData()
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


class InsertInterveneRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InsertInterveneRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InsertInterveneRuleResponse, self).to_map()
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
            temp_model = InsertInterveneRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncTasksRequest(TeaModel):
    def __init__(self, agent_key=None, create_time_end=None, create_time_start=None, current=None, size=None,
                 task_code=None, task_name=None, task_status=None, task_status_list=None, task_type=None, task_type_list=None):
        self.agent_key = agent_key  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_time_start = create_time_start  # type: str
        self.current = current  # type: int
        self.size = size  # type: int
        self.task_code = task_code  # type: str
        self.task_name = task_name  # type: str
        self.task_status = task_status  # type: int
        self.task_status_list = task_status_list  # type: list[int]
        self.task_type = task_type  # type: str
        self.task_type_list = task_type_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsyncTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_list is not None:
            result['TaskStatusList'] = self.task_status_list
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_list is not None:
            result['TaskTypeList'] = self.task_type_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusList') is not None:
            self.task_status_list = m.get('TaskStatusList')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeList') is not None:
            self.task_type_list = m.get('TaskTypeList')
        return self


class ListAsyncTasksShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, create_time_end=None, create_time_start=None, current=None, size=None,
                 task_code=None, task_name=None, task_status=None, task_status_list_shrink=None, task_type=None,
                 task_type_list_shrink=None):
        self.agent_key = agent_key  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_time_start = create_time_start  # type: str
        self.current = current  # type: int
        self.size = size  # type: int
        self.task_code = task_code  # type: str
        self.task_name = task_name  # type: str
        self.task_status = task_status  # type: int
        self.task_status_list_shrink = task_status_list_shrink  # type: str
        self.task_type = task_type  # type: str
        self.task_type_list_shrink = task_type_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsyncTasksShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_list_shrink is not None:
            result['TaskStatusList'] = self.task_status_list_shrink
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_list_shrink is not None:
            result['TaskTypeList'] = self.task_type_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusList') is not None:
            self.task_status_list_shrink = m.get('TaskStatusList')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeList') is not None:
            self.task_type_list_shrink = m.get('TaskTypeList')
        return self


class ListAsyncTasksResponseBodyData(TeaModel):
    def __init__(self, create_time=None, create_user=None, id=None, task_code=None, task_definition=None,
                 task_end_time=None, task_error_message=None, task_execute_time=None, task_id=None,
                 task_inner_error_message=None, task_intermediate_result=None, task_name=None, task_param=None, task_progress_message=None,
                 task_result=None, task_retry_count=None, task_start_time=None, task_status=None, task_type=None,
                 update_time=None, update_user=None):
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.id = id  # type: long
        self.task_code = task_code  # type: str
        self.task_definition = task_definition  # type: str
        self.task_end_time = task_end_time  # type: str
        self.task_error_message = task_error_message  # type: str
        self.task_execute_time = task_execute_time  # type: str
        self.task_id = task_id  # type: str
        self.task_inner_error_message = task_inner_error_message  # type: str
        self.task_intermediate_result = task_intermediate_result  # type: str
        self.task_name = task_name  # type: str
        self.task_param = task_param  # type: str
        self.task_progress_message = task_progress_message  # type: str
        self.task_result = task_result  # type: str
        self.task_retry_count = task_retry_count  # type: str
        self.task_start_time = task_start_time  # type: str
        self.task_status = task_status  # type: int
        self.task_type = task_type  # type: str
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAsyncTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_definition is not None:
            result['TaskDefinition'] = self.task_definition
        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_execute_time is not None:
            result['TaskExecuteTime'] = self.task_execute_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_inner_error_message is not None:
            result['TaskInnerErrorMessage'] = self.task_inner_error_message
        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        if self.task_progress_message is not None:
            result['TaskProgressMessage'] = self.task_progress_message
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_retry_count is not None:
            result['TaskRetryCount'] = self.task_retry_count
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskDefinition') is not None:
            self.task_definition = m.get('TaskDefinition')
        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskExecuteTime') is not None:
            self.task_execute_time = m.get('TaskExecuteTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskInnerErrorMessage') is not None:
            self.task_inner_error_message = m.get('TaskInnerErrorMessage')
        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        if m.get('TaskProgressMessage') is not None:
            self.task_progress_message = m.get('TaskProgressMessage')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskRetryCount') is not None:
            self.task_retry_count = m.get('TaskRetryCount')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class ListAsyncTasksResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, http_status_code=None, message=None, request_id=None,
                 size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[ListAsyncTasksResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAsyncTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAsyncTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAsyncTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAsyncTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAsyncTasksResponse, self).to_map()
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
            temp_model = ListAsyncTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBuildConfigsRequest(TeaModel):
    def __init__(self, agent_key=None, type=None):
        self.agent_key = agent_key  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBuildConfigsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBuildConfigsResponseBodyDataKeywords(TeaModel):
    def __init__(self, description=None, key=None):
        self.description = description  # type: str
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBuildConfigsResponseBodyDataKeywords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListBuildConfigsResponseBodyData(TeaModel):
    def __init__(self, build_in=None, create_time=None, create_user=None, id=None, keywords=None, tag=None,
                 tag_description=None, type=None, update_time=None, update_user=None):
        self.build_in = build_in  # type: bool
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.id = id  # type: long
        self.keywords = keywords  # type: list[ListBuildConfigsResponseBodyDataKeywords]
        self.tag = tag  # type: str
        self.tag_description = tag_description  # type: str
        self.type = type  # type: str
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str

    def validate(self):
        if self.keywords:
            for k in self.keywords:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBuildConfigsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_in is not None:
            result['BuildIn'] = self.build_in
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        result['Keywords'] = []
        if self.keywords is not None:
            for k in self.keywords:
                result['Keywords'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BuildIn') is not None:
            self.build_in = m.get('BuildIn')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.keywords = []
        if m.get('Keywords') is not None:
            for k in m.get('Keywords'):
                temp_model = ListBuildConfigsResponseBodyDataKeywords()
                self.keywords.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class ListBuildConfigsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListBuildConfigsResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListBuildConfigsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListBuildConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBuildConfigsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListBuildConfigsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBuildConfigsResponse, self).to_map()
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
            temp_model = ListBuildConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDialoguesRequest(TeaModel):
    def __init__(self, agent_key=None, current=None, dialogue_type=None, end_time=None, size=None, start_time=None,
                 task_id=None):
        self.agent_key = agent_key  # type: str
        self.current = current  # type: int
        self.dialogue_type = dialogue_type  # type: int
        self.end_time = end_time  # type: str
        self.size = size  # type: int
        self.start_time = start_time  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDialoguesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.current is not None:
            result['Current'] = self.current
        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListDialoguesResponseBodyData(TeaModel):
    def __init__(self, bot=None, create_time=None, create_user=None, dialogue_type=None, task_id=None, user=None):
        self.bot = bot  # type: str
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.dialogue_type = dialogue_type  # type: int
        self.task_id = task_id  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDialoguesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot is not None:
            result['Bot'] = self.bot
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bot') is not None:
            self.bot = m.get('Bot')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class ListDialoguesResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, http_status_code=None, message=None, request_id=None,
                 size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[ListDialoguesResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDialoguesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDialoguesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDialoguesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDialoguesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDialoguesResponse, self).to_map()
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
            temp_model = ListDialoguesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGeneratedContentsRequest(TeaModel):
    def __init__(self, agent_key=None, content_domain=None, current=None, end_time=None, size=None, start_time=None,
                 title=None):
        self.agent_key = agent_key  # type: str
        self.content_domain = content_domain  # type: str
        self.current = current  # type: int
        self.end_time = end_time  # type: str
        self.size = size  # type: int
        self.start_time = start_time  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGeneratedContentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.current is not None:
            result['Current'] = self.current
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListGeneratedContentsResponseBodyData(TeaModel):
    def __init__(self, content=None, content_domain=None, content_text=None, create_time=None, create_user=None,
                 device_id=None, id=None, keyword_list=None, keywords=None, prompt=None, task_id=None, title=None,
                 update_time=None, update_user=None, uuid=None):
        self.content = content  # type: str
        self.content_domain = content_domain  # type: str
        self.content_text = content_text  # type: str
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.device_id = device_id  # type: str
        self.id = id  # type: long
        self.keyword_list = keyword_list  # type: list[str]
        self.keywords = keywords  # type: str
        self.prompt = prompt  # type: str
        self.task_id = task_id  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGeneratedContentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword_list is not None:
            result['KeywordList'] = self.keyword_list
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeywordList') is not None:
            self.keyword_list = m.get('KeywordList')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListGeneratedContentsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, http_status_code=None, message=None, request_id=None,
                 size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[ListGeneratedContentsResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGeneratedContentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGeneratedContentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListGeneratedContentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGeneratedContentsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGeneratedContentsResponse, self).to_map()
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
            temp_model = ListGeneratedContentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotNewsWithTypeRequest(TeaModel):
    def __init__(self, agent_key=None, current=None, news_type=None, news_types=None, size=None):
        self.agent_key = agent_key  # type: str
        self.current = current  # type: int
        self.news_type = news_type  # type: str
        self.news_types = news_types  # type: list[str]
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotNewsWithTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.current is not None:
            result['Current'] = self.current
        if self.news_type is not None:
            result['NewsType'] = self.news_type
        if self.news_types is not None:
            result['NewsTypes'] = self.news_types
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')
        if m.get('NewsTypes') is not None:
            self.news_types = m.get('NewsTypes')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListHotNewsWithTypeShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, current=None, news_type=None, news_types_shrink=None, size=None):
        self.agent_key = agent_key  # type: str
        self.current = current  # type: int
        self.news_type = news_type  # type: str
        self.news_types_shrink = news_types_shrink  # type: str
        self.size = size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotNewsWithTypeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.current is not None:
            result['Current'] = self.current
        if self.news_type is not None:
            result['NewsType'] = self.news_type
        if self.news_types_shrink is not None:
            result['NewsTypes'] = self.news_types_shrink
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')
        if m.get('NewsTypes') is not None:
            self.news_types_shrink = m.get('NewsTypes')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListHotNewsWithTypeResponseBodyDataNews(TeaModel):
    def __init__(self, author=None, content=None, doc_uuid=None, image_urls=None, pub_time=None, search_source=None,
                 search_source_name=None, source=None, summary=None, tag=None, title=None, update_time=None, url=None):
        self.author = author  # type: str
        self.content = content  # type: str
        self.doc_uuid = doc_uuid  # type: str
        self.image_urls = image_urls  # type: list[str]
        self.pub_time = pub_time  # type: str
        self.search_source = search_source  # type: str
        self.search_source_name = search_source_name  # type: str
        self.source = source  # type: str
        self.summary = summary  # type: str
        self.tag = tag  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotNewsWithTypeResponseBodyDataNews, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.search_source is not None:
            result['SearchSource'] = self.search_source
        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')
        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListHotNewsWithTypeResponseBodyData(TeaModel):
    def __init__(self, news=None, news_type=None, news_type_name=None, total_pages=None):
        self.news = news  # type: list[ListHotNewsWithTypeResponseBodyDataNews]
        self.news_type = news_type  # type: str
        self.news_type_name = news_type_name  # type: str
        self.total_pages = total_pages  # type: int

    def validate(self):
        if self.news:
            for k in self.news:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotNewsWithTypeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['News'] = []
        if self.news is not None:
            for k in self.news:
                result['News'].append(k.to_map() if k else None)
        if self.news_type is not None:
            result['NewsType'] = self.news_type
        if self.news_type_name is not None:
            result['NewsTypeName'] = self.news_type_name
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.news = []
        if m.get('News') is not None:
            for k in m.get('News'):
                temp_model = ListHotNewsWithTypeResponseBodyDataNews()
                self.news.append(temp_model.from_map(k))
        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')
        if m.get('NewsTypeName') is not None:
            self.news_type_name = m.get('NewsTypeName')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListHotNewsWithTypeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListHotNewsWithTypeResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotNewsWithTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotNewsWithTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotNewsWithTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHotNewsWithTypeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotNewsWithTypeResponse, self).to_map()
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
            temp_model = ListHotNewsWithTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterveneCntRequest(TeaModel):
    def __init__(self, agent_key=None, page_index=None, page_size=None):
        self.agent_key = agent_key  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterveneCntRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneCntResponseBodyData(TeaModel):
    def __init__(self, cnt_list=None, page_cnt=None, page_index=None, page_size=None):
        self.cnt_list = cnt_list  # type: list[any]
        self.page_cnt = page_cnt  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterveneCntResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cnt_list is not None:
            result['CntList'] = self.cnt_list
        if self.page_cnt is not None:
            result['PageCnt'] = self.page_cnt
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CntList') is not None:
            self.cnt_list = m.get('CntList')
        if m.get('PageCnt') is not None:
            self.page_cnt = m.get('PageCnt')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneCntResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListInterveneCntResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInterveneCntResponseBody, self).to_map()
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
            temp_model = ListInterveneCntResponseBodyData()
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


class ListInterveneCntResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterveneCntResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterveneCntResponse, self).to_map()
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
            temp_model = ListInterveneCntResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterveneImportTasksRequest(TeaModel):
    def __init__(self, agent_key=None, page_index=None, page_size=None):
        self.agent_key = agent_key  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterveneImportTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneImportTasksResponseBodyDataStatusList(TeaModel):
    def __init__(self, msg=None, percentage=None, status=None, task_id=None, task_name=None):
        self.msg = msg  # type: str
        self.percentage = percentage  # type: int
        self.status = status  # type: int
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterveneImportTasksResponseBodyDataStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListInterveneImportTasksResponseBodyData(TeaModel):
    def __init__(self, page_index=None, page_size=None, status_list=None, total_size=None):
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.status_list = status_list  # type: list[ListInterveneImportTasksResponseBodyDataStatusList]
        self.total_size = total_size  # type: int

    def validate(self):
        if self.status_list:
            for k in self.status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterveneImportTasksResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['StatusList'] = []
        if self.status_list is not None:
            for k in self.status_list:
                result['StatusList'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.status_list = []
        if m.get('StatusList') is not None:
            for k in m.get('StatusList'):
                temp_model = ListInterveneImportTasksResponseBodyDataStatusList()
                self.status_list.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListInterveneImportTasksResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListInterveneImportTasksResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInterveneImportTasksResponseBody, self).to_map()
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
            temp_model = ListInterveneImportTasksResponseBodyData()
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


class ListInterveneImportTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterveneImportTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterveneImportTasksResponse, self).to_map()
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
            temp_model = ListInterveneImportTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterveneRulesRequest(TeaModel):
    def __init__(self, agent_key=None, page_index=None, page_size=None):
        self.agent_key = agent_key  # type: str
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterveneRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig(TeaModel):
    def __init__(self, answer_type=None, message=None, namespace=None):
        self.answer_type = answer_type  # type: int
        self.message = message  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class ListInterveneRulesResponseBodyDataInterveneRuleList(TeaModel):
    def __init__(self, answer_config=None, create_time=None, effect_time=None, intervene_type=None,
                 namespace_list=None, rule_id=None, rule_name=None):
        self.answer_config = answer_config  # type: list[ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig]
        self.create_time = create_time  # type: str
        self.effect_time = effect_time  # type: str
        self.intervene_type = intervene_type  # type: int
        self.namespace_list = namespace_list  # type: list[str]
        self.rule_id = rule_id  # type: long
        self.rule_name = rule_name  # type: str

    def validate(self):
        if self.answer_config:
            for k in self.answer_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterveneRulesResponseBodyDataInterveneRuleList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k in self.answer_config:
                result['AnswerConfig'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k in m.get('AnswerConfig'):
                temp_model = ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig()
                self.answer_config.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListInterveneRulesResponseBodyData(TeaModel):
    def __init__(self, count=None, intervene_rule_list=None, page_index=None, page_size=None):
        self.count = count  # type: long
        self.intervene_rule_list = intervene_rule_list  # type: list[ListInterveneRulesResponseBodyDataInterveneRuleList]
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.intervene_rule_list:
            for k in self.intervene_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInterveneRulesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['InterveneRuleList'] = []
        if self.intervene_rule_list is not None:
            for k in self.intervene_rule_list:
                result['InterveneRuleList'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.intervene_rule_list = []
        if m.get('InterveneRuleList') is not None:
            for k in m.get('InterveneRuleList'):
                temp_model = ListInterveneRulesResponseBodyDataInterveneRuleList()
                self.intervene_rule_list.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneRulesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListInterveneRulesResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListInterveneRulesResponseBody, self).to_map()
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
            temp_model = ListInterveneRulesResponseBodyData()
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


class ListInterveneRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInterveneRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInterveneRulesResponse, self).to_map()
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
            temp_model = ListInterveneRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntervenesRequest(TeaModel):
    def __init__(self, agent_key=None, intervene_type=None, page_index=None, page_size=None, query=None,
                 rule_id=None):
        self.agent_key = agent_key  # type: str
        self.intervene_type = intervene_type  # type: int
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.rule_id = rule_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntervenesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListIntervenesResponseBodyDataInterveneList(TeaModel):
    def __init__(self, id=None, query=None):
        # id
        self.id = id  # type: str
        self.query = query  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListIntervenesResponseBodyDataInterveneList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ListIntervenesResponseBodyData(TeaModel):
    def __init__(self, intervene_list=None, page_index=None, page_size=None, total_size=None):
        self.intervene_list = intervene_list  # type: list[ListIntervenesResponseBodyDataInterveneList]
        self.page_index = page_index  # type: int
        self.page_size = page_size  # type: int
        self.total_size = total_size  # type: long

    def validate(self):
        if self.intervene_list:
            for k in self.intervene_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListIntervenesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InterveneList'] = []
        if self.intervene_list is not None:
            for k in self.intervene_list:
                result['InterveneList'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.intervene_list = []
        if m.get('InterveneList') is not None:
            for k in m.get('InterveneList'):
                temp_model = ListIntervenesResponseBodyDataInterveneList()
                self.intervene_list.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListIntervenesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ListIntervenesResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListIntervenesResponseBody, self).to_map()
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
            temp_model = ListIntervenesResponseBodyData()
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


class ListIntervenesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListIntervenesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListIntervenesResponse, self).to_map()
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
            temp_model = ListIntervenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMaterialDocumentsRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, create_time_end=None, create_time_start=None, current=None,
                 doc_type=None, doc_type_list=None, generate_public_url=None, id=None, keywords=None, query=None,
                 share_attr=None, size=None, title=None, update_time_end=None, update_time_start=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_time_start = create_time_start  # type: str
        self.current = current  # type: int
        self.doc_type = doc_type  # type: str
        self.doc_type_list = doc_type_list  # type: list[str]
        self.generate_public_url = generate_public_url  # type: bool
        self.id = id  # type: long
        self.keywords = keywords  # type: list[str]
        self.query = query  # type: str
        self.share_attr = share_attr  # type: int
        self.size = size  # type: int
        self.title = title  # type: str
        self.update_time_end = update_time_end  # type: str
        self.update_time_start = update_time_start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMaterialDocumentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_type_list is not None:
            result['DocTypeList'] = self.doc_type_list
        if self.generate_public_url is not None:
            result['GeneratePublicUrl'] = self.generate_public_url
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.query is not None:
            result['Query'] = self.query
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.size is not None:
            result['Size'] = self.size
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_end is not None:
            result['UpdateTimeEnd'] = self.update_time_end
        if self.update_time_start is not None:
            result['UpdateTimeStart'] = self.update_time_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocTypeList') is not None:
            self.doc_type_list = m.get('DocTypeList')
        if m.get('GeneratePublicUrl') is not None:
            self.generate_public_url = m.get('GeneratePublicUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeEnd') is not None:
            self.update_time_end = m.get('UpdateTimeEnd')
        if m.get('UpdateTimeStart') is not None:
            self.update_time_start = m.get('UpdateTimeStart')
        return self


class ListMaterialDocumentsShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, create_time_end=None, create_time_start=None, current=None,
                 doc_type=None, doc_type_list_shrink=None, generate_public_url=None, id=None, keywords_shrink=None,
                 query=None, share_attr=None, size=None, title=None, update_time_end=None, update_time_start=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.create_time_end = create_time_end  # type: str
        self.create_time_start = create_time_start  # type: str
        self.current = current  # type: int
        self.doc_type = doc_type  # type: str
        self.doc_type_list_shrink = doc_type_list_shrink  # type: str
        self.generate_public_url = generate_public_url  # type: bool
        self.id = id  # type: long
        self.keywords_shrink = keywords_shrink  # type: str
        self.query = query  # type: str
        self.share_attr = share_attr  # type: int
        self.size = size  # type: int
        self.title = title  # type: str
        self.update_time_end = update_time_end  # type: str
        self.update_time_start = update_time_start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMaterialDocumentsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_type_list_shrink is not None:
            result['DocTypeList'] = self.doc_type_list_shrink
        if self.generate_public_url is not None:
            result['GeneratePublicUrl'] = self.generate_public_url
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink
        if self.query is not None:
            result['Query'] = self.query
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.size is not None:
            result['Size'] = self.size
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_end is not None:
            result['UpdateTimeEnd'] = self.update_time_end
        if self.update_time_start is not None:
            result['UpdateTimeStart'] = self.update_time_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocTypeList') is not None:
            self.doc_type_list_shrink = m.get('DocTypeList')
        if m.get('GeneratePublicUrl') is not None:
            self.generate_public_url = m.get('GeneratePublicUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeEnd') is not None:
            self.update_time_end = m.get('UpdateTimeEnd')
        if m.get('UpdateTimeStart') is not None:
            self.update_time_start = m.get('UpdateTimeStart')
        return self


class ListMaterialDocumentsResponseBodyData(TeaModel):
    def __init__(self, author=None, create_time=None, create_user=None, create_user_name=None, doc_keywords=None,
                 doc_type=None, external_url=None, html_content=None, id=None, pub_time=None, public_url=None,
                 share_attr=None, src_from=None, summary=None, text_content=None, thumbnail_in_base_64=None, title=None,
                 update_time=None, update_user=None, update_user_name=None, url=None):
        self.author = author  # type: str
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.create_user_name = create_user_name  # type: str
        self.doc_keywords = doc_keywords  # type: list[str]
        self.doc_type = doc_type  # type: str
        self.external_url = external_url  # type: str
        self.html_content = html_content  # type: str
        self.id = id  # type: long
        self.pub_time = pub_time  # type: str
        self.public_url = public_url  # type: str
        self.share_attr = share_attr  # type: int
        self.src_from = src_from  # type: str
        self.summary = summary  # type: str
        self.text_content = text_content  # type: str
        self.thumbnail_in_base_64 = thumbnail_in_base_64  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str
        self.update_user_name = update_user_name  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMaterialDocumentsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.thumbnail_in_base_64 is not None:
            result['ThumbnailInBase64'] = self.thumbnail_in_base_64
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('ThumbnailInBase64') is not None:
            self.thumbnail_in_base_64 = m.get('ThumbnailInBase64')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListMaterialDocumentsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, http_status_code=None, message=None, request_id=None,
                 size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[ListMaterialDocumentsResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMaterialDocumentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMaterialDocumentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMaterialDocumentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMaterialDocumentsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMaterialDocumentsResponse, self).to_map()
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
            temp_model = ListMaterialDocumentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVersionsRequest(TeaModel):
    def __init__(self, agent_key=None):
        self.agent_key = agent_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ListVersionsResponseBodyData(TeaModel):
    def __init__(self, concurrent_count=None, end_time=None, instance_count=None, instance_id=None, order_id=None,
                 product_type=None, quota=None, start_time=None, use_quota=None, version_detail=None, version_name=None,
                 version_status=None):
        self.concurrent_count = concurrent_count  # type: int
        self.end_time = end_time  # type: str
        self.instance_count = instance_count  # type: int
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: long
        self.product_type = product_type  # type: str
        self.quota = quota  # type: int
        self.start_time = start_time  # type: str
        self.use_quota = use_quota  # type: int
        self.version_detail = version_detail  # type: str
        self.version_name = version_name  # type: str
        self.version_status = version_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVersionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrent_count is not None:
            result['ConcurrentCount'] = self.concurrent_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.use_quota is not None:
            result['UseQuota'] = self.use_quota
        if self.version_detail is not None:
            result['VersionDetail'] = self.version_detail
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConcurrentCount') is not None:
            self.concurrent_count = m.get('ConcurrentCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UseQuota') is not None:
            self.use_quota = m.get('UseQuota')
        if m.get('VersionDetail') is not None:
            self.version_detail = m.get('VersionDetail')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        return self


class ListVersionsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[ListVersionsResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVersionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVersionsResponse, self).to_map()
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
            temp_model = ListVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAsyncTaskRequest(TeaModel):
    def __init__(self, agent_key=None, task_id=None):
        self.agent_key = agent_key  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryAsyncTaskResponseBodyData(TeaModel):
    def __init__(self, create_time=None, create_user=None, task_code=None, task_error_message=None, task_id=None,
                 task_intermediate_result=None, task_name=None, task_param=None, task_progress_message=None, task_result=None,
                 task_retry_count=None, task_status=None, update_time=None, update_user=None):
        self.create_time = create_time  # type: str
        self.create_user = create_user  # type: str
        self.task_code = task_code  # type: str
        self.task_error_message = task_error_message  # type: str
        self.task_id = task_id  # type: str
        self.task_intermediate_result = task_intermediate_result  # type: str
        self.task_name = task_name  # type: str
        self.task_param = task_param  # type: str
        self.task_progress_message = task_progress_message  # type: str
        self.task_result = task_result  # type: str
        self.task_retry_count = task_retry_count  # type: str
        self.task_status = task_status  # type: int
        self.update_time = update_time  # type: str
        self.update_user = update_user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAsyncTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        if self.task_progress_message is not None:
            result['TaskProgressMessage'] = self.task_progress_message
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_retry_count is not None:
            result['TaskRetryCount'] = self.task_retry_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        if m.get('TaskProgressMessage') is not None:
            self.task_progress_message = m.get('TaskProgressMessage')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskRetryCount') is not None:
            self.task_retry_count = m.get('TaskRetryCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class QueryAsyncTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAsyncTaskResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAsyncTaskResponseBody, self).to_map()
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
            temp_model = QueryAsyncTaskResponseBodyData()
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


class QueryAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAsyncTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAsyncTaskResponse, self).to_map()
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
            temp_model = QueryAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveDataSourceOrderConfigRequestUserConfigDataSourceList(TeaModel):
    def __init__(self, code=None, name=None, number=None, type=None):
        self.code = code  # type: str
        self.name = name  # type: str
        self.number = number  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveDataSourceOrderConfigRequestUserConfigDataSourceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveDataSourceOrderConfigRequest(TeaModel):
    def __init__(self, agent_key=None, product_code=None, user_config_data_source_list=None):
        self.agent_key = agent_key  # type: str
        self.product_code = product_code  # type: str
        self.user_config_data_source_list = user_config_data_source_list  # type: list[SaveDataSourceOrderConfigRequestUserConfigDataSourceList]

    def validate(self):
        if self.user_config_data_source_list:
            for k in self.user_config_data_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SaveDataSourceOrderConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['UserConfigDataSourceList'] = []
        if self.user_config_data_source_list is not None:
            for k in self.user_config_data_source_list:
                result['UserConfigDataSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.user_config_data_source_list = []
        if m.get('UserConfigDataSourceList') is not None:
            for k in m.get('UserConfigDataSourceList'):
                temp_model = SaveDataSourceOrderConfigRequestUserConfigDataSourceList()
                self.user_config_data_source_list.append(temp_model.from_map(k))
        return self


class SaveDataSourceOrderConfigShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, product_code=None, user_config_data_source_list_shrink=None):
        self.agent_key = agent_key  # type: str
        self.product_code = product_code  # type: str
        self.user_config_data_source_list_shrink = user_config_data_source_list_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveDataSourceOrderConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_config_data_source_list_shrink is not None:
            result['UserConfigDataSourceList'] = self.user_config_data_source_list_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserConfigDataSourceList') is not None:
            self.user_config_data_source_list_shrink = m.get('UserConfigDataSourceList')
        return self


class SaveDataSourceOrderConfigResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveDataSourceOrderConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveDataSourceOrderConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveDataSourceOrderConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveDataSourceOrderConfigResponse, self).to_map()
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
            temp_model = SaveDataSourceOrderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveMaterialDocumentRequest(TeaModel):
    def __init__(self, agent_key=None, author=None, both_save_private_and_share=None, doc_keywords=None,
                 doc_type=None, external_url=None, html_content=None, pub_time=None, share_attr=None, src_from=None,
                 summary=None, text_content=None, title=None, url=None):
        self.agent_key = agent_key  # type: str
        self.author = author  # type: str
        self.both_save_private_and_share = both_save_private_and_share  # type: bool
        self.doc_keywords = doc_keywords  # type: list[str]
        self.doc_type = doc_type  # type: str
        self.external_url = external_url  # type: str
        self.html_content = html_content  # type: str
        self.pub_time = pub_time  # type: str
        self.share_attr = share_attr  # type: int
        self.src_from = src_from  # type: str
        self.summary = summary  # type: str
        self.text_content = text_content  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveMaterialDocumentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.both_save_private_and_share is not None:
            result['BothSavePrivateAndShare'] = self.both_save_private_and_share
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('BothSavePrivateAndShare') is not None:
            self.both_save_private_and_share = m.get('BothSavePrivateAndShare')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SaveMaterialDocumentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, author=None, both_save_private_and_share=None, doc_keywords_shrink=None,
                 doc_type=None, external_url=None, html_content=None, pub_time=None, share_attr=None, src_from=None,
                 summary=None, text_content=None, title=None, url=None):
        self.agent_key = agent_key  # type: str
        self.author = author  # type: str
        self.both_save_private_and_share = both_save_private_and_share  # type: bool
        self.doc_keywords_shrink = doc_keywords_shrink  # type: str
        self.doc_type = doc_type  # type: str
        self.external_url = external_url  # type: str
        self.html_content = html_content  # type: str
        self.pub_time = pub_time  # type: str
        self.share_attr = share_attr  # type: int
        self.src_from = src_from  # type: str
        self.summary = summary  # type: str
        self.text_content = text_content  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveMaterialDocumentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.both_save_private_and_share is not None:
            result['BothSavePrivateAndShare'] = self.both_save_private_and_share
        if self.doc_keywords_shrink is not None:
            result['DocKeywords'] = self.doc_keywords_shrink
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('BothSavePrivateAndShare') is not None:
            self.both_save_private_and_share = m.get('BothSavePrivateAndShare')
        if m.get('DocKeywords') is not None:
            self.doc_keywords_shrink = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SaveMaterialDocumentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveMaterialDocumentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveMaterialDocumentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveMaterialDocumentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveMaterialDocumentResponse, self).to_map()
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
            temp_model = SaveMaterialDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchNewsRequest(TeaModel):
    def __init__(self, agent_key=None, filter_not_null=None, include_content=None, page=None, page_size=None,
                 query=None, search_sources=None):
        self.agent_key = agent_key  # type: str
        self.filter_not_null = filter_not_null  # type: bool
        self.include_content = include_content  # type: bool
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.search_sources = search_sources  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchNewsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.filter_not_null is not None:
            result['FilterNotNull'] = self.filter_not_null
        if self.include_content is not None:
            result['IncludeContent'] = self.include_content
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.search_sources is not None:
            result['SearchSources'] = self.search_sources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FilterNotNull') is not None:
            self.filter_not_null = m.get('FilterNotNull')
        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchSources') is not None:
            self.search_sources = m.get('SearchSources')
        return self


class SearchNewsShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, filter_not_null=None, include_content=None, page=None, page_size=None,
                 query=None, search_sources_shrink=None):
        self.agent_key = agent_key  # type: str
        self.filter_not_null = filter_not_null  # type: bool
        self.include_content = include_content  # type: bool
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.query = query  # type: str
        self.search_sources_shrink = search_sources_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchNewsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.filter_not_null is not None:
            result['FilterNotNull'] = self.filter_not_null
        if self.include_content is not None:
            result['IncludeContent'] = self.include_content
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.search_sources_shrink is not None:
            result['SearchSources'] = self.search_sources_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FilterNotNull') is not None:
            self.filter_not_null = m.get('FilterNotNull')
        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchSources') is not None:
            self.search_sources_shrink = m.get('SearchSources')
        return self


class SearchNewsResponseBodyData(TeaModel):
    def __init__(self, author=None, content=None, doc_uuid=None, image_urls=None, pub_time=None, search_source=None,
                 search_source_name=None, source=None, summary=None, tag=None, title=None, update_time=None, url=None):
        self.author = author  # type: str
        self.content = content  # type: str
        self.doc_uuid = doc_uuid  # type: str
        self.image_urls = image_urls  # type: list[str]
        self.pub_time = pub_time  # type: str
        self.search_source = search_source  # type: str
        self.search_source_name = search_source_name  # type: str
        self.source = source  # type: str
        self.summary = summary  # type: str
        self.tag = tag  # type: str
        self.title = title  # type: str
        self.update_time = update_time  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchNewsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.search_source is not None:
            result['SearchSource'] = self.search_source
        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')
        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SearchNewsResponseBody(TeaModel):
    def __init__(self, code=None, current=None, data=None, http_status_code=None, message=None, request_id=None,
                 size=None, success=None, total=None):
        self.code = code  # type: str
        self.current = current  # type: int
        self.data = data  # type: list[SearchNewsResponseBodyData]
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.size = size  # type: int
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchNewsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchNewsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchNewsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchNewsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchNewsResponse, self).to_map()
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
            temp_model = SearchNewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAsyncTaskRequest(TeaModel):
    def __init__(self, agent_key=None, task_code=None, task_execute_time=None, task_name=None, task_param=None):
        self.agent_key = agent_key  # type: str
        self.task_code = task_code  # type: str
        self.task_execute_time = task_execute_time  # type: str
        self.task_name = task_name  # type: str
        self.task_param = task_param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAsyncTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_execute_time is not None:
            result['TaskExecuteTime'] = self.task_execute_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskExecuteTime') is not None:
            self.task_execute_time = m.get('TaskExecuteTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        return self


class SubmitAsyncTaskResponseBodyData(TeaModel):
    def __init__(self, task_id=None, task_intermediate_result=None, task_name=None):
        self.task_id = task_id  # type: str
        self.task_intermediate_result = task_intermediate_result  # type: any
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAsyncTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class SubmitAsyncTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitAsyncTaskResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitAsyncTaskResponseBody, self).to_map()
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
            temp_model = SubmitAsyncTaskResponseBodyData()
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


class SubmitAsyncTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAsyncTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAsyncTaskResponse, self).to_map()
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
            temp_model = SubmitAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGeneratedContentRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, content_text=None, id=None, keywords=None, prompt=None,
                 title=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.content_text = content_text  # type: str
        self.id = id  # type: long
        self.keywords = keywords  # type: list[str]
        self.prompt = prompt  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGeneratedContentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateGeneratedContentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, content=None, content_text=None, id=None, keywords_shrink=None, prompt=None,
                 title=None):
        self.agent_key = agent_key  # type: str
        self.content = content  # type: str
        self.content_text = content_text  # type: str
        self.id = id  # type: long
        self.keywords_shrink = keywords_shrink  # type: str
        self.prompt = prompt  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGeneratedContentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateGeneratedContentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGeneratedContentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGeneratedContentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGeneratedContentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGeneratedContentResponse, self).to_map()
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
            temp_model = UpdateGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMaterialDocumentRequest(TeaModel):
    def __init__(self, agent_key=None, author=None, doc_keywords=None, doc_type=None, external_url=None,
                 html_content=None, id=None, pub_time=None, share_attr=None, src_from=None, summary=None, text_content=None,
                 title=None, url=None):
        self.agent_key = agent_key  # type: str
        self.author = author  # type: str
        self.doc_keywords = doc_keywords  # type: list[str]
        self.doc_type = doc_type  # type: str
        self.external_url = external_url  # type: str
        self.html_content = html_content  # type: str
        self.id = id  # type: long
        self.pub_time = pub_time  # type: str
        self.share_attr = share_attr  # type: int
        self.src_from = src_from  # type: str
        self.summary = summary  # type: str
        self.text_content = text_content  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialDocumentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateMaterialDocumentShrinkRequest(TeaModel):
    def __init__(self, agent_key=None, author=None, doc_keywords_shrink=None, doc_type=None, external_url=None,
                 html_content=None, id=None, pub_time=None, share_attr=None, src_from=None, summary=None, text_content=None,
                 title=None, url=None):
        self.agent_key = agent_key  # type: str
        self.author = author  # type: str
        self.doc_keywords_shrink = doc_keywords_shrink  # type: str
        self.doc_type = doc_type  # type: str
        self.external_url = external_url  # type: str
        self.html_content = html_content  # type: str
        self.id = id  # type: long
        self.pub_time = pub_time  # type: str
        self.share_attr = share_attr  # type: int
        self.src_from = src_from  # type: str
        self.summary = summary  # type: str
        self.text_content = text_content  # type: str
        self.title = title  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialDocumentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.doc_keywords_shrink is not None:
            result['DocKeywords'] = self.doc_keywords_shrink
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('DocKeywords') is not None:
            self.doc_keywords_shrink = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateMaterialDocumentResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMaterialDocumentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMaterialDocumentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateMaterialDocumentResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMaterialDocumentResponse, self).to_map()
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
            temp_model = UpdateMaterialDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


