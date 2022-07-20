# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class CancelReserveTaskRequest(TeaModel):
    def __init__(self, client_token=None, task_id=None):
        # 客户端幂等性 token
        self.client_token = client_token  # type: str
        # 创建容量预定任务时返回的 taskId
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelReserveTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelReserveTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # pop的requestId
        self.request_id = request_id  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelReserveTaskResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelReserveTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelReserveTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelReserveTaskResponse, self).to_map()
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
            temp_model = CancelReserveTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAdaptationRequestAdaptTarget(TeaModel):
    def __init__(self, bit_rate=None, frame_rate=None, resolution=None, start_program=None):
        self.bit_rate = bit_rate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.resolution = resolution  # type: str
        self.start_program = start_program  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAdaptationRequestAdaptTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class CreateAdaptationRequest(TeaModel):
    def __init__(self, adapt_target=None, app_version_id=None):
        self.adapt_target = adapt_target  # type: CreateAdaptationRequestAdaptTarget
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super(CreateAdaptationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            temp_model = CreateAdaptationRequestAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class CreateAdaptationShrinkRequest(TeaModel):
    def __init__(self, adapt_target_shrink=None, app_version_id=None):
        self.adapt_target_shrink = adapt_target_shrink  # type: str
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAdaptationShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target_shrink is not None:
            result['AdaptTarget'] = self.adapt_target_shrink
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            self.adapt_target_shrink = m.get('AdaptTarget')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class CreateAdaptationResponseBody(TeaModel):
    def __init__(self, adapt_apply_id=None, request_id=None):
        self.adapt_apply_id = adapt_apply_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAdaptationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAdaptationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAdaptationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAdaptationResponse, self).to_map()
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
            temp_model = CreateAdaptationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(self, app_name=None, app_type=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        return self


class CreateAppResponseBody(TeaModel):
    def __init__(self, app_id=None, request_id=None):
        self.app_id = app_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppResponse, self).to_map()
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionRequestStartParameters(TeaModel):
    def __init__(self, key=None, value=None):
        # key
        self.key = key  # type: str
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


class CreateAppSessionBatchSyncRequestAppInfosStartParameters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncRequestAppInfosStartParameters, self).to_map()
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


class CreateAppSessionBatchSyncRequestAppInfosSystemInfo(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncRequestAppInfosSystemInfo, self).to_map()
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


class CreateAppSessionBatchSyncRequestAppInfosTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncRequestAppInfosTags, self).to_map()
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


class CreateAppSessionBatchSyncRequestAppInfos(TeaModel):
    def __init__(self, app_id=None, app_version=None, client_ip=None, custom_user_id=None, customer_session_id=None,
                 district_id=None, project_id=None, start_parameters=None, system_info=None, tags=None):
        self.app_id = app_id  # type: str
        self.app_version = app_version  # type: str
        self.client_ip = client_ip  # type: str
        self.custom_user_id = custom_user_id  # type: str
        self.customer_session_id = customer_session_id  # type: str
        self.district_id = district_id  # type: str
        self.project_id = project_id  # type: str
        self.start_parameters = start_parameters  # type: list[CreateAppSessionBatchSyncRequestAppInfosStartParameters]
        self.system_info = system_info  # type: list[CreateAppSessionBatchSyncRequestAppInfosSystemInfo]
        self.tags = tags  # type: list[CreateAppSessionBatchSyncRequestAppInfosTags]

    def validate(self):
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncRequestAppInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.customer_session_id is not None:
            result['CustomerSessionId'] = self.customer_session_id
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('CustomerSessionId') is not None:
            self.customer_session_id = m.get('CustomerSessionId')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfosTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchSyncRequest(TeaModel):
    def __init__(self, app_infos=None, batch_id=None):
        self.app_infos = app_infos  # type: list[CreateAppSessionBatchSyncRequestAppInfos]
        self.batch_id = batch_id  # type: str

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = CreateAppSessionBatchSyncRequestAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class CreateAppSessionBatchSyncShrinkRequest(TeaModel):
    def __init__(self, app_infos_shrink=None, batch_id=None):
        self.app_infos_shrink = app_infos_shrink  # type: str
        self.batch_id = batch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_infos_shrink is not None:
            result['AppInfos'] = self.app_infos_shrink
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos_shrink = m.get('AppInfos')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        return self


class CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo(TeaModel):
    def __init__(self, error_code=None, error_message=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class CreateAppSessionBatchSyncResponseBodyFailedList(TeaModel):
    def __init__(self, app_id=None, custom_session_id=None, failed_info=None):
        self.app_id = app_id  # type: str
        self.custom_session_id = custom_session_id  # type: str
        self.failed_info = failed_info  # type: CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo

    def validate(self):
        if self.failed_info:
            self.failed_info.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponseBodyFailedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.failed_info is not None:
            result['FailedInfo'] = self.failed_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('FailedInfo') is not None:
            temp_model = CreateAppSessionBatchSyncResponseBodyFailedListFailedInfo()
            self.failed_info = temp_model.from_map(m['FailedInfo'])
        return self


class CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints(TeaModel):
    def __init__(self, access_host=None, access_port=None, district_id=None, isp=None, name=None, type=None):
        self.access_host = access_host  # type: str
        self.access_port = access_port  # type: str
        self.district_id = district_id  # type: str
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_host is not None:
            result['AccessHost'] = self.access_host
        if self.access_port is not None:
            result['AccessPort'] = self.access_port
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessHost') is not None:
            self.access_host = m.get('AccessHost')
        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppSessionBatchSyncResponseBodyResultListBizInfo(TeaModel):
    def __init__(self, biz=None, endpoints=None):
        self.biz = biz  # type: dict[str, any]
        self.endpoints = endpoints  # type: list[CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints]

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponseBodyResultListBizInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = CreateAppSessionBatchSyncResponseBodyResultListBizInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchSyncResponseBodyResultList(TeaModel):
    def __init__(self, app_id=None, app_version=None, biz_info=None, custom_session_id=None,
                 platform_session_id=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        self.biz_info = biz_info  # type: CreateAppSessionBatchSyncResponseBodyResultListBizInfo
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponseBodyResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BizInfo') is not None:
            temp_model = CreateAppSessionBatchSyncResponseBodyResultListBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        return self


class CreateAppSessionBatchSyncResponseBody(TeaModel):
    def __init__(self, batch_id=None, failed_list=None, request_id=None, result_list=None):
        # 自定义会话id
        self.batch_id = batch_id  # type: str
        self.failed_list = failed_list  # type: list[CreateAppSessionBatchSyncResponseBodyFailedList]
        # 请求id
        self.request_id = request_id  # type: str
        self.result_list = result_list  # type: list[CreateAppSessionBatchSyncResponseBodyResultList]

    def validate(self):
        if self.failed_list:
            for k in self.failed_list:
                if k:
                    k.validate()
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        result['FailedList'] = []
        if self.failed_list is not None:
            for k in self.failed_list:
                result['FailedList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        self.failed_list = []
        if m.get('FailedList') is not None:
            for k in m.get('FailedList'):
                temp_model = CreateAppSessionBatchSyncResponseBodyFailedList()
                self.failed_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = CreateAppSessionBatchSyncResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchSyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppSessionBatchSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchSyncResponse, self).to_map()
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
            temp_model = CreateAppSessionBatchSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionSyncRequestStartParameters(TeaModel):
    def __init__(self, key=None, value=None):
        # key
        self.key = key  # type: str
        # value
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionSyncRequestStartParameters, self).to_map()
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


class CreateAppSessionSyncRequestSystemInfo(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionSyncRequestSystemInfo, self).to_map()
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


class CreateAppSessionSyncRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionSyncRequestTags, self).to_map()
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


class CreateAppSessionSyncRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, client_ip=None, custom_session_id=None, custom_user_id=None,
                 district_id=None, project_id=None, start_parameters=None, system_info=None, tags=None):
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
        self.district_id = district_id  # type: str
        self.project_id = project_id  # type: str
        # 启动参数
        self.start_parameters = start_parameters  # type: list[CreateAppSessionSyncRequestStartParameters]
        # 系统信息：如端侧机型等信息
        self.system_info = system_info  # type: list[CreateAppSessionSyncRequestSystemInfo]
        self.tags = tags  # type: list[CreateAppSessionSyncRequestTags]

    def validate(self):
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.system_info:
            for k in self.system_info:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionSyncRequest, self).to_map()
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
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionSyncRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionSyncRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateAppSessionSyncRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateAppSessionSyncResponseBodyBizInfoEndpoints(TeaModel):
    def __init__(self, access_host=None, access_port=None, district_id=None, isp=None, name=None, type=None):
        self.access_host = access_host  # type: str
        self.access_port = access_port  # type: str
        self.district_id = district_id  # type: str
        self.isp = isp  # type: str
        self.name = name  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionSyncResponseBodyBizInfoEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_host is not None:
            result['AccessHost'] = self.access_host
        if self.access_port is not None:
            result['AccessPort'] = self.access_port
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.isp is not None:
            result['Isp'] = self.isp
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessHost') is not None:
            self.access_host = m.get('AccessHost')
        if m.get('AccessPort') is not None:
            self.access_port = m.get('AccessPort')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('Isp') is not None:
            self.isp = m.get('Isp')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateAppSessionSyncResponseBodyBizInfo(TeaModel):
    def __init__(self, biz=None, endpoints=None):
        self.biz = biz  # type: dict[str, any]
        self.endpoints = endpoints  # type: list[CreateAppSessionSyncResponseBodyBizInfoEndpoints]

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionSyncResponseBodyBizInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz is not None:
            result['Biz'] = self.biz
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Biz') is not None:
            self.biz = m.get('Biz')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = CreateAppSessionSyncResponseBodyBizInfoEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        return self


class CreateAppSessionSyncResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, biz_info=None, custom_session_id=None,
                 platform_session_id=None, request_id=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        self.biz_info = biz_info  # type: CreateAppSessionSyncResponseBodyBizInfo
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super(CreateAppSessionSyncResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
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
        if m.get('BizInfo') is not None:
            temp_model = CreateAppSessionSyncResponseBodyBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionSyncResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppSessionSyncResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppSessionSyncResponse, self).to_map()
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
            temp_model = CreateAppSessionSyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppVersionRequest(TeaModel):
    def __init__(self, app_id=None, app_version_name=None):
        self.app_id = app_id  # type: str
        self.app_version_name = app_version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class CreateAppVersionResponseBody(TeaModel):
    def __init__(self, app_version_id=None, request_id=None):
        self.app_version_id = app_version_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAppVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppVersionResponse, self).to_map()
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
            temp_model = CreateAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCapacityReservationRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, client_token=None, district_id=None,
                 expect_resource_ready_time=None, expect_session_capacity=None, project_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 应用版本ID，如果不填，采用控制台设置的默认版本
        self.app_version = app_version  # type: str
        # 客户端 token，保持幂等性。
        self.client_token = client_token  # type: str
        # 大区 id
        self.district_id = district_id  # type: str
        # 预期资源ready可服务时间 时间格式 yyyy-mm-dd HH:MM:SS 比如
        self.expect_resource_ready_time = expect_resource_ready_time  # type: str
        # 预期创建出的容器能支持的 session 数量。GCS 内部会根据适配自动计算出所需要的资源量，以及多种机型的配比。
        self.expect_session_capacity = expect_session_capacity  # type: int
        # 项目ID
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCapacityReservationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.expect_resource_ready_time is not None:
            result['ExpectResourceReadyTime'] = self.expect_resource_ready_time
        if self.expect_session_capacity is not None:
            result['ExpectSessionCapacity'] = self.expect_session_capacity
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ExpectResourceReadyTime') is not None:
            self.expect_resource_ready_time = m.get('ExpectResourceReadyTime')
        if m.get('ExpectSessionCapacity') is not None:
            self.expect_session_capacity = m.get('ExpectSessionCapacity')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateCapacityReservationResponseBody(TeaModel):
    def __init__(self, curr_max_allocatable_session_capacity=None, request_id=None, task_id=None):
        # 当前最大可分配的 session 库存，注意两次调用之间，该库存值可能有变动
        self.curr_max_allocatable_session_capacity = curr_max_allocatable_session_capacity  # type: int
        # pop的requestId
        self.request_id = request_id  # type: str
        # 容器创建任务 id
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateCapacityReservationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.curr_max_allocatable_session_capacity is not None:
            result['CurrMaxAllocatableSessionCapacity'] = self.curr_max_allocatable_session_capacity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrMaxAllocatableSessionCapacity') is not None:
            self.curr_max_allocatable_session_capacity = m.get('CurrMaxAllocatableSessionCapacity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateCapacityReservationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateCapacityReservationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateCapacityReservationResponse, self).to_map()
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
            temp_model = CreateCapacityReservationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequestProjectQuotaLimit(TeaModel):
    def __init__(self, district_limit_map=None, limit_type=None):
        # key - districtId
        self.district_limit_map = district_limit_map  # type: dict[str, ProjectQuotaLimitDistrictLimitMapValue]
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(CreateProjectRequestProjectQuotaLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = ProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class CreateProjectRequest(TeaModel):
    def __init__(self, bound_app_id_list=None, operator_id=None, operator_type=None, project_memo=None,
                 project_name=None, project_quota_limit=None):
        self.bound_app_id_list = bound_app_id_list  # type: list[str]
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        self.project_memo = project_memo  # type: str
        # project name
        self.project_name = project_name  # type: str
        # key : districtId
        self.project_quota_limit = project_quota_limit  # type: CreateProjectRequestProjectQuotaLimit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super(CreateProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list is not None:
            result['BoundAppIdList'] = self.bound_app_id_list
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = CreateProjectRequestProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class CreateProjectShrinkRequest(TeaModel):
    def __init__(self, bound_app_id_list_shrink=None, operator_id=None, operator_type=None, project_memo=None,
                 project_name=None, project_quota_limit_shrink=None):
        self.bound_app_id_list_shrink = bound_app_id_list_shrink  # type: str
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        self.project_memo = project_memo  # type: str
        # project name
        self.project_name = project_name  # type: str
        # key : districtId
        self.project_quota_limit_shrink = project_quota_limit_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list_shrink is not None:
            result['BoundAppIdList'] = self.bound_app_id_list_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit_shrink is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list_shrink = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            self.project_quota_limit_shrink = m.get('ProjectQuotaLimit')
        return self


class CreateProjectResponseBodyData(TeaModel):
    def __init__(self, code=None, data=None, message=None, project_id=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: dict[str, any]
        # 业务处理消息摘要
        self.message = message  # type: str
        self.project_id = project_id  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: CreateProjectResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateProjectResponseBody, self).to_map()
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
            temp_model = CreateProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateProjectResponse, self).to_map()
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppRequest, self).to_map()
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


