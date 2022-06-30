# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


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


class CreateAppSessionRequestResultStoreStoreInfo(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionRequestResultStoreStoreInfo, self).to_map()
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


class CreateAppSessionRequestResultStore(TeaModel):
    def __init__(self, need=None, store_info=None, type=None):
        self.need = need  # type: bool
        self.store_info = store_info  # type: list[CreateAppSessionRequestResultStoreStoreInfo]
        self.type = type  # type: str

    def validate(self):
        if self.store_info:
            for k in self.store_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionRequestResultStore, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need is not None:
            result['Need'] = self.need
        result['StoreInfo'] = []
        if self.store_info is not None:
            for k in self.store_info:
                result['StoreInfo'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Need') is not None:
            self.need = m.get('Need')
        self.store_info = []
        if m.get('StoreInfo') is not None:
            for k in m.get('StoreInfo'):
                temp_model = CreateAppSessionRequestResultStoreStoreInfo()
                self.store_info.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
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


class CreateAppSessionRequestStartParametersV2(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionRequestStartParametersV2, self).to_map()
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
                 dataset_id=None, enable_postpaid=None, result_store=None, start_parameters=None, start_parameters_v2=None,
                 system_info=None, timeout=None):
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
        self.dataset_id = dataset_id  # type: str
        self.enable_postpaid = enable_postpaid  # type: bool
        self.result_store = result_store  # type: CreateAppSessionRequestResultStore
        # 启动参数
        self.start_parameters = start_parameters  # type: list[CreateAppSessionRequestStartParameters]
        self.start_parameters_v2 = start_parameters_v2  # type: list[CreateAppSessionRequestStartParametersV2]
        # 系统信息：如端侧机型等信息
        self.system_info = system_info  # type: list[CreateAppSessionRequestSystemInfo]
        self.timeout = timeout  # type: long

    def validate(self):
        if self.result_store:
            self.result_store.validate()
        if self.start_parameters:
            for k in self.start_parameters:
                if k:
                    k.validate()
        if self.start_parameters_v2:
            for k in self.start_parameters_v2:
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
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.enable_postpaid is not None:
            result['EnablePostpaid'] = self.enable_postpaid
        if self.result_store is not None:
            result['ResultStore'] = self.result_store.to_map()
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['StartParametersV2'] = []
        if self.start_parameters_v2 is not None:
            for k in self.start_parameters_v2:
                result['StartParametersV2'].append(k.to_map() if k else None)
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
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('EnablePostpaid') is not None:
            self.enable_postpaid = m.get('EnablePostpaid')
        if m.get('ResultStore') is not None:
            temp_model = CreateAppSessionRequestResultStore()
            self.result_store = temp_model.from_map(m['ResultStore'])
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.start_parameters_v2 = []
        if m.get('StartParametersV2') is not None:
            for k in m.get('StartParametersV2'):
                temp_model = CreateAppSessionRequestStartParametersV2()
                self.start_parameters_v2.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionRequestSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionShrinkRequestStartParameters(TeaModel):
    def __init__(self, key=None, value=None):
        # key
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionShrinkRequestStartParameters, self).to_map()
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


class CreateAppSessionShrinkRequestSystemInfo(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionShrinkRequestSystemInfo, self).to_map()
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


