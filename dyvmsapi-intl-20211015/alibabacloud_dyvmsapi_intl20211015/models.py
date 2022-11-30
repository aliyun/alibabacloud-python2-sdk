# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class BackendCallGroupRequest(TeaModel):
    def __init__(self, called_number=None, caller_id_number=None, country_id=None, owner_id=None, play_times=None,
                 resource_owner_account=None, resource_owner_id=None, send_type=None, speed=None, task_name=None, timing_start=None,
                 tts_code=None, voice_code=None, volume=None):
        self.called_number = called_number  # type: list[str]
        self.caller_id_number = caller_id_number  # type: str
        self.country_id = country_id  # type: str
        self.owner_id = owner_id  # type: long
        self.play_times = play_times  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.send_type = send_type  # type: long
        self.speed = speed  # type: long
        self.task_name = task_name  # type: str
        self.timing_start = timing_start  # type: str
        self.tts_code = tts_code  # type: str
        self.voice_code = voice_code  # type: str
        self.volume = volume  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackendCallGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class BackendCallGroupShrinkRequest(TeaModel):
    def __init__(self, called_number_shrink=None, caller_id_number=None, country_id=None, owner_id=None,
                 play_times=None, resource_owner_account=None, resource_owner_id=None, send_type=None, speed=None,
                 task_name=None, timing_start=None, tts_code=None, voice_code=None, volume=None):
        self.called_number_shrink = called_number_shrink  # type: str
        self.caller_id_number = caller_id_number  # type: str
        self.country_id = country_id  # type: str
        self.owner_id = owner_id  # type: long
        self.play_times = play_times  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.send_type = send_type  # type: long
        self.speed = speed  # type: long
        self.task_name = task_name  # type: str
        self.timing_start = timing_start  # type: str
        self.tts_code = tts_code  # type: str
        self.voice_code = voice_code  # type: str
        self.volume = volume  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackendCallGroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number_shrink is not None:
            result['CalledNumber'] = self.called_number_shrink
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.voice_code is not None:
            result['VoiceCode'] = self.voice_code
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number_shrink = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('VoiceCode') is not None:
            self.voice_code = m.get('VoiceCode')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class BackendCallGroupResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, task_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackendCallGroupResponseBody, self).to_map()
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


class BackendCallGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BackendCallGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BackendCallGroupResponse, self).to_map()
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
            temp_model = BackendCallGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BackendCallSignalRequest(TeaModel):
    def __init__(self, called_number=None, caller_id_number=None, country_id=None, owner_id=None, play_times=None,
                 resource_owner_account=None, resource_owner_id=None, speed=None, tts_code=None, tts_param=None, volume=None):
        self.called_number = called_number  # type: str
        self.caller_id_number = caller_id_number  # type: str
        self.country_id = country_id  # type: str
        self.owner_id = owner_id  # type: long
        self.play_times = play_times  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.speed = speed  # type: long
        self.tts_code = tts_code  # type: str
        self.tts_param = tts_param  # type: str
        self.volume = volume  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackendCallSignalRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.play_times is not None:
            result['PlayTimes'] = self.play_times
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.tts_code is not None:
            result['TtsCode'] = self.tts_code
        if self.tts_param is not None:
            result['TtsParam'] = self.tts_param
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PlayTimes') is not None:
            self.play_times = m.get('PlayTimes')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('TtsCode') is not None:
            self.tts_code = m.get('TtsCode')
        if m.get('TtsParam') is not None:
            self.tts_param = m.get('TtsParam')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class BackendCallSignalResponseBody(TeaModel):
    def __init__(self, call_id=None, code=None, message=None, request_id=None):
        self.call_id = call_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BackendCallSignalResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BackendCallSignalResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BackendCallSignalResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BackendCallSignalResponse, self).to_map()
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
            temp_model = BackendCallSignalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancleGroupCallRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, task_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancleGroupCallRequest, self).to_map()
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


class CancleGroupCallResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None, task_id=None):
        self.code = code  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancleGroupCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancleGroupCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancleGroupCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancleGroupCallResponse, self).to_map()
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
            temp_model = CancleGroupCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApplyNumberRecordRequest(TeaModel):
    def __init__(self, apply_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.apply_id = apply_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplyNumberRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteApplyNumberRecordResponseBody(TeaModel):
    def __init__(self, apply_id=None, code=None, message=None, request_id=None):
        self.apply_id = apply_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApplyNumberRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApplyNumberRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApplyNumberRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApplyNumberRecordResponse, self).to_map()
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
            temp_model = DeleteApplyNumberRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteQualificationRequest(TeaModel):
    def __init__(self, owner_id=None, qualification_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQualificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteQualificationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, qualification_id=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.qualification_id = qualification_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteQualificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteQualificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteQualificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteQualificationResponse, self).to_map()
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
            temp_model = DeleteQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSipTrunkApplyRequest(TeaModel):
    def __init__(self, apply_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.apply_id = apply_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSipTrunkApplyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteSipTrunkApplyResponseBody(TeaModel):
    def __init__(self, apply_id=None, code=None, message=None, request_id=None):
        self.apply_id = apply_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSipTrunkApplyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSipTrunkApplyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSipTrunkApplyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSipTrunkApplyResponse, self).to_map()
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
            temp_model = DeleteSipTrunkApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVoiceFileRequest(TeaModel):
    def __init__(self, file_id=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.file_id = file_id  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVoiceFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DeleteVoiceFileResponseBody(TeaModel):
    def __init__(self, code=None, file_id=None, message=None, request_id=None):
        self.code = code  # type: str
        self.file_id = file_id  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVoiceFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteVoiceFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVoiceFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVoiceFileResponse, self).to_map()
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
            temp_model = DeleteVoiceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVoiceTtsRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None, template_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVoiceTtsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteVoiceTtsResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, template_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVoiceTtsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteVoiceTtsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVoiceTtsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVoiceTtsResponse, self).to_map()
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
            temp_model = DeleteVoiceTtsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadTemplateFileRequest(TeaModel):
    def __init__(self, file_type=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.file_type = file_type  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadTemplateFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class DownloadTemplateFileResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, url=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DownloadTemplateFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DownloadTemplateFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DownloadTemplateFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DownloadTemplateFileResponse, self).to_map()
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
            temp_model = DownloadTemplateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIntlVoiceOpenStatusRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntlVoiceOpenStatusRequest, self).to_map()
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