class DeleteAppResponseBody(TeaModel):
    def __init__(self, app_id=None, request_id=None):
        self.app_id = app_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppResponse, self).to_map()
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppVersionRequest(TeaModel):
    def __init__(self, app_version_id=None):
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class DeleteAppVersionResponseBody(TeaModel):
    def __init__(self, app_version_id=None, request_id=None):
        self.app_version_id = app_version_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAppVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAppVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAppVersionResponse, self).to_map()
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
            temp_model = DeleteAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, project_id=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # project Id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBodyData(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: DeleteProjectResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteProjectResponseBody, self).to_map()
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
            temp_model = DeleteProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteProjectResponse, self).to_map()
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAdaptationRequest(TeaModel):
    def __init__(self, adapt_apply_id=None, app_version_id=None):
        self.adapt_apply_id = adapt_apply_id  # type: long
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAdaptationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class GetAdaptationResponseBodyAdaptTarget(TeaModel):
    def __init__(self, bit_rate=None, frame_rate=None, resolution=None, start_program=None):
        self.bit_rate = bit_rate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.resolution = resolution  # type: str
        self.start_program = start_program  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAdaptationResponseBodyAdaptTarget, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['BitRate'] = self.bit_rate
        if self.frame_rate is not None:
            result['FrameRate'] = self.frame_rate
        if self.resolution is not None:
            result['Resolution'] = self.resolution
        if self.start_program is not None:
            result['StartProgram'] = self.start_program
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BitRate') is not None:
            self.bit_rate = m.get('BitRate')
        if m.get('FrameRate') is not None:
            self.frame_rate = m.get('FrameRate')
        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')
        if m.get('StartProgram') is not None:
            self.start_program = m.get('StartProgram')
        return self


class GetAdaptationResponseBody(TeaModel):
    def __init__(self, adapt_apply_id=None, adapt_target=None, app_id=None, app_version_id=None, gmt_create=None,
                 gmt_modified=None, request_id=None):
        self.adapt_apply_id = adapt_apply_id  # type: long
        self.adapt_target = adapt_target  # type: GetAdaptationResponseBodyAdaptTarget
        self.app_id = app_id  # type: str
        self.app_version_id = app_version_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super(GetAdaptationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AdaptTarget') is not None:
            temp_model = GetAdaptationResponseBodyAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAdaptationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAdaptationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAdaptationResponse, self).to_map()
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
            temp_model = GetAdaptationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppRequest, self).to_map()
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


class GetAppResponseBody(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_type=None, gmt_create=None, gmt_modified=None,
                 request_id=None, version_adapt_num=None, version_total_num=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.request_id = request_id  # type: str
        self.version_adapt_num = version_adapt_num  # type: long
        self.version_total_num = version_total_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version_adapt_num is not None:
            result['VersionAdaptNum'] = self.version_adapt_num
        if self.version_total_num is not None:
            result['VersionTotalNum'] = self.version_total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VersionAdaptNum') is not None:
            self.version_adapt_num = m.get('VersionAdaptNum')
        if m.get('VersionTotalNum') is not None:
            self.version_total_num = m.get('VersionTotalNum')
        return self


class GetAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppResponse, self).to_map()
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppCcuRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, project_id=None):
        # 自定义会话id
        self.app_id = app_id  # type: str
        self.app_version = app_version  # type: str
        # 平台会话id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppCcuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetAppCcuResponseBody(TeaModel):
    def __init__(self, request_id=None, timestamp=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 自定义会话id
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppCcuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetAppCcuResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppCcuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppCcuResponse, self).to_map()
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
            temp_model = GetAppCcuResponseBody()
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


class GetAppSessionResponseBodyBizInfo(TeaModel):
    def __init__(self, start_time=None, stop_time=None):
        self.start_time = start_time  # type: str
        self.stop_time = stop_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSessionResponseBodyBizInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        return self


class GetAppSessionResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, biz_info=None, custom_session_id=None,
                 platform_session_id=None, request_id=None, status=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        self.biz_info = biz_info  # type: GetAppSessionResponseBodyBizInfo
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str
        # 状态
        self.status = status  # type: str

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super(GetAppSessionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
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
        if m.get('BizInfo') is not None:
            temp_model = GetAppSessionResponseBodyBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
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


class GetAppVersionRequest(TeaModel):
    def __init__(self, app_version_id=None):
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        return self


class GetAppVersionResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version_id=None, app_version_name=None, app_version_status=None,
                 app_version_status_memo=None, consume_cu=None, file_address=None, file_size=None, file_upload_finish_time=None,
                 file_upload_type=None, gmt_create=None, gmt_modified=None, request_id=None):
        self.app_id = app_id  # type: str
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.app_version_status = app_version_status  # type: str
        self.app_version_status_memo = app_version_status_memo  # type: str
        self.consume_cu = consume_cu  # type: float
        self.file_address = file_address  # type: str
        self.file_size = file_size  # type: long
        self.file_upload_finish_time = file_upload_finish_time  # type: str
        self.file_upload_type = file_upload_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_status is not None:
            result['AppVersionStatus'] = self.app_version_status
        if self.app_version_status_memo is not None:
            result['AppVersionStatusMemo'] = self.app_version_status_memo
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_finish_time is not None:
            result['FileUploadFinishTime'] = self.file_upload_finish_time
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionStatus') is not None:
            self.app_version_status = m.get('AppVersionStatus')
        if m.get('AppVersionStatusMemo') is not None:
            self.app_version_status_memo = m.get('AppVersionStatusMemo')
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadFinishTime') is not None:
            self.file_upload_finish_time = m.get('FileUploadFinishTime')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAppVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppVersionResponse, self).to_map()
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
            temp_model = GetAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCapacityRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, district_id=None, page_num=None, page_size=None,
                 project_id=None):
        # 按照 appId 来匹配
        self.app_id = app_id  # type: str
        # 按照 app 版本来匹配
        self.app_version = app_version  # type: str
        # 大区 id
        self.district_id = district_id  # type: str
        # 第几页，默认从 1 开始
        self.page_num = page_num  # type: int
        # 一页大小，默认 20，最大 100
        self.page_size = page_size  # type: int
        # 项目 id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCapacityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetCapacityResponseBodyCapacities(TeaModel):
    def __init__(self, app_id=None, app_version=None, district_id=None, session_capacity=None):
        # 创建容器时指定的 appId
        self.app_id = app_id  # type: str
        # 创建容器时指定的版本
        self.app_version = app_version  # type: str
        # 该容器所属大区 id
        self.district_id = district_id  # type: str
        # 可支撑 session 数量
        self.session_capacity = session_capacity  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCapacityResponseBodyCapacities, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.session_capacity is not None:
            result['SessionCapacity'] = self.session_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('SessionCapacity') is not None:
            self.session_capacity = m.get('SessionCapacity')
        return self


