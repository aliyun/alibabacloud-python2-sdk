# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelVideoTaskRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelVideoTaskRequestApp, self).to_map()
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


class CancelVideoTaskRequest(TeaModel):
    def __init__(self, app=None, task_uuid=None, tenant_id=None):
        self.app = app  # type: CancelVideoTaskRequestApp
        self.task_uuid = task_uuid  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super(CancelVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = CancelVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelVideoTaskShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, task_uuid=None, tenant_id=None):
        self.app_shrink = app_shrink  # type: str
        self.task_uuid = task_uuid  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelVideoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CancelVideoTaskResponseBodyData(TeaModel):
    def __init__(self, fail_reason=None, is_cancel=None, task_uuid=None):
        self.fail_reason = fail_reason  # type: str
        self.is_cancel = is_cancel  # type: bool
        self.task_uuid = task_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelVideoTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.is_cancel is not None:
            result['IsCancel'] = self.is_cancel
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('IsCancel') is not None:
            self.is_cancel = m.get('IsCancel')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class CancelVideoTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CancelVideoTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CancelVideoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CancelVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelVideoTaskResponse, self).to_map()
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
            temp_model = CancelVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClientAuthRequest(TeaModel):
    def __init__(self, app_id=None, device_id=None, device_info=None, device_type=None, license=None, tenant_id=None):
        self.app_id = app_id  # type: str
        self.device_id = device_id  # type: str
        self.device_info = device_info  # type: str
        self.device_type = device_type  # type: str
        self.license = license  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClientAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.license is not None:
            result['License'] = self.license
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceInfo') is not None:
            self.device_info = m.get('DeviceInfo')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ClientAuthResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClientAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClientAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClientAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClientAuthResponse, self).to_map()
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
            temp_model = ClientAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClientStartRequest(TeaModel):
    def __init__(self, app_id=None, tenant_id=None):
        self.app_id = app_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClientStartRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ClientStartResponseBodyData(TeaModel):
    def __init__(self, im_token=None):
        self.im_token = im_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClientStartResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.im_token is not None:
            result['ImToken'] = self.im_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ImToken') is not None:
            self.im_token = m.get('ImToken')
        return self


class ClientStartResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: ClientStartResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ClientStartResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = ClientStartResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClientStartResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClientStartResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClientStartResponse, self).to_map()
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
            temp_model = ClientStartResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloseTimedResetOperateRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseTimedResetOperateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CloseTimedResetOperateResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CloseTimedResetOperateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class CloseTimedResetOperateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CloseTimedResetOperateResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CloseTimedResetOperateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = CloseTimedResetOperateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CloseTimedResetOperateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CloseTimedResetOperateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CloseTimedResetOperateResponse, self).to_map()
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
            temp_model = CloseTimedResetOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Create2dAvatarRequest(TeaModel):
    def __init__(self, callback=None, description=None, image=None, name=None, orientation=None, portrait=None,
                 tenant_id=None, transparent=None, video=None):
        self.callback = callback  # type: bool
        self.description = description  # type: str
        self.image = image  # type: str
        self.name = name  # type: str
        self.orientation = orientation  # type: int
        self.portrait = portrait  # type: str
        self.tenant_id = tenant_id  # type: long
        self.transparent = transparent  # type: bool
        self.video = video  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Create2dAvatarRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transparent is not None:
            result['Transparent'] = self.transparent
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Transparent') is not None:
            self.transparent = m.get('Transparent')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class Create2dAvatarResponseBodyData(TeaModel):
    def __init__(self, code=None):
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Create2dAvatarResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class Create2dAvatarResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: Create2dAvatarResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(Create2dAvatarResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = Create2dAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class Create2dAvatarResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Create2dAvatarResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Create2dAvatarResponse, self).to_map()
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
            temp_model = Create2dAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAvatarRequest(TeaModel):
    def __init__(self, code=None, tenant_id=None):
        self.code = code  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAvatarRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DeleteAvatarResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAvatarResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAvatarResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAvatarResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAvatarResponse, self).to_map()
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
            temp_model = DeleteAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DuplexDecisionRequestDialogContextHistories(TeaModel):
    def __init__(self, robot=None, user=None):
        self.robot = robot  # type: str
        self.user = user  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DuplexDecisionRequestDialogContextHistories, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.robot is not None:
            result['Robot'] = self.robot
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Robot') is not None:
            self.robot = m.get('Robot')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class DuplexDecisionRequestDialogContext(TeaModel):
    def __init__(self, cur_utterance_idx=None, histories=None):
        self.cur_utterance_idx = cur_utterance_idx  # type: int
        self.histories = histories  # type: list[DuplexDecisionRequestDialogContextHistories]

    def validate(self):
        if self.histories:
            for k in self.histories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DuplexDecisionRequestDialogContext, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_utterance_idx is not None:
            result['CurUtteranceIdx'] = self.cur_utterance_idx
        result['Histories'] = []
        if self.histories is not None:
            for k in self.histories:
                result['Histories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurUtteranceIdx') is not None:
            self.cur_utterance_idx = m.get('CurUtteranceIdx')
        self.histories = []
        if m.get('Histories') is not None:
            for k in m.get('Histories'):
                temp_model = DuplexDecisionRequestDialogContextHistories()
                self.histories.append(temp_model.from_map(k))
        return self


