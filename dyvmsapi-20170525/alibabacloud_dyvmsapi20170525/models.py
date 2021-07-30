# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddRtcAccountRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRtcAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class AddRtcAccountResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRtcAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddRtcAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddRtcAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRtcAccountResponse, self).to_map()
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
            temp_model = AddRtcAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVirtualNumberRelationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 corp_name_list=None, number_list=None, route_type=None, phone_num=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.corp_name_list = corp_name_list  # type: str
        self.number_list = number_list  # type: str
        self.route_type = route_type  # type: int
        self.phone_num = phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVirtualNumberRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.corp_name_list is not None:
            result['CorpNameList'] = self.corp_name_list
        if self.number_list is not None:
            result['NumberList'] = self.number_list
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('CorpNameList') is not None:
            self.corp_name_list = m.get('CorpNameList')
        if m.get('NumberList') is not None:
            self.number_list = m.get('NumberList')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        return self


class AddVirtualNumberRelationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVirtualNumberRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddVirtualNumberRelationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddVirtualNumberRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddVirtualNumberRelationResponse, self).to_map()
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
            temp_model = AddVirtualNumberRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchRobotSmartCallRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, called_show_number=None,
                 corp_name=None, called_number=None, dialog_id=None, early_media_asr=None, task_name=None, schedule_time=None,
                 schedule_call=None, tts_param=None, tts_param_head=None, is_self_line=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.called_show_number = called_show_number  # type: str
        self.corp_name = corp_name  # type: str
        self.called_number = called_number  # type: str
        self.dialog_id = dialog_id  # type: str
        self.early_media_asr = early_media_asr  # type: bool
        self.task_name = task_name  # type: str
        self.schedule_time = schedule_time  # type: long
        self.schedule_call = schedule_call  # type: bool
        self.tts_param = tts_param  # type: str
        self.tts_param_head = tts_param_head  # type: str
        self.is_self_line = is_self_line  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchRobotSmartCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.schedule_call is not None:
            result['ScheduleCall'] = self.schedule_call
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.tts_param_head is not None:
            result['TtsParamHead'] = self.tts_param_head
        if self.is_self_line is not None:
            result['IsSelfLine'] = self.is_self_line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('ScheduleCall') is not None:
            self.schedule_call = m.get('ScheduleCall')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('TtsParamHead') is not None:
            self.tts_param_head = m.get('TtsParamHead')
        if m.get('IsSelfLine') is not None:
            self.is_self_line = m.get('IsSelfLine')
        return self


class BatchRobotSmartCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, task_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchRobotSmartCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class BatchRobotSmartCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchRobotSmartCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchRobotSmartCallResponse, self).to_map()
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
            temp_model = BatchRobotSmartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindNumberAndVoipIdRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None,
                 voip_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.voip_id = voip_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindNumberAndVoipIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.voip_id is not None:
            result['VoipId'] = self.voip_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VoipId') is not None:
            self.voip_id = m.get('VoipId')
        return self


class BindNumberAndVoipIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindNumberAndVoipIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindNumberAndVoipIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BindNumberAndVoipIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindNumberAndVoipIdResponse, self).to_map()
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
            temp_model = BindNumberAndVoipIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelCallRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, call_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class CancelCallResponseBody(TeaModel):
    def __init__(self, status=None, code=None, message=None, request_id=None):
        self.status = status  # type: bool
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelCallResponse, self).to_map()
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
            temp_model = CancelCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelOrderRobotTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOrderRobotTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelOrderRobotTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelOrderRobotTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelOrderRobotTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelOrderRobotTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelOrderRobotTaskResponse, self).to_map()
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
            temp_model = CancelOrderRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRobotTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRobotTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelRobotTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelRobotTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelRobotTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CancelRobotTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelRobotTaskResponse, self).to_map()
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
            temp_model = CancelRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClickToDialRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, caller_show_number=None,
                 caller_number=None, called_show_number=None, called_number=None, record_flag=None, asr_flag=None,
                 session_timeout=None, asr_model_id=None, out_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.caller_show_number = caller_show_number  # type: str
        self.caller_number = caller_number  # type: str
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.record_flag = record_flag  # type: bool
        self.asr_flag = asr_flag  # type: bool
        self.session_timeout = session_timeout  # type: int
        self.asr_model_id = asr_model_id  # type: str
        self.out_id = out_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClickToDialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.caller_show_number is not None:
            result['CallerShowNumber'] = self.caller_show_number
        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag
        if self.asr_flag is not None:
            result['AsrFlag'] = self.asr_flag
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CallerShowNumber') is not None:
            self.caller_show_number = m.get('CallerShowNumber')
        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')
        if m.get('AsrFlag') is not None:
            self.asr_flag = m.get('AsrFlag')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        return self


class ClickToDialResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, call_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClickToDialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class ClickToDialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ClickToDialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClickToDialResponse, self).to_map()
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
            temp_model = ClickToDialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseSipAccountRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, partner_id=None,
                 sip_account_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.partner_id = partner_id  # type: long
        self.sip_account_id = sip_account_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseSipAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.sip_account_id is not None:
            result['SipAccountID'] = self.sip_account_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('SipAccountID') is not None:
            self.sip_account_id = m.get('SipAccountID')
        return self


class CloseSipAccountResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseSipAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CloseSipAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CloseSipAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseSipAccountResponse, self).to_map()
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
            temp_model = CloseSipAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCallTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_name=None,
                 biz_type=None, template_code=None, template_name=None, resource_type=None, resource=None, data_type=None,
                 data=None, fire_time=None, stop_time=None, schedule_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_name = task_name  # type: str
        self.biz_type = biz_type  # type: str
        self.template_code = template_code  # type: str
        self.template_name = template_name  # type: str
        self.resource_type = resource_type  # type: str
        self.resource = resource  # type: str
        self.data_type = data_type  # type: str
        self.data = data  # type: str
        self.fire_time = fire_time  # type: str
        self.stop_time = stop_time  # type: str
        self.schedule_type = schedule_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCallTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.data is not None:
            result['Data'] = self.data
        if self.fire_time is not None:
            result['FireTime'] = self.fire_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        return self


class CreateCallTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCallTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCallTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateCallTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCallTaskResponse, self).to_map()
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
            temp_model = CreateCallTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRobotTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_name=None,
                 dialog_id=None, corp_name=None, caller=None, number_status_ident=None, retry_type=None,
                 recall_state_codes=None, recall_times=None, recall_interval=None, is_self_line=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_name = task_name  # type: str
        self.dialog_id = dialog_id  # type: long
        self.corp_name = corp_name  # type: str
        self.caller = caller  # type: str
        self.number_status_ident = number_status_ident  # type: bool
        self.retry_type = retry_type  # type: int
        self.recall_state_codes = recall_state_codes  # type: str
        self.recall_times = recall_times  # type: int
        self.recall_interval = recall_interval  # type: int
        self.is_self_line = is_self_line  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRobotTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.number_status_ident is not None:
            result['NumberStatusIdent'] = self.number_status_ident
        if self.retry_type is not None:
            result['RetryType'] = self.retry_type
        if self.recall_state_codes is not None:
            result['RecallStateCodes'] = self.recall_state_codes
        if self.recall_times is not None:
            result['RecallTimes'] = self.recall_times
        if self.recall_interval is not None:
            result['RecallInterval'] = self.recall_interval
        if self.is_self_line is not None:
            result['IsSelfLine'] = self.is_self_line
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('NumberStatusIdent') is not None:
            self.number_status_ident = m.get('NumberStatusIdent')
        if m.get('RetryType') is not None:
            self.retry_type = m.get('RetryType')
        if m.get('RecallStateCodes') is not None:
            self.recall_state_codes = m.get('RecallStateCodes')
        if m.get('RecallTimes') is not None:
            self.recall_times = m.get('RecallTimes')
        if m.get('RecallInterval') is not None:
            self.recall_interval = m.get('RecallInterval')
        if m.get('IsSelfLine') is not None:
            self.is_self_line = m.get('IsSelfLine')
        return self


class CreateRobotTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRobotTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRobotTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRobotTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRobotTaskResponse, self).to_map()
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
            temp_model = CreateRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSipAccountRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, partner_id=None,
                 business_key=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.partner_id = partner_id  # type: long
        self.business_key = business_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSipAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.partner_id is not None:
            result['PartnerId'] = self.partner_id
        if self.business_key is not None:
            result['BusinessKey'] = self.business_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PartnerId') is not None:
            self.partner_id = m.get('PartnerId')
        if m.get('BusinessKey') is not None:
            self.business_key = m.get('BusinessKey')
        return self


class CreateSipAccountResponseBodyData(TeaModel):
    def __init__(self, sip_account_id=None, voip_name=None, voip_password=None):
        self.sip_account_id = sip_account_id  # type: str
        self.voip_name = voip_name  # type: str
        self.voip_password = voip_password  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSipAccountResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sip_account_id is not None:
            result['SipAccountID'] = self.sip_account_id
        if self.voip_name is not None:
            result['VoipName'] = self.voip_name
        if self.voip_password is not None:
            result['VoipPassword'] = self.voip_password
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SipAccountID') is not None:
            self.sip_account_id = m.get('SipAccountID')
        if m.get('VoipName') is not None:
            self.voip_name = m.get('VoipName')
        if m.get('VoipPassword') is not None:
            self.voip_password = m.get('VoipPassword')
        return self


class CreateSipAccountResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: CreateSipAccountResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateSipAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = CreateSipAccountResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class CreateSipAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateSipAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSipAccountResponse, self).to_map()
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
            temp_model = CreateSipAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRobotTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRobotTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteRobotTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRobotTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRobotTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteRobotTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRobotTaskResponse, self).to_map()
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
            temp_model = DeleteRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRecordDataRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 account_type=None, account_id=None, acid=None, sec_level=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.account_type = account_type  # type: str
        self.account_id = account_id  # type: str
        self.acid = acid  # type: str
        self.sec_level = sec_level  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.sec_level is not None:
            result['SecLevel'] = self.sec_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('SecLevel') is not None:
            self.sec_level = m.get('SecLevel')
        return self


class DescribeRecordDataResponseBody(TeaModel):
    def __init__(self, oss_link=None, request_id=None, agent_id=None, acid=None, code=None, message=None):
        self.oss_link = oss_link  # type: str
        self.request_id = request_id  # type: str
        self.agent_id = agent_id  # type: str
        self.acid = acid  # type: str
        self.code = code  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRecordDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_link is not None:
            result['OssLink'] = self.oss_link
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.acid is not None:
            result['Acid'] = self.acid
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssLink') is not None:
            self.oss_link = m.get('OssLink')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('Acid') is not None:
            self.acid = m.get('Acid')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DescribeRecordDataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRecordDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRecordDataResponse, self).to_map()
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
            temp_model = DescribeRecordDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoRtcNumberAuthRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoRtcNumberAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class DoRtcNumberAuthResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoRtcNumberAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DoRtcNumberAuthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DoRtcNumberAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoRtcNumberAuthResponse, self).to_map()
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
            temp_model = DoRtcNumberAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DoubleCallSeatRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, caller_show_number=None,
                 caller_number=None, called_show_number=None, called_number=None, record_flag=None, asr_flag=None,
                 session_timeout=None, asr_model_id=None, out_id=None, call_type=None, record_point=None, voice_code=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.caller_show_number = caller_show_number  # type: str
        self.caller_number = caller_number  # type: str
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.record_flag = record_flag  # type: bool
        self.asr_flag = asr_flag  # type: bool
        self.session_timeout = session_timeout  # type: int
        self.asr_model_id = asr_model_id  # type: str
        self.out_id = out_id  # type: str
        self.call_type = call_type  # type: str
        self.record_point = record_point  # type: int
        self.voice_code = voice_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoubleCallSeatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.caller_show_number is not None:
            result['CallerShowNumber'] = self.caller_show_number
        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag
        if self.asr_flag is not None:
            result['AsrFlag'] = self.asr_flag
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.record_point is not None:
            result['RecordPoint'] = self.record_point
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CallerShowNumber') is not None:
            self.caller_show_number = m.get('CallerShowNumber')
        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')
        if m.get('AsrFlag') is not None:
            self.asr_flag = m.get('AsrFlag')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('RecordPoint') is not None:
            self.record_point = m.get('RecordPoint')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        return self


class DoubleCallSeatResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, call_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DoubleCallSeatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class DoubleCallSeatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DoubleCallSeatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DoubleCallSeatResponse, self).to_map()
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
            temp_model = DoubleCallSeatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteCallTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None,
                 status=None, fire_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long
        self.status = status  # type: str
        self.fire_time = fire_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteCallTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.status is not None:
            result['Status'] = self.status
        if self.fire_time is not None:
            result['FireTime'] = self.fire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')
        return self


class ExecuteCallTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ExecuteCallTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ExecuteCallTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ExecuteCallTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ExecuteCallTaskResponse, self).to_map()
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
            temp_model = ExecuteCallTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotlineQualificationByOrderRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, order_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineQualificationByOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetHotlineQualificationByOrderResponseBodyData(TeaModel):
    def __init__(self, status=None, qualification_id=None, order_id=None):
        self.status = status  # type: str
        self.qualification_id = qualification_id  # type: str
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHotlineQualificationByOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class GetHotlineQualificationByOrderResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: GetHotlineQualificationByOrderResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetHotlineQualificationByOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetHotlineQualificationByOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetHotlineQualificationByOrderResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHotlineQualificationByOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHotlineQualificationByOrderResponse, self).to_map()
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
            temp_model = GetHotlineQualificationByOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRtcTokenRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, user_id=None,
                 device_id=None, is_custom_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.user_id = user_id  # type: str
        self.device_id = device_id  # type: str
        self.is_custom_account = is_custom_account  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRtcTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.is_custom_account is not None:
            result['IsCustomAccount'] = self.is_custom_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IsCustomAccount') is not None:
            self.is_custom_account = m.get('IsCustomAccount')
        return self


class GetRtcTokenResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRtcTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRtcTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRtcTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRtcTokenResponse, self).to_map()
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
            temp_model = GetRtcTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, token_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.token_type = token_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.token_type is not None:
            result['TokenType'] = self.token_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, code=None, message=None, token=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.token = token  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.token is not None:
            result['Token'] = self.token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTokenResponse, self).to_map()
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
            temp_model = GetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IvrCallRequestMenuKeyMap(TeaModel):
    def __init__(self, key=None, tts_params=None, code=None):
        self.key = key  # type: str
        self.tts_params = tts_params  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IvrCallRequestMenuKeyMap, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.tts_params is not None:
            result['TtsParams'] = self.tts_params
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('TtsParams') is not None:
            self.tts_params = m.get('TtsParams')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class IvrCallRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, called_show_number=None,
                 called_number=None, start_code=None, start_tts_params=None, play_times=None, bye_code=None, bye_tts_params=None,
                 timeout=None, out_id=None, menu_key_map=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.start_code = start_code  # type: str
        self.start_tts_params = start_tts_params  # type: str
        self.play_times = play_times  # type: long
        self.bye_code = bye_code  # type: str
        self.bye_tts_params = bye_tts_params  # type: str
        self.timeout = timeout  # type: int
        self.out_id = out_id  # type: str
        self.menu_key_map = menu_key_map  # type: list[IvrCallRequestMenuKeyMap]

    def validate(self):
        if self.menu_key_map:
            for k in self.menu_key_map:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(IvrCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.start_code is not None:
            result['StartCode'] = self.start_code
        if self.start_tts_params is not None:
            result['StartTtsParams'] = self.start_tts_params
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.bye_code is not None:
            result['ByeCode'] = self.bye_code
        if self.bye_tts_params is not None:
            result['ByeTtsParams'] = self.bye_tts_params
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.out_id is not None:
            result['OutId'] = self.out_id
        result['MenuKeyMap'] = []
        if self.menu_key_map is not None:
            for k in self.menu_key_map:
                result['MenuKeyMap'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('StartCode') is not None:
            self.start_code = m.get('StartCode')
        if m.get('StartTtsParams') is not None:
            self.start_tts_params = m.get('StartTtsParams')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ByeCode') is not None:
            self.bye_code = m.get('ByeCode')
        if m.get('ByeTtsParams') is not None:
            self.bye_tts_params = m.get('ByeTtsParams')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        self.menu_key_map = []
        if m.get('MenuKeyMap') is not None:
            for k in m.get('MenuKeyMap'):
                temp_model = IvrCallRequestMenuKeyMap()
                self.menu_key_map.append(temp_model.from_map(k))
        return self


class IvrCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, call_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IvrCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class IvrCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: IvrCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(IvrCallResponse, self).to_map()
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
            temp_model = IvrCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, page_number=None,
                 page_size=None, template_name=None, status=None, task_name=None, task_id=None, biz_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.template_name = template_name  # type: str
        self.status = status  # type: str
        self.task_name = task_name  # type: str
        self.task_id = task_id  # type: str
        self.biz_type = biz_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCallTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.status is not None:
            result['Status'] = self.status
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        return self


class ListCallTaskResponseBodyData(TeaModel):
    def __init__(self, status=None, data=None, data_type=None, task_name=None, completed_count=None,
                 total_count=None, template_name=None, stop_time=None, biz_type=None, resource=None, template_code=None,
                 fire_time=None, complete_time=None, completed_rate=None, id=None):
        self.status = status  # type: str
        self.data = data  # type: str
        self.data_type = data_type  # type: str
        self.task_name = task_name  # type: str
        self.completed_count = completed_count  # type: long
        self.total_count = total_count  # type: long
        self.template_name = template_name  # type: str
        self.stop_time = stop_time  # type: str
        self.biz_type = biz_type  # type: str
        self.resource = resource  # type: str
        self.template_code = template_code  # type: str
        self.fire_time = fire_time  # type: str
        self.complete_time = complete_time  # type: str
        self.completed_rate = completed_rate  # type: int
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCallTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.data is not None:
            result['Data'] = self.data
        if self.data_type is not None:
            result['DataType'] = self.data_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.completed_count is not None:
            result['CompletedCount'] = self.completed_count
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.resource is not None:
            result['Resource'] = self.resource
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.fire_time is not None:
            result['FireTime'] = self.fire_time
        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time
        if self.completed_rate is not None:
            result['CompletedRate'] = self.completed_rate
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('CompletedCount') is not None:
            self.completed_count = m.get('CompletedCount')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('FireTime') is not None:
            self.fire_time = m.get('FireTime')
        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')
        if m.get('CompletedRate') is not None:
            self.completed_rate = m.get('CompletedRate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListCallTaskResponseBody(TeaModel):
    def __init__(self, code=None, page_size=None, page_number=None, request_id=None, total=None, data=None):
        self.code = code  # type: str
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long
        self.request_id = request_id  # type: str
        self.total = total  # type: long
        self.data = data  # type: list[ListCallTaskResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCallTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCallTaskResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListCallTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCallTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCallTaskResponse, self).to_map()
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
            temp_model = ListCallTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallTaskDetailRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None,
                 called_num=None, status=None, page_number=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long
        self.called_num = called_num  # type: str
        self.status = status  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCallTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.status is not None:
            result['Status'] = self.status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCallTaskDetailResponseBodyData(TeaModel):
    def __init__(self, status=None, duration=None, called_num=None, caller=None, id=None):
        self.status = status  # type: str
        self.duration = duration  # type: long
        self.called_num = called_num  # type: str
        self.caller = caller  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCallTaskDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListCallTaskDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, total_page=None, page_size=None, page_number=None, total=None,
                 data=None):
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.total_page = total_page  # type: long
        self.page_size = page_size  # type: long
        self.page_number = page_number  # type: long
        self.total = total  # type: long
        self.data = data  # type: list[ListCallTaskDetailResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCallTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.total is not None:
            result['Total'] = self.total
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCallTaskDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListCallTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListCallTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCallTaskDetailResponse, self).to_map()
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
            temp_model = ListCallTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineTransferNumberRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, qualification_id=None,
                 page_no=None, page_size=None, hotline_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.hotline_number = hotline_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineTransferNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        return self


class ListHotlineTransferNumberResponseBodyDataValues(TeaModel):
    def __init__(self, phone_number=None, number_owner_name=None, qualification_id=None, hotline_number=None,
                 identity_card=None, res_unique_code=None):
        self.phone_number = phone_number  # type: str
        self.number_owner_name = number_owner_name  # type: str
        self.qualification_id = qualification_id  # type: str
        self.hotline_number = hotline_number  # type: str
        self.identity_card = identity_card  # type: str
        self.res_unique_code = res_unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineTransferNumberResponseBodyDataValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.number_owner_name is not None:
            result['NumberOwnerName'] = self.number_owner_name
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        if self.identity_card is not None:
            result['IdentityCard'] = self.identity_card
        if self.res_unique_code is not None:
            result['ResUniqueCode'] = self.res_unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('NumberOwnerName') is not None:
            self.number_owner_name = m.get('NumberOwnerName')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        if m.get('IdentityCard') is not None:
            self.identity_card = m.get('IdentityCard')
        if m.get('ResUniqueCode') is not None:
            self.res_unique_code = m.get('ResUniqueCode')
        return self


class ListHotlineTransferNumberResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total=None, values=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long
        self.values = values  # type: list[ListHotlineTransferNumberResponseBodyDataValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotlineTransferNumberResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListHotlineTransferNumberResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListHotlineTransferNumberResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: ListHotlineTransferNumberResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListHotlineTransferNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListHotlineTransferNumberResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListHotlineTransferNumberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHotlineTransferNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotlineTransferNumberResponse, self).to_map()
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
            temp_model = ListHotlineTransferNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotlineTransferRegisterFileRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, qualification_id=None,
                 page_no=None, page_size=None, hotline_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.hotline_number = hotline_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineTransferRegisterFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        return self


class ListHotlineTransferRegisterFileResponseBodyDataValues(TeaModel):
    def __init__(self, mng_op_mail=None, mng_op_name=None, corp_name=None, agree=None, mng_op_mobile=None,
                 mng_op_identity_card=None, hotline_number=None, qualification_id=None, res_unique_code=None):
        self.mng_op_mail = mng_op_mail  # type: str
        self.mng_op_name = mng_op_name  # type: str
        self.corp_name = corp_name  # type: str
        self.agree = agree  # type: str
        self.mng_op_mobile = mng_op_mobile  # type: str
        self.mng_op_identity_card = mng_op_identity_card  # type: str
        self.hotline_number = hotline_number  # type: str
        self.qualification_id = qualification_id  # type: str
        self.res_unique_code = res_unique_code  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHotlineTransferRegisterFileResponseBodyDataValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mng_op_mail is not None:
            result['MngOpMail'] = self.mng_op_mail
        if self.mng_op_name is not None:
            result['MngOpName'] = self.mng_op_name
        if self.corp_name is not None:
            result['CorpName'] = self.corp_name
        if self.agree is not None:
            result['Agree'] = self.agree
        if self.mng_op_mobile is not None:
            result['MngOpMobile'] = self.mng_op_mobile
        if self.mng_op_identity_card is not None:
            result['MngOpIdentityCard'] = self.mng_op_identity_card
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.res_unique_code is not None:
            result['ResUniqueCode'] = self.res_unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MngOpMail') is not None:
            self.mng_op_mail = m.get('MngOpMail')
        if m.get('MngOpName') is not None:
            self.mng_op_name = m.get('MngOpName')
        if m.get('CorpName') is not None:
            self.corp_name = m.get('CorpName')
        if m.get('Agree') is not None:
            self.agree = m.get('Agree')
        if m.get('MngOpMobile') is not None:
            self.mng_op_mobile = m.get('MngOpMobile')
        if m.get('MngOpIdentityCard') is not None:
            self.mng_op_identity_card = m.get('MngOpIdentityCard')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResUniqueCode') is not None:
            self.res_unique_code = m.get('ResUniqueCode')
        return self


class ListHotlineTransferRegisterFileResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total=None, values=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: long
        self.values = values  # type: list[ListHotlineTransferRegisterFileResponseBodyDataValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHotlineTransferRegisterFileResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = ListHotlineTransferRegisterFileResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class ListHotlineTransferRegisterFileResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: ListHotlineTransferRegisterFileResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListHotlineTransferRegisterFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListHotlineTransferRegisterFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListHotlineTransferRegisterFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHotlineTransferRegisterFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHotlineTransferRegisterFileResponse, self).to_map()
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
            temp_model = ListHotlineTransferRegisterFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOrderedNumbersRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrderedNumbersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        return self


class ListOrderedNumbersResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, numbers=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.numbers = numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOrderedNumbersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.numbers is not None:
            result['Numbers'] = self.numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Numbers') is not None:
            self.numbers = m.get('Numbers')
        return self


class ListOrderedNumbersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOrderedNumbersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOrderedNumbersResponse, self).to_map()
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
            temp_model = ListOrderedNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOutboundStrategiesRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 bu_id=None, keyword=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.bu_id = bu_id  # type: long
        self.keyword = keyword  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOutboundStrategiesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListOutboundStrategiesResponseBodyOutboundStrategies(TeaModel):
    def __init__(self, status=None, success_rate=None, process=None, gmt_modified_str=None, outbound_num=None,
                 modifier_id=None, scene_name=None, creator_id=None, robot_name=None, modifier_name=None,
                 resource_allocation=None, ext_attr=None, num_type=None, bu_id=None, robot_id=None, creator_name=None,
                 department_id=None, robot_type=None, rule_code=None, name=None, gmt_create_str=None, id=None):
        self.status = status  # type: int
        self.success_rate = success_rate  # type: int
        self.process = process  # type: int
        self.gmt_modified_str = gmt_modified_str  # type: str
        self.outbound_num = outbound_num  # type: str
        self.modifier_id = modifier_id  # type: long
        self.scene_name = scene_name  # type: str
        self.creator_id = creator_id  # type: long
        self.robot_name = robot_name  # type: str
        self.modifier_name = modifier_name  # type: str
        self.resource_allocation = resource_allocation  # type: int
        self.ext_attr = ext_attr  # type: str
        self.num_type = num_type  # type: int
        self.bu_id = bu_id  # type: long
        self.robot_id = robot_id  # type: str
        self.creator_name = creator_name  # type: str
        self.department_id = department_id  # type: long
        self.robot_type = robot_type  # type: int
        self.rule_code = rule_code  # type: long
        self.name = name  # type: str
        self.gmt_create_str = gmt_create_str  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOutboundStrategiesResponseBodyOutboundStrategies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        if self.process is not None:
            result['Process'] = self.process
        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str
        if self.outbound_num is not None:
            result['OutboundNum'] = self.outbound_num
        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id
        if self.robot_name is not None:
            result['RobotName'] = self.robot_name
        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name
        if self.resource_allocation is not None:
            result['ResourceAllocation'] = self.resource_allocation
        if self.ext_attr is not None:
            result['ExtAttr'] = self.ext_attr
        if self.num_type is not None:
            result['NumType'] = self.num_type
        if self.bu_id is not None:
            result['BuId'] = self.bu_id
        if self.robot_id is not None:
            result['RobotId'] = self.robot_id
        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id
        if self.robot_type is not None:
            result['RobotType'] = self.robot_type
        if self.rule_code is not None:
            result['RuleCode'] = self.rule_code
        if self.name is not None:
            result['name'] = self.name
        if self.gmt_create_str is not None:
            result['GmtCreateStr'] = self.gmt_create_str
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')
        if m.get('OutboundNum') is not None:
            self.outbound_num = m.get('OutboundNum')
        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')
        if m.get('RobotName') is not None:
            self.robot_name = m.get('RobotName')
        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')
        if m.get('ResourceAllocation') is not None:
            self.resource_allocation = m.get('ResourceAllocation')
        if m.get('ExtAttr') is not None:
            self.ext_attr = m.get('ExtAttr')
        if m.get('NumType') is not None:
            self.num_type = m.get('NumType')
        if m.get('BuId') is not None:
            self.bu_id = m.get('BuId')
        if m.get('RobotId') is not None:
            self.robot_id = m.get('RobotId')
        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')
        if m.get('RobotType') is not None:
            self.robot_type = m.get('RobotType')
        if m.get('RuleCode') is not None:
            self.rule_code = m.get('RuleCode')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('GmtCreateStr') is not None:
            self.gmt_create_str = m.get('GmtCreateStr')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListOutboundStrategiesResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, outbound_strategies=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.outbound_strategies = outbound_strategies  # type: list[ListOutboundStrategiesResponseBodyOutboundStrategies]

    def validate(self):
        if self.outbound_strategies:
            for k in self.outbound_strategies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOutboundStrategiesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OutboundStrategies'] = []
        if self.outbound_strategies is not None:
            for k in self.outbound_strategies:
                result['OutboundStrategies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.outbound_strategies = []
        if m.get('OutboundStrategies') is not None:
            for k in m.get('OutboundStrategies'):
                temp_model = ListOutboundStrategiesResponseBodyOutboundStrategies()
                self.outbound_strategies.append(temp_model.from_map(k))
        return self


class ListOutboundStrategiesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListOutboundStrategiesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOutboundStrategiesResponse, self).to_map()
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
            temp_model = ListOutboundStrategiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRobotTaskCallsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, page_no=None,
                 page_size=None, task_id=None, duration_from=None, duration_to=None, dialog_count_from=None,
                 dialog_count_to=None, hangup_direction=None, call_result=None, called=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.task_id = task_id  # type: str
        self.duration_from = duration_from  # type: str
        self.duration_to = duration_to  # type: str
        self.dialog_count_from = dialog_count_from  # type: str
        self.dialog_count_to = dialog_count_to  # type: str
        self.hangup_direction = hangup_direction  # type: str
        self.call_result = call_result  # type: str
        self.called = called  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRobotTaskCallsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.duration_from is not None:
            result['DurationFrom'] = self.duration_from
        if self.duration_to is not None:
            result['DurationTo'] = self.duration_to
        if self.dialog_count_from is not None:
            result['DialogCountFrom'] = self.dialog_count_from
        if self.dialog_count_to is not None:
            result['DialogCountTo'] = self.dialog_count_to
        if self.hangup_direction is not None:
            result['HangupDirection'] = self.hangup_direction
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.called is not None:
            result['Called'] = self.called
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('DurationFrom') is not None:
            self.duration_from = m.get('DurationFrom')
        if m.get('DurationTo') is not None:
            self.duration_to = m.get('DurationTo')
        if m.get('DialogCountFrom') is not None:
            self.dialog_count_from = m.get('DialogCountFrom')
        if m.get('DialogCountTo') is not None:
            self.dialog_count_to = m.get('DialogCountTo')
        if m.get('HangupDirection') is not None:
            self.hangup_direction = m.get('HangupDirection')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Called') is not None:
            self.called = m.get('Called')
        return self


class ListRobotTaskCallsResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, page_no=None, code=None, message=None, page_size=None,
                 total_count=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str
        self.page_no = page_no  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRobotTaskCallsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRobotTaskCallsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListRobotTaskCallsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRobotTaskCallsResponse, self).to_map()
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
            temp_model = ListRobotTaskCallsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallDetailByCallIdRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, call_id=None,
                 prod_id=None, query_date=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.call_id = call_id  # type: str
        self.prod_id = prod_id  # type: long
        self.query_date = query_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallDetailByCallIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.prod_id is not None:
            result['ProdId'] = self.prod_id
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('ProdId') is not None:
            self.prod_id = m.get('ProdId')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        return self


class QueryCallDetailByCallIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallDetailByCallIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCallDetailByCallIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCallDetailByCallIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCallDetailByCallIdResponse, self).to_map()
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
            temp_model = QueryCallDetailByCallIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallDetailByTaskIdRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None,
                 query_date=None, callee=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str
        self.query_date = query_date  # type: long
        self.callee = callee  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallDetailByTaskIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        if self.callee is not None:
            result['Callee'] = self.callee
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        return self


class QueryCallDetailByTaskIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallDetailByTaskIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryCallDetailByTaskIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCallDetailByTaskIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCallDetailByTaskIdResponse, self).to_map()
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
            temp_model = QueryCallDetailByTaskIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallInPoolTransferConfigRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallInPoolTransferConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class QueryCallInPoolTransferConfigResponseBodyDataDetails(TeaModel):
    def __init__(self, called=None):
        self.called = called  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallInPoolTransferConfigResponseBodyDataDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called is not None:
            result['Called'] = self.called
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Called') is not None:
            self.called = m.get('Called')
        return self


