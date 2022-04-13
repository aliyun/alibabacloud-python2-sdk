# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AdaptCreateServiceRequestAdaptTarget(TeaModel):
    def __init__(self, bit_rate=None, frame_rate=None, resolution=None, start_program=None):
        self.bit_rate = bit_rate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.resolution = resolution  # type: str
        self.start_program = start_program  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdaptCreateServiceRequestAdaptTarget, self).to_map()
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


class AdaptCreateServiceRequest(TeaModel):
    def __init__(self, adapt_target=None, app_version_id=None, app_version_name=None, request_app=None):
        self.adapt_target = adapt_target  # type: AdaptCreateServiceRequestAdaptTarget
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super(AdaptCreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            temp_model = AdaptCreateServiceRequestAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AdaptCreateServiceShrinkRequest(TeaModel):
    def __init__(self, adapt_target_shrink=None, app_version_id=None, app_version_name=None, request_app=None):
        self.adapt_target_shrink = adapt_target_shrink  # type: str
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdaptCreateServiceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_target_shrink is not None:
            result['AdaptTarget'] = self.adapt_target_shrink
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptTarget') is not None:
            self.adapt_target_shrink = m.get('AdaptTarget')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AdaptCreateServiceResponseBodyData(TeaModel):
    def __init__(self, adapt_apply_id=None):
        self.adapt_apply_id = adapt_apply_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdaptCreateServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        return self


class AdaptCreateServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AdaptCreateServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AdaptCreateServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AdaptCreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AdaptCreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AdaptCreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AdaptCreateServiceResponse, self).to_map()
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
            temp_model = AdaptCreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AdaptGetServiceRequest(TeaModel):
    def __init__(self, app_version_id=None, request_app=None):
        self.app_version_id = app_version_id  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdaptGetServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AdaptGetServiceResponseBodyDataAdaptTarget(TeaModel):
    def __init__(self, bit_rate=None, frame_rate=None, resolution=None, start_program=None):
        self.bit_rate = bit_rate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.resolution = resolution  # type: str
        self.start_program = start_program  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AdaptGetServiceResponseBodyDataAdaptTarget, self).to_map()
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


class AdaptGetServiceResponseBodyData(TeaModel):
    def __init__(self, adapt_status=None, adapt_target=None, app_id=None, app_version_id=None, gmt_create=None,
                 gmt_modified=None, id=None, tenant_id=None):
        self.adapt_status = adapt_status  # type: str
        self.adapt_target = adapt_target  # type: AdaptGetServiceResponseBodyDataAdaptTarget
        self.app_id = app_id  # type: str
        self.app_version_id = app_version_id  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()

    def to_map(self):
        _map = super(AdaptGetServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_status is not None:
            result['AdaptStatus'] = self.adapt_status
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
        if self.id is not None:
            result['Id'] = self.id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptStatus') is not None:
            self.adapt_status = m.get('AdaptStatus')
        if m.get('AdaptTarget') is not None:
            temp_model = AdaptGetServiceResponseBodyDataAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AdaptGetServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AdaptGetServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AdaptGetServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AdaptGetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AdaptGetServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AdaptGetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AdaptGetServiceResponse, self).to_map()
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
            temp_model = AdaptGetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppCreateServiceRequest(TeaModel):
    def __init__(self, app_name=None, app_type=None, request_app=None):
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppCreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppCreateServiceResponseBodyData(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppCreateServiceResponseBodyData, self).to_map()
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


class AppCreateServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppCreateServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppCreateServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppCreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppCreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppCreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppCreateServiceResponse, self).to_map()
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
            temp_model = AppCreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppDeleteServiceRequest(TeaModel):
    def __init__(self, app_id=None, request_app=None):
        self.app_id = app_id  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppDeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppDeleteServiceResponseBodyData(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppDeleteServiceResponseBodyData, self).to_map()
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


class AppDeleteServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppDeleteServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppDeleteServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppDeleteServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppDeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppDeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppDeleteServiceResponse, self).to_map()
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
            temp_model = AppDeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppGetServiceRequest(TeaModel):
    def __init__(self, app_id=None, request_app=None):
        self.app_id = app_id  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppGetServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppGetServiceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_type=None, biz_type=None, gmt_create=None, gmt_modified=None,
                 tenant_id=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.biz_type = biz_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppGetServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppGetServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppGetServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppGetServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppGetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppGetServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppGetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppGetServiceResponse, self).to_map()
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
            temp_model = AppGetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppListServiceRequest(TeaModel):
    def __init__(self, key_search=None, page_number=None, page_size=None, request_app=None):
        self.key_search = key_search  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppListServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppListServiceResponseBodyDataApps(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_type=None, gmt_create=None, gmt_modified=None, tenant_id=None,
                 version_adapt_num=None, version_total_num=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.tenant_id = tenant_id  # type: long
        self.version_adapt_num = version_adapt_num  # type: long
        self.version_total_num = version_total_num  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppListServiceResponseBodyDataApps, self).to_map()
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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VersionAdaptNum') is not None:
            self.version_adapt_num = m.get('VersionAdaptNum')
        if m.get('VersionTotalNum') is not None:
            self.version_total_num = m.get('VersionTotalNum')
        return self


class AppListServiceResponseBodyData(TeaModel):
    def __init__(self, apps=None, total=None):
        self.apps = apps  # type: list[AppListServiceResponseBodyDataApps]
        self.total = total  # type: long

    def validate(self):
        if self.apps:
            for k in self.apps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AppListServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Apps'] = []
        if self.apps is not None:
            for k in self.apps:
                result['Apps'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.apps = []
        if m.get('Apps') is not None:
            for k in m.get('Apps'):
                temp_model = AppListServiceResponseBodyDataApps()
                self.apps.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class AppListServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppListServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppListServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppListServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppListServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppListServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppListServiceResponse, self).to_map()
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
            temp_model = AppListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppModifyServiceRequest(TeaModel):
    def __init__(self, app_id=None, app_name=None, request_app=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppModifyServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppModifyServiceResponseBodyData(TeaModel):
    def __init__(self, app_id=None):
        self.app_id = app_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppModifyServiceResponseBodyData, self).to_map()
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


class AppModifyServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppModifyServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppModifyServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppModifyServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppModifyServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppModifyServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppModifyServiceResponse, self).to_map()
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
            temp_model = AppModifyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionCreateServiceRequest(TeaModel):
    def __init__(self, app_id=None, app_version_name=None, file_address=None, file_size=None, file_upload_type=None,
                 request_app=None):
        self.app_id = app_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.file_address = file_address  # type: str
        self.file_size = file_size  # type: long
        self.file_upload_type = file_upload_type  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionCreateServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_upload_type is not None:
            result['FileUploadType'] = self.file_upload_type
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileUploadType') is not None:
            self.file_upload_type = m.get('FileUploadType')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionCreateServiceResponseBodyData(TeaModel):
    def __init__(self, app_version_id=None):
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionCreateServiceResponseBodyData, self).to_map()
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


class AppVersionCreateServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppVersionCreateServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppVersionCreateServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionCreateServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionCreateServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppVersionCreateServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppVersionCreateServiceResponse, self).to_map()
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
            temp_model = AppVersionCreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionDeleteServiceRequest(TeaModel):
    def __init__(self, app_version_id=None, request_app=None):
        self.app_version_id = app_version_id  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionDeleteServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionDeleteServiceResponseBodyData(TeaModel):
    def __init__(self, app_version_id=None):
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionDeleteServiceResponseBodyData, self).to_map()
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


class AppVersionDeleteServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppVersionDeleteServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppVersionDeleteServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionDeleteServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionDeleteServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppVersionDeleteServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppVersionDeleteServiceResponse, self).to_map()
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
            temp_model = AppVersionDeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionGetServiceRequest(TeaModel):
    def __init__(self, app_version_id=None, request_app=None):
        self.app_version_id = app_version_id  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionGetServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionGetServiceResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_version_id=None, app_version_name=None, app_version_status=None,
                 app_version_status_memo=None, consume_cu=None, file_address=None, file_size=None, file_upload_finish_time=None,
                 file_upload_type=None, gmt_create=None, gmt_modified=None, source_version_id=None, tenant_id=None):
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
        self.source_version_id = source_version_id  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionGetServiceResponseBodyData, self).to_map()
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
        if self.source_version_id is not None:
            result['SourceVersionId'] = self.source_version_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
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
        if m.get('SourceVersionId') is not None:
            self.source_version_id = m.get('SourceVersionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppVersionGetServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppVersionGetServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppVersionGetServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionGetServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionGetServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppVersionGetServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppVersionGetServiceResponse, self).to_map()
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
            temp_model = AppVersionGetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionListServiceRequest(TeaModel):
    def __init__(self, app_id=None, page_number=None, page_size=None, request_app=None):
        self.app_id = app_id  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionListServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionListServiceResponseBodyDataVersions(TeaModel):
    def __init__(self, app_id=None, app_version_id=None, app_version_name=None, app_version_status=None,
                 app_version_status_memo=None, consume_cu=None, file_address=None, file_size=None, file_upload_finish_time=None,
                 file_upload_type=None, gmt_create=None, gmt_modified=None, tenant_id=None):
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
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionListServiceResponseBodyDataVersions, self).to_map()
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
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
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
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppVersionListServiceResponseBodyData(TeaModel):
    def __init__(self, total=None, versions=None):
        self.total = total  # type: long
        self.versions = versions  # type: list[AppVersionListServiceResponseBodyDataVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AppVersionListServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = AppVersionListServiceResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class AppVersionListServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppVersionListServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppVersionListServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionListServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionListServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppVersionListServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppVersionListServiceResponse, self).to_map()
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
            temp_model = AppVersionListServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionModifyServiceRequest(TeaModel):
    def __init__(self, app_version_id=None, app_version_name=None, request_app=None):
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionModifyServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionModifyServiceResponseBodyData(TeaModel):
    def __init__(self, app_version_id=None):
        self.app_version_id = app_version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionModifyServiceResponseBodyData, self).to_map()
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


class AppVersionModifyServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppVersionModifyServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppVersionModifyServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionModifyServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionModifyServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppVersionModifyServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppVersionModifyServiceResponse, self).to_map()
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
            temp_model = AppVersionModifyServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppVersionQueryServiceRequest(TeaModel):
    def __init__(self, key_search=None, page_number=None, page_size=None, request_app=None):
        self.key_search = key_search  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionQueryServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key_search is not None:
            result['KeySearch'] = self.key_search
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KeySearch') is not None:
            self.key_search = m.get('KeySearch')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class AppVersionQueryServiceResponseBodyDataVersions(TeaModel):
    def __init__(self, app_id=None, app_name=None, app_version_id=None, app_version_name=None, tenant_id=None):
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppVersionQueryServiceResponseBodyDataVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class AppVersionQueryServiceResponseBodyData(TeaModel):
    def __init__(self, total=None, versions=None):
        self.total = total  # type: long
        self.versions = versions  # type: list[AppVersionQueryServiceResponseBodyDataVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AppVersionQueryServiceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['Total'] = self.total
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = AppVersionQueryServiceResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class AppVersionQueryServiceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AppVersionQueryServiceResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AppVersionQueryServiceResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = AppVersionQueryServiceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AppVersionQueryServiceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppVersionQueryServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppVersionQueryServiceResponse, self).to_map()
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
            temp_model = AppVersionQueryServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppliedConsumStatRequest(TeaModel):
    def __init__(self, applied_id=None, operator_id=None, operator_type=None, package_type=None,
                 query_end_date=None, query_start_date=None):
        self.applied_id = applied_id  # type: list[str]
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 查询结束时间
        self.query_end_date = query_end_date  # type: str
        # 查询开始时间
        self.query_start_date = query_start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedConsumStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class AppliedConsumStatShrinkRequest(TeaModel):
    def __init__(self, applied_id_shrink=None, operator_id=None, operator_type=None, package_type=None,
                 query_end_date=None, query_start_date=None):
        self.applied_id_shrink = applied_id_shrink  # type: str
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 查询结束时间
        self.query_end_date = query_end_date  # type: str
        # 查询开始时间
        self.query_start_date = query_start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedConsumStatShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id_shrink is not None:
            result['AppliedId'] = self.applied_id_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id_shrink = m.get('AppliedId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class AppliedConsumStatResponseBodyData(TeaModel):
    def __init__(self, applied_consumption_map=None):
        # 应用消耗Cu统计
        self.applied_consumption_map = applied_consumption_map  # type: dict[str, list[DataAppliedConsumptionMapValue]]

    def validate(self):
        if self.applied_consumption_map:
            for v in self.applied_consumption_map.values():
                for k1 in v:
                    if k1:
                        k1.validate()

    def to_map(self):
        _map = super(AppliedConsumStatResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppliedConsumptionMap'] = {}
        if self.applied_consumption_map is not None:
            for k, v in self.applied_consumption_map.items():
                l1 = []
                for k1 in v:
                    l1.append(k1.to_map() if k1 else None)
                result['appliedConsumptionMap'][k] = l1
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.applied_consumption_map = {}
        if m.get('AppliedConsumptionMap') is not None:
            for k, v in m.get('AppliedConsumptionMap').items():
                l1 = []
                for k1 in v:
                    temp_model = DataAppliedConsumptionMapValue()
                    l1.append(temp_model.from_map(k1))
                self.applied_consumption_map['k'] = l1
        return self


class AppliedConsumStatResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: AppliedConsumStatResponseBodyData
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
        _map = super(AppliedConsumStatResponseBody, self).to_map()
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
            temp_model = AppliedConsumStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppliedConsumStatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppliedConsumStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppliedConsumStatResponse, self).to_map()
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
            temp_model = AppliedConsumStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppliedNearRealStatRequest(TeaModel):
    def __init__(self, applied_version_id=None, operator_id=None, operator_type=None, order_by=None,
                 package_type=None, page_number=None, page_size=None):
        self.applied_version_id = applied_version_id  # type: list[str]
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 排序类型。默认：AppliedConcurrency_Desc,AppliedNearRealOrderConditionType[AppliedConcurrency_Desc(AppliedConcurrency_Desc,根据实时并发路数降序排列),AppliedConcurrency_Asc(AppliedConcurrency_Asc,根据实时并发路数升序排列),AppliedConsumptionCu_Desc(AppliedConsumptionCu_Desc,根据实时CU消耗降序排列),AppliedConsumptionCu_Asc(AppliedConsumptionCu_Asc,根据实时CU消耗升序排列),orderByType,desc]
        self.order_by = order_by  # type: str
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 当前页码，默认1
        self.page_number = page_number  # type: int
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedNearRealStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_version_id is not None:
            result['AppliedVersionId'] = self.applied_version_id
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedVersionId') is not None:
            self.applied_version_id = m.get('AppliedVersionId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class AppliedNearRealStatShrinkRequest(TeaModel):
    def __init__(self, applied_version_id_shrink=None, operator_id=None, operator_type=None, order_by=None,
                 package_type=None, page_number=None, page_size=None):
        self.applied_version_id_shrink = applied_version_id_shrink  # type: str
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 排序类型。默认：AppliedConcurrency_Desc,AppliedNearRealOrderConditionType[AppliedConcurrency_Desc(AppliedConcurrency_Desc,根据实时并发路数降序排列),AppliedConcurrency_Asc(AppliedConcurrency_Asc,根据实时并发路数升序排列),AppliedConsumptionCu_Desc(AppliedConsumptionCu_Desc,根据实时CU消耗降序排列),AppliedConsumptionCu_Asc(AppliedConsumptionCu_Asc,根据实时CU消耗升序排列),orderByType,desc]
        self.order_by = order_by  # type: str
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 当前页码，默认1
        self.page_number = page_number  # type: int
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedNearRealStatShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_version_id_shrink is not None:
            result['AppliedVersionId'] = self.applied_version_id_shrink
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedVersionId') is not None:
            self.applied_version_id_shrink = m.get('AppliedVersionId')
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class AppliedNearRealStatResponseBodyDataRecords(TeaModel):
    def __init__(self, applied_id=None, applied_name=None, applied_version_id=None, applied_version_name=None,
                 concurrency=None, consumption_cu=None):
        # 应用ID
        self.applied_id = applied_id  # type: str
        # 应用名称
        self.applied_name = applied_name  # type: str
        # 应用版本ID
        self.applied_version_id = applied_version_id  # type: str
        # 应用版本名称
        self.applied_version_name = applied_version_name  # type: str
        # 实时消耗并发
        self.concurrency = concurrency  # type: long
        # 实时消耗CU
        self.consumption_cu = consumption_cu  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedNearRealStatResponseBodyDataRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.applied_name is not None:
            result['AppliedName'] = self.applied_name
        if self.applied_version_id is not None:
            result['AppliedVersionId'] = self.applied_version_id
        if self.applied_version_name is not None:
            result['AppliedVersionName'] = self.applied_version_name
        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency
        if self.consumption_cu is not None:
            result['ConsumptionCu'] = self.consumption_cu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('AppliedName') is not None:
            self.applied_name = m.get('AppliedName')
        if m.get('AppliedVersionId') is not None:
            self.applied_version_id = m.get('AppliedVersionId')
        if m.get('AppliedVersionName') is not None:
            self.applied_version_name = m.get('AppliedVersionName')
        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')
        if m.get('ConsumptionCu') is not None:
            self.consumption_cu = m.get('ConsumptionCu')
        return self


class AppliedNearRealStatResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, pages=None, records=None, total_count=None):
        # 当前页码，默认1
        self.page_number = page_number  # type: long
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: long
        # 总页数
        self.pages = pages  # type: long
        # 结果集
        self.records = records  # type: list[AppliedNearRealStatResponseBodyDataRecords]
        # 总共项数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AppliedNearRealStatResponseBodyData, self).to_map()
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
                temp_model = AppliedNearRealStatResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class AppliedNearRealStatResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: AppliedNearRealStatResponseBodyData
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
        _map = super(AppliedNearRealStatResponseBody, self).to_map()
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
            temp_model = AppliedNearRealStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppliedNearRealStatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppliedNearRealStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppliedNearRealStatResponse, self).to_map()
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
            temp_model = AppliedNearRealStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AppliedStatRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, query_end_date=None, query_start_date=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 查询结束时间
        self.query_end_date = query_end_date  # type: str
        # 查询开始时间
        self.query_start_date = query_start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class AppliedStatResponseBodyData(TeaModel):
    def __init__(self, active_applications=None, average_daily_runtime=None, peak_concurrency=None,
                 secondary_average_time=None):
        # 活跃应用个数
        self.active_applications = active_applications  # type: long
        # 日均应用运行时长
        self.average_daily_runtime = average_daily_runtime  # type: long
        # 应用并发数量峰值
        self.peak_concurrency = peak_concurrency  # type: long
        # 次均应用时长
        self.secondary_average_time = secondary_average_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AppliedStatResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_applications is not None:
            result['ActiveApplications'] = self.active_applications
        if self.average_daily_runtime is not None:
            result['AverageDailyRuntime'] = self.average_daily_runtime
        if self.peak_concurrency is not None:
            result['PeakConcurrency'] = self.peak_concurrency
        if self.secondary_average_time is not None:
            result['SecondaryAverageTime'] = self.secondary_average_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveApplications') is not None:
            self.active_applications = m.get('ActiveApplications')
        if m.get('AverageDailyRuntime') is not None:
            self.average_daily_runtime = m.get('AverageDailyRuntime')
        if m.get('PeakConcurrency') is not None:
            self.peak_concurrency = m.get('PeakConcurrency')
        if m.get('SecondaryAverageTime') is not None:
            self.secondary_average_time = m.get('SecondaryAverageTime')
        return self


class AppliedStatResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: AppliedStatResponseBodyData
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
        _map = super(AppliedStatResponseBody, self).to_map()
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
            temp_model = AppliedStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AppliedStatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AppliedStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AppliedStatResponse, self).to_map()
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
            temp_model = AppliedStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


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
                 start_parameters=None, system_info=None):
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
        # 启动参数
        self.start_parameters = start_parameters  # type: list[CreateAppSessionRequestStartParameters]
        # 系统信息：如端侧机型等信息
        self.system_info = system_info  # type: list[CreateAppSessionRequestSystemInfo]

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
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppSessionBatchRequestAppInfosStartParameters(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchRequestAppInfosStartParameters, self).to_map()
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


class CreateAppSessionBatchRequestAppInfosSystemInfo(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchRequestAppInfosSystemInfo, self).to_map()
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


class CreateAppSessionBatchRequestAppInfos(TeaModel):
    def __init__(self, app_id=None, app_version=None, client_ip=None, custom_user_id=None, customer_session_id=None,
                 start_parameters=None, system_info=None):
        self.app_id = app_id  # type: str
        self.app_version = app_version  # type: str
        self.client_ip = client_ip  # type: str
        self.custom_user_id = custom_user_id  # type: str
        self.customer_session_id = customer_session_id  # type: str
        self.start_parameters = start_parameters  # type: list[CreateAppSessionBatchRequestAppInfosStartParameters]
        self.system_info = system_info  # type: list[CreateAppSessionBatchRequestAppInfosSystemInfo]

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
        _map = super(CreateAppSessionBatchRequestAppInfos, self).to_map()
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
        result['StartParameters'] = []
        if self.start_parameters is not None:
            for k in self.start_parameters:
                result['StartParameters'].append(k.to_map() if k else None)
        result['SystemInfo'] = []
        if self.system_info is not None:
            for k in self.system_info:
                result['SystemInfo'].append(k.to_map() if k else None)
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
        self.start_parameters = []
        if m.get('StartParameters') is not None:
            for k in m.get('StartParameters'):
                temp_model = CreateAppSessionBatchRequestAppInfosStartParameters()
                self.start_parameters.append(temp_model.from_map(k))
        self.system_info = []
        if m.get('SystemInfo') is not None:
            for k in m.get('SystemInfo'):
                temp_model = CreateAppSessionBatchRequestAppInfosSystemInfo()
                self.system_info.append(temp_model.from_map(k))
        return self