class GetCapacityResponseBody(TeaModel):
    def __init__(self, capacities=None, page_num=None, page_size=None, request_id=None, total=None):
        # 回满足匹配的
        self.capacities = capacities  # type: list[GetCapacityResponseBodyCapacities]
        # 第几页
        self.page_num = page_num  # type: int
        # 每页大小
        self.page_size = page_size  # type: int
        # pop的requestId
        self.request_id = request_id  # type: str
        # 满足匹配条件的总量
        self.total = total  # type: int

    def validate(self):
        if self.capacities:
            for k in self.capacities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCapacityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Capacities'] = []
        if self.capacities is not None:
            for k in self.capacities:
                result['Capacities'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.capacities = []
        if m.get('Capacities') is not None:
            for k in m.get('Capacities'):
                temp_model = GetCapacityResponseBodyCapacities()
                self.capacities.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetCapacityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCapacityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCapacityResponse, self).to_map()
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
            temp_model = GetCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, project_id=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # project id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetProjectResponseBodyDataProjectQuotaLimit(TeaModel):
    def __init__(self, district_limit_map=None, limit_type=None):
        # key - districtId
        self.district_limit_map = district_limit_map  # type: dict[str, DataProjectQuotaLimitDistrictLimitMapValue]
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(GetProjectResponseBodyDataProjectQuotaLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = DataProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class GetProjectResponseBodyData(TeaModel):
    def __init__(self, bound_app_nums=None, gmt_create=None, gmt_modified=None, project_id=None, project_memo=None,
                 project_name=None, project_quota_limit=None):
        # 项目关联的应用数量
        self.bound_app_nums = bound_app_nums  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.project_id = project_id  # type: str
        self.project_memo = project_memo  # type: str
        self.project_name = project_name  # type: str
        # key : districtId
        self.project_quota_limit = project_quota_limit  # type: GetProjectResponseBodyDataProjectQuotaLimit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super(GetProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_nums is not None:
            result['BoundAppNums'] = self.bound_app_nums
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BoundAppNums') is not None:
            self.bound_app_nums = m.get('BoundAppNums')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = GetProjectResponseBodyDataProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: GetProjectResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetProjectResponseBody, self).to_map()
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
            temp_model = GetProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetProjectResponse, self).to_map()
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
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetReserveTaskDetailRequest(TeaModel):
    def __init__(self, task_id=None):
        # 创建容量预定任务时返回的 taskId
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReserveTaskDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetReserveTaskDetailResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, curr_completed_session_capacity=None, district_id=None,
                 expect_resource_ready_time=None, expect_session_capacity=None, project_id=None, request_id=None, task_id=None,
                 task_status=None):
        # 容量预定时的 appId
        self.app_id = app_id  # type: str
        # 容量预定时的 appVersion
        self.app_version = app_version  # type: str
        # 当前任务已经生产完成的会话路数
        self.curr_completed_session_capacity = curr_completed_session_capacity  # type: int
        # 容量预定时指定的大区id
        self.district_id = district_id  # type: str
        # 容量预定，期望生效时间
        self.expect_resource_ready_time = expect_resource_ready_time  # type: str
        # 容量预定期望的会话路数
        self.expect_session_capacity = expect_session_capacity  # type: int
        # 容量预定时的 projectId
        self.project_id = project_id  # type: str
        # pop的requestId
        self.request_id = request_id  # type: str
        # 容器创建任务 id
        self.task_id = task_id  # type: str
        # 任务状态
        self.task_status = task_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetReserveTaskDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.curr_completed_session_capacity is not None:
            result['CurrCompletedSessionCapacity'] = self.curr_completed_session_capacity
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.expect_resource_ready_time is not None:
            result['ExpectResourceReadyTime'] = self.expect_resource_ready_time
        if self.expect_session_capacity is not None:
            result['ExpectSessionCapacity'] = self.expect_session_capacity
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('CurrCompletedSessionCapacity') is not None:
            self.curr_completed_session_capacity = m.get('CurrCompletedSessionCapacity')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ExpectResourceReadyTime') is not None:
            self.expect_resource_ready_time = m.get('ExpectResourceReadyTime')
        if m.get('ExpectSessionCapacity') is not None:
            self.expect_session_capacity = m.get('ExpectSessionCapacity')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetReserveTaskDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetReserveTaskDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetReserveTaskDetailResponse, self).to_map()
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
            temp_model = GetReserveTaskDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcePublicIPsRequest(TeaModel):
    def __init__(self, page_num=None, page_size=None, project_id=None):
        # 第几页，默认从 1 开始
        self.page_num = page_num  # type: int
        # 一页大小，默认 20，最大 100
        self.page_size = page_size  # type: int
        # 项目 id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePublicIPsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetResourcePublicIPsResponseBodyIpList(TeaModel):
    def __init__(self, ip=None, project_id=None):
        # ip
        self.ip = ip  # type: str
        # 项目 id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetResourcePublicIPsResponseBodyIpList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class GetResourcePublicIPsResponseBody(TeaModel):
    def __init__(self, ip_list=None, page_num=None, page_size=None, request_id=None, total=None):
        # ip 列表
        self.ip_list = ip_list  # type: list[GetResourcePublicIPsResponseBodyIpList]
        # 第几页
        self.page_num = page_num  # type: int
        # 每页大小
        self.page_size = page_size  # type: int
        # pop的requestId
        self.request_id = request_id  # type: str
        # 满足匹配条件的总量
        self.total = total  # type: int

    def validate(self):
        if self.ip_list:
            for k in self.ip_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetResourcePublicIPsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpList'] = []
        if self.ip_list is not None:
            for k in self.ip_list:
                result['IpList'].append(k.to_map() if k else None)
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_list = []
        if m.get('IpList') is not None:
            for k in m.get('IpList'):
                temp_model = GetResourcePublicIPsResponseBodyIpList()
                self.ip_list.append(temp_model.from_map(k))
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetResourcePublicIPsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetResourcePublicIPsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetResourcePublicIPsResponse, self).to_map()
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
            temp_model = GetResourcePublicIPsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTenantResponseBodyData(TeaModel):
    def __init__(self, charge_mode=None, contacts_mobile=None, contacts_name=None, industry_category=None,
                 scence_desc=None, status=None, tenant_id=None, tenant_name=None):
        # 计收模式
        self.charge_mode = charge_mode  # type: str
        # 联系人电话
        self.contacts_mobile = contacts_mobile  # type: str
        # 联系人
        self.contacts_name = contacts_name  # type: str
        # 租户所属行业(Code)
        self.industry_category = industry_category  # type: str
        # 业务场景描述
        self.scence_desc = scence_desc  # type: str
        # 租户状态
        self.status = status  # type: str
        # 租户ID(AlipayUserId)
        self.tenant_id = tenant_id  # type: str
        # 租户名称
        self.tenant_name = tenant_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTenantResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_mode is not None:
            result['ChargeMode'] = self.charge_mode
        if self.contacts_mobile is not None:
            result['ContactsMobile'] = self.contacts_mobile
        if self.contacts_name is not None:
            result['ContactsName'] = self.contacts_name
        if self.industry_category is not None:
            result['IndustryCategory'] = self.industry_category
        if self.scence_desc is not None:
            result['ScenceDesc'] = self.scence_desc
        if self.status is not None:
            result['Status'] = self.status
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChargeMode') is not None:
            self.charge_mode = m.get('ChargeMode')
        if m.get('ContactsMobile') is not None:
            self.contacts_mobile = m.get('ContactsMobile')
        if m.get('ContactsName') is not None:
            self.contacts_name = m.get('ContactsName')
        if m.get('IndustryCategory') is not None:
            self.industry_category = m.get('IndustryCategory')
        if m.get('ScenceDesc') is not None:
            self.scence_desc = m.get('ScenceDesc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class GetTenantResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: GetTenantResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTenantResponseBody, self).to_map()
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
            temp_model = GetTenantResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTenantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetTenantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTenantResponse, self).to_map()
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
            temp_model = GetTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppRequest(TeaModel):
    def __init__(self, key_search=None, page_number=None, page_size=None):
        self.key_search = key_search  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppResponseBodyApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_type=None, gmt_create=None, gmt_modified=None,
                 version_adapt_num=None, version_total_num=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.version_adapt_num = version_adapt_num  # type: long
        self.version_total_num = version_total_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppResponseBodyApps, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.version_adapt_num is not None:
            result['VersionAdaptNum'] = self.version_adapt_num
        if self.version_total_num is not None:
            result['VersionTotalNum'] = self.version_total_num
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('VersionAdaptNum') is not None:
            self.version_adapt_num = m.get('VersionAdaptNum')
        if m.get('VersionTotalNum') is not None:
            self.version_total_num = m.get('VersionTotalNum')
        return self


class ListAppResponseBody(TeaModel):
    def __init__(self, apps=None, request_id=None, total=None):
        self.apps = apps  # type: list[ListAppResponseBodyApps]
        self.request_id = request_id  # type: str
        self.total = total  # type: long

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = ListAppResponseBodyApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppResponse, self).to_map()
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
            temp_model = ListAppResponseBody()
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


class ListAppSessionsResponseBodyAppSessionsBizInfo(TeaModel):
    def __init__(self, start_time=None, stop_time=None):
        self.start_time = start_time  # type: str
        self.stop_time = stop_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppSessionsResponseBodyAppSessionsBizInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        return self