class QueryCallInPoolTransferConfigResponseBodyData(TeaModel):
    def __init__(self, gmt_create=None, called_route_mode=None, transfer_timeout=None, details=None):
        self.gmt_create = gmt_create  # type: long
        self.called_route_mode = called_route_mode  # type: str
        self.transfer_timeout = transfer_timeout  # type: str
        self.details = details  # type: list[QueryCallInPoolTransferConfigResponseBodyDataDetails]

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCallInPoolTransferConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.called_route_mode is not None:
            result['CalledRouteMode'] = self.called_route_mode
        if self.transfer_timeout is not None:
            result['TransferTimeout'] = self.transfer_timeout
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('CalledRouteMode') is not None:
            self.called_route_mode = m.get('CalledRouteMode')
        if m.get('TransferTimeout') is not None:
            self.transfer_timeout = m.get('TransferTimeout')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = QueryCallInPoolTransferConfigResponseBodyDataDetails()
                self.details.append(temp_model.from_map(k))
        return self


class QueryCallInPoolTransferConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryCallInPoolTransferConfigResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCallInPoolTransferConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryCallInPoolTransferConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCallInPoolTransferConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCallInPoolTransferConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCallInPoolTransferConfigResponse, self).to_map()
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
            temp_model = QueryCallInPoolTransferConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCallInTransferRecordRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None,
                 call_in_caller=None, query_date=None, page_no=None, page_size=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.call_in_caller = call_in_caller  # type: str
        self.query_date = query_date  # type: str
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallInTransferRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.call_in_caller is not None:
            result['CallInCaller'] = self.call_in_caller
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('CallInCaller') is not None:
            self.call_in_caller = m.get('CallInCaller')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryCallInTransferRecordResponseBodyDataValues(TeaModel):
    def __init__(self, call_in_called=None, transfer_called=None, record_url=None, transfer_caller=None,
                 gmt_create=None, call_in_caller=None):
        self.call_in_called = call_in_called  # type: str
        self.transfer_called = transfer_called  # type: str
        self.record_url = record_url  # type: str
        self.transfer_caller = transfer_caller  # type: str
        self.gmt_create = gmt_create  # type: long
        self.call_in_caller = call_in_caller  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCallInTransferRecordResponseBodyDataValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_in_called is not None:
            result['CallInCalled'] = self.call_in_called
        if self.transfer_called is not None:
            result['TransferCalled'] = self.transfer_called
        if self.record_url is not None:
            result['RecordUrl'] = self.record_url
        if self.transfer_caller is not None:
            result['TransferCaller'] = self.transfer_caller
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.call_in_caller is not None:
            result['CallInCaller'] = self.call_in_caller
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallInCalled') is not None:
            self.call_in_called = m.get('CallInCalled')
        if m.get('TransferCalled') is not None:
            self.transfer_called = m.get('TransferCalled')
        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')
        if m.get('TransferCaller') is not None:
            self.transfer_caller = m.get('TransferCaller')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('CallInCaller') is not None:
            self.call_in_caller = m.get('CallInCaller')
        return self


class QueryCallInTransferRecordResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total=None, values=None):
        self.page_no = page_no  # type: long
        self.page_size = page_size  # type: long
        self.total = total  # type: long
        self.values = values  # type: list[QueryCallInTransferRecordResponseBodyDataValues]

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCallInTransferRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['Values'] = []
        if self.values is not None:
            for k in self.values:
                result['Values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.values = []
        if m.get('Values') is not None:
            for k in m.get('Values'):
                temp_model = QueryCallInTransferRecordResponseBodyDataValues()
                self.values.append(temp_model.from_map(k))
        return self


class QueryCallInTransferRecordResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, data=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.data = data  # type: QueryCallInTransferRecordResponseBodyData

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCallInTransferRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = QueryCallInTransferRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class QueryCallInTransferRecordResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryCallInTransferRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCallInTransferRecordResponse, self).to_map()
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
            temp_model = QueryCallInTransferRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotInfoListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, audit_status=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.audit_status = audit_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotInfoListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.audit_status is not None:
            result['AuditStatus'] = self.audit_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('AuditStatus') is not None:
            self.audit_status = m.get('AuditStatus')
        return self


class QueryRobotInfoListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotInfoListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRobotInfoListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRobotInfoListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRobotInfoListResponse, self).to_map()
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
            temp_model = QueryRobotInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskCallDetailRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None,
                 callee=None, query_date=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long
        self.callee = callee  # type: str
        self.query_date = query_date  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskCallDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.callee is not None:
            result['Callee'] = self.callee
        if self.query_date is not None:
            result['QueryDate'] = self.query_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')
        if m.get('QueryDate') is not None:
            self.query_date = m.get('QueryDate')
        return self


class QueryRobotTaskCallDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskCallDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRobotTaskCallDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRobotTaskCallDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRobotTaskCallDetailResponse, self).to_map()
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
            temp_model = QueryRobotTaskCallDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskCallListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, page_no=None,
                 page_size=None, task_id=None, duration_from=None, duration_to=None, dialog_count_from=None,
                 dialog_count_to=None, hangup_direction=None, call_result=None, called=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.task_id = task_id  # type: str
        self.duration_from = duration_from  # type: str
        self.duration_to = duration_to  # type: str
        self.dialog_count_from = dialog_count_from  # type: str
        self.dialog_count_to = dialog_count_to  # type: str
        self.hangup_direction = hangup_direction  # type: str
        self.call_result = call_result  # type: str
        self.called = called  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskCallListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.duration_from is not None:
            result['DurationFrom'] = self.duration_from
        if self.duration_to is not None:
            result['DurationTo'] = self.duration_to
        if self.dialog_count_from is not None:
            result['DialogCountFrom'] = self.dialog_count_from
        if self.dialog_count_to is not None:
            result['DialogCountTo'] = self.dialog_count_to
        if self.hangup_direction is not None:
            result['HangupDirection'] = self.hangup_direction
        if self.call_result is not None:
            result['CallResult'] = self.call_result
        if self.called is not None:
            result['Called'] = self.called
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('DurationFrom') is not None:
            self.duration_from = m.get('DurationFrom')
        if m.get('DurationTo') is not None:
            self.duration_to = m.get('DurationTo')
        if m.get('DialogCountFrom') is not None:
            self.dialog_count_from = m.get('DialogCountFrom')
        if m.get('DialogCountTo') is not None:
            self.dialog_count_to = m.get('DialogCountTo')
        if m.get('HangupDirection') is not None:
            self.hangup_direction = m.get('HangupDirection')
        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')
        if m.get('Called') is not None:
            self.called = m.get('Called')
        return self


class QueryRobotTaskCallListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskCallListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRobotTaskCallListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRobotTaskCallListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRobotTaskCallListResponse, self).to_map()
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
            temp_model = QueryRobotTaskCallListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskDetailRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class QueryRobotTaskDetailResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRobotTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRobotTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRobotTaskDetailResponse, self).to_map()
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
            temp_model = QueryRobotTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotTaskListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_name=None,
                 status=None, time=None, page_size=None, page_no=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_name = task_name  # type: str
        self.status = status  # type: str
        self.time = time  # type: str
        self.page_size = page_size  # type: int
        self.page_no = page_no  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.status is not None:
            result['Status'] = self.status
        if self.time is not None:
            result['Time'] = self.time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        return self


class QueryRobotTaskListResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None, page_no=None, code=None, message=None, page_size=None,
                 total_count=None):
        self.data = data  # type: str
        self.request_id = request_id  # type: str
        self.page_no = page_no  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.page_size = page_size  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotTaskListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryRobotTaskListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRobotTaskListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRobotTaskListResponse, self).to_map()
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
            temp_model = QueryRobotTaskListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRobotv2AllListRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotv2AllListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryRobotv2AllListResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRobotv2AllListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRobotv2AllListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRobotv2AllListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRobotv2AllListResponse, self).to_map()
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
            temp_model = QueryRobotv2AllListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRtcNumberAuthStatusRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRtcNumberAuthStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class QueryRtcNumberAuthStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRtcNumberAuthStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRtcNumberAuthStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryRtcNumberAuthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRtcNumberAuthStatusResponse, self).to_map()
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
            temp_model = QueryRtcNumberAuthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVirtualNumberRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 page_no=None, page_size=None, route_type=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.route_type = route_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVirtualNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        return self


class QueryVirtualNumberResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVirtualNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVirtualNumberResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryVirtualNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVirtualNumberResponse, self).to_map()
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
            temp_model = QueryVirtualNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVirtualNumberRelationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 page_no=None, page_size=None, route_type=None, qualification_id=None, region_name_city=None, spec_id=None,
                 related_num=None, phone_num=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.route_type = route_type  # type: int
        self.qualification_id = qualification_id  # type: long
        self.region_name_city = region_name_city  # type: str
        self.spec_id = spec_id  # type: long
        self.related_num = related_num  # type: str
        self.phone_num = phone_num  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVirtualNumberRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.route_type is not None:
            result['RouteType'] = self.route_type
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.region_name_city is not None:
            result['RegionNameCity'] = self.region_name_city
        if self.spec_id is not None:
            result['SpecId'] = self.spec_id
        if self.related_num is not None:
            result['RelatedNum'] = self.related_num
        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('RegionNameCity') is not None:
            self.region_name_city = m.get('RegionNameCity')
        if m.get('SpecId') is not None:
            self.spec_id = m.get('SpecId')
        if m.get('RelatedNum') is not None:
            self.related_num = m.get('RelatedNum')
        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')
        return self


class QueryVirtualNumberRelationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVirtualNumberRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVirtualNumberRelationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryVirtualNumberRelationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVirtualNumberRelationResponse, self).to_map()
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
            temp_model = QueryVirtualNumberRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVoipNumberBindInfosRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None,
                 voip_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.voip_id = voip_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVoipNumberBindInfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.voip_id is not None:
            result['VoipId'] = self.voip_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VoipId') is not None:
            self.voip_id = m.get('VoipId')
        return self


class QueryVoipNumberBindInfosResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVoipNumberBindInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryVoipNumberBindInfosResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryVoipNumberBindInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVoipNumberBindInfosResponse, self).to_map()
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
            temp_model = QueryVoipNumberBindInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportVoipProblemsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, channel_id=None,
                 voip_id=None, title=None, desc=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.channel_id = channel_id  # type: str
        self.voip_id = voip_id  # type: str
        self.title = title  # type: str
        self.desc = desc  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportVoipProblemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.voip_id is not None:
            result['VoipId'] = self.voip_id
        if self.title is not None:
            result['Title'] = self.title
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('VoipId') is not None:
            self.voip_id = m.get('VoipId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class ReportVoipProblemsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportVoipProblemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReportVoipProblemsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReportVoipProblemsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportVoipProblemsResponse, self).to_map()
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
            temp_model = ReportVoipProblemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVerificationRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, verify_type=None,
                 biz_type=None, target=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.verify_type = verify_type  # type: str
        self.biz_type = biz_type  # type: str
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class SendVerificationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVerificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendVerificationResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendVerificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVerificationResponse, self).to_map()
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
            temp_model = SendVerificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetTransferCalleePoolConfigRequestDetails(TeaModel):
    def __init__(self, caller=None, called=None):
        self.caller = caller  # type: str
        self.called = called  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTransferCalleePoolConfigRequestDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.caller is not None:
            result['Caller'] = self.caller
        if self.called is not None:
            result['Called'] = self.called
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Caller') is not None:
            self.caller = m.get('Caller')
        if m.get('Called') is not None:
            self.called = m.get('Called')
        return self


class SetTransferCalleePoolConfigRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None,
                 qualification_id=None, called_route_mode=None, details=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.qualification_id = qualification_id  # type: str
        self.called_route_mode = called_route_mode  # type: str
        self.details = details  # type: list[SetTransferCalleePoolConfigRequestDetails]

    def validate(self):
        if self.details:
            for k in self.details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SetTransferCalleePoolConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.called_route_mode is not None:
            result['CalledRouteMode'] = self.called_route_mode
        result['Details'] = []
        if self.details is not None:
            for k in self.details:
                result['Details'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('CalledRouteMode') is not None:
            self.called_route_mode = m.get('CalledRouteMode')
        self.details = []
        if m.get('Details') is not None:
            for k in m.get('Details'):
                temp_model = SetTransferCalleePoolConfigRequestDetails()
                self.details.append(temp_model.from_map(k))
        return self


class SetTransferCalleePoolConfigResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetTransferCalleePoolConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetTransferCalleePoolConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetTransferCalleePoolConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetTransferCalleePoolConfigResponse, self).to_map()
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
            temp_model = SetTransferCalleePoolConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleCallByTtsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, called_show_number=None,
                 called_number=None, tts_code=None, tts_param=None, play_times=None, volume=None, speed=None, out_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.tts_code = tts_code  # type: str
        self.tts_param = tts_param  # type: str
        self.play_times = play_times  # type: int
        self.volume = volume  # type: int
        self.speed = speed  # type: int
        self.out_id = out_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleCallByTtsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.out_id is not None:
            result['OutId'] = self.out_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        return self


class SingleCallByTtsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, call_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleCallByTtsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class SingleCallByTtsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SingleCallByTtsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SingleCallByTtsResponse, self).to_map()
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
            temp_model = SingleCallByTtsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleCallByVoiceRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, called_show_number=None,
                 called_number=None, voice_code=None, play_times=None, volume=None, speed=None, out_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.voice_code = voice_code  # type: str
        self.play_times = play_times  # type: int
        self.volume = volume  # type: int
        self.speed = speed  # type: int
        self.out_id = out_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleCallByVoiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.out_id is not None:
            result['OutId'] = self.out_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        return self


class SingleCallByVoiceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, call_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleCallByVoiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class SingleCallByVoiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SingleCallByVoiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SingleCallByVoiceResponse, self).to_map()
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
            temp_model = SingleCallByVoiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartCallRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, called_show_number=None,
                 called_number=None, voice_code=None, record_flag=None, volume=None, speed=None, asr_model_id=None,
                 pause_time=None, mute_time=None, action_code_break=None, out_id=None, dynamic_id=None, early_media_asr=None,
                 voice_code_param=None, session_timeout=None, action_code_time_break=None, tts_style=None, tts_volume=None,
                 tts_speed=None, tts_conf=None, asr_base_id=None, stream_asr=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.called_show_number = called_show_number  # type: str
        self.called_number = called_number  # type: str
        self.voice_code = voice_code  # type: str
        self.record_flag = record_flag  # type: bool
        self.volume = volume  # type: int
        self.speed = speed  # type: int
        self.asr_model_id = asr_model_id  # type: str
        self.pause_time = pause_time  # type: int
        self.mute_time = mute_time  # type: int
        self.action_code_break = action_code_break  # type: bool
        self.out_id = out_id  # type: str
        self.dynamic_id = dynamic_id  # type: str
        self.early_media_asr = early_media_asr  # type: bool
        self.voice_code_param = voice_code_param  # type: str
        self.session_timeout = session_timeout  # type: int
        self.action_code_time_break = action_code_time_break  # type: int
        self.tts_style = tts_style  # type: str
        self.tts_volume = tts_volume  # type: int
        self.tts_speed = tts_speed  # type: int
        self.tts_conf = tts_conf  # type: bool
        self.asr_base_id = asr_base_id  # type: str
        self.stream_asr = stream_asr  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmartCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.called_show_number is not None:
            result['CalledShowNumber'] = self.called_show_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.record_flag is not None:
            result['RecordFlag'] = self.record_flag
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.asr_model_id is not None:
            result['AsrModelId'] = self.asr_model_id
        if self.pause_time is not None:
            result['PauseTime'] = self.pause_time
        if self.mute_time is not None:
            result['MuteTime'] = self.mute_time
        if self.action_code_break is not None:
            result['ActionCodeBreak'] = self.action_code_break
        if self.out_id is not None:
            result['OutId'] = self.out_id
        if self.dynamic_id is not None:
            result['DynamicId'] = self.dynamic_id
        if self.early_media_asr is not None:
            result['EarlyMediaAsr'] = self.early_media_asr
        if self.voice_code_param is not None:
            result['VoiceCodeParam'] = self.voice_code_param
        if self.session_timeout is not None:
            result['SessionTimeout'] = self.session_timeout
        if self.action_code_time_break is not None:
            result['ActionCodeTimeBreak'] = self.action_code_time_break
        if self.tts_style is not None:
            result['TtsStyle'] = self.tts_style
        if self.tts_volume is not None:
            result['TtsVolume'] = self.tts_volume
        if self.tts_speed is not None:
            result['TtsSpeed'] = self.tts_speed
        if self.tts_conf is not None:
            result['TtsConf'] = self.tts_conf
        if self.asr_base_id is not None:
            result['AsrBaseId'] = self.asr_base_id
        if self.stream_asr is not None:
            result['StreamAsr'] = self.stream_asr
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CalledShowNumber') is not None:
            self.called_show_number = m.get('CalledShowNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('RecordFlag') is not None:
            self.record_flag = m.get('RecordFlag')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('AsrModelId') is not None:
            self.asr_model_id = m.get('AsrModelId')
        if m.get('PauseTime') is not None:
            self.pause_time = m.get('PauseTime')
        if m.get('MuteTime') is not None:
            self.mute_time = m.get('MuteTime')
        if m.get('ActionCodeBreak') is not None:
            self.action_code_break = m.get('ActionCodeBreak')
        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')
        if m.get('DynamicId') is not None:
            self.dynamic_id = m.get('DynamicId')
        if m.get('EarlyMediaAsr') is not None:
            self.early_media_asr = m.get('EarlyMediaAsr')
        if m.get('VoiceCodeParam') is not None:
            self.voice_code_param = m.get('VoiceCodeParam')
        if m.get('SessionTimeout') is not None:
            self.session_timeout = m.get('SessionTimeout')
        if m.get('ActionCodeTimeBreak') is not None:
            self.action_code_time_break = m.get('ActionCodeTimeBreak')
        if m.get('TtsStyle') is not None:
            self.tts_style = m.get('TtsStyle')
        if m.get('TtsVolume') is not None:
            self.tts_volume = m.get('TtsVolume')
        if m.get('TtsSpeed') is not None:
            self.tts_speed = m.get('TtsSpeed')
        if m.get('TtsConf') is not None:
            self.tts_conf = m.get('TtsConf')
        if m.get('AsrBaseId') is not None:
            self.asr_base_id = m.get('AsrBaseId')
        if m.get('StreamAsr') is not None:
            self.stream_asr = m.get('StreamAsr')
        return self


class SmartCallResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, call_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.call_id = call_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmartCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        return self


class SmartCallResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SmartCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmartCallResponse, self).to_map()
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
            temp_model = SmartCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SmartCallOperateRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, call_id=None,
                 command=None, param=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.call_id = call_id  # type: str
        self.command = command  # type: str
        self.param = param  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmartCallOperateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.command is not None:
            result['Command'] = self.command
        if self.param is not None:
            result['Param'] = self.param
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Param') is not None:
            self.param = m.get('Param')
        return self