class GetIntlVoiceOpenStatusResponseBody(TeaModel):
    def __init__(self, code=None, message=None, open_status=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.open_status = open_status  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetIntlVoiceOpenStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.open_status is not None:
            result['OpenStatus'] = self.open_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('OpenStatus') is not None:
            self.open_status = m.get('OpenStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetIntlVoiceOpenStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetIntlVoiceOpenStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetIntlVoiceOpenStatusResponse, self).to_map()
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
            temp_model = GetIntlVoiceOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssInfoForUploadFileRequest(TeaModel):
    def __init__(self, biz_type=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssInfoForUploadFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class GetOssInfoForUploadFileResponseBody(TeaModel):
    def __init__(self, access_key_id=None, expire_time=None, host=None, policy=None, request_id=None, signature=None,
                 start_with=None):
        self.access_key_id = access_key_id  # type: str
        self.expire_time = expire_time  # type: str
        self.host = host  # type: str
        self.policy = policy  # type: str
        self.request_id = request_id  # type: str
        self.signature = signature  # type: str
        self.start_with = start_with  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssInfoForUploadFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host is not None:
            result['Host'] = self.host
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.start_with is not None:
            result['StartWith'] = self.start_with
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('StartWith') is not None:
            self.start_with = m.get('StartWith')
        return self


class GetOssInfoForUploadFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetOssInfoForUploadFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOssInfoForUploadFileResponse, self).to_map()
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
            temp_model = GetOssInfoForUploadFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HomeStartRequest(TeaModel):
    def __init__(self, business_type=None, end_time=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None):
        self.business_type = business_type  # type: long
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HomeStartRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class HomeStartResponseBodyModelList(TeaModel):
    def __init__(self, call_failed=None, call_success=None, call_total=None, date=None, success_rate=None):
        self.call_failed = call_failed  # type: long
        self.call_success = call_success  # type: long
        self.call_total = call_total  # type: long
        self.date = date  # type: str
        self.success_rate = success_rate  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(HomeStartResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_failed is not None:
            result['CallFailed'] = self.call_failed
        if self.call_success is not None:
            result['CallSuccess'] = self.call_success
        if self.call_total is not None:
            result['CallTotal'] = self.call_total
        if self.date is not None:
            result['Date'] = self.date
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallFailed') is not None:
            self.call_failed = m.get('CallFailed')
        if m.get('CallSuccess') is not None:
            self.call_success = m.get('CallSuccess')
        if m.get('CallTotal') is not None:
            self.call_total = m.get('CallTotal')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        return self


class HomeStartResponseBodyModel(TeaModel):
    def __init__(self, cdr_dr_url=None, list=None):
        self.cdr_dr_url = cdr_dr_url  # type: str
        self.list = list  # type: list[HomeStartResponseBodyModelList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(HomeStartResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdr_dr_url is not None:
            result['CdrDrUrl'] = self.cdr_dr_url
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdrDrUrl') is not None:
            self.cdr_dr_url = m.get('CdrDrUrl')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = HomeStartResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        return self


class HomeStartResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, model=None, request_id=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: long
        self.message = message  # type: str
        self.model = model  # type: HomeStartResponseBodyModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(HomeStartResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = HomeStartResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class HomeStartResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: HomeStartResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HomeStartResponse, self).to_map()
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
            temp_model = HomeStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplyNumberRecordRequest(TeaModel):
    def __init__(self, country_id=None, end_time=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, start_time=None, status=None):
        self.country_id = country_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplyNumberRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListApplyNumberRecordResponseBodyList(TeaModel):
    def __init__(self, amount=None, apply_id=None, apply_note=None, audit_note=None, audit_ts=None, batch_index=None,
                 commit_ts=None, country_id=None, inbound_concurrency=None, outbound_concurrency=None, phone_type=None,
                 qualification_id=None, scene=None, status=None, support=None, update_ts=None):
        self.amount = amount  # type: str
        self.apply_id = apply_id  # type: str
        self.apply_note = apply_note  # type: str
        self.audit_note = audit_note  # type: str
        self.audit_ts = audit_ts  # type: str
        self.batch_index = batch_index  # type: long
        self.commit_ts = commit_ts  # type: str
        self.country_id = country_id  # type: str
        self.inbound_concurrency = inbound_concurrency  # type: long
        self.outbound_concurrency = outbound_concurrency  # type: long
        self.phone_type = phone_type  # type: long
        self.qualification_id = qualification_id  # type: str
        self.scene = scene  # type: str
        self.status = status  # type: long
        self.support = support  # type: long
        self.update_ts = update_ts  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApplyNumberRecordResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.apply_note is not None:
            result['ApplyNote'] = self.apply_note
        if self.audit_note is not None:
            result['AuditNote'] = self.audit_note
        if self.audit_ts is not None:
            result['AuditTs'] = self.audit_ts
        if self.batch_index is not None:
            result['BatchIndex'] = self.batch_index
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.inbound_concurrency is not None:
            result['InboundConcurrency'] = self.inbound_concurrency
        if self.outbound_concurrency is not None:
            result['OutboundConcurrency'] = self.outbound_concurrency
        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.status is not None:
            result['Status'] = self.status
        if self.support is not None:
            result['Support'] = self.support
        if self.update_ts is not None:
            result['UpdateTs'] = self.update_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('ApplyNote') is not None:
            self.apply_note = m.get('ApplyNote')
        if m.get('AuditNote') is not None:
            self.audit_note = m.get('AuditNote')
        if m.get('AuditTs') is not None:
            self.audit_ts = m.get('AuditTs')
        if m.get('BatchIndex') is not None:
            self.batch_index = m.get('BatchIndex')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('InboundConcurrency') is not None:
            self.inbound_concurrency = m.get('InboundConcurrency')
        if m.get('OutboundConcurrency') is not None:
            self.outbound_concurrency = m.get('OutboundConcurrency')
        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        if m.get('UpdateTs') is not None:
            self.update_ts = m.get('UpdateTs')
        return self


class ListApplyNumberRecordResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListApplyNumberRecordResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApplyNumberRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListApplyNumberRecordResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListApplyNumberRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApplyNumberRecordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApplyNumberRecordResponse, self).to_map()
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
            temp_model = ListApplyNumberRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNumberRequest(TeaModel):
    def __init__(self, apply_id=None, country_id=None, number=None, number_name=None, owner_id=None,
                 page_number=None, page_size=None, phone_type=None, resource_owner_account=None, resource_owner_id=None):
        self.apply_id = apply_id  # type: str
        self.country_id = country_id  # type: str
        self.number = number  # type: str
        self.number_name = number_name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.phone_type = phone_type  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.number is not None:
            result['Number'] = self.number
        if self.number_name is not None:
            result['NumberName'] = self.number_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberName') is not None:
            self.number_name = m.get('NumberName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class ListNumberResponseBodyList(TeaModel):
    def __init__(self, apply_id=None, country_id=None, disable_ts=None, inbound_concurrency=None, number=None,
                 number_name=None, outbound_concurrency=None, phone_type=None, qualification_id=None, resource_id=None,
                 status=None, supplier_id=None, support=None, update_ts=None):
        self.apply_id = apply_id  # type: str
        self.country_id = country_id  # type: str
        self.disable_ts = disable_ts  # type: str
        self.inbound_concurrency = inbound_concurrency  # type: long
        self.number = number  # type: str
        self.number_name = number_name  # type: str
        self.outbound_concurrency = outbound_concurrency  # type: long
        self.phone_type = phone_type  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_id = resource_id  # type: str
        self.status = status  # type: long
        self.supplier_id = supplier_id  # type: str
        self.support = support  # type: long
        self.update_ts = update_ts  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListNumberResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.disable_ts is not None:
            result['DisableTs'] = self.disable_ts
        if self.inbound_concurrency is not None:
            result['InboundConcurrency'] = self.inbound_concurrency
        if self.number is not None:
            result['Number'] = self.number
        if self.number_name is not None:
            result['NumberName'] = self.number_name
        if self.outbound_concurrency is not None:
            result['OutboundConcurrency'] = self.outbound_concurrency
        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.supplier_id is not None:
            result['SupplierId'] = self.supplier_id
        if self.support is not None:
            result['Support'] = self.support
        if self.update_ts is not None:
            result['UpdateTs'] = self.update_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('DisableTs') is not None:
            self.disable_ts = m.get('DisableTs')
        if m.get('InboundConcurrency') is not None:
            self.inbound_concurrency = m.get('InboundConcurrency')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('NumberName') is not None:
            self.number_name = m.get('NumberName')
        if m.get('OutboundConcurrency') is not None:
            self.outbound_concurrency = m.get('OutboundConcurrency')
        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SupplierId') is not None:
            self.supplier_id = m.get('SupplierId')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        if m.get('UpdateTs') is not None:
            self.update_ts = m.get('UpdateTs')
        return self


class ListNumberResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListNumberResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListNumberResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListNumberResponse, self).to_map()
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
            temp_model = ListNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListQualificationRequest(TeaModel):
    def __init__(self, company_name=None, contact_phone=None, country_id=None, end_time=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None,
                 status=None):
        self.company_name = company_name  # type: str
        self.contact_phone = contact_phone  # type: str
        self.country_id = country_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQualificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListQualificationResponseBodyList(TeaModel):
    def __init__(self, address=None, audit_remark=None, audit_ts=None, business_license_file_key=None,
                 commit_ts=None, company_name=None, contact_email=None, contact_name=None, contact_phone=None,
                 country_id=None, legal_id=None, legal_license_file_key=None, legal_name=None, network_access_file_key=None,
                 qualification_id=None, status=None, unified_code=None, update_ts=None):
        self.address = address  # type: str
        self.audit_remark = audit_remark  # type: str
        self.audit_ts = audit_ts  # type: str
        self.business_license_file_key = business_license_file_key  # type: str
        self.commit_ts = commit_ts  # type: str
        self.company_name = company_name  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone = contact_phone  # type: str
        self.country_id = country_id  # type: str
        self.legal_id = legal_id  # type: str
        self.legal_license_file_key = legal_license_file_key  # type: str
        self.legal_name = legal_name  # type: str
        self.network_access_file_key = network_access_file_key  # type: str
        self.qualification_id = qualification_id  # type: str
        self.status = status  # type: long
        self.unified_code = unified_code  # type: str
        self.update_ts = update_ts  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListQualificationResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.audit_remark is not None:
            result['AuditRemark'] = self.audit_remark
        if self.audit_ts is not None:
            result['AuditTs'] = self.audit_ts
        if self.business_license_file_key is not None:
            result['BusinessLicenseFileKey'] = self.business_license_file_key
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.legal_id is not None:
            result['LegalId'] = self.legal_id
        if self.legal_license_file_key is not None:
            result['LegalLicenseFileKey'] = self.legal_license_file_key
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.network_access_file_key is not None:
            result['NetworkAccessFileKey'] = self.network_access_file_key
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.status is not None:
            result['Status'] = self.status
        if self.unified_code is not None:
            result['UnifiedCode'] = self.unified_code
        if self.update_ts is not None:
            result['UpdateTs'] = self.update_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('AuditRemark') is not None:
            self.audit_remark = m.get('AuditRemark')
        if m.get('AuditTs') is not None:
            self.audit_ts = m.get('AuditTs')
        if m.get('BusinessLicenseFileKey') is not None:
            self.business_license_file_key = m.get('BusinessLicenseFileKey')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('LegalId') is not None:
            self.legal_id = m.get('LegalId')
        if m.get('LegalLicenseFileKey') is not None:
            self.legal_license_file_key = m.get('LegalLicenseFileKey')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('NetworkAccessFileKey') is not None:
            self.network_access_file_key = m.get('NetworkAccessFileKey')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UnifiedCode') is not None:
            self.unified_code = m.get('UnifiedCode')
        if m.get('UpdateTs') is not None:
            self.update_ts = m.get('UpdateTs')
        return self


class ListQualificationResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListQualificationResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListQualificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListQualificationResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListQualificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListQualificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListQualificationResponse, self).to_map()
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
            temp_model = ListQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReceiptRequest(TeaModel):
    def __init__(self, business_type=None, end_time=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None):
        self.business_type = business_type  # type: int
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListReceiptRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListReceiptResponseBodyList(TeaModel):
    def __init__(self, call_failed_count=None, call_success_count=None, call_total_count=None, date=None):
        self.call_failed_count = call_failed_count  # type: int
        self.call_success_count = call_success_count  # type: int
        self.call_total_count = call_total_count  # type: int
        self.date = date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListReceiptResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_failed_count is not None:
            result['CallFailedCount'] = self.call_failed_count
        if self.call_success_count is not None:
            result['CallSuccessCount'] = self.call_success_count
        if self.call_total_count is not None:
            result['CallTotalCount'] = self.call_total_count
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallFailedCount') is not None:
            self.call_failed_count = m.get('CallFailedCount')
        if m.get('CallSuccessCount') is not None:
            self.call_success_count = m.get('CallSuccessCount')
        if m.get('CallTotalCount') is not None:
            self.call_total_count = m.get('CallTotalCount')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class ListReceiptResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, receipt_url=None, request_id=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListReceiptResponseBodyList]
        self.message = message  # type: str
        self.receipt_url = receipt_url  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListReceiptResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.receipt_url is not None:
            result['ReceiptUrl'] = self.receipt_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListReceiptResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReceiptUrl') is not None:
            self.receipt_url = m.get('ReceiptUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListReceiptResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListReceiptResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListReceiptResponse, self).to_map()
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
            temp_model = ListReceiptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSipTrunkRequest(TeaModel):
    def __init__(self, end_time=None, owner_id=None, page_number=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None, status=None):
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSipTrunkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListSipTrunkResponseBodyList(TeaModel):
    def __init__(self, apply_id=None, apply_note=None, audit_note=None, audit_ts=None, commit_ts=None,
                 country_id=None, inbound_ip_ports=None, outbound_ips=None, qualification_id=None, scene=None, status=None,
                 update_ts=None, user_uuid=None):
        self.apply_id = apply_id  # type: str
        self.apply_note = apply_note  # type: str
        self.audit_note = audit_note  # type: str
        self.audit_ts = audit_ts  # type: str
        self.commit_ts = commit_ts  # type: str
        self.country_id = country_id  # type: str
        self.inbound_ip_ports = inbound_ip_ports  # type: str
        self.outbound_ips = outbound_ips  # type: str
        self.qualification_id = qualification_id  # type: str
        self.scene = scene  # type: str
        self.status = status  # type: str
        self.update_ts = update_ts  # type: str
        self.user_uuid = user_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSipTrunkResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.apply_note is not None:
            result['ApplyNote'] = self.apply_note
        if self.audit_note is not None:
            result['AuditNote'] = self.audit_note
        if self.audit_ts is not None:
            result['AuditTs'] = self.audit_ts
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.inbound_ip_ports is not None:
            result['InboundIpPorts'] = self.inbound_ip_ports
        if self.outbound_ips is not None:
            result['OutboundIps'] = self.outbound_ips
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.status is not None:
            result['Status'] = self.status
        if self.update_ts is not None:
            result['UpdateTs'] = self.update_ts
        if self.user_uuid is not None:
            result['UserUuid'] = self.user_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('ApplyNote') is not None:
            self.apply_note = m.get('ApplyNote')
        if m.get('AuditNote') is not None:
            self.audit_note = m.get('AuditNote')
        if m.get('AuditTs') is not None:
            self.audit_ts = m.get('AuditTs')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('InboundIpPorts') is not None:
            self.inbound_ip_ports = m.get('InboundIpPorts')
        if m.get('OutboundIps') is not None:
            self.outbound_ips = m.get('OutboundIps')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTs') is not None:
            self.update_ts = m.get('UpdateTs')
        if m.get('UserUuid') is not None:
            self.user_uuid = m.get('UserUuid')
        return self


class ListSipTrunkResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListSipTrunkResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSipTrunkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSipTrunkResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSipTrunkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSipTrunkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSipTrunkResponse, self).to_map()
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
            temp_model = ListSipTrunkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSipTrunkDetailRequest(TeaModel):
    def __init__(self, called_number=None, calling_number=None, country_id=None, end_time=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.country_id = country_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSipTrunkDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListSipTrunkDetailResponseBodyList(TeaModel):
    def __init__(self, answer_time=None, answered=None, busi_type=None, call_end_time=None, call_type=None,
                 called_ip=None, called_num=None, called_num_region=None, called_num_type=None, caller_display=None,
                 caller_ip=None, caller_num=None, caller_num_region=None, caller_num_type=None, duration=None, hangup=None,
                 hangup_type=None, ivn_cli_type=None, record_url=None, start_time=None, user_uuid=None, uuid=None):
        self.answer_time = answer_time  # type: str
        self.answered = answered  # type: long
        self.busi_type = busi_type  # type: str
        self.call_end_time = call_end_time  # type: str
        self.call_type = call_type  # type: str
        self.called_ip = called_ip  # type: str
        self.called_num = called_num  # type: str
        self.called_num_region = called_num_region  # type: str
        self.called_num_type = called_num_type  # type: str
        self.caller_display = caller_display  # type: str
        self.caller_ip = caller_ip  # type: str
        self.caller_num = caller_num  # type: str
        self.caller_num_region = caller_num_region  # type: str
        self.caller_num_type = caller_num_type  # type: str
        self.duration = duration  # type: long
        self.hangup = hangup  # type: long
        self.hangup_type = hangup_type  # type: long
        self.ivn_cli_type = ivn_cli_type  # type: str
        self.record_url = record_url  # type: str
        self.start_time = start_time  # type: str
        self.user_uuid = user_uuid  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSipTrunkDetailResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time
        if self.answered is not None:
            result['Answered'] = self.answered
        if self.busi_type is not None:
            result['BusiType'] = self.busi_type
        if self.call_end_time is not None:
            result['CallEndTime'] = self.call_end_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.called_ip is not None:
            result['CalledIp'] = self.called_ip
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.called_num_region is not None:
            result['CalledNumRegion'] = self.called_num_region
        if self.called_num_type is not None:
            result['CalledNumType'] = self.called_num_type
        if self.caller_display is not None:
            result['CallerDisplay'] = self.caller_display
        if self.caller_ip is not None:
            result['CallerIp'] = self.caller_ip
        if self.caller_num is not None:
            result['CallerNum'] = self.caller_num
        if self.caller_num_region is not None:
            result['CallerNumRegion'] = self.caller_num_region
        if self.caller_num_type is not None:
            result['CallerNumType'] = self.caller_num_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hangup is not None:
            result['Hangup'] = self.hangup
        if self.hangup_type is not None:
            result['HangupType'] = self.hangup_type
        if self.ivn_cli_type is not None:
            result['IvnCliType'] = self.ivn_cli_type
        if self.record_url is not None:
            result['RecordUrl'] = self.record_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_uuid is not None:
            result['UserUuid'] = self.user_uuid
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')
        if m.get('Answered') is not None:
            self.answered = m.get('Answered')
        if m.get('BusiType') is not None:
            self.busi_type = m.get('BusiType')
        if m.get('CallEndTime') is not None:
            self.call_end_time = m.get('CallEndTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CalledIp') is not None:
            self.called_ip = m.get('CalledIp')
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('CalledNumRegion') is not None:
            self.called_num_region = m.get('CalledNumRegion')
        if m.get('CalledNumType') is not None:
            self.called_num_type = m.get('CalledNumType')
        if m.get('CallerDisplay') is not None:
            self.caller_display = m.get('CallerDisplay')
        if m.get('CallerIp') is not None:
            self.caller_ip = m.get('CallerIp')
        if m.get('CallerNum') is not None:
            self.caller_num = m.get('CallerNum')
        if m.get('CallerNumRegion') is not None:
            self.caller_num_region = m.get('CallerNumRegion')
        if m.get('CallerNumType') is not None:
            self.caller_num_type = m.get('CallerNumType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Hangup') is not None:
            self.hangup = m.get('Hangup')
        if m.get('HangupType') is not None:
            self.hangup_type = m.get('HangupType')
        if m.get('IvnCliType') is not None:
            self.ivn_cli_type = m.get('IvnCliType')
        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserUuid') is not None:
            self.user_uuid = m.get('UserUuid')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListSipTrunkDetailResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListSipTrunkDetailResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSipTrunkDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSipTrunkDetailResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSipTrunkDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSipTrunkDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSipTrunkDetailResponse, self).to_map()
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
            temp_model = ListSipTrunkDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSipTrunkStatRequest(TeaModel):
    def __init__(self, called_number=None, calling_number=None, end_time=None, owner_id=None, page_number=None,
                 page_size=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSipTrunkStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListSipTrunkStatResponseBodyList(TeaModel):
    def __init__(self, answered_calls=None, answered_rate=None, average_duration=None, billing=None,
                 called_number=None, calling_number=None, failed_calls=None, total_calls=None, total_duration=None):
        self.answered_calls = answered_calls  # type: long
        self.answered_rate = answered_rate  # type: long
        self.average_duration = average_duration  # type: long
        self.billing = billing  # type: long
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.failed_calls = failed_calls  # type: long
        self.total_calls = total_calls  # type: long
        self.total_duration = total_duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSipTrunkStatResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answered_calls is not None:
            result['AnsweredCalls'] = self.answered_calls
        if self.answered_rate is not None:
            result['AnsweredRate'] = self.answered_rate
        if self.average_duration is not None:
            result['AverageDuration'] = self.average_duration
        if self.billing is not None:
            result['Billing'] = self.billing
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.failed_calls is not None:
            result['FailedCalls'] = self.failed_calls
        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnsweredCalls') is not None:
            self.answered_calls = m.get('AnsweredCalls')
        if m.get('AnsweredRate') is not None:
            self.answered_rate = m.get('AnsweredRate')
        if m.get('AverageDuration') is not None:
            self.average_duration = m.get('AverageDuration')
        if m.get('Billing') is not None:
            self.billing = m.get('Billing')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('FailedCalls') is not None:
            self.failed_calls = m.get('FailedCalls')
        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class ListSipTrunkStatResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListSipTrunkStatResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSipTrunkStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSipTrunkStatResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSipTrunkStatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSipTrunkStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSipTrunkStatResponse, self).to_map()
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
            temp_model = ListSipTrunkStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVoiceCallRequest(TeaModel):
    def __init__(self, business_type=None, calling_number=None, country_id=None, end_time=None, owner_id=None,
                 page_number=None, page_size=None, resource_owner_account=None, resource_owner_id=None, send_type=None,
                 start_time=None, status=None, task_id=None, task_name=None):
        self.business_type = business_type  # type: long
        self.calling_number = calling_number  # type: str
        self.country_id = country_id  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.send_type = send_type  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: long
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListVoiceCallResponseBodyList(TeaModel):
    def __init__(self, answered_calls=None, business_type=None, called_calls=None, calling_number=None,
                 commit_ts=None, country_id=None, failed_calls=None, group_call_type=None, request_id=None, send_type=None,
                 status=None, task_id=None, task_name=None, template_content=None, template_id=None, ticker_ts=None,
                 total_calls=None, total_duration=None, user_uuid=None):
        self.answered_calls = answered_calls  # type: long
        self.business_type = business_type  # type: long
        self.called_calls = called_calls  # type: long
        self.calling_number = calling_number  # type: str
        self.commit_ts = commit_ts  # type: str
        self.country_id = country_id  # type: str
        self.failed_calls = failed_calls  # type: long
        self.group_call_type = group_call_type  # type: long
        self.request_id = request_id  # type: str
        self.send_type = send_type  # type: long
        self.status = status  # type: str
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str
        self.template_content = template_content  # type: str
        self.template_id = template_id  # type: str
        self.ticker_ts = ticker_ts  # type: str
        self.total_calls = total_calls  # type: long
        self.total_duration = total_duration  # type: long
        self.user_uuid = user_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceCallResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answered_calls is not None:
            result['AnsweredCalls'] = self.answered_calls
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.called_calls is not None:
            result['CalledCalls'] = self.called_calls
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.failed_calls is not None:
            result['FailedCalls'] = self.failed_calls
        if self.group_call_type is not None:
            result['GroupCallType'] = self.group_call_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.ticker_ts is not None:
            result['TickerTs'] = self.ticker_ts
        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        if self.user_uuid is not None:
            result['UserUuid'] = self.user_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnsweredCalls') is not None:
            self.answered_calls = m.get('AnsweredCalls')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CalledCalls') is not None:
            self.called_calls = m.get('CalledCalls')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('FailedCalls') is not None:
            self.failed_calls = m.get('FailedCalls')
        if m.get('GroupCallType') is not None:
            self.group_call_type = m.get('GroupCallType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TickerTs') is not None:
            self.ticker_ts = m.get('TickerTs')
        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        if m.get('UserUuid') is not None:
            self.user_uuid = m.get('UserUuid')
        return self


class ListVoiceCallResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListVoiceCallResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVoiceCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListVoiceCallResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVoiceCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVoiceCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVoiceCallResponse, self).to_map()
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
            temp_model = ListVoiceCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVoiceCallDetailRequest(TeaModel):
    def __init__(self, business_type=None, called_number=None, calling_number=None, country_id=None, end_time=None,
                 hangup_type=None, owner_id=None, page_number=None, page_size=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None, status=None, task_id=None, task_name=None):
        self.business_type = business_type  # type: long
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.country_id = country_id  # type: str
        self.end_time = end_time  # type: str
        self.hangup_type = hangup_type  # type: long
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.status = status  # type: long
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceCallDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.hangup_type is not None:
            result['HangupType'] = self.hangup_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('HangupType') is not None:
            self.hangup_type = m.get('HangupType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListVoiceCallDetailResponseBodyList(TeaModel):
    def __init__(self, billing=None, business_type=None, called_number=None, calling_number=None, commit_ts=None,
                 country_id=None, duration=None, end_ts=None, hangup_type=None, send_type=None, start_ts=None, status=None,
                 task_id=None, task_name=None):
        self.billing = billing  # type: long
        self.business_type = business_type  # type: long
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.commit_ts = commit_ts  # type: str
        self.country_id = country_id  # type: str
        self.duration = duration  # type: long
        self.end_ts = end_ts  # type: str
        self.hangup_type = hangup_type  # type: long
        self.send_type = send_type  # type: long
        self.start_ts = start_ts  # type: str
        self.status = status  # type: long
        self.task_id = task_id  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceCallDetailResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.billing is not None:
            result['Billing'] = self.billing
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.end_ts is not None:
            result['EndTs'] = self.end_ts
        if self.hangup_type is not None:
            result['HangupType'] = self.hangup_type
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.start_ts is not None:
            result['StartTs'] = self.start_ts
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Billing') is not None:
            self.billing = m.get('Billing')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')
        if m.get('HangupType') is not None:
            self.hangup_type = m.get('HangupType')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListVoiceCallDetailResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListVoiceCallDetailResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVoiceCallDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListVoiceCallDetailResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVoiceCallDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVoiceCallDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVoiceCallDetailResponse, self).to_map()
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
            temp_model = ListVoiceCallDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVoiceCallStatRequest(TeaModel):
    def __init__(self, business_type=None, end_time=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, start_time=None, task_name=None):
        self.business_type = business_type  # type: long
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str
        self.task_name = task_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceCallStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListVoiceCallStatResponseBodyList(TeaModel):
    def __init__(self, answered_calls=None, answered_rate=None, average_duration=None, billing=None,
                 business_type=None, failed_calls=None, total_calls=None, total_duration=None):
        self.answered_calls = answered_calls  # type: long
        self.answered_rate = answered_rate  # type: long
        self.average_duration = average_duration  # type: long
        self.billing = billing  # type: long
        self.business_type = business_type  # type: long
        self.failed_calls = failed_calls  # type: long
        self.total_calls = total_calls  # type: long
        self.total_duration = total_duration  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceCallStatResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answered_calls is not None:
            result['AnsweredCalls'] = self.answered_calls
        if self.answered_rate is not None:
            result['AnsweredRate'] = self.answered_rate
        if self.average_duration is not None:
            result['AverageDuration'] = self.average_duration
        if self.billing is not None:
            result['Billing'] = self.billing
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.failed_calls is not None:
            result['FailedCalls'] = self.failed_calls
        if self.total_calls is not None:
            result['TotalCalls'] = self.total_calls
        if self.total_duration is not None:
            result['TotalDuration'] = self.total_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnsweredCalls') is not None:
            self.answered_calls = m.get('AnsweredCalls')
        if m.get('AnsweredRate') is not None:
            self.answered_rate = m.get('AnsweredRate')
        if m.get('AverageDuration') is not None:
            self.average_duration = m.get('AverageDuration')
        if m.get('Billing') is not None:
            self.billing = m.get('Billing')
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('FailedCalls') is not None:
            self.failed_calls = m.get('FailedCalls')
        if m.get('TotalCalls') is not None:
            self.total_calls = m.get('TotalCalls')
        if m.get('TotalDuration') is not None:
            self.total_duration = m.get('TotalDuration')
        return self


class ListVoiceCallStatResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListVoiceCallStatResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVoiceCallStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListVoiceCallStatResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVoiceCallStatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVoiceCallStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVoiceCallStatResponse, self).to_map()
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
            temp_model = ListVoiceCallStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVoiceFileRequest(TeaModel):
    def __init__(self, country_id=None, file_name=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, status=None):
        self.country_id = country_id  # type: str
        self.file_name = file_name  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListVoiceFileResponseBodyList(TeaModel):
    def __init__(self, audit_remark=None, commit_ts=None, country_id=None, file_id=None, file_key=None,
                 file_name=None, file_url=None, qualification_id=None, status=None, update_ts=None):
        self.audit_remark = audit_remark  # type: str
        self.commit_ts = commit_ts  # type: str
        self.country_id = country_id  # type: str
        self.file_id = file_id  # type: str
        self.file_key = file_key  # type: str
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.qualification_id = qualification_id  # type: str
        self.status = status  # type: long
        self.update_ts = update_ts  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceFileResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_remark is not None:
            result['AuditRemark'] = self.audit_remark
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.status is not None:
            result['Status'] = self.status
        if self.update_ts is not None:
            result['UpdateTs'] = self.update_ts
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditRemark') is not None:
            self.audit_remark = m.get('AuditRemark')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTs') is not None:
            self.update_ts = m.get('UpdateTs')
        return self


class ListVoiceFileResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListVoiceFileResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVoiceFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListVoiceFileResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVoiceFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVoiceFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVoiceFileResponse, self).to_map()
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
            temp_model = ListVoiceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVoiceTtsRequest(TeaModel):
    def __init__(self, country_id=None, owner_id=None, page_number=None, page_size=None,
                 resource_owner_account=None, resource_owner_id=None, status=None, template_name=None):
        self.country_id = country_id  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.status = status  # type: long
        self.template_name = template_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceTtsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.status is not None:
            result['Status'] = self.status
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListVoiceTtsResponseBodyList(TeaModel):
    def __init__(self, audit_by=None, audit_remark=None, audit_ts=None, commit_ts=None, country_id=None,
                 language=None, qualification_id=None, speed=None, status=None, template_id=None, template_name=None,
                 template_text=None, update_ts=None, user_uuid=None):
        self.audit_by = audit_by  # type: str
        self.audit_remark = audit_remark  # type: str
        self.audit_ts = audit_ts  # type: str
        self.commit_ts = commit_ts  # type: str
        self.country_id = country_id  # type: str
        self.language = language  # type: str
        self.qualification_id = qualification_id  # type: str
        self.speed = speed  # type: int
        self.status = status  # type: int
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_text = template_text  # type: str
        self.update_ts = update_ts  # type: str
        self.user_uuid = user_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVoiceTtsResponseBodyList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audit_by is not None:
            result['AuditBy'] = self.audit_by
        if self.audit_remark is not None:
            result['AuditRemark'] = self.audit_remark
        if self.audit_ts is not None:
            result['AuditTs'] = self.audit_ts
        if self.commit_ts is not None:
            result['CommitTs'] = self.commit_ts
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.language is not None:
            result['Language'] = self.language
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        if self.update_ts is not None:
            result['UpdateTs'] = self.update_ts
        if self.user_uuid is not None:
            result['UserUuid'] = self.user_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuditBy') is not None:
            self.audit_by = m.get('AuditBy')
        if m.get('AuditRemark') is not None:
            self.audit_remark = m.get('AuditRemark')
        if m.get('AuditTs') is not None:
            self.audit_ts = m.get('AuditTs')
        if m.get('CommitTs') is not None:
            self.commit_ts = m.get('CommitTs')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        if m.get('UpdateTs') is not None:
            self.update_ts = m.get('UpdateTs')
        if m.get('UserUuid') is not None:
            self.user_uuid = m.get('UserUuid')
        return self