class CreateAppSessionBatchRequest(TeaModel):
    def __init__(self, app_infos=None, custom_task_id=None, timeout=None):
        self.app_infos = app_infos  # type: list[CreateAppSessionBatchRequestAppInfos]
        self.custom_task_id = custom_task_id  # type: str
        self.timeout = timeout  # type: int

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = CreateAppSessionBatchRequestAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionBatchShrinkRequest(TeaModel):
    def __init__(self, app_infos_shrink=None, custom_task_id=None, timeout=None):
        self.app_infos_shrink = app_infos_shrink  # type: str
        self.custom_task_id = custom_task_id  # type: str
        self.timeout = timeout  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_infos_shrink is not None:
            result['AppInfos'] = self.app_infos_shrink
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInfos') is not None:
            self.app_infos_shrink = m.get('AppInfos')
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class CreateAppSessionBatchResponseBody(TeaModel):
    def __init__(self, custom_task_id=None, platform_task_id=None, request_id=None):
        # 自定义会话id
        self.custom_task_id = custom_task_id  # type: str
        # 平台会话id
        self.platform_task_id = platform_task_id  # type: str
        # 请求id
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAppSessionBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_task_id is not None:
            result['CustomTaskId'] = self.custom_task_id
        if self.platform_task_id is not None:
            result['PlatformTaskId'] = self.platform_task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomTaskId') is not None:
            self.custom_task_id = m.get('CustomTaskId')
        if m.get('PlatformTaskId') is not None:
            self.platform_task_id = m.get('PlatformTaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAppSessionBatchResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateAppSessionBatchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAppSessionBatchResponse, self).to_map()
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
            temp_model = CreateAppSessionBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUploadTaskRequest(TeaModel):
    def __init__(self, app_id=None, app_type=None, bucket_name=None, env=None, file_address=None, file_size=None,
                 file_type=None, progress=None, region=None, status=None, upload_tool_version=None, upload_type=None,
                 version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 应用类型
        self.app_type = app_type  # type: str
        # 上传的bucket名称
        self.bucket_name = bucket_name  # type: str
        # 环境
        self.env = env  # type: str
        # 游戏链接
        self.file_address = file_address  # type: str
        # 文件大小
        self.file_size = file_size  # type: long
        # 上传文件类型
        self.file_type = file_type  # type: str
        # 上传进度
        self.progress = progress  # type: float
        # 上传的bucket所在region
        self.region = region  # type: str
        # 上传状态
        self.status = status  # type: str
        # 上传工具版本
        self.upload_tool_version = upload_tool_version  # type: str
        # 上传任务类型
        self.upload_type = upload_type  # type: str
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadTaskRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.env is not None:
            result['Env'] = self.env
        if self.file_address is not None:
            result['FileAddress'] = self.file_address
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.region is not None:
            result['Region'] = self.region
        if self.status is not None:
            result['Status'] = self.status
        if self.upload_tool_version is not None:
            result['UploadToolVersion'] = self.upload_tool_version
        if self.upload_type is not None:
            result['UploadType'] = self.upload_type
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('FileAddress') is not None:
            self.file_address = m.get('FileAddress')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UploadToolVersion') is not None:
            self.upload_tool_version = m.get('UploadToolVersion')
        if m.get('UploadType') is not None:
            self.upload_type = m.get('UploadType')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class CreateUploadTaskResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUploadTaskResponseBody, self).to_map()
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


class CreateUploadTaskResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUploadTaskResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUploadTaskResponse, self).to_map()
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
            temp_model = CreateUploadTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppListResponseBodyData(TeaModel):
    def __init__(self, app_id=None, app_name=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 应用名称
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppListResponseBodyData, self).to_map()
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


class GetAppListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: list[GetAppListResponseBodyData]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetAppListResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetAppListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAppListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAppListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAppListResponse, self).to_map()
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
            temp_model = GetAppListResponseBody()
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


class GetAppSessionResponseBodyScheduleInfo(TeaModel):
    def __init__(self, key=None, value=None):
        # key数值，枚举有多个数值，例如： RegionId 大区id ServerIp 服务端 IP ServerPort 端口
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAppSessionResponseBodyScheduleInfo, self).to_map()
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


class GetAppSessionResponseBody(TeaModel):
    def __init__(self, app_id=None, app_version=None, custom_session_id=None, platform_session_id=None,
                 request_id=None, schedule_info=None, status=None):
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
        self.schedule_info = schedule_info  # type: list[GetAppSessionResponseBodyScheduleInfo]
        # 状态
        self.status = status  # type: str

    def validate(self):
        if self.schedule_info:
            for k in self.schedule_info:
                if k:
                    k.validate()

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
        result['ScheduleInfo'] = []
        if self.schedule_info is not None:
            for k in self.schedule_info:
                result['ScheduleInfo'].append(k.to_map() if k else None)
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
        self.schedule_info = []
        if m.get('ScheduleInfo') is not None:
            for k in m.get('ScheduleInfo'):
                temp_model = GetAppSessionResponseBodyScheduleInfo()
                self.schedule_info.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetAppSessionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAppSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNeedUploadFileListRequest(TeaModel):
    def __init__(self, app_id=None, env=None, hash_list=None, version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 环境
        self.env = env  # type: str
        self.hash_list = hash_list  # type: list[str]
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNeedUploadFileListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env is not None:
            result['Env'] = self.env
        if self.hash_list is not None:
            result['HashList'] = self.hash_list
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('HashList') is not None:
            self.hash_list = m.get('HashList')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetNeedUploadFileListResponseBodyData(TeaModel):
    def __init__(self, err=None, need_upload_file_list=None, success=None):
        # 错误信息
        self.err = err  # type: str
        # 待上传文件列表
        self.need_upload_file_list = need_upload_file_list  # type: list[str]
        # 请求结果
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNeedUploadFileListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err is not None:
            result['Err'] = self.err
        if self.need_upload_file_list is not None:
            result['NeedUploadFileList'] = self.need_upload_file_list
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Err') is not None:
            self.err = m.get('Err')
        if m.get('NeedUploadFileList') is not None:
            self.need_upload_file_list = m.get('NeedUploadFileList')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetNeedUploadFileListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetNeedUploadFileListResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetNeedUploadFileListResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetNeedUploadFileListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNeedUploadFileListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetNeedUploadFileListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNeedUploadFileListResponse, self).to_map()
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
            temp_model = GetNeedUploadFileListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssInfoResponseBodyData(TeaModel):
    def __init__(self, first=None, second=None):
        self.first = first  # type: str
        self.second = second  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetOssInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first is not None:
            result['First'] = self.first
        if self.second is not None:
            result['Second'] = self.second
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('First') is not None:
            self.first = m.get('First')
        if m.get('Second') is not None:
            self.second = m.get('Second')
        return self


class GetOssInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetOssInfoResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetOssInfoResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetOssInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetOssInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetOssInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetOssInfoResponse, self).to_map()
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
            temp_model = GetOssInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTenantIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: long
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTenantIdResponseBody, self).to_map()
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


class GetTenantIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetTenantIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetTenantIdResponse, self).to_map()
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
            temp_model = GetTenantIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTokenRequest(TeaModel):
    def __init__(self, app_id=None, bucket=None, env=None, region=None, version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 存储桶
        self.bucket = bucket  # type: str
        # 环境
        self.env = env  # type: str
        # 区域ID
        self.region = region  # type: str
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bucket is not None:
            result['Bucket'] = self.bucket
        if self.env is not None:
            result['Env'] = self.env
        if self.region is not None:
            result['Region'] = self.region
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class GetTokenResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, access_key_secret=None, endpoint=None, expiration=None,
                 internal_endpoint=None, security_token=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.endpoint = endpoint  # type: str
        self.expiration = expiration  # type: str
        self.internal_endpoint = internal_endpoint  # type: str
        self.security_token = security_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetTokenResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.access_key_secret is not None:
            result['AccessKeySecret'] = self.access_key_secret
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.expiration is not None:
            result['Expiration'] = self.expiration
        if self.internal_endpoint is not None:
            result['InternalEndpoint'] = self.internal_endpoint
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('AccessKeySecret') is not None:
            self.access_key_secret = m.get('AccessKeySecret')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')
        if m.get('InternalEndpoint') is not None:
            self.internal_endpoint = m.get('InternalEndpoint')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        return self


class GetTokenResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: GetTokenResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetTokenResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = GetTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class GetUploadToolUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: dict[str, str]
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUploadToolUrlResponseBody, self).to_map()
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


class GetUploadToolUrlResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUploadToolUrlResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUploadToolUrlResponse, self).to_map()
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
            temp_model = GetUploadToolUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HasActivateResponseBodyData(TeaModel):
    def __init__(self, success=None):
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(HasActivateResponseBodyData, self).to_map()
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


class HasActivateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: HasActivateResponseBodyData
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
        _map = super(HasActivateResponseBody, self).to_map()
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
            temp_model = HasActivateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasActivateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: HasActivateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HasActivateResponse, self).to_map()
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
            temp_model = HasActivateResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListAppSessionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAppSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PageQueryResourcePackageListRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, package_type=None, page_number=None, page_size=None,
                 query_valid_type=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 资源包类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 当前页码，默认1
        self.page_number = page_number  # type: int
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: int
        # 查询过期的资源包类型,ResourcePackageValidQueryConditionType[All(查询所有资源包),CurrentlyValid(查询当前有效的资源包(已开始，未结束)),PendingValid(未开始,即将生效的资源包),AllValid(已开始未结束 + 即将开始 的资源包),PendingInvalid5m(5min内即将到期的资源包),HasInvalid(已经过期的资源包),queryType,desc]
        self.query_valid_type = query_valid_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageQueryResourcePackageListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query_valid_type is not None:
            result['QueryValidType'] = self.query_valid_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('QueryValidType') is not None:
            self.query_valid_type = m.get('QueryValidType')
        return self


class PageQueryResourcePackageListResponseBodyDataRecords(TeaModel):
    def __init__(self, current_amount=None, gmt_valid_begin=None, gmt_valid_end=None, init_amount=None,
                 package_instance_id=None, package_type=None):
        # 当前资源包剩余总量
        self.current_amount = current_amount  # type: long
        # 资源包有效开始时间
        self.gmt_valid_begin = gmt_valid_begin  # type: str
        # 资源包有效结束时间
        self.gmt_valid_end = gmt_valid_end  # type: str
        # 当前资源包购买总量
        self.init_amount = init_amount  # type: long
        # 资源包实例ID
        self.package_instance_id = package_instance_id  # type: str
        # 资源包类型
        self.package_type = package_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PageQueryResourcePackageListResponseBodyDataRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_amount is not None:
            result['CurrentAmount'] = self.current_amount
        if self.gmt_valid_begin is not None:
            result['GmtValidBegin'] = self.gmt_valid_begin
        if self.gmt_valid_end is not None:
            result['GmtValidEnd'] = self.gmt_valid_end
        if self.init_amount is not None:
            result['InitAmount'] = self.init_amount
        if self.package_instance_id is not None:
            result['PackageInstanceId'] = self.package_instance_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentAmount') is not None:
            self.current_amount = m.get('CurrentAmount')
        if m.get('GmtValidBegin') is not None:
            self.gmt_valid_begin = m.get('GmtValidBegin')
        if m.get('GmtValidEnd') is not None:
            self.gmt_valid_end = m.get('GmtValidEnd')
        if m.get('InitAmount') is not None:
            self.init_amount = m.get('InitAmount')
        if m.get('PackageInstanceId') is not None:
            self.package_instance_id = m.get('PackageInstanceId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class PageQueryResourcePackageListResponseBodyData(TeaModel):
    def __init__(self, page_number=None, page_size=None, pages=None, records=None, total_count=None):
        # 当前页码，默认1
        self.page_number = page_number  # type: long
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: long
        # 总页数
        self.pages = pages  # type: long
        # 结果集
        self.records = records  # type: list[PageQueryResourcePackageListResponseBodyDataRecords]
        # 总共项数
        self.total_count = total_count  # type: long

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PageQueryResourcePackageListResponseBodyData, self).to_map()
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
                temp_model = PageQueryResourcePackageListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class PageQueryResourcePackageListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: PageQueryResourcePackageListResponseBodyData
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
        _map = super(PageQueryResourcePackageListResponseBody, self).to_map()
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
            temp_model = PageQueryResourcePackageListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PageQueryResourcePackageListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: PageQueryResourcePackageListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PageQueryResourcePackageListResponse, self).to_map()
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
            temp_model = PageQueryResourcePackageListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAdaptRecordsRequest(TeaModel):
    def __init__(self, app_version_id=None, request_app=None):
        self.app_version_id = app_version_id  # type: str
        self.request_app = request_app  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.request_app is not None:
            result['RequestApp'] = self.request_app
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('RequestApp') is not None:
            self.request_app = m.get('RequestApp')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget(TeaModel):
    def __init__(self, bit_rate=None, frame_rate=None, resolution=None, start_program=None):
        self.bit_rate = bit_rate  # type: int
        self.frame_rate = frame_rate  # type: int
        self.resolution = resolution  # type: str
        self.start_program = start_program  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget, self).to_map()
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


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu(TeaModel):
    def __init__(self, average=None, maximum=None, minimum=None, number_of_cores=None, quantile_80=None):
        self.average = average  # type: float
        self.maximum = maximum  # type: float
        self.minimum = minimum  # type: float
        self.number_of_cores = number_of_cores  # type: float
        self.quantile_80 = quantile_80  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.number_of_cores is not None:
            result['NumberOfCores'] = self.number_of_cores
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('NumberOfCores') is not None:
            self.number_of_cores = m.get('NumberOfCores')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization(TeaModel):
    def __init__(self, average=None, maximum=None, minimum=None, number_of_cores=None, quantile_80=None):
        self.average = average  # type: float
        self.maximum = maximum  # type: float
        self.minimum = minimum  # type: float
        self.number_of_cores = number_of_cores  # type: float
        self.quantile_80 = quantile_80  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.number_of_cores is not None:
            result['NumberOfCores'] = self.number_of_cores
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('NumberOfCores') is not None:
            self.number_of_cores = m.get('NumberOfCores')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization(TeaModel):
    def __init__(self, average=None, maximum=None, minimum=None, quantile_80=None, total=None):
        self.average = average  # type: float
        self.maximum = maximum  # type: float
        self.minimum = minimum  # type: float
        self.quantile_80 = quantile_80  # type: float
        self.total = total  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu(TeaModel):
    def __init__(self, gpu_usedutilization=None, mem_usedutilization=None):
        self.gpu_usedutilization = gpu_usedutilization  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization
        self.mem_usedutilization = mem_usedutilization  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization

    def validate(self):
        if self.gpu_usedutilization:
            self.gpu_usedutilization.validate()
        if self.mem_usedutilization:
            self.mem_usedutilization.validate()

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpu_usedutilization is not None:
            result['GpuUsedutilization'] = self.gpu_usedutilization.to_map()
        if self.mem_usedutilization is not None:
            result['MemUsedutilization'] = self.mem_usedutilization.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GpuUsedutilization') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuGpuUsedutilization()
            self.gpu_usedutilization = temp_model.from_map(m['GpuUsedutilization'])
        if m.get('MemUsedutilization') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpuMemUsedutilization()
            self.mem_usedutilization = temp_model.from_map(m['MemUsedutilization'])
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem(TeaModel):
    def __init__(self, average=None, maximum=None, minimum=None, quantile_80=None, total=None):
        self.average = average  # type: float
        self.maximum = maximum  # type: float
        self.minimum = minimum  # type: float
        self.quantile_80 = quantile_80  # type: float
        self.total = total  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.average is not None:
            result['Average'] = self.average
        if self.maximum is not None:
            result['Maximum'] = self.maximum
        if self.minimum is not None:
            result['Minimum'] = self.minimum
        if self.quantile_80 is not None:
            result['Quantile80'] = self.quantile_80
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Average') is not None:
            self.average = m.get('Average')
        if m.get('Maximum') is not None:
            self.maximum = m.get('Maximum')
        if m.get('Minimum') is not None:
            self.minimum = m.get('Minimum')
        if m.get('Quantile80') is not None:
            self.quantile_80 = m.get('Quantile80')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo(TeaModel):
    def __init__(self, cpu=None, gpu=None, mem=None):
        self.cpu = cpu  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu
        self.gpu = gpu  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu
        self.mem = mem  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem

    def validate(self):
        if self.cpu:
            self.cpu.validate()
        if self.gpu:
            self.gpu.validate()
        if self.mem:
            self.mem.validate()

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['Cpu'] = self.cpu.to_map()
        if self.gpu is not None:
            result['Gpu'] = self.gpu.to_map()
        if self.mem is not None:
            result['Mem'] = self.mem.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cpu') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoCpu()
            self.cpu = temp_model.from_map(m['Cpu'])
        if m.get('Gpu') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoGpu()
            self.gpu = temp_model.from_map(m['Gpu'])
        if m.get('Mem') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfoMem()
            self.mem = temp_model.from_map(m['Mem'])
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo(TeaModel):
    def __init__(self, cpu_type=None, gpu_type=None, name=None):
        self.cpu_type = cpu_type  # type: str
        self.gpu_type = gpu_type  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_type is not None:
            result['CpuType'] = self.cpu_type
        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CpuType') is not None:
            self.cpu_type = m.get('CpuType')
        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class QueryAdaptRecordsResponseBodyDataAdaptRecords(TeaModel):
    def __init__(self, adapt_apply_id=None, adapt_record_id=None, adapt_status=None, adapt_target=None, app_id=None,
                 app_version_id=None, calculation_evaluation_info=None, consume_cu=None, container_type=None,
                 file_download_path=None, gmt_create=None, gmt_modified=None, image_type=None, is_must_select=None, isv=None,
                 max_concurrency=None, memo=None, priority=None, server_info=None, tenant_id=None, vm_type=None):
        self.adapt_apply_id = adapt_apply_id  # type: long
        self.adapt_record_id = adapt_record_id  # type: long
        self.adapt_status = adapt_status  # type: str
        self.adapt_target = adapt_target  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget
        self.app_id = app_id  # type: str
        self.app_version_id = app_version_id  # type: str
        self.calculation_evaluation_info = calculation_evaluation_info  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo
        self.consume_cu = consume_cu  # type: float
        # 蔚领：1 独占虚机，2 支持多开 (EXCLUSIVE: 独占虚机, SHARED: 支持多开)
        self.container_type = container_type  # type: str
        self.file_download_path = file_download_path  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.image_type = image_type  # type: str
        self.is_must_select = is_must_select  # type: bool
        self.isv = isv  # type: str
        self.max_concurrency = max_concurrency  # type: int
        self.memo = memo  # type: str
        self.priority = priority  # type: int
        self.server_info = server_info  # type: QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo
        self.tenant_id = tenant_id  # type: long
        self.vm_type = vm_type  # type: str

    def validate(self):
        if self.adapt_target:
            self.adapt_target.validate()
        if self.calculation_evaluation_info:
            self.calculation_evaluation_info.validate()
        if self.server_info:
            self.server_info.validate()

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyDataAdaptRecords, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        if self.adapt_record_id is not None:
            result['AdaptRecordId'] = self.adapt_record_id
        if self.adapt_status is not None:
            result['AdaptStatus'] = self.adapt_status
        if self.adapt_target is not None:
            result['AdaptTarget'] = self.adapt_target.to_map()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.calculation_evaluation_info is not None:
            result['CalculationEvaluationInfo'] = self.calculation_evaluation_info.to_map()
        if self.consume_cu is not None:
            result['ConsumeCu'] = self.consume_cu
        if self.container_type is not None:
            result['ContainerType'] = self.container_type
        if self.file_download_path is not None:
            result['FileDownloadPath'] = self.file_download_path
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.image_type is not None:
            result['ImageType'] = self.image_type
        if self.is_must_select is not None:
            result['IsMustSelect'] = self.is_must_select
        if self.isv is not None:
            result['Isv'] = self.isv
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.server_info is not None:
            result['ServerInfo'] = self.server_info.to_map()
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.vm_type is not None:
            result['VmType'] = self.vm_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        if m.get('AdaptRecordId') is not None:
            self.adapt_record_id = m.get('AdaptRecordId')
        if m.get('AdaptStatus') is not None:
            self.adapt_status = m.get('AdaptStatus')
        if m.get('AdaptTarget') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsAdaptTarget()
            self.adapt_target = temp_model.from_map(m['AdaptTarget'])
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('CalculationEvaluationInfo') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsCalculationEvaluationInfo()
            self.calculation_evaluation_info = temp_model.from_map(m['CalculationEvaluationInfo'])
        if m.get('ConsumeCu') is not None:
            self.consume_cu = m.get('ConsumeCu')
        if m.get('ContainerType') is not None:
            self.container_type = m.get('ContainerType')
        if m.get('FileDownloadPath') is not None:
            self.file_download_path = m.get('FileDownloadPath')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')
        if m.get('IsMustSelect') is not None:
            self.is_must_select = m.get('IsMustSelect')
        if m.get('Isv') is not None:
            self.isv = m.get('Isv')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('ServerInfo') is not None:
            temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecordsServerInfo()
            self.server_info = temp_model.from_map(m['ServerInfo'])
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VmType') is not None:
            self.vm_type = m.get('VmType')
        return self


