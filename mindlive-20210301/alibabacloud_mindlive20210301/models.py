# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class LoginDeviceRequest(TeaModel):
    def __init__(self, user_id=None, user_source=None):
        self.user_id = user_id  # type: str
        self.user_source = user_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source is not None:
            result['UserSource'] = self.user_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSource') is not None:
            self.user_source = m.get('UserSource')
        return self


class LoginDeviceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoginDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LoginDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LoginDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LoginDeviceResponse, self).to_map()
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
            temp_model = LoginDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LogoutDeviceRequest(TeaModel):
    def __init__(self, user_id=None, user_source=None):
        self.user_id = user_id  # type: str
        self.user_source = user_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogoutDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_source is not None:
            result['UserSource'] = self.user_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserSource') is not None:
            self.user_source = m.get('UserSource')
        return self


class LogoutDeviceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(LogoutDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LogoutDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LogoutDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LogoutDeviceResponse, self).to_map()
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
            temp_model = LogoutDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryItemBackgroundsRequest(TeaModel):
    def __init__(self, item_ids=None):
        self.item_ids = item_ids  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemBackgroundsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_ids is not None:
            result['ItemIds'] = self.item_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemIds') is not None:
            self.item_ids = m.get('ItemIds')
        return self


class QueryItemBackgroundsShrinkRequest(TeaModel):
    def __init__(self, item_ids_shrink=None):
        self.item_ids_shrink = item_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemBackgroundsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_ids_shrink is not None:
            result['ItemIds'] = self.item_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemIds') is not None:
            self.item_ids_shrink = m.get('ItemIds')
        return self


class QueryItemBackgroundsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryItemBackgroundsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryItemBackgroundsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryItemBackgroundsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryItemBackgroundsResponse, self).to_map()
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
            temp_model = QueryItemBackgroundsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportCurrentBackgroundRequest(TeaModel):
    def __init__(self, bg_config=None, mode=None, open=None, resource_uuid=None):
        self.bg_config = bg_config  # type: dict[str, any]
        self.mode = mode  # type: str
        self.open = open  # type: bool
        self.resource_uuid = resource_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportCurrentBackgroundRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_config is not None:
            result['BgConfig'] = self.bg_config
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.open is not None:
            result['Open'] = self.open
        if self.resource_uuid is not None:
            result['ResourceUuid'] = self.resource_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BgConfig') is not None:
            self.bg_config = m.get('BgConfig')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('ResourceUuid') is not None:
            self.resource_uuid = m.get('ResourceUuid')
        return self


class ReportCurrentBackgroundShrinkRequest(TeaModel):
    def __init__(self, bg_config_shrink=None, mode=None, open=None, resource_uuid=None):
        self.bg_config_shrink = bg_config_shrink  # type: str
        self.mode = mode  # type: str
        self.open = open  # type: bool
        self.resource_uuid = resource_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportCurrentBackgroundShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_config_shrink is not None:
            result['BgConfig'] = self.bg_config_shrink
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.open is not None:
            result['Open'] = self.open
        if self.resource_uuid is not None:
            result['ResourceUuid'] = self.resource_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BgConfig') is not None:
            self.bg_config_shrink = m.get('BgConfig')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('ResourceUuid') is not None:
            self.resource_uuid = m.get('ResourceUuid')
        return self


class ReportCurrentBackgroundResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportCurrentBackgroundResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportCurrentBackgroundResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportCurrentBackgroundResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportCurrentBackgroundResponse, self).to_map()
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
            temp_model = ReportCurrentBackgroundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportDevConfigRequest(TeaModel):
    def __init__(self, configs=None):
        self.configs = configs  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportDevConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        return self


class ReportDevConfigResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportDevConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportDevConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportDevConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportDevConfigResponse, self).to_map()
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
            temp_model = ReportDevConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportLiveStateRequest(TeaModel):
    def __init__(self, anchor_id=None, id=None, live_mode=None, live_state=None, start_time=None, type=None):
        self.anchor_id = anchor_id  # type: str
        self.id = id  # type: str
        self.live_mode = live_mode  # type: str
        self.live_state = live_state  # type: str
        self.start_time = start_time  # type: long
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportLiveStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.id is not None:
            result['Id'] = self.id
        if self.live_mode is not None:
            result['LiveMode'] = self.live_mode
        if self.live_state is not None:
            result['LiveState'] = self.live_state
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LiveMode') is not None:
            self.live_mode = m.get('LiveMode')
        if m.get('LiveState') is not None:
            self.live_state = m.get('LiveState')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ReportLiveStateResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportLiveStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportLiveStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportLiveStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportLiveStateResponse, self).to_map()
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
            temp_model = ReportLiveStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportScreenRequest(TeaModel):
    def __init__(self, oss_bucket_name=None, oss_object_key=None):
        self.oss_bucket_name = oss_bucket_name  # type: str
        self.oss_object_key = oss_object_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportScreenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name
        if self.oss_object_key is not None:
            result['OssObjectKey'] = self.oss_object_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')
        if m.get('OssObjectKey') is not None:
            self.oss_object_key = m.get('OssObjectKey')
        return self


class ReportScreenResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportScreenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportScreenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportScreenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportScreenResponse, self).to_map()
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
            temp_model = ReportScreenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUserConfigRequest(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUserConfigRequest, self).to_map()
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


class ReportUserConfigResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUserConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ReportUserConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReportUserConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportUserConfigResponse, self).to_map()
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
            temp_model = ReportUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestAuthorizationDataResponseBodyData(TeaModel):
    def __init__(self, url=None):
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestAuthorizationDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RequestAuthorizationDataResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestAuthorizationDataResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestAuthorizationDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestAuthorizationDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestAuthorizationDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestAuthorizationDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestAuthorizationDataResponse, self).to_map()
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
            temp_model = RequestAuthorizationDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestBackgroundResponseBodyData(TeaModel):
    def __init__(self, bg_config=None, download_url=None, file_type=None, mode=None, open=None, resource_uuid=None,
                 scope=None):
        self.bg_config = bg_config  # type: dict[str, any]
        self.download_url = download_url  # type: str
        self.file_type = file_type  # type: str
        self.mode = mode  # type: str
        self.open = open  # type: bool
        self.resource_uuid = resource_uuid  # type: str
        self.scope = scope  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestBackgroundResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bg_config is not None:
            result['BgConfig'] = self.bg_config
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.open is not None:
            result['Open'] = self.open
        if self.resource_uuid is not None:
            result['ResourceUuid'] = self.resource_uuid
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BgConfig') is not None:
            self.bg_config = m.get('BgConfig')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('Open') is not None:
            self.open = m.get('Open')
        if m.get('ResourceUuid') is not None:
            self.resource_uuid = m.get('ResourceUuid')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class RequestBackgroundResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestBackgroundResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestBackgroundResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestBackgroundResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestBackgroundResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestBackgroundResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestBackgroundResponse, self).to_map()
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
            temp_model = RequestBackgroundResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestBindDataRequest(TeaModel):
    def __init__(self, live_source=None):
        self.live_source = live_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestBindDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_source is not None:
            result['LiveSource'] = self.live_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveSource') is not None:
            self.live_source = m.get('LiveSource')
        return self


class RequestBindDataResponseBodyData(TeaModel):
    def __init__(self, code=None, max_keep_seconds=None, short_url=None, url=None):
        self.code = code  # type: str
        self.max_keep_seconds = max_keep_seconds  # type: int
        self.short_url = short_url  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestBindDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.max_keep_seconds is not None:
            result['MaxKeepSeconds'] = self.max_keep_seconds
        if self.short_url is not None:
            result['ShortUrl'] = self.short_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MaxKeepSeconds') is not None:
            self.max_keep_seconds = m.get('MaxKeepSeconds')
        if m.get('ShortUrl') is not None:
            self.short_url = m.get('ShortUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RequestBindDataResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestBindDataResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestBindDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestBindDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestBindDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestBindDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestBindDataResponse, self).to_map()
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
            temp_model = RequestBindDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestBindingStateResponseBodyData(TeaModel):
    def __init__(self, bind_at=None, device_id=None, user_avatar=None, user_id=None, user_nick=None,
                 user_source=None):
        self.bind_at = bind_at  # type: long
        self.device_id = device_id  # type: str
        self.user_avatar = user_avatar  # type: str
        self.user_id = user_id  # type: str
        self.user_nick = user_nick  # type: str
        self.user_source = user_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestBindingStateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_at is not None:
            result['BindAt'] = self.bind_at
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.user_avatar is not None:
            result['UserAvatar'] = self.user_avatar
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_nick is not None:
            result['UserNick'] = self.user_nick
        if self.user_source is not None:
            result['UserSource'] = self.user_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BindAt') is not None:
            self.bind_at = m.get('BindAt')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('UserAvatar') is not None:
            self.user_avatar = m.get('UserAvatar')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserNick') is not None:
            self.user_nick = m.get('UserNick')
        if m.get('UserSource') is not None:
            self.user_source = m.get('UserSource')
        return self


class RequestBindingStateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestBindingStateResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestBindingStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestBindingStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestBindingStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestBindingStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestBindingStateResponse, self).to_map()
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
            temp_model = RequestBindingStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestDeviceInfoResponseBodyData(TeaModel):
    def __init__(self, device_id=None, device_name=None, device_sn=None, public_ip=None):
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.device_sn = device_sn  # type: str
        self.public_ip = public_ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestDeviceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')
        return self


class RequestDeviceInfoResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestDeviceInfoResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestDeviceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestDeviceInfoResponse, self).to_map()
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
            temp_model = RequestDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestIotTriadResponseBodyData(TeaModel):
    def __init__(self, device_name=None, device_secret=None, product_key=None):
        self.device_name = device_name  # type: str
        self.device_secret = device_secret  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestIotTriadResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_secret is not None:
            result['DeviceSecret'] = self.device_secret
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSecret') is not None:
            self.device_secret = m.get('DeviceSecret')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class RequestIotTriadResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestIotTriadResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestIotTriadResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestIotTriadResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestIotTriadResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestIotTriadResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestIotTriadResponse, self).to_map()
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
            temp_model = RequestIotTriadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestLiveSellPointStateResponseBodyData(TeaModel):
    def __init__(self, display=None):
        self.display = display  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestLiveSellPointStateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class RequestLiveSellPointStateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestLiveSellPointStateResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestLiveSellPointStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestLiveSellPointStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestLiveSellPointStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestLiveSellPointStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestLiveSellPointStateResponse, self).to_map()
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
            temp_model = RequestLiveSellPointStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestLiveTeleprompterStateResponseBodyData(TeaModel):
    def __init__(self, display=None):
        self.display = display  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestLiveTeleprompterStateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class RequestLiveTeleprompterStateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestLiveTeleprompterStateResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestLiveTeleprompterStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestLiveTeleprompterStateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestLiveTeleprompterStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestLiveTeleprompterStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestLiveTeleprompterStateResponse, self).to_map()
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
            temp_model = RequestLiveTeleprompterStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestOssStsRequest(TeaModel):
    def __init__(self, app_code=None, expire_seconds=None):
        self.app_code = app_code  # type: str
        self.expire_seconds = expire_seconds  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestOssStsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.expire_seconds is not None:
            result['ExpireSeconds'] = self.expire_seconds
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('ExpireSeconds') is not None:
            self.expire_seconds = m.get('ExpireSeconds')
        return self


class RequestOssStsResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, bucket=None, end_point=None, expire=None,
                 object_key_prefix=None, security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.bucket = bucket  # type: str
        self.end_point = end_point  # type: str
        self.expire = expire  # type: str
        self.object_key_prefix = object_key_prefix  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestOssStsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.end_point is not None:
            result['EndPoint'] = self.end_point
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.object_key_prefix is not None:
            result['ObjectKeyPrefix'] = self.object_key_prefix
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('ObjectKeyPrefix') is not None:
            self.object_key_prefix = m.get('ObjectKeyPrefix')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class RequestOssStsResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestOssStsResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestOssStsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestOssStsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestOssStsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestOssStsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestOssStsResponse, self).to_map()
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
            temp_model = RequestOssStsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestPasterResponseBodyData(TeaModel):
    def __init__(self, configs=None, download_url=None, resource_uuid=None):
        self.configs = configs  # type: dict[str, any]
        self.download_url = download_url  # type: str
        self.resource_uuid = resource_uuid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestPasterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.configs is not None:
            result['Configs'] = self.configs
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.resource_uuid is not None:
            result['ResourceUuid'] = self.resource_uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('ResourceUuid') is not None:
            self.resource_uuid = m.get('ResourceUuid')
        return self


class RequestPasterResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: list[RequestPasterResponseBodyData]
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RequestPasterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = RequestPasterResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestPasterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestPasterResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestPasterResponse, self).to_map()
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
            temp_model = RequestPasterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestResetDataRequest(TeaModel):
    def __init__(self, live_source=None):
        self.live_source = live_source  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestResetDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_source is not None:
            result['LiveSource'] = self.live_source
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LiveSource') is not None:
            self.live_source = m.get('LiveSource')
        return self


class RequestResetDataResponseBodyData(TeaModel):
    def __init__(self, full_url=None, url=None):
        self.full_url = full_url  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestResetDataResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.full_url is not None:
            result['FullUrl'] = self.full_url
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FullUrl') is not None:
            self.full_url = m.get('FullUrl')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RequestResetDataResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestResetDataResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestResetDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestResetDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestResetDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestResetDataResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestResetDataResponse, self).to_map()
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
            temp_model = RequestResetDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestServiceInfoResponseBodyData(TeaModel):
    def __init__(self, service_effect_at=None, service_expire_at=None, service_pack_name=None):
        self.service_effect_at = service_effect_at  # type: long
        self.service_expire_at = service_expire_at  # type: long
        self.service_pack_name = service_pack_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestServiceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_effect_at is not None:
            result['ServiceEffectAt'] = self.service_effect_at
        if self.service_expire_at is not None:
            result['ServiceExpireAt'] = self.service_expire_at
        if self.service_pack_name is not None:
            result['ServicePackName'] = self.service_pack_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceEffectAt') is not None:
            self.service_effect_at = m.get('ServiceEffectAt')
        if m.get('ServiceExpireAt') is not None:
            self.service_expire_at = m.get('ServiceExpireAt')
        if m.get('ServicePackName') is not None:
            self.service_pack_name = m.get('ServicePackName')
        return self


class RequestServiceInfoResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestServiceInfoResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestServiceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestServiceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestServiceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestServiceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestServiceInfoResponse, self).to_map()
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
            temp_model = RequestServiceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestUserConfigRequest(TeaModel):
    def __init__(self, key=None):
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestUserConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class RequestUserConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestUserConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestUserConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestUserConfigResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestUserConfigResponse, self).to_map()
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
            temp_model = RequestUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RequestUserSellPointTemplateResponseBodyData(TeaModel):
    def __init__(self, display_config=None, template_config=None, template_uuid=None, url=None):
        self.display_config = display_config  # type: dict[str, any]
        self.template_config = template_config  # type: dict[str, any]
        self.template_uuid = template_uuid  # type: str
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RequestUserSellPointTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_config is not None:
            result['DisplayConfig'] = self.display_config
        if self.template_config is not None:
            result['TemplateConfig'] = self.template_config
        if self.template_uuid is not None:
            result['TemplateUuid'] = self.template_uuid
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayConfig') is not None:
            self.display_config = m.get('DisplayConfig')
        if m.get('TemplateConfig') is not None:
            self.template_config = m.get('TemplateConfig')
        if m.get('TemplateUuid') is not None:
            self.template_uuid = m.get('TemplateUuid')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RequestUserSellPointTemplateResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: RequestUserSellPointTemplateResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RequestUserSellPointTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RequestUserSellPointTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RequestUserSellPointTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RequestUserSellPointTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RequestUserSellPointTemplateResponse, self).to_map()
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
            temp_model = RequestUserSellPointTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetDeviceRequest(TeaModel):
    def __init__(self, code=None):
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetDeviceRequest, self).to_map()
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


class ResetDeviceResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResetDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetDeviceResponse, self).to_map()
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
            temp_model = ResetDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCurrentItemRequest(TeaModel):
    def __init__(self, item_id=None):
        self.item_id = item_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCurrentItemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        return self


class UpdateCurrentItemResponseBodyDataItemBackground(TeaModel):
    def __init__(self, download_url=None, file_type=None, item_id=None, resource_uuid=None, scope=None):
        self.download_url = download_url  # type: str
        self.file_type = file_type  # type: str
        self.item_id = item_id  # type: str
        self.resource_uuid = resource_uuid  # type: str
        self.scope = scope  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCurrentItemResponseBodyDataItemBackground, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.item_id is not None:
            result['ItemId'] = self.item_id
        if self.resource_uuid is not None:
            result['ResourceUuid'] = self.resource_uuid
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')
        if m.get('ResourceUuid') is not None:
            self.resource_uuid = m.get('ResourceUuid')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class UpdateCurrentItemResponseBodyData(TeaModel):
    def __init__(self, item_background=None):
        self.item_background = item_background  # type: UpdateCurrentItemResponseBodyDataItemBackground

    def validate(self):
        if self.item_background:
            self.item_background.validate()

    def to_map(self):
        _map = super(UpdateCurrentItemResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.item_background is not None:
            result['ItemBackground'] = self.item_background.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ItemBackground') is not None:
            temp_model = UpdateCurrentItemResponseBodyDataItemBackground()
            self.item_background = temp_model.from_map(m['ItemBackground'])
        return self


class UpdateCurrentItemResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, request_id=None, success=None):
        self.data = data  # type: UpdateCurrentItemResponseBodyData
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateCurrentItemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = UpdateCurrentItemResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCurrentItemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCurrentItemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCurrentItemResponse, self).to_map()
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
            temp_model = UpdateCurrentItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveSellPointStateRequest(TeaModel):
    def __init__(self, display=None):
        self.display = display  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveSellPointStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class UpdateLiveSellPointStateResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveSellPointStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLiveSellPointStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLiveSellPointStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLiveSellPointStateResponse, self).to_map()
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
            temp_model = UpdateLiveSellPointStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveTeleprompterStateRequest(TeaModel):
    def __init__(self, display=None):
        self.display = display  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveTeleprompterStateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display is not None:
            result['Display'] = self.display
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Display') is not None:
            self.display = m.get('Display')
        return self


class UpdateLiveTeleprompterStateResponseBody(TeaModel):
    def __init__(self, error_code=None, error_message=None, request_id=None, success=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLiveTeleprompterStateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLiveTeleprompterStateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLiveTeleprompterStateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLiveTeleprompterStateResponse, self).to_map()
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
            temp_model = UpdateLiveTeleprompterStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