class ListVoiceTtsResponseBody(TeaModel):
    def __init__(self, code=None, list=None, message=None, request_id=None, total=None):
        self.code = code  # type: str
        self.list = list  # type: list[ListVoiceTtsResponseBodyList]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVoiceTtsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListVoiceTtsResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVoiceTtsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVoiceTtsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVoiceTtsResponse, self).to_map()
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
            temp_model = ListVoiceTtsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NumberEnableRequest(TeaModel):
    def __init__(self, enable=None, number=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.enable = enable  # type: bool
        self.number = number  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(NumberEnableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.number is not None:
            result['Number'] = self.number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class NumberEnableResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NumberEnableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NumberEnableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NumberEnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NumberEnableResponse, self).to_map()
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
            temp_model = NumberEnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenIntlVoiceServiceRequest(TeaModel):
    def __init__(self, env=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.env = env  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenIntlVoiceServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.env is not None:
            result['Env'] = self.env
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class OpenIntlVoiceServiceResponseBody(TeaModel):
    def __init__(self, code=None, message=None, model=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.model = model  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenIntlVoiceServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model
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
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class OpenIntlVoiceServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenIntlVoiceServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenIntlVoiceServiceResponse, self).to_map()
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
            temp_model = OpenIntlVoiceServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OswTest1Request(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OswTest1Request, self).to_map()
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


class OswTest1ResponseBody(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super(OswTest1ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m=None):
        m = m or dict()
        return self


class OswTest1Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OswTest1ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OswTest1Response, self).to_map()
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
            temp_model = OswTest1ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFileOssUrlRequest(TeaModel):
    def __init__(self, biz_type=None, file_key=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None):
        self.biz_type = biz_type  # type: str
        self.file_key = file_key  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFileOssUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class QueryFileOssUrlResponseBody(TeaModel):
    def __init__(self, access_key_id=None, request_id=None, url=None):
        self.access_key_id = access_key_id  # type: str
        self.request_id = request_id  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFileOssUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryFileOssUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFileOssUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFileOssUrlResponse, self).to_map()
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
            temp_model = QueryFileOssUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryHomeStatRequest(TeaModel):
    def __init__(self, business_type=None, end_time=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, start_time=None):
        self.business_type = business_type  # type: long
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHomeStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_type is not None:
            result['BusinessType'] = self.business_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BusinessType') is not None:
            self.business_type = m.get('BusinessType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryHomeStatResponseBodyModelList(TeaModel):
    def __init__(self, call_failed=None, call_success=None, call_total=None, date=None, success_rate=None):
        self.call_failed = call_failed  # type: long
        self.call_success = call_success  # type: long
        self.call_total = call_total  # type: long
        self.date = date  # type: str
        self.success_rate = success_rate  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryHomeStatResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.call_failed is not None:
            result['CallFailed'] = self.call_failed
        if self.call_success is not None:
            result['CallSuccess'] = self.call_success
        if self.call_total is not None:
            result['CallTotal'] = self.call_total
        if self.date is not None:
            result['Date'] = self.date
        if self.success_rate is not None:
            result['SuccessRate'] = self.success_rate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CallFailed') is not None:
            self.call_failed = m.get('CallFailed')
        if m.get('CallSuccess') is not None:
            self.call_success = m.get('CallSuccess')
        if m.get('CallTotal') is not None:
            self.call_total = m.get('CallTotal')
        if m.get('Date') is not None:
            self.date = m.get('Date')
        if m.get('SuccessRate') is not None:
            self.success_rate = m.get('SuccessRate')
        return self


class QueryHomeStatResponseBodyModel(TeaModel):
    def __init__(self, cdr_dr_url=None, list=None):
        self.cdr_dr_url = cdr_dr_url  # type: str
        self.list = list  # type: list[QueryHomeStatResponseBodyModelList]

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryHomeStatResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdr_dr_url is not None:
            result['CdrDrUrl'] = self.cdr_dr_url
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdrDrUrl') is not None:
            self.cdr_dr_url = m.get('CdrDrUrl')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryHomeStatResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        return self


class QueryHomeStatResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, model=None, request_id=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: long
        self.message = message  # type: str
        self.model = model  # type: QueryHomeStatResponseBodyModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(QueryHomeStatResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = QueryHomeStatResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryHomeStatResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryHomeStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryHomeStatResponse, self).to_map()
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
            temp_model = QueryHomeStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordingEnableRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordingEnableRequest, self).to_map()
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


class QueryRecordingEnableResponseBody(TeaModel):
    def __init__(self, code=None, enable=None, message=None, request_id=None):
        self.code = code  # type: str
        self.enable = enable  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordingEnableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryRecordingEnableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordingEnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordingEnableResponse, self).to_map()
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
            temp_model = QueryRecordingEnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServiceEnableRequest(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryServiceEnableRequest, self).to_map()
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