class QueryAdaptRecordsResponseBodyData(TeaModel):
    def __init__(self, adapt_apply_id=None, adapt_records=None, app_id=None, app_name=None, app_type=None,
                 app_version_id=None, app_version_name=None, app_version_serviceype=None, tenant_id=None, tenant_name=None):
        self.adapt_apply_id = adapt_apply_id  # type: long
        self.adapt_records = adapt_records  # type: list[QueryAdaptRecordsResponseBodyDataAdaptRecords]
        self.app_id = app_id  # type: str
        self.app_name = app_name  # type: str
        self.app_type = app_type  # type: str
        self.app_version_id = app_version_id  # type: str
        self.app_version_name = app_version_name  # type: str
        self.app_version_serviceype = app_version_serviceype  # type: str
        self.tenant_id = tenant_id  # type: long
        self.tenant_name = tenant_name  # type: str

    def validate(self):
        if self.adapt_records:
            for k in self.adapt_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.adapt_apply_id is not None:
            result['AdaptApplyId'] = self.adapt_apply_id
        result['AdaptRecords'] = []
        if self.adapt_records is not None:
            for k in self.adapt_records:
                result['AdaptRecords'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_type is not None:
            result['AppType'] = self.app_type
        if self.app_version_id is not None:
            result['AppVersionId'] = self.app_version_id
        if self.app_version_name is not None:
            result['AppVersionName'] = self.app_version_name
        if self.app_version_serviceype is not None:
            result['AppVersionServiceype'] = self.app_version_serviceype
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdaptApplyId') is not None:
            self.adapt_apply_id = m.get('AdaptApplyId')
        self.adapt_records = []
        if m.get('AdaptRecords') is not None:
            for k in m.get('AdaptRecords'):
                temp_model = QueryAdaptRecordsResponseBodyDataAdaptRecords()
                self.adapt_records.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')
        if m.get('AppVersionId') is not None:
            self.app_version_id = m.get('AppVersionId')
        if m.get('AppVersionName') is not None:
            self.app_version_name = m.get('AppVersionName')
        if m.get('AppVersionServiceype') is not None:
            self.app_version_serviceype = m.get('AppVersionServiceype')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')
        return self


class QueryAdaptRecordsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: QueryAdaptRecordsResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryAdaptRecordsResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryAdaptRecordsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryAdaptRecordsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryAdaptRecordsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryAdaptRecordsResponse, self).to_map()
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
            temp_model = QueryAdaptRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUploadProgressRequest(TeaModel):
    def __init__(self, query_upload_progress_requests=None):
        self.query_upload_progress_requests = query_upload_progress_requests  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUploadProgressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_upload_progress_requests is not None:
            result['QueryUploadProgressRequests'] = self.query_upload_progress_requests
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('QueryUploadProgressRequests') is not None:
            self.query_upload_progress_requests = m.get('QueryUploadProgressRequests')
        return self


