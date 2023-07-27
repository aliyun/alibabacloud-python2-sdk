# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddApListToApgroupRequest(TeaModel):
    def __init__(self, ap_group_id=None, ap_mac_list=None, app_code=None, app_name=None):
        self.ap_group_id = ap_group_id  # type: str
        self.ap_mac_list = ap_mac_list  # type: dict[str, any]
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddApListToApgroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_id is not None:
            result['ApGroupId'] = self.ap_group_id
        if self.ap_mac_list is not None:
            result['ApMacList'] = self.ap_mac_list
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApGroupId') is not None:
            self.ap_group_id = m.get('ApGroupId')
        if m.get('ApMacList') is not None:
            self.ap_mac_list = m.get('ApMacList')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class AddApListToApgroupShrinkRequest(TeaModel):
    def __init__(self, ap_group_id=None, ap_mac_list_shrink=None, app_code=None, app_name=None):
        self.ap_group_id = ap_group_id  # type: str
        self.ap_mac_list_shrink = ap_mac_list_shrink  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddApListToApgroupShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_id is not None:
            result['ApGroupId'] = self.ap_group_id
        if self.ap_mac_list_shrink is not None:
            result['ApMacList'] = self.ap_mac_list_shrink
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApGroupId') is not None:
            self.ap_group_id = m.get('ApGroupId')
        if m.get('ApMacList') is not None:
            self.ap_mac_list_shrink = m.get('ApMacList')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class AddApListToApgroupResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddApListToApgroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class AddApListToApgroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddApListToApgroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddApListToApgroupResponse, self).to_map()
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
            temp_model = AddApListToApgroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DelApThirdAppRequest(TeaModel):
    def __init__(self, ap_asset_id=None, app_code=None, app_name=None, id=None, mac=None):
        self.ap_asset_id = ap_asset_id  # type: long
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.id = id  # type: long
        self.mac = mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelApThirdAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class DelApThirdAppResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DelApThirdAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DelApThirdAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DelApThirdAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DelApThirdAppResponse, self).to_map()
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
            temp_model = DelApThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApSsidConfigRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, radio_index=None, ssid=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.radio_index = radio_index  # type: str
        self.ssid = ssid  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApSsidConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index
        if self.ssid is not None:
            result['Ssid'] = self.ssid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')
        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')
        return self


class DeleteApSsidConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApSsidConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class DeleteApSsidConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApSsidConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApSsidConfigResponse, self).to_map()
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
            temp_model = DeleteApSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApgroupConfigRequest(TeaModel):
    def __init__(self, ap_group_uuid=None, app_code=None, app_name=None):
        self.ap_group_uuid = ap_group_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApgroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class DeleteApgroupConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApgroupConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class DeleteApgroupConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApgroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApgroupConfigResponse, self).to_map()
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
            temp_model = DeleteApgroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApgroupSsidConfigRequest(TeaModel):
    def __init__(self, apgroup_id=None, app_code=None, app_name=None, id=None):
        self.apgroup_id = apgroup_id  # type: long
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApgroupSsidConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteApgroupSsidConfigResponseBodyData(TeaModel):
    def __init__(self, id=None, task_id=None):
        self.id = id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApgroupSsidConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteApgroupSsidConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: DeleteApgroupSsidConfigResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteApgroupSsidConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = DeleteApgroupSsidConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApgroupSsidConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApgroupSsidConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApgroupSsidConfigResponse, self).to_map()
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
            temp_model = DeleteApgroupSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteApgroupThirdAppRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.id = id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApgroupThirdAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteApgroupThirdAppResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteApgroupThirdAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteApgroupThirdAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteApgroupThirdAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteApgroupThirdAppResponse, self).to_map()
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
            temp_model = DeleteApgroupThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNetDeviceInfoRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, ids=None, request_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.ids = ids  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetDeviceInfoResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: list[long]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteNetDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNetDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteNetDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteNetDeviceInfoResponse, self).to_map()
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
            temp_model = DeleteNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EditApgroupThirdAppRequest(TeaModel):
    def __init__(self, apgroup_id=None, app_code=None, app_data=None, app_name=None, apply_to_sub_group=None,
                 category=None, config_type=None, id=None, inherit_parent_group=None, third_app_name=None):
        self.apgroup_id = apgroup_id  # type: long
        self.app_code = app_code  # type: str
        self.app_data = app_data  # type: str
        self.app_name = app_name  # type: str
        self.apply_to_sub_group = apply_to_sub_group  # type: int
        self.category = category  # type: int
        self.config_type = config_type  # type: str
        self.id = id  # type: long
        self.inherit_parent_group = inherit_parent_group  # type: int
        self.third_app_name = third_app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditApgroupThirdAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_data is not None:
            result['AppData'] = self.app_data
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.apply_to_sub_group is not None:
            result['ApplyToSubGroup'] = self.apply_to_sub_group
        if self.category is not None:
            result['Category'] = self.category
        if self.config_type is not None:
            result['ConfigType'] = self.config_type
        if self.id is not None:
            result['Id'] = self.id
        if self.inherit_parent_group is not None:
            result['InheritParentGroup'] = self.inherit_parent_group
        if self.third_app_name is not None:
            result['ThirdAppName'] = self.third_app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ApplyToSubGroup') is not None:
            self.apply_to_sub_group = m.get('ApplyToSubGroup')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ConfigType') is not None:
            self.config_type = m.get('ConfigType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InheritParentGroup') is not None:
            self.inherit_parent_group = m.get('InheritParentGroup')
        if m.get('ThirdAppName') is not None:
            self.third_app_name = m.get('ThirdAppName')
        return self


class EditApgroupThirdAppResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EditApgroupThirdAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EditApgroupThirdAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EditApgroupThirdAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EditApgroupThirdAppResponse, self).to_map()
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
            temp_model = EditApgroupThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EffectApConfigRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EffectApConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class EffectApConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EffectApConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class EffectApConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EffectApConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EffectApConfigResponse, self).to_map()
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
            temp_model = EffectApConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EffectApgroupConfigRequest(TeaModel):
    def __init__(self, ap_group_uuid=None, app_code=None, app_name=None):
        self.ap_group_uuid = ap_group_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EffectApgroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class EffectApgroupConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(EffectApgroupConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class EffectApgroupConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EffectApgroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EffectApgroupConfigResponse, self).to_map()
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
            temp_model = EffectApgroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApAddressByMacRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, language=None, mac=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.language = language  # type: str
        self.mac = mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApAddressByMacRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.language is not None:
            result['Language'] = self.language
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class GetApAddressByMacResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApAddressByMacResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApAddressByMacResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApAddressByMacResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApAddressByMacResponse, self).to_map()
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
            temp_model = GetApAddressByMacResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApAssetRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApAssetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApAssetResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApAssetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApAssetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApAssetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApAssetResponse, self).to_map()
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
            temp_model = GetApAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApDetailStatusRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, mac=None, need_apgroup_info=None, need_radio_status=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.mac = mac  # type: str
        self.need_apgroup_info = need_apgroup_info  # type: bool
        self.need_radio_status = need_radio_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApDetailStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.need_apgroup_info is not None:
            result['NeedApgroupInfo'] = self.need_apgroup_info
        if self.need_radio_status is not None:
            result['NeedRadioStatus'] = self.need_radio_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('NeedApgroupInfo') is not None:
            self.need_apgroup_info = m.get('NeedApgroupInfo')
        if m.get('NeedRadioStatus') is not None:
            self.need_radio_status = m.get('NeedRadioStatus')
        return self


class GetApDetailStatusResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApDetailStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApDetailStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApDetailStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApDetailStatusResponse, self).to_map()
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
            temp_model = GetApDetailStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApDetailedConfigRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApDetailedConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApDetailedConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApDetailedConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApDetailedConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApDetailedConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApDetailedConfigResponse, self).to_map()
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
            temp_model = GetApDetailedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApInfoFromPoolRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApInfoFromPoolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApInfoFromPoolResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApInfoFromPoolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApInfoFromPoolResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApInfoFromPoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApInfoFromPoolResponse, self).to_map()
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
            temp_model = GetApInfoFromPoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApRunHistoryTimeSerRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, end=None, start=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.end = end  # type: long
        self.start = start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApRunHistoryTimeSerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetApRunHistoryTimeSerResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApRunHistoryTimeSerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApRunHistoryTimeSerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApRunHistoryTimeSerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApRunHistoryTimeSerResponse, self).to_map()
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
            temp_model = GetApRunHistoryTimeSerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApStatusByGroupIdRequest(TeaModel):
    def __init__(self, apgroup_id=None, app_code=None, app_name=None, cursor=None, page_size=None):
        self.apgroup_id = apgroup_id  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.cursor = cursor  # type: long
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApStatusByGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetApStatusByGroupIdResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApStatusByGroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApStatusByGroupIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApStatusByGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApStatusByGroupIdResponse, self).to_map()
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
            temp_model = GetApStatusByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupConfigByIdentityRequest(TeaModel):
    def __init__(self, apgroup_id=None, apgroup_uuid=None, app_code=None, app_name=None):
        self.apgroup_id = apgroup_id  # type: long
        self.apgroup_uuid = apgroup_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupConfigByIdentityRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupConfigByIdentityResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupConfigByIdentityResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApgroupConfigByIdentityResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApgroupConfigByIdentityResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApgroupConfigByIdentityResponse, self).to_map()
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
            temp_model = GetApgroupConfigByIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupDetailedConfigRequest(TeaModel):
    def __init__(self, apgroup_id=None, apgroup_uuid=None, app_code=None, app_name=None):
        self.apgroup_id = apgroup_id  # type: long
        self.apgroup_uuid = apgroup_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupDetailedConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupDetailedConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupDetailedConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetApgroupDetailedConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApgroupDetailedConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApgroupDetailedConfigResponse, self).to_map()
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
            temp_model = GetApgroupDetailedConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupIdRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupIdResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApgroupIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApgroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApgroupIdResponse, self).to_map()
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
            temp_model = GetApgroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetApgroupSsidConfigRequest(TeaModel):
    def __init__(self, ap_group_uuid=None, app_code=None, app_name=None):
        self.ap_group_uuid = ap_group_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupSsidConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class GetApgroupSsidConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: list[dict[str, any]]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetApgroupSsidConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetApgroupSsidConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetApgroupSsidConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetApgroupSsidConfigResponse, self).to_map()
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
            temp_model = GetApgroupSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBatchTaskProgressRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, task_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBatchTaskProgressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetBatchTaskProgressResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBatchTaskProgressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBatchTaskProgressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetBatchTaskProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBatchTaskProgressResponse, self).to_map()
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
            temp_model = GetBatchTaskProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupMiscAggTimeSerRequest(TeaModel):
    def __init__(self, apgroup_uuid=None, app_code=None, app_name=None, end=None, start=None):
        self.apgroup_uuid = apgroup_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.end = end  # type: long
        self.start = start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupMiscAggTimeSerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetGroupMiscAggTimeSerResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetGroupMiscAggTimeSerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetGroupMiscAggTimeSerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetGroupMiscAggTimeSerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetGroupMiscAggTimeSerResponse, self).to_map()
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
            temp_model = GetGroupMiscAggTimeSerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetDeviceInfoRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, cursor=None, host_name=None, id=None, idc=None,
                 logic_net_pod=None, manufacturer=None, mgn_ip=None, model=None, net_pod=None, page_size=None, password=None,
                 request_id=None, role=None, service_tag=None, username=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.cursor = cursor  # type: long
        self.host_name = host_name  # type: str
        self.id = id  # type: long
        self.idc = idc  # type: str
        self.logic_net_pod = logic_net_pod  # type: str
        self.manufacturer = manufacturer  # type: str
        self.mgn_ip = mgn_ip  # type: str
        self.model = model  # type: str
        self.net_pod = net_pod  # type: str
        self.page_size = page_size  # type: int
        self.password = password  # type: str
        self.request_id = request_id  # type: str
        self.role = role  # type: str
        self.service_tag = service_tag  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.password is not None:
            result['Password'] = self.password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetNetDeviceInfoResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: list[dict[str, any]]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNetDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNetDeviceInfoResponse, self).to_map()
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
            temp_model = GetNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNetDeviceInfoWithSizeRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, cursor=None, host_name=None, id=None, idc=None,
                 logic_net_pod=None, manufacturer=None, mgn_ip=None, model=None, net_pod=None, page_size=None, password=None,
                 request_id=None, role=None, service_tag=None, username=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.cursor = cursor  # type: long
        self.host_name = host_name  # type: str
        self.id = id  # type: long
        self.idc = idc  # type: str
        self.logic_net_pod = logic_net_pod  # type: str
        self.manufacturer = manufacturer  # type: str
        self.mgn_ip = mgn_ip  # type: str
        self.model = model  # type: str
        self.net_pod = net_pod  # type: str
        self.page_size = page_size  # type: int
        self.password = password  # type: str
        self.request_id = request_id  # type: str
        self.role = role  # type: str
        self.service_tag = service_tag  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetDeviceInfoWithSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.password is not None:
            result['Password'] = self.password
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetNetDeviceInfoWithSizeResponseBodyData(TeaModel):
    def __init__(self, count=None, data=None):
        self.count = count  # type: long
        self.data = data  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetNetDeviceInfoWithSizeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetNetDeviceInfoWithSizeResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: GetNetDeviceInfoWithSizeResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetNetDeviceInfoWithSizeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetNetDeviceInfoWithSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetNetDeviceInfoWithSizeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetNetDeviceInfoWithSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetNetDeviceInfoWithSizeResponse, self).to_map()
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
            temp_model = GetNetDeviceInfoWithSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPageVisitDataRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, end_time=None, pid=None, start_time=None):
        # appCode
        self.app_code = app_code  # type: str
        # appName
        self.app_name = app_name  # type: str
        # endTime
        self.end_time = end_time  # type: str
        # pId
        self.pid = pid  # type: str
        # startTime
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPageVisitDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.pid is not None:
            result['PId'] = self.pid
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PId') is not None:
            self.pid = m.get('PId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetPageVisitDataResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPageVisitDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPageVisitDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPageVisitDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPageVisitDataResponse, self).to_map()
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
            temp_model = GetPageVisitDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRadioRunHistoryTimeSerRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, end=None, start=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.end = end  # type: long
        self.start = start  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRadioRunHistoryTimeSerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.end is not None:
            result['End'] = self.end
        if self.start is not None:
            result['Start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Start') is not None:
            self.start = m.get('Start')
        return self


class GetRadioRunHistoryTimeSerResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRadioRunHistoryTimeSerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRadioRunHistoryTimeSerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRadioRunHistoryTimeSerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRadioRunHistoryTimeSerResponse, self).to_map()
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
            temp_model = GetRadioRunHistoryTimeSerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStaDetailedStatusByMacRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, sta_mac=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.sta_mac = sta_mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStaDetailedStatusByMacRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.sta_mac is not None:
            result['StaMac'] = self.sta_mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StaMac') is not None:
            self.sta_mac = m.get('StaMac')
        return self


class GetStaDetailedStatusByMacResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStaDetailedStatusByMacResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetStaDetailedStatusByMacResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStaDetailedStatusByMacResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStaDetailedStatusByMacResponse, self).to_map()
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
            temp_model = GetStaDetailedStatusByMacResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStaStatusListByApRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, cursor=None, page_size=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.cursor = cursor  # type: long
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStaStatusListByApRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetStaStatusListByApResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetStaStatusListByApResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetStaStatusListByApResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetStaStatusListByApResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetStaStatusListByApResponse, self).to_map()
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
            temp_model = GetStaStatusListByApResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class JudgeXingTianBusinessRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, realm_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.realm_id = realm_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JudgeXingTianBusinessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.realm_id is not None:
            result['RealmId'] = self.realm_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RealmId') is not None:
            self.realm_id = m.get('RealmId')
        return self


class JudgeXingTianBusinessResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: bool
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(JudgeXingTianBusinessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class JudgeXingTianBusinessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: JudgeXingTianBusinessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(JudgeXingTianBusinessResponse, self).to_map()
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
            temp_model = JudgeXingTianBusinessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickStaRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, sta_mac=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.sta_mac = sta_mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickStaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.sta_mac is not None:
            result['StaMac'] = self.sta_mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('StaMac') is not None:
            self.sta_mac = m.get('StaMac')
        return self


class KickStaResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(KickStaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class KickStaResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: KickStaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(KickStaResponse, self).to_map()
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
            temp_model = KickStaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApgroupDescendantRequest(TeaModel):
    def __init__(self, apgroup_id=None, apgroup_uuid=None, app_code=None, app_name=None, cursor=None, level=None,
                 page_size=None):
        self.apgroup_id = apgroup_id  # type: long
        self.apgroup_uuid = apgroup_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.cursor = cursor  # type: long
        self.level = level  # type: long
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApgroupDescendantRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.level is not None:
            result['Level'] = self.level
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApgroupDescendantResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApgroupDescendantResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListApgroupDescendantResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApgroupDescendantResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApgroupDescendantResponse, self).to_map()
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
            temp_model = ListApgroupDescendantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobOrdersRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, changing_type=None, client_system=None, client_unique_id=None,
                 cursor=None, end_time=None, handler=None, id=None, order_status=None, page_size=None, request_id=None,
                 start_time=None, status=None, title=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.changing_type = changing_type  # type: str
        self.client_system = client_system  # type: str
        self.client_unique_id = client_unique_id  # type: str
        self.cursor = cursor  # type: long
        self.end_time = end_time  # type: str
        self.handler = handler  # type: str
        self.id = id  # type: str
        self.order_status = order_status  # type: str
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobOrdersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.changing_type is not None:
            result['ChangingType'] = self.changing_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.handler is not None:
            result['Handler'] = self.handler
        if self.id is not None:
            result['Id'] = self.id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ChangingType') is not None:
            self.changing_type = m.get('ChangingType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Handler') is not None:
            self.handler = m.get('Handler')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListJobOrdersResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: list[dict[str, any]]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobOrdersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListJobOrdersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobOrdersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobOrdersResponse, self).to_map()
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
            temp_model = ListJobOrdersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobOrdersWithSizeRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, changing_type=None, client_system=None, client_unique_id=None,
                 cursor=None, end_time=None, handler=None, id=None, order_status=None, page_size=None, request_id=None,
                 start_time=None, status=None, title=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.changing_type = changing_type  # type: str
        self.client_system = client_system  # type: str
        self.client_unique_id = client_unique_id  # type: str
        self.cursor = cursor  # type: long
        self.end_time = end_time  # type: str
        self.handler = handler  # type: str
        self.id = id  # type: str
        self.order_status = order_status  # type: str
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.start_time = start_time  # type: str
        self.status = status  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobOrdersWithSizeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.changing_type is not None:
            result['ChangingType'] = self.changing_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.cursor is not None:
            result['Cursor'] = self.cursor
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.handler is not None:
            result['Handler'] = self.handler
        if self.id is not None:
            result['Id'] = self.id
        if self.order_status is not None:
            result['OrderStatus'] = self.order_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ChangingType') is not None:
            self.changing_type = m.get('ChangingType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Cursor') is not None:
            self.cursor = m.get('Cursor')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Handler') is not None:
            self.handler = m.get('Handler')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListJobOrdersWithSizeResponseBodyData(TeaModel):
    def __init__(self, count=None, data=None):
        self.count = count  # type: long
        self.data = data  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListJobOrdersWithSizeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListJobOrdersWithSizeResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: ListJobOrdersWithSizeResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListJobOrdersWithSizeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListJobOrdersWithSizeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListJobOrdersWithSizeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListJobOrdersWithSizeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListJobOrdersWithSizeResponse, self).to_map()
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
            temp_model = ListJobOrdersWithSizeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NewApgroupConfigRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, name=None, parent_apgroup_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.name = name  # type: str
        self.parent_apgroup_id = parent_apgroup_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewApgroupConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_apgroup_id is not None:
            result['ParentApgroupId'] = self.parent_apgroup_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentApgroupId') is not None:
            self.parent_apgroup_id = m.get('ParentApgroupId')
        return self


class NewApgroupConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewApgroupConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class NewApgroupConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NewApgroupConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NewApgroupConfigResponse, self).to_map()
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
            temp_model = NewApgroupConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NewJobOrderRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, callback_url=None, change_type=None, client_system=None,
                 client_unique_id=None, creator=None, params=None, refer_url=None, request_id=None, title=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.callback_url = callback_url  # type: str
        self.change_type = change_type  # type: str
        self.client_system = client_system  # type: str
        self.client_unique_id = client_unique_id  # type: str
        self.creator = creator  # type: str
        self.params = params  # type: dict[str, any]
        self.refer_url = refer_url  # type: str
        self.request_id = request_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewJobOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.change_type is not None:
            result['ChangeType'] = self.change_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.params is not None:
            result['Params'] = self.params
        if self.refer_url is not None:
            result['ReferUrl'] = self.refer_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('ReferUrl') is not None:
            self.refer_url = m.get('ReferUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class NewJobOrderShrinkRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, callback_url=None, change_type=None, client_system=None,
                 client_unique_id=None, creator=None, params_shrink=None, refer_url=None, request_id=None, title=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.callback_url = callback_url  # type: str
        self.change_type = change_type  # type: str
        self.client_system = client_system  # type: str
        self.client_unique_id = client_unique_id  # type: str
        self.creator = creator  # type: str
        self.params_shrink = params_shrink  # type: str
        self.refer_url = refer_url  # type: str
        self.request_id = request_id  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewJobOrderShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.change_type is not None:
            result['ChangeType'] = self.change_type
        if self.client_system is not None:
            result['ClientSystem'] = self.client_system
        if self.client_unique_id is not None:
            result['ClientUniqueId'] = self.client_unique_id
        if self.creator is not None:
            result['Creator'] = self.creator
        if self.params_shrink is not None:
            result['Params'] = self.params_shrink
        if self.refer_url is not None:
            result['ReferUrl'] = self.refer_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('ChangeType') is not None:
            self.change_type = m.get('ChangeType')
        if m.get('ClientSystem') is not None:
            self.client_system = m.get('ClientSystem')
        if m.get('ClientUniqueId') is not None:
            self.client_unique_id = m.get('ClientUniqueId')
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')
        if m.get('Params') is not None:
            self.params_shrink = m.get('Params')
        if m.get('ReferUrl') is not None:
            self.refer_url = m.get('ReferUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class NewJobOrderResponseBodyData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewJobOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class NewJobOrderResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: NewJobOrderResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(NewJobOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = NewJobOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NewJobOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NewJobOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NewJobOrderResponse, self).to_map()
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
            temp_model = NewJobOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class NewNetDeviceInfoRequestDevices(TeaModel):
    def __init__(self, host_name=None, idc=None, logic_net_pod=None, manufacturer=None, mgn_ip=None, model=None,
                 net_pod=None, password=None, role=None, service_tag=None, username=None):
        self.host_name = host_name  # type: str
        self.idc = idc  # type: str
        self.logic_net_pod = logic_net_pod  # type: str
        self.manufacturer = manufacturer  # type: str
        self.mgn_ip = mgn_ip  # type: str
        self.model = model  # type: str
        self.net_pod = net_pod  # type: str
        self.password = password  # type: str
        self.role = role  # type: str
        self.service_tag = service_tag  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewNetDeviceInfoRequestDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.password is not None:
            result['Password'] = self.password
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class NewNetDeviceInfoRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, devices=None, request_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.devices = devices  # type: list[NewNetDeviceInfoRequestDevices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(NewNetDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = NewNetDeviceInfoRequestDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NewNetDeviceInfoResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: list[long]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(NewNetDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class NewNetDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: NewNetDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(NewNetDeviceInfoResponse, self).to_map()
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
            temp_model = NewNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutAppConfigAndSaveRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, configure_type=None, current_time=None, data=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.configure_type = configure_type  # type: str
        self.current_time = current_time  # type: long
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutAppConfigAndSaveRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.configure_type is not None:
            result['ConfigureType'] = self.configure_type
        if self.current_time is not None:
            result['CurrentTime'] = self.current_time
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ConfigureType') is not None:
            self.configure_type = m.get('ConfigureType')
        if m.get('CurrentTime') is not None:
            self.current_time = m.get('CurrentTime')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class PutAppConfigAndSaveResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(PutAppConfigAndSaveResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class PutAppConfigAndSaveResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PutAppConfigAndSaveResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PutAppConfigAndSaveResponse, self).to_map()
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
            temp_model = PutAppConfigAndSaveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryJobOrderRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, order_id=None, request_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.order_id = order_id  # type: long
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryJobOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryJobOrderResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryJobOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryJobOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryJobOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryJobOrderResponse, self).to_map()
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
            temp_model = QueryJobOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootApRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootApRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class RebootApResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RebootApResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RebootApResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RebootApResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RebootApResponse, self).to_map()
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
            temp_model = RebootApResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterApAssetRequest(TeaModel):
    def __init__(self, ap_group_uuid=None, app_code=None, app_name=None, id=None, mac=None, serial_no=None):
        self.ap_group_uuid = ap_group_uuid  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.id = id  # type: long
        self.mac = mac  # type: str
        self.serial_no = serial_no  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterApAssetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_group_uuid is not None:
            result['ApGroupUUId'] = self.ap_group_uuid
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApGroupUUId') is not None:
            self.ap_group_uuid = m.get('ApGroupUUId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        return self


class RegisterApAssetResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterApAssetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterApAssetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterApAssetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterApAssetResponse, self).to_map()
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
            temp_model = RegisterApAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RepairApRadioRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, radio_index=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.radio_index = radio_index  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RepairApRadioRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')
        return self


class RepairApRadioResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: bool
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RepairApRadioResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RepairApRadioResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RepairApRadioResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RepairApRadioResponse, self).to_map()
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
            temp_model = RepairApRadioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApBasicConfigRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, country=None, dai=None, description=None, echo_int=None,
                 failover=None, id=None, insecure_allowed=None, lan_ip=None, lan_mask=None, lan_status=None, log_ip=None,
                 log_level=None, name=None, passwd=None, protocol=None, route=None, scan=None, token_server=None, vpn=None,
                 work_mode=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.country = country  # type: str
        self.dai = dai  # type: str
        self.description = description  # type: str
        self.echo_int = echo_int  # type: int
        self.failover = failover  # type: int
        self.id = id  # type: long
        self.insecure_allowed = insecure_allowed  # type: int
        self.lan_ip = lan_ip  # type: str
        self.lan_mask = lan_mask  # type: str
        self.lan_status = lan_status  # type: int
        self.log_ip = log_ip  # type: str
        self.log_level = log_level  # type: int
        self.name = name  # type: str
        self.passwd = passwd  # type: str
        self.protocol = protocol  # type: str
        self.route = route  # type: str
        self.scan = scan  # type: int
        self.token_server = token_server  # type: str
        self.vpn = vpn  # type: str
        self.work_mode = work_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApBasicConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.country is not None:
            result['Country'] = self.country
        if self.dai is not None:
            result['Dai'] = self.dai
        if self.description is not None:
            result['Description'] = self.description
        if self.echo_int is not None:
            result['EchoInt'] = self.echo_int
        if self.failover is not None:
            result['Failover'] = self.failover
        if self.id is not None:
            result['Id'] = self.id
        if self.insecure_allowed is not None:
            result['InsecureAllowed'] = self.insecure_allowed
        if self.lan_ip is not None:
            result['LanIp'] = self.lan_ip
        if self.lan_mask is not None:
            result['LanMask'] = self.lan_mask
        if self.lan_status is not None:
            result['LanStatus'] = self.lan_status
        if self.log_ip is not None:
            result['LogIp'] = self.log_ip
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.name is not None:
            result['Name'] = self.name
        if self.passwd is not None:
            result['Passwd'] = self.passwd
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.route is not None:
            result['Route'] = self.route
        if self.scan is not None:
            result['Scan'] = self.scan
        if self.token_server is not None:
            result['TokenServer'] = self.token_server
        if self.vpn is not None:
            result['Vpn'] = self.vpn
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Dai') is not None:
            self.dai = m.get('Dai')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EchoInt') is not None:
            self.echo_int = m.get('EchoInt')
        if m.get('Failover') is not None:
            self.failover = m.get('Failover')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsecureAllowed') is not None:
            self.insecure_allowed = m.get('InsecureAllowed')
        if m.get('LanIp') is not None:
            self.lan_ip = m.get('LanIp')
        if m.get('LanMask') is not None:
            self.lan_mask = m.get('LanMask')
        if m.get('LanStatus') is not None:
            self.lan_status = m.get('LanStatus')
        if m.get('LogIp') is not None:
            self.log_ip = m.get('LogIp')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('Scan') is not None:
            self.scan = m.get('Scan')
        if m.get('TokenServer') is not None:
            self.token_server = m.get('TokenServer')
        if m.get('Vpn') is not None:
            self.vpn = m.get('Vpn')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        return self


class SaveApBasicConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApBasicConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApBasicConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApBasicConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApBasicConfigResponse, self).to_map()
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
            temp_model = SaveApBasicConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApPortalConfigRequest(TeaModel):
    def __init__(self, ap_config_id=None, app_auth_url=None, app_code=None, app_name=None, auth_key=None,
                 auth_secret=None, check_url=None, client_download=None, client_upload=None, countdown=None, network=None,
                 portal_types=None, portal_url=None, time_stamp=None, total_download=None, total_upload=None, web_auth_url=None,
                 whitelist=None):
        self.ap_config_id = ap_config_id  # type: long
        self.app_auth_url = app_auth_url  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.auth_key = auth_key  # type: str
        self.auth_secret = auth_secret  # type: str
        self.check_url = check_url  # type: str
        self.client_download = client_download  # type: int
        self.client_upload = client_upload  # type: int
        self.countdown = countdown  # type: int
        self.network = network  # type: int
        self.portal_types = portal_types  # type: list[str]
        self.portal_url = portal_url  # type: str
        self.time_stamp = time_stamp  # type: long
        self.total_download = total_download  # type: int
        self.total_upload = total_upload  # type: int
        self.web_auth_url = web_auth_url  # type: str
        self.whitelist = whitelist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApPortalConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_config_id is not None:
            result['ApConfigId'] = self.ap_config_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types is not None:
            result['PortalTypes'] = self.portal_types
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApConfigId') is not None:
            self.ap_config_id = m.get('ApConfigId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApPortalConfigShrinkRequest(TeaModel):
    def __init__(self, ap_config_id=None, app_auth_url=None, app_code=None, app_name=None, auth_key=None,
                 auth_secret=None, check_url=None, client_download=None, client_upload=None, countdown=None, network=None,
                 portal_types_shrink=None, portal_url=None, time_stamp=None, total_download=None, total_upload=None, web_auth_url=None,
                 whitelist=None):
        self.ap_config_id = ap_config_id  # type: long
        self.app_auth_url = app_auth_url  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.auth_key = auth_key  # type: str
        self.auth_secret = auth_secret  # type: str
        self.check_url = check_url  # type: str
        self.client_download = client_download  # type: int
        self.client_upload = client_upload  # type: int
        self.countdown = countdown  # type: int
        self.network = network  # type: int
        self.portal_types_shrink = portal_types_shrink  # type: str
        self.portal_url = portal_url  # type: str
        self.time_stamp = time_stamp  # type: long
        self.total_download = total_download  # type: int
        self.total_upload = total_upload  # type: int
        self.web_auth_url = web_auth_url  # type: str
        self.whitelist = whitelist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApPortalConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_config_id is not None:
            result['ApConfigId'] = self.ap_config_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types_shrink is not None:
            result['PortalTypes'] = self.portal_types_shrink
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApConfigId') is not None:
            self.ap_config_id = m.get('ApConfigId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types_shrink = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApPortalConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApPortalConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApPortalConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApPortalConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApPortalConfigResponse, self).to_map()
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
            temp_model = SaveApPortalConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApRadioConfigRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, bcast_rate=None, beacon_int=None, channel=None, disabled=None,
                 frag=None, htmode=None, hwmode=None, id=None, mcast_rate=None, mgmt_rate=None, minrate=None, noscan=None,
                 probereq=None, require_mode=None, rts=None, shortgi=None, txpower=None, uapsd=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.bcast_rate = bcast_rate  # type: int
        self.beacon_int = beacon_int  # type: int
        self.channel = channel  # type: str
        self.disabled = disabled  # type: str
        self.frag = frag  # type: int
        self.htmode = htmode  # type: str
        self.hwmode = hwmode  # type: str
        self.id = id  # type: long
        self.mcast_rate = mcast_rate  # type: int
        self.mgmt_rate = mgmt_rate  # type: int
        self.minrate = minrate  # type: int
        self.noscan = noscan  # type: str
        self.probereq = probereq  # type: str
        self.require_mode = require_mode  # type: str
        self.rts = rts  # type: int
        self.shortgi = shortgi  # type: str
        self.txpower = txpower  # type: str
        self.uapsd = uapsd  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApRadioConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.bcast_rate is not None:
            result['BcastRate'] = self.bcast_rate
        if self.beacon_int is not None:
            result['BeaconInt'] = self.beacon_int
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.frag is not None:
            result['Frag'] = self.frag
        if self.htmode is not None:
            result['Htmode'] = self.htmode
        if self.hwmode is not None:
            result['Hwmode'] = self.hwmode
        if self.id is not None:
            result['Id'] = self.id
        if self.mcast_rate is not None:
            result['McastRate'] = self.mcast_rate
        if self.mgmt_rate is not None:
            result['MgmtRate'] = self.mgmt_rate
        if self.minrate is not None:
            result['Minrate'] = self.minrate
        if self.noscan is not None:
            result['Noscan'] = self.noscan
        if self.probereq is not None:
            result['Probereq'] = self.probereq
        if self.require_mode is not None:
            result['RequireMode'] = self.require_mode
        if self.rts is not None:
            result['Rts'] = self.rts
        if self.shortgi is not None:
            result['Shortgi'] = self.shortgi
        if self.txpower is not None:
            result['Txpower'] = self.txpower
        if self.uapsd is not None:
            result['Uapsd'] = self.uapsd
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('BcastRate') is not None:
            self.bcast_rate = m.get('BcastRate')
        if m.get('BeaconInt') is not None:
            self.beacon_int = m.get('BeaconInt')
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('Frag') is not None:
            self.frag = m.get('Frag')
        if m.get('Htmode') is not None:
            self.htmode = m.get('Htmode')
        if m.get('Hwmode') is not None:
            self.hwmode = m.get('Hwmode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('McastRate') is not None:
            self.mcast_rate = m.get('McastRate')
        if m.get('MgmtRate') is not None:
            self.mgmt_rate = m.get('MgmtRate')
        if m.get('Minrate') is not None:
            self.minrate = m.get('Minrate')
        if m.get('Noscan') is not None:
            self.noscan = m.get('Noscan')
        if m.get('Probereq') is not None:
            self.probereq = m.get('Probereq')
        if m.get('RequireMode') is not None:
            self.require_mode = m.get('RequireMode')
        if m.get('Rts') is not None:
            self.rts = m.get('Rts')
        if m.get('Shortgi') is not None:
            self.shortgi = m.get('Shortgi')
        if m.get('Txpower') is not None:
            self.txpower = m.get('Txpower')
        if m.get('Uapsd') is not None:
            self.uapsd = m.get('Uapsd')
        return self


class SaveApRadioConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApRadioConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApRadioConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApRadioConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApRadioConfigResponse, self).to_map()
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
            temp_model = SaveApRadioConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApSsidConfigRequest(TeaModel):
    def __init__(self, acct_port=None, acct_secret=None, acct_server=None, acct_status_server_work=None,
                 ap_asset_id=None, app_code=None, app_name=None, arp_proxy_enable=None, auth_cache=None, auth_port=None,
                 auth_secret=None, auth_server=None, auth_status_server_work=None, cir=None, cir_step=None, cir_type=None,
                 cir_ul=None, dae_client=None, dae_port=None, dae_secret=None, disabled=None, disassoc_low_ack=None,
                 disassoc_weak_rssi=None, dynamic_vlan=None, enc_key=None, encryption=None, fourth_auth_port=None,
                 fourth_auth_secret=None, fourth_auth_server=None, ft_over_ds=None, hidden=None, id=None, ieee_80211r=None,
                 ieee_80211w=None, ignore_weak_probe=None, isolate=None, lite_effect=None, mac=None, max_inactivity=None,
                 maxassoc=None, mobility_domain=None, multicast_forward=None, nasid=None, nd_proxy_work=None, network=None,
                 ownip=None, radio_index=None, secondary_acct_port=None, secondary_acct_secret=None,
                 secondary_acct_server=None, secondary_auth_port=None, secondary_auth_secret=None, secondary_auth_server=None,
                 send_config_to_ap=None, short_preamble=None, ssid=None, ssid_lb=None, third_auth_port=None, third_auth_secret=None,
                 third_auth_server=None, type=None, vlan_dhcp=None, wmm=None):
        self.acct_port = acct_port  # type: int
        self.acct_secret = acct_secret  # type: str
        self.acct_server = acct_server  # type: str
        self.acct_status_server_work = acct_status_server_work  # type: int
        self.ap_asset_id = ap_asset_id  # type: long
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.arp_proxy_enable = arp_proxy_enable  # type: int
        self.auth_cache = auth_cache  # type: str
        self.auth_port = auth_port  # type: int
        self.auth_secret = auth_secret  # type: str
        self.auth_server = auth_server  # type: str
        self.auth_status_server_work = auth_status_server_work  # type: int
        self.cir = cir  # type: long
        self.cir_step = cir_step  # type: long
        self.cir_type = cir_type  # type: int
        self.cir_ul = cir_ul  # type: long
        self.dae_client = dae_client  # type: str
        self.dae_port = dae_port  # type: int
        self.dae_secret = dae_secret  # type: str
        self.disabled = disabled  # type: str
        self.disassoc_low_ack = disassoc_low_ack  # type: str
        self.disassoc_weak_rssi = disassoc_weak_rssi  # type: int
        self.dynamic_vlan = dynamic_vlan  # type: int
        self.enc_key = enc_key  # type: str
        self.encryption = encryption  # type: str
        self.fourth_auth_port = fourth_auth_port  # type: int
        self.fourth_auth_secret = fourth_auth_secret  # type: str
        self.fourth_auth_server = fourth_auth_server  # type: str
        self.ft_over_ds = ft_over_ds  # type: int
        self.hidden = hidden  # type: str
        self.id = id  # type: long
        self.ieee_80211r = ieee_80211r  # type: int
        self.ieee_80211w = ieee_80211w  # type: str
        self.ignore_weak_probe = ignore_weak_probe  # type: int
        self.isolate = isolate  # type: str
        self.lite_effect = lite_effect  # type: bool
        self.mac = mac  # type: str
        self.max_inactivity = max_inactivity  # type: int
        self.maxassoc = maxassoc  # type: int
        self.mobility_domain = mobility_domain  # type: str
        self.multicast_forward = multicast_forward  # type: int
        self.nasid = nasid  # type: str
        self.nd_proxy_work = nd_proxy_work  # type: int
        self.network = network  # type: int
        self.ownip = ownip  # type: str
        self.radio_index = radio_index  # type: str
        self.secondary_acct_port = secondary_acct_port  # type: int
        self.secondary_acct_secret = secondary_acct_secret  # type: str
        self.secondary_acct_server = secondary_acct_server  # type: str
        self.secondary_auth_port = secondary_auth_port  # type: int
        self.secondary_auth_secret = secondary_auth_secret  # type: str
        self.secondary_auth_server = secondary_auth_server  # type: str
        self.send_config_to_ap = send_config_to_ap  # type: bool
        self.short_preamble = short_preamble  # type: str
        self.ssid = ssid  # type: str
        self.ssid_lb = ssid_lb  # type: int
        self.third_auth_port = third_auth_port  # type: int
        self.third_auth_secret = third_auth_secret  # type: str
        self.third_auth_server = third_auth_server  # type: str
        self.type = type  # type: int
        self.vlan_dhcp = vlan_dhcp  # type: int
        self.wmm = wmm  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApSsidConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acct_port is not None:
            result['AcctPort'] = self.acct_port
        if self.acct_secret is not None:
            result['AcctSecret'] = self.acct_secret
        if self.acct_server is not None:
            result['AcctServer'] = self.acct_server
        if self.acct_status_server_work is not None:
            result['AcctStatusServerWork'] = self.acct_status_server_work
        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.arp_proxy_enable is not None:
            result['ArpProxyEnable'] = self.arp_proxy_enable
        if self.auth_cache is not None:
            result['AuthCache'] = self.auth_cache
        if self.auth_port is not None:
            result['AuthPort'] = self.auth_port
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.auth_server is not None:
            result['AuthServer'] = self.auth_server
        if self.auth_status_server_work is not None:
            result['AuthStatusServerWork'] = self.auth_status_server_work
        if self.cir is not None:
            result['Cir'] = self.cir
        if self.cir_step is not None:
            result['CirStep'] = self.cir_step
        if self.cir_type is not None:
            result['CirType'] = self.cir_type
        if self.cir_ul is not None:
            result['CirUl'] = self.cir_ul
        if self.dae_client is not None:
            result['DaeClient'] = self.dae_client
        if self.dae_port is not None:
            result['DaePort'] = self.dae_port
        if self.dae_secret is not None:
            result['DaeSecret'] = self.dae_secret
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.disassoc_low_ack is not None:
            result['DisassocLowAck'] = self.disassoc_low_ack
        if self.disassoc_weak_rssi is not None:
            result['DisassocWeakRssi'] = self.disassoc_weak_rssi
        if self.dynamic_vlan is not None:
            result['DynamicVlan'] = self.dynamic_vlan
        if self.enc_key is not None:
            result['EncKey'] = self.enc_key
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.fourth_auth_port is not None:
            result['FourthAuthPort'] = self.fourth_auth_port
        if self.fourth_auth_secret is not None:
            result['FourthAuthSecret'] = self.fourth_auth_secret
        if self.fourth_auth_server is not None:
            result['FourthAuthServer'] = self.fourth_auth_server
        if self.ft_over_ds is not None:
            result['FtOverDs'] = self.ft_over_ds
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.id is not None:
            result['Id'] = self.id
        if self.ieee_80211r is not None:
            result['Ieee80211r'] = self.ieee_80211r
        if self.ieee_80211w is not None:
            result['Ieee80211w'] = self.ieee_80211w
        if self.ignore_weak_probe is not None:
            result['IgnoreWeakProbe'] = self.ignore_weak_probe
        if self.isolate is not None:
            result['Isolate'] = self.isolate
        if self.lite_effect is not None:
            result['LiteEffect'] = self.lite_effect
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.max_inactivity is not None:
            result['MaxInactivity'] = self.max_inactivity
        if self.maxassoc is not None:
            result['Maxassoc'] = self.maxassoc
        if self.mobility_domain is not None:
            result['MobilityDomain'] = self.mobility_domain
        if self.multicast_forward is not None:
            result['MulticastForward'] = self.multicast_forward
        if self.nasid is not None:
            result['Nasid'] = self.nasid
        if self.nd_proxy_work is not None:
            result['NdProxyWork'] = self.nd_proxy_work
        if self.network is not None:
            result['Network'] = self.network
        if self.ownip is not None:
            result['Ownip'] = self.ownip
        if self.radio_index is not None:
            result['RadioIndex'] = self.radio_index
        if self.secondary_acct_port is not None:
            result['SecondaryAcctPort'] = self.secondary_acct_port
        if self.secondary_acct_secret is not None:
            result['SecondaryAcctSecret'] = self.secondary_acct_secret
        if self.secondary_acct_server is not None:
            result['SecondaryAcctServer'] = self.secondary_acct_server
        if self.secondary_auth_port is not None:
            result['SecondaryAuthPort'] = self.secondary_auth_port
        if self.secondary_auth_secret is not None:
            result['SecondaryAuthSecret'] = self.secondary_auth_secret
        if self.secondary_auth_server is not None:
            result['SecondaryAuthServer'] = self.secondary_auth_server
        if self.send_config_to_ap is not None:
            result['SendConfigToAp'] = self.send_config_to_ap
        if self.short_preamble is not None:
            result['ShortPreamble'] = self.short_preamble
        if self.ssid is not None:
            result['Ssid'] = self.ssid
        if self.ssid_lb is not None:
            result['SsidLb'] = self.ssid_lb
        if self.third_auth_port is not None:
            result['ThirdAuthPort'] = self.third_auth_port
        if self.third_auth_secret is not None:
            result['ThirdAuthSecret'] = self.third_auth_secret
        if self.third_auth_server is not None:
            result['ThirdAuthServer'] = self.third_auth_server
        if self.type is not None:
            result['Type'] = self.type
        if self.vlan_dhcp is not None:
            result['VlanDhcp'] = self.vlan_dhcp
        if self.wmm is not None:
            result['Wmm'] = self.wmm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcctPort') is not None:
            self.acct_port = m.get('AcctPort')
        if m.get('AcctSecret') is not None:
            self.acct_secret = m.get('AcctSecret')
        if m.get('AcctServer') is not None:
            self.acct_server = m.get('AcctServer')
        if m.get('AcctStatusServerWork') is not None:
            self.acct_status_server_work = m.get('AcctStatusServerWork')
        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('ArpProxyEnable') is not None:
            self.arp_proxy_enable = m.get('ArpProxyEnable')
        if m.get('AuthCache') is not None:
            self.auth_cache = m.get('AuthCache')
        if m.get('AuthPort') is not None:
            self.auth_port = m.get('AuthPort')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('AuthServer') is not None:
            self.auth_server = m.get('AuthServer')
        if m.get('AuthStatusServerWork') is not None:
            self.auth_status_server_work = m.get('AuthStatusServerWork')
        if m.get('Cir') is not None:
            self.cir = m.get('Cir')
        if m.get('CirStep') is not None:
            self.cir_step = m.get('CirStep')
        if m.get('CirType') is not None:
            self.cir_type = m.get('CirType')
        if m.get('CirUl') is not None:
            self.cir_ul = m.get('CirUl')
        if m.get('DaeClient') is not None:
            self.dae_client = m.get('DaeClient')
        if m.get('DaePort') is not None:
            self.dae_port = m.get('DaePort')
        if m.get('DaeSecret') is not None:
            self.dae_secret = m.get('DaeSecret')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DisassocLowAck') is not None:
            self.disassoc_low_ack = m.get('DisassocLowAck')
        if m.get('DisassocWeakRssi') is not None:
            self.disassoc_weak_rssi = m.get('DisassocWeakRssi')
        if m.get('DynamicVlan') is not None:
            self.dynamic_vlan = m.get('DynamicVlan')
        if m.get('EncKey') is not None:
            self.enc_key = m.get('EncKey')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('FourthAuthPort') is not None:
            self.fourth_auth_port = m.get('FourthAuthPort')
        if m.get('FourthAuthSecret') is not None:
            self.fourth_auth_secret = m.get('FourthAuthSecret')
        if m.get('FourthAuthServer') is not None:
            self.fourth_auth_server = m.get('FourthAuthServer')
        if m.get('FtOverDs') is not None:
            self.ft_over_ds = m.get('FtOverDs')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ieee80211r') is not None:
            self.ieee_80211r = m.get('Ieee80211r')
        if m.get('Ieee80211w') is not None:
            self.ieee_80211w = m.get('Ieee80211w')
        if m.get('IgnoreWeakProbe') is not None:
            self.ignore_weak_probe = m.get('IgnoreWeakProbe')
        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')
        if m.get('LiteEffect') is not None:
            self.lite_effect = m.get('LiteEffect')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('MaxInactivity') is not None:
            self.max_inactivity = m.get('MaxInactivity')
        if m.get('Maxassoc') is not None:
            self.maxassoc = m.get('Maxassoc')
        if m.get('MobilityDomain') is not None:
            self.mobility_domain = m.get('MobilityDomain')
        if m.get('MulticastForward') is not None:
            self.multicast_forward = m.get('MulticastForward')
        if m.get('Nasid') is not None:
            self.nasid = m.get('Nasid')
        if m.get('NdProxyWork') is not None:
            self.nd_proxy_work = m.get('NdProxyWork')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('Ownip') is not None:
            self.ownip = m.get('Ownip')
        if m.get('RadioIndex') is not None:
            self.radio_index = m.get('RadioIndex')
        if m.get('SecondaryAcctPort') is not None:
            self.secondary_acct_port = m.get('SecondaryAcctPort')
        if m.get('SecondaryAcctSecret') is not None:
            self.secondary_acct_secret = m.get('SecondaryAcctSecret')
        if m.get('SecondaryAcctServer') is not None:
            self.secondary_acct_server = m.get('SecondaryAcctServer')
        if m.get('SecondaryAuthPort') is not None:
            self.secondary_auth_port = m.get('SecondaryAuthPort')
        if m.get('SecondaryAuthSecret') is not None:
            self.secondary_auth_secret = m.get('SecondaryAuthSecret')
        if m.get('SecondaryAuthServer') is not None:
            self.secondary_auth_server = m.get('SecondaryAuthServer')
        if m.get('SendConfigToAp') is not None:
            self.send_config_to_ap = m.get('SendConfigToAp')
        if m.get('ShortPreamble') is not None:
            self.short_preamble = m.get('ShortPreamble')
        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')
        if m.get('SsidLb') is not None:
            self.ssid_lb = m.get('SsidLb')
        if m.get('ThirdAuthPort') is not None:
            self.third_auth_port = m.get('ThirdAuthPort')
        if m.get('ThirdAuthSecret') is not None:
            self.third_auth_secret = m.get('ThirdAuthSecret')
        if m.get('ThirdAuthServer') is not None:
            self.third_auth_server = m.get('ThirdAuthServer')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VlanDhcp') is not None:
            self.vlan_dhcp = m.get('VlanDhcp')
        if m.get('Wmm') is not None:
            self.wmm = m.get('Wmm')
        return self


class SaveApSsidConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApSsidConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SaveApSsidConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApSsidConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApSsidConfigResponse, self).to_map()
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
            temp_model = SaveApSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApThirdAppRequest(TeaModel):
    def __init__(self, add_style=None, ap_asset_id=None, app_code=None, app_data=None, app_name=None, category=None,
                 id=None, mac=None, third_app_name=None, version=None):
        self.add_style = add_style  # type: int
        self.ap_asset_id = ap_asset_id  # type: long
        self.app_code = app_code  # type: str
        self.app_data = app_data  # type: str
        self.app_name = app_name  # type: str
        self.category = category  # type: int
        self.id = id  # type: long
        self.mac = mac  # type: str
        self.third_app_name = third_app_name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApThirdAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_style is not None:
            result['AddStyle'] = self.add_style
        if self.ap_asset_id is not None:
            result['ApAssetId'] = self.ap_asset_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_data is not None:
            result['AppData'] = self.app_data
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.third_app_name is not None:
            result['ThirdAppName'] = self.third_app_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddStyle') is not None:
            self.add_style = m.get('AddStyle')
        if m.get('ApAssetId') is not None:
            self.ap_asset_id = m.get('ApAssetId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppData') is not None:
            self.app_data = m.get('AppData')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('ThirdAppName') is not None:
            self.third_app_name = m.get('ThirdAppName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class SaveApThirdAppResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApThirdAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApThirdAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApThirdAppResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApThirdAppResponse, self).to_map()
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
            temp_model = SaveApThirdAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApgroupBasicConfigRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, country=None, dai=None, description=None, echo_int=None,
                 failover=None, id=None, insecure_allowed=None, is_config_strong_consistency=None, lan_ip=None,
                 lan_mask=None, lan_status=None, log_ip=None, log_level=None, name=None, parent_apgroup_id=None, passwd=None,
                 protocol=None, route=None, scan=None, token_server=None, vpn=None, work_mode=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.country = country  # type: str
        self.dai = dai  # type: str
        self.description = description  # type: str
        self.echo_int = echo_int  # type: int
        self.failover = failover  # type: int
        self.id = id  # type: long
        self.insecure_allowed = insecure_allowed  # type: int
        self.is_config_strong_consistency = is_config_strong_consistency  # type: bool
        self.lan_ip = lan_ip  # type: str
        self.lan_mask = lan_mask  # type: str
        self.lan_status = lan_status  # type: int
        self.log_ip = log_ip  # type: str
        self.log_level = log_level  # type: int
        self.name = name  # type: str
        self.parent_apgroup_id = parent_apgroup_id  # type: long
        self.passwd = passwd  # type: str
        self.protocol = protocol  # type: str
        self.route = route  # type: str
        self.scan = scan  # type: int
        self.token_server = token_server  # type: str
        self.vpn = vpn  # type: str
        self.work_mode = work_mode  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupBasicConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.country is not None:
            result['Country'] = self.country
        if self.dai is not None:
            result['Dai'] = self.dai
        if self.description is not None:
            result['Description'] = self.description
        if self.echo_int is not None:
            result['EchoInt'] = self.echo_int
        if self.failover is not None:
            result['Failover'] = self.failover
        if self.id is not None:
            result['Id'] = self.id
        if self.insecure_allowed is not None:
            result['InsecureAllowed'] = self.insecure_allowed
        if self.is_config_strong_consistency is not None:
            result['IsConfigStrongConsistency'] = self.is_config_strong_consistency
        if self.lan_ip is not None:
            result['LanIp'] = self.lan_ip
        if self.lan_mask is not None:
            result['LanMask'] = self.lan_mask
        if self.lan_status is not None:
            result['LanStatus'] = self.lan_status
        if self.log_ip is not None:
            result['LogIp'] = self.log_ip
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.name is not None:
            result['Name'] = self.name
        if self.parent_apgroup_id is not None:
            result['ParentApgroupId'] = self.parent_apgroup_id
        if self.passwd is not None:
            result['Passwd'] = self.passwd
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.route is not None:
            result['Route'] = self.route
        if self.scan is not None:
            result['Scan'] = self.scan
        if self.token_server is not None:
            result['TokenServer'] = self.token_server
        if self.vpn is not None:
            result['Vpn'] = self.vpn
        if self.work_mode is not None:
            result['WorkMode'] = self.work_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('Dai') is not None:
            self.dai = m.get('Dai')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EchoInt') is not None:
            self.echo_int = m.get('EchoInt')
        if m.get('Failover') is not None:
            self.failover = m.get('Failover')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('InsecureAllowed') is not None:
            self.insecure_allowed = m.get('InsecureAllowed')
        if m.get('IsConfigStrongConsistency') is not None:
            self.is_config_strong_consistency = m.get('IsConfigStrongConsistency')
        if m.get('LanIp') is not None:
            self.lan_ip = m.get('LanIp')
        if m.get('LanMask') is not None:
            self.lan_mask = m.get('LanMask')
        if m.get('LanStatus') is not None:
            self.lan_status = m.get('LanStatus')
        if m.get('LogIp') is not None:
            self.log_ip = m.get('LogIp')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ParentApgroupId') is not None:
            self.parent_apgroup_id = m.get('ParentApgroupId')
        if m.get('Passwd') is not None:
            self.passwd = m.get('Passwd')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('Route') is not None:
            self.route = m.get('Route')
        if m.get('Scan') is not None:
            self.scan = m.get('Scan')
        if m.get('TokenServer') is not None:
            self.token_server = m.get('TokenServer')
        if m.get('Vpn') is not None:
            self.vpn = m.get('Vpn')
        if m.get('WorkMode') is not None:
            self.work_mode = m.get('WorkMode')
        return self


class SaveApgroupBasicConfigResponseBodyData(TeaModel):
    def __init__(self, id=None, task_id=None):
        self.id = id  # type: long
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupBasicConfigResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SaveApgroupBasicConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: SaveApgroupBasicConfigResponseBodyData
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SaveApgroupBasicConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SaveApgroupBasicConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApgroupBasicConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApgroupBasicConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApgroupBasicConfigResponse, self).to_map()
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
            temp_model = SaveApgroupBasicConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApgroupPortalConfigRequest(TeaModel):
    def __init__(self, apgroup_id=None, app_auth_url=None, app_code=None, app_name=None, auth_key=None,
                 auth_secret=None, check_url=None, client_download=None, client_upload=None, countdown=None, network=None,
                 portal_types=None, portal_url=None, time_stamp=None, total_download=None, total_upload=None, web_auth_url=None,
                 whitelist=None):
        self.apgroup_id = apgroup_id  # type: long
        self.app_auth_url = app_auth_url  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.auth_key = auth_key  # type: str
        self.auth_secret = auth_secret  # type: str
        self.check_url = check_url  # type: str
        self.client_download = client_download  # type: int
        self.client_upload = client_upload  # type: int
        self.countdown = countdown  # type: int
        self.network = network  # type: int
        self.portal_types = portal_types  # type: list[str]
        self.portal_url = portal_url  # type: str
        self.time_stamp = time_stamp  # type: long
        self.total_download = total_download  # type: int
        self.total_upload = total_upload  # type: int
        self.web_auth_url = web_auth_url  # type: str
        self.whitelist = whitelist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupPortalConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types is not None:
            result['PortalTypes'] = self.portal_types
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApgroupPortalConfigShrinkRequest(TeaModel):
    def __init__(self, apgroup_id=None, app_auth_url=None, app_code=None, app_name=None, auth_key=None,
                 auth_secret=None, check_url=None, client_download=None, client_upload=None, countdown=None, network=None,
                 portal_types_shrink=None, portal_url=None, time_stamp=None, total_download=None, total_upload=None, web_auth_url=None,
                 whitelist=None):
        self.apgroup_id = apgroup_id  # type: long
        self.app_auth_url = app_auth_url  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.auth_key = auth_key  # type: str
        self.auth_secret = auth_secret  # type: str
        self.check_url = check_url  # type: str
        self.client_download = client_download  # type: int
        self.client_upload = client_upload  # type: int
        self.countdown = countdown  # type: int
        self.network = network  # type: int
        self.portal_types_shrink = portal_types_shrink  # type: str
        self.portal_url = portal_url  # type: str
        self.time_stamp = time_stamp  # type: long
        self.total_download = total_download  # type: int
        self.total_upload = total_upload  # type: int
        self.web_auth_url = web_auth_url  # type: str
        self.whitelist = whitelist  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupPortalConfigShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_auth_url is not None:
            result['AppAuthUrl'] = self.app_auth_url
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.check_url is not None:
            result['CheckUrl'] = self.check_url
        if self.client_download is not None:
            result['ClientDownload'] = self.client_download
        if self.client_upload is not None:
            result['ClientUpload'] = self.client_upload
        if self.countdown is not None:
            result['Countdown'] = self.countdown
        if self.network is not None:
            result['Network'] = self.network
        if self.portal_types_shrink is not None:
            result['PortalTypes'] = self.portal_types_shrink
        if self.portal_url is not None:
            result['PortalUrl'] = self.portal_url
        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp
        if self.total_download is not None:
            result['TotalDownload'] = self.total_download
        if self.total_upload is not None:
            result['TotalUpload'] = self.total_upload
        if self.web_auth_url is not None:
            result['WebAuthUrl'] = self.web_auth_url
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppAuthUrl') is not None:
            self.app_auth_url = m.get('AppAuthUrl')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('CheckUrl') is not None:
            self.check_url = m.get('CheckUrl')
        if m.get('ClientDownload') is not None:
            self.client_download = m.get('ClientDownload')
        if m.get('ClientUpload') is not None:
            self.client_upload = m.get('ClientUpload')
        if m.get('Countdown') is not None:
            self.countdown = m.get('Countdown')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('PortalTypes') is not None:
            self.portal_types_shrink = m.get('PortalTypes')
        if m.get('PortalUrl') is not None:
            self.portal_url = m.get('PortalUrl')
        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')
        if m.get('TotalDownload') is not None:
            self.total_download = m.get('TotalDownload')
        if m.get('TotalUpload') is not None:
            self.total_upload = m.get('TotalUpload')
        if m.get('WebAuthUrl') is not None:
            self.web_auth_url = m.get('WebAuthUrl')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class SaveApgroupPortalConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: list[long]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupPortalConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SaveApgroupPortalConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApgroupPortalConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApgroupPortalConfigResponse, self).to_map()
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
            temp_model = SaveApgroupPortalConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveApgroupSsidConfigRequest(TeaModel):
    def __init__(self, acct_port=None, acct_secret=None, acct_server=None, apgroup_id=None, app_code=None,
                 app_name=None, auth_cache=None, auth_port=None, auth_secret=None, auth_server=None, binding=None, cir=None,
                 dae_client=None, dae_port=None, dae_secret=None, disabled=None, disassoc_low_ack=None,
                 disassoc_weak_rssi=None, dynamic_vlan=None, effect=None, enc_key=None, encryption=None, hidden=None, id=None,
                 ieee_80211w=None, ignore_weak_probe=None, isolate=None, lite_effect=None, max_inactivity=None, maxassoc=None,
                 multicast_forward=None, nasid=None, network=None, new_ssid=None, ownip=None, secondary_acct_port=None,
                 secondary_acct_secret=None, secondary_acct_server=None, secondary_auth_port=None, secondary_auth_secret=None,
                 secondary_auth_server=None, short_preamble=None, ssid=None, ssid_lb=None, type=None, vlan_dhcp=None, wmm=None):
        self.acct_port = acct_port  # type: int
        self.acct_secret = acct_secret  # type: str
        self.acct_server = acct_server  # type: str
        self.apgroup_id = apgroup_id  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.auth_cache = auth_cache  # type: str
        self.auth_port = auth_port  # type: int
        self.auth_secret = auth_secret  # type: str
        self.auth_server = auth_server  # type: str
        self.binding = binding  # type: str
        self.cir = cir  # type: long
        self.dae_client = dae_client  # type: str
        self.dae_port = dae_port  # type: int
        self.dae_secret = dae_secret  # type: str
        self.disabled = disabled  # type: str
        self.disassoc_low_ack = disassoc_low_ack  # type: str
        self.disassoc_weak_rssi = disassoc_weak_rssi  # type: int
        self.dynamic_vlan = dynamic_vlan  # type: int
        self.effect = effect  # type: bool
        self.enc_key = enc_key  # type: str
        self.encryption = encryption  # type: str
        self.hidden = hidden  # type: str
        self.id = id  # type: long
        self.ieee_80211w = ieee_80211w  # type: str
        self.ignore_weak_probe = ignore_weak_probe  # type: int
        self.isolate = isolate  # type: str
        self.lite_effect = lite_effect  # type: bool
        self.max_inactivity = max_inactivity  # type: int
        self.maxassoc = maxassoc  # type: str
        self.multicast_forward = multicast_forward  # type: int
        self.nasid = nasid  # type: str
        self.network = network  # type: int
        self.new_ssid = new_ssid  # type: str
        self.ownip = ownip  # type: str
        self.secondary_acct_port = secondary_acct_port  # type: int
        self.secondary_acct_secret = secondary_acct_secret  # type: str
        self.secondary_acct_server = secondary_acct_server  # type: str
        self.secondary_auth_port = secondary_auth_port  # type: int
        self.secondary_auth_secret = secondary_auth_secret  # type: str
        self.secondary_auth_server = secondary_auth_server  # type: str
        self.short_preamble = short_preamble  # type: str
        self.ssid = ssid  # type: str
        self.ssid_lb = ssid_lb  # type: int
        self.type = type  # type: int
        self.vlan_dhcp = vlan_dhcp  # type: int
        self.wmm = wmm  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupSsidConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acct_port is not None:
            result['AcctPort'] = self.acct_port
        if self.acct_secret is not None:
            result['AcctSecret'] = self.acct_secret
        if self.acct_server is not None:
            result['AcctServer'] = self.acct_server
        if self.apgroup_id is not None:
            result['ApgroupId'] = self.apgroup_id
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.auth_cache is not None:
            result['AuthCache'] = self.auth_cache
        if self.auth_port is not None:
            result['AuthPort'] = self.auth_port
        if self.auth_secret is not None:
            result['AuthSecret'] = self.auth_secret
        if self.auth_server is not None:
            result['AuthServer'] = self.auth_server
        if self.binding is not None:
            result['Binding'] = self.binding
        if self.cir is not None:
            result['Cir'] = self.cir
        if self.dae_client is not None:
            result['DaeClient'] = self.dae_client
        if self.dae_port is not None:
            result['DaePort'] = self.dae_port
        if self.dae_secret is not None:
            result['DaeSecret'] = self.dae_secret
        if self.disabled is not None:
            result['Disabled'] = self.disabled
        if self.disassoc_low_ack is not None:
            result['DisassocLowAck'] = self.disassoc_low_ack
        if self.disassoc_weak_rssi is not None:
            result['DisassocWeakRssi'] = self.disassoc_weak_rssi
        if self.dynamic_vlan is not None:
            result['DynamicVlan'] = self.dynamic_vlan
        if self.effect is not None:
            result['Effect'] = self.effect
        if self.enc_key is not None:
            result['EncKey'] = self.enc_key
        if self.encryption is not None:
            result['Encryption'] = self.encryption
        if self.hidden is not None:
            result['Hidden'] = self.hidden
        if self.id is not None:
            result['Id'] = self.id
        if self.ieee_80211w is not None:
            result['Ieee80211w'] = self.ieee_80211w
        if self.ignore_weak_probe is not None:
            result['IgnoreWeakProbe'] = self.ignore_weak_probe
        if self.isolate is not None:
            result['Isolate'] = self.isolate
        if self.lite_effect is not None:
            result['LiteEffect'] = self.lite_effect
        if self.max_inactivity is not None:
            result['MaxInactivity'] = self.max_inactivity
        if self.maxassoc is not None:
            result['Maxassoc'] = self.maxassoc
        if self.multicast_forward is not None:
            result['MulticastForward'] = self.multicast_forward
        if self.nasid is not None:
            result['Nasid'] = self.nasid
        if self.network is not None:
            result['Network'] = self.network
        if self.new_ssid is not None:
            result['NewSsid'] = self.new_ssid
        if self.ownip is not None:
            result['Ownip'] = self.ownip
        if self.secondary_acct_port is not None:
            result['SecondaryAcctPort'] = self.secondary_acct_port
        if self.secondary_acct_secret is not None:
            result['SecondaryAcctSecret'] = self.secondary_acct_secret
        if self.secondary_acct_server is not None:
            result['SecondaryAcctServer'] = self.secondary_acct_server
        if self.secondary_auth_port is not None:
            result['SecondaryAuthPort'] = self.secondary_auth_port
        if self.secondary_auth_secret is not None:
            result['SecondaryAuthSecret'] = self.secondary_auth_secret
        if self.secondary_auth_server is not None:
            result['SecondaryAuthServer'] = self.secondary_auth_server
        if self.short_preamble is not None:
            result['ShortPreamble'] = self.short_preamble
        if self.ssid is not None:
            result['Ssid'] = self.ssid
        if self.ssid_lb is not None:
            result['SsidLb'] = self.ssid_lb
        if self.type is not None:
            result['Type'] = self.type
        if self.vlan_dhcp is not None:
            result['VlanDhcp'] = self.vlan_dhcp
        if self.wmm is not None:
            result['Wmm'] = self.wmm
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcctPort') is not None:
            self.acct_port = m.get('AcctPort')
        if m.get('AcctSecret') is not None:
            self.acct_secret = m.get('AcctSecret')
        if m.get('AcctServer') is not None:
            self.acct_server = m.get('AcctServer')
        if m.get('ApgroupId') is not None:
            self.apgroup_id = m.get('ApgroupId')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AuthCache') is not None:
            self.auth_cache = m.get('AuthCache')
        if m.get('AuthPort') is not None:
            self.auth_port = m.get('AuthPort')
        if m.get('AuthSecret') is not None:
            self.auth_secret = m.get('AuthSecret')
        if m.get('AuthServer') is not None:
            self.auth_server = m.get('AuthServer')
        if m.get('Binding') is not None:
            self.binding = m.get('Binding')
        if m.get('Cir') is not None:
            self.cir = m.get('Cir')
        if m.get('DaeClient') is not None:
            self.dae_client = m.get('DaeClient')
        if m.get('DaePort') is not None:
            self.dae_port = m.get('DaePort')
        if m.get('DaeSecret') is not None:
            self.dae_secret = m.get('DaeSecret')
        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')
        if m.get('DisassocLowAck') is not None:
            self.disassoc_low_ack = m.get('DisassocLowAck')
        if m.get('DisassocWeakRssi') is not None:
            self.disassoc_weak_rssi = m.get('DisassocWeakRssi')
        if m.get('DynamicVlan') is not None:
            self.dynamic_vlan = m.get('DynamicVlan')
        if m.get('Effect') is not None:
            self.effect = m.get('Effect')
        if m.get('EncKey') is not None:
            self.enc_key = m.get('EncKey')
        if m.get('Encryption') is not None:
            self.encryption = m.get('Encryption')
        if m.get('Hidden') is not None:
            self.hidden = m.get('Hidden')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Ieee80211w') is not None:
            self.ieee_80211w = m.get('Ieee80211w')
        if m.get('IgnoreWeakProbe') is not None:
            self.ignore_weak_probe = m.get('IgnoreWeakProbe')
        if m.get('Isolate') is not None:
            self.isolate = m.get('Isolate')
        if m.get('LiteEffect') is not None:
            self.lite_effect = m.get('LiteEffect')
        if m.get('MaxInactivity') is not None:
            self.max_inactivity = m.get('MaxInactivity')
        if m.get('Maxassoc') is not None:
            self.maxassoc = m.get('Maxassoc')
        if m.get('MulticastForward') is not None:
            self.multicast_forward = m.get('MulticastForward')
        if m.get('Nasid') is not None:
            self.nasid = m.get('Nasid')
        if m.get('Network') is not None:
            self.network = m.get('Network')
        if m.get('NewSsid') is not None:
            self.new_ssid = m.get('NewSsid')
        if m.get('Ownip') is not None:
            self.ownip = m.get('Ownip')
        if m.get('SecondaryAcctPort') is not None:
            self.secondary_acct_port = m.get('SecondaryAcctPort')
        if m.get('SecondaryAcctSecret') is not None:
            self.secondary_acct_secret = m.get('SecondaryAcctSecret')
        if m.get('SecondaryAcctServer') is not None:
            self.secondary_acct_server = m.get('SecondaryAcctServer')
        if m.get('SecondaryAuthPort') is not None:
            self.secondary_auth_port = m.get('SecondaryAuthPort')
        if m.get('SecondaryAuthSecret') is not None:
            self.secondary_auth_secret = m.get('SecondaryAuthSecret')
        if m.get('SecondaryAuthServer') is not None:
            self.secondary_auth_server = m.get('SecondaryAuthServer')
        if m.get('ShortPreamble') is not None:
            self.short_preamble = m.get('ShortPreamble')
        if m.get('Ssid') is not None:
            self.ssid = m.get('Ssid')
        if m.get('SsidLb') is not None:
            self.ssid_lb = m.get('SsidLb')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VlanDhcp') is not None:
            self.vlan_dhcp = m.get('VlanDhcp')
        if m.get('Wmm') is not None:
            self.wmm = m.get('Wmm')
        return self


class SaveApgroupSsidConfigResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: list[long]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SaveApgroupSsidConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SaveApgroupSsidConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SaveApgroupSsidConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SaveApgroupSsidConfigResponse, self).to_map()
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
            temp_model = SaveApgroupSsidConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApAddressRequest(TeaModel):
    def __init__(self, ap_area_name=None, ap_building_name=None, ap_campus_name=None, ap_city_name=None,
                 ap_floor=None, ap_group=None, ap_name=None, ap_nation_name=None, ap_province_name=None, ap_unit_id=None,
                 ap_unit_name=None, app_code=None, app_name=None, direction=None, language=None, lat=None, lng=None, mac=None):
        self.ap_area_name = ap_area_name  # type: str
        self.ap_building_name = ap_building_name  # type: str
        self.ap_campus_name = ap_campus_name  # type: str
        self.ap_city_name = ap_city_name  # type: str
        self.ap_floor = ap_floor  # type: str
        self.ap_group = ap_group  # type: str
        self.ap_name = ap_name  # type: str
        self.ap_nation_name = ap_nation_name  # type: str
        self.ap_province_name = ap_province_name  # type: str
        self.ap_unit_id = ap_unit_id  # type: long
        self.ap_unit_name = ap_unit_name  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.direction = direction  # type: str
        self.language = language  # type: str
        self.lat = lat  # type: str
        self.lng = lng  # type: str
        self.mac = mac  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApAddressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_area_name is not None:
            result['ApAreaName'] = self.ap_area_name
        if self.ap_building_name is not None:
            result['ApBuildingName'] = self.ap_building_name
        if self.ap_campus_name is not None:
            result['ApCampusName'] = self.ap_campus_name
        if self.ap_city_name is not None:
            result['ApCityName'] = self.ap_city_name
        if self.ap_floor is not None:
            result['ApFloor'] = self.ap_floor
        if self.ap_group is not None:
            result['ApGroup'] = self.ap_group
        if self.ap_name is not None:
            result['ApName'] = self.ap_name
        if self.ap_nation_name is not None:
            result['ApNationName'] = self.ap_nation_name
        if self.ap_province_name is not None:
            result['ApProvinceName'] = self.ap_province_name
        if self.ap_unit_id is not None:
            result['ApUnitId'] = self.ap_unit_id
        if self.ap_unit_name is not None:
            result['ApUnitName'] = self.ap_unit_name
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.direction is not None:
            result['Direction'] = self.direction
        if self.language is not None:
            result['Language'] = self.language
        if self.lat is not None:
            result['Lat'] = self.lat
        if self.lng is not None:
            result['Lng'] = self.lng
        if self.mac is not None:
            result['Mac'] = self.mac
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApAreaName') is not None:
            self.ap_area_name = m.get('ApAreaName')
        if m.get('ApBuildingName') is not None:
            self.ap_building_name = m.get('ApBuildingName')
        if m.get('ApCampusName') is not None:
            self.ap_campus_name = m.get('ApCampusName')
        if m.get('ApCityName') is not None:
            self.ap_city_name = m.get('ApCityName')
        if m.get('ApFloor') is not None:
            self.ap_floor = m.get('ApFloor')
        if m.get('ApGroup') is not None:
            self.ap_group = m.get('ApGroup')
        if m.get('ApName') is not None:
            self.ap_name = m.get('ApName')
        if m.get('ApNationName') is not None:
            self.ap_nation_name = m.get('ApNationName')
        if m.get('ApProvinceName') is not None:
            self.ap_province_name = m.get('ApProvinceName')
        if m.get('ApUnitId') is not None:
            self.ap_unit_id = m.get('ApUnitId')
        if m.get('ApUnitName') is not None:
            self.ap_unit_name = m.get('ApUnitName')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Lat') is not None:
            self.lat = m.get('Lat')
        if m.get('Lng') is not None:
            self.lng = m.get('Lng')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        return self


class SetApAddressResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApAddressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SetApAddressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApAddressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApAddressResponse, self).to_map()
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
            temp_model = SetApAddressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetApNameRequest(TeaModel):
    def __init__(self, ap_mac=None, app_code=None, app_name=None, name=None):
        self.ap_mac = ap_mac  # type: str
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ap_mac is not None:
            result['ApMac'] = self.ap_mac
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApMac') is not None:
            self.ap_mac = m.get('ApMac')
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class SetApNameResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None):
        self.data = data  # type: str
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetApNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class SetApNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetApNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetApNameResponse, self).to_map()
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
            temp_model = SetApNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnRegisterApAssetRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, asset_apgroup_id=None, category=None, id=None, mac=None,
                 serial_no=None, use_for=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.asset_apgroup_id = asset_apgroup_id  # type: long
        self.category = category  # type: int
        self.id = id  # type: long
        self.mac = mac  # type: str
        self.serial_no = serial_no  # type: str
        self.use_for = use_for  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnRegisterApAssetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.asset_apgroup_id is not None:
            result['AssetApgroupId'] = self.asset_apgroup_id
        if self.category is not None:
            result['Category'] = self.category
        if self.id is not None:
            result['Id'] = self.id
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.serial_no is not None:
            result['SerialNo'] = self.serial_no
        if self.use_for is not None:
            result['UseFor'] = self.use_for
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AssetApgroupId') is not None:
            self.asset_apgroup_id = m.get('AssetApgroupId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('SerialNo') is not None:
            self.serial_no = m.get('SerialNo')
        if m.get('UseFor') is not None:
            self.use_for = m.get('UseFor')
        return self


class UnRegisterApAssetResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: dict[str, any]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnRegisterApAssetResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnRegisterApAssetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnRegisterApAssetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnRegisterApAssetResponse, self).to_map()
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
            temp_model = UnRegisterApAssetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNetDeviceInfoRequestDevices(TeaModel):
    def __init__(self, host_name=None, id=None, idc=None, logic_net_pod=None, manufacturer=None, mgn_ip=None,
                 model=None, net_pod=None, password=None, role=None, service_tag=None, username=None):
        self.host_name = host_name  # type: str
        self.id = id  # type: long
        self.idc = idc  # type: str
        self.logic_net_pod = logic_net_pod  # type: str
        self.manufacturer = manufacturer  # type: str
        self.mgn_ip = mgn_ip  # type: str
        self.model = model  # type: str
        self.net_pod = net_pod  # type: str
        self.password = password  # type: str
        self.role = role  # type: str
        self.service_tag = service_tag  # type: str
        self.username = username  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNetDeviceInfoRequestDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.id is not None:
            result['Id'] = self.id
        if self.idc is not None:
            result['Idc'] = self.idc
        if self.logic_net_pod is not None:
            result['LogicNetPod'] = self.logic_net_pod
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.mgn_ip is not None:
            result['MgnIp'] = self.mgn_ip
        if self.model is not None:
            result['Model'] = self.model
        if self.net_pod is not None:
            result['NetPod'] = self.net_pod
        if self.password is not None:
            result['Password'] = self.password
        if self.role is not None:
            result['Role'] = self.role
        if self.service_tag is not None:
            result['ServiceTag'] = self.service_tag
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Idc') is not None:
            self.idc = m.get('Idc')
        if m.get('LogicNetPod') is not None:
            self.logic_net_pod = m.get('LogicNetPod')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('MgnIp') is not None:
            self.mgn_ip = m.get('MgnIp')
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('NetPod') is not None:
            self.net_pod = m.get('NetPod')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ServiceTag') is not None:
            self.service_tag = m.get('ServiceTag')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class UpdateNetDeviceInfoRequest(TeaModel):
    def __init__(self, app_code=None, app_name=None, devices=None, request_id=None):
        self.app_code = app_code  # type: str
        self.app_name = app_name  # type: str
        self.devices = devices  # type: list[UpdateNetDeviceInfoRequestDevices]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.devices:
            for k in self.devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateNetDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_code is not None:
            result['AppCode'] = self.app_code
        if self.app_name is not None:
            result['AppName'] = self.app_name
        result['Devices'] = []
        if self.devices is not None:
            for k in self.devices:
                result['Devices'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        self.devices = []
        if m.get('Devices') is not None:
            for k in m.get('Devices'):
                temp_model = UpdateNetDeviceInfoRequestDevices()
                self.devices.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNetDeviceInfoResponseBody(TeaModel):
    def __init__(self, data=None, error_code=None, error_message=None, is_success=None, request_id=None):
        self.data = data  # type: list[long]
        self.error_code = error_code  # type: int
        self.error_message = error_message  # type: str
        self.is_success = is_success  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateNetDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNetDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateNetDeviceInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateNetDeviceInfoResponse, self).to_map()
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
            temp_model = UpdateNetDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