class QueryServiceEnableResponseBody(TeaModel):
    def __init__(self, code=None, enable=None, message=None, request_id=None):
        self.code = code  # type: str
        self.enable = enable  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryServiceEnableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryServiceEnableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryServiceEnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryServiceEnableResponse, self).to_map()
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
            temp_model = QueryServiceEnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordingEnableRequest(TeaModel):
    def __init__(self, enable=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.enable = enable  # type: bool
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordingEnableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class RecordingEnableResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordingEnableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecordingEnableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RecordingEnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecordingEnableResponse, self).to_map()
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
            temp_model = RecordingEnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetReceiptUrlRequest(TeaModel):
    def __init__(self, cdr_dr_url=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.cdr_dr_url = cdr_dr_url  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetReceiptUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdr_dr_url is not None:
            result['CdrDrUrl'] = self.cdr_dr_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CdrDrUrl') is not None:
            self.cdr_dr_url = m.get('CdrDrUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SetReceiptUrlResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetReceiptUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetReceiptUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetReceiptUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetReceiptUrlResponse, self).to_map()
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
            temp_model = SetReceiptUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SipTrunkDetailRequest(TeaModel):
    def __init__(self, called_number=None, calling_number=None, end_time=None, owner_id=None, page_number=None,
                 page_size=None, region_id=None, resource_owner_account=None, resource_owner_id=None, start_time=None):
        self.called_number = called_number  # type: str
        self.calling_number = calling_number  # type: str
        self.end_time = end_time  # type: str
        self.owner_id = owner_id  # type: long
        self.page_number = page_number  # type: long
        self.page_size = page_size  # type: long
        self.region_id = region_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SipTrunkDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class SipTrunkDetailResponseBodyModelList(TeaModel):
    def __init__(self, answer_time=None, answered=None, busi_type=None, call_end_time=None, call_type=None,
                 called_ip=None, called_num=None, called_num_region=None, called_num_type=None, caller_display=None,
                 caller_ip=None, caller_num=None, caller_num_region=None, caller_num_type=None, duration=None, hangup=None,
                 hangup_type=None, lvn_cli_type=None, record_url=None, start_time=None, user_uuid=None, uuid=None):
        self.answer_time = answer_time  # type: str
        self.answered = answered  # type: long
        self.busi_type = busi_type  # type: str
        self.call_end_time = call_end_time  # type: str
        self.call_type = call_type  # type: str
        self.called_ip = called_ip  # type: str
        self.called_num = called_num  # type: str
        self.called_num_region = called_num_region  # type: str
        self.called_num_type = called_num_type  # type: str
        self.caller_display = caller_display  # type: str
        self.caller_ip = caller_ip  # type: str
        self.caller_num = caller_num  # type: str
        self.caller_num_region = caller_num_region  # type: str
        self.caller_num_type = caller_num_type  # type: str
        self.duration = duration  # type: long
        self.hangup = hangup  # type: long
        self.hangup_type = hangup_type  # type: long
        self.lvn_cli_type = lvn_cli_type  # type: str
        self.record_url = record_url  # type: str
        self.start_time = start_time  # type: str
        self.user_uuid = user_uuid  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SipTrunkDetailResponseBodyModelList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_time is not None:
            result['AnswerTime'] = self.answer_time
        if self.answered is not None:
            result['Answered'] = self.answered
        if self.busi_type is not None:
            result['BusiType'] = self.busi_type
        if self.call_end_time is not None:
            result['CallEndTime'] = self.call_end_time
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.called_ip is not None:
            result['CalledIp'] = self.called_ip
        if self.called_num is not None:
            result['CalledNum'] = self.called_num
        if self.called_num_region is not None:
            result['CalledNumRegion'] = self.called_num_region
        if self.called_num_type is not None:
            result['CalledNumType'] = self.called_num_type
        if self.caller_display is not None:
            result['CallerDisplay'] = self.caller_display
        if self.caller_ip is not None:
            result['CallerIp'] = self.caller_ip
        if self.caller_num is not None:
            result['CallerNum'] = self.caller_num
        if self.caller_num_region is not None:
            result['CallerNumRegion'] = self.caller_num_region
        if self.caller_num_type is not None:
            result['CallerNumType'] = self.caller_num_type
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hangup is not None:
            result['Hangup'] = self.hangup
        if self.hangup_type is not None:
            result['HangupType'] = self.hangup_type
        if self.lvn_cli_type is not None:
            result['LvnCliType'] = self.lvn_cli_type
        if self.record_url is not None:
            result['RecordUrl'] = self.record_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.user_uuid is not None:
            result['UserUuid'] = self.user_uuid
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnswerTime') is not None:
            self.answer_time = m.get('AnswerTime')
        if m.get('Answered') is not None:
            self.answered = m.get('Answered')
        if m.get('BusiType') is not None:
            self.busi_type = m.get('BusiType')
        if m.get('CallEndTime') is not None:
            self.call_end_time = m.get('CallEndTime')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('CalledIp') is not None:
            self.called_ip = m.get('CalledIp')
        if m.get('CalledNum') is not None:
            self.called_num = m.get('CalledNum')
        if m.get('CalledNumRegion') is not None:
            self.called_num_region = m.get('CalledNumRegion')
        if m.get('CalledNumType') is not None:
            self.called_num_type = m.get('CalledNumType')
        if m.get('CallerDisplay') is not None:
            self.caller_display = m.get('CallerDisplay')
        if m.get('CallerIp') is not None:
            self.caller_ip = m.get('CallerIp')
        if m.get('CallerNum') is not None:
            self.caller_num = m.get('CallerNum')
        if m.get('CallerNumRegion') is not None:
            self.caller_num_region = m.get('CallerNumRegion')
        if m.get('CallerNumType') is not None:
            self.caller_num_type = m.get('CallerNumType')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Hangup') is not None:
            self.hangup = m.get('Hangup')
        if m.get('HangupType') is not None:
            self.hangup_type = m.get('HangupType')
        if m.get('LvnCliType') is not None:
            self.lvn_cli_type = m.get('LvnCliType')
        if m.get('RecordUrl') is not None:
            self.record_url = m.get('RecordUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UserUuid') is not None:
            self.user_uuid = m.get('UserUuid')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class SipTrunkDetailResponseBodyModel(TeaModel):
    def __init__(self, list=None, total=None):
        self.list = list  # type: list[SipTrunkDetailResponseBodyModelList]
        self.total = total  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SipTrunkDetailResponseBodyModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = SipTrunkDetailResponseBodyModelList()
                self.list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SipTrunkDetailResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, model=None, request_id=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: long
        self.message = message  # type: str
        self.model = model  # type: SipTrunkDetailResponseBodyModel
        self.request_id = request_id  # type: str

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super(SipTrunkDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Model') is not None:
            temp_model = SipTrunkDetailResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SipTrunkDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SipTrunkDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SipTrunkDetailResponse, self).to_map()
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
            temp_model = SipTrunkDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitGroupCallRequest(TeaModel):
    def __init__(self, biz_type=None, caller_id_number=None, country_id=None, file_key=None, file_name=None,
                 group_call_type=None, owner_id=None, product_code=None, resource_owner_account=None, resource_owner_id=None,
                 send_type=None, task_name=None, template_id=None, timing_start=None):
        self.biz_type = biz_type  # type: str
        self.caller_id_number = caller_id_number  # type: str
        self.country_id = country_id  # type: str
        self.file_key = file_key  # type: str
        self.file_name = file_name  # type: str
        self.group_call_type = group_call_type  # type: long
        self.owner_id = owner_id  # type: long
        self.product_code = product_code  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.send_type = send_type  # type: long
        self.task_name = task_name  # type: str
        self.template_id = template_id  # type: str
        self.timing_start = timing_start  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitGroupCallRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.caller_id_number is not None:
            result['CallerIdNumber'] = self.caller_id_number
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.group_call_type is not None:
            result['GroupCallType'] = self.group_call_type
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.send_type is not None:
            result['SendType'] = self.send_type
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.timing_start is not None:
            result['TimingStart'] = self.timing_start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('CallerIdNumber') is not None:
            self.caller_id_number = m.get('CallerIdNumber')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('GroupCallType') is not None:
            self.group_call_type = m.get('GroupCallType')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('SendType') is not None:
            self.send_type = m.get('SendType')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TimingStart') is not None:
            self.timing_start = m.get('TimingStart')
        return self


class SubmitGroupCallResponseBody(TeaModel):
    def __init__(self, code=None, request_id=None, task_id=None):
        self.code = code  # type: str
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitGroupCallResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SubmitGroupCallResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitGroupCallResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitGroupCallResponse, self).to_map()
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
            temp_model = SubmitGroupCallResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitNumberRequestNumberList(TeaModel):
    def __init__(self, amount=None, inbound_concurrency=None, outbound_concurrency=None, phone_type=None,
                 support=None):
        self.amount = amount  # type: long
        self.inbound_concurrency = inbound_concurrency  # type: long
        self.outbound_concurrency = outbound_concurrency  # type: long
        self.phone_type = phone_type  # type: long
        self.support = support  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitNumberRequestNumberList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.inbound_concurrency is not None:
            result['InboundConcurrency'] = self.inbound_concurrency
        if self.outbound_concurrency is not None:
            result['OutboundConcurrency'] = self.outbound_concurrency
        if self.phone_type is not None:
            result['PhoneType'] = self.phone_type
        if self.support is not None:
            result['Support'] = self.support
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')
        if m.get('InboundConcurrency') is not None:
            self.inbound_concurrency = m.get('InboundConcurrency')
        if m.get('OutboundConcurrency') is not None:
            self.outbound_concurrency = m.get('OutboundConcurrency')
        if m.get('PhoneType') is not None:
            self.phone_type = m.get('PhoneType')
        if m.get('Support') is not None:
            self.support = m.get('Support')
        return self


class SubmitNumberRequest(TeaModel):
    def __init__(self, apply_note=None, country_id=None, number_list=None, owner_id=None, qualification_id=None,
                 resource_owner_account=None, resource_owner_id=None, scene=None):
        self.apply_note = apply_note  # type: str
        self.country_id = country_id  # type: str
        self.number_list = number_list  # type: list[SubmitNumberRequestNumberList]
        self.owner_id = owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.scene = scene  # type: str

    def validate(self):
        if self.number_list:
            for k in self.number_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SubmitNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_note is not None:
            result['ApplyNote'] = self.apply_note
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        result['NumberList'] = []
        if self.number_list is not None:
            for k in self.number_list:
                result['NumberList'].append(k.to_map() if k else None)
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyNote') is not None:
            self.apply_note = m.get('ApplyNote')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        self.number_list = []
        if m.get('NumberList') is not None:
            for k in m.get('NumberList'):
                temp_model = SubmitNumberRequestNumberList()
                self.number_list.append(temp_model.from_map(k))
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class SubmitNumberShrinkRequest(TeaModel):
    def __init__(self, apply_note=None, country_id=None, number_list_shrink=None, owner_id=None,
                 qualification_id=None, resource_owner_account=None, resource_owner_id=None, scene=None):
        self.apply_note = apply_note  # type: str
        self.country_id = country_id  # type: str
        self.number_list_shrink = number_list_shrink  # type: str
        self.owner_id = owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitNumberShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_note is not None:
            result['ApplyNote'] = self.apply_note
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.number_list_shrink is not None:
            result['NumberList'] = self.number_list_shrink
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyNote') is not None:
            self.apply_note = m.get('ApplyNote')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('NumberList') is not None:
            self.number_list_shrink = m.get('NumberList')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class SubmitNumberResponseBody(TeaModel):
    def __init__(self, apply_id=None, code=None, request_id=None):
        self.apply_id = apply_id  # type: str
        self.code = code  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitNumberResponse, self).to_map()
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
            temp_model = SubmitNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitQualificationRequest(TeaModel):
    def __init__(self, address=None, business_license_file_key=None, company_name=None, contact_email=None,
                 contact_name=None, contact_phone=None, country_id=None, legal_id=None, legal_license_file_key=None,
                 legal_name=None, network_access_file_key=None, owner_id=None, resource_owner_account=None,
                 resource_owner_id=None, unified_code=None):
        self.address = address  # type: str
        self.business_license_file_key = business_license_file_key  # type: str
        self.company_name = company_name  # type: str
        self.contact_email = contact_email  # type: str
        self.contact_name = contact_name  # type: str
        self.contact_phone = contact_phone  # type: str
        self.country_id = country_id  # type: str
        self.legal_id = legal_id  # type: str
        self.legal_license_file_key = legal_license_file_key  # type: str
        self.legal_name = legal_name  # type: str
        self.network_access_file_key = network_access_file_key  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.unified_code = unified_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitQualificationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.business_license_file_key is not None:
            result['BusinessLicenseFileKey'] = self.business_license_file_key
        if self.company_name is not None:
            result['CompanyName'] = self.company_name
        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.contact_phone is not None:
            result['ContactPhone'] = self.contact_phone
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.legal_id is not None:
            result['LegalId'] = self.legal_id
        if self.legal_license_file_key is not None:
            result['LegalLicenseFileKey'] = self.legal_license_file_key
        if self.legal_name is not None:
            result['LegalName'] = self.legal_name
        if self.network_access_file_key is not None:
            result['NetworkAccessFileKey'] = self.network_access_file_key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.unified_code is not None:
            result['UnifiedCode'] = self.unified_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('BusinessLicenseFileKey') is not None:
            self.business_license_file_key = m.get('BusinessLicenseFileKey')
        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')
        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('ContactPhone') is not None:
            self.contact_phone = m.get('ContactPhone')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('LegalId') is not None:
            self.legal_id = m.get('LegalId')
        if m.get('LegalLicenseFileKey') is not None:
            self.legal_license_file_key = m.get('LegalLicenseFileKey')
        if m.get('LegalName') is not None:
            self.legal_name = m.get('LegalName')
        if m.get('NetworkAccessFileKey') is not None:
            self.network_access_file_key = m.get('NetworkAccessFileKey')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('UnifiedCode') is not None:
            self.unified_code = m.get('UnifiedCode')
        return self