class CreateAppSessionShrinkRequest(TeaModel):
    def __init__(self, app_id=None, app_version=None, client_ip=None, custom_session_id=None, custom_user_id=None,
                 dataset_id=None, enable_postpaid=None, result_store_shrink=None, start_parameters=None,
                 start_parameters_v2shrink=None, system_info=None, timeout=None):
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
        self.dataset_id = dataset_id  # type: str
        self.enable_postpaid = enable_postpaid  # type: bool
        self.result_store_shrink = result_store_shrink  # type: str
        # 启动参数
        self.start_parameters = start_parameters  # type: list[CreateAppSessionShrinkRequestStartParameters]
        self.start_parameters_v2shrink = start_parameters_v2shrink  # type: str
        # 系统信息：如端侧机型等信息
        self.system_info = system_info  # type: list[CreateAppSessionShrinkRequestSystemInfo]
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
        _map = super(CreateAppSessionShrinkRequest, self).to_map()
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
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.enable_postpaid is not None:
            result['EnablePostpaid'] = self.enable_postpaid
        if self.result_store_shrink is not None:
            result['ResultStore'] = self.result_store_shrink
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        if self.start_parameters_v2shrink is not None:
            result['StartParametersV2'] = self.start_parameters_v2shrink
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
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('EnablePostpaid') is not None:
            self.enable_postpaid = m.get('EnablePostpaid')
        if m.get('ResultStore') is not None:
            self.result_store_shrink = m.get('ResultStore')
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionShrinkRequestStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        if m.get('StartParametersV2') is not None:
            self.start_parameters_v2shrink = m.get('StartParametersV2')
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionShrinkRequestSystemInfo()
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


class CreateDatasetDeployTaskRequest(TeaModel):
    def __init__(self, client_token=None, custom_param=None, need_unzip=None, oss_bucket=None, oss_file_path=None,
                 oss_region_id=None, source_type=None):
        self.client_token = client_token  # type: str
        self.custom_param = custom_param  # type: str
        self.need_unzip = need_unzip  # type: bool
        self.oss_bucket = oss_bucket  # type: str
        self.oss_file_path = oss_file_path  # type: str
        self.oss_region_id = oss_region_id  # type: str
        self.source_type = source_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasetDeployTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.custom_param is not None:
            result['CustomParam'] = self.custom_param
        if self.need_unzip is not None:
            result['NeedUnzip'] = self.need_unzip
        if self.oss_bucket is not None:
            result['OssBucket'] = self.oss_bucket
        if self.oss_file_path is not None:
            result['OssFilePath'] = self.oss_file_path
        if self.oss_region_id is not None:
            result['OssRegionId'] = self.oss_region_id
        if self.source_type is not None:
            result['SourceType'] = self.source_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CustomParam') is not None:
            self.custom_param = m.get('CustomParam')
        if m.get('NeedUnzip') is not None:
            self.need_unzip = m.get('NeedUnzip')
        if m.get('OssBucket') is not None:
            self.oss_bucket = m.get('OssBucket')
        if m.get('OssFilePath') is not None:
            self.oss_file_path = m.get('OssFilePath')
        if m.get('OssRegionId') is not None:
            self.oss_region_id = m.get('OssRegionId')
        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')
        return self


class CreateDatasetDeployTaskResponseBody(TeaModel):
    def __init__(self, request_id=None, task_id=None):
        # 请求id
        self.request_id = request_id  # type: str
        # 应用版本
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDatasetDeployTaskResponseBody, self).to_map()
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


class CreateDatasetDeployTaskResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDatasetDeployTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDatasetDeployTaskResponse, self).to_map()
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
            temp_model = CreateDatasetDeployTaskResponseBody()
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


class GetDatasetRequest(TeaModel):
    def __init__(self, dataset_id=None):
        self.dataset_id = dataset_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        return self


class GetDatasetResponseBody(TeaModel):
    def __init__(self, custom_param=None, dataset_id=None, dataset_size=None, request_id=None):
        # 应用id
        self.custom_param = custom_param  # type: str
        # 自定义会话id
        self.dataset_id = dataset_id  # type: str
        self.dataset_size = dataset_size  # type: long
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDatasetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_param is not None:
            result['CustomParam'] = self.custom_param
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id
        if self.dataset_size is not None:
            result['DatasetSize'] = self.dataset_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomParam') is not None:
            self.custom_param = m.get('CustomParam')
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')
        if m.get('DatasetSize') is not None:
            self.dataset_size = m.get('DatasetSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDatasetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDatasetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDatasetResponse, self).to_map()
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
            temp_model = GetDatasetResponseBody()
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


