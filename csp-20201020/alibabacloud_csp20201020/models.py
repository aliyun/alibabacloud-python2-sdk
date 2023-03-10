# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddAclAuthorizationRequest(TeaModel):
    def __init__(self, acl_operation=None, client_token=None, pattern_type=None, resource_name=None,
                 resource_type=None):
        self.acl_operation = acl_operation  # type: str
        self.client_token = client_token  # type: str
        self.pattern_type = pattern_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAclAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation is not None:
            result['AclOperation'] = self.acl_operation
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperation') is not None:
            self.acl_operation = m.get('AclOperation')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class AddAclAuthorizationResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, http_status_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAclAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAclAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAclAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAclAuthorizationResponse, self).to_map()
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
            temp_model = AddAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddAuthenticatedUserRequest(TeaModel):
    def __init__(self, client_token=None, instance_id=None, password=None, user_name=None):
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAuthenticatedUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class AddAuthenticatedUserResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, http_status_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddAuthenticatedUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAuthenticatedUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddAuthenticatedUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddAuthenticatedUserResponse, self).to_map()
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
            temp_model = AddAuthenticatedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckClusterNameRequest(TeaModel):
    def __init__(self, cluster_name=None):
        self.cluster_name = cluster_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckClusterNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        return self


class CheckClusterNameResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckClusterNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckClusterNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckClusterNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckClusterNameResponse, self).to_map()
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
            temp_model = CheckClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckInventoryRequest(TeaModel):
    def __init__(self, cluster_info=None):
        self.cluster_info = cluster_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckInventoryRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        return self


class CheckInventoryResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckInventoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckInventoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckInventoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckInventoryResponse, self).to_map()
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
            temp_model = CheckInventoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckLeftCuRequest(TeaModel):
    def __init__(self, cu_num=None, region_id=None, zone_id=None):
        self.cu_num = cu_num  # type: int
        self.region_id = region_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckLeftCuRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckLeftCuResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckLeftCuResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckLeftCuResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckLeftCuResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckLeftCuResponse, self).to_map()
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
            temp_model = CheckLeftCuResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserAccountResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckUserAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckUserAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckUserAccountResponse, self).to_map()
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
            temp_model = CheckUserAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUserResourceRequest(TeaModel):
    def __init__(self, cluster_info=None, type=None):
        self.cluster_info = cluster_info  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserResourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckUserResourceResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUserResourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckUserResourceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckUserResourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckUserResourceResponse, self).to_map()
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
            temp_model = CheckUserResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckVpcRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None):
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVpcRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CheckVpcResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVpcResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckVpcResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckVpcResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckVpcResponse, self).to_map()
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
            temp_model = CheckVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckVswitchRequest(TeaModel):
    def __init__(self, region_id=None, v_switch_ids=None, vpc_id=None, zone_id=None):
        self.region_id = region_id  # type: str
        self.v_switch_ids = v_switch_ids  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVswitchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CheckVswitchResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckVswitchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckVswitchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckVswitchResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckVswitchResponse, self).to_map()
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
            temp_model = CheckVswitchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, client_token=None, cluster_info=None):
        self.client_token = client_token  # type: str
        self.cluster_info = cluster_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        return self


class CreateClusterResponseBodyData(TeaModel):
    def __init__(self, began_on=None, end_on=None, order_id=None):
        self.began_on = began_on  # type: long
        self.end_on = end_on  # type: long
        self.order_id = order_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.began_on is not None:
            result['BeganOn'] = self.began_on
        if self.end_on is not None:
            result['EndOn'] = self.end_on
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeganOn') is not None:
            self.began_on = m.get('BeganOn')
        if m.get('EndOn') is not None:
            self.end_on = m.get('EndOn')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: CreateClusterResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateClusterResponse, self).to_map()
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
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDefaultRoleRequest(TeaModel):
    def __init__(self, client_token=None):
        self.client_token = client_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefaultRoleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        return self


class CreateDefaultRoleResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDefaultRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDefaultRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDefaultRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDefaultRoleResponse, self).to_map()
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
            temp_model = CreateDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOrderRequest(TeaModel):
    def __init__(self, client_token=None, order_info=None):
        self.client_token = client_token  # type: str
        self.order_info = order_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.order_info is not None:
            result['OrderInfo'] = self.order_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OrderInfo') is not None:
            self.order_info = m.get('OrderInfo')
        return self


class CreateOrderResponseBodyData(TeaModel):
    def __init__(self, order_id=None):
        self.order_id = order_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateOrderResponseBodyData, self).to_map()
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


class CreateOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: CreateOrderResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = CreateOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateOrderResponse, self).to_map()
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAclAuthorizationRequest(TeaModel):
    def __init__(self, acl_operation=None, instance_id=None, pattern_type=None, resource_name=None,
                 resource_type=None):
        self.acl_operation = acl_operation  # type: str
        self.instance_id = instance_id  # type: str
        self.pattern_type = pattern_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation is not None:
            result['AclOperation'] = self.acl_operation
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperation') is not None:
            self.acl_operation = m.get('AclOperation')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DeleteAclAuthorizationResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, http_status_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAclAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAclAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAclAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAclAuthorizationResponse, self).to_map()
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
            temp_model = DeleteAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAuthenticatedUserRequest(TeaModel):
    def __init__(self, instance_id=None, password=None, user_name=None):
        self.instance_id = instance_id  # type: str
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthenticatedUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteAuthenticatedUserResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, http_status_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAuthenticatedUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteAuthenticatedUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAuthenticatedUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAuthenticatedUserResponse, self).to_map()
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
            temp_model = DeleteAuthenticatedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterDetailRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetClusterDetailResponseBodyDataClusterInfo(TeaModel):
    def __init__(self, bucket_name=None, connect_cpu=None, connect_enabled=None, connect_replica=None,
                 control_center_cpu=None, control_center_data_storage_integer=None, control_center_enabled=None,
                 control_center_replica=None, kafka_cpu=None, kafka_data_storage=None, kafka_replica=None, kafkarestproxy_enabled=None,
                 ksql_cpu=None, ksql_data_storage_integer=None, ksql_enabled=None, ksql_replica=None, rest_proxy_cpu=None,
                 rest_proxy_replica=None, schemaregistry_cpu=None, schemaregistry_enabled=None, schemaregistry_replica=None,
                 zookeeper_cpu=None, zookeeper_enabled=None, zookeeper_replica=None, zookeeper_storage_integer=None):
        self.bucket_name = bucket_name  # type: str
        self.connect_cpu = connect_cpu  # type: int
        self.connect_enabled = connect_enabled  # type: bool
        self.connect_replica = connect_replica  # type: int
        self.control_center_cpu = control_center_cpu  # type: int
        self.control_center_data_storage_integer = control_center_data_storage_integer  # type: int
        self.control_center_enabled = control_center_enabled  # type: bool
        self.control_center_replica = control_center_replica  # type: int
        self.kafka_cpu = kafka_cpu  # type: int
        self.kafka_data_storage = kafka_data_storage  # type: str
        self.kafka_replica = kafka_replica  # type: int
        self.kafkarestproxy_enabled = kafkarestproxy_enabled  # type: bool
        self.ksql_cpu = ksql_cpu  # type: int
        self.ksql_data_storage_integer = ksql_data_storage_integer  # type: int
        self.ksql_enabled = ksql_enabled  # type: bool
        self.ksql_replica = ksql_replica  # type: int
        self.rest_proxy_cpu = rest_proxy_cpu  # type: int
        self.rest_proxy_replica = rest_proxy_replica  # type: int
        self.schemaregistry_cpu = schemaregistry_cpu  # type: int
        self.schemaregistry_enabled = schemaregistry_enabled  # type: bool
        self.schemaregistry_replica = schemaregistry_replica  # type: int
        self.zookeeper_cpu = zookeeper_cpu  # type: int
        self.zookeeper_enabled = zookeeper_enabled  # type: bool
        self.zookeeper_replica = zookeeper_replica  # type: int
        self.zookeeper_storage_integer = zookeeper_storage_integer  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetClusterDetailResponseBodyDataClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.connect_cpu is not None:
            result['ConnectCpu'] = self.connect_cpu
        if self.connect_enabled is not None:
            result['ConnectEnabled'] = self.connect_enabled
        if self.connect_replica is not None:
            result['ConnectReplica'] = self.connect_replica
        if self.control_center_cpu is not None:
            result['ControlCenterCpu'] = self.control_center_cpu
        if self.control_center_data_storage_integer is not None:
            result['ControlCenterDataStorageInteger'] = self.control_center_data_storage_integer
        if self.control_center_enabled is not None:
            result['ControlCenterEnabled'] = self.control_center_enabled
        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica
        if self.kafka_cpu is not None:
            result['KafkaCpu'] = self.kafka_cpu
        if self.kafka_data_storage is not None:
            result['KafkaDataStorage'] = self.kafka_data_storage
        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica
        if self.kafkarestproxy_enabled is not None:
            result['KafkarestproxyEnabled'] = self.kafkarestproxy_enabled
        if self.ksql_cpu is not None:
            result['KsqlCpu'] = self.ksql_cpu
        if self.ksql_data_storage_integer is not None:
            result['KsqlDataStorageInteger'] = self.ksql_data_storage_integer
        if self.ksql_enabled is not None:
            result['KsqlEnabled'] = self.ksql_enabled
        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica
        if self.rest_proxy_cpu is not None:
            result['RestProxyCpu'] = self.rest_proxy_cpu
        if self.rest_proxy_replica is not None:
            result['RestProxyReplica'] = self.rest_proxy_replica
        if self.schemaregistry_cpu is not None:
            result['SchemaregistryCpu'] = self.schemaregistry_cpu
        if self.schemaregistry_enabled is not None:
            result['SchemaregistryEnabled'] = self.schemaregistry_enabled
        if self.schemaregistry_replica is not None:
            result['SchemaregistryReplica'] = self.schemaregistry_replica
        if self.zookeeper_cpu is not None:
            result['ZookeeperCpu'] = self.zookeeper_cpu
        if self.zookeeper_enabled is not None:
            result['ZookeeperEnabled'] = self.zookeeper_enabled
        if self.zookeeper_replica is not None:
            result['ZookeeperReplica'] = self.zookeeper_replica
        if self.zookeeper_storage_integer is not None:
            result['ZookeeperStorageInteger'] = self.zookeeper_storage_integer
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('ConnectCpu') is not None:
            self.connect_cpu = m.get('ConnectCpu')
        if m.get('ConnectEnabled') is not None:
            self.connect_enabled = m.get('ConnectEnabled')
        if m.get('ConnectReplica') is not None:
            self.connect_replica = m.get('ConnectReplica')
        if m.get('ControlCenterCpu') is not None:
            self.control_center_cpu = m.get('ControlCenterCpu')
        if m.get('ControlCenterDataStorageInteger') is not None:
            self.control_center_data_storage_integer = m.get('ControlCenterDataStorageInteger')
        if m.get('ControlCenterEnabled') is not None:
            self.control_center_enabled = m.get('ControlCenterEnabled')
        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')
        if m.get('KafkaCpu') is not None:
            self.kafka_cpu = m.get('KafkaCpu')
        if m.get('KafkaDataStorage') is not None:
            self.kafka_data_storage = m.get('KafkaDataStorage')
        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')
        if m.get('KafkarestproxyEnabled') is not None:
            self.kafkarestproxy_enabled = m.get('KafkarestproxyEnabled')
        if m.get('KsqlCpu') is not None:
            self.ksql_cpu = m.get('KsqlCpu')
        if m.get('KsqlDataStorageInteger') is not None:
            self.ksql_data_storage_integer = m.get('KsqlDataStorageInteger')
        if m.get('KsqlEnabled') is not None:
            self.ksql_enabled = m.get('KsqlEnabled')
        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')
        if m.get('RestProxyCpu') is not None:
            self.rest_proxy_cpu = m.get('RestProxyCpu')
        if m.get('RestProxyReplica') is not None:
            self.rest_proxy_replica = m.get('RestProxyReplica')
        if m.get('SchemaregistryCpu') is not None:
            self.schemaregistry_cpu = m.get('SchemaregistryCpu')
        if m.get('SchemaregistryEnabled') is not None:
            self.schemaregistry_enabled = m.get('SchemaregistryEnabled')
        if m.get('SchemaregistryReplica') is not None:
            self.schemaregistry_replica = m.get('SchemaregistryReplica')
        if m.get('ZookeeperCpu') is not None:
            self.zookeeper_cpu = m.get('ZookeeperCpu')
        if m.get('ZookeeperEnabled') is not None:
            self.zookeeper_enabled = m.get('ZookeeperEnabled')
        if m.get('ZookeeperReplica') is not None:
            self.zookeeper_replica = m.get('ZookeeperReplica')
        if m.get('ZookeeperStorageInteger') is not None:
            self.zookeeper_storage_integer = m.get('ZookeeperStorageInteger')
        return self


