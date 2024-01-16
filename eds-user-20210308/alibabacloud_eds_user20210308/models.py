# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class GroupResources(TeaModel):
    def __init__(self, region=None, resource_id=None, resource_type=None):
        self.region = region  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GroupResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class WaIdPermissions(TeaModel):
    def __init__(self, code=None, is_basic_child=None, name=None, sub_permissions=None, type=None):
        self.code = code  # type: str
        self.is_basic_child = is_basic_child  # type: bool
        self.name = name  # type: str
        self.sub_permissions = sub_permissions  # type: list[WaIdPermissions]
        self.type = type  # type: str

    def validate(self):
        if self.sub_permissions:
            for k in self.sub_permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(WaIdPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_basic_child is not None:
            result['IsBasicChild'] = self.is_basic_child
        if self.name is not None:
            result['Name'] = self.name
        result['SubPermissions'] = []
        if self.sub_permissions is not None:
            for k in self.sub_permissions:
                result['SubPermissions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsBasicChild') is not None:
            self.is_basic_child = m.get('IsBasicChild')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.sub_permissions = []
        if m.get('SubPermissions') is not None:
            for k in m.get('SubPermissions'):
                temp_model = WaIdPermissions()
                self.sub_permissions.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CheckUsedPropertyRequest(TeaModel):
    def __init__(self, property_id=None):
        self.property_id = property_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUsedPropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class CheckUsedPropertyResponseBody(TeaModel):
    def __init__(self, request_id=None, use_count=None):
        self.request_id = request_id  # type: str
        self.use_count = use_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUsedPropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class CheckUsedPropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckUsedPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckUsedPropertyResponse, self).to_map()
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
            temp_model = CheckUsedPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckUsedPropertyValueRequest(TeaModel):
    def __init__(self, property_id=None, property_value_id=None):
        # The ID of the property.
        self.property_id = property_id  # type: long
        # The ID of the property value.
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUsedPropertyValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class CheckUsedPropertyValueResponseBody(TeaModel):
    def __init__(self, request_id=None, use_count=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of convenience users that are associated with the property value.
        self.use_count = use_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckUsedPropertyValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.use_count is not None:
            result['UseCount'] = self.use_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UseCount') is not None:
            self.use_count = m.get('UseCount')
        return self


class CheckUsedPropertyValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckUsedPropertyValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckUsedPropertyValueResponse, self).to_map()
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
            temp_model = CheckUsedPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePropertyRequest(TeaModel):
    def __init__(self, property_key=None, property_values=None):
        self.property_key = property_key  # type: str
        self.property_values = property_values  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')
        return self


class CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues(TeaModel):
    def __init__(self, error_code=None, error_message=None, property_id=None, property_value=None):
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.property_id = property_id  # type: long
        self.property_value = property_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        return self


class CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues(TeaModel):
    def __init__(self, property_value=None, property_value_id=None):
        self.property_value = property_value  # type: str
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class CreatePropertyResponseBodyCreateResultSavePropertyValueModel(TeaModel):
    def __init__(self, failed_property_values=None, save_property_values=None):
        self.failed_property_values = failed_property_values  # type: list[CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues]
        self.save_property_values = save_property_values  # type: list[CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues]

    def validate(self):
        if self.failed_property_values:
            for k in self.failed_property_values:
                if k:
                    k.validate()
        if self.save_property_values:
            for k in self.save_property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreatePropertyResponseBodyCreateResultSavePropertyValueModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedPropertyValues'] = []
        if self.failed_property_values is not None:
            for k in self.failed_property_values:
                result['FailedPropertyValues'].append(k.to_map() if k else None)
        result['SavePropertyValues'] = []
        if self.save_property_values is not None:
            for k in self.save_property_values:
                result['SavePropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_property_values = []
        if m.get('FailedPropertyValues') is not None:
            for k in m.get('FailedPropertyValues'):
                temp_model = CreatePropertyResponseBodyCreateResultSavePropertyValueModelFailedPropertyValues()
                self.failed_property_values.append(temp_model.from_map(k))
        self.save_property_values = []
        if m.get('SavePropertyValues') is not None:
            for k in m.get('SavePropertyValues'):
                temp_model = CreatePropertyResponseBodyCreateResultSavePropertyValueModelSavePropertyValues()
                self.save_property_values.append(temp_model.from_map(k))
        return self


class CreatePropertyResponseBodyCreateResult(TeaModel):
    def __init__(self, property_id=None, property_key=None, save_property_value_model=None):
        self.property_id = property_id  # type: long
        self.property_key = property_key  # type: str
        self.save_property_value_model = save_property_value_model  # type: CreatePropertyResponseBodyCreateResultSavePropertyValueModel

    def validate(self):
        if self.save_property_value_model:
            self.save_property_value_model.validate()

    def to_map(self):
        _map = super(CreatePropertyResponseBodyCreateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.save_property_value_model is not None:
            result['SavePropertyValueModel'] = self.save_property_value_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('SavePropertyValueModel') is not None:
            temp_model = CreatePropertyResponseBodyCreateResultSavePropertyValueModel()
            self.save_property_value_model = temp_model.from_map(m['SavePropertyValueModel'])
        return self


class CreatePropertyResponseBody(TeaModel):
    def __init__(self, create_result=None, request_id=None):
        self.create_result = create_result  # type: CreatePropertyResponseBodyCreateResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        _map = super(CreatePropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateResult') is not None:
            temp_model = CreatePropertyResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m['CreateResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePropertyResponse, self).to_map()
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
            temp_model = CreatePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUsersRequestUsers(TeaModel):
    def __init__(self, email=None, end_user_id=None, org_id=None, owner_type=None, password=None, phone=None,
                 real_nick_name=None, remark=None):
        # The email address of the end user. The email address is used to receive notifications about events such as desktop assignment. You must specify an email address or a mobile number to receive notifications.
        self.email = email  # type: str
        # The name of the end user. The name must be 3 to 24 characters in length, and can contain lowercase letters, digits, and underscores (\_).
        self.end_user_id = end_user_id  # type: str
        # The organization to which the end user belongs.
        self.org_id = org_id  # type: str
        # The type of the account ownership.
        self.owner_type = owner_type  # type: str
        # The password of the end user.
        self.password = password  # type: str
        # Mobile numbers are not supported on the international site (alibabacloud.com).
        self.phone = phone  # type: str
        self.real_nick_name = real_nick_name  # type: str
        # The remarks of the end user.
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUsersRequestUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.password is not None:
            result['Password'] = self.password
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateUsersRequest(TeaModel):
    def __init__(self, auto_lock_time=None, password=None, users=None):
        self.auto_lock_time = auto_lock_time  # type: str
        # The initial password. If this parameter is left empty, an email for password reset is sent to the specified email address.
        self.password = password  # type: str
        # Details of the convenience users.
        self.users = users  # type: list[CreateUsersRequestUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time
        if self.password is not None:
            result['Password'] = self.password
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = CreateUsersRequestUsers()
                self.users.append(temp_model.from_map(k))
        return self


class CreateUsersResponseBodyCreateResultCreatedUsers(TeaModel):
    def __init__(self, email=None, end_user_id=None, phone=None, real_nick_name=None, remark=None):
        # The email address of the end user.
        self.email = email  # type: str
        # The name of the end user.
        self.end_user_id = end_user_id  # type: str
        # The mobile number of the end user.
        self.phone = phone  # type: str
        self.real_nick_name = real_nick_name  # type: str
        # The remarks of the end user.
        self.remark = remark  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUsersResponseBodyCreateResultCreatedUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateUsersResponseBodyCreateResultFailedUsers(TeaModel):
    def __init__(self, email=None, end_user_id=None, error_code=None, error_message=None, phone=None):
        # The email address of the end user.
        self.email = email  # type: str
        # The name of the end user.
        self.end_user_id = end_user_id  # type: str
        # The error code returned if the request failed.
        self.error_code = error_code  # type: str
        # The error message returned.
        self.error_message = error_message  # type: str
        # The mobile number of the end user.
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUsersResponseBodyCreateResultFailedUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class CreateUsersResponseBodyCreateResult(TeaModel):
    def __init__(self, created_users=None, failed_users=None):
        # Details of the created convenience users.
        self.created_users = created_users  # type: list[CreateUsersResponseBodyCreateResultCreatedUsers]
        # Details of the convenience users that failed to be created.
        self.failed_users = failed_users  # type: list[CreateUsersResponseBodyCreateResultFailedUsers]

    def validate(self):
        if self.created_users:
            for k in self.created_users:
                if k:
                    k.validate()
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateUsersResponseBodyCreateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CreatedUsers'] = []
        if self.created_users is not None:
            for k in self.created_users:
                result['CreatedUsers'].append(k.to_map() if k else None)
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.created_users = []
        if m.get('CreatedUsers') is not None:
            for k in m.get('CreatedUsers'):
                temp_model = CreateUsersResponseBodyCreateResultCreatedUsers()
                self.created_users.append(temp_model.from_map(k))
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = CreateUsersResponseBodyCreateResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        return self


class CreateUsersResponseBody(TeaModel):
    def __init__(self, create_result=None, request_id=None):
        # The result of user creation.
        self.create_result = create_result  # type: CreateUsersResponseBodyCreateResult
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.create_result:
            self.create_result.validate()

    def to_map(self):
        _map = super(CreateUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_result is not None:
            result['CreateResult'] = self.create_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateResult') is not None:
            temp_model = CreateUsersResponseBodyCreateResult()
            self.create_result = temp_model.from_map(m['CreateResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUsersResponse, self).to_map()
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
            temp_model = CreateUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserPropertyValueRequest(TeaModel):
    def __init__(self, property_id=None, property_value_id=None, user_id=None):
        # DeleteUserPropertyValue
        self.property_id = property_id  # type: long
        self.property_value_id = property_value_id  # type: long
        # Dissociates a user property from a user.
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserPropertyValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserPropertyValueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserPropertyValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteUserPropertyValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserPropertyValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserPropertyValueResponse, self).to_map()
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
            temp_model = DeleteUserPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMfaDevicesRequest(TeaModel):
    def __init__(self, ad_domain=None, end_user_ids=None, max_results=None, next_token=None, serial_numbers=None):
        self.ad_domain = ad_domain  # type: str
        # The list of username of convenience users.
        self.end_user_ids = end_user_ids  # type: list[str]
        # The maximum number of entries to return. Valid values: 1 to 500.
        # 
        # Default value: 100.
        self.max_results = max_results  # type: long
        # The query token. Set the value to the NextToken value returned in the last call.
        self.next_token = next_token  # type: str
        # The list of serial numbers of the virtual MFA devices.
        self.serial_numbers = serial_numbers  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMfaDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.serial_numbers is not None:
            result['SerialNumbers'] = self.serial_numbers
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('SerialNumbers') is not None:
            self.serial_numbers = m.get('SerialNumbers')
        return self


class DescribeMfaDevicesResponseBodyMfaDevices(TeaModel):
    def __init__(self, consecutive_fails=None, device_type=None, email=None, end_user_id=None, gmt_enabled=None,
                 gmt_unlock=None, id=None, serial_number=None, status=None):
        # The number of consecutive failures to bind the virtual MFA device, or the number of MFA failures based on the virtual MFA device.
        self.consecutive_fails = consecutive_fails  # type: int
        # The types of the virtual MFA device. Set the value to TOTP_VIRTUAL, which indicates that the virtual MFA devices follow the Time-based One-time Password (TOTP) algorithm.
        self.device_type = device_type  # type: str
        # This parameter is unavailable.
        self.email = email  # type: str
        # The username of the convenience user that uses the virtual MFA device.
        self.end_user_id = end_user_id  # type: str
        # The time when the virtual MFA device was enabled. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_enabled = gmt_enabled  # type: str
        # The time when a locked virtual MFA device is automatically unlocked. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.gmt_unlock = gmt_unlock  # type: str
        # This parameter is unavailable.
        self.id = id  # type: long
        # The serial number of the virtual MFA device, which is a unique identifier.
        self.serial_number = serial_number  # type: str
        # The status of the virtual MFA device. Valid values:
        # 
        # *   UNBOUND
        # *   NORMAL
        # *   LOCKED
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMfaDevicesResponseBodyMfaDevices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consecutive_fails is not None:
            result['ConsecutiveFails'] = self.consecutive_fails
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.gmt_enabled is not None:
            result['GmtEnabled'] = self.gmt_enabled
        if self.gmt_unlock is not None:
            result['GmtUnlock'] = self.gmt_unlock
        if self.id is not None:
            result['Id'] = self.id
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConsecutiveFails') is not None:
            self.consecutive_fails = m.get('ConsecutiveFails')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('GmtEnabled') is not None:
            self.gmt_enabled = m.get('GmtEnabled')
        if m.get('GmtUnlock') is not None:
            self.gmt_unlock = m.get('GmtUnlock')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeMfaDevicesResponseBody(TeaModel):
    def __init__(self, mfa_devices=None, next_token=None, request_id=None):
        # Details about the virtual MFA devices.
        self.mfa_devices = mfa_devices  # type: list[DescribeMfaDevicesResponseBodyMfaDevices]
        # The token that determines the start point of the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.mfa_devices:
            for k in self.mfa_devices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMfaDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MfaDevices'] = []
        if self.mfa_devices is not None:
            for k in self.mfa_devices:
                result['MfaDevices'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mfa_devices = []
        if m.get('MfaDevices') is not None:
            for k in m.get('MfaDevices'):
                temp_model = DescribeMfaDevicesResponseBodyMfaDevices()
                self.mfa_devices.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeMfaDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMfaDevicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMfaDevicesResponse, self).to_map()
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
            temp_model = DescribeMfaDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUsersRequest(TeaModel):
    def __init__(self, biz_type=None, end_user_ids=None, exclude_end_user_ids=None, filter=None, group_id=None,
                 max_results=None, next_token=None, org_id=None, solution_id=None):
        self.biz_type = biz_type  # type: str
        # The list of usernames that must be exactly matched.
        self.end_user_ids = end_user_ids  # type: list[str]
        # The list of usernames to be exactly excluded.
        self.exclude_end_user_ids = exclude_end_user_ids  # type: list[str]
        # The string that is used for fuzzy search. You perform fuzzy search by username (EndUserId) and email address (Email). Wildcard characters (\*) are supported. For example, if you set this parameter to `a*m`, usernames or email addresses that start with `a` and end with `m` are returned.
        self.filter = filter  # type: str
        self.group_id = group_id  # type: str
        # The number of entries per page.
        # 
        # *   Valid values: 1 to 500
        # *   Default value: 500
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.\
        # If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the return value of NextToken to perform the next query.
        self.next_token = next_token  # type: str
        # The ID of the organization in which you want to query users.
        self.org_id = org_id  # type: str
        self.solution_id = solution_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.solution_id is not None:
            result['SolutionId'] = self.solution_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('SolutionId') is not None:
            self.solution_id = m.get('SolutionId')
        return self


class DescribeUsersResponseBodyUsersGroups(TeaModel):
    def __init__(self, group_id=None, group_name=None):
        self.group_id = group_id  # type: str
        self.group_name = group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsersResponseBodyUsersGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class DescribeUsersResponseBodyUsersOrgs(TeaModel):
    def __init__(self, org_id=None, org_name=None):
        self.org_id = org_id  # type: str
        self.org_name = org_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUsersResponseBodyUsersOrgs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.org_name is not None:
            result['OrgName'] = self.org_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OrgName') is not None:
            self.org_name = m.get('OrgName')
        return self


class DescribeUsersResponseBodyUsers(TeaModel):
    def __init__(self, address=None, avatar=None, email=None, end_user_id=None, groups=None, id=None,
                 is_tenant_manager=None, job_number=None, nick_name=None, org_id=None, orgs=None, owner_type=None, phone=None,
                 remark=None, status=None, wy_id=None):
        self.address = address  # type: str
        self.avatar = avatar  # type: str
        # The email address.
        self.email = email  # type: str
        # The name of the user.
        self.end_user_id = end_user_id  # type: str
        self.groups = groups  # type: list[DescribeUsersResponseBodyUsersGroups]
        # The ID of the user.
        self.id = id  # type: long
        # Indicates whether the user is an administrator. If the convenience user is of the administrator-activated type, you must specify a user administrator. Notifications such as password reset on a client are sent to the email address or mobile phone of the user administrator. For more information, see [Create a convenience user](~~214472~~).
        self.is_tenant_manager = is_tenant_manager  # type: bool
        self.job_number = job_number  # type: str
        # The nickname of the user.
        self.nick_name = nick_name  # type: str
        # The ID of the organization to which the user belongs.
        self.org_id = org_id  # type: str
        self.orgs = orgs  # type: list[DescribeUsersResponseBodyUsersOrgs]
        # The type of the convenience account.
        # 
        # *   The administrator-activated type. The administrator specifies the username and the password of the convenience account. User notifications such as password reset are sent to the email address or mobile number of the administrator.
        # *   The user-activated type. The administrator specifies the username and the email address or mobile number of a user. Activation notifications are sent to the email address or mobile number of the user.
        # 
        # Valid values:
        # 
        # *   CreateFromManager
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     administrator-activated
        # 
        #     <!-- -->
        # 
        # *   Normal: user-activated
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.owner_type = owner_type  # type: str
        # The mobile number of the user. If you leave this parameter empty, the value of this parameter is not returned.
        self.phone = phone  # type: str
        # The remarks on the user.
        self.remark = remark  # type: str
        # The status of the user.
        self.status = status  # type: long
        # The user ID that is globally unique.
        self.wy_id = wy_id  # type: str

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()
        if self.orgs:
            for k in self.orgs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.id is not None:
            result['Id'] = self.id
        if self.is_tenant_manager is not None:
            result['IsTenantManager'] = self.is_tenant_manager
        if self.job_number is not None:
            result['JobNumber'] = self.job_number
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        result['Orgs'] = []
        if self.orgs is not None:
            for k in self.orgs:
                result['Orgs'].append(k.to_map() if k else None)
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        if self.wy_id is not None:
            result['WyId'] = self.wy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = DescribeUsersResponseBodyUsersGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsTenantManager') is not None:
            self.is_tenant_manager = m.get('IsTenantManager')
        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        self.orgs = []
        if m.get('Orgs') is not None:
            for k in m.get('Orgs'):
                temp_model = DescribeUsersResponseBodyUsersOrgs()
                self.orgs.append(temp_model.from_map(k))
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')
        return self


class DescribeUsersResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, users=None):
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        # Details of the convenience users.
        self.users = users  # type: list[DescribeUsersResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = DescribeUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class DescribeUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUsersResponse, self).to_map()
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
            temp_model = DescribeUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FilterUsersRequestOrderParam(TeaModel):
    def __init__(self, order_field=None, order_type=None):
        # The way to sort query results.
        # 
        # Valid values:
        # 
        # *   EndUserId
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   id
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   gmt_created
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.order_field = order_field  # type: str
        # Specifies whether to sort query results in ascending or descending order. Valid values:
        # 
        # Valid values:
        # 
        # *   ASC: ascending
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DESC (default): descending
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.order_type = order_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersRequestOrderParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_field is not None:
            result['OrderField'] = self.order_field
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        return self


class FilterUsersRequestPropertyFilterParam(TeaModel):
    def __init__(self, property_id=None, property_value_ids=None):
        # The ID of the property.
        self.property_id = property_id  # type: long
        # The IDs of the property values.
        self.property_value_ids = property_value_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersRequestPropertyFilterParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_ids is not None:
            result['PropertyValueIds'] = self.property_value_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueIds') is not None:
            self.property_value_ids = m.get('PropertyValueIds')
        return self


class FilterUsersRequestPropertyKeyValueFilterParam(TeaModel):
    def __init__(self, property_key=None, property_values=None):
        # The property name.
        self.property_key = property_key  # type: str
        # The property values.
        self.property_values = property_values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersRequestPropertyKeyValueFilterParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')
        return self


class FilterUsersRequest(TeaModel):
    def __init__(self, exclude_end_user_ids=None, filter=None, include_desktop_count=None,
                 include_desktop_group_count=None, max_results=None, next_token=None, order_param=None, org_id=None, owner_type=None,
                 property_filter_param=None, property_key_value_filter_param=None):
        # The list of usernames to be precisely excluded.
        self.exclude_end_user_ids = exclude_end_user_ids  # type: list[str]
        # The string that is used for fuzzy search. You can use usernames and email addresses to perform fuzzy search. Wildcard characters (\*) are supported for this parameter. For example, if you set this parameter to a\*m, the usernames or an email addresses that start with a or end with m are returned.
        self.filter = filter  # type: str
        # Specifies whether to return information about cloud desktops that are assigned to the convenience user.
        self.include_desktop_count = include_desktop_count  # type: bool
        # Specifies whether to return the number of desktop groups that are assigned to the user.
        self.include_desktop_group_count = include_desktop_group_count  # type: bool
        # The number of entries per page. If you set this parameter to a value greater than 100, the system resets the value to 100.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token  # type: str
        # The parameter that supports to sort query results.
        self.order_param = order_param  # type: FilterUsersRequestOrderParam
        # The ID of the organization.
        self.org_id = org_id  # type: str
        # The type of the account ownership.
        self.owner_type = owner_type  # type: str
        # The list of properties for fuzzy search.
        self.property_filter_param = property_filter_param  # type: list[FilterUsersRequestPropertyFilterParam]
        # The list of property names and property values.
        self.property_key_value_filter_param = property_key_value_filter_param  # type: list[FilterUsersRequestPropertyKeyValueFilterParam]

    def validate(self):
        if self.order_param:
            self.order_param.validate()
        if self.property_filter_param:
            for k in self.property_filter_param:
                if k:
                    k.validate()
        if self.property_key_value_filter_param:
            for k in self.property_key_value_filter_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FilterUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.include_desktop_count is not None:
            result['IncludeDesktopCount'] = self.include_desktop_count
        if self.include_desktop_group_count is not None:
            result['IncludeDesktopGroupCount'] = self.include_desktop_group_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_param is not None:
            result['OrderParam'] = self.order_param.to_map()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['PropertyFilterParam'] = []
        if self.property_filter_param is not None:
            for k in self.property_filter_param:
                result['PropertyFilterParam'].append(k.to_map() if k else None)
        result['PropertyKeyValueFilterParam'] = []
        if self.property_key_value_filter_param is not None:
            for k in self.property_key_value_filter_param:
                result['PropertyKeyValueFilterParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IncludeDesktopCount') is not None:
            self.include_desktop_count = m.get('IncludeDesktopCount')
        if m.get('IncludeDesktopGroupCount') is not None:
            self.include_desktop_group_count = m.get('IncludeDesktopGroupCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderParam') is not None:
            temp_model = FilterUsersRequestOrderParam()
            self.order_param = temp_model.from_map(m['OrderParam'])
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.property_filter_param = []
        if m.get('PropertyFilterParam') is not None:
            for k in m.get('PropertyFilterParam'):
                temp_model = FilterUsersRequestPropertyFilterParam()
                self.property_filter_param.append(temp_model.from_map(k))
        self.property_key_value_filter_param = []
        if m.get('PropertyKeyValueFilterParam') is not None:
            for k in m.get('PropertyKeyValueFilterParam'):
                temp_model = FilterUsersRequestPropertyKeyValueFilterParam()
                self.property_key_value_filter_param.append(temp_model.from_map(k))
        return self


class FilterUsersShrinkRequestPropertyFilterParam(TeaModel):
    def __init__(self, property_id=None, property_value_ids=None):
        # The ID of the property.
        self.property_id = property_id  # type: long
        # The IDs of the property values.
        self.property_value_ids = property_value_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersShrinkRequestPropertyFilterParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_ids is not None:
            result['PropertyValueIds'] = self.property_value_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueIds') is not None:
            self.property_value_ids = m.get('PropertyValueIds')
        return self


class FilterUsersShrinkRequestPropertyKeyValueFilterParam(TeaModel):
    def __init__(self, property_key=None, property_values=None):
        # The property name.
        self.property_key = property_key  # type: str
        # The property values.
        self.property_values = property_values  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersShrinkRequestPropertyKeyValueFilterParam, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_values is not None:
            result['PropertyValues'] = self.property_values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyValues') is not None:
            self.property_values = m.get('PropertyValues')
        return self


class FilterUsersShrinkRequest(TeaModel):
    def __init__(self, exclude_end_user_ids=None, filter=None, include_desktop_count=None,
                 include_desktop_group_count=None, max_results=None, next_token=None, order_param_shrink=None, org_id=None, owner_type=None,
                 property_filter_param=None, property_key_value_filter_param=None):
        # The list of usernames to be precisely excluded.
        self.exclude_end_user_ids = exclude_end_user_ids  # type: list[str]
        # The string that is used for fuzzy search. You can use usernames and email addresses to perform fuzzy search. Wildcard characters (\*) are supported for this parameter. For example, if you set this parameter to a\*m, the usernames or an email addresses that start with a or end with m are returned.
        self.filter = filter  # type: str
        # Specifies whether to return information about cloud desktops that are assigned to the convenience user.
        self.include_desktop_count = include_desktop_count  # type: bool
        # Specifies whether to return the number of desktop groups that are assigned to the user.
        self.include_desktop_group_count = include_desktop_group_count  # type: bool
        # The number of entries per page. If you set this parameter to a value greater than 100, the system resets the value to 100.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token  # type: str
        # The parameter that supports to sort query results.
        self.order_param_shrink = order_param_shrink  # type: str
        # The ID of the organization.
        self.org_id = org_id  # type: str
        # The type of the account ownership.
        self.owner_type = owner_type  # type: str
        # The list of properties for fuzzy search.
        self.property_filter_param = property_filter_param  # type: list[FilterUsersShrinkRequestPropertyFilterParam]
        # The list of property names and property values.
        self.property_key_value_filter_param = property_key_value_filter_param  # type: list[FilterUsersShrinkRequestPropertyKeyValueFilterParam]

    def validate(self):
        if self.property_filter_param:
            for k in self.property_filter_param:
                if k:
                    k.validate()
        if self.property_key_value_filter_param:
            for k in self.property_key_value_filter_param:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FilterUsersShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_end_user_ids is not None:
            result['ExcludeEndUserIds'] = self.exclude_end_user_ids
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.include_desktop_count is not None:
            result['IncludeDesktopCount'] = self.include_desktop_count
        if self.include_desktop_group_count is not None:
            result['IncludeDesktopGroupCount'] = self.include_desktop_group_count
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.order_param_shrink is not None:
            result['OrderParam'] = self.order_param_shrink
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        result['PropertyFilterParam'] = []
        if self.property_filter_param is not None:
            for k in self.property_filter_param:
                result['PropertyFilterParam'].append(k.to_map() if k else None)
        result['PropertyKeyValueFilterParam'] = []
        if self.property_key_value_filter_param is not None:
            for k in self.property_key_value_filter_param:
                result['PropertyKeyValueFilterParam'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeEndUserIds') is not None:
            self.exclude_end_user_ids = m.get('ExcludeEndUserIds')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('IncludeDesktopCount') is not None:
            self.include_desktop_count = m.get('IncludeDesktopCount')
        if m.get('IncludeDesktopGroupCount') is not None:
            self.include_desktop_group_count = m.get('IncludeDesktopGroupCount')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('OrderParam') is not None:
            self.order_param_shrink = m.get('OrderParam')
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        self.property_filter_param = []
        if m.get('PropertyFilterParam') is not None:
            for k in m.get('PropertyFilterParam'):
                temp_model = FilterUsersShrinkRequestPropertyFilterParam()
                self.property_filter_param.append(temp_model.from_map(k))
        self.property_key_value_filter_param = []
        if m.get('PropertyKeyValueFilterParam') is not None:
            for k in m.get('PropertyKeyValueFilterParam'):
                temp_model = FilterUsersShrinkRequestPropertyKeyValueFilterParam()
                self.property_key_value_filter_param.append(temp_model.from_map(k))
        return self


class FilterUsersResponseBodyUsersExternalInfo(TeaModel):
    def __init__(self, external_name=None, job_number=None):
        # The account that is connected to the user.
        self.external_name = external_name  # type: str
        # The account, student ID, or employee ID that is connected to the user.
        self.job_number = job_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersResponseBodyUsersExternalInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.external_name is not None:
            result['ExternalName'] = self.external_name
        if self.job_number is not None:
            result['JobNumber'] = self.job_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExternalName') is not None:
            self.external_name = m.get('ExternalName')
        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')
        return self


class FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues(TeaModel):
    def __init__(self, property_value=None, property_value_id=None):
        # The property value.
        self.property_value = property_value  # type: str
        # The property value ID.
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class FilterUsersResponseBodyUsersUserSetPropertiesModels(TeaModel):
    def __init__(self, property_id=None, property_key=None, property_type=None, property_values=None, user_id=None,
                 user_name=None):
        # The property ID.
        self.property_id = property_id  # type: long
        # The property name.
        self.property_key = property_key  # type: str
        # The property ID.
        self.property_type = property_type  # type: int
        # The property value.
        self.property_values = property_values  # type: list[FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues]
        # The ID of the user that is bound to the property.
        self.user_id = user_id  # type: long
        # The name of the user that is bound to the property.
        self.user_name = user_name  # type: str

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FilterUsersResponseBodyUsersUserSetPropertiesModels, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.property_type is not None:
            result['PropertyType'] = self.property_type
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('PropertyType') is not None:
            self.property_type = m.get('PropertyType')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = FilterUsersResponseBodyUsersUserSetPropertiesModelsPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class FilterUsersResponseBodyUsers(TeaModel):
    def __init__(self, desktop_count=None, desktop_group_count=None, email=None, enable_admin_access=None,
                 end_user_id=None, external_info=None, id=None, is_tenant_manager=None, owner_type=None, phone=None,
                 real_nick_name=None, remark=None, status=None, user_set_properties_models=None):
        # The number of cloud desktops that are assigned to the user.
        self.desktop_count = desktop_count  # type: long
        # The number of authorized desktop groups that are owned by the user. This value is returned if you set `IncludeDesktopGroupCount` to `true`.
        self.desktop_group_count = desktop_group_count  # type: long
        # The email address.
        self.email = email  # type: str
        # Indicates whether the user is a local administrator.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.enable_admin_access = enable_admin_access  # type: bool
        # The username.
        self.end_user_id = end_user_id  # type: str
        # The additional information about the user.
        self.external_info = external_info  # type: FilterUsersResponseBodyUsersExternalInfo
        # The user ID.
        self.id = id  # type: long
        # Indicates whether the user is a tenant administrator.
        # 
        # Valid values:
        # 
        # *   true
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   false
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.is_tenant_manager = is_tenant_manager  # type: bool
        # The type of the account ownership.
        # 
        # Valid values:
        # 
        # *   CreateFromManager
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     administrator-activated
        # 
        #     <!-- -->
        # 
        # *   Normal
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     user-activated
        # 
        #     <!-- -->
        self.owner_type = owner_type  # type: str
        # The mobile number.
        self.phone = phone  # type: str
        self.real_nick_name = real_nick_name  # type: str
        # The remarks.
        self.remark = remark  # type: str
        # The user status.
        # 
        # Valid values:
        # 
        # *   0: The user status is normal.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   9: The user is locked.
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.status = status  # type: long
        # Details of the properties.
        self.user_set_properties_models = user_set_properties_models  # type: list[FilterUsersResponseBodyUsersUserSetPropertiesModels]

    def validate(self):
        if self.external_info:
            self.external_info.validate()
        if self.user_set_properties_models:
            for k in self.user_set_properties_models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FilterUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desktop_count is not None:
            result['DesktopCount'] = self.desktop_count
        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count
        if self.email is not None:
            result['Email'] = self.email
        if self.enable_admin_access is not None:
            result['EnableAdminAccess'] = self.enable_admin_access
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.external_info is not None:
            result['ExternalInfo'] = self.external_info.to_map()
        if self.id is not None:
            result['Id'] = self.id
        if self.is_tenant_manager is not None:
            result['IsTenantManager'] = self.is_tenant_manager
        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.status is not None:
            result['Status'] = self.status
        result['UserSetPropertiesModels'] = []
        if self.user_set_properties_models is not None:
            for k in self.user_set_properties_models:
                result['UserSetPropertiesModels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DesktopCount') is not None:
            self.desktop_count = m.get('DesktopCount')
        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EnableAdminAccess') is not None:
            self.enable_admin_access = m.get('EnableAdminAccess')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ExternalInfo') is not None:
            temp_model = FilterUsersResponseBodyUsersExternalInfo()
            self.external_info = temp_model.from_map(m['ExternalInfo'])
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsTenantManager') is not None:
            self.is_tenant_manager = m.get('IsTenantManager')
        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.user_set_properties_models = []
        if m.get('UserSetPropertiesModels') is not None:
            for k in m.get('UserSetPropertiesModels'):
                temp_model = FilterUsersResponseBodyUsersUserSetPropertiesModels()
                self.user_set_properties_models.append(temp_model.from_map(k))
        return self


class FilterUsersResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, users=None):
        # The pagination token that is used in the next request to retrieve a new page of results. If not all results are returned in a query, a value is returned for the NextToken parameter. In this case, you can use the returned NextToken value to start the next query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # Details of the convenience users.
        self.users = users  # type: list[FilterUsersResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(FilterUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = FilterUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class FilterUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FilterUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FilterUsersResponse, self).to_map()
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
            temp_model = FilterUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetManagerInfoByAuthCodeRequest(TeaModel):
    def __init__(self, auth_code=None):
        self.auth_code = auth_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetManagerInfoByAuthCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        return self


class GetManagerInfoByAuthCodeResponseBody(TeaModel):
    def __init__(self, org_id=None, phone=None, request_id=None, team_name=None, user_name=None, wa_id=None):
        self.org_id = org_id  # type: str
        self.phone = phone  # type: str
        self.request_id = request_id  # type: str
        self.team_name = team_name  # type: str
        self.user_name = user_name  # type: str
        self.wa_id = wa_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetManagerInfoByAuthCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.org_id is not None:
            result['OrgId'] = self.org_id
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.team_name is not None:
            result['TeamName'] = self.team_name
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.wa_id is not None:
            result['WaId'] = self.wa_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TeamName') is not None:
            self.team_name = m.get('TeamName')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('WaId') is not None:
            self.wa_id = m.get('WaId')
        return self


class GetManagerInfoByAuthCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetManagerInfoByAuthCodeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetManagerInfoByAuthCodeResponse, self).to_map()
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
            temp_model = GetManagerInfoByAuthCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPropertyResponseBodyPropertiesPropertyValues(TeaModel):
    def __init__(self, property_value=None, property_value_id=None):
        # The value of the property.
        self.property_value = property_value  # type: str
        # The ID of the property value.
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPropertyResponseBodyPropertiesPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class ListPropertyResponseBodyProperties(TeaModel):
    def __init__(self, property_id=None, property_key=None, property_values=None):
        # The ID of the property.
        self.property_id = property_id  # type: long
        # The name of the property.
        self.property_key = property_key  # type: str
        # Details about the property values.
        self.property_values = property_values  # type: list[ListPropertyResponseBodyPropertiesPropertyValues]

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPropertyResponseBodyProperties, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = ListPropertyResponseBodyPropertiesPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        return self


class ListPropertyResponseBody(TeaModel):
    def __init__(self, next_token=None, properties=None, request_id=None):
        # The token that is used for the next query. If this parameter is empty, all results have been returned.
        self.next_token = next_token  # type: str
        # The information about the properties.
        self.properties = properties  # type: list[ListPropertyResponseBodyProperties]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Properties'] = []
        if self.properties is not None:
            for k in self.properties:
                result['Properties'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.properties = []
        if m.get('Properties') is not None:
            for k in m.get('Properties'):
                temp_model = ListPropertyResponseBodyProperties()
                self.properties.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPropertyResponse, self).to_map()
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
            temp_model = ListPropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPropertyValueRequest(TeaModel):
    def __init__(self, property_id=None):
        # The ID of the property. You can call the [ListProperty](~~410890~~) operation to query the property ID.
        self.property_id = property_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPropertyValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class ListPropertyValueResponseBodyPropertyValueInfos(TeaModel):
    def __init__(self, property_value=None, property_value_id=None):
        # The value of the property.
        self.property_value = property_value  # type: str
        # The ID of the property value.
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPropertyValueResponseBodyPropertyValueInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class ListPropertyValueResponseBody(TeaModel):
    def __init__(self, property_value_infos=None, request_id=None):
        # Details about property values.
        self.property_value_infos = property_value_infos  # type: list[ListPropertyValueResponseBodyPropertyValueInfos]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.property_value_infos:
            for k in self.property_value_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPropertyValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PropertyValueInfos'] = []
        if self.property_value_infos is not None:
            for k in self.property_value_infos:
                result['PropertyValueInfos'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.property_value_infos = []
        if m.get('PropertyValueInfos') is not None:
            for k in m.get('PropertyValueInfos'):
                temp_model = ListPropertyValueResponseBodyPropertyValueInfos()
                self.property_value_infos.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPropertyValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPropertyValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPropertyValueResponse, self).to_map()
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
            temp_model = ListPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockMfaDeviceRequest(TeaModel):
    def __init__(self, ad_domain=None, serial_number=None):
        # The address of the Active Directory (AD) workspace.
        self.ad_domain = ad_domain  # type: str
        # The serial number of the virtual MFA device, which is a unique identifier.
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockMfaDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class LockMfaDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockMfaDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LockMfaDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockMfaDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockMfaDeviceResponse, self).to_map()
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
            temp_model = LockMfaDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockUsersRequest(TeaModel):
    def __init__(self, users=None):
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class LockUsersResponseBodyLockUsersResultFailedUsers(TeaModel):
    def __init__(self, end_user_id=None, error_code=None, error_message=None):
        self.end_user_id = end_user_id  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockUsersResponseBodyLockUsersResultFailedUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class LockUsersResponseBodyLockUsersResult(TeaModel):
    def __init__(self, failed_users=None, locked_users=None):
        self.failed_users = failed_users  # type: list[LockUsersResponseBodyLockUsersResultFailedUsers]
        self.locked_users = locked_users  # type: list[str]

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LockUsersResponseBodyLockUsersResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.locked_users is not None:
            result['LockedUsers'] = self.locked_users
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = LockUsersResponseBodyLockUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('LockedUsers') is not None:
            self.locked_users = m.get('LockedUsers')
        return self


class LockUsersResponseBody(TeaModel):
    def __init__(self, lock_users_result=None, request_id=None):
        self.lock_users_result = lock_users_result  # type: LockUsersResponseBodyLockUsersResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.lock_users_result:
            self.lock_users_result.validate()

    def to_map(self):
        _map = super(LockUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_users_result is not None:
            result['LockUsersResult'] = self.lock_users_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LockUsersResult') is not None:
            temp_model = LockUsersResponseBodyLockUsersResult()
            self.lock_users_result = temp_model.from_map(m['LockUsersResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LockUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockUsersResponse, self).to_map()
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
            temp_model = LockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserRequest(TeaModel):
    def __init__(self, email=None, end_user_id=None, phone=None):
        self.email = email  # type: str
        self.end_user_id = end_user_id  # type: str
        self.phone = phone  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['Email'] = self.email
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.phone is not None:
            result['Phone'] = self.phone
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        return self


class ModifyUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserResponse, self).to_map()
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
            temp_model = ModifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySyncStatusByAliUidResponseBodyData(TeaModel):
    def __init__(self, ali_uid=None, corp_id=None, gmt_created=None, gmt_modified=None, id=None,
                 latest_begin_time=None, latest_end_time=None, latest_success_time=None, status=None):
        self.ali_uid = ali_uid  # type: long
        self.corp_id = corp_id  # type: str
        self.gmt_created = gmt_created  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.id = id  # type: long
        self.latest_begin_time = latest_begin_time  # type: str
        self.latest_end_time = latest_end_time  # type: str
        self.latest_success_time = latest_success_time  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySyncStatusByAliUidResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id
        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.latest_begin_time is not None:
            result['LatestBeginTime'] = self.latest_begin_time
        if self.latest_end_time is not None:
            result['LatestEndTime'] = self.latest_end_time
        if self.latest_success_time is not None:
            result['LatestSuccessTime'] = self.latest_success_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')
        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LatestBeginTime') is not None:
            self.latest_begin_time = m.get('LatestBeginTime')
        if m.get('LatestEndTime') is not None:
            self.latest_end_time = m.get('LatestEndTime')
        if m.get('LatestSuccessTime') is not None:
            self.latest_success_time = m.get('LatestSuccessTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QuerySyncStatusByAliUidResponseBody(TeaModel):
    def __init__(self, code=None, data=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QuerySyncStatusByAliUidResponseBodyData
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QuerySyncStatusByAliUidResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
            temp_model = QuerySyncStatusByAliUidResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QuerySyncStatusByAliUidResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySyncStatusByAliUidResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySyncStatusByAliUidResponse, self).to_map()
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
            temp_model = QuerySyncStatusByAliUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMfaDeviceRequest(TeaModel):
    def __init__(self, ad_domain=None, serial_number=None):
        self.ad_domain = ad_domain  # type: str
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMfaDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class RemoveMfaDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveMfaDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveMfaDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveMfaDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveMfaDeviceResponse, self).to_map()
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
            temp_model = RemoveMfaDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemovePropertyRequest(TeaModel):
    def __init__(self, property_id=None):
        self.property_id = property_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemovePropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        return self


class RemovePropertyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemovePropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemovePropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemovePropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemovePropertyResponse, self).to_map()
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
            temp_model = RemovePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersRequest(TeaModel):
    def __init__(self, users=None):
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class RemoveUsersResponseBodyRemoveUsersResultFailedUsers(TeaModel):
    def __init__(self, end_user_id=None, error_code=None, error_message=None):
        self.end_user_id = end_user_id  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUsersResponseBodyRemoveUsersResultFailedUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class RemoveUsersResponseBodyRemoveUsersResult(TeaModel):
    def __init__(self, failed_users=None, removed_users=None):
        self.failed_users = failed_users  # type: list[RemoveUsersResponseBodyRemoveUsersResultFailedUsers]
        self.removed_users = removed_users  # type: list[str]

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveUsersResponseBodyRemoveUsersResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.removed_users is not None:
            result['RemovedUsers'] = self.removed_users
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = RemoveUsersResponseBodyRemoveUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('RemovedUsers') is not None:
            self.removed_users = m.get('RemovedUsers')
        return self


class RemoveUsersResponseBody(TeaModel):
    def __init__(self, remove_users_result=None, request_id=None):
        self.remove_users_result = remove_users_result  # type: RemoveUsersResponseBodyRemoveUsersResult
        self.request_id = request_id  # type: str

    def validate(self):
        if self.remove_users_result:
            self.remove_users_result.validate()

    def to_map(self):
        _map = super(RemoveUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.remove_users_result is not None:
            result['RemoveUsersResult'] = self.remove_users_result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RemoveUsersResult') is not None:
            temp_model = RemoveUsersResponseBodyRemoveUsersResult()
            self.remove_users_result = temp_model.from_map(m['RemoveUsersResult'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUsersResponse, self).to_map()
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
            temp_model = RemoveUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetUserPasswordRequest(TeaModel):
    def __init__(self, notify_type=None, users=None):
        # The method to notify the user after the password is reset.
        self.notify_type = notify_type  # type: int
        # The names of the convenience users whose passwords you want to reset.
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetUserPasswordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_type is not None:
            result['NotifyType'] = self.notify_type
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NotifyType') is not None:
            self.notify_type = m.get('NotifyType')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class ResetUserPasswordResponseBodyResetUsersResultFailedUsers(TeaModel):
    def __init__(self, end_user_id=None, error_code=None, error_message=None):
        # The ID of the convenience user whose password failed to be reset.
        self.end_user_id = end_user_id  # type: str
        # The error code.
        self.error_code = error_code  # type: str
        # The error message.
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetUserPasswordResponseBodyResetUsersResultFailedUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class ResetUserPasswordResponseBodyResetUsersResult(TeaModel):
    def __init__(self, failed_users=None, reset_users=None):
        # The information about the convenience users whose passwords failed to be reset.
        self.failed_users = failed_users  # type: list[ResetUserPasswordResponseBodyResetUsersResultFailedUsers]
        # The convenience users to which the system sent a password reset email.
        self.reset_users = reset_users  # type: list[str]

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ResetUserPasswordResponseBodyResetUsersResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.reset_users is not None:
            result['ResetUsers'] = self.reset_users
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = ResetUserPasswordResponseBodyResetUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('ResetUsers') is not None:
            self.reset_users = m.get('ResetUsers')
        return self


class ResetUserPasswordResponseBody(TeaModel):
    def __init__(self, request_id=None, reset_users_result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of resetting the password of the convenience user.
        self.reset_users_result = reset_users_result  # type: ResetUserPasswordResponseBodyResetUsersResult

    def validate(self):
        if self.reset_users_result:
            self.reset_users_result.validate()

    def to_map(self):
        _map = super(ResetUserPasswordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.reset_users_result is not None:
            result['ResetUsersResult'] = self.reset_users_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResetUsersResult') is not None:
            temp_model = ResetUserPasswordResponseBodyResetUsersResult()
            self.reset_users_result = temp_model.from_map(m['ResetUsersResult'])
        return self


class ResetUserPasswordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetUserPasswordResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetUserPasswordResponse, self).to_map()
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
            temp_model = ResetUserPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserPropertyValueRequest(TeaModel):
    def __init__(self, property_id=None, property_value_id=None, user_id=None, user_name=None):
        self.property_id = property_id  # type: long
        self.property_value_id = property_value_id  # type: long
        # Associates a user property with a user.
        self.user_id = user_id  # type: long
        # SetUserPropertyValue
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserPropertyValueRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class SetUserPropertyValueResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetUserPropertyValueResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetUserPropertyValueResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetUserPropertyValueResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetUserPropertyValueResponse, self).to_map()
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
            temp_model = SetUserPropertyValueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncAllEduInfoResponseBody(TeaModel):
    def __init__(self, code=None, http_status_code=None, message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.http_status_code = http_status_code  # type: int
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SyncAllEduInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SyncAllEduInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SyncAllEduInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SyncAllEduInfoResponse, self).to_map()
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
            temp_model = SyncAllEduInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockMfaDeviceRequest(TeaModel):
    def __init__(self, ad_domain=None, serial_number=None):
        # The address of the Active Directory (AD) workspace.
        self.ad_domain = ad_domain  # type: str
        # The serial number of the virtual MFA device, which is a unique identifier.
        self.serial_number = serial_number  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockMfaDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad_domain is not None:
            result['AdDomain'] = self.ad_domain
        if self.serial_number is not None:
            result['SerialNumber'] = self.serial_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdDomain') is not None:
            self.ad_domain = m.get('AdDomain')
        if m.get('SerialNumber') is not None:
            self.serial_number = m.get('SerialNumber')
        return self


class UnlockMfaDeviceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockMfaDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnlockMfaDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockMfaDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockMfaDeviceResponse, self).to_map()
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
            temp_model = UnlockMfaDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUsersRequest(TeaModel):
    def __init__(self, auto_lock_time=None, users=None):
        self.auto_lock_time = auto_lock_time  # type: str
        self.users = users  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_lock_time is not None:
            result['AutoLockTime'] = self.auto_lock_time
        if self.users is not None:
            result['Users'] = self.users
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoLockTime') is not None:
            self.auto_lock_time = m.get('AutoLockTime')
        if m.get('Users') is not None:
            self.users = m.get('Users')
        return self


class UnlockUsersResponseBodyUnlockUsersResultFailedUsers(TeaModel):
    def __init__(self, end_user_id=None, error_code=None, error_message=None):
        self.end_user_id = end_user_id  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockUsersResponseBodyUnlockUsersResultFailedUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        return self


class UnlockUsersResponseBodyUnlockUsersResult(TeaModel):
    def __init__(self, failed_users=None, unlocked_users=None):
        self.failed_users = failed_users  # type: list[UnlockUsersResponseBodyUnlockUsersResultFailedUsers]
        self.unlocked_users = unlocked_users  # type: list[str]

    def validate(self):
        if self.failed_users:
            for k in self.failed_users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnlockUsersResponseBodyUnlockUsersResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k in self.failed_users:
                result['FailedUsers'].append(k.to_map() if k else None)
        if self.unlocked_users is not None:
            result['UnlockedUsers'] = self.unlocked_users
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k in m.get('FailedUsers'):
                temp_model = UnlockUsersResponseBodyUnlockUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k))
        if m.get('UnlockedUsers') is not None:
            self.unlocked_users = m.get('UnlockedUsers')
        return self


class UnlockUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, unlock_users_result=None):
        self.request_id = request_id  # type: str
        self.unlock_users_result = unlock_users_result  # type: UnlockUsersResponseBodyUnlockUsersResult

    def validate(self):
        if self.unlock_users_result:
            self.unlock_users_result.validate()

    def to_map(self):
        _map = super(UnlockUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.unlock_users_result is not None:
            result['UnlockUsersResult'] = self.unlock_users_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UnlockUsersResult') is not None:
            temp_model = UnlockUsersResponseBodyUnlockUsersResult()
            self.unlock_users_result = temp_model.from_map(m['UnlockUsersResult'])
        return self


class UnlockUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockUsersResponse, self).to_map()
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
            temp_model = UnlockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePropertyRequestPropertyValues(TeaModel):
    def __init__(self, property_value=None, property_value_id=None):
        # The new property value.
        self.property_value = property_value  # type: str
        # The ID of property value that you want to modify. You can call the [ListProperty](~~410890~~) operation to query the property value ID.
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePropertyRequestPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class UpdatePropertyRequest(TeaModel):
    def __init__(self, property_id=None, property_key=None, property_values=None):
        # The ID of the property that you want to modify. You can call the [ListProperty](~~410890~~) operation to query the property ID.
        self.property_id = property_id  # type: long
        # The new property name.
        self.property_key = property_key  # type: str
        # The values of property.
        self.property_values = property_values  # type: list[UpdatePropertyRequestPropertyValues]

    def validate(self):
        if self.property_values:
            for k in self.property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePropertyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        result['PropertyValues'] = []
        if self.property_values is not None:
            for k in self.property_values:
                result['PropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        self.property_values = []
        if m.get('PropertyValues') is not None:
            for k in m.get('PropertyValues'):
                temp_model = UpdatePropertyRequestPropertyValues()
                self.property_values.append(temp_model.from_map(k))
        return self


class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues(TeaModel):
    def __init__(self, error_code=None, error_message=None, property_id=None, property_value=None):
        # The error code.
        self.error_code = error_code  # type: str
        # The error message.
        self.error_message = error_message  # type: str
        # The ID of the property.
        self.property_id = property_id  # type: long
        # The value of the property.
        self.property_value = property_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        return self


class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues(TeaModel):
    def __init__(self, property_value=None, property_value_id=None):
        # The value of the property.
        self.property_value = property_value  # type: str
        # The ID of the property value.
        self.property_value_id = property_value_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_value is not None:
            result['PropertyValue'] = self.property_value
        if self.property_value_id is not None:
            result['PropertyValueId'] = self.property_value_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyValue') is not None:
            self.property_value = m.get('PropertyValue')
        if m.get('PropertyValueId') is not None:
            self.property_value_id = m.get('PropertyValueId')
        return self


class UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel(TeaModel):
    def __init__(self, failed_property_values=None, save_property_values=None):
        # The property values that failed to be modified.
        self.failed_property_values = failed_property_values  # type: list[UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues]
        # The property values that were modified.
        self.save_property_values = save_property_values  # type: list[UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues]

    def validate(self):
        if self.failed_property_values:
            for k in self.failed_property_values:
                if k:
                    k.validate()
        if self.save_property_values:
            for k in self.save_property_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedPropertyValues'] = []
        if self.failed_property_values is not None:
            for k in self.failed_property_values:
                result['FailedPropertyValues'].append(k.to_map() if k else None)
        result['SavePropertyValues'] = []
        if self.save_property_values is not None:
            for k in self.save_property_values:
                result['SavePropertyValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_property_values = []
        if m.get('FailedPropertyValues') is not None:
            for k in m.get('FailedPropertyValues'):
                temp_model = UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelFailedPropertyValues()
                self.failed_property_values.append(temp_model.from_map(k))
        self.save_property_values = []
        if m.get('SavePropertyValues') is not None:
            for k in m.get('SavePropertyValues'):
                temp_model = UpdatePropertyResponseBodyUpdateResultSavePropertyValueModelSavePropertyValues()
                self.save_property_values.append(temp_model.from_map(k))
        return self


class UpdatePropertyResponseBodyUpdateResult(TeaModel):
    def __init__(self, property_id=None, property_key=None, save_property_value_model=None):
        # The ID of the property.
        self.property_id = property_id  # type: long
        # The name of the property.
        self.property_key = property_key  # type: str
        # The result of the property value modification.
        self.save_property_value_model = save_property_value_model  # type: UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel

    def validate(self):
        if self.save_property_value_model:
            self.save_property_value_model.validate()

    def to_map(self):
        _map = super(UpdatePropertyResponseBodyUpdateResult, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['PropertyId'] = self.property_id
        if self.property_key is not None:
            result['PropertyKey'] = self.property_key
        if self.save_property_value_model is not None:
            result['SavePropertyValueModel'] = self.save_property_value_model.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PropertyId') is not None:
            self.property_id = m.get('PropertyId')
        if m.get('PropertyKey') is not None:
            self.property_key = m.get('PropertyKey')
        if m.get('SavePropertyValueModel') is not None:
            temp_model = UpdatePropertyResponseBodyUpdateResultSavePropertyValueModel()
            self.save_property_value_model = temp_model.from_map(m['SavePropertyValueModel'])
        return self


class UpdatePropertyResponseBody(TeaModel):
    def __init__(self, request_id=None, update_result=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the modification.
        self.update_result = update_result  # type: UpdatePropertyResponseBodyUpdateResult

    def validate(self):
        if self.update_result:
            self.update_result.validate()

    def to_map(self):
        _map = super(UpdatePropertyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.update_result is not None:
            result['UpdateResult'] = self.update_result.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UpdateResult') is not None:
            temp_model = UpdatePropertyResponseBodyUpdateResult()
            self.update_result = temp_model.from_map(m['UpdateResult'])
        return self


class UpdatePropertyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePropertyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePropertyResponse, self).to_map()
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
            temp_model = UpdatePropertyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


