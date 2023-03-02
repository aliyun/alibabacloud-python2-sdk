# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class RegisterDeviceRequest(TeaModel):
    def __init__(self, app_key=None, device_id=None, extend=None, sdk_code=None, user_device_id=None):
        self.app_key = app_key  # type: str
        self.device_id = device_id  # type: str
        self.extend = extend  # type: dict[str, any]
        self.sdk_code = sdk_code  # type: str
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.extend is not None:
            result['Extend'] = self.extend
        if self.sdk_code is not None:
            result['SdkCode'] = self.sdk_code
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        if m.get('SdkCode') is not None:
            self.sdk_code = m.get('SdkCode')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class RegisterDeviceShrinkRequest(TeaModel):
    def __init__(self, app_key=None, device_id=None, extend_shrink=None, sdk_code=None, user_device_id=None):
        self.app_key = app_key  # type: str
        self.device_id = device_id  # type: str
        self.extend_shrink = extend_shrink  # type: str
        self.sdk_code = sdk_code  # type: str
        self.user_device_id = user_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDeviceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.extend_shrink is not None:
            result['Extend'] = self.extend_shrink
        if self.sdk_code is not None:
            result['SdkCode'] = self.sdk_code
        if self.user_device_id is not None:
            result['UserDeviceId'] = self.user_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Extend') is not None:
            self.extend_shrink = m.get('Extend')
        if m.get('SdkCode') is not None:
            self.sdk_code = m.get('SdkCode')
        if m.get('UserDeviceId') is not None:
            self.user_device_id = m.get('UserDeviceId')
        return self


class RegisterDeviceResponseBodyData(TeaModel):
    def __init__(self, license=None, public_key=None, rid=None, signature=None):
        self.license = license  # type: str
        self.public_key = public_key  # type: str
        self.rid = rid  # type: str
        self.signature = signature  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.license is not None:
            result['License'] = self.license
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.rid is not None:
            result['Rid'] = self.rid
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('License') is not None:
            self.license = m.get('License')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('Rid') is not None:
            self.rid = m.get('Rid')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class RegisterDeviceResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, message=None, request_id=None):
        self.data = data  # type: RegisterDeviceResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RegisterDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RegisterDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterDeviceResponse, self).to_map()
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
            temp_model = RegisterDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


