# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class SendMessageRequestTextRequest(TeaModel):
    def __init__(self, command_type=None, id=None, speech_text=None):
        self.command_type = command_type  # type: str
        self.id = id  # type: str
        self.speech_text = speech_text  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandType') is not None:
            self.command_type = m.get('CommandType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpeechText') is not None:
            self.speech_text = m.get('SpeechText')
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, session_id=None, tenant_id=None, text_request=None):
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text_request = text_request  # type: SendMessageRequestTextRequest

    def validate(self):
        if self.text_request:
            self.text_request.validate()

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request is not None:
            result['TextRequest'] = self.text_request.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            temp_model = SendMessageRequestTextRequest()
            self.text_request = temp_model.from_map(m['TextRequest'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(self, session_id=None, tenant_id=None, text_request_shrink=None):
        self.session_id = session_id  # type: str
        self.tenant_id = tenant_id  # type: long
        self.text_request_shrink = text_request_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.text_request_shrink is not None:
            result['TextRequest'] = self.text_request_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TextRequest') is not None:
            self.text_request_shrink = m.get('TextRequest')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SendMessageResponseBody()
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
    def __init__(self, app=None, tenant_id=None, user=None):
        self.app = app  # type: StartInstanceRequestApp
        self.tenant_id = tenant_id  # type: long
        self.user = user  # type: StartInstanceRequestUser

    def validate(self):
        if self.app:
            self.app.validate()
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(StartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app is not None:
            result['App'] = self.app.to_map()
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('User') is not None:
            temp_model = StartInstanceRequestUser()
            self.user = temp_model.from_map(m['User'])
        return self


class StartInstanceShrinkRequest(TeaModel):
    def __init__(self, app_shrink=None, tenant_id=None, user_shrink=None):
        self.app_shrink = app_shrink  # type: str
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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_shrink is not None:
            result['User'] = self.user_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('App') is not None:
            self.app_shrink = m.get('App')
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
    def __init__(self, channel=None, request_id=None, session_id=None):
        self.channel = channel  # type: StartInstanceResponseBodyDataChannel
        self.request_id = request_id  # type: str
        self.session_id = session_id  # type: str

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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
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
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