class SmartCallOperateResponseBody(TeaModel):
    def __init__(self, status=None, code=None, message=None, request_id=None):
        self.status = status  # type: bool
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SmartCallOperateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SmartCallOperateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SmartCallOperateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SmartCallOperateResponse, self).to_map()
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
            temp_model = SmartCallOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartMicroOutboundRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, prod_code=None,
                 account_type=None, account_id=None, command_code=None, calling_number=None, called_number=None, ext_info=None,
                 app_name=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.prod_code = prod_code  # type: str
        self.account_type = account_type  # type: str
        self.account_id = account_id  # type: str
        self.command_code = command_code  # type: str
        self.calling_number = calling_number  # type: str
        self.called_number = called_number  # type: str
        self.ext_info = ext_info  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMicroOutboundRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code
        if self.account_type is not None:
            result['AccountType'] = self.account_type
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.command_code is not None:
            result['CommandCode'] = self.command_code
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CommandCode') is not None:
            self.command_code = m.get('CommandCode')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class StartMicroOutboundResponseBody(TeaModel):
    def __init__(self, customer_info=None, request_id=None, invoke_cmd_id=None, code=None, invoke_create_time=None,
                 message=None):
        self.customer_info = customer_info  # type: str
        self.request_id = request_id  # type: str
        self.invoke_cmd_id = invoke_cmd_id  # type: str
        self.code = code  # type: str
        self.invoke_create_time = invoke_create_time  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartMicroOutboundResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.customer_info is not None:
            result['CustomerInfo'] = self.customer_info
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.invoke_cmd_id is not None:
            result['InvokeCmdId'] = self.invoke_cmd_id
        if self.code is not None:
            result['Code'] = self.code
        if self.invoke_create_time is not None:
            result['InvokeCreateTime'] = self.invoke_create_time
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomerInfo') is not None:
            self.customer_info = m.get('CustomerInfo')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('InvokeCmdId') is not None:
            self.invoke_cmd_id = m.get('InvokeCmdId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InvokeCreateTime') is not None:
            self.invoke_create_time = m.get('InvokeCreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class StartMicroOutboundResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartMicroOutboundResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartMicroOutboundResponse, self).to_map()
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
            temp_model = StartMicroOutboundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartRobotTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None,
                 schedule_time=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long
        self.schedule_time = schedule_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRobotTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        return self


class StartRobotTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartRobotTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartRobotTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartRobotTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartRobotTaskResponse, self).to_map()
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
            temp_model = StartRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopRobotTaskRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRobotTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class StopRobotTaskResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopRobotTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopRobotTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopRobotTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopRobotTaskResponse, self).to_map()
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
            temp_model = StopRobotTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos(TeaModel):
    def __init__(self, phone_number=None, phone_number_owner_name=None, identity_card=None):
        self.phone_number = phone_number  # type: str
        self.phone_number_owner_name = phone_number_owner_name  # type: str
        self.identity_card = identity_card  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.phone_number_owner_name is not None:
            result['PhoneNumberOwnerName'] = self.phone_number_owner_name
        if self.identity_card is not None:
            result['IdentityCard'] = self.identity_card
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PhoneNumberOwnerName') is not None:
            self.phone_number_owner_name = m.get('PhoneNumberOwnerName')
        if m.get('IdentityCard') is not None:
            self.identity_card = m.get('IdentityCard')
        return self


class SubmitHotlineTransferRegisterRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, qualification_id=None,
                 operator_name=None, operator_mail=None, operator_mail_verify_code=None, operator_mobile=None,
                 operator_mobile_verify_code=None, operator_identity_card=None, agreement=None, hotline_number=None,
                 transfer_phone_number_infos=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.operator_name = operator_name  # type: str
        self.operator_mail = operator_mail  # type: str
        self.operator_mail_verify_code = operator_mail_verify_code  # type: str
        self.operator_mobile = operator_mobile  # type: str
        self.operator_mobile_verify_code = operator_mobile_verify_code  # type: str
        self.operator_identity_card = operator_identity_card  # type: str
        self.agreement = agreement  # type: str
        self.hotline_number = hotline_number  # type: str
        self.transfer_phone_number_infos = transfer_phone_number_infos  # type: list[SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos]

    def validate(self):
        if self.transfer_phone_number_infos:
            for k in self.transfer_phone_number_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubmitHotlineTransferRegisterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name
        if self.operator_mail is not None:
            result['OperatorMail'] = self.operator_mail
        if self.operator_mail_verify_code is not None:
            result['OperatorMailVerifyCode'] = self.operator_mail_verify_code
        if self.operator_mobile is not None:
            result['OperatorMobile'] = self.operator_mobile
        if self.operator_mobile_verify_code is not None:
            result['OperatorMobileVerifyCode'] = self.operator_mobile_verify_code
        if self.operator_identity_card is not None:
            result['OperatorIdentityCard'] = self.operator_identity_card
        if self.agreement is not None:
            result['Agreement'] = self.agreement
        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number
        result['TransferPhoneNumberInfos'] = []
        if self.transfer_phone_number_infos is not None:
            for k in self.transfer_phone_number_infos:
                result['TransferPhoneNumberInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')
        if m.get('OperatorMail') is not None:
            self.operator_mail = m.get('OperatorMail')
        if m.get('OperatorMailVerifyCode') is not None:
            self.operator_mail_verify_code = m.get('OperatorMailVerifyCode')
        if m.get('OperatorMobile') is not None:
            self.operator_mobile = m.get('OperatorMobile')
        if m.get('OperatorMobileVerifyCode') is not None:
            self.operator_mobile_verify_code = m.get('OperatorMobileVerifyCode')
        if m.get('OperatorIdentityCard') is not None:
            self.operator_identity_card = m.get('OperatorIdentityCard')
        if m.get('Agreement') is not None:
            self.agreement = m.get('Agreement')
        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')
        self.transfer_phone_number_infos = []
        if m.get('TransferPhoneNumberInfos') is not None:
            for k in m.get('TransferPhoneNumberInfos'):
                temp_model = SubmitHotlineTransferRegisterRequestTransferPhoneNumberInfos()
                self.transfer_phone_number_infos.append(temp_model.from_map(k))
        return self


class SubmitHotlineTransferRegisterResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitHotlineTransferRegisterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitHotlineTransferRegisterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SubmitHotlineTransferRegisterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitHotlineTransferRegisterResponse, self).to_map()
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
            temp_model = SubmitHotlineTransferRegisterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindNumberAndVoipIdRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None,
                 voip_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str
        self.voip_id = voip_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindNumberAndVoipIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.voip_id is not None:
            result['VoipId'] = self.voip_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('VoipId') is not None:
            self.voip_id = m.get('VoipId')
        return self


class UnbindNumberAndVoipIdResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindNumberAndVoipIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindNumberAndVoipIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnbindNumberAndVoipIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindNumberAndVoipIdResponse, self).to_map()
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
            temp_model = UnbindNumberAndVoipIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UndoRtcNumberAuthRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, phone_number=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.phone_number = phone_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UndoRtcNumberAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        return self


class UndoRtcNumberAuthResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UndoRtcNumberAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UndoRtcNumberAuthResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UndoRtcNumberAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UndoRtcNumberAuthResponse, self).to_map()
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
            temp_model = UndoRtcNumberAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UploadRobotTaskCalledFileRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, id=None,
                 called_number=None, tts_param=None, tts_param_head=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.id = id  # type: long
        self.called_number = called_number  # type: str
        self.tts_param = tts_param  # type: str
        self.tts_param_head = tts_param_head  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRobotTaskCalledFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.id is not None:
            result['Id'] = self.id
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.tts_param_head is not None:
            result['TtsParamHead'] = self.tts_param_head
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('TtsParamHead') is not None:
            self.tts_param_head = m.get('TtsParamHead')
        return self


class UploadRobotTaskCalledFileResponseBody(TeaModel):
    def __init__(self, code=None, message=None, data=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.data = data  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UploadRobotTaskCalledFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UploadRobotTaskCalledFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UploadRobotTaskCalledFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UploadRobotTaskCalledFileResponse, self).to_map()
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
            temp_model = UploadRobotTaskCalledFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoipAddAccountRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, device_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoipAddAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class VoipAddAccountResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoipAddAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoipAddAccountResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VoipAddAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VoipAddAccountResponse, self).to_map()
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
            temp_model = VoipAddAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VoipGetTokenRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, voip_id=None,
                 device_id=None, is_custom_account=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.voip_id = voip_id  # type: str
        self.device_id = device_id  # type: str
        self.is_custom_account = is_custom_account  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoipGetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.voip_id is not None:
            result['VoipId'] = self.voip_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.is_custom_account is not None:
            result['IsCustomAccount'] = self.is_custom_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('VoipId') is not None:
            self.voip_id = m.get('VoipId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('IsCustomAccount') is not None:
            self.is_custom_account = m.get('IsCustomAccount')
        return self


class VoipGetTokenResponseBody(TeaModel):
    def __init__(self, code=None, message=None, module=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.module = module  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VoipGetTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.module is not None:
            result['Module'] = self.module
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Module') is not None:
            self.module = m.get('Module')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VoipGetTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VoipGetTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VoipGetTokenResponse, self).to_map()
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
            temp_model = VoipGetTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