class ListAppSessionsResponseBodyAppSessions(TeaModel):
    def __init__(self, app_id=None, app_version=None, biz_info=None, custom_session_id=None,
                 platform_session_id=None, status=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 应用版本
        self.app_version = app_version  # type: str
        self.biz_info = biz_info  # type: ListAppSessionsResponseBodyAppSessionsBizInfo
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 平台会话id
        self.platform_session_id = platform_session_id  # type: str
        # 状态
        self.status = status  # type: str

    def validate(self):
        if self.biz_info:
            self.biz_info.validate()

    def to_map(self):
        _map = super(ListAppSessionsResponseBodyAppSessions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.biz_info is not None:
            result['BizInfo'] = self.biz_info.to_map()
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
        if m.get('BizInfo') is not None:
            temp_model = ListAppSessionsResponseBodyAppSessionsBizInfo()
            self.biz_info = temp_model.from_map(m['BizInfo'])
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListAppSessionsResponseBody(TeaModel):
    def __init__(self, app_sessions=None, page_number=None, page_size=None, request_id=None, total_count=None):
        self.app_sessions = app_sessions  # type: list[ListAppSessionsResponseBodyAppSessions]
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        # 请求id
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

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
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
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
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class ListAppVersionRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None):
        self.app_id = app_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAppVersionResponseBodyVersions(TeaModel):
    def __init__(self, app_id=None, app_version_id=None, app_version_name=None, app_version_status=None,
                 app_version_status_memo=None, consume_cu=None, file_address=None, file_size=None, file_upload_finish_time=None,
                 file_upload_type=None, gmt_create=None, gmt_modified=None):
        self.app_id = app_id  # type: str
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.app_version_status = app_version_status  # type: str
        self.app_version_status_memo = app_version_status_memo  # type: str
        self.consume_cu = consume_cu  # type: float
        self.file_address = file_address  # type: str
        self.file_size = file_size  # type: long
        self.file_upload_finish_time = file_upload_finish_time  # type: str
        self.file_upload_type = file_upload_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAppVersionResponseBodyVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_status is not None:
            result['AppVersionStatus'] = self.app_version_status
        if self.app_version_status_memo is not None:
            result['AppVersionStatusMemo'] = self.app_version_status_memo
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_finish_time is not None:
            result['FileUploadFinishTime'] = self.file_upload_finish_time
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionStatus') is not None:
            self.app_version_status = m.get('AppVersionStatus')
        if m.get('AppVersionStatusMemo') is not None:
            self.app_version_status_memo = m.get('AppVersionStatusMemo')
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadFinishTime') is not None:
            self.file_upload_finish_time = m.get('FileUploadFinishTime')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        return self


class ListAppVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, total=None, versions=None):
        self.request_id = request_id  # type: str
        self.total = total  # type: long
        self.versions = versions  # type: list[ListAppVersionResponseBodyVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAppVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = ListAppVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListAppVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAppVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAppVersionResponse, self).to_map()
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
            temp_model = ListAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class ModifyAppResponseBody(TeaModel):
    def __init__(self, app_id=None, request_id=None):
        self.app_id = app_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppResponse, self).to_map()
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
            temp_model = ModifyAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAppVersionRequest(TeaModel):
    def __init__(self, app_version_id=None, app_version_name=None):
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class ModifyAppVersionResponseBody(TeaModel):
    def __init__(self, app_version_id=None, request_id=None):
        self.app_version_id = app_version_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAppVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyAppVersionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAppVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAppVersionResponse, self).to_map()
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
            temp_model = ModifyAppVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyProjectRequestProjectQuotaLimit(TeaModel):
    def __init__(self, district_limit_map=None, limit_type=None):
        # key - districtId
        self.district_limit_map = district_limit_map  # type: dict[str, ProjectQuotaLimitDistrictLimitMapValue]
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(ModifyProjectRequestProjectQuotaLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = ProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class ModifyProjectRequest(TeaModel):
    def __init__(self, bound_app_id_list=None, operator_id=None, operator_type=None, project_id=None,
                 project_memo=None, project_name=None, project_quota_limit=None):
        self.bound_app_id_list = bound_app_id_list  # type: list[str]
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # project Id
        self.project_id = project_id  # type: str
        self.project_memo = project_memo  # type: str
        # project name
        self.project_name = project_name  # type: str
        # key : districtId
        self.project_quota_limit = project_quota_limit  # type: ModifyProjectRequestProjectQuotaLimit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super(ModifyProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list is not None:
            result['BoundAppIdList'] = self.bound_app_id_list
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = ModifyProjectRequestProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class ModifyProjectShrinkRequest(TeaModel):
    def __init__(self, bound_app_id_list_shrink=None, operator_id=None, operator_type=None, project_id=None,
                 project_memo=None, project_name=None, project_quota_limit_shrink=None):
        self.bound_app_id_list_shrink = bound_app_id_list_shrink  # type: str
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # project Id
        self.project_id = project_id  # type: str
        self.project_memo = project_memo  # type: str
        # project name
        self.project_name = project_name  # type: str
        # key : districtId
        self.project_quota_limit_shrink = project_quota_limit_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProjectShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_id_list_shrink is not None:
            result['BoundAppIdList'] = self.bound_app_id_list_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit_shrink is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BoundAppIdList') is not None:
            self.bound_app_id_list_shrink = m.get('BoundAppIdList')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            self.project_quota_limit_shrink = m.get('ProjectQuotaLimit')
        return self


class ModifyProjectResponseBodyData(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: ModifyProjectResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ModifyProjectResponseBody, self).to_map()
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
            temp_model = ModifyProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyProjectResponse, self).to_map()
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
            temp_model = ModifyProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryProjectRequest(TeaModel):
    def __init__(self, key_search=None, operator_id=None, operator_type=None, page_number=None, page_size=None):
        # projectId or projectName like
        self.key_search = key_search  # type: str
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 当前页码，默认1
        self.page_number = page_number  # type: int
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageQueryProjectRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit(TeaModel):
    def __init__(self, district_limit_map=None, limit_type=None):
        # key - districtId
        self.district_limit_map = district_limit_map  # type: dict[str, DataRecordsProjectQuotaLimitDistrictLimitMapValue]
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = DataRecordsProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class PageQueryProjectResponseBodyDataRecords(TeaModel):
    def __init__(self, bound_app_nums=None, gmt_create=None, gmt_modified=None, project_id=None, project_memo=None,
                 project_name=None, project_quota_limit=None):
        # 项目关联的应用数量
        self.bound_app_nums = bound_app_nums  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.project_id = project_id  # type: str
        self.project_memo = project_memo  # type: str
        self.project_name = project_name  # type: str
        # key : districtId
        self.project_quota_limit = project_quota_limit  # type: PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super(PageQueryProjectResponseBodyDataRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bound_app_nums is not None:
            result['BoundAppNums'] = self.bound_app_nums
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.project_memo is not None:
            result['ProjectMemo'] = self.project_memo
        if self.project_name is not None:
            result['ProjectName'] = self.project_name
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BoundAppNums') is not None:
            self.bound_app_nums = m.get('BoundAppNums')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ProjectMemo') is not None:
            self.project_memo = m.get('ProjectMemo')
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = PageQueryProjectResponseBodyDataRecordsProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        return self


class PageQueryProjectResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, pages=None, records=None, total_count=None):
        # 当前页码，默认1
        self.page_number = page_number  # type: long
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: long
        # 总页数
        self.pages = pages  # type: long
        # 结果集
        self.records = records  # type: list[PageQueryProjectResponseBodyDataRecords]
        # 总共项数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PageQueryProjectResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PageQueryProjectResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageQueryProjectResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: PageQueryProjectResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PageQueryProjectResponseBody, self).to_map()
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
            temp_model = PageQueryProjectResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageQueryProjectResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PageQueryProjectResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageQueryProjectResponse, self).to_map()
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
            temp_model = PageQueryProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryProjectAppsRequest(TeaModel):
    def __init__(self, app_id=None, operator_id=None, operator_type=None, page_number=None, page_size=None,
                 project_id=None):
        self.app_id = app_id  # type: str
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 当前页码，默认1
        self.page_number = page_number  # type: int
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: int
        # projectId
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageQueryProjectAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PageQueryProjectAppsResponseBodyDataRecords(TeaModel):
    def __init__(self, app_id=None, app_name=None, gmt_create=None, project_id=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.gmt_create = gmt_create  # type: str
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageQueryProjectAppsResponseBodyDataRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class PageQueryProjectAppsResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, pages=None, records=None, total_count=None):
        # 当前页码，默认1
        self.page_number = page_number  # type: long
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: long
        # 总页数
        self.pages = pages  # type: long
        # 结果集
        self.records = records  # type: list[PageQueryProjectAppsResponseBodyDataRecords]
        # 总共项数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PageQueryProjectAppsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pages is not None:
            result['Pages'] = self.pages
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Pages') is not None:
            self.pages = m.get('Pages')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = PageQueryProjectAppsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageQueryProjectAppsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: PageQueryProjectAppsResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PageQueryProjectAppsResponseBody, self).to_map()
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
            temp_model = PageQueryProjectAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageQueryProjectAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PageQueryProjectAppsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageQueryProjectAppsResponse, self).to_map()
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
            temp_model = PageQueryProjectAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDistrictMetaResponseBodyDataProjectQuotaLimit(TeaModel):
    def __init__(self, district_limit_map=None, limit_type=None):
        # key - districtId
        self.district_limit_map = district_limit_map  # type: dict[str, DataProjectQuotaLimitDistrictLimitMapValue]
        # 限制类型 ：目前默认 - ReserveContainer
        self.limit_type = limit_type  # type: str

    def validate(self):
        if self.district_limit_map:
            for v in self.district_limit_map.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(RefreshDistrictMetaResponseBodyDataProjectQuotaLimit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DistrictLimitMap'] = {}
        if self.district_limit_map is not None:
            for k, v in self.district_limit_map.items():
                result['DistrictLimitMap'][k] = v.to_map()
        if self.limit_type is not None:
            result['LimitType'] = self.limit_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.district_limit_map = {}
        if m.get('DistrictLimitMap') is not None:
            for k, v in m.get('DistrictLimitMap').items():
                temp_model = DataProjectQuotaLimitDistrictLimitMapValue()
                self.district_limit_map[k] = temp_model.from_map(v)
        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')
        return self


class RefreshDistrictMetaResponseBodyData(TeaModel):
    def __init__(self, code=None, data=None, message=None, project_quota_limit=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: dict[str, any]
        # 业务处理消息摘要
        self.message = message  # type: str
        self.project_quota_limit = project_quota_limit  # type: RefreshDistrictMetaResponseBodyDataProjectQuotaLimit
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.project_quota_limit:
            self.project_quota_limit.validate()

    def to_map(self):
        _map = super(RefreshDistrictMetaResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.project_quota_limit is not None:
            result['ProjectQuotaLimit'] = self.project_quota_limit.to_map()
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ProjectQuotaLimit') is not None:
            temp_model = RefreshDistrictMetaResponseBodyDataProjectQuotaLimit()
            self.project_quota_limit = temp_model.from_map(m['ProjectQuotaLimit'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshDistrictMetaResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: RefreshDistrictMetaResponseBodyData
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RefreshDistrictMetaResponseBody, self).to_map()
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
            temp_model = RefreshDistrictMetaResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshDistrictMetaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshDistrictMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshDistrictMetaResponse, self).to_map()
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
            temp_model = RefreshDistrictMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseCapacityRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, district_id=None, expect_release_session_capacity=None,
                 project_id=None):
        # app id
        self.app_id = app_id  # type: str
        self.app_version = app_version  # type: str
        # 大区 id
        self.district_id = district_id  # type: str
        # 期望释放的会话路数
        self.expect_release_session_capacity = expect_release_session_capacity  # type: int
        # 项目 id
        self.project_id = project_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseCapacityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.expect_release_session_capacity is not None:
            result['ExpectReleaseSessionCapacity'] = self.expect_release_session_capacity
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('ExpectReleaseSessionCapacity') is not None:
            self.expect_release_session_capacity = m.get('ExpectReleaseSessionCapacity')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ReleaseCapacityResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # pop的requestId
        self.request_id = request_id  # type: str
        # 容器异步释放任务 id
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReleaseCapacityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReleaseCapacityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReleaseCapacityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReleaseCapacityResponse, self).to_map()
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
            temp_model = ReleaseCapacityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopAppSessionRequestStopParam(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionRequestStopParam, self).to_map()
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


class StopAppSessionRequest(TeaModel):
    def __init__(self, custom_session_id=None, platform_session_id=None, stop_param=None):
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 自定义用户id
        self.platform_session_id = platform_session_id  # type: str
        self.stop_param = stop_param  # type: list[StopAppSessionRequestStopParam]

    def validate(self):
        if self.stop_param:
            for k in self.stop_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StopAppSessionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        result['StopParam'] = []
        if self.stop_param is not None:
            for k in self.stop_param:
                result['StopParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        self.stop_param = []
        if m.get('StopParam') is not None:
            for k in m.get('StopParam'):
                temp_model = StopAppSessionRequestStopParam()
                self.stop_param.append(temp_model.from_map(k))
        return self


class StopAppSessionShrinkRequest(TeaModel):
    def __init__(self, custom_session_id=None, platform_session_id=None, stop_param_shrink=None):
        # 自定义会话id
        self.custom_session_id = custom_session_id  # type: str
        # 自定义用户id
        self.platform_session_id = platform_session_id  # type: str
        self.stop_param_shrink = stop_param_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_session_id is not None:
            result['CustomSessionId'] = self.custom_session_id
        if self.platform_session_id is not None:
            result['PlatformSessionId'] = self.platform_session_id
        if self.stop_param_shrink is not None:
            result['StopParam'] = self.stop_param_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomSessionId') is not None:
            self.custom_session_id = m.get('CustomSessionId')
        if m.get('PlatformSessionId') is not None:
            self.platform_session_id = m.get('PlatformSessionId')
        if m.get('StopParam') is not None:
            self.stop_param_shrink = m.get('StopParam')
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


class StopAppSessionBatchRequestStopParam(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionBatchRequestStopParam, self).to_map()
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


class StopAppSessionBatchRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionBatchRequestTags, self).to_map()
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


class StopAppSessionBatchRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, batch_id=None, project_id=None, stop_param=None, tags=None):
        self.app_id = app_id  # type: str
        self.app_version = app_version  # type: str
        # 自定义用户id
        self.batch_id = batch_id  # type: str
        # 自定义会话id
        self.project_id = project_id  # type: str
        self.stop_param = stop_param  # type: list[StopAppSessionBatchRequestStopParam]
        self.tags = tags  # type: list[StopAppSessionBatchRequestTags]

    def validate(self):
        if self.stop_param:
            for k in self.stop_param:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StopAppSessionBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        result['StopParam'] = []
        if self.stop_param is not None:
            for k in self.stop_param:
                result['StopParam'].append(k.to_map() if k else None)
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        self.stop_param = []
        if m.get('StopParam') is not None:
            for k in m.get('StopParam'):
                temp_model = StopAppSessionBatchRequestStopParam()
                self.stop_param.append(temp_model.from_map(k))
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = StopAppSessionBatchRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class StopAppSessionBatchShrinkRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionBatchShrinkRequestTags, self).to_map()
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


class StopAppSessionBatchShrinkRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, batch_id=None, project_id=None, stop_param_shrink=None,
                 tags=None):
        self.app_id = app_id  # type: str
        self.app_version = app_version  # type: str
        # 自定义用户id
        self.batch_id = batch_id  # type: str
        # 自定义会话id
        self.project_id = project_id  # type: str
        self.stop_param_shrink = stop_param_shrink  # type: str
        self.tags = tags  # type: list[StopAppSessionBatchShrinkRequestTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StopAppSessionBatchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version is not None:
            result['AppVersion'] = self.app_version
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.stop_param_shrink is not None:
            result['StopParam'] = self.stop_param_shrink
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersion') is not None:
            self.app_version = m.get('AppVersion')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('StopParam') is not None:
            self.stop_param_shrink = m.get('StopParam')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = StopAppSessionBatchShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class StopAppSessionBatchResponseBody(TeaModel):
    def __init__(self, app_id=None, batch_id=None, project_id=None, request_id=None):
        # 应用id
        self.app_id = app_id  # type: str
        # 自定义会话id
        self.batch_id = batch_id  # type: str
        # 平台会话id
        self.project_id = project_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopAppSessionBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopAppSessionBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopAppSessionBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopAppSessionBatchResponse, self).to_map()
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
            temp_model = StopAppSessionBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VersionCheckSameNameServiceRequest(TeaModel):
    def __init__(self, app_id=None, app_version_name=None):
        self.app_id = app_id  # type: str
        self.app_version_name = app_version_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VersionCheckSameNameServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        return self


class VersionCheckSameNameServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VersionCheckSameNameServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VersionCheckSameNameServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: VersionCheckSameNameServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VersionCheckSameNameServiceResponse, self).to_map()
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
            temp_model = VersionCheckSameNameServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProjectQuotaLimitDistrictLimitMapValue(TeaModel):
    def __init__(self, district_id=None, district_name=None, max_limit=None):
        # 大区ID
        self.district_id = district_id  # type: str
        # 大区名称
        self.district_name = district_name  # type: str
        # 上限
        self.max_limit = max_limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ProjectQuotaLimitDistrictLimitMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_name is not None:
            result['DistrictName'] = self.district_name
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictName') is not None:
            self.district_name = m.get('DistrictName')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        return self


class DataProjectQuotaLimitDistrictLimitMapValue(TeaModel):
    def __init__(self, district_id=None, district_name=None, max_limit=None):
        # 大区ID
        self.district_id = district_id  # type: str
        # 大区名称
        self.district_name = district_name  # type: str
        # 上限
        self.max_limit = max_limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataProjectQuotaLimitDistrictLimitMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_name is not None:
            result['DistrictName'] = self.district_name
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictName') is not None:
            self.district_name = m.get('DistrictName')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        return self


class DataRecordsProjectQuotaLimitDistrictLimitMapValue(TeaModel):
    def __init__(self, district_id=None, district_name=None, max_limit=None):
        # 大区ID
        self.district_id = district_id  # type: str
        # 大区名称
        self.district_name = district_name  # type: str
        # 上限
        self.max_limit = max_limit  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataRecordsProjectQuotaLimitDistrictLimitMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.district_id is not None:
            result['DistrictId'] = self.district_id
        if self.district_name is not None:
            result['DistrictName'] = self.district_name
        if self.max_limit is not None:
            result['MaxLimit'] = self.max_limit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DistrictId') is not None:
            self.district_id = m.get('DistrictId')
        if m.get('DistrictName') is not None:
            self.district_name = m.get('DistrictName')
        if m.get('MaxLimit') is not None:
            self.max_limit = m.get('MaxLimit')
        return self