class GetClusterDetailResponseBodyData(TeaModel):
    def __init__(self, ask_cluster_id=None, auto_renew=None, begin_time=None, cluster_biz_id=None, cluster_id=None,
                 cluster_info=None, cluster_name=None, cluster_status=None, cluster_status_value=None, connector_visible=None,
                 control_center_url=None, duration=None, expire_time=None, gmt_create=None, gmt_modified=None, order_biz_id=None,
                 package_type=None, pricing_cycle=None, public_server_cert=None, region_id=None, running_time=None,
                 server_cert=None, storage_size=None, template_version=None, tiered_storage_visible=None, zone_id=None):
        self.ask_cluster_id = ask_cluster_id  # type: str
        self.auto_renew = auto_renew  # type: bool
        self.begin_time = begin_time  # type: long
        self.cluster_biz_id = cluster_biz_id  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_info = cluster_info  # type: GetClusterDetailResponseBodyDataClusterInfo
        self.cluster_name = cluster_name  # type: str
        self.cluster_status = cluster_status  # type: str
        self.cluster_status_value = cluster_status_value  # type: int
        self.connector_visible = connector_visible  # type: bool
        self.control_center_url = control_center_url  # type: str
        self.duration = duration  # type: int
        self.expire_time = expire_time  # type: long
        self.gmt_create = gmt_create  # type: long
        self.gmt_modified = gmt_modified  # type: long
        self.order_biz_id = order_biz_id  # type: str
        self.package_type = package_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.public_server_cert = public_server_cert  # type: str
        self.region_id = region_id  # type: str
        self.running_time = running_time  # type: long
        self.server_cert = server_cert  # type: str
        self.storage_size = storage_size  # type: int
        self.template_version = template_version  # type: str
        self.tiered_storage_visible = tiered_storage_visible  # type: bool
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.cluster_info:
            self.cluster_info.validate()

    def to_map(self):
        _map = super(GetClusterDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ask_cluster_id is not None:
            result['AskClusterID'] = self.ask_cluster_id
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.connector_visible is not None:
            result['ConnectorVisible'] = self.connector_visible
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.public_server_cert is not None:
            result['PublicServerCert'] = self.public_server_cert
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.running_time is not None:
            result['RunningTime'] = self.running_time
        if self.server_cert is not None:
            result['ServerCert'] = self.server_cert
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.tiered_storage_visible is not None:
            result['TieredStorageVisible'] = self.tiered_storage_visible
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AskClusterID') is not None:
            self.ask_cluster_id = m.get('AskClusterID')
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInfo') is not None:
            temp_model = GetClusterDetailResponseBodyDataClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ConnectorVisible') is not None:
            self.connector_visible = m.get('ConnectorVisible')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('PublicServerCert') is not None:
            self.public_server_cert = m.get('PublicServerCert')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RunningTime') is not None:
            self.running_time = m.get('RunningTime')
        if m.get('ServerCert') is not None:
            self.server_cert = m.get('ServerCert')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('TieredStorageVisible') is not None:
            self.tiered_storage_visible = m.get('TieredStorageVisible')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetClusterDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: GetClusterDetailResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetClusterDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetClusterDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class GetClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetClusterDetailResponse, self).to_map()
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
            temp_model = GetClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConfigInfoResponseBodyDataSpecVersionInfosPricingInfos(TeaModel):
    def __init__(self, duration=None, pricing_cycle=None):
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetConfigInfoResponseBodyDataSpecVersionInfosPricingInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class GetConfigInfoResponseBodyDataSpecVersionInfos(TeaModel):
    def __init__(self, multi_azpermission=None, package_type=None, pricing_infos=None, spec_version=None,
                 spec_version_en=None, visible=None):
        self.multi_azpermission = multi_azpermission  # type: bool
        self.package_type = package_type  # type: str
        self.pricing_infos = pricing_infos  # type: list[GetConfigInfoResponseBodyDataSpecVersionInfosPricingInfos]
        self.spec_version = spec_version  # type: str
        self.spec_version_en = spec_version_en  # type: str
        self.visible = visible  # type: bool

    def validate(self):
        if self.pricing_infos:
            for k in self.pricing_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConfigInfoResponseBodyDataSpecVersionInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_azpermission is not None:
            result['MultiAZPermission'] = self.multi_azpermission
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        result['PricingInfos'] = []
        if self.pricing_infos is not None:
            for k in self.pricing_infos:
                result['PricingInfos'].append(k.to_map() if k else None)
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.spec_version_en is not None:
            result['SpecVersionEn'] = self.spec_version_en
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MultiAZPermission') is not None:
            self.multi_azpermission = m.get('MultiAZPermission')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        self.pricing_infos = []
        if m.get('PricingInfos') is not None:
            for k in m.get('PricingInfos'):
                temp_model = GetConfigInfoResponseBodyDataSpecVersionInfosPricingInfos()
                self.pricing_infos.append(temp_model.from_map(k))
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('SpecVersionEn') is not None:
            self.spec_version_en = m.get('SpecVersionEn')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class GetConfigInfoResponseBodyData(TeaModel):
    def __init__(self, product_code=None, spec_version_infos=None):
        self.product_code = product_code  # type: str
        self.spec_version_infos = spec_version_infos  # type: list[GetConfigInfoResponseBodyDataSpecVersionInfos]

    def validate(self):
        if self.spec_version_infos:
            for k in self.spec_version_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetConfigInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['SpecVersionInfos'] = []
        if self.spec_version_infos is not None:
            for k in self.spec_version_infos:
                result['SpecVersionInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.spec_version_infos = []
        if m.get('SpecVersionInfos') is not None:
            for k in m.get('SpecVersionInfos'):
                temp_model = GetConfigInfoResponseBodyDataSpecVersionInfos()
                self.spec_version_infos.append(temp_model.from_map(k))
        return self


class GetConfigInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: GetConfigInfoResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetConfigInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = GetConfigInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetConfigInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetConfigInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetConfigInfoResponse, self).to_map()
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
            temp_model = GetConfigInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCspConnectorDeployedListRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCspConnectorDeployedListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetCspConnectorDeployedListResponseBodyDataOwner(TeaModel):
    def __init__(self, logo=None, name=None, url=None, user_name=None):
        self.logo = logo  # type: str
        self.name = name  # type: str
        self.url = url  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCspConnectorDeployedListResponseBodyDataOwner, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetCspConnectorDeployedListResponseBodyData(TeaModel):
    def __init__(self, component_types=None, description=None, hub_url=None, last_modified=None, logo=None,
                 name=None, owner=None, title=None, version=None):
        self.component_types = component_types  # type: list[str]
        self.description = description  # type: str
        self.hub_url = hub_url  # type: str
        self.last_modified = last_modified  # type: long
        self.logo = logo  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: GetCspConnectorDeployedListResponseBodyDataOwner
        self.title = title  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super(GetCspConnectorDeployedListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_types is not None:
            result['ComponentTypes'] = self.component_types
        if self.description is not None:
            result['Description'] = self.description
        if self.hub_url is not None:
            result['HubUrl'] = self.hub_url
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentTypes') is not None:
            self.component_types = m.get('ComponentTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HubUrl') is not None:
            self.hub_url = m.get('HubUrl')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            temp_model = GetCspConnectorDeployedListResponseBodyDataOwner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetCspConnectorDeployedListResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[GetCspConnectorDeployedListResponseBodyData]
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCspConnectorDeployedListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = GetCspConnectorDeployedListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCspConnectorDeployedListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCspConnectorDeployedListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCspConnectorDeployedListResponse, self).to_map()
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
            temp_model = GetCspConnectorDeployedListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCspSpecificationInfoResponseBodyDataConfiguration(TeaModel):
    def __init__(self, component_format_name=None, component_name=None, default_cu_num=None, default_replica=None,
                 default_storage=None, max_cu_num=None, max_replica=None, max_storage=None, min_cu_num=None, min_replica=None,
                 min_storage=None, modify_enabled=None):
        self.component_format_name = component_format_name  # type: str
        self.component_name = component_name  # type: str
        self.default_cu_num = default_cu_num  # type: int
        self.default_replica = default_replica  # type: int
        self.default_storage = default_storage  # type: int
        self.max_cu_num = max_cu_num  # type: int
        self.max_replica = max_replica  # type: int
        self.max_storage = max_storage  # type: int
        self.min_cu_num = min_cu_num  # type: int
        self.min_replica = min_replica  # type: int
        self.min_storage = min_storage  # type: int
        self.modify_enabled = modify_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCspSpecificationInfoResponseBodyDataConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_format_name is not None:
            result['ComponentFormatName'] = self.component_format_name
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.default_cu_num is not None:
            result['DefaultCuNum'] = self.default_cu_num
        if self.default_replica is not None:
            result['DefaultReplica'] = self.default_replica
        if self.default_storage is not None:
            result['DefaultStorage'] = self.default_storage
        if self.max_cu_num is not None:
            result['MaxCuNum'] = self.max_cu_num
        if self.max_replica is not None:
            result['MaxReplica'] = self.max_replica
        if self.max_storage is not None:
            result['MaxStorage'] = self.max_storage
        if self.min_cu_num is not None:
            result['MinCuNum'] = self.min_cu_num
        if self.min_replica is not None:
            result['MinReplica'] = self.min_replica
        if self.min_storage is not None:
            result['MinStorage'] = self.min_storage
        if self.modify_enabled is not None:
            result['ModifyEnabled'] = self.modify_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentFormatName') is not None:
            self.component_format_name = m.get('ComponentFormatName')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('DefaultCuNum') is not None:
            self.default_cu_num = m.get('DefaultCuNum')
        if m.get('DefaultReplica') is not None:
            self.default_replica = m.get('DefaultReplica')
        if m.get('DefaultStorage') is not None:
            self.default_storage = m.get('DefaultStorage')
        if m.get('MaxCuNum') is not None:
            self.max_cu_num = m.get('MaxCuNum')
        if m.get('MaxReplica') is not None:
            self.max_replica = m.get('MaxReplica')
        if m.get('MaxStorage') is not None:
            self.max_storage = m.get('MaxStorage')
        if m.get('MinCuNum') is not None:
            self.min_cu_num = m.get('MinCuNum')
        if m.get('MinReplica') is not None:
            self.min_replica = m.get('MinReplica')
        if m.get('MinStorage') is not None:
            self.min_storage = m.get('MinStorage')
        if m.get('ModifyEnabled') is not None:
            self.modify_enabled = m.get('ModifyEnabled')
        return self