class QueryUploadProgressResponseBodyDataContentVersions(TeaModel):
    def __init__(self, app_id=None, progress=None, tenant_id=None, version_id=None):
        self.app_id = app_id  # type: str
        self.progress = progress  # type: float
        self.tenant_id = tenant_id  # type: long
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUploadProgressResponseBodyDataContentVersions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class QueryUploadProgressResponseBodyDataContent(TeaModel):
    def __init__(self, versions=None):
        self.versions = versions  # type: list[QueryUploadProgressResponseBodyDataContentVersions]

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryUploadProgressResponseBodyDataContent, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['Versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.versions = []
        if m.get('Versions') is not None:
            for k in m.get('Versions'):
                temp_model = QueryUploadProgressResponseBodyDataContentVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class QueryUploadProgressResponseBodyData(TeaModel):
    def __init__(self, code=None, content=None, message=None):
        # 查询结果
        self.code = code  # type: str
        # 进度信息
        self.content = content  # type: QueryUploadProgressResponseBodyDataContent
        # 查询信息
        self.message = message  # type: str

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        _map = super(QueryUploadProgressResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.content is not None:
            result['Content'] = self.content.to_map()
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Content') is not None:
            temp_model = QueryUploadProgressResponseBodyDataContent()
            self.content = temp_model.from_map(m['Content'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class QueryUploadProgressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: QueryUploadProgressResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryUploadProgressResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = QueryUploadProgressResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryUploadProgressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryUploadProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUploadProgressResponse, self).to_map()
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
            temp_model = QueryUploadProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordFinishedFileRequestFileFingerprintDTOList(TeaModel):
    def __init__(self, file_hash=None, file_size=None):
        # 文件hash
        self.file_hash = file_hash  # type: str
        # 文件大小
        self.file_size = file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordFinishedFileRequestFileFingerprintDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class RecordFinishedFileRequest(TeaModel):
    def __init__(self, app_id=None, bucket_name=None, env=None, file_fingerprint_dtolist=None, file_size=None,
                 file_type=None, region=None, tool_version=None, version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 上传的bucket名称
        self.bucket_name = bucket_name  # type: str
        # 环境
        self.env = env  # type: str
        # 用于pop传入的文件指纹信息
        self.file_fingerprint_dtolist = file_fingerprint_dtolist  # type: list[RecordFinishedFileRequestFileFingerprintDTOList]
        # 文件大小
        self.file_size = file_size  # type: long
        # 上传文件类型
        self.file_type = file_type  # type: str
        # 上传的bucket所在region
        self.region = region  # type: str
        # 上传工具版本
        self.tool_version = tool_version  # type: str
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        if self.file_fingerprint_dtolist:
            for k in self.file_fingerprint_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RecordFinishedFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.env is not None:
            result['Env'] = self.env
        result['FileFingerprintDTOList'] = []
        if self.file_fingerprint_dtolist is not None:
            for k in self.file_fingerprint_dtolist:
                result['FileFingerprintDTOList'].append(k.to_map() if k else None)
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.region is not None:
            result['Region'] = self.region
        if self.tool_version is not None:
            result['ToolVersion'] = self.tool_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        self.file_fingerprint_dtolist = []
        if m.get('FileFingerprintDTOList') is not None:
            for k in m.get('FileFingerprintDTOList'):
                temp_model = RecordFinishedFileRequestFileFingerprintDTOList()
                self.file_fingerprint_dtolist.append(temp_model.from_map(k))
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ToolVersion') is not None:
            self.tool_version = m.get('ToolVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class RecordFinishedFileResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RecordFinishedFileResponseBody, self).to_map()
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


class RecordFinishedFileResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RecordFinishedFileResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RecordFinishedFileResponse, self).to_map()
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
            temp_model = RecordFinishedFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReplicateVersionRequest(TeaModel):
    def __init__(self, app_id=None, source_version_id=None, target_version_id=None, tenant_id=None):
        # 应用Id
        self.app_id = app_id  # type: str
        # 源头版本Id
        self.source_version_id = source_version_id  # type: str
        # 复制目标版本Id
        self.target_version_id = target_version_id  # type: str
        # 租户Id
        self.tenant_id = tenant_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplicateVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.source_version_id is not None:
            result['SourceVersionId'] = self.source_version_id
        if self.target_version_id is not None:
            result['TargetVersionId'] = self.target_version_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SourceVersionId') is not None:
            self.source_version_id = m.get('SourceVersionId')
        if m.get('TargetVersionId') is not None:
            self.target_version_id = m.get('TargetVersionId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class ReplicateVersionResponseBodyData(TeaModel):
    def __init__(self, code=None, message=None):
        # 复制结果
        self.code = code  # type: str
        # 复制结果信息
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReplicateVersionResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ReplicateVersionResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: ReplicateVersionResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ReplicateVersionResponseBody, self).to_map()
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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            temp_model = ReplicateVersionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ReplicateVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReplicateVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReplicateVersionResponse, self).to_map()
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
            temp_model = ReplicateVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUploadProgressRequest(TeaModel):
    def __init__(self, app_id=None, env=None, progress=None, version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 环境
        self.env = env  # type: str
        # 上传进度
        self.progress = progress  # type: float
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUploadProgressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env is not None:
            result['Env'] = self.env
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ReportUploadProgressResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUploadProgressResponseBody, self).to_map()
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


class ReportUploadProgressResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReportUploadProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportUploadProgressResponse, self).to_map()
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
            temp_model = ReportUploadProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUploadResultRequestFileFingerprintDTOList(TeaModel):
    def __init__(self, file_hash=None, file_size=None):
        # 文件hash
        self.file_hash = file_hash  # type: str
        # 文件大小
        self.file_size = file_size  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUploadResultRequestFileFingerprintDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_hash is not None:
            result['FileHash'] = self.file_hash
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileHash') is not None:
            self.file_hash = m.get('FileHash')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        return self


class ReportUploadResultRequest(TeaModel):
    def __init__(self, app_id=None, bucket_name=None, env=None, file_fingerprint_dtolist=None, file_size=None,
                 file_type=None, region=None, tool_version=None, version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 上传的bucket名称
        self.bucket_name = bucket_name  # type: str
        # 环境
        self.env = env  # type: str
        # 用于pop传入的文件指纹信息
        self.file_fingerprint_dtolist = file_fingerprint_dtolist  # type: list[ReportUploadResultRequestFileFingerprintDTOList]
        # 文件大小
        self.file_size = file_size  # type: long
        # 上传文件类型
        self.file_type = file_type  # type: str
        # 上传的bucket所在region
        self.region = region  # type: str
        # 上传工具版本
        self.tool_version = tool_version  # type: str
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        if self.file_fingerprint_dtolist:
            for k in self.file_fingerprint_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ReportUploadResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.env is not None:
            result['Env'] = self.env
        result['FileFingerprintDTOList'] = []
        if self.file_fingerprint_dtolist is not None:
            for k in self.file_fingerprint_dtolist:
                result['FileFingerprintDTOList'].append(k.to_map() if k else None)
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.region is not None:
            result['Region'] = self.region
        if self.tool_version is not None:
            result['ToolVersion'] = self.tool_version
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        self.file_fingerprint_dtolist = []
        if m.get('FileFingerprintDTOList') is not None:
            for k in m.get('FileFingerprintDTOList'):
                temp_model = ReportUploadResultRequestFileFingerprintDTOList()
                self.file_fingerprint_dtolist.append(temp_model.from_map(k))
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ToolVersion') is not None:
            self.tool_version = m.get('ToolVersion')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ReportUploadResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUploadResultResponseBody, self).to_map()
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


class ReportUploadResultResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReportUploadResultResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportUploadResultResponse, self).to_map()
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
            temp_model = ReportUploadResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReportUploadStatusRequest(TeaModel):
    def __init__(self, app_id=None, env=None, memo=None, status=None, version_id=None):
        # 应用ID
        self.app_id = app_id  # type: str
        # 环境
        self.env = env  # type: str
        # 备注信息
        self.memo = memo  # type: str
        # 上传状态
        self.status = status  # type: str
        # 版本ID
        self.version_id = version_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUploadStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.env is not None:
            result['Env'] = self.env
        if self.memo is not None:
            result['Memo'] = self.memo
        if self.status is not None:
            result['Status'] = self.status
        if self.version_id is not None:
            result['VersionId'] = self.version_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Env') is not None:
            self.env = m.get('Env')
        if m.get('Memo') is not None:
            self.memo = m.get('Memo')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')
        return self


class ReportUploadStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: bool
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReportUploadStatusResponseBody, self).to_map()
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


class ReportUploadStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ReportUploadStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReportUploadStatusResponse, self).to_map()
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
            temp_model = ReportUploadStatusResponseBody()
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StopAppSessionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StopAppSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TotalAppliedConsumStatRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, package_type=None, query_end_date=None,
                 query_start_date=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 查询结束时间
        self.query_end_date = query_end_date  # type: str
        # 查询开始时间
        self.query_start_date = query_start_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TotalAppliedConsumStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.query_end_date is not None:
            result['QueryEndDate'] = self.query_end_date
        if self.query_start_date is not None:
            result['QueryStartDate'] = self.query_start_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('QueryEndDate') is not None:
            self.query_end_date = m.get('QueryEndDate')
        if m.get('QueryStartDate') is not None:
            self.query_start_date = m.get('QueryStartDate')
        return self


class TotalAppliedConsumStatResponseBodyData(TeaModel):
    def __init__(self, applied_id=None, consumption_cu=None, stat_date=None):
        # 应用ID
        self.applied_id = applied_id  # type: str
        # 分钟级消耗CU
        self.consumption_cu = consumption_cu  # type: long
        # 统计日期
        self.stat_date = stat_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TotalAppliedConsumStatResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.consumption_cu is not None:
            result['ConsumptionCu'] = self.consumption_cu
        if self.stat_date is not None:
            result['StatDate'] = self.stat_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('ConsumptionCu') is not None:
            self.consumption_cu = m.get('ConsumptionCu')
        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')
        return self


class TotalAppliedConsumStatResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: list[TotalAppliedConsumStatResponseBodyData]
        # 业务处理消息摘要
        self.message = message  # type: str
        # 操作请求ID
        self.request_id = request_id  # type: str
        # 业务处理是否成功
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TotalAppliedConsumStatResponseBody, self).to_map()
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
                temp_model = TotalAppliedConsumStatResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TotalAppliedConsumStatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TotalAppliedConsumStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TotalAppliedConsumStatResponse, self).to_map()
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
            temp_model = TotalAppliedConsumStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TotalAppliedNearRealStatRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, order_by=None, package_type=None, page_number=None,
                 page_size=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 排序类型。默认：AppliedConcurrency_Desc,AppliedNearRealOrderConditionType[AppliedConcurrency_Desc(AppliedConcurrency_Desc,根据实时并发路数降序排列),AppliedConcurrency_Asc(AppliedConcurrency_Asc,根据实时并发路数升序排列),AppliedConsumptionCu_Desc(AppliedConsumptionCu_Desc,根据实时CU消耗降序排列),AppliedConsumptionCu_Asc(AppliedConsumptionCu_Asc,根据实时CU消耗升序排列),orderByType,desc]
        self.order_by = order_by  # type: str
        # 资源类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str
        # 当前页码，默认1
        self.page_number = page_number  # type: int
        # 每页项数，默认20,最大100
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(TotalAppliedNearRealStatRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class TotalAppliedNearRealStatResponseBodyData(TeaModel):
    def __init__(self, total_concurrency=None, total_consumption_cu=None):
        # 实时消耗并发
        self.total_concurrency = total_concurrency  # type: long
        # 实时消耗CU
        self.total_consumption_cu = total_consumption_cu  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(TotalAppliedNearRealStatResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_concurrency is not None:
            result['TotalConcurrency'] = self.total_concurrency
        if self.total_consumption_cu is not None:
            result['TotalConsumptionCu'] = self.total_consumption_cu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalConcurrency') is not None:
            self.total_concurrency = m.get('TotalConcurrency')
        if m.get('TotalConsumptionCu') is not None:
            self.total_consumption_cu = m.get('TotalConsumptionCu')
        return self


class TotalAppliedNearRealStatResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: TotalAppliedNearRealStatResponseBodyData
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
        _map = super(TotalAppliedNearRealStatResponseBody, self).to_map()
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
            temp_model = TotalAppliedNearRealStatResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TotalAppliedNearRealStatResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TotalAppliedNearRealStatResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TotalAppliedNearRealStatResponse, self).to_map()
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
            temp_model = TotalAppliedNearRealStatResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TotalQueryResourcePackageRequest(TeaModel):
    def __init__(self, operator_id=None, operator_type=None, package_type=None):
        # 请求操作人Id
        self.operator_id = operator_id  # type: str
        # 请求操作人类型
        self.operator_type = operator_type  # type: str
        # 资源包类型,PackageType[CU(cu),code,cssResourceType,desc]
        self.package_type = package_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TotalQueryResourcePackageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class TotalQueryResourcePackageResponseBodyData(TeaModel):
    def __init__(self, tenant_uid=None, total_amount=None, total_date=None):
        # 租户UserId
        self.tenant_uid = tenant_uid  # type: str
        # 当前所有有效资源包总量
        self.total_amount = total_amount  # type: long
        # 计算时间
        self.total_date = total_date  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TotalQueryResourcePackageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_uid is not None:
            result['TenantUid'] = self.tenant_uid
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        if self.total_date is not None:
            result['TotalDate'] = self.total_date
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TenantUid') is not None:
            self.tenant_uid = m.get('TenantUid')
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        if m.get('TotalDate') is not None:
            self.total_date = m.get('TotalDate')
        return self


class TotalQueryResourcePackageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None, success=None):
        # 业务处理结果Code
        self.code = code  # type: str
        # 业务对象
        self.data = data  # type: TotalQueryResourcePackageResponseBodyData
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
        _map = super(TotalQueryResourcePackageResponseBody, self).to_map()
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
            temp_model = TotalQueryResourcePackageResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TotalQueryResourcePackageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TotalQueryResourcePackageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TotalQueryResourcePackageResponse, self).to_map()
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
            temp_model = TotalQueryResourcePackageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DataAppliedConsumptionMapValue(TeaModel):
    def __init__(self, applied_id=None, stat_date=None, consumption_cu=None):
        # 应用ID
        self.applied_id = applied_id  # type: str
        # 统计日期
        self.stat_date = stat_date  # type: str
        # 分钟级消耗CU
        self.consumption_cu = consumption_cu  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DataAppliedConsumptionMapValue, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.applied_id is not None:
            result['AppliedId'] = self.applied_id
        if self.stat_date is not None:
            result['StatDate'] = self.stat_date
        if self.consumption_cu is not None:
            result['ConsumptionCu'] = self.consumption_cu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppliedId') is not None:
            self.applied_id = m.get('AppliedId')
        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')
        if m.get('ConsumptionCu') is not None:
            self.consumption_cu = m.get('ConsumptionCu')
        return self