class DuplexDecisionRequest(TeaModel):
    def __init__(self, app_id=None, biz_request_id=None, call_time=None, custom_keywords=None, dialog_context=None,
                 dialog_status=None, interrupt_type=None, session_id=None, tenant_id=None, text=None):
        self.app_id = app_id  # type: str
        self.biz_request_id = biz_request_id  # type: str
        self.call_time = call_time  # type: int
        self.custom_keywords = custom_keywords  # type: list[str]
        self.dialog_context = dialog_context  # type: DuplexDecisionRequestDialogContext
        self.dialog_status = dialog_status  # type: str
        self.interrupt_type = interrupt_type  # type: int
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str

    def validate(self):
        if self.dialog_context:
            self.dialog_context.validate()

    def to_map(self):
        _map = super(DuplexDecisionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_request_id is not None:
            result['BizRequestId'] = self.biz_request_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.custom_keywords is not None:
            result['CustomKeywords'] = self.custom_keywords
        if self.dialog_context is not None:
            result['DialogContext'] = self.dialog_context.to_map()
        if self.dialog_status is not None:
            result['DialogStatus'] = self.dialog_status
        if self.interrupt_type is not None:
            result['InterruptType'] = self.interrupt_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizRequestId') is not None:
            self.biz_request_id = m.get('BizRequestId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CustomKeywords') is not None:
            self.custom_keywords = m.get('CustomKeywords')
        if m.get('DialogContext') is not None:
            temp_model = DuplexDecisionRequestDialogContext()
            self.dialog_context = temp_model.from_map(m['DialogContext'])
        if m.get('DialogStatus') is not None:
            self.dialog_status = m.get('DialogStatus')
        if m.get('InterruptType') is not None:
            self.interrupt_type = m.get('InterruptType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DuplexDecisionShrinkRequest(TeaModel):
    def __init__(self, app_id=None, biz_request_id=None, call_time=None, custom_keywords_shrink=None,
                 dialog_context_shrink=None, dialog_status=None, interrupt_type=None, session_id=None, tenant_id=None, text=None):
        self.app_id = app_id  # type: str
        self.biz_request_id = biz_request_id  # type: str
        self.call_time = call_time  # type: int
        self.custom_keywords_shrink = custom_keywords_shrink  # type: str
        self.dialog_context_shrink = dialog_context_shrink  # type: str
        self.dialog_status = dialog_status  # type: str
        self.interrupt_type = interrupt_type  # type: int
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DuplexDecisionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.biz_request_id is not None:
            result['BizRequestId'] = self.biz_request_id
        if self.call_time is not None:
            result['CallTime'] = self.call_time
        if self.custom_keywords_shrink is not None:
            result['CustomKeywords'] = self.custom_keywords_shrink
        if self.dialog_context_shrink is not None:
            result['DialogContext'] = self.dialog_context_shrink
        if self.dialog_status is not None:
            result['DialogStatus'] = self.dialog_status
        if self.interrupt_type is not None:
            result['InterruptType'] = self.interrupt_type
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BizRequestId') is not None:
            self.biz_request_id = m.get('BizRequestId')
        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')
        if m.get('CustomKeywords') is not None:
            self.custom_keywords_shrink = m.get('CustomKeywords')
        if m.get('DialogContext') is not None:
            self.dialog_context_shrink = m.get('DialogContext')
        if m.get('DialogStatus') is not None:
            self.dialog_status = m.get('DialogStatus')
        if m.get('InterruptType') is not None:
            self.interrupt_type = m.get('InterruptType')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class DuplexDecisionResponseBodyData(TeaModel):
    def __init__(self, action_type=None, grab_type=None, output_text=None):
        self.action_type = action_type  # type: str
        self.grab_type = grab_type  # type: str
        self.output_text = output_text  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DuplexDecisionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.grab_type is not None:
            result['GrabType'] = self.grab_type
        if self.output_text is not None:
            result['OutputText'] = self.output_text
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('GrabType') is not None:
            self.grab_type = m.get('GrabType')
        if m.get('OutputText') is not None:
            self.output_text = m.get('OutputText')
        return self


class DuplexDecisionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DuplexDecisionResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DuplexDecisionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = DuplexDecisionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DuplexDecisionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DuplexDecisionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DuplexDecisionResponse, self).to_map()
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
            temp_model = DuplexDecisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoTaskInfoRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTaskInfoRequestApp, self).to_map()
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


class GetVideoTaskInfoRequest(TeaModel):
    def __init__(self, app=None, task_uuid=None, tenant_id=None):
        self.app = app  # type: GetVideoTaskInfoRequestApp
        self.task_uuid = task_uuid  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super(GetVideoTaskInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = GetVideoTaskInfoRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVideoTaskInfoShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, task_uuid=None, tenant_id=None):
        self.app_shrink = app_shrink  # type: str
        self.task_uuid = task_uuid  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTaskInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class GetVideoTaskInfoResponseBodyDataTaskResult(TeaModel):
    def __init__(self, alpha_url=None, fail_code=None, fail_reason=None, preview_pic=None, subtitles_url=None,
                 video_duration=None, video_url=None, word_subtitles_url=None):
        self.alpha_url = alpha_url  # type: str
        self.fail_code = fail_code  # type: str
        self.fail_reason = fail_reason  # type: str
        self.preview_pic = preview_pic  # type: str
        self.subtitles_url = subtitles_url  # type: str
        self.video_duration = video_duration  # type: int
        self.video_url = video_url  # type: str
        # 字粒度的时间戳文件，特定任务支持
        self.word_subtitles_url = word_subtitles_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVideoTaskInfoResponseBodyDataTaskResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_url is not None:
            result['AlphaUrl'] = self.alpha_url
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.preview_pic is not None:
            result['PreviewPic'] = self.preview_pic
        if self.subtitles_url is not None:
            result['SubtitlesUrl'] = self.subtitles_url
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.word_subtitles_url is not None:
            result['WordSubtitlesUrl'] = self.word_subtitles_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaUrl') is not None:
            self.alpha_url = m.get('AlphaUrl')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('PreviewPic') is not None:
            self.preview_pic = m.get('PreviewPic')
        if m.get('SubtitlesUrl') is not None:
            self.subtitles_url = m.get('SubtitlesUrl')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('WordSubtitlesUrl') is not None:
            self.word_subtitles_url = m.get('WordSubtitlesUrl')
        return self


