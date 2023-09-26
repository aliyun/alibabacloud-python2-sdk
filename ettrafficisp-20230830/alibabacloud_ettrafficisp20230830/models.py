# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AkDisableRequest(TeaModel):
    def __init__(self, access_key_id=None, access_key_name=None, permissions=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_name = access_key_name  # type: str
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkDisableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_name is not None:
            result['accessKeyName'] = self.access_key_name
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeyName') is not None:
            self.access_key_name = m.get('accessKeyName')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class AkDisableResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkDisableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AkDisableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AkDisableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AkDisableResponse, self).to_map()
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
            temp_model = AkDisableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AkEnableRequest(TeaModel):
    def __init__(self, access_key_id=None, access_key_name=None, permissions=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_name = access_key_name  # type: str
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkEnableRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_name is not None:
            result['accessKeyName'] = self.access_key_name
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeyName') is not None:
            self.access_key_name = m.get('accessKeyName')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class AkEnableResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkEnableResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AkEnableResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AkEnableResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AkEnableResponse, self).to_map()
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
            temp_model = AkEnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AkGenerateRequest(TeaModel):
    def __init__(self, access_key_name=None, permissions=None, user_id=None):
        self.access_key_name = access_key_name  # type: str
        self.permissions = permissions  # type: list[str]
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkGenerateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_name is not None:
            result['accessKeyName'] = self.access_key_name
        if self.permissions is not None:
            result['permissions'] = self.permissions
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyName') is not None:
            self.access_key_name = m.get('accessKeyName')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AkGenerateResponseBodyData(TeaModel):
    def __init__(self, access_key_id=None, access_key_name=None, access_key_secret=None, user_id=None):
        # Access Key ID
        self.access_key_id = access_key_id  # type: str
        self.access_key_name = access_key_name  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkGenerateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_name is not None:
            result['accessKeyName'] = self.access_key_name
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeyName') is not None:
            self.access_key_name = m.get('accessKeyName')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class AkGenerateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AkGenerateResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AkGenerateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AkGenerateResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AkGenerateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AkGenerateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AkGenerateResponse, self).to_map()
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
            temp_model = AkGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AkListPageRequest(TeaModel):
    def __init__(self, page=None, size=None, start=None):
        self.page = page  # type: int
        self.size = size  # type: int
        self.start = start  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkListPageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class AkListPageResponseBodyDataDataListPermissions(TeaModel):
    def __init__(self, auth_time=None, description=None, group=None, permission_code=None, permission_name=None):
        self.auth_time = auth_time  # type: str
        self.description = description  # type: str
        self.group = group  # type: str
        self.permission_code = permission_code  # type: str
        self.permission_name = permission_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkListPageResponseBodyDataDataListPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_time is not None:
            result['authTime'] = self.auth_time
        if self.description is not None:
            result['description'] = self.description
        if self.group is not None:
            result['group'] = self.group
        if self.permission_code is not None:
            result['permissionCode'] = self.permission_code
        if self.permission_name is not None:
            result['permissionName'] = self.permission_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('authTime') is not None:
            self.auth_time = m.get('authTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('permissionCode') is not None:
            self.permission_code = m.get('permissionCode')
        if m.get('permissionName') is not None:
            self.permission_name = m.get('permissionName')
        return self


class AkListPageResponseBodyDataDataList(TeaModel):
    def __init__(self, access_key_id=None, access_key_name=None, access_key_secret=None, active=None,
                 gmt_create=None, gmt_modify=None, last_call_time=None, permissions=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_name = access_key_name  # type: str
        self.access_key_secret = access_key_secret  # type: str
        self.active = active  # type: int
        self.gmt_create = gmt_create  # type: str
        self.gmt_modify = gmt_modify  # type: str
        self.last_call_time = last_call_time  # type: str
        self.permissions = permissions  # type: list[AkListPageResponseBodyDataDataListPermissions]

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AkListPageResponseBodyDataDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_name is not None:
            result['accessKeyName'] = self.access_key_name
        if self.access_key_secret is not None:
            result['accessKeySecret'] = self.access_key_secret
        if self.active is not None:
            result['active'] = self.active
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modify is not None:
            result['gmtModify'] = self.gmt_modify
        if self.last_call_time is not None:
            result['lastCallTime'] = self.last_call_time
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeyName') is not None:
            self.access_key_name = m.get('accessKeyName')
        if m.get('accessKeySecret') is not None:
            self.access_key_secret = m.get('accessKeySecret')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModify') is not None:
            self.gmt_modify = m.get('gmtModify')
        if m.get('lastCallTime') is not None:
            self.last_call_time = m.get('lastCallTime')
        self.permissions = []
        if m.get('permissions') is not None:
            for k in m.get('permissions'):
                temp_model = AkListPageResponseBodyDataDataListPermissions()
                self.permissions.append(temp_model.from_map(k))
        return self


class AkListPageResponseBodyData(TeaModel):
    def __init__(self, count=None, current_page=None, data_list=None, total_page=None):
        self.count = count  # type: int
        self.current_page = current_page  # type: int
        self.data_list = data_list  # type: list[AkListPageResponseBodyDataDataList]
        self.total_page = total_page  # type: int

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AkListPageResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.current_page is not None:
            result['currentPage'] = self.current_page
        result['dataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['dataList'].append(k.to_map() if k else None)
        if self.total_page is not None:
            result['totalPage'] = self.total_page
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')
        self.data_list = []
        if m.get('dataList') is not None:
            for k in m.get('dataList'):
                temp_model = AkListPageResponseBodyDataDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')
        return self


class AkListPageResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: AkListPageResponseBodyData
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AkListPageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = AkListPageResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AkListPageResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AkListPageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AkListPageResponse, self).to_map()
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
            temp_model = AkListPageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AkUpdateRequest(TeaModel):
    def __init__(self, access_key_id=None, access_key_name=None, permissions=None):
        self.access_key_id = access_key_id  # type: str
        self.access_key_name = access_key_name  # type: str
        self.permissions = permissions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkUpdateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_key_id is not None:
            result['accessKeyId'] = self.access_key_id
        if self.access_key_name is not None:
            result['accessKeyName'] = self.access_key_name
        if self.permissions is not None:
            result['permissions'] = self.permissions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('accessKeyId') is not None:
            self.access_key_id = m.get('accessKeyId')
        if m.get('accessKeyName') is not None:
            self.access_key_name = m.get('accessKeyName')
        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')
        return self


class AkUpdateResponseBody(TeaModel):
    def __init__(self, code=None, message=None, request_id=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AkUpdateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AkUpdateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AkUpdateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AkUpdateResponse, self).to_map()
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
            temp_model = AkUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DimGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, message=None, request_id=None):
        self.code = code  # type: str
        self.data = data  # type: any
        self.message = message  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DimGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DimGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DimGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DimGroupResponse, self).to_map()
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
            temp_model = DimGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


