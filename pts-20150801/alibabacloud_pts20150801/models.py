# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateTransactionRequest(TeaModel):
    def __init__(self, script_id=None, transaction_name=None):
        self.script_id = script_id  # type: int
        self.transaction_name = transaction_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransactionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.transaction_name is not None:
            result['TransactionName'] = self.transaction_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TransactionName') is not None:
            self.transaction_name = m.get('TransactionName')
        return self


class CreateTransactionResponseBody(TeaModel):
    def __init__(self, request_id=None, transaction_id=None):
        self.request_id = request_id  # type: str
        self.transaction_id = transaction_id  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTransactionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.transaction_id is not None:
            result['TransactionId'] = self.transaction_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TransactionId') is not None:
            self.transaction_id = m.get('TransactionId')
        return self


class CreateTransactionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTransactionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTransactionResponse, self).to_map()
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
            temp_model = CreateTransactionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKeySecretResponseBody(TeaModel):
    def __init__(self, key=None, request_id=None, secret=None):
        self.key = key  # type: str
        self.request_id = request_id  # type: str
        self.secret = secret  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetKeySecretResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.secret is not None:
            result['Secret'] = self.secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Secret') is not None:
            self.secret = m.get('Secret')
        return self


class GetKeySecretResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetKeySecretResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetKeySecretResponse, self).to_map()
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
            temp_model = GetKeySecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScriptRequest(TeaModel):
    def __init__(self, script_id=None, tfsname=None):
        self.script_id = script_id  # type: int
        self.tfsname = tfsname  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScriptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.tfsname is not None:
            result['Tfsname'] = self.tfsname
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Tfsname') is not None:
            self.tfsname = m.get('Tfsname')
        return self


class GetScriptResponseBody(TeaModel):
    def __init__(self, request_id=None, script=None):
        self.request_id = request_id  # type: str
        self.script = script  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetScriptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class GetScriptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetScriptResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetScriptResponse, self).to_map()
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
            temp_model = GetScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTasksRequest(TeaModel):
    def __init__(self, status=None):
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTasksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetTasksResponseBody(TeaModel):
    def __init__(self, request_id=None, tasks=None):
        self.request_id = request_id  # type: str
        self.tasks = tasks  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTasksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tasks is not None:
            result['Tasks'] = self.tasks
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')
        return self


class GetTasksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTasksResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTasksResponse, self).to_map()
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
            temp_model = GetTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportLogSampleRequest(TeaModel):
    def __init__(self, log_sample=None, scenario_id=None, wskey=None):
        self.log_sample = log_sample  # type: str
        self.scenario_id = scenario_id  # type: int
        self.wskey = wskey  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportLogSampleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_sample is not None:
            result['LogSample'] = self.log_sample
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.wskey is not None:
            result['Wskey'] = self.wskey
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LogSample') is not None:
            self.log_sample = m.get('LogSample')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Wskey') is not None:
            self.wskey = m.get('Wskey')
        return self


class ReportLogSampleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportLogSampleResponseBody, self).to_map()
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


class ReportLogSampleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportLogSampleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportLogSampleResponse, self).to_map()
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
            temp_model = ReportLogSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportTestSampleRequest(TeaModel):
    def __init__(self, test_sample=None):
        self.test_sample = test_sample  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportTestSampleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.test_sample is not None:
            result['TestSample'] = self.test_sample
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TestSample') is not None:
            self.test_sample = m.get('TestSample')
        return self


class ReportTestSampleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportTestSampleResponseBody, self).to_map()
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


class ReportTestSampleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportTestSampleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportTestSampleResponse, self).to_map()
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
            temp_model = ReportTestSampleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportVuserRequest(TeaModel):
    def __init__(self, gmt_created=None, scenario_id=None, vuser=None, wskey=None):
        self.gmt_created = gmt_created  # type: long
        self.scenario_id = scenario_id  # type: int
        self.vuser = vuser  # type: int
        self.wskey = wskey  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportVuserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.vuser is not None:
            result['Vuser'] = self.vuser
        if self.wskey is not None:
            result['Wskey'] = self.wskey
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Vuser') is not None:
            self.vuser = m.get('Vuser')
        if m.get('Wskey') is not None:
            self.wskey = m.get('Wskey')
        return self


class ReportVuserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportVuserResponseBody, self).to_map()
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


class ReportVuserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportVuserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportVuserResponse, self).to_map()
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
            temp_model = ReportVuserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendWangWangRequest(TeaModel):
    def __init__(self, msg=None, title=None, to=None):
        self.msg = msg  # type: str
        self.title = title  # type: str
        self.to = to  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendWangWangRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.title is not None:
            result['Title'] = self.title
        if self.to is not None:
            result['To'] = self.to
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('To') is not None:
            self.to = m.get('To')
        return self


class SendWangWangShrinkRequest(TeaModel):
    def __init__(self, msg=None, title=None, to_shrink=None):
        self.msg = msg  # type: str
        self.title = title  # type: str
        self.to_shrink = to_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendWangWangShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.title is not None:
            result['Title'] = self.title
        if self.to_shrink is not None:
            result['To'] = self.to_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('To') is not None:
            self.to_shrink = m.get('To')
        return self


class SendWangWangResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendWangWangResponseBody, self).to_map()
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


class SendWangWangResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendWangWangResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendWangWangResponse, self).to_map()
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
            temp_model = SendWangWangResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetScenarioStatusRequest(TeaModel):
    def __init__(self, node_ip=None, scenario_id=None, status=None, wskey=None):
        self.node_ip = node_ip  # type: str
        self.scenario_id = scenario_id  # type: int
        self.status = status  # type: int
        self.wskey = wskey  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetScenarioStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_ip is not None:
            result['NodeIp'] = self.node_ip
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.status is not None:
            result['Status'] = self.status
        if self.wskey is not None:
            result['Wskey'] = self.wskey
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NodeIp') is not None:
            self.node_ip = m.get('NodeIp')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Wskey') is not None:
            self.wskey = m.get('Wskey')
        return self


class SetScenarioStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetScenarioStatusResponseBody, self).to_map()
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


class SetScenarioStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetScenarioStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetScenarioStatusResponse, self).to_map()
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
            temp_model = SetScenarioStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTaskStatusRequest(TeaModel):
    def __init__(self, status=None, wskey=None):
        self.status = status  # type: str
        self.wskey = wskey  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTaskStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.wskey is not None:
            result['Wskey'] = self.wskey
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Wskey') is not None:
            self.wskey = m.get('Wskey')
        return self


class SetTaskStatusResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTaskStatusResponseBody, self).to_map()
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


class SetTaskStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetTaskStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetTaskStatusResponse, self).to_map()
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
            temp_model = SetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTaskRequest(TeaModel):
    def __init__(self, msg=None, task_id=None, type=None):
        self.msg = msg  # type: str
        self.task_id = task_id  # type: int
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class StopTaskResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTaskResponseBody, self).to_map()
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


class StopTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopTaskResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopTaskResponse, self).to_map()
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
            temp_model = StopTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