class GetVideoTaskInfoResponseBodyData(TeaModel):
    def __init__(self, process=None, status=None, task_result=None, task_uuid=None, type=None):
        self.process = process  # type: str
        self.status = status  # type: str
        self.task_result = task_result  # type: GetVideoTaskInfoResponseBodyDataTaskResult
        self.task_uuid = task_uuid  # type: str
        self.type = type  # type: str

    def validate(self):
        if self.task_result:
            self.task_result.validate()

    def to_map(self):
        _map = super(GetVideoTaskInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.process is not None:
            result['Process'] = self.process
        if self.status is not None:
            result['Status'] = self.status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Process') is not None:
            self.process = m.get('Process')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskResult') is not None:
            temp_model = GetVideoTaskInfoResponseBodyDataTaskResult()
            self.task_result = temp_model.from_map(m['TaskResult'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetVideoTaskInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetVideoTaskInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetVideoTaskInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = GetVideoTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVideoTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVideoTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVideoTaskInfoResponse, self).to_map()
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
            temp_model = GetVideoTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LicenseAuthRequest(TeaModel):
    def __init__(self, app_id=None, license=None, tenant_id=None):
        self.app_id = app_id  # type: str
        self.license = license  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(LicenseAuthRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.license is not None:
            result['License'] = self.license
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class LicenseAuthResponseBodyData(TeaModel):
    def __init__(self, token=None):
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LicenseAuthResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class LicenseAuthResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: LicenseAuthResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(LicenseAuthResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = LicenseAuthResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LicenseAuthResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LicenseAuthResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LicenseAuthResponse, self).to_map()
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
            temp_model = LicenseAuthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvatarRequest(TeaModel):
    def __init__(self, code=None, tenant_id=None):
        self.code = code  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvatarRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryAvatarResponseBodyDataSupportedResolutionsOffline(TeaModel):
    def __init__(self, desc=None, height=None, width=None):
        self.desc = desc  # type: str
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvatarResponseBodyDataSupportedResolutionsOffline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarResponseBodyDataSupportedResolutionsOnline(TeaModel):
    def __init__(self, desc=None, height=None, width=None):
        self.desc = desc  # type: str
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvatarResponseBodyDataSupportedResolutionsOnline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarResponseBodyDataSupportedResolutions(TeaModel):
    def __init__(self, offline=None, online=None):
        self.offline = offline  # type: list[QueryAvatarResponseBodyDataSupportedResolutionsOffline]
        self.online = online  # type: list[QueryAvatarResponseBodyDataSupportedResolutionsOnline]

    def validate(self):
        if self.offline:
            for k in self.offline:
                if k:
                    k.validate()
        if self.online:
            for k in self.online:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAvatarResponseBodyDataSupportedResolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Offline'] = []
        if self.offline is not None:
            for k in self.offline:
                result['Offline'].append(k.to_map() if k else None)
        result['Online'] = []
        if self.online is not None:
            for k in self.online:
                result['Online'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.offline = []
        if m.get('Offline') is not None:
            for k in m.get('Offline'):
                temp_model = QueryAvatarResponseBodyDataSupportedResolutionsOffline()
                self.offline.append(temp_model.from_map(k))
        self.online = []
        if m.get('Online') is not None:
            for k in m.get('Online'):
                temp_model = QueryAvatarResponseBodyDataSupportedResolutionsOnline()
                self.online.append(temp_model.from_map(k))
        return self


class QueryAvatarResponseBodyData(TeaModel):
    def __init__(self, all_locate_images=None, avatar_type=None, description=None, image=None,
                 make_fail_reason=None, make_stage=None, make_status=None, model_type=None, name=None, portrait=None,
                 supported_resolutions=None):
        self.all_locate_images = all_locate_images  # type: dict[str, any]
        self.avatar_type = avatar_type  # type: str
        self.description = description  # type: str
        self.image = image  # type: str
        self.make_fail_reason = make_fail_reason  # type: str
        self.make_stage = make_stage  # type: str
        self.make_status = make_status  # type: str
        self.model_type = model_type  # type: str
        self.name = name  # type: str
        self.portrait = portrait  # type: str
        self.supported_resolutions = supported_resolutions  # type: QueryAvatarResponseBodyDataSupportedResolutions

    def validate(self):
        if self.supported_resolutions:
            self.supported_resolutions.validate()

    def to_map(self):
        _map = super(QueryAvatarResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_locate_images is not None:
            result['AllLocateImages'] = self.all_locate_images
        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.make_fail_reason is not None:
            result['MakeFailReason'] = self.make_fail_reason
        if self.make_stage is not None:
            result['MakeStage'] = self.make_stage
        if self.make_status is not None:
            result['MakeStatus'] = self.make_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.name is not None:
            result['Name'] = self.name
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.supported_resolutions is not None:
            result['SupportedResolutions'] = self.supported_resolutions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllLocateImages') is not None:
            self.all_locate_images = m.get('AllLocateImages')
        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('MakeFailReason') is not None:
            self.make_fail_reason = m.get('MakeFailReason')
        if m.get('MakeStage') is not None:
            self.make_stage = m.get('MakeStage')
        if m.get('MakeStatus') is not None:
            self.make_status = m.get('MakeStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('SupportedResolutions') is not None:
            temp_model = QueryAvatarResponseBodyDataSupportedResolutions()
            self.supported_resolutions = temp_model.from_map(m['SupportedResolutions'])
        return self


class QueryAvatarResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAvatarResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAvatarResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvatarResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAvatarResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAvatarResponse, self).to_map()
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
            temp_model = QueryAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAvatarListRequest(TeaModel):
    def __init__(self, model_type=None, page_no=None, page_size=None, tenant_id=None):
        self.model_type = model_type  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvatarListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryAvatarListResponseBodyDataListSupportedResolutionsOffline(TeaModel):
    def __init__(self, desc=None, height=None, width=None):
        self.desc = desc  # type: str
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvatarListResponseBodyDataListSupportedResolutionsOffline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarListResponseBodyDataListSupportedResolutionsOnline(TeaModel):
    def __init__(self, desc=None, height=None, width=None):
        self.desc = desc  # type: str
        self.height = height  # type: int
        self.width = width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAvatarListResponseBodyDataListSupportedResolutionsOnline, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.height is not None:
            result['Height'] = self.height
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class QueryAvatarListResponseBodyDataListSupportedResolutions(TeaModel):
    def __init__(self, offline=None, online=None):
        self.offline = offline  # type: list[QueryAvatarListResponseBodyDataListSupportedResolutionsOffline]
        self.online = online  # type: list[QueryAvatarListResponseBodyDataListSupportedResolutionsOnline]

    def validate(self):
        if self.offline:
            for k in self.offline:
                if k:
                    k.validate()
        if self.online:
            for k in self.online:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAvatarListResponseBodyDataListSupportedResolutions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Offline'] = []
        if self.offline is not None:
            for k in self.offline:
                result['Offline'].append(k.to_map() if k else None)
        result['Online'] = []
        if self.online is not None:
            for k in self.online:
                result['Online'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.offline = []
        if m.get('Offline') is not None:
            for k in m.get('Offline'):
                temp_model = QueryAvatarListResponseBodyDataListSupportedResolutionsOffline()
                self.offline.append(temp_model.from_map(k))
        self.online = []
        if m.get('Online') is not None:
            for k in m.get('Online'):
                temp_model = QueryAvatarListResponseBodyDataListSupportedResolutionsOnline()
                self.online.append(temp_model.from_map(k))
        return self


class QueryAvatarListResponseBodyDataList(TeaModel):
    def __init__(self, avatar_type=None, code=None, description=None, image=None, make_fail_reason=None,
                 make_stage=None, make_status=None, model_type=None, name=None, portrait=None, supported_resolutions=None):
        self.avatar_type = avatar_type  # type: str
        self.code = code  # type: str
        self.description = description  # type: str
        self.image = image  # type: str
        self.make_fail_reason = make_fail_reason  # type: str
        self.make_stage = make_stage  # type: str
        self.make_status = make_status  # type: str
        self.model_type = model_type  # type: str
        self.name = name  # type: str
        self.portrait = portrait  # type: str
        self.supported_resolutions = supported_resolutions  # type: QueryAvatarListResponseBodyDataListSupportedResolutions

    def validate(self):
        if self.supported_resolutions:
            self.supported_resolutions.validate()

    def to_map(self):
        _map = super(QueryAvatarListResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_type is not None:
            result['AvatarType'] = self.avatar_type
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.make_fail_reason is not None:
            result['MakeFailReason'] = self.make_fail_reason
        if self.make_stage is not None:
            result['MakeStage'] = self.make_stage
        if self.make_status is not None:
            result['MakeStatus'] = self.make_status
        if self.model_type is not None:
            result['ModelType'] = self.model_type
        if self.name is not None:
            result['Name'] = self.name
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.supported_resolutions is not None:
            result['SupportedResolutions'] = self.supported_resolutions.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvatarType') is not None:
            self.avatar_type = m.get('AvatarType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('MakeFailReason') is not None:
            self.make_fail_reason = m.get('MakeFailReason')
        if m.get('MakeStage') is not None:
            self.make_stage = m.get('MakeStage')
        if m.get('MakeStatus') is not None:
            self.make_status = m.get('MakeStatus')
        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('SupportedResolutions') is not None:
            temp_model = QueryAvatarListResponseBodyDataListSupportedResolutions()
            self.supported_resolutions = temp_model.from_map(m['SupportedResolutions'])
        return self


class QueryAvatarListResponseBodyData(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total_count=None, total_page=None):
        self.list = list  # type: list[QueryAvatarListResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: int
        self.total_page = total_page  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAvatarListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryAvatarListResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class QueryAvatarListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAvatarListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAvatarListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryAvatarListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAvatarListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryAvatarListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAvatarListResponse, self).to_map()
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
            temp_model = QueryAvatarListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRunningInstanceRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRunningInstanceRequestApp, self).to_map()
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


class QueryRunningInstanceRequest(TeaModel):
    def __init__(self, app=None, session_id=None, tenant_id=None):
        self.app = app  # type: QueryRunningInstanceRequestApp
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super(QueryRunningInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = QueryRunningInstanceRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRunningInstanceShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, session_id=None, tenant_id=None):
        self.app_shrink = app_shrink  # type: str
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRunningInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryRunningInstanceResponseBodyDataChannel(TeaModel):
    def __init__(self, app_id=None, channel_id=None, expired_time=None, gslb=None, nonce=None, token=None, type=None,
                 user_id=None, user_info_in_channel=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.expired_time = expired_time  # type: str
        self.gslb = gslb  # type: list[str]
        self.nonce = nonce  # type: str
        self.token = token  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.user_info_in_channel = user_info_in_channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRunningInstanceResponseBodyDataChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info_in_channel is not None:
            result['UserInfoInChannel'] = self.user_info_in_channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfoInChannel') is not None:
            self.user_info_in_channel = m.get('UserInfoInChannel')
        return self


class QueryRunningInstanceResponseBodyDataUser(TeaModel):
    def __init__(self, user_id=None, user_name=None):
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRunningInstanceResponseBodyDataUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class QueryRunningInstanceResponseBodyData(TeaModel):
    def __init__(self, channel=None, session_id=None, user=None):
        self.channel = channel  # type: QueryRunningInstanceResponseBodyDataChannel
        self.session_id = session_id  # type: str
        self.user = user  # type: QueryRunningInstanceResponseBodyDataUser

    def validate(self):
        if self.channel:
            self.channel.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(QueryRunningInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = QueryRunningInstanceResponseBodyDataChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('User') is not None:
            temp_model = QueryRunningInstanceResponseBodyDataUser()
            self.user = temp_model.from_map(m['User'])
        return self


class QueryRunningInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[QueryRunningInstanceResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRunningInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
                temp_model = QueryRunningInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRunningInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRunningInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRunningInstanceResponse, self).to_map()
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
            temp_model = QueryRunningInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimedResetOperateStatusRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTimedResetOperateStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTimedResetOperateStatusResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, status=None, status_str=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.status = status  # type: long
        self.status_str = status_str  # type: str
        self.tenant_id = tenant_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTimedResetOperateStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_str is not None:
            result['StatusStr'] = self.status_str
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusStr') is not None:
            self.status_str = m.get('StatusStr')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class QueryTimedResetOperateStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryTimedResetOperateStatusResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTimedResetOperateStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryTimedResetOperateStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimedResetOperateStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTimedResetOperateStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTimedResetOperateStatusResponse, self).to_map()
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
            temp_model = QueryTimedResetOperateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVideoTaskInfoRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVideoTaskInfoRequestApp, self).to_map()
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


class QueryVideoTaskInfoRequest(TeaModel):
    def __init__(self, app=None, order_by_id=None, page_no=None, page_size=None, status=None, task_uuid=None,
                 tenant_id=None, title=None, type=None):
        self.app = app  # type: QueryVideoTaskInfoRequestApp
        self.order_by_id = order_by_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.task_uuid = task_uuid  # type: str
        self.tenant_id = tenant_id  # type: long
        self.title = title  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.app:
            self.app.validate()

    def to_map(self):
        _map = super(QueryVideoTaskInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.order_by_id is not None:
            result['OrderById'] = self.order_by_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = QueryVideoTaskInfoRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('OrderById') is not None:
            self.order_by_id = m.get('OrderById')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryVideoTaskInfoShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, order_by_id=None, page_no=None, page_size=None, status=None, task_uuid=None,
                 tenant_id=None, title=None, type=None):
        self.app_shrink = app_shrink  # type: str
        self.order_by_id = order_by_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.status = status  # type: int
        self.task_uuid = task_uuid  # type: str
        self.tenant_id = tenant_id  # type: long
        self.title = title  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVideoTaskInfoShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.order_by_id is not None:
            result['OrderById'] = self.order_by_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status is not None:
            result['Status'] = self.status
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('OrderById') is not None:
            self.order_by_id = m.get('OrderById')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryVideoTaskInfoResponseBodyDataListTaskResult(TeaModel):
    def __init__(self, alpha_url=None, fail_code=None, fail_reason=None, preview_pic=None, subtitles_url=None,
                 video_duration=None, video_url=None, word_subtitles_url=None):
        self.alpha_url = alpha_url  # type: str
        self.fail_code = fail_code  # type: str
        self.fail_reason = fail_reason  # type: str
        self.preview_pic = preview_pic  # type: str
        self.subtitles_url = subtitles_url  # type: str
        self.video_duration = video_duration  # type: int
        self.video_url = video_url  # type: str
        self.word_subtitles_url = word_subtitles_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVideoTaskInfoResponseBodyDataListTaskResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_url is not None:
            result['AlphaUrl'] = self.alpha_url
        if self.fail_code is not None:
            result['FailCode'] = self.fail_code
        if self.fail_reason is not None:
            result['FailReason'] = self.fail_reason
        if self.preview_pic is not None:
            result['PreviewPic'] = self.preview_pic
        if self.subtitles_url is not None:
            result['SubtitlesUrl'] = self.subtitles_url
        if self.video_duration is not None:
            result['VideoDuration'] = self.video_duration
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.word_subtitles_url is not None:
            result['WordSubtitlesUrl'] = self.word_subtitles_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaUrl') is not None:
            self.alpha_url = m.get('AlphaUrl')
        if m.get('FailCode') is not None:
            self.fail_code = m.get('FailCode')
        if m.get('FailReason') is not None:
            self.fail_reason = m.get('FailReason')
        if m.get('PreviewPic') is not None:
            self.preview_pic = m.get('PreviewPic')
        if m.get('SubtitlesUrl') is not None:
            self.subtitles_url = m.get('SubtitlesUrl')
        if m.get('VideoDuration') is not None:
            self.video_duration = m.get('VideoDuration')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('WordSubtitlesUrl') is not None:
            self.word_subtitles_url = m.get('WordSubtitlesUrl')
        return self


class QueryVideoTaskInfoResponseBodyDataList(TeaModel):
    def __init__(self, status=None, task_result=None, task_uuid=None, title=None, type=None):
        self.status = status  # type: int
        self.task_result = task_result  # type: QueryVideoTaskInfoResponseBodyDataListTaskResult
        self.task_uuid = task_uuid  # type: str
        self.title = title  # type: str
        self.type = type  # type: int

    def validate(self):
        if self.task_result:
            self.task_result.validate()

    def to_map(self):
        _map = super(QueryVideoTaskInfoResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.task_result is not None:
            result['TaskResult'] = self.task_result.to_map()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskResult') is not None:
            temp_model = QueryVideoTaskInfoResponseBodyDataListTaskResult()
            self.task_result = temp_model.from_map(m['TaskResult'])
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryVideoTaskInfoResponseBodyData(TeaModel):
    def __init__(self, list=None, page_no=None, page_size=None, total_count=None):
        self.list = list  # type: list[QueryVideoTaskInfoResponseBodyDataList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total_count = total_count  # type: long

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryVideoTaskInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryVideoTaskInfoResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryVideoTaskInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryVideoTaskInfoResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryVideoTaskInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = QueryVideoTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVideoTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryVideoTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVideoTaskInfoResponse, self).to_map()
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
            temp_model = QueryVideoTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Render3dAvatarRequest(TeaModel):
    def __init__(self, app_id=None, code=None, tenant_id=None):
        self.app_id = app_id  # type: str
        self.code = code  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(Render3dAvatarRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.code is not None:
            result['Code'] = self.code
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class Render3dAvatarResponseBodyData(TeaModel):
    def __init__(self, render_data=None):
        self.render_data = render_data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Render3dAvatarResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.render_data is not None:
            result['RenderData'] = self.render_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenderData') is not None:
            self.render_data = m.get('RenderData')
        return self


class Render3dAvatarResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: Render3dAvatarResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(Render3dAvatarResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = Render3dAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class Render3dAvatarResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Render3dAvatarResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Render3dAvatarResponse, self).to_map()
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
            temp_model = Render3dAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCommandRequest(TeaModel):
    def __init__(self, code=None, content=None, feedback=None, session_id=None, tenant_id=None, unique_code=None):
        self.code = code  # type: str
        self.content = content  # type: dict[str, any]
        self.feedback = feedback  # type: bool
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.unique_code = unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendCommandShrinkRequest(TeaModel):
    def __init__(self, code=None, content_shrink=None, feedback=None, session_id=None, tenant_id=None,
                 unique_code=None):
        self.code = code  # type: str
        self.content_shrink = content_shrink  # type: str
        self.feedback = feedback  # type: bool
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.unique_code = unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommandShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content_shrink is not None:
            result['Content'] = self.content_shrink
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendCommandResponseBodyData(TeaModel):
    def __init__(self, session_id=None, unique_code=None):
        self.session_id = session_id  # type: str
        self.unique_code = unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendCommandResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendCommandResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendCommandResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendCommandResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SendCommandResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendCommandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendCommandResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendCommandResponse, self).to_map()
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
            temp_model = SendCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequestStreamExtension(TeaModel):
    def __init__(self, index=None, is_stream=None, position=None):
        self.index = index  # type: int
        self.is_stream = is_stream  # type: bool
        self.position = position  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequestStreamExtension, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.is_stream is not None:
            result['IsStream'] = self.is_stream
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('IsStream') is not None:
            self.is_stream = m.get('IsStream')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class SendMessageRequestTextRequest(TeaModel):
    def __init__(self, command_type=None, id=None, speech_text=None, interrupt=None):
        self.command_type = command_type  # type: str
        self.id = id  # type: str
        self.speech_text = speech_text  # type: str
        self.interrupt = interrupt  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequestTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_type is not None:
            result['CommandType'] = self.command_type
        if self.id is not None:
            result['Id'] = self.id
        if self.speech_text is not None:
            result['SpeechText'] = self.speech_text
        if self.interrupt is not None:
            result['interrupt'] = self.interrupt
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpeechText') is not None:
            self.speech_text = m.get('SpeechText')
        if m.get('interrupt') is not None:
            self.interrupt = m.get('interrupt')
        return self


class SendMessageRequestVAMLRequest(TeaModel):
    def __init__(self, code=None, vaml=None):
        self.code = code  # type: str
        self.vaml = vaml  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequestVAMLRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.vaml is not None:
            result['Vaml'] = self.vaml
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Vaml') is not None:
            self.vaml = m.get('Vaml')
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, feedback=None, session_id=None, stream_extension=None, tenant_id=None, text_request=None,
                 vamlrequest=None):
        self.feedback = feedback  # type: bool
        self.session_id = session_id  # type: str
        self.stream_extension = stream_extension  # type: SendMessageRequestStreamExtension
        self.tenant_id = tenant_id  # type: long
        self.text_request = text_request  # type: SendMessageRequestTextRequest
        self.vamlrequest = vamlrequest  # type: SendMessageRequestVAMLRequest

    def validate(self):
        if self.stream_extension:
            self.stream_extension.validate()
        if self.text_request:
            self.text_request.validate()
        if self.vamlrequest:
            self.vamlrequest.validate()

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension is not None:
            result['StreamExtension'] = self.stream_extension.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request is not None:
            result['TextRequest'] = self.text_request.to_map()
        if self.vamlrequest is not None:
            result['VAMLRequest'] = self.vamlrequest.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            temp_model = SendMessageRequestStreamExtension()
            self.stream_extension = temp_model.from_map(m['StreamExtension'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            temp_model = SendMessageRequestTextRequest()
            self.text_request = temp_model.from_map(m['TextRequest'])
        if m.get('VAMLRequest') is not None:
            temp_model = SendMessageRequestVAMLRequest()
            self.vamlrequest = temp_model.from_map(m['VAMLRequest'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(self, feedback=None, session_id=None, stream_extension_shrink=None, tenant_id=None,
                 text_request_shrink=None, vamlrequest_shrink=None):
        self.feedback = feedback  # type: bool
        self.session_id = session_id  # type: str
        self.stream_extension_shrink = stream_extension_shrink  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text_request_shrink = text_request_shrink  # type: str
        self.vamlrequest_shrink = vamlrequest_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension_shrink is not None:
            result['StreamExtension'] = self.stream_extension_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request_shrink is not None:
            result['TextRequest'] = self.text_request_shrink
        if self.vamlrequest_shrink is not None:
            result['VAMLRequest'] = self.vamlrequest_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            self.stream_extension_shrink = m.get('StreamExtension')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            self.text_request_shrink = m.get('TextRequest')
        if m.get('VAMLRequest') is not None:
            self.vamlrequest_shrink = m.get('VAMLRequest')
        return self


class SendMessageResponseBodyData(TeaModel):
    def __init__(self, request_id=None, session_id=None):
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, success=None):
        # Id of the request
        self.code = code  # type: str
        self.data = data  # type: SendMessageResponseBodyData
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = SendMessageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendTextRequestStreamExtension(TeaModel):
    def __init__(self, index=None, is_stream=None, position=None):
        self.index = index  # type: int
        self.is_stream = is_stream  # type: bool
        self.position = position  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTextRequestStreamExtension, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.index is not None:
            result['Index'] = self.index
        if self.is_stream is not None:
            result['IsStream'] = self.is_stream
        if self.position is not None:
            result['Position'] = self.position
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('IsStream') is not None:
            self.is_stream = m.get('IsStream')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        return self


class SendTextRequest(TeaModel):
    def __init__(self, feedback=None, interrupt=None, session_id=None, stream_extension=None, tenant_id=None,
                 text=None, unique_code=None):
        self.feedback = feedback  # type: bool
        self.interrupt = interrupt  # type: bool
        self.session_id = session_id  # type: str
        self.stream_extension = stream_extension  # type: SendTextRequestStreamExtension
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str
        self.unique_code = unique_code  # type: str

    def validate(self):
        if self.stream_extension:
            self.stream_extension.validate()

    def to_map(self):
        _map = super(SendTextRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension is not None:
            result['StreamExtension'] = self.stream_extension.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            temp_model = SendTextRequestStreamExtension()
            self.stream_extension = temp_model.from_map(m['StreamExtension'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendTextShrinkRequest(TeaModel):
    def __init__(self, feedback=None, interrupt=None, session_id=None, stream_extension_shrink=None, tenant_id=None,
                 text=None, unique_code=None):
        self.feedback = feedback  # type: bool
        self.interrupt = interrupt  # type: bool
        self.session_id = session_id  # type: str
        self.stream_extension_shrink = stream_extension_shrink  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str
        self.unique_code = unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTextShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feedback is not None:
            result['Feedback'] = self.feedback
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.stream_extension_shrink is not None:
            result['StreamExtension'] = self.stream_extension_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Feedback') is not None:
            self.feedback = m.get('Feedback')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StreamExtension') is not None:
            self.stream_extension_shrink = m.get('StreamExtension')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendTextResponseBodyData(TeaModel):
    def __init__(self, session_id=None, unique_code=None):
        self.session_id = session_id  # type: str
        self.unique_code = unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendTextResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendTextResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendTextResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendTextResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SendTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendTextResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendTextResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendTextResponse, self).to_map()
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
            temp_model = SendTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendVamlRequest(TeaModel):
    def __init__(self, session_id=None, tenant_id=None, vaml=None):
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.vaml = vaml  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVamlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vaml is not None:
            result['Vaml'] = self.vaml
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Vaml') is not None:
            self.vaml = m.get('Vaml')
        return self


class SendVamlResponseBodyData(TeaModel):
    def __init__(self, session_id=None, unique_code=None):
        self.session_id = session_id  # type: str
        self.unique_code = unique_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendVamlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.unique_code is not None:
            result['UniqueCode'] = self.unique_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('UniqueCode') is not None:
            self.unique_code = m.get('UniqueCode')
        return self


class SendVamlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SendVamlResponseBodyData
        self.message = message  # type: str
        # Id of the request
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SendVamlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SendVamlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SendVamlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendVamlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendVamlResponse, self).to_map()
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
            temp_model = SendVamlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequestApp, self).to_map()
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


class StartInstanceRequestChannel(TeaModel):
    def __init__(self, req_config=None, type=None):
        self.req_config = req_config  # type: dict[str, any]
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequestChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.req_config is not None:
            result['ReqConfig'] = self.req_config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReqConfig') is not None:
            self.req_config = m.get('ReqConfig')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class StartInstanceRequestCommandRequest(TeaModel):
    def __init__(self, alpha_switch=None):
        self.alpha_switch = alpha_switch  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequestCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_switch is not None:
            result['AlphaSwitch'] = self.alpha_switch
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaSwitch') is not None:
            self.alpha_switch = m.get('AlphaSwitch')
        return self


class StartInstanceRequestUser(TeaModel):
    def __init__(self, user_id=None, user_name=None):
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequestUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, app=None, channel=None, command_request=None, tenant_id=None, user=None):
        self.app = app  # type: StartInstanceRequestApp
        self.channel = channel  # type: StartInstanceRequestChannel
        self.command_request = command_request  # type: StartInstanceRequestCommandRequest
        self.tenant_id = tenant_id  # type: long
        self.user = user  # type: StartInstanceRequestUser

    def validate(self):
        if self.app:
            self.app.validate()
        if self.channel:
            self.channel.validate()
        if self.command_request:
            self.command_request.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(StartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.command_request is not None:
            result['CommandRequest'] = self.command_request.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = StartInstanceRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('Channel') is not None:
            temp_model = StartInstanceRequestChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('CommandRequest') is not None:
            temp_model = StartInstanceRequestCommandRequest()
            self.command_request = temp_model.from_map(m['CommandRequest'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            temp_model = StartInstanceRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class StartInstanceShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, channel_shrink=None, command_request_shrink=None, tenant_id=None,
                 user_shrink=None):
        self.app_shrink = app_shrink  # type: str
        self.channel_shrink = channel_shrink  # type: str
        self.command_request_shrink = command_request_shrink  # type: str
        self.tenant_id = tenant_id  # type: long
        self.user_shrink = user_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.channel_shrink is not None:
            result['Channel'] = self.channel_shrink
        if self.command_request_shrink is not None:
            result['CommandRequest'] = self.command_request_shrink
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('Channel') is not None:
            self.channel_shrink = m.get('Channel')
        if m.get('CommandRequest') is not None:
            self.command_request_shrink = m.get('CommandRequest')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            self.user_shrink = m.get('User')
        return self


class StartInstanceResponseBodyDataChannel(TeaModel):
    def __init__(self, app_id=None, channel_id=None, expired_time=None, gslb=None, nonce=None, token=None, type=None,
                 user_id=None, user_info_in_channel=None):
        self.app_id = app_id  # type: str
        self.channel_id = channel_id  # type: str
        self.expired_time = expired_time  # type: str
        self.gslb = gslb  # type: list[str]
        self.nonce = nonce  # type: str
        self.token = token  # type: str
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.user_info_in_channel = user_info_in_channel  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBodyDataChannel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.gslb is not None:
            result['Gslb'] = self.gslb
        if self.nonce is not None:
            result['Nonce'] = self.nonce
        if self.token is not None:
            result['Token'] = self.token
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_info_in_channel is not None:
            result['UserInfoInChannel'] = self.user_info_in_channel
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Gslb') is not None:
            self.gslb = m.get('Gslb')
        if m.get('Nonce') is not None:
            self.nonce = m.get('Nonce')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserInfoInChannel') is not None:
            self.user_info_in_channel = m.get('UserInfoInChannel')
        return self


class StartInstanceResponseBodyData(TeaModel):
    def __init__(self, channel=None, request_id=None, session_id=None, token=None):
        self.channel = channel  # type: StartInstanceResponseBodyDataChannel
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str
        self.token = token  # type: str

    def validate(self):
        if self.channel:
            self.channel.validate()

    def to_map(self):
        _map = super(StartInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Channel') is not None:
            temp_model = StartInstanceResponseBodyDataChannel()
            self.channel = temp_model.from_map(m['Channel'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: StartInstanceResponseBodyData
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StartInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartInstanceResponse, self).to_map()
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartTimedResetOperateRequest(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTimedResetOperateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StartTimedResetOperateResponseBodyData(TeaModel):
    def __init__(self, instance_id=None, tenant_id=None):
        self.instance_id = instance_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartTimedResetOperateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StartTimedResetOperateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: StartTimedResetOperateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StartTimedResetOperateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = StartTimedResetOperateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartTimedResetOperateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartTimedResetOperateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartTimedResetOperateResponse, self).to_map()
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
            temp_model = StartTimedResetOperateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInstanceRequest(TeaModel):
    def __init__(self, session_id=None, tenant_id=None):
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class StopInstanceResponseBodyData(TeaModel):
    def __init__(self, request_id=None, session_id=None):
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class StopInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: StopInstanceResponseBodyData
        self.message = message  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(StopInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = StopInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopInstanceResponse, self).to_map()
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
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioTo2DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskRequestApp, self).to_map()
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


class SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(self, code=None):
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(self, alpha_format=None, background_image_url=None, is_alpha=None, resolution=None):
        self.alpha_format = alpha_format  # type: int
        self.background_image_url = background_image_url  # type: str
        self.is_alpha = is_alpha  # type: bool
        self.resolution = resolution  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class SubmitAudioTo2DAvatarVideoTaskRequest(TeaModel):
    def __init__(self, app=None, avatar_info=None, callback=None, callback_params=None, ext_params=None,
                 tenant_id=None, title=None, url=None, video_info=None):
        self.app = app  # type: SubmitAudioTo2DAvatarVideoTaskRequestApp
        self.avatar_info = avatar_info  # type: SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.title = title  # type: str
        self.url = url  # type: str
        self.video_info = video_info  # type: SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo

    def validate(self):
        if self.app:
            self.app.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitAudioTo2DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitAudioTo2DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, avatar_info_shrink=None, callback=None, callback_params=None,
                 ext_params=None, tenant_id=None, title=None, url=None, video_info_shrink=None):
        self.app_shrink = app_shrink  # type: str
        self.avatar_info_shrink = avatar_info_shrink  # type: str
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.title = title  # type: str
        self.url = url  # type: str
        self.video_info_shrink = video_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitAudioTo2DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(self, task_uuid=None):
        self.task_uuid = task_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitAudioTo2DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitAudioTo2DAvatarVideoTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SubmitAudioTo2DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitAudioTo2DAvatarVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAudioTo2DAvatarVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAudioTo2DAvatarVideoTaskResponse, self).to_map()
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
            temp_model = SubmitAudioTo2DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAudioTo3DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskRequestApp, self).to_map()
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


class SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(self, angle=None, code=None, industry_code=None, locate=None):
        self.angle = angle  # type: int
        self.code = code  # type: str
        self.industry_code = industry_code  # type: str
        self.locate = locate  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.code is not None:
            result['Code'] = self.code
        if self.industry_code is not None:
            result['IndustryCode'] = self.industry_code
        if self.locate is not None:
            result['Locate'] = self.locate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IndustryCode') is not None:
            self.industry_code = m.get('IndustryCode')
        if m.get('Locate') is not None:
            self.locate = m.get('Locate')
        return self


class SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(self, alpha_format=None, background_image_url=None, is_alpha=None, resolution=None):
        self.alpha_format = alpha_format  # type: int
        self.background_image_url = background_image_url  # type: str
        self.is_alpha = is_alpha  # type: bool
        self.resolution = resolution  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        return self


class SubmitAudioTo3DAvatarVideoTaskRequest(TeaModel):
    def __init__(self, app=None, avatar_info=None, callback=None, callback_params=None, ext_params=None,
                 tenant_id=None, title=None, url=None, video_info=None):
        self.app = app  # type: SubmitAudioTo3DAvatarVideoTaskRequestApp
        self.avatar_info = avatar_info  # type: SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.title = title  # type: str
        self.url = url  # type: str
        self.video_info = video_info  # type: SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo

    def validate(self):
        if self.app:
            self.app.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitAudioTo3DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitAudioTo3DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, avatar_info_shrink=None, callback=None, callback_params=None,
                 ext_params=None, tenant_id=None, title=None, url=None, video_info_shrink=None):
        self.app_shrink = app_shrink  # type: str
        self.avatar_info_shrink = avatar_info_shrink  # type: str
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.title = title  # type: str
        self.url = url  # type: str
        self.video_info_shrink = video_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitAudioTo3DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(self, task_uuid=None):
        self.task_uuid = task_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitAudioTo3DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitAudioTo3DAvatarVideoTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SubmitAudioTo3DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitAudioTo3DAvatarVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitAudioTo3DAvatarVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitAudioTo3DAvatarVideoTaskResponse, self).to_map()
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
            temp_model = SubmitAudioTo3DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextTo2DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskRequestApp, self).to_map()
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


class SubmitTextTo2DAvatarVideoTaskRequestAudioInfo(TeaModel):
    def __init__(self, pitch_rate=None, speech_rate=None, voice=None, volume=None):
        self.pitch_rate = pitch_rate  # type: int
        self.speech_rate = speech_rate  # type: int
        self.voice = voice  # type: str
        self.volume = volume  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskRequestAudioInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(self, code=None):
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class SubmitTextTo2DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(self, alpha_format=None, background_image_url=None, is_alpha=None, is_subtitles=None,
                 resolution=None, subtitle_embedded=None):
        self.alpha_format = alpha_format  # type: int
        self.background_image_url = background_image_url  # type: str
        self.is_alpha = is_alpha  # type: bool
        self.is_subtitles = is_subtitles  # type: bool
        self.resolution = resolution  # type: int
        self.subtitle_embedded = subtitle_embedded  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskRequestVideoInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.subtitle_embedded is not None:
            result['SubtitleEmbedded'] = self.subtitle_embedded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SubtitleEmbedded') is not None:
            self.subtitle_embedded = m.get('SubtitleEmbedded')
        return self


class SubmitTextTo2DAvatarVideoTaskRequest(TeaModel):
    def __init__(self, app=None, audio_info=None, avatar_info=None, callback=None, callback_params=None,
                 ext_params=None, tenant_id=None, text=None, title=None, video_info=None):
        self.app = app  # type: SubmitTextTo2DAvatarVideoTaskRequestApp
        self.audio_info = audio_info  # type: SubmitTextTo2DAvatarVideoTaskRequestAudioInfo
        self.avatar_info = avatar_info  # type: SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str
        self.title = title  # type: str
        self.video_info = video_info  # type: SubmitTextTo2DAvatarVideoTaskRequestVideoInfo

    def validate(self):
        if self.app:
            self.app.validate()
        if self.audio_info:
            self.audio_info.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.audio_info is not None:
            result['AudioInfo'] = self.audio_info.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AudioInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestAudioInfo()
            self.audio_info = temp_model.from_map(m['AudioInfo'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextTo2DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextTo2DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, audio_info_shrink=None, avatar_info_shrink=None, callback=None,
                 callback_params=None, ext_params=None, tenant_id=None, text=None, title=None, video_info_shrink=None):
        self.app_shrink = app_shrink  # type: str
        self.audio_info_shrink = audio_info_shrink  # type: str
        self.avatar_info_shrink = avatar_info_shrink  # type: str
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str
        self.title = title  # type: str
        self.video_info_shrink = video_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.audio_info_shrink is not None:
            result['AudioInfo'] = self.audio_info_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AudioInfo') is not None:
            self.audio_info_shrink = m.get('AudioInfo')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextTo2DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(self, task_uuid=None):
        self.task_uuid = task_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextTo2DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitTextTo2DAvatarVideoTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SubmitTextTo2DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextTo2DAvatarVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTextTo2DAvatarVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTextTo2DAvatarVideoTaskResponse, self).to_map()
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
            temp_model = SubmitTextTo2DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTextTo3DAvatarVideoTaskRequestApp(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskRequestApp, self).to_map()
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


class SubmitTextTo3DAvatarVideoTaskRequestAudioInfo(TeaModel):
    def __init__(self, pitch_rate=None, speech_rate=None, voice=None, volume=None):
        self.pitch_rate = pitch_rate  # type: int
        self.speech_rate = speech_rate  # type: int
        self.voice = voice  # type: str
        self.volume = volume  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskRequestAudioInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pitch_rate is not None:
            result['PitchRate'] = self.pitch_rate
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PitchRate') is not None:
            self.pitch_rate = m.get('PitchRate')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo(TeaModel):
    def __init__(self, angle=None, code=None, industry_code=None, locate=None):
        self.angle = angle  # type: int
        self.code = code  # type: str
        self.industry_code = industry_code  # type: str
        self.locate = locate  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.angle is not None:
            result['Angle'] = self.angle
        if self.code is not None:
            result['Code'] = self.code
        if self.industry_code is not None:
            result['IndustryCode'] = self.industry_code
        if self.locate is not None:
            result['Locate'] = self.locate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Angle') is not None:
            self.angle = m.get('Angle')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IndustryCode') is not None:
            self.industry_code = m.get('IndustryCode')
        if m.get('Locate') is not None:
            self.locate = m.get('Locate')
        return self


class SubmitTextTo3DAvatarVideoTaskRequestVideoInfo(TeaModel):
    def __init__(self, alpha_format=None, background_image_url=None, is_alpha=None, is_subtitles=None,
                 resolution=None, subtitle_embedded=None):
        self.alpha_format = alpha_format  # type: int
        self.background_image_url = background_image_url  # type: str
        self.is_alpha = is_alpha  # type: bool
        self.is_subtitles = is_subtitles  # type: bool
        self.resolution = resolution  # type: int
        self.subtitle_embedded = subtitle_embedded  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskRequestVideoInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpha_format is not None:
            result['AlphaFormat'] = self.alpha_format
        if self.background_image_url is not None:
            result['BackgroundImageUrl'] = self.background_image_url
        if self.is_alpha is not None:
            result['IsAlpha'] = self.is_alpha
        if self.is_subtitles is not None:
            result['IsSubtitles'] = self.is_subtitles
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.subtitle_embedded is not None:
            result['SubtitleEmbedded'] = self.subtitle_embedded
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlphaFormat') is not None:
            self.alpha_format = m.get('AlphaFormat')
        if m.get('BackgroundImageUrl') is not None:
            self.background_image_url = m.get('BackgroundImageUrl')
        if m.get('IsAlpha') is not None:
            self.is_alpha = m.get('IsAlpha')
        if m.get('IsSubtitles') is not None:
            self.is_subtitles = m.get('IsSubtitles')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('SubtitleEmbedded') is not None:
            self.subtitle_embedded = m.get('SubtitleEmbedded')
        return self


class SubmitTextTo3DAvatarVideoTaskRequest(TeaModel):
    def __init__(self, app=None, audio_info=None, avatar_info=None, callback=None, callback_params=None,
                 ext_params=None, tenant_id=None, text=None, title=None, video_info=None):
        self.app = app  # type: SubmitTextTo3DAvatarVideoTaskRequestApp
        self.audio_info = audio_info  # type: SubmitTextTo3DAvatarVideoTaskRequestAudioInfo
        self.avatar_info = avatar_info  # type: SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str
        self.title = title  # type: str
        self.video_info = video_info  # type: SubmitTextTo3DAvatarVideoTaskRequestVideoInfo

    def validate(self):
        if self.app:
            self.app.validate()
        if self.audio_info:
            self.audio_info.validate()
        if self.avatar_info:
            self.avatar_info.validate()
        if self.video_info:
            self.video_info.validate()

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
        if self.audio_info is not None:
            result['AudioInfo'] = self.audio_info.to_map()
        if self.avatar_info is not None:
            result['AvatarInfo'] = self.avatar_info.to_map()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info is not None:
            result['VideoInfo'] = self.video_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestApp()
            self.app = temp_model.from_map(m['App'])
        if m.get('AudioInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestAudioInfo()
            self.audio_info = temp_model.from_map(m['AudioInfo'])
        if m.get('AvatarInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestAvatarInfo()
            self.avatar_info = temp_model.from_map(m['AvatarInfo'])
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            temp_model = SubmitTextTo3DAvatarVideoTaskRequestVideoInfo()
            self.video_info = temp_model.from_map(m['VideoInfo'])
        return self


class SubmitTextTo3DAvatarVideoTaskShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, audio_info_shrink=None, avatar_info_shrink=None, callback=None,
                 callback_params=None, ext_params=None, tenant_id=None, text=None, title=None, video_info_shrink=None):
        self.app_shrink = app_shrink  # type: str
        self.audio_info_shrink = audio_info_shrink  # type: str
        self.avatar_info_shrink = avatar_info_shrink  # type: str
        self.callback = callback  # type: bool
        self.callback_params = callback_params  # type: str
        self.ext_params = ext_params  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text = text  # type: str
        self.title = title  # type: str
        self.video_info_shrink = video_info_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_shrink is not None:
            result['App'] = self.app_shrink
        if self.audio_info_shrink is not None:
            result['AudioInfo'] = self.audio_info_shrink
        if self.avatar_info_shrink is not None:
            result['AvatarInfo'] = self.avatar_info_shrink
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.callback_params is not None:
            result['CallbackParams'] = self.callback_params
        if self.ext_params is not None:
            result['ExtParams'] = self.ext_params
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.video_info_shrink is not None:
            result['VideoInfo'] = self.video_info_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
        if m.get('AudioInfo') is not None:
            self.audio_info_shrink = m.get('AudioInfo')
        if m.get('AvatarInfo') is not None:
            self.avatar_info_shrink = m.get('AvatarInfo')
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('CallbackParams') is not None:
            self.callback_params = m.get('CallbackParams')
        if m.get('ExtParams') is not None:
            self.ext_params = m.get('ExtParams')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('VideoInfo') is not None:
            self.video_info_shrink = m.get('VideoInfo')
        return self


class SubmitTextTo3DAvatarVideoTaskResponseBodyData(TeaModel):
    def __init__(self, task_uuid=None):
        self.task_uuid = task_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_uuid is not None:
            result['TaskUuid'] = self.task_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskUuid') is not None:
            self.task_uuid = m.get('TaskUuid')
        return self


class SubmitTextTo3DAvatarVideoTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: SubmitTextTo3DAvatarVideoTaskResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = SubmitTextTo3DAvatarVideoTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTextTo3DAvatarVideoTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SubmitTextTo3DAvatarVideoTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SubmitTextTo3DAvatarVideoTaskResponse, self).to_map()
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
            temp_model = SubmitTextTo3DAvatarVideoTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class Update2dAvatarRequest(TeaModel):
    def __init__(self, callback=None, code=None, description=None, image=None, name=None, orientation=None,
                 portrait=None, tenant_id=None, transparent=None, video=None):
        self.callback = callback  # type: bool
        self.code = code  # type: str
        self.description = description  # type: str
        self.image = image  # type: str
        self.name = name  # type: str
        self.orientation = orientation  # type: int
        self.portrait = portrait  # type: str
        self.tenant_id = tenant_id  # type: long
        self.transparent = transparent  # type: bool
        self.video = video  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Update2dAvatarRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.code is not None:
            result['Code'] = self.code
        if self.description is not None:
            result['Description'] = self.description
        if self.image is not None:
            result['Image'] = self.image
        if self.name is not None:
            result['Name'] = self.name
        if self.orientation is not None:
            result['Orientation'] = self.orientation
        if self.portrait is not None:
            result['Portrait'] = self.portrait
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.transparent is not None:
            result['Transparent'] = self.transparent
        if self.video is not None:
            result['Video'] = self.video
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Image') is not None:
            self.image = m.get('Image')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Orientation') is not None:
            self.orientation = m.get('Orientation')
        if m.get('Portrait') is not None:
            self.portrait = m.get('Portrait')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('Transparent') is not None:
            self.transparent = m.get('Transparent')
        if m.get('Video') is not None:
            self.video = m.get('Video')
        return self


class Update2dAvatarResponseBodyData(TeaModel):
    def __init__(self, code=None):
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(Update2dAvatarResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class Update2dAvatarResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: Update2dAvatarResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(Update2dAvatarResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
            temp_model = Update2dAvatarResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class Update2dAvatarResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: Update2dAvatarResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(Update2dAvatarResponse, self).to_map()
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
            temp_model = Update2dAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