class GetCspSpecificationInfoResponseBodyData(TeaModel):
    def __init__(self, configuration=None):
        self.configuration = configuration  # type: list[GetCspSpecificationInfoResponseBodyDataConfiguration]

    def validate(self):
        if self.configuration:
            for k in self.configuration:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetCspSpecificationInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Configuration'] = []
        if self.configuration is not None:
            for k in self.configuration:
                result['Configuration'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.configuration = []
        if m.get('Configuration') is not None:
            for k in m.get('Configuration'):
                temp_model = GetCspSpecificationInfoResponseBodyDataConfiguration()
                self.configuration.append(temp_model.from_map(k))
        return self


class GetCspSpecificationInfoResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: GetCspSpecificationInfoResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCspSpecificationInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCspSpecificationInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCspSpecificationInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCspSpecificationInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCspSpecificationInfoResponse, self).to_map()
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
            temp_model = GetCspSpecificationInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCspUpgradeLimitInfoResponseBodyData(TeaModel):
    def __init__(self, connector_cpu=None, connector_modified=None, connector_replica=None,
                 control_center_cpu=None, control_center_modified=None, control_center_replica=None, kafka_cpu=None,
                 kafka_data_storage=None, kafka_data_storage_integer=None, kafka_replica=None, ksql_cpu=None, ksql_modified=None,
                 ksql_replica=None, rest_proxy_cpu=None, rest_proxy_modified=None, rest_proxy_replica=None,
                 schemaregistry_cpu=None, schemaregistry_modified=None, schemaregistry_replica=None, zookeeper_cpu=None,
                 zookeeper_modified=None, zookeeper_replica=None):
        self.connector_cpu = connector_cpu  # type: int
        self.connector_modified = connector_modified  # type: bool
        self.connector_replica = connector_replica  # type: int
        self.control_center_cpu = control_center_cpu  # type: int
        self.control_center_modified = control_center_modified  # type: bool
        self.control_center_replica = control_center_replica  # type: int
        self.kafka_cpu = kafka_cpu  # type: int
        self.kafka_data_storage = kafka_data_storage  # type: str
        self.kafka_data_storage_integer = kafka_data_storage_integer  # type: int
        self.kafka_replica = kafka_replica  # type: int
        self.ksql_cpu = ksql_cpu  # type: int
        self.ksql_modified = ksql_modified  # type: bool
        self.ksql_replica = ksql_replica  # type: int
        self.rest_proxy_cpu = rest_proxy_cpu  # type: int
        self.rest_proxy_modified = rest_proxy_modified  # type: bool
        self.rest_proxy_replica = rest_proxy_replica  # type: int
        self.schemaregistry_cpu = schemaregistry_cpu  # type: int
        self.schemaregistry_modified = schemaregistry_modified  # type: bool
        self.schemaregistry_replica = schemaregistry_replica  # type: int
        self.zookeeper_cpu = zookeeper_cpu  # type: int
        self.zookeeper_modified = zookeeper_modified  # type: bool
        self.zookeeper_replica = zookeeper_replica  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCspUpgradeLimitInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_cpu is not None:
            result['ConnectorCpu'] = self.connector_cpu
        if self.connector_modified is not None:
            result['ConnectorModified'] = self.connector_modified
        if self.connector_replica is not None:
            result['ConnectorReplica'] = self.connector_replica
        if self.control_center_cpu is not None:
            result['ControlCenterCpu'] = self.control_center_cpu
        if self.control_center_modified is not None:
            result['ControlCenterModified'] = self.control_center_modified
        if self.control_center_replica is not None:
            result['ControlCenterReplica'] = self.control_center_replica
        if self.kafka_cpu is not None:
            result['KafkaCpu'] = self.kafka_cpu
        if self.kafka_data_storage is not None:
            result['KafkaDataStorage'] = self.kafka_data_storage
        if self.kafka_data_storage_integer is not None:
            result['KafkaDataStorageInteger'] = self.kafka_data_storage_integer
        if self.kafka_replica is not None:
            result['KafkaReplica'] = self.kafka_replica
        if self.ksql_cpu is not None:
            result['KsqlCpu'] = self.ksql_cpu
        if self.ksql_modified is not None:
            result['KsqlModified'] = self.ksql_modified
        if self.ksql_replica is not None:
            result['KsqlReplica'] = self.ksql_replica
        if self.rest_proxy_cpu is not None:
            result['RestProxyCpu'] = self.rest_proxy_cpu
        if self.rest_proxy_modified is not None:
            result['RestProxyModified'] = self.rest_proxy_modified
        if self.rest_proxy_replica is not None:
            result['RestProxyReplica'] = self.rest_proxy_replica
        if self.schemaregistry_cpu is not None:
            result['SchemaregistryCpu'] = self.schemaregistry_cpu
        if self.schemaregistry_modified is not None:
            result['SchemaregistryModified'] = self.schemaregistry_modified
        if self.schemaregistry_replica is not None:
            result['SchemaregistryReplica'] = self.schemaregistry_replica
        if self.zookeeper_cpu is not None:
            result['ZookeeperCpu'] = self.zookeeper_cpu
        if self.zookeeper_modified is not None:
            result['ZookeeperModified'] = self.zookeeper_modified
        if self.zookeeper_replica is not None:
            result['ZookeeperReplica'] = self.zookeeper_replica
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectorCpu') is not None:
            self.connector_cpu = m.get('ConnectorCpu')
        if m.get('ConnectorModified') is not None:
            self.connector_modified = m.get('ConnectorModified')
        if m.get('ConnectorReplica') is not None:
            self.connector_replica = m.get('ConnectorReplica')
        if m.get('ControlCenterCpu') is not None:
            self.control_center_cpu = m.get('ControlCenterCpu')
        if m.get('ControlCenterModified') is not None:
            self.control_center_modified = m.get('ControlCenterModified')
        if m.get('ControlCenterReplica') is not None:
            self.control_center_replica = m.get('ControlCenterReplica')
        if m.get('KafkaCpu') is not None:
            self.kafka_cpu = m.get('KafkaCpu')
        if m.get('KafkaDataStorage') is not None:
            self.kafka_data_storage = m.get('KafkaDataStorage')
        if m.get('KafkaDataStorageInteger') is not None:
            self.kafka_data_storage_integer = m.get('KafkaDataStorageInteger')
        if m.get('KafkaReplica') is not None:
            self.kafka_replica = m.get('KafkaReplica')
        if m.get('KsqlCpu') is not None:
            self.ksql_cpu = m.get('KsqlCpu')
        if m.get('KsqlModified') is not None:
            self.ksql_modified = m.get('KsqlModified')
        if m.get('KsqlReplica') is not None:
            self.ksql_replica = m.get('KsqlReplica')
        if m.get('RestProxyCpu') is not None:
            self.rest_proxy_cpu = m.get('RestProxyCpu')
        if m.get('RestProxyModified') is not None:
            self.rest_proxy_modified = m.get('RestProxyModified')
        if m.get('RestProxyReplica') is not None:
            self.rest_proxy_replica = m.get('RestProxyReplica')
        if m.get('SchemaregistryCpu') is not None:
            self.schemaregistry_cpu = m.get('SchemaregistryCpu')
        if m.get('SchemaregistryModified') is not None:
            self.schemaregistry_modified = m.get('SchemaregistryModified')
        if m.get('SchemaregistryReplica') is not None:
            self.schemaregistry_replica = m.get('SchemaregistryReplica')
        if m.get('ZookeeperCpu') is not None:
            self.zookeeper_cpu = m.get('ZookeeperCpu')
        if m.get('ZookeeperModified') is not None:
            self.zookeeper_modified = m.get('ZookeeperModified')
        if m.get('ZookeeperReplica') is not None:
            self.zookeeper_replica = m.get('ZookeeperReplica')
        return self


class GetCspUpgradeLimitInfoResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: GetCspUpgradeLimitInfoResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCspUpgradeLimitInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCspUpgradeLimitInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCspUpgradeLimitInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCspUpgradeLimitInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCspUpgradeLimitInfoResponse, self).to_map()
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
            temp_model = GetCspUpgradeLimitInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRenewSpecVersionInfoRequest(TeaModel):
    def __init__(self, package_type=None, region_id=None):
        self.package_type = package_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRenewSpecVersionInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetRenewSpecVersionInfoResponseBodyDataPricingInfos(TeaModel):
    def __init__(self, duration=None, pricing_cycle=None):
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRenewSpecVersionInfoResponseBodyDataPricingInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class GetRenewSpecVersionInfoResponseBodyData(TeaModel):
    def __init__(self, multi_azpermission=None, package_type=None, pricing_infos=None, product_code=None,
                 region_id=None, spec_version=None, spec_version_en=None, visible=None):
        self.multi_azpermission = multi_azpermission  # type: bool
        self.package_type = package_type  # type: str
        self.pricing_infos = pricing_infos  # type: list[GetRenewSpecVersionInfoResponseBodyDataPricingInfos]
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str
        self.spec_version = spec_version  # type: str
        self.spec_version_en = spec_version_en  # type: str
        self.visible = visible  # type: bool

    def validate(self):
        if self.pricing_infos:
            for k in self.pricing_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRenewSpecVersionInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_azpermission is not None:
            result['MultiAZPermission'] = self.multi_azpermission
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        result['PricingInfos'] = []
        if self.pricing_infos is not None:
            for k in self.pricing_infos:
                result['PricingInfos'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.spec_version_en is not None:
            result['SpecVersionEn'] = self.spec_version_en
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MultiAZPermission') is not None:
            self.multi_azpermission = m.get('MultiAZPermission')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        self.pricing_infos = []
        if m.get('PricingInfos') is not None:
            for k in m.get('PricingInfos'):
                temp_model = GetRenewSpecVersionInfoResponseBodyDataPricingInfos()
                self.pricing_infos.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('SpecVersionEn') is not None:
            self.spec_version_en = m.get('SpecVersionEn')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class GetRenewSpecVersionInfoResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: GetRenewSpecVersionInfoResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetRenewSpecVersionInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetRenewSpecVersionInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetRenewSpecVersionInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRenewSpecVersionInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRenewSpecVersionInfoResponse, self).to_map()
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
            temp_model = GetRenewSpecVersionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSpecVersionInfoResponseBodyDataPricingInfos(TeaModel):
    def __init__(self, duration=None, pricing_cycle=None):
        self.duration = duration  # type: int
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSpecVersionInfoResponseBodyDataPricingInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class GetSpecVersionInfoResponseBodyData(TeaModel):
    def __init__(self, multi_azpermission=None, package_type=None, pricing_infos=None, product_code=None,
                 region_id=None, spec_version=None, spec_version_en=None, visible=None):
        self.multi_azpermission = multi_azpermission  # type: bool
        self.package_type = package_type  # type: str
        self.pricing_infos = pricing_infos  # type: list[GetSpecVersionInfoResponseBodyDataPricingInfos]
        self.product_code = product_code  # type: str
        self.region_id = region_id  # type: str
        self.spec_version = spec_version  # type: str
        self.spec_version_en = spec_version_en  # type: str
        self.visible = visible  # type: bool

    def validate(self):
        if self.pricing_infos:
            for k in self.pricing_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSpecVersionInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.multi_azpermission is not None:
            result['MultiAZPermission'] = self.multi_azpermission
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        result['PricingInfos'] = []
        if self.pricing_infos is not None:
            for k in self.pricing_infos:
                result['PricingInfos'].append(k.to_map() if k else None)
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.spec_version_en is not None:
            result['SpecVersionEn'] = self.spec_version_en
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MultiAZPermission') is not None:
            self.multi_azpermission = m.get('MultiAZPermission')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        self.pricing_infos = []
        if m.get('PricingInfos') is not None:
            for k in m.get('PricingInfos'):
                temp_model = GetSpecVersionInfoResponseBodyDataPricingInfos()
                self.pricing_infos.append(temp_model.from_map(k))
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('SpecVersionEn') is not None:
            self.spec_version_en = m.get('SpecVersionEn')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class GetSpecVersionInfoResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[GetSpecVersionInfoResponseBodyData]
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetSpecVersionInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = GetSpecVersionInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSpecVersionInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetSpecVersionInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSpecVersionInfoResponse, self).to_map()
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
            temp_model = GetSpecVersionInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserAclDetailRequest(TeaModel):
    def __init__(self, instance_id=None, pattern_type=None, permission_type=None, resource_name=None,
                 resource_type=None, user_name=None):
        self.instance_id = instance_id  # type: str
        self.pattern_type = pattern_type  # type: str
        self.permission_type = permission_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserAclDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class GetUserAclDetailResponseBodyData(TeaModel):
    def __init__(self, acl_operation_list=None, pattern_type=None, permission_type=None, resource_name=None,
                 resource_type=None):
        self.acl_operation_list = acl_operation_list  # type: list[str]
        self.pattern_type = pattern_type  # type: str
        self.permission_type = permission_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserAclDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_list is not None:
            result['AclOperationList'] = self.acl_operation_list
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperationList') is not None:
            self.acl_operation_list = m.get('AclOperationList')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetUserAclDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: GetUserAclDetailResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetUserAclDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetUserAclDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetUserAclDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserAclDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserAclDetailResponse, self).to_map()
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
            temp_model = GetUserAclDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVersionInfosResponseBodyData(TeaModel):
    def __init__(self, spec_version=None, spec_version_en=None):
        self.spec_version = spec_version  # type: str
        self.spec_version_en = spec_version_en  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVersionInfosResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.spec_version_en is not None:
            result['SpecVersionEn'] = self.spec_version_en
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('SpecVersionEn') is not None:
            self.spec_version_en = m.get('SpecVersionEn')
        return self


class GetVersionInfosResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[GetVersionInfosResponseBodyData]
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetVersionInfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = GetVersionInfosResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetVersionInfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVersionInfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVersionInfosResponse, self).to_map()
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
            temp_model = GetVersionInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HasDefaultRoleResponseBodyData(TeaModel):
    def __init__(self, has_auth=None, role_auth_url=None):
        self.has_auth = has_auth  # type: bool
        self.role_auth_url = role_auth_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(HasDefaultRoleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_auth is not None:
            result['HasAuth'] = self.has_auth
        if self.role_auth_url is not None:
            result['RoleAuthUrl'] = self.role_auth_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasAuth') is not None:
            self.has_auth = m.get('HasAuth')
        if m.get('RoleAuthUrl') is not None:
            self.role_auth_url = m.get('RoleAuthUrl')
        return self


class HasDefaultRoleResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: HasDefaultRoleResponseBodyData
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(HasDefaultRoleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = HasDefaultRoleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class HasDefaultRoleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: HasDefaultRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(HasDefaultRoleResponse, self).to_map()
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
            temp_model = HasDefaultRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAclAuthorizationRequest(TeaModel):
    def __init__(self, instance_id=None, pattern_type=None, permission_type=None, resource_name=None,
                 resource_type=None, user_name=None):
        self.instance_id = instance_id  # type: str
        self.pattern_type = pattern_type  # type: str
        self.permission_type = permission_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAclAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListAclAuthorizationResponseBodyData(TeaModel):
    def __init__(self, acl_operation_list=None, pattern_type=None, permission_type=None, resource_name=None,
                 resource_type=None):
        self.acl_operation_list = acl_operation_list  # type: list[str]
        self.pattern_type = pattern_type  # type: str
        self.permission_type = permission_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAclAuthorizationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operation_list is not None:
            result['AclOperationList'] = self.acl_operation_list
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperationList') is not None:
            self.acl_operation_list = m.get('AclOperationList')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListAclAuthorizationResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListAclAuthorizationResponseBodyData]
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAclAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = ListAclAuthorizationResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAclAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAclAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAclAuthorizationResponse, self).to_map()
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
            temp_model = ListAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAuthenticatedUserRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticatedUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListAuthenticatedUserResponseBodyData(TeaModel):
    def __init__(self, creation_time=None, user_name=None):
        self.creation_time = creation_time  # type: long
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAuthenticatedUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListAuthenticatedUserResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListAuthenticatedUserResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAuthenticatedUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = ListAuthenticatedUserResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAuthenticatedUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAuthenticatedUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAuthenticatedUserResponse, self).to_map()
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
            temp_model = ListAuthenticatedUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentInfoRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListComponentInfoResponseBodyData(TeaModel):
    def __init__(self, service_external_link=None, service_internal_link=None, service_name=None):
        self.service_external_link = service_external_link  # type: str
        self.service_internal_link = service_internal_link  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_external_link is not None:
            result['ServiceExternalLink'] = self.service_external_link
        if self.service_internal_link is not None:
            result['ServiceInternalLink'] = self.service_internal_link
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceExternalLink') is not None:
            self.service_external_link = m.get('ServiceExternalLink')
        if m.get('ServiceInternalLink') is not None:
            self.service_internal_link = m.get('ServiceInternalLink')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class ListComponentInfoResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListComponentInfoResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = ListComponentInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListComponentInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListComponentInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentInfoResponse, self).to_map()
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
            temp_model = ListComponentInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCspConnectorDetailRequest(TeaModel):
    def __init__(self, name=None, owner=None, package_type=None, types=None):
        self.name = name  # type: str
        self.owner = owner  # type: int
        self.package_type = package_type  # type: str
        self.types = types  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCspConnectorDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.types is not None:
            result['Types'] = self.types
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Types') is not None:
            self.types = m.get('Types')
        return self