class SubmitQualificationResponseBody(TeaModel):
    def __init__(self, code=None, message=None, qualification_id=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.qualification_id = qualification_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitQualificationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitQualificationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitQualificationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitQualificationResponse, self).to_map()
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
            temp_model = SubmitQualificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitSipTrunkRequest(TeaModel):
    def __init__(self, apply_note=None, country_id=None, inbound_ip_ports=None, outbound_ips=None, owner_id=None,
                 qualification_id=None, resource_owner_account=None, resource_owner_id=None, scene=None):
        self.apply_note = apply_note  # type: str
        self.country_id = country_id  # type: str
        self.inbound_ip_ports = inbound_ip_ports  # type: str
        self.outbound_ips = outbound_ips  # type: str
        self.owner_id = owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.scene = scene  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSipTrunkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_note is not None:
            result['ApplyNote'] = self.apply_note
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.inbound_ip_ports is not None:
            result['InboundIpPorts'] = self.inbound_ip_ports
        if self.outbound_ips is not None:
            result['OutboundIps'] = self.outbound_ips
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyNote') is not None:
            self.apply_note = m.get('ApplyNote')
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('InboundIpPorts') is not None:
            self.inbound_ip_ports = m.get('InboundIpPorts')
        if m.get('OutboundIps') is not None:
            self.outbound_ips = m.get('OutboundIps')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class SubmitSipTrunkResponseBody(TeaModel):
    def __init__(self, apply_id=None, code=None, message=None, request_id=None):
        self.apply_id = apply_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitSipTrunkResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitSipTrunkResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitSipTrunkResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitSipTrunkResponse, self).to_map()
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
            temp_model = SubmitSipTrunkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitVoiceFileRequest(TeaModel):
    def __init__(self, country_id=None, file_key=None, file_name=None, file_url=None, owner_id=None,
                 qualification_id=None, resource_owner_account=None, resource_owner_id=None):
        self.country_id = country_id  # type: str
        self.file_key = file_key  # type: str
        self.file_name = file_name  # type: str
        self.file_url = file_url  # type: str
        self.owner_id = owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitVoiceFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class SubmitVoiceFileResponseBody(TeaModel):
    def __init__(self, apply_id=None, code=None, message=None, request_id=None):
        self.apply_id = apply_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitVoiceFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitVoiceFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitVoiceFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitVoiceFileResponse, self).to_map()
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
            temp_model = SubmitVoiceFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitVoiceTtsRequest(TeaModel):
    def __init__(self, country_id=None, language=None, owner_id=None, qualification_id=None,
                 resource_owner_account=None, resource_owner_id=None, speed=None, status=None, template_id=None, template_name=None,
                 template_text=None):
        self.country_id = country_id  # type: str
        self.language = language  # type: str
        self.owner_id = owner_id  # type: long
        self.qualification_id = qualification_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long
        self.speed = speed  # type: long
        self.status = status  # type: long
        self.template_id = template_id  # type: str
        self.template_name = template_name  # type: str
        self.template_text = template_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitVoiceTtsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.country_id is not None:
            result['CountryId'] = self.country_id
        if self.language is not None:
            result['Language'] = self.language
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.qualification_id is not None:
            result['QualificationId'] = self.qualification_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        if self.speed is not None:
            result['Speed'] = self.speed
        if self.status is not None:
            result['Status'] = self.status
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_text is not None:
            result['TemplateText'] = self.template_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('QualificationId') is not None:
            self.qualification_id = m.get('QualificationId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateText') is not None:
            self.template_text = m.get('TemplateText')
        return self


class SubmitVoiceTtsResponseBody(TeaModel):
    def __init__(self, apply_id=None, code=None, message=None, request_id=None):
        self.apply_id = apply_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitVoiceTtsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_id is not None:
            result['ApplyId'] = self.apply_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyId') is not None:
            self.apply_id = m.get('ApplyId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SubmitVoiceTtsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitVoiceTtsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitVoiceTtsResponse, self).to_map()
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
            temp_model = SubmitVoiceTtsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNumberRequest(TeaModel):
    def __init__(self, note=None, number=None, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.note = note  # type: str
        self.number = number  # type: str
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNumberRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.note is not None:
            result['Note'] = self.note
        if self.number is not None:
            result['Number'] = self.number
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')
        return self


class UpdateNumberResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNumberResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNumberResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNumberResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNumberResponse, self).to_map()
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
            temp_model = UpdateNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Test02Request(TeaModel):
    def __init__(self, owner_id=None, resource_owner_account=None, resource_owner_id=None):
        self.owner_id = owner_id  # type: long
        self.resource_owner_account = resource_owner_account  # type: str
        self.resource_owner_id = resource_owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Test02Request, self).to_map()
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


class Test02ResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Test02ResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class Test02Response(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Test02ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Test02Response, self).to_map()
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
            temp_model = Test02ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


