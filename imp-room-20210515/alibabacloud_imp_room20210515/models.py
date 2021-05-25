# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GetLoginTokenRequestRequestParams(TeaModel):
    def __init__(self, app_uid=None, app_key=None, device_id=None):
        # 用户ID
        self.app_uid = app_uid  # type: str
        # AppKey
        self.app_key = app_key  # type: str
        # 设备ID
        self.device_id = device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenRequestRequestParams, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(self, app_id=None, request_params=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params = request_params  # type: GetLoginTokenRequestRequestParams

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super(GetLoginTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetLoginTokenRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetLoginTokenShrinkRequest(TeaModel):
    def __init__(self, app_id=None, request_params_shrink=None):
        # AppId
        self.app_id = app_id  # type: str
        self.request_params_shrink = request_params_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetLoginTokenResponseBodyResult(TeaModel):
    def __init__(self, access_token=None, refresh_token=None, access_token_expired_time=None):
        # 登录Tokon
        self.access_token = access_token  # type: str
        # 更新Token
        self.refresh_token = refresh_token  # type: str
        # 登录Token过期时间
        self.access_token_expired_time = access_token_expired_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoginTokenResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, code=None, message=None, result=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.code = code  # type: str
        self.message = message  # type: str
        self.result = result  # type: GetLoginTokenResponseBodyResult

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(GetLoginTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetLoginTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetLoginTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLoginTokenResponse, self).to_map()
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequestRequest(TeaModel):
    def __init__(self, domain=None, biz_type=None, template_id=None, room_id=None, title=None, notice=None,
                 owner_id=None, extension=None):
        # 租户名
        self.domain = domain  # type: str
        # 业务类型
        self.biz_type = biz_type  # type: str
        # 模板id
        self.template_id = template_id  # type: str
        # 房间id
        self.room_id = room_id  # type: str
        # 房间标题
        self.title = title  # type: str
        # 房间公告
        self.notice = notice  # type: str
        # 房主id
        self.owner_id = owner_id  # type: str
        # 拓展字段
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateRoomRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: CreateRoomRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(CreateRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateRoomResponseBodyResult(TeaModel):
    def __init__(self, room_id=None):
        # 房间id
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRoomResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, response_success=None, error_code=None, error_msg=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateRoomResponseBodyResult
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateRoomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CreateRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRoomResponse, self).to_map()
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyRoomRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None):
        # 租户名
        self.domain = domain  # type: str
        # 房间id
        self.room_id = room_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyRoomRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class DestroyRoomRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: DestroyRoomRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(DestroyRoomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = DestroyRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class DestroyRoomResponseBody(TeaModel):
    def __init__(self, request_id=None, response_success=None, error_code=None, error_msg=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DestroyRoomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class DestroyRoomResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DestroyRoomResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DestroyRoomResponse, self).to_map()
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
            temp_model = DestroyRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestRequest(TeaModel):
    def __init__(self, domain=None, room_id=None, plugin_id=None, extension=None):
        # 租户名
        self.domain = domain  # type: str
        # 房间id
        self.room_id = room_id  # type: str
        # 插件ID
        self.plugin_id = plugin_id  # type: str
        # 拓展字段
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(self, request=None):
        self.request = request  # type: CreateInstanceRequestRequest

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateInstanceRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateInstanceResponseBodyResult(TeaModel):
    def __init__(self, instance_id=None, extension=None):
        # 插件实例ID
        self.instance_id = instance_id  # type: str
        # 扩展信息
        self.extension = extension  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBodyResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None, response_success=None, error_code=None, error_msg=None):
        # Id of the request
        self.request_id = request_id  # type: str
        self.result = result  # type: CreateInstanceResponseBodyResult
        self.response_success = response_success  # type: bool
        # 错误码
        self.error_code = error_code  # type: str
        # 错误信息
        self.error_msg = error_msg  # type: str

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateInstanceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
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
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