class ListCspConnectorDetailShrinkRequest(TeaModel):
    def __init__(self, name=None, owner=None, package_type=None, types_shrink=None):
        self.name = name  # type: str
        self.owner = owner  # type: int
        self.package_type = package_type  # type: str
        self.types_shrink = types_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCspConnectorDetailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.types_shrink is not None:
            result['Types'] = self.types_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('Types') is not None:
            self.types_shrink = m.get('Types')
        return self


class ListCspConnectorDetailResponseBodyDataOwner(TeaModel):
    def __init__(self, logo=None, name=None, url=None, user_name=None):
        self.logo = logo  # type: str
        self.name = name  # type: str
        self.url = url  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCspConnectorDetailResponseBodyDataOwner, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.url is not None:
            result['Url'] = self.url
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListCspConnectorDetailResponseBodyData(TeaModel):
    def __init__(self, component_types=None, description=None, hub_url=None, last_modified=None, logo=None,
                 name=None, owner=None, title=None, version=None):
        self.component_types = component_types  # type: list[str]
        self.description = description  # type: str
        self.hub_url = hub_url  # type: str
        self.last_modified = last_modified  # type: long
        self.logo = logo  # type: str
        self.name = name  # type: str
        self.owner = owner  # type: ListCspConnectorDetailResponseBodyDataOwner
        self.title = title  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.owner:
            self.owner.validate()

    def to_map(self):
        _map = super(ListCspConnectorDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_types is not None:
            result['ComponentTypes'] = self.component_types
        if self.description is not None:
            result['Description'] = self.description
        if self.hub_url is not None:
            result['HubUrl'] = self.hub_url
        if self.last_modified is not None:
            result['LastModified'] = self.last_modified
        if self.logo is not None:
            result['Logo'] = self.logo
        if self.name is not None:
            result['Name'] = self.name
        if self.owner is not None:
            result['Owner'] = self.owner.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentTypes') is not None:
            self.component_types = m.get('ComponentTypes')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HubUrl') is not None:
            self.hub_url = m.get('HubUrl')
        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')
        if m.get('Logo') is not None:
            self.logo = m.get('Logo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Owner') is not None:
            temp_model = ListCspConnectorDetailResponseBodyDataOwner()
            self.owner = temp_model.from_map(m['Owner'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListCspConnectorDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListCspConnectorDetailResponseBodyData]
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCspConnectorDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = ListCspConnectorDetailResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCspConnectorDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCspConnectorDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCspConnectorDetailResponse, self).to_map()
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
            temp_model = ListCspConnectorDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOssinfosRequest(TeaModel):
    def __init__(self, bucket_name_prefix=None, region_id=None):
        self.bucket_name_prefix = bucket_name_prefix  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOssinfosRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name_prefix is not None:
            result['BucketNamePrefix'] = self.bucket_name_prefix
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketNamePrefix') is not None:
            self.bucket_name_prefix = m.get('BucketNamePrefix')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOssinfosResponseBodyData(TeaModel):
    def __init__(self, bucket_name=None, endpoint=None, oxs_endpoint=None, vpc_endpoint=None):
        self.bucket_name = bucket_name  # type: str
        self.endpoint = endpoint  # type: str
        self.oxs_endpoint = oxs_endpoint  # type: str
        self.vpc_endpoint = vpc_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOssinfosResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.oxs_endpoint is not None:
            result['OxsEndpoint'] = self.oxs_endpoint
        if self.vpc_endpoint is not None:
            result['VpcEndpoint'] = self.vpc_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('OxsEndpoint') is not None:
            self.oxs_endpoint = m.get('OxsEndpoint')
        if m.get('VpcEndpoint') is not None:
            self.vpc_endpoint = m.get('VpcEndpoint')
        return self


class ListOssinfosResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: list[ListOssinfosResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOssinfosResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListOssinfosResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListOssinfosResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOssinfosResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOssinfosResponse, self).to_map()
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
            temp_model = ListOssinfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyData(TeaModel):
    def __init__(self, description=None, description_en=None, region_id=None, region_name=None):
        self.description = description  # type: str
        self.description_en = description_en  # type: str
        self.region_id = region_id  # type: str
        self.region_name = region_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListRegionsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.description_en is not None:
            result['DescriptionEn'] = self.description_en
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DescriptionEn') is not None:
            self.description_en = m.get('DescriptionEn')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[ListRegionsResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
                temp_model = ListRegionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListRegionsResponse, self).to_map()
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityGroupsRequest(TeaModel):
    def __init__(self, vpc_id=None):
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListSecurityGroupsResponseBodyData(TeaModel):
    def __init__(self, creation_time=None, description=None, security_group_id=None, security_group_name=None,
                 vpc_id=None):
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.security_group_id = security_group_id  # type: str
        self.security_group_name = security_group_name  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityGroupsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.security_group_name is not None:
            result['SecurityGroupName'] = self.security_group_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('SecurityGroupName') is not None:
            self.security_group_name = m.get('SecurityGroupName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListSecurityGroupsResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: list[ListSecurityGroupsResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListSecurityGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecurityGroupsResponse, self).to_map()
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
            temp_model = ListSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcsRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcsResponseBodyData(TeaModel):
    def __init__(self, cidr_block=None, description=None, region_id=None, status=None, vpc_id=None, vpc_name=None):
        self.cidr_block = cidr_block  # type: str
        self.description = description  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vpc_name = vpc_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        return self


class ListVpcsResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: list[ListVpcsResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVpcsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVpcsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcsResponse, self).to_map()
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
            temp_model = ListVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVswitchesRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, vpc_id=None, zone_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVswitchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVswitchesResponseBodyData(TeaModel):
    def __init__(self, available_ip_address_count=None, cidr_block=None, creation_time=None, description=None,
                 is_default=None, status=None, v_switch_id=None, v_switch_name=None, vpc_id=None, zone_id=None):
        self.available_ip_address_count = available_ip_address_count  # type: long
        self.cidr_block = cidr_block  # type: str
        self.creation_time = creation_time  # type: str
        self.description = description  # type: str
        self.is_default = is_default  # type: bool
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.v_switch_name = v_switch_name  # type: str
        self.vpc_id = vpc_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVswitchesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVswitchesResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: list[ListVswitchesResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVswitchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListVswitchesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListVswitchesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVswitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVswitchesResponse, self).to_map()
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
            temp_model = ListVswitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListZonesResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[str]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListZonesResponse, self).to_map()
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
            temp_model = ListZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAclAuthorizationRequest(TeaModel):
    def __init__(self, acl_operations=None, client_token=None, instance_id=None, pattern_type=None,
                 permission_type=None, resource_name=None, resource_type=None, user_name=None):
        self.acl_operations = acl_operations  # type: str
        self.client_token = client_token  # type: str
        self.instance_id = instance_id  # type: str
        self.pattern_type = pattern_type  # type: str
        self.permission_type = permission_type  # type: str
        self.resource_name = resource_name  # type: str
        self.resource_type = resource_type  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAclAuthorizationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_operations is not None:
            result['AclOperations'] = self.acl_operations
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pattern_type is not None:
            result['PatternType'] = self.pattern_type
        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AclOperations') is not None:
            self.acl_operations = m.get('AclOperations')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PatternType') is not None:
            self.pattern_type = m.get('PatternType')
        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyAclAuthorizationResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, http_status_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAclAuthorizationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyAclAuthorizationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAclAuthorizationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAclAuthorizationResponse, self).to_map()
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
            temp_model = ModifyAclAuthorizationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserPasswordRequest(TeaModel):
    def __init__(self, instance_id=None, password=None, user_name=None):
        self.instance_id = instance_id  # type: str
        self.password = password  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ModifyUserPasswordResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, http_status_code=None, request_id=None, success=None):
        self.data = data  # type: bool
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyUserPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserPasswordResponse, self).to_map()
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
            temp_model = ModifyUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPriceRequest(TeaModel):
    def __init__(self, cluster_info=None):
        self.cluster_info = cluster_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterInfo') is not None:
            self.cluster_info = m.get('ClusterInfo')
        return self


class QueryPriceResponseBodyDataCspSoftPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPriceResponseBodyDataCspSoftPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryPriceResponseBodyData(TeaModel):
    def __init__(self, csp_soft_price_info=None):
        self.csp_soft_price_info = csp_soft_price_info  # type: QueryPriceResponseBodyDataCspSoftPriceInfo

    def validate(self):
        if self.csp_soft_price_info:
            self.csp_soft_price_info.validate()

    def to_map(self):
        _map = super(QueryPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csp_soft_price_info is not None:
            result['CspSoftPriceInfo'] = self.csp_soft_price_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CspSoftPriceInfo') is not None:
            temp_model = QueryPriceResponseBodyDataCspSoftPriceInfo()
            self.csp_soft_price_info = temp_model.from_map(m['CspSoftPriceInfo'])
        return self


class QueryPriceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPriceResponseBodyData
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QueryPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPriceResponse, self).to_map()
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
            temp_model = QueryPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRenewPriceRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, pricing_cycle=None):
        self.duration = duration  # type: str
        self.instance_id = instance_id  # type: str
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class QueryRenewPriceResponseBodyDataCspSoftPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRenewPriceResponseBodyDataCspSoftPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryRenewPriceResponseBodyData(TeaModel):
    def __init__(self, csp_soft_price_info=None):
        self.csp_soft_price_info = csp_soft_price_info  # type: QueryRenewPriceResponseBodyDataCspSoftPriceInfo

    def validate(self):
        if self.csp_soft_price_info:
            self.csp_soft_price_info.validate()

    def to_map(self):
        _map = super(QueryRenewPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csp_soft_price_info is not None:
            result['CspSoftPriceInfo'] = self.csp_soft_price_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CspSoftPriceInfo') is not None:
            temp_model = QueryRenewPriceResponseBodyDataCspSoftPriceInfo()
            self.csp_soft_price_info = temp_model.from_map(m['CspSoftPriceInfo'])
        return self


class QueryRenewPriceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: QueryRenewPriceResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRenewPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryRenewPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRenewPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRenewPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRenewPriceResponse, self).to_map()
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
            temp_model = QueryRenewPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScaleUpPriceRequest(TeaModel):
    def __init__(self, broker_number=None, connector_cpu=None, connector_num=None, control_center_cpu=None,
                 control_center_num=None, control_center_storage=None, cu_number=None, disk_size=None, instance_id=None, ksql_cpu=None,
                 ksql_num=None, ksql_storage=None, rest_proxy_cpu=None, rest_proxy_num=None, schemaregistry_cpu=None,
                 schemaregistry_num=None, zookeeper_cpu=None, zookeeper_num=None, zookeeper_storage=None):
        self.broker_number = broker_number  # type: int
        self.connector_cpu = connector_cpu  # type: int
        self.connector_num = connector_num  # type: int
        self.control_center_cpu = control_center_cpu  # type: int
        self.control_center_num = control_center_num  # type: int
        self.control_center_storage = control_center_storage  # type: int
        self.cu_number = cu_number  # type: int
        self.disk_size = disk_size  # type: int
        self.instance_id = instance_id  # type: str
        self.ksql_cpu = ksql_cpu  # type: int
        self.ksql_num = ksql_num  # type: int
        self.ksql_storage = ksql_storage  # type: int
        self.rest_proxy_cpu = rest_proxy_cpu  # type: int
        self.rest_proxy_num = rest_proxy_num  # type: int
        self.schemaregistry_cpu = schemaregistry_cpu  # type: int
        self.schemaregistry_num = schemaregistry_num  # type: int
        self.zookeeper_cpu = zookeeper_cpu  # type: int
        self.zookeeper_num = zookeeper_num  # type: int
        self.zookeeper_storage = zookeeper_storage  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpPriceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_number is not None:
            result['BrokerNumber'] = self.broker_number
        if self.connector_cpu is not None:
            result['ConnectorCpu'] = self.connector_cpu
        if self.connector_num is not None:
            result['ConnectorNum'] = self.connector_num
        if self.control_center_cpu is not None:
            result['ControlCenterCpu'] = self.control_center_cpu
        if self.control_center_num is not None:
            result['ControlCenterNum'] = self.control_center_num
        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage
        if self.cu_number is not None:
            result['CuNumber'] = self.cu_number
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ksql_cpu is not None:
            result['KsqlCpu'] = self.ksql_cpu
        if self.ksql_num is not None:
            result['KsqlNum'] = self.ksql_num
        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage
        if self.rest_proxy_cpu is not None:
            result['RestProxyCpu'] = self.rest_proxy_cpu
        if self.rest_proxy_num is not None:
            result['RestProxyNum'] = self.rest_proxy_num
        if self.schemaregistry_cpu is not None:
            result['SchemaregistryCpu'] = self.schemaregistry_cpu
        if self.schemaregistry_num is not None:
            result['SchemaregistryNum'] = self.schemaregistry_num
        if self.zookeeper_cpu is not None:
            result['ZookeeperCpu'] = self.zookeeper_cpu
        if self.zookeeper_num is not None:
            result['ZookeeperNum'] = self.zookeeper_num
        if self.zookeeper_storage is not None:
            result['ZookeeperStorage'] = self.zookeeper_storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerNumber') is not None:
            self.broker_number = m.get('BrokerNumber')
        if m.get('ConnectorCpu') is not None:
            self.connector_cpu = m.get('ConnectorCpu')
        if m.get('ConnectorNum') is not None:
            self.connector_num = m.get('ConnectorNum')
        if m.get('ControlCenterCpu') is not None:
            self.control_center_cpu = m.get('ControlCenterCpu')
        if m.get('ControlCenterNum') is not None:
            self.control_center_num = m.get('ControlCenterNum')
        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')
        if m.get('CuNumber') is not None:
            self.cu_number = m.get('CuNumber')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KsqlCpu') is not None:
            self.ksql_cpu = m.get('KsqlCpu')
        if m.get('KsqlNum') is not None:
            self.ksql_num = m.get('KsqlNum')
        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')
        if m.get('RestProxyCpu') is not None:
            self.rest_proxy_cpu = m.get('RestProxyCpu')
        if m.get('RestProxyNum') is not None:
            self.rest_proxy_num = m.get('RestProxyNum')
        if m.get('SchemaregistryCpu') is not None:
            self.schemaregistry_cpu = m.get('SchemaregistryCpu')
        if m.get('SchemaregistryNum') is not None:
            self.schemaregistry_num = m.get('SchemaregistryNum')
        if m.get('ZookeeperCpu') is not None:
            self.zookeeper_cpu = m.get('ZookeeperCpu')
        if m.get('ZookeeperNum') is not None:
            self.zookeeper_num = m.get('ZookeeperNum')
        if m.get('ZookeeperStorage') is not None:
            self.zookeeper_storage = m.get('ZookeeperStorage')
        return self


class QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo(TeaModel):
    def __init__(self, currency=None, discount_price=None, original_price=None, trade_price=None):
        self.currency = currency  # type: str
        self.discount_price = discount_price  # type: float
        self.original_price = original_price  # type: float
        self.trade_price = trade_price  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.currency is not None:
            result['Currency'] = self.currency
        if self.discount_price is not None:
            result['DiscountPrice'] = self.discount_price
        if self.original_price is not None:
            result['OriginalPrice'] = self.original_price
        if self.trade_price is not None:
            result['TradePrice'] = self.trade_price
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Currency') is not None:
            self.currency = m.get('Currency')
        if m.get('DiscountPrice') is not None:
            self.discount_price = m.get('DiscountPrice')
        if m.get('OriginalPrice') is not None:
            self.original_price = m.get('OriginalPrice')
        if m.get('TradePrice') is not None:
            self.trade_price = m.get('TradePrice')
        return self


class QueryScaleUpPriceResponseBodyData(TeaModel):
    def __init__(self, csp_soft_price_info=None):
        self.csp_soft_price_info = csp_soft_price_info  # type: QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo

    def validate(self):
        if self.csp_soft_price_info:
            self.csp_soft_price_info.validate()

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.csp_soft_price_info is not None:
            result['CspSoftPriceInfo'] = self.csp_soft_price_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CspSoftPriceInfo') is not None:
            temp_model = QueryScaleUpPriceResponseBodyDataCspSoftPriceInfo()
            self.csp_soft_price_info = temp_model.from_map(m['CspSoftPriceInfo'])
        return self


class QueryScaleUpPriceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: QueryScaleUpPriceResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryScaleUpPriceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = QueryScaleUpPriceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScaleUpPriceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryScaleUpPriceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryScaleUpPriceResponse, self).to_map()
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
            temp_model = QueryScaleUpPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUnpaidOrderRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUnpaidOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryUnpaidOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: list[long]
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryUnpaidOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUnpaidOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryUnpaidOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryUnpaidOrderResponse, self).to_map()
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
            temp_model = QueryUnpaidOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenewInstanceRequest(TeaModel):
    def __init__(self, duration=None, instance_id=None, pricing_cycle=None):
        self.duration = duration  # type: str
        self.instance_id = instance_id  # type: str
        self.pricing_cycle = pricing_cycle  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        return self


