# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CreateAppSessionRequestStartParameters(TeaModel):
    def __init__(self, key=None, value=None):
        # key
        self.key = key  # type: str
        # value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionRequestStartParameters, self).to_map()
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


class CreateAppSessionRequestSystemInfo(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionRequestSystemInfo, self).to_map()
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


class CreateAppSessionRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, client_ip=None, custom_session_id=None, custom_user_id=None,
                 enable_postpaid=None, start_parameters=None, system_info=None, timeout=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        # 客户端ip
        self.client_ip = client_ip  # type: str
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 自定义用户id
        self.custom_user_id = custom_user_id  # type: str
        self.enable_postpaid = enable_postpaid  # type: bool
        # 启动参数
        self.start_parameters = start_parameters  # type: list[CreateAppSessionRequestStartParameters]
        # 系统信息：如端侧机型等信息
        self.system_info = system_info  # type: list[CreateAppSessionRequestSystemInfo]
        self.timeout = timeout  # type: long

    def validate(self):
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.enable_postpaid is not None:
            result['EnablePostpaid'] = self.enable_postpaid
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('EnablePostpaid') is not None:
            self.enable_postpaid = m.get('EnablePostpaid')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, custom_session_id=None, platform_session_id=None,
                 request_id=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppSessionResponse, self).to_map()
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
            temp_model = CreateAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppSessionRequest(TeaModel):
    def __init__(self, custom_session_id=None, platform_session_id=None):
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class GetAppSessionResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, custom_session_id=None, platform_session_id=None,
                 request_id=None, status=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAppSessionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppSessionResponse, self).to_map()
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
            temp_model = GetAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppSessionsRequest(TeaModel):
    def __init__(self, app_id=None, custom_session_ids=None, page_number=None, page_size=None,
                 platform_session_ids=None):
        self.app_id = app_id  # type: str
        # 自定义会话id
        self.custom_session_ids = custom_session_ids  # type: list[str]
        # 页码
        self.page_number = page_number  # type: int
        # 分页大小
        self.page_size = page_size  # type: int
        # 自定义用户id
        self.platform_session_ids = platform_session_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppSessionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.custom_session_ids is not None:
            result['CustomSessionIds'] = self.custom_session_ids
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.platform_session_ids is not None:
            result['PlatformSessionIds'] = self.platform_session_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CustomSessionIds') is not None:
            self.custom_session_ids = m.get('CustomSessionIds')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlatformSessionIds') is not None:
            self.platform_session_ids = m.get('PlatformSessionIds')
        return self


class ListAppSessionsResponseBodyAppSessions(TeaModel):
    def __init__(self, app_id=None, app_version=None, custom_session_id=None, platform_session_id=None, status=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 状态
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppSessionsResponseBodyAppSessions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppSessionsResponseBody(TeaModel):
    def __init__(self, app_sessions=None, page_number=None, page_size=None, request_id=None):
        self.app_sessions = app_sessions  # type: list[ListAppSessionsResponseBodyAppSessions]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.app_sessions:
            for k in self.app_sessions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppSessionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppSessions'] = []
        if self.app_sessions is not None:
            for k in self.app_sessions:
                result['AppSessions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_sessions = []
        if m.get('AppSessions') is not None:
            for k in m.get('AppSessions'):
                temp_model = ListAppSessionsResponseBodyAppSessions()
                self.app_sessions.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListAppSessionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppSessionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppSessionsResponse, self).to_map()
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
            temp_model = ListAppSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppSessionRequest(TeaModel):
    def __init__(self, custom_session_id=None, platform_session_id=None):
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 自定义用户id
        self.platform_session_id = platform_session_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class StopAppSessionResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, custom_session_id=None, platform_session_id=None,
                 request_id=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppSessionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopAppSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAppSessionResponse, self).to_map()
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
            temp_model = StopAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