class RenewInstanceResponseBodyData(TeaModel):
    def __init__(self, order_ids=None):
        self.order_ids = order_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RenewInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class RenewInstanceResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: RenewInstanceResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(RenewInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = RenewInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RenewInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RenewInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RenewInstanceResponse, self).to_map()
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
            temp_model = RenewInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleUpClusterRequest(TeaModel):
    def __init__(self, broker_number=None, connector_cpu=None, connector_num=None, control_center_cpu=None,
                 control_center_num=None, control_center_storage=None, cu_number=None, disk_size=None, instance_id=None, ksql_cpu=None,
                 ksql_num=None, ksql_storage=None, rest_proxy_cpu=None, rest_proxy_num=None, schemaregistry_cpu=None,
                 schemaregistry_num=None, zookeeper_cpu=None, zookeeper_num=None, zookeeper_storage=None):
        self.broker_number = broker_number  # type: int
        self.connector_cpu = connector_cpu  # type: int
        self.connector_num = connector_num  # type: int
        self.control_center_cpu = control_center_cpu  # type: int
        self.control_center_num = control_center_num  # type: int
        self.control_center_storage = control_center_storage  # type: int
        self.cu_number = cu_number  # type: int
        self.disk_size = disk_size  # type: int
        self.instance_id = instance_id  # type: str
        self.ksql_cpu = ksql_cpu  # type: int
        self.ksql_num = ksql_num  # type: int
        self.ksql_storage = ksql_storage  # type: int
        self.rest_proxy_cpu = rest_proxy_cpu  # type: int
        self.rest_proxy_num = rest_proxy_num  # type: int
        self.schemaregistry_cpu = schemaregistry_cpu  # type: int
        self.schemaregistry_num = schemaregistry_num  # type: int
        self.zookeeper_cpu = zookeeper_cpu  # type: int
        self.zookeeper_num = zookeeper_num  # type: int
        self.zookeeper_storage = zookeeper_storage  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleUpClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_number is not None:
            result['BrokerNumber'] = self.broker_number
        if self.connector_cpu is not None:
            result['ConnectorCpu'] = self.connector_cpu
        if self.connector_num is not None:
            result['ConnectorNum'] = self.connector_num
        if self.control_center_cpu is not None:
            result['ControlCenterCpu'] = self.control_center_cpu
        if self.control_center_num is not None:
            result['ControlCenterNum'] = self.control_center_num
        if self.control_center_storage is not None:
            result['ControlCenterStorage'] = self.control_center_storage
        if self.cu_number is not None:
            result['CuNumber'] = self.cu_number
        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ksql_cpu is not None:
            result['KsqlCpu'] = self.ksql_cpu
        if self.ksql_num is not None:
            result['KsqlNum'] = self.ksql_num
        if self.ksql_storage is not None:
            result['KsqlStorage'] = self.ksql_storage
        if self.rest_proxy_cpu is not None:
            result['RestProxyCpu'] = self.rest_proxy_cpu
        if self.rest_proxy_num is not None:
            result['RestProxyNum'] = self.rest_proxy_num
        if self.schemaregistry_cpu is not None:
            result['SchemaregistryCpu'] = self.schemaregistry_cpu
        if self.schemaregistry_num is not None:
            result['SchemaregistryNum'] = self.schemaregistry_num
        if self.zookeeper_cpu is not None:
            result['ZookeeperCpu'] = self.zookeeper_cpu
        if self.zookeeper_num is not None:
            result['ZookeeperNum'] = self.zookeeper_num
        if self.zookeeper_storage is not None:
            result['ZookeeperStorage'] = self.zookeeper_storage
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerNumber') is not None:
            self.broker_number = m.get('BrokerNumber')
        if m.get('ConnectorCpu') is not None:
            self.connector_cpu = m.get('ConnectorCpu')
        if m.get('ConnectorNum') is not None:
            self.connector_num = m.get('ConnectorNum')
        if m.get('ControlCenterCpu') is not None:
            self.control_center_cpu = m.get('ControlCenterCpu')
        if m.get('ControlCenterNum') is not None:
            self.control_center_num = m.get('ControlCenterNum')
        if m.get('ControlCenterStorage') is not None:
            self.control_center_storage = m.get('ControlCenterStorage')
        if m.get('CuNumber') is not None:
            self.cu_number = m.get('CuNumber')
        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KsqlCpu') is not None:
            self.ksql_cpu = m.get('KsqlCpu')
        if m.get('KsqlNum') is not None:
            self.ksql_num = m.get('KsqlNum')
        if m.get('KsqlStorage') is not None:
            self.ksql_storage = m.get('KsqlStorage')
        if m.get('RestProxyCpu') is not None:
            self.rest_proxy_cpu = m.get('RestProxyCpu')
        if m.get('RestProxyNum') is not None:
            self.rest_proxy_num = m.get('RestProxyNum')
        if m.get('SchemaregistryCpu') is not None:
            self.schemaregistry_cpu = m.get('SchemaregistryCpu')
        if m.get('SchemaregistryNum') is not None:
            self.schemaregistry_num = m.get('SchemaregistryNum')
        if m.get('ZookeeperCpu') is not None:
            self.zookeeper_cpu = m.get('ZookeeperCpu')
        if m.get('ZookeeperNum') is not None:
            self.zookeeper_num = m.get('ZookeeperNum')
        if m.get('ZookeeperStorage') is not None:
            self.zookeeper_storage = m.get('ZookeeperStorage')
        return self


class ScaleUpClusterResponseBodyData(TeaModel):
    def __init__(self, order_ids=None):
        self.order_ids = order_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ScaleUpClusterResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_ids is not None:
            result['OrderIds'] = self.order_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderIds') is not None:
            self.order_ids = m.get('OrderIds')
        return self


class ScaleUpClusterResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: ScaleUpClusterResponseBodyData
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ScaleUpClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ScaleUpClusterResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScaleUpClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ScaleUpClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ScaleUpClusterResponse, self).to_map()
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
            temp_model = ScaleUpClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchClusterInstancesRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_name=None, page_number=None, page_size=None, region_id=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_name = cluster_name  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchClusterInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class SearchClusterInstancesResponseBodyDataClusterInstanceInfo(TeaModel):
    def __init__(self, control_center_login_name=None, duration=None, open_colddata_archiving=None,
                 oss_bucket_path=None, oss_endpoint=None, pay_type=None, pricing_cycle=None, spec_version=None, vpc_id=None,
                 vsw_ids=None):
        self.control_center_login_name = control_center_login_name  # type: str
        self.duration = duration  # type: int
        self.open_colddata_archiving = open_colddata_archiving  # type: bool
        self.oss_bucket_path = oss_bucket_path  # type: str
        self.oss_endpoint = oss_endpoint  # type: str
        self.pay_type = pay_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.spec_version = spec_version  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vsw_ids = vsw_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBodyDataClusterInstanceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_center_login_name is not None:
            result['ControlCenterLoginName'] = self.control_center_login_name
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.open_colddata_archiving is not None:
            result['OpenColddataArchiving'] = self.open_colddata_archiving
        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path
        if self.oss_endpoint is not None:
            result['OssEndpoint'] = self.oss_endpoint
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vsw_ids is not None:
            result['VswIds'] = self.vsw_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlCenterLoginName') is not None:
            self.control_center_login_name = m.get('ControlCenterLoginName')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('OpenColddataArchiving') is not None:
            self.open_colddata_archiving = m.get('OpenColddataArchiving')
        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')
        if m.get('OssEndpoint') is not None:
            self.oss_endpoint = m.get('OssEndpoint')
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswIds') is not None:
            self.vsw_ids = m.get('VswIds')
        return self


class SearchClusterInstancesResponseBodyData(TeaModel):
    def __init__(self, cku_conf=None, cluster_id=None, cluster_instance_info=None, cluster_name=None,
                 cluster_size=None, cluster_status=None, cluster_status_value=None, connector_visible=None,
                 control_center_url=None, cu_num=None, expire_time=None, gmt_create=None, gmt_modified=None, open_ksql=None,
                 order_biz_id=None, package_type=None, region_id=None, storage_size=None, template_version=None,
                 unpaid_order_ids=None, valid_broker_number=None, version=None, zone_id=None):
        self.cku_conf = cku_conf  # type: str
        self.cluster_id = cluster_id  # type: str
        self.cluster_instance_info = cluster_instance_info  # type: SearchClusterInstancesResponseBodyDataClusterInstanceInfo
        self.cluster_name = cluster_name  # type: str
        self.cluster_size = cluster_size  # type: int
        self.cluster_status = cluster_status  # type: str
        self.cluster_status_value = cluster_status_value  # type: int
        self.connector_visible = connector_visible  # type: bool
        self.control_center_url = control_center_url  # type: str
        self.cu_num = cu_num  # type: int
        self.expire_time = expire_time  # type: long
        self.gmt_create = gmt_create  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.open_ksql = open_ksql  # type: bool
        self.order_biz_id = order_biz_id  # type: str
        self.package_type = package_type  # type: str
        self.region_id = region_id  # type: str
        self.storage_size = storage_size  # type: int
        self.template_version = template_version  # type: str
        self.unpaid_order_ids = unpaid_order_ids  # type: list[long]
        self.valid_broker_number = valid_broker_number  # type: bool
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.cluster_instance_info:
            self.cluster_instance_info.validate()

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cku_conf is not None:
            result['CkuConf'] = self.cku_conf
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_instance_info is not None:
            result['ClusterInstanceInfo'] = self.cluster_instance_info.to_map()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_size is not None:
            result['ClusterSize'] = self.cluster_size
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.cluster_status_value is not None:
            result['ClusterStatusValue'] = self.cluster_status_value
        if self.connector_visible is not None:
            result['ConnectorVisible'] = self.connector_visible
        if self.control_center_url is not None:
            result['ControlCenterUrl'] = self.control_center_url
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.open_ksql is not None:
            result['OpenKsql'] = self.open_ksql
        if self.order_biz_id is not None:
            result['OrderBizId'] = self.order_biz_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version
        if self.unpaid_order_ids is not None:
            result['UnpaidOrderIds'] = self.unpaid_order_ids
        if self.valid_broker_number is not None:
            result['ValidBrokerNumber'] = self.valid_broker_number
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CkuConf') is not None:
            self.cku_conf = m.get('CkuConf')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterInstanceInfo') is not None:
            temp_model = SearchClusterInstancesResponseBodyDataClusterInstanceInfo()
            self.cluster_instance_info = temp_model.from_map(m['ClusterInstanceInfo'])
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterSize') is not None:
            self.cluster_size = m.get('ClusterSize')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('ClusterStatusValue') is not None:
            self.cluster_status_value = m.get('ClusterStatusValue')
        if m.get('ConnectorVisible') is not None:
            self.connector_visible = m.get('ConnectorVisible')
        if m.get('ControlCenterUrl') is not None:
            self.control_center_url = m.get('ControlCenterUrl')
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('OpenKsql') is not None:
            self.open_ksql = m.get('OpenKsql')
        if m.get('OrderBizId') is not None:
            self.order_biz_id = m.get('OrderBizId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')
        if m.get('UnpaidOrderIds') is not None:
            self.unpaid_order_ids = m.get('UnpaidOrderIds')
        if m.get('ValidBrokerNumber') is not None:
            self.valid_broker_number = m.get('ValidBrokerNumber')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchClusterInstancesResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None, total=None):
        self.data = data  # type: list[SearchClusterInstancesResponseBodyData]
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool
        self.total = total  # type: int

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SearchClusterInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchClusterInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchClusterInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SearchClusterInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SearchClusterInstancesResponse, self).to_map()
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
            temp_model = SearchClusterInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SingleOrderRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleOrderRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList(TeaModel):
    def __init__(self, broker_number=None, cu_num_per_broker=None, storage_size_per_broker=None):
        self.broker_number = broker_number  # type: int
        self.cu_num_per_broker = cu_num_per_broker  # type: int
        self.storage_size_per_broker = storage_size_per_broker  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.broker_number is not None:
            result['BrokerNumber'] = self.broker_number
        if self.cu_num_per_broker is not None:
            result['CuNumPerBroker'] = self.cu_num_per_broker
        if self.storage_size_per_broker is not None:
            result['StorageSizePerBroker'] = self.storage_size_per_broker
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BrokerNumber') is not None:
            self.broker_number = m.get('BrokerNumber')
        if m.get('CuNumPerBroker') is not None:
            self.cu_num_per_broker = m.get('CuNumPerBroker')
        if m.get('StorageSizePerBroker') is not None:
            self.storage_size_per_broker = m.get('StorageSizePerBroker')
        return self


class SingleOrderResponseBodyDataCspResourceConfig(TeaModel):
    def __init__(self, broker_config_list=None, multi_available_zone_permission=None):
        self.broker_config_list = broker_config_list  # type: list[SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList]
        self.multi_available_zone_permission = multi_available_zone_permission  # type: bool

    def validate(self):
        if self.broker_config_list:
            for k in self.broker_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SingleOrderResponseBodyDataCspResourceConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['BrokerConfigList'] = []
        if self.broker_config_list is not None:
            for k in self.broker_config_list:
                result['BrokerConfigList'].append(k.to_map() if k else None)
        if self.multi_available_zone_permission is not None:
            result['MultiAvailableZonePermission'] = self.multi_available_zone_permission
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.broker_config_list = []
        if m.get('BrokerConfigList') is not None:
            for k in m.get('BrokerConfigList'):
                temp_model = SingleOrderResponseBodyDataCspResourceConfigBrokerConfigList()
                self.broker_config_list.append(temp_model.from_map(k))
        if m.get('MultiAvailableZonePermission') is not None:
            self.multi_available_zone_permission = m.get('MultiAvailableZonePermission')
        return self


class SingleOrderResponseBodyDataEcsGroupList(TeaModel):
    def __init__(self, disk_capacity=None, disk_count=None, disk_type=None, host_group_name=None,
                 host_group_type=None, instance_type=None, node_count=None, sys_disk_capacity=None, sys_disk_type=None):
        self.disk_capacity = disk_capacity  # type: int
        self.disk_count = disk_count  # type: int
        self.disk_type = disk_type  # type: str
        self.host_group_name = host_group_name  # type: str
        self.host_group_type = host_group_type  # type: str
        self.instance_type = instance_type  # type: str
        self.node_count = node_count  # type: int
        self.sys_disk_capacity = sys_disk_capacity  # type: int
        self.sys_disk_type = sys_disk_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SingleOrderResponseBodyDataEcsGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_capacity is not None:
            result['DiskCapacity'] = self.disk_capacity
        if self.disk_count is not None:
            result['DiskCount'] = self.disk_count
        if self.disk_type is not None:
            result['DiskType'] = self.disk_type
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.host_group_type is not None:
            result['HostGroupType'] = self.host_group_type
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.sys_disk_capacity is not None:
            result['SysDiskCapacity'] = self.sys_disk_capacity
        if self.sys_disk_type is not None:
            result['SysDiskType'] = self.sys_disk_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskCapacity') is not None:
            self.disk_capacity = m.get('DiskCapacity')
        if m.get('DiskCount') is not None:
            self.disk_count = m.get('DiskCount')
        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('HostGroupType') is not None:
            self.host_group_type = m.get('HostGroupType')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('SysDiskCapacity') is not None:
            self.sys_disk_capacity = m.get('SysDiskCapacity')
        if m.get('SysDiskType') is not None:
            self.sys_disk_type = m.get('SysDiskType')
        return self


class SingleOrderResponseBodyData(TeaModel):
    def __init__(self, auto_renew=None, cluster_id=None, cluster_size=None, cluster_status=None,
                 csp_resource_config=None, cu_num=None, duration=None, ecs_group_list=None, instance_id=None, order_id=None,
                 package_type=None, pricing_cycle=None, spec_version=None, storage_size=None):
        self.auto_renew = auto_renew  # type: bool
        self.cluster_id = cluster_id  # type: str
        self.cluster_size = cluster_size  # type: int
        self.cluster_status = cluster_status  # type: int
        self.csp_resource_config = csp_resource_config  # type: SingleOrderResponseBodyDataCspResourceConfig
        self.cu_num = cu_num  # type: int
        self.duration = duration  # type: int
        self.ecs_group_list = ecs_group_list  # type: list[SingleOrderResponseBodyDataEcsGroupList]
        self.instance_id = instance_id  # type: str
        self.order_id = order_id  # type: str
        self.package_type = package_type  # type: str
        self.pricing_cycle = pricing_cycle  # type: str
        self.spec_version = spec_version  # type: str
        self.storage_size = storage_size  # type: int

    def validate(self):
        if self.csp_resource_config:
            self.csp_resource_config.validate()
        if self.ecs_group_list:
            for k in self.ecs_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(SingleOrderResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_size is not None:
            result['ClusterSize'] = self.cluster_size
        if self.cluster_status is not None:
            result['ClusterStatus'] = self.cluster_status
        if self.csp_resource_config is not None:
            result['CspResourceConfig'] = self.csp_resource_config.to_map()
        if self.cu_num is not None:
            result['CuNum'] = self.cu_num
        if self.duration is not None:
            result['Duration'] = self.duration
        result['EcsGroupList'] = []
        if self.ecs_group_list is not None:
            for k in self.ecs_group_list:
                result['EcsGroupList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        if self.pricing_cycle is not None:
            result['PricingCycle'] = self.pricing_cycle
        if self.spec_version is not None:
            result['SpecVersion'] = self.spec_version
        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSize') is not None:
            self.cluster_size = m.get('ClusterSize')
        if m.get('ClusterStatus') is not None:
            self.cluster_status = m.get('ClusterStatus')
        if m.get('CspResourceConfig') is not None:
            temp_model = SingleOrderResponseBodyDataCspResourceConfig()
            self.csp_resource_config = temp_model.from_map(m['CspResourceConfig'])
        if m.get('CuNum') is not None:
            self.cu_num = m.get('CuNum')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        self.ecs_group_list = []
        if m.get('EcsGroupList') is not None:
            for k in m.get('EcsGroupList'):
                temp_model = SingleOrderResponseBodyDataEcsGroupList()
                self.ecs_group_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        if m.get('PricingCycle') is not None:
            self.pricing_cycle = m.get('PricingCycle')
        if m.get('SpecVersion') is not None:
            self.spec_version = m.get('SpecVersion')
        if m.get('StorageSize') is not None:
            self.storage_size = m.get('StorageSize')
        return self


class SingleOrderResponseBody(TeaModel):
    def __init__(self, data=None, err_message=None, error_code=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: SingleOrderResponseBodyData
        self.err_message = err_message  # type: str
        self.error_code = error_code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(SingleOrderResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = SingleOrderResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SingleOrderResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SingleOrderResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SingleOrderResponse, self).to_map()
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
            temp_model = SingleOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateClusterNameRequest(TeaModel):
    def __init__(self, cluster_name=None, instance_id=None):
        self.cluster_name = cluster_name  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateClusterNameResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateClusterNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateClusterNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateClusterNameResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateClusterNameResponse, self).to_map()
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
            temp_model = UpdateClusterNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCspConnectorDetailRequestConnectorDetails(TeaModel):
    def __init__(self, name=None, owner=None, version=None):
        self.name = name  # type: str
        self.owner = owner  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCspConnectorDetailRequestConnectorDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateCspConnectorDetailRequest(TeaModel):
    def __init__(self, connector_details=None, instance_id=None):
        self.connector_details = connector_details  # type: list[UpdateCspConnectorDetailRequestConnectorDetails]
        self.instance_id = instance_id  # type: str

    def validate(self):
        if self.connector_details:
            for k in self.connector_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateCspConnectorDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectorDetails'] = []
        if self.connector_details is not None:
            for k in self.connector_details:
                result['ConnectorDetails'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connector_details = []
        if m.get('ConnectorDetails') is not None:
            for k in m.get('ConnectorDetails'):
                temp_model = UpdateCspConnectorDetailRequestConnectorDetails()
                self.connector_details.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateCspConnectorDetailShrinkRequest(TeaModel):
    def __init__(self, connector_details_shrink=None, instance_id=None):
        self.connector_details_shrink = connector_details_shrink  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCspConnectorDetailShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connector_details_shrink is not None:
            result['ConnectorDetails'] = self.connector_details_shrink
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectorDetails') is not None:
            self.connector_details_shrink = m.get('ConnectorDetails')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UpdateCspConnectorDetailResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: str
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateCspConnectorDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCspConnectorDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateCspConnectorDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateCspConnectorDetailResponse, self).to_map()
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
            temp_model = UpdateCspConnectorDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePublicNetworkStatusRequest(TeaModel):
    def __init__(self, instance_id=None, public_network_enabled=None):
        self.instance_id = instance_id  # type: str
        self.public_network_enabled = public_network_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePublicNetworkStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_network_enabled is not None:
            result['PublicNetworkEnabled'] = self.public_network_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicNetworkEnabled') is not None:
            self.public_network_enabled = m.get('PublicNetworkEnabled')
        return self


class UpdatePublicNetworkStatusResponseBody(TeaModel):
    def __init__(self, data=None, err_code=None, err_message=None, http_status_code=None, request_id=None,
                 success=None):
        self.data = data  # type: bool
        self.err_code = err_code  # type: int
        self.err_message = err_message  # type: str
        self.http_status_code = http_status_code  # type: int
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePublicNetworkStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_code is not None:
            result['ErrCode'] = self.err_code
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePublicNetworkStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePublicNetworkStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePublicNetworkStatusResponse, self).to_map()
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
            temp_model = UpdatePublicNetworkStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


