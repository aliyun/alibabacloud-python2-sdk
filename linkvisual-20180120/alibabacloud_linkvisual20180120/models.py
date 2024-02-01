# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddEventRecordPlanDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, plan_id=None, product_key=None,
                 stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.plan_id = plan_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEventRecordPlanDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class AddEventRecordPlanDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddEventRecordPlanDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddEventRecordPlanDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddEventRecordPlanDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddEventRecordPlanDeviceResponse, self).to_map()
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
            temp_model = AddEventRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceDeviceGroupRequest(TeaModel):
    def __init__(self, device_group_name=None, isolation_id=None):
        self.device_group_name = device_group_name  # type: str
        self.isolation_id = isolation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceDeviceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class AddFaceDeviceGroupResponseBodyData(TeaModel):
    def __init__(self, device_group_id=None, device_group_name=None, modified_time=None):
        self.device_group_id = device_group_id  # type: str
        self.device_group_name = device_group_name  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceDeviceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class AddFaceDeviceGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: AddFaceDeviceGroupResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddFaceDeviceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceDeviceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceDeviceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceDeviceGroupResponse, self).to_map()
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
            temp_model = AddFaceDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceDeviceToDeviceGroupRequest(TeaModel):
    def __init__(self, device_group_id=None, device_name=None, iot_instance_id=None, isolation_id=None,
                 product_key=None):
        self.device_group_id = device_group_id  # type: str
        self.device_name = device_name  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceDeviceToDeviceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class AddFaceDeviceToDeviceGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceDeviceToDeviceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceDeviceToDeviceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceDeviceToDeviceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceDeviceToDeviceGroupResponse, self).to_map()
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
            temp_model = AddFaceDeviceToDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserRequest(TeaModel):
    def __init__(self, custom_user_id=None, face_pic_url=None, isolation_id=None, name=None, params=None):
        self.custom_user_id = custom_user_id  # type: str
        self.face_pic_url = face_pic_url  # type: str
        self.isolation_id = isolation_id  # type: str
        self.name = name  # type: str
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class AddFaceUserResponseBodyData(TeaModel):
    def __init__(self, custom_user_id=None, name=None, params=None, user_id=None):
        self.custom_user_id = custom_user_id  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddFaceUserResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: AddFaceUserResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddFaceUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceUserResponse, self).to_map()
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
            temp_model = AddFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserGroupRequest(TeaModel):
    def __init__(self, isolation_id=None, user_group_name=None):
        self.isolation_id = isolation_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class AddFaceUserGroupResponseBodyData(TeaModel):
    def __init__(self, modified_time=None, user_group_id=None, user_group_name=None):
        self.modified_time = modified_time  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class AddFaceUserGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: AddFaceUserGroupResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddFaceUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceUserGroupResponse, self).to_map()
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
            temp_model = AddFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(self, device_group_id=None, iot_instance_id=None, isolation_id=None, relation=None,
                 user_group_id=None):
        self.device_group_id = device_group_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.relation = relation  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserGroupAndDeviceGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(self, control_id=None, modified_time=None):
        self.control_id = control_id  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserGroupAndDeviceGroupRelationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: AddFaceUserGroupAndDeviceGroupRelationResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(AddFaceUserGroupAndDeviceGroupRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = AddFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceUserGroupAndDeviceGroupRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceUserGroupAndDeviceGroupRelationResponse, self).to_map()
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
            temp_model = AddFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserPictureRequest(TeaModel):
    def __init__(self, face_pic_url=None, isolation_id=None, user_id=None):
        self.face_pic_url = face_pic_url  # type: str
        self.isolation_id = isolation_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserPictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddFaceUserPictureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: dict[str, any]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserPictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserPictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceUserPictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceUserPictureResponse, self).to_map()
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
            temp_model = AddFaceUserPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddFaceUserToUserGroupRequest(TeaModel):
    def __init__(self, isolation_id=None, user_group_id=None, user_id=None):
        self.isolation_id = isolation_id  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserToUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddFaceUserToUserGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddFaceUserToUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddFaceUserToUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddFaceUserToUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddFaceUserToUserGroupResponse, self).to_map()
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
            temp_model = AddFaceUserToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRecordPlanDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, plan_id=None, product_key=None,
                 stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.plan_id = plan_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordPlanDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class AddRecordPlanDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddRecordPlanDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRecordPlanDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddRecordPlanDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddRecordPlanDeviceResponse, self).to_map()
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
            temp_model = AddRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQueryVisionDeviceInfoRequest(TeaModel):
    def __init__(self, device_name_list=None, iot_id_list=None, iot_instance_id=None, product_key=None):
        self.device_name_list = device_name_list  # type: list[str]
        self.iot_id_list = iot_id_list  # type: list[str]
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name_list is not None:
            result['DeviceNameList'] = self.device_name_list
        if self.iot_id_list is not None:
            result['IotIdList'] = self.iot_id_list
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNameList') is not None:
            self.device_name_list = m.get('DeviceNameList')
        if m.get('IotIdList') is not None:
            self.iot_id_list = m.get('IotIdList')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo(TeaModel):
    def __init__(self, device_protocol=None, gb_id=None, net_protocol=None, nick_name=None, password=None,
                 sub_product_key=None):
        self.device_protocol = device_protocol  # type: int
        self.gb_id = gb_id  # type: str
        self.net_protocol = net_protocol  # type: int
        self.nick_name = nick_name  # type: str
        self.password = password  # type: str
        self.sub_product_key = sub_product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_protocol is not None:
            result['DeviceProtocol'] = self.device_protocol
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.net_protocol is not None:
            result['NetProtocol'] = self.net_protocol
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.password is not None:
            result['Password'] = self.password
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceProtocol') is not None:
            self.device_protocol = m.get('DeviceProtocol')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('NetProtocol') is not None:
            self.net_protocol = m.get('NetProtocol')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo(TeaModel):
    def __init__(self, pull_auth_key=None, pull_key_expire_time=None, push_auth_key=None,
                 push_key_expire_time=None, push_url_sample=None, stream_name=None, stream_status=None):
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_key_expire_time = pull_key_expire_time  # type: int
        self.push_auth_key = push_auth_key  # type: str
        self.push_key_expire_time = push_key_expire_time  # type: int
        self.push_url_sample = push_url_sample  # type: str
        self.stream_name = stream_name  # type: str
        self.stream_status = stream_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.push_url_sample is not None:
            result['PushUrlSample'] = self.push_url_sample
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('PushUrlSample') is not None:
            self.push_url_sample = m.get('PushUrlSample')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList(TeaModel):
    def __init__(self, description=None, device_type=None, gb_device_info=None, iot_id=None, rtmp_device_info=None):
        self.description = description  # type: str
        self.device_type = device_type  # type: int
        self.gb_device_info = gb_device_info  # type: BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo
        self.iot_id = iot_id  # type: str
        self.rtmp_device_info = rtmp_device_info  # type: BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo

    def validate(self):
        if self.gb_device_info:
            self.gb_device_info.validate()
        if self.rtmp_device_info:
            self.rtmp_device_info.validate()

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.gb_device_info is not None:
            result['GbDeviceInfo'] = self.gb_device_info.to_map()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.rtmp_device_info is not None:
            result['RtmpDeviceInfo'] = self.rtmp_device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('GbDeviceInfo') is not None:
            temp_model = BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListGbDeviceInfo()
            self.gb_device_info = temp_model.from_map(m['GbDeviceInfo'])
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('RtmpDeviceInfo') is not None:
            temp_model = BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoListRtmpDeviceInfo()
            self.rtmp_device_info = temp_model.from_map(m['RtmpDeviceInfo'])
        return self


class BatchQueryVisionDeviceInfoResponseBodyData(TeaModel):
    def __init__(self, device_info_list=None):
        self.device_info_list = device_info_list  # type: list[BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList]

    def validate(self):
        if self.device_info_list:
            for k in self.device_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k in self.device_info_list:
                result['DeviceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k in m.get('DeviceInfoList'):
                temp_model = BatchQueryVisionDeviceInfoResponseBodyDataDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k))
        return self


class BatchQueryVisionDeviceInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: BatchQueryVisionDeviceInfoResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = BatchQueryVisionDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BatchQueryVisionDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchQueryVisionDeviceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchQueryVisionDeviceInfoResponse, self).to_map()
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
            temp_model = BatchQueryVisionDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindPictureSearchAppWithDevicesRequest(TeaModel):
    def __init__(self, app_instance_id=None, device_iot_ids=None, iot_instance_id=None):
        self.app_instance_id = app_instance_id  # type: str
        self.device_iot_ids = device_iot_ids  # type: list[str]
        self.iot_instance_id = iot_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindPictureSearchAppWithDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class BindPictureSearchAppWithDevicesResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindPictureSearchAppWithDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class BindPictureSearchAppWithDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindPictureSearchAppWithDevicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindPictureSearchAppWithDevicesResponse, self).to_map()
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
            temp_model = BindPictureSearchAppWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckFaceUserDoExistOnDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_instance_id=None, isolation_id=None, product_key=None, user_id=None):
        self.device_name = device_name  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.product_key = product_key  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckFaceUserDoExistOnDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CheckFaceUserDoExistOnDeviceResponseBodyData(TeaModel):
    def __init__(self, do_exist=None):
        self.do_exist = do_exist  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckFaceUserDoExistOnDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.do_exist is not None:
            result['DoExist'] = self.do_exist
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DoExist') is not None:
            self.do_exist = m.get('DoExist')
        return self


class CheckFaceUserDoExistOnDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CheckFaceUserDoExistOnDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CheckFaceUserDoExistOnDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CheckFaceUserDoExistOnDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CheckFaceUserDoExistOnDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckFaceUserDoExistOnDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckFaceUserDoExistOnDeviceResponse, self).to_map()
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
            temp_model = CheckFaceUserDoExistOnDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearFaceDeviceDBRequest(TeaModel):
    def __init__(self, device_name=None, iot_instance_id=None, isolation_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearFaceDeviceDBRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ClearFaceDeviceDBResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: dict[str, any]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearFaceDeviceDBResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClearFaceDeviceDBResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClearFaceDeviceDBResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearFaceDeviceDBResponse, self).to_map()
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
            temp_model = ClearFaceDeviceDBResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEventRecordPlanRequest(TeaModel):
    def __init__(self, event_types=None, name=None, pre_record_duration=None, record_duration=None,
                 template_id=None):
        self.event_types = event_types  # type: str
        self.name = name  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.record_duration = record_duration  # type: int
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventRecordPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        if self.name is not None:
            result['Name'] = self.name
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateEventRecordPlanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEventRecordPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateEventRecordPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEventRecordPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEventRecordPlanResponse, self).to_map()
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
            temp_model = CreateEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGbDeviceRequest(TeaModel):
    def __init__(self, description=None, device_name=None, device_type=None, gb_id=None, iot_instance_id=None,
                 media_net_protocol=None, password=None, product_key=None, sub_product_key=None):
        self.description = description  # type: str
        self.device_name = device_name  # type: str
        self.device_type = device_type  # type: int
        self.gb_id = gb_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.media_net_protocol = media_net_protocol  # type: str
        self.password = password  # type: str
        self.product_key = product_key  # type: str
        self.sub_product_key = sub_product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGbDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.media_net_protocol is not None:
            result['MediaNetProtocol'] = self.media_net_protocol
        if self.password is not None:
            result['Password'] = self.password
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('MediaNetProtocol') is not None:
            self.media_net_protocol = m.get('MediaNetProtocol')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class CreateGbDeviceResponseBodyData(TeaModel):
    def __init__(self, device_name=None, iot_id=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGbDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class CreateGbDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateGbDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateGbDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateGbDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGbDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGbDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGbDeviceResponse, self).to_map()
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
            temp_model = CreateGbDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocalFileUploadJobRequestTimeSlot(TeaModel):
    def __init__(self, device_name=None, end_time=None, iot_id=None, product_key=None, start_time=None):
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: int
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str
        self.start_time = start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocalFileUploadJobRequestTimeSlot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateLocalFileUploadJobRequest(TeaModel):
    def __init__(self, iot_instance_id=None, time_slot=None):
        self.iot_instance_id = iot_instance_id  # type: str
        self.time_slot = time_slot  # type: list[CreateLocalFileUploadJobRequestTimeSlot]

    def validate(self):
        if self.time_slot:
            for k in self.time_slot:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateLocalFileUploadJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        result['TimeSlot'] = []
        if self.time_slot is not None:
            for k in self.time_slot:
                result['TimeSlot'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        self.time_slot = []
        if m.get('TimeSlot') is not None:
            for k in m.get('TimeSlot'):
                temp_model = CreateLocalFileUploadJobRequestTimeSlot()
                self.time_slot.append(temp_model.from_map(k))
        return self


class CreateLocalFileUploadJobResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocalFileUploadJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateLocalFileUploadJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateLocalFileUploadJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateLocalFileUploadJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateLocalFileUploadJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLocalFileUploadJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLocalFileUploadJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLocalFileUploadJobResponse, self).to_map()
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
            temp_model = CreateLocalFileUploadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLocalRecordDownloadByTimeJobRequest(TeaModel):
    def __init__(self, begin_time=None, device_name=None, end_time=None, iot_id=None, iot_instance_id=None,
                 product_key=None, speed=None):
        self.begin_time = begin_time  # type: int
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.speed = speed  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocalRecordDownloadByTimeJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.speed is not None:
            result['Speed'] = self.speed
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Speed') is not None:
            self.speed = m.get('Speed')
        return self


class CreateLocalRecordDownloadByTimeJobResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLocalRecordDownloadByTimeJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateLocalRecordDownloadByTimeJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateLocalRecordDownloadByTimeJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateLocalRecordDownloadByTimeJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateLocalRecordDownloadByTimeJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateLocalRecordDownloadByTimeJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLocalRecordDownloadByTimeJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLocalRecordDownloadByTimeJobResponse, self).to_map()
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
            temp_model = CreateLocalRecordDownloadByTimeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePictureSearchAppRequest(TeaModel):
    def __init__(self, desc=None, iot_instance_id=None, name=None):
        self.desc = desc  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePictureSearchAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreatePictureSearchAppResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePictureSearchAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePictureSearchAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePictureSearchAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePictureSearchAppResponse, self).to_map()
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
            temp_model = CreatePictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePictureSearchJobRequest(TeaModel):
    def __init__(self, app_instance_id=None, body_threshold=None, end_time=None, picture_search_type=None,
                 search_pic_url=None, start_time=None, threshold=None):
        self.app_instance_id = app_instance_id  # type: str
        self.body_threshold = body_threshold  # type: float
        self.end_time = end_time  # type: long
        self.picture_search_type = picture_search_type  # type: int
        self.search_pic_url = search_pic_url  # type: str
        self.start_time = start_time  # type: long
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePictureSearchJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.body_threshold is not None:
            result['BodyThreshold'] = self.body_threshold
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('BodyThreshold') is not None:
            self.body_threshold = m.get('BodyThreshold')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class CreatePictureSearchJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreatePictureSearchJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePictureSearchJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreatePictureSearchJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreatePictureSearchJobResponse, self).to_map()
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
            temp_model = CreatePictureSearchJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecordDownloadByTimeJobRequest(TeaModel):
    def __init__(self, begin_time=None, device_name=None, end_time=None, iot_id=None, iot_instance_id=None,
                 product_key=None, record_type=None, stream_type=None):
        self.begin_time = begin_time  # type: int
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.record_type = record_type  # type: int
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecordDownloadByTimeJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class CreateRecordDownloadByTimeJobResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecordDownloadByTimeJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateRecordDownloadByTimeJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateRecordDownloadByTimeJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateRecordDownloadByTimeJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateRecordDownloadByTimeJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRecordDownloadByTimeJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRecordDownloadByTimeJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRecordDownloadByTimeJobResponse, self).to_map()
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
            temp_model = CreateRecordDownloadByTimeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRecordPlanRequest(TeaModel):
    def __init__(self, name=None, template_id=None):
        self.name = name  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecordPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateRecordPlanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRecordPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRecordPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRecordPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRecordPlanResponse, self).to_map()
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
            temp_model = CreateRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRtmpDeviceRequest(TeaModel):
    def __init__(self, description=None, device_name=None, iot_instance_id=None, product_key=None,
                 pull_auth_key=None, pull_key_expire_time=None, push_auth_key=None, push_key_expire_time=None,
                 sub_stream_name=None):
        self.description = description  # type: str
        self.device_name = device_name  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_key_expire_time = pull_key_expire_time  # type: int
        self.push_auth_key = push_auth_key  # type: str
        self.push_key_expire_time = push_key_expire_time  # type: int
        self.sub_stream_name = sub_stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRtmpDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.sub_stream_name is not None:
            result['SubStreamName'] = self.sub_stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('SubStreamName') is not None:
            self.sub_stream_name = m.get('SubStreamName')
        return self


class CreateRtmpDeviceResponseBodyData(TeaModel):
    def __init__(self, device_name=None, iot_id=None, stream_name=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateRtmpDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class CreateRtmpDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateRtmpDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateRtmpDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateRtmpDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateRtmpDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateRtmpDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateRtmpDeviceResponse, self).to_map()
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
            temp_model = CreateRtmpDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamPushJobRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, job_type=None, product_key=None,
                 push_url=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_type = job_type  # type: int
        self.product_key = product_key  # type: str
        self.push_url = push_url  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamPushJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class CreateStreamPushJobResponseBodyData(TeaModel):
    def __init__(self, job_id=None):
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamPushJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class CreateStreamPushJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: CreateStreamPushJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(CreateStreamPushJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = CreateStreamPushJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStreamPushJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateStreamPushJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStreamPushJobResponse, self).to_map()
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
            temp_model = CreateStreamPushJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStreamSnapshotJobRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None,
                 snapshot_interval=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.snapshot_interval = snapshot_interval  # type: int
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamSnapshotJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.snapshot_interval is not None:
            result['SnapshotInterval'] = self.snapshot_interval
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SnapshotInterval') is not None:
            self.snapshot_interval = m.get('SnapshotInterval')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class CreateStreamSnapshotJobResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateStreamSnapshotJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateStreamSnapshotJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateStreamSnapshotJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateStreamSnapshotJobResponse, self).to_map()
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
            temp_model = CreateStreamSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTimeTemplateRequestTimeSections(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTimeTemplateRequestTimeSections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class CreateTimeTemplateRequest(TeaModel):
    def __init__(self, all_day=None, name=None, time_sections=None):
        self.all_day = all_day  # type: int
        self.name = name  # type: str
        self.time_sections = time_sections  # type: list[CreateTimeTemplateRequestTimeSections]

    def validate(self):
        if self.time_sections:
            for k in self.time_sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateTimeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.name is not None:
            result['Name'] = self.name
        result['TimeSections'] = []
        if self.time_sections is not None:
            for k in self.time_sections:
                result['TimeSections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k in m.get('TimeSections'):
                temp_model = CreateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k))
        return self


class CreateTimeTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTimeTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTimeTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTimeTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTimeTemplateResponse, self).to_map()
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
            temp_model = CreateTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRecordPlanRequest(TeaModel):
    def __init__(self, plan_id=None):
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventRecordPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteEventRecordPlanResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventRecordPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRecordPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventRecordPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventRecordPlanResponse, self).to_map()
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
            temp_model = DeleteEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventRecordPlanDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventRecordPlanDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DeleteEventRecordPlanDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEventRecordPlanDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteEventRecordPlanDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEventRecordPlanDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEventRecordPlanDeviceResponse, self).to_map()
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
            temp_model = DeleteEventRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceDeviceGroupRequest(TeaModel):
    def __init__(self, device_group_id=None, isolation_id=None):
        self.device_group_id = device_group_id  # type: str
        self.isolation_id = isolation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceDeviceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class DeleteFaceDeviceGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceDeviceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceDeviceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaceDeviceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaceDeviceGroupResponse, self).to_map()
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
            temp_model = DeleteFaceDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserRequest(TeaModel):
    def __init__(self, isolation_id=None, user_id=None):
        self.isolation_id = isolation_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteFaceUserResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaceUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaceUserResponse, self).to_map()
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
            temp_model = DeleteFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserGroupRequest(TeaModel):
    def __init__(self, isolation_id=None, user_group_id=None):
        self.isolation_id = isolation_id  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteFaceUserGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaceUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaceUserGroupResponse, self).to_map()
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
            temp_model = DeleteFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(self, control_id=None, isolation_id=None):
        self.control_id = control_id  # type: str
        self.isolation_id = isolation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserGroupAndDeviceGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserGroupAndDeviceGroupRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaceUserGroupAndDeviceGroupRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaceUserGroupAndDeviceGroupRelationResponse, self).to_map()
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
            temp_model = DeleteFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceUserPictureRequest(TeaModel):
    def __init__(self, face_pic_md_5=None, isolation_id=None, user_id=None):
        self.face_pic_md_5 = face_pic_md_5  # type: str
        self.isolation_id = isolation_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserPictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_md_5 is not None:
            result['FacePicMd5'] = self.face_pic_md_5
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FacePicMd5') is not None:
            self.face_pic_md_5 = m.get('FacePicMd5')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteFaceUserPictureResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFaceUserPictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFaceUserPictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFaceUserPictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFaceUserPictureResponse, self).to_map()
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
            temp_model = DeleteFaceUserPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGbDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGbDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteGbDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGbDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGbDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGbDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGbDeviceResponse, self).to_map()
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
            temp_model = DeleteGbDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLocalFileUploadJobRequest(TeaModel):
    def __init__(self, iot_instance_id=None, job_id=None):
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLocalFileUploadJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DeleteLocalFileUploadJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: dict[str, any]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLocalFileUploadJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteLocalFileUploadJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLocalFileUploadJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLocalFileUploadJobResponse, self).to_map()
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
            temp_model = DeleteLocalFileUploadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePictureRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, picture_id_list=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.picture_id_list = picture_id_list  # type: list[str]
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.picture_id_list is not None:
            result['PictureIdList'] = self.picture_id_list
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PictureIdList') is not None:
            self.picture_id_list = m.get('PictureIdList')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeletePictureResponseBodyData(TeaModel):
    def __init__(self, deleted_count=None):
        self.deleted_count = deleted_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeletePictureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        return self


class DeletePictureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DeletePictureResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeletePictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = DeletePictureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeletePictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeletePictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeletePictureResponse, self).to_map()
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
            temp_model = DeletePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordRequest(TeaModel):
    def __init__(self, device_name=None, file_name_list=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.file_name_list = file_name_list  # type: list[str]
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.file_name_list is not None:
            result['FileNameList'] = self.file_name_list
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FileNameList') is not None:
            self.file_name_list = m.get('FileNameList')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteRecordResponseBodyData(TeaModel):
    def __init__(self, deleted_count=None):
        self.deleted_count = deleted_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deleted_count is not None:
            result['DeletedCount'] = self.deleted_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeletedCount') is not None:
            self.deleted_count = m.get('DeletedCount')
        return self


class DeleteRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DeleteRecordResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DeleteRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = DeleteRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRecordResponse, self).to_map()
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
            temp_model = DeleteRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordPlanRequest(TeaModel):
    def __init__(self, plan_id=None):
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class DeleteRecordPlanResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRecordPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRecordPlanResponse, self).to_map()
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
            temp_model = DeleteRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRecordPlanDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordPlanDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DeleteRecordPlanDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRecordPlanDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRecordPlanDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRecordPlanDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRecordPlanDeviceResponse, self).to_map()
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
            temp_model = DeleteRecordPlanDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRtmpDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRtmpDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteRtmpDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRtmpDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRtmpDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRtmpDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRtmpDeviceResponse, self).to_map()
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
            temp_model = DeleteRtmpDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRtmpKeyRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.type = type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRtmpKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DeleteRtmpKeyResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteRtmpKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteRtmpKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteRtmpKeyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteRtmpKeyResponse, self).to_map()
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
            temp_model = DeleteRtmpKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamPushJobRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, job_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_id = job_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStreamPushJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class DeleteStreamPushJobResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStreamPushJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStreamPushJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteStreamPushJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStreamPushJobResponse, self).to_map()
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
            temp_model = DeleteStreamPushJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteStreamSnapshotJobRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStreamSnapshotJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class DeleteStreamSnapshotJobResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteStreamSnapshotJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteStreamSnapshotJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteStreamSnapshotJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteStreamSnapshotJobResponse, self).to_map()
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
            temp_model = DeleteStreamSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTimeTemplateRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTimeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class DeleteTimeTemplateResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTimeTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteTimeTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTimeTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTimeTemplateResponse, self).to_map()
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
            temp_model = DeleteTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetectUserFaceByUrlRequest(TeaModel):
    def __init__(self, face_pic_url=None):
        self.face_pic_url = face_pic_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectUserFaceByUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        return self


class DetectUserFaceByUrlResponseBodyDataDataFaceRects(TeaModel):
    def __init__(self, face_rects_data=None):
        self.face_rects_data = face_rects_data  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectUserFaceByUrlResponseBodyDataDataFaceRects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_rects_data is not None:
            result['FaceRectsData'] = self.face_rects_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceRectsData') is not None:
            self.face_rects_data = m.get('FaceRectsData')
        return self


class DetectUserFaceByUrlResponseBodyDataDataLandmarks(TeaModel):
    def __init__(self, landmarks_data=None):
        self.landmarks_data = landmarks_data  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetectUserFaceByUrlResponseBodyDataDataLandmarks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.landmarks_data is not None:
            result['LandmarksData'] = self.landmarks_data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LandmarksData') is not None:
            self.landmarks_data = m.get('LandmarksData')
        return self


class DetectUserFaceByUrlResponseBodyDataData(TeaModel):
    def __init__(self, age=None, blur_score=None, face_probability=None, face_rects=None, gender=None,
                 good_for_library=None, good_for_recognition=None, landmarks=None, occlusion_score=None, pose_score=None):
        self.age = age  # type: int
        self.blur_score = blur_score  # type: float
        self.face_probability = face_probability  # type: float
        self.face_rects = face_rects  # type: DetectUserFaceByUrlResponseBodyDataDataFaceRects
        self.gender = gender  # type: int
        self.good_for_library = good_for_library  # type: bool
        self.good_for_recognition = good_for_recognition  # type: bool
        self.landmarks = landmarks  # type: DetectUserFaceByUrlResponseBodyDataDataLandmarks
        self.occlusion_score = occlusion_score  # type: float
        self.pose_score = pose_score  # type: float

    def validate(self):
        if self.face_rects:
            self.face_rects.validate()
        if self.landmarks:
            self.landmarks.validate()

    def to_map(self):
        _map = super(DetectUserFaceByUrlResponseBodyDataData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.age is not None:
            result['Age'] = self.age
        if self.blur_score is not None:
            result['BlurScore'] = self.blur_score
        if self.face_probability is not None:
            result['FaceProbability'] = self.face_probability
        if self.face_rects is not None:
            result['FaceRects'] = self.face_rects.to_map()
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.good_for_library is not None:
            result['GoodForLibrary'] = self.good_for_library
        if self.good_for_recognition is not None:
            result['GoodForRecognition'] = self.good_for_recognition
        if self.landmarks is not None:
            result['Landmarks'] = self.landmarks.to_map()
        if self.occlusion_score is not None:
            result['OcclusionScore'] = self.occlusion_score
        if self.pose_score is not None:
            result['PoseScore'] = self.pose_score
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Age') is not None:
            self.age = m.get('Age')
        if m.get('BlurScore') is not None:
            self.blur_score = m.get('BlurScore')
        if m.get('FaceProbability') is not None:
            self.face_probability = m.get('FaceProbability')
        if m.get('FaceRects') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyDataDataFaceRects()
            self.face_rects = temp_model.from_map(m['FaceRects'])
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('GoodForLibrary') is not None:
            self.good_for_library = m.get('GoodForLibrary')
        if m.get('GoodForRecognition') is not None:
            self.good_for_recognition = m.get('GoodForRecognition')
        if m.get('Landmarks') is not None:
            temp_model = DetectUserFaceByUrlResponseBodyDataDataLandmarks()
            self.landmarks = temp_model.from_map(m['Landmarks'])
        if m.get('OcclusionScore') is not None:
            self.occlusion_score = m.get('OcclusionScore')
        if m.get('PoseScore') is not None:
            self.pose_score = m.get('PoseScore')
        return self


class DetectUserFaceByUrlResponseBodyData(TeaModel):
    def __init__(self, data=None):
        self.data = data  # type: list[DetectUserFaceByUrlResponseBodyDataData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetectUserFaceByUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = DetectUserFaceByUrlResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        return self


class DetectUserFaceByUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: DetectUserFaceByUrlResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(DetectUserFaceByUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = DetectUserFaceByUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DetectUserFaceByUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetectUserFaceByUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetectUserFaceByUrlResponse, self).to_map()
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
            temp_model = DetectUserFaceByUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableGbSubDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, sub_device_id=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.sub_device_id = sub_device_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableGbSubDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.sub_device_id is not None:
            result['SubDeviceId'] = self.sub_device_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SubDeviceId') is not None:
            self.sub_device_id = m.get('SubDeviceId')
        return self


class EnableGbSubDeviceResponseBodyData(TeaModel):
    def __init__(self, device_name=None, product_key=None):
        self.device_name = device_name  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableGbSubDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class EnableGbSubDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: EnableGbSubDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(EnableGbSubDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = EnableGbSubDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EnableGbSubDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableGbSubDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableGbSubDeviceResponse, self).to_map()
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
            temp_model = EnableGbSubDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPictureSearchJobStatusRequest(TeaModel):
    def __init__(self, app_instance_id=None, job_id=None):
        self.app_instance_id = app_instance_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPictureSearchJobStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetPictureSearchJobStatusResponseBodyData(TeaModel):
    def __init__(self, create_time=None, end_time=None, job_id=None, job_status=None, search_pic_url=None,
                 start_time=None, threshold=None):
        self.create_time = create_time  # type: long
        self.end_time = end_time  # type: long
        self.job_id = job_id  # type: str
        self.job_status = job_status  # type: int
        self.search_pic_url = search_pic_url  # type: str
        self.start_time = start_time  # type: long
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPictureSearchJobStatusResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class GetPictureSearchJobStatusResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: GetPictureSearchJobStatusResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetPictureSearchJobStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = GetPictureSearchJobStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPictureSearchJobStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPictureSearchJobStatusResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPictureSearchJobStatusResponse, self).to_map()
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
            temp_model = GetPictureSearchJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PictureSearchPictureRequest(TeaModel):
    def __init__(self, app_instance_id=None, contain_pic_url=None, current_page=None, end_time=None, page_size=None,
                 picture_search_type=None, search_pic_url=None, start_time=None, threshold=None):
        self.app_instance_id = app_instance_id  # type: str
        self.contain_pic_url = contain_pic_url  # type: bool
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.page_size = page_size  # type: int
        self.picture_search_type = picture_search_type  # type: int
        self.search_pic_url = search_pic_url  # type: str
        self.start_time = start_time  # type: long
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(PictureSearchPictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.contain_pic_url is not None:
            result['ContainPicUrl'] = self.contain_pic_url
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.picture_search_type is not None:
            result['PictureSearchType'] = self.picture_search_type
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('ContainPicUrl') is not None:
            self.contain_pic_url = m.get('ContainPicUrl')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PictureSearchType') is not None:
            self.picture_search_type = m.get('PictureSearchType')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class PictureSearchPictureResponseBodyDataPageData(TeaModel):
    def __init__(self, event_time=None, gateway_iot_id=None, iot_id=None, pic_url=None, threshold=None,
                 vector_id=None, vector_type=None):
        self.event_time = event_time  # type: long
        self.gateway_iot_id = gateway_iot_id  # type: str
        self.iot_id = iot_id  # type: str
        self.pic_url = pic_url  # type: str
        self.threshold = threshold  # type: float
        self.vector_id = vector_id  # type: str
        self.vector_type = vector_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(PictureSearchPictureResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        if self.vector_type is not None:
            result['VectorType'] = self.vector_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        if m.get('VectorType') is not None:
            self.vector_type = m.get('VectorType')
        return self


class PictureSearchPictureResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[PictureSearchPictureResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(PictureSearchPictureResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = PictureSearchPictureResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class PictureSearchPictureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: PictureSearchPictureResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(PictureSearchPictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = PictureSearchPictureResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PictureSearchPictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: PictureSearchPictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(PictureSearchPictureResponse, self).to_map()
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
            temp_model = PictureSearchPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryCarProcessEventsRequest(TeaModel):
    def __init__(self, action_type=None, area_index=None, begin_time=None, current_page=None, end_time=None,
                 iot_instance_id=None, page_size=None, plate_no=None, sub_device_name=None, sub_iot_id=None, sub_product_key=None):
        self.action_type = action_type  # type: int
        self.area_index = area_index  # type: int
        self.begin_time = begin_time  # type: long
        self.current_page = current_page  # type: int
        self.end_time = end_time  # type: long
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int
        self.plate_no = plate_no  # type: str
        self.sub_device_name = sub_device_name  # type: str
        self.sub_iot_id = sub_iot_id  # type: str
        self.sub_product_key = sub_product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCarProcessEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.area_index is not None:
            result['AreaIndex'] = self.area_index
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.sub_device_name is not None:
            result['SubDeviceName'] = self.sub_device_name
        if self.sub_iot_id is not None:
            result['SubIotId'] = self.sub_iot_id
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AreaIndex') is not None:
            self.area_index = m.get('AreaIndex')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('SubDeviceName') is not None:
            self.sub_device_name = m.get('SubDeviceName')
        if m.get('SubIotId') is not None:
            self.sub_iot_id = m.get('SubIotId')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class QueryCarProcessEventsResponseBodyDataPageData(TeaModel):
    def __init__(self, action_type=None, area_index=None, confidence=None, event_id=None, event_pic_id=None,
                 event_pic_url=None, event_time=None, event_type=None, iot_id=None, plate_no=None, sub_device_name=None,
                 sub_device_nick_name=None, sub_iot_id=None, sub_product_key=None, task_id=None):
        self.action_type = action_type  # type: int
        self.area_index = area_index  # type: int
        self.confidence = confidence  # type: int
        self.event_id = event_id  # type: str
        self.event_pic_id = event_pic_id  # type: str
        self.event_pic_url = event_pic_url  # type: str
        self.event_time = event_time  # type: long
        self.event_type = event_type  # type: int
        self.iot_id = iot_id  # type: str
        self.plate_no = plate_no  # type: str
        self.sub_device_name = sub_device_name  # type: str
        self.sub_device_nick_name = sub_device_nick_name  # type: str
        self.sub_iot_id = sub_iot_id  # type: str
        self.sub_product_key = sub_product_key  # type: str
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryCarProcessEventsResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_type is not None:
            result['ActionType'] = self.action_type
        if self.area_index is not None:
            result['AreaIndex'] = self.area_index
        if self.confidence is not None:
            result['Confidence'] = self.confidence
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_pic_id is not None:
            result['EventPicId'] = self.event_pic_id
        if self.event_pic_url is not None:
            result['EventPicUrl'] = self.event_pic_url
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.plate_no is not None:
            result['PlateNo'] = self.plate_no
        if self.sub_device_name is not None:
            result['SubDeviceName'] = self.sub_device_name
        if self.sub_device_nick_name is not None:
            result['SubDeviceNickName'] = self.sub_device_nick_name
        if self.sub_iot_id is not None:
            result['SubIotId'] = self.sub_iot_id
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')
        if m.get('AreaIndex') is not None:
            self.area_index = m.get('AreaIndex')
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventPicId') is not None:
            self.event_pic_id = m.get('EventPicId')
        if m.get('EventPicUrl') is not None:
            self.event_pic_url = m.get('EventPicUrl')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PlateNo') is not None:
            self.plate_no = m.get('PlateNo')
        if m.get('SubDeviceName') is not None:
            self.sub_device_name = m.get('SubDeviceName')
        if m.get('SubDeviceNickName') is not None:
            self.sub_device_nick_name = m.get('SubDeviceNickName')
        if m.get('SubIotId') is not None:
            self.sub_iot_id = m.get('SubIotId')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryCarProcessEventsResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[QueryCarProcessEventsResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryCarProcessEventsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryCarProcessEventsResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryCarProcessEventsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryCarProcessEventsResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryCarProcessEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryCarProcessEventsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryCarProcessEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryCarProcessEventsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryCarProcessEventsResponse, self).to_map()
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
            temp_model = QueryCarProcessEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventRequest(TeaModel):
    def __init__(self, begin_time=None, current_page=None, device_name=None, end_time=None, event_type=None,
                 iot_id=None, iot_instance_id=None, page_size=None, product_key=None):
        self.begin_time = begin_time  # type: long
        self.current_page = current_page  # type: int
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: long
        self.event_type = event_type  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceEventRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDeviceEventResponseBodyDataList(TeaModel):
    def __init__(self, event_data=None, event_desc=None, event_id=None, event_pic_id=None, event_time=None,
                 event_type=None):
        self.event_data = event_data  # type: str
        self.event_desc = event_desc  # type: str
        self.event_id = event_id  # type: str
        self.event_pic_id = event_pic_id  # type: str
        self.event_time = event_time  # type: str
        self.event_type = event_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceEventResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_data is not None:
            result['EventData'] = self.event_data
        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.event_pic_id is not None:
            result['EventPicId'] = self.event_pic_id
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventData') is not None:
            self.event_data = m.get('EventData')
        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('EventPicId') is not None:
            self.event_pic_id = m.get('EventPicId')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        return self


class QueryDeviceEventResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_count=None, page_size=None, total=None):
        self.list = list  # type: list[QueryDeviceEventResponseBodyDataList]
        self.page = page  # type: int
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDeviceEventResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryDeviceEventResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryDeviceEventResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDeviceEventResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDeviceEventResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceEventResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceEventResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceEventResponse, self).to_map()
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
            temp_model = QueryDeviceEventResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventPictureRequest(TeaModel):
    def __init__(self, device_name=None, event_id=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.event_id = event_id  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceEventPictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDeviceEventPictureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceEventPictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventPictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceEventPictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceEventPictureResponse, self).to_map()
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
            temp_model = QueryDeviceEventPictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceEventRecordRequest(TeaModel):
    def __init__(self, device_name=None, event_id=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.event_id = event_id  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceEventRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.event_id is not None:
            result['EventId'] = self.event_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryDeviceEventRecordResponseBodyData(TeaModel):
    def __init__(self, begin_time=None, end_time=None, file_name=None, vod_url=None):
        self.begin_time = begin_time  # type: str
        self.end_time = end_time  # type: str
        self.file_name = file_name  # type: str
        self.vod_url = vod_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceEventRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceEventRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[QueryDeviceEventRecordResponseBodyData]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDeviceEventRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryDeviceEventRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceEventRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceEventRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceEventRecordResponse, self).to_map()
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
            temp_model = QueryDeviceEventRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureByListRequest(TeaModel):
    def __init__(self, device_name=None, expire_time=None, iot_id=None, iot_instance_id=None, picture_id_list=None,
                 picture_type=None, product_key=None, thumb_width=None):
        self.device_name = device_name  # type: str
        self.expire_time = expire_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.picture_id_list = picture_id_list  # type: list[str]
        self.picture_type = picture_type  # type: int
        self.product_key = product_key  # type: str
        self.thumb_width = thumb_width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicePictureByListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.picture_id_list is not None:
            result['PictureIdList'] = self.picture_id_list
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.thumb_width is not None:
            result['ThumbWidth'] = self.thumb_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PictureIdList') is not None:
            self.picture_id_list = m.get('PictureIdList')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ThumbWidth') is not None:
            self.thumb_width = m.get('ThumbWidth')
        return self


class QueryDevicePictureByListResponseBodyDataPicData(TeaModel):
    def __init__(self, iot_id=None, pic_create_time=None, pic_id=None, pic_url=None, thumb_url=None):
        self.iot_id = iot_id  # type: str
        self.pic_create_time = pic_create_time  # type: long
        self.pic_id = pic_id  # type: str
        self.pic_url = pic_url  # type: str
        self.thumb_url = thumb_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicePictureByListResponseBodyDataPicData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        return self


class QueryDevicePictureByListResponseBodyData(TeaModel):
    def __init__(self, pic_data=None):
        self.pic_data = pic_data  # type: list[QueryDevicePictureByListResponseBodyDataPicData]

    def validate(self):
        if self.pic_data:
            for k in self.pic_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDevicePictureByListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['picData'] = []
        if self.pic_data is not None:
            for k in self.pic_data:
                result['picData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.pic_data = []
        if m.get('picData') is not None:
            for k in m.get('picData'):
                temp_model = QueryDevicePictureByListResponseBodyDataPicData()
                self.pic_data.append(temp_model.from_map(k))
        return self


class QueryDevicePictureByListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDevicePictureByListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDevicePictureByListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicePictureByListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureByListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDevicePictureByListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDevicePictureByListResponse, self).to_map()
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
            temp_model = QueryDevicePictureByListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureFileRequest(TeaModel):
    def __init__(self, capture_id=None, device_name=None, expire_time=None, iot_id=None, iot_instance_id=None,
                 picture_type=None, product_key=None, thumb_width=None):
        self.capture_id = capture_id  # type: str
        self.device_name = device_name  # type: str
        self.expire_time = expire_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.picture_type = picture_type  # type: int
        self.product_key = product_key  # type: str
        self.thumb_width = thumb_width  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicePictureFileRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capture_id is not None:
            result['CaptureId'] = self.capture_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.thumb_width is not None:
            result['ThumbWidth'] = self.thumb_width
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaptureId') is not None:
            self.capture_id = m.get('CaptureId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('ThumbWidth') is not None:
            self.thumb_width = m.get('ThumbWidth')
        return self


class QueryDevicePictureFileResponseBodyData(TeaModel):
    def __init__(self, iot_id=None, pic_create_time=None, pic_id=None, pic_url=None, thumb_url=None):
        self.iot_id = iot_id  # type: str
        self.pic_create_time = pic_create_time  # type: long
        self.pic_id = pic_id  # type: str
        self.pic_url = pic_url  # type: str
        self.thumb_url = thumb_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicePictureFileResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        return self


class QueryDevicePictureFileResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDevicePictureFileResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDevicePictureFileResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicePictureFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureFileResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDevicePictureFileResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDevicePictureFileResponse, self).to_map()
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
            temp_model = QueryDevicePictureFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDevicePictureLifeCycleRequest(TeaModel):
    def __init__(self, iot_id=None):
        self.iot_id = iot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicePictureLifeCycleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePictureLifeCycleResponseBodyData(TeaModel):
    def __init__(self, day=None, iot_id=None):
        self.day = day  # type: int
        self.iot_id = iot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDevicePictureLifeCycleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDevicePictureLifeCycleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDevicePictureLifeCycleResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDevicePictureLifeCycleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDevicePictureLifeCycleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDevicePictureLifeCycleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDevicePictureLifeCycleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDevicePictureLifeCycleResponse, self).to_map()
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
            temp_model = QueryDevicePictureLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceRecordLifeCycleRequest(TeaModel):
    def __init__(self, device_list=None):
        self.device_list = device_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceRecordLifeCycleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_list is not None:
            result['DeviceList'] = self.device_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceList') is not None:
            self.device_list = m.get('DeviceList')
        return self


class QueryDeviceRecordLifeCycleResponseBodyData(TeaModel):
    def __init__(self, day=None, iot_id=None):
        self.day = day  # type: int
        self.iot_id = iot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceRecordLifeCycleResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        return self


class QueryDeviceRecordLifeCycleResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: int
        self.data = data  # type: list[QueryDeviceRecordLifeCycleResponseBodyData]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryDeviceRecordLifeCycleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryDeviceRecordLifeCycleResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceRecordLifeCycleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceRecordLifeCycleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceRecordLifeCycleResponse, self).to_map()
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
            temp_model = QueryDeviceRecordLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceVodUrlRequest(TeaModel):
    def __init__(self, device_name=None, enable_stun=None, encrypt_type=None, file_name=None, iot_id=None,
                 iot_instance_id=None, play_un_limited=None, product_key=None, scheme=None, seek_time=None, should_encrypt=None,
                 url_valid_duration=None):
        self.device_name = device_name  # type: str
        self.enable_stun = enable_stun  # type: bool
        self.encrypt_type = encrypt_type  # type: int
        self.file_name = file_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.play_un_limited = play_un_limited  # type: bool
        self.product_key = product_key  # type: str
        self.scheme = scheme  # type: str
        self.seek_time = seek_time  # type: int
        self.should_encrypt = should_encrypt  # type: bool
        self.url_valid_duration = url_valid_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceVodUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryDeviceVodUrlResponseBodyData(TeaModel):
    def __init__(self, decrypt_key=None, stun_info=None, vod_url=None):
        self.decrypt_key = decrypt_key  # type: str
        self.stun_info = stun_info  # type: str
        self.vod_url = vod_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceVodUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceVodUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDeviceVodUrlResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDeviceVodUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceVodUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceVodUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceVodUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceVodUrlResponse, self).to_map()
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
            temp_model = QueryDeviceVodUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceVodUrlByTimeRequest(TeaModel):
    def __init__(self, begin_time=None, device_name=None, enable_stun=None, encrypt_type=None, end_time=None,
                 iot_id=None, iot_instance_id=None, play_un_limited=None, product_key=None, scheme=None, seek_time=None,
                 should_encrypt=None, url_valid_duration=None):
        self.begin_time = begin_time  # type: int
        self.device_name = device_name  # type: str
        self.enable_stun = enable_stun  # type: bool
        self.encrypt_type = encrypt_type  # type: int
        self.end_time = end_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.play_un_limited = play_un_limited  # type: bool
        self.product_key = product_key  # type: str
        self.scheme = scheme  # type: str
        self.seek_time = seek_time  # type: int
        self.should_encrypt = should_encrypt  # type: bool
        self.url_valid_duration = url_valid_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceVodUrlByTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryDeviceVodUrlByTimeResponseBodyData(TeaModel):
    def __init__(self, decrypt_key=None, stun_info=None, vod_url=None):
        self.decrypt_key = decrypt_key  # type: str
        self.stun_info = stun_info  # type: str
        self.vod_url = vod_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryDeviceVodUrlByTimeResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decrypt_key is not None:
            result['DecryptKey'] = self.decrypt_key
        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DecryptKey') is not None:
            self.decrypt_key = m.get('DecryptKey')
        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryDeviceVodUrlByTimeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryDeviceVodUrlByTimeResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryDeviceVodUrlByTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryDeviceVodUrlByTimeResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryDeviceVodUrlByTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryDeviceVodUrlByTimeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryDeviceVodUrlByTimeResponse, self).to_map()
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
            temp_model = QueryDeviceVodUrlByTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDetailRequest(TeaModel):
    def __init__(self, plan_id=None):
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlanDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryEventRecordPlanDetailResponseBodyDataTemplateInfo(TeaModel):
    def __init__(self, all_day=None, default=None, name=None, template_id=None, time_section_list=None):
        self.all_day = all_day  # type: int
        self.default = default  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_section_list = time_section_list  # type: list[QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList]

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDetailResponseBodyDataTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryEventRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryEventRecordPlanDetailResponseBodyData(TeaModel):
    def __init__(self, name=None, plan_id=None, pre_record_duration=None, record_duration=None, template_id=None,
                 template_info=None):
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.record_duration = record_duration  # type: int
        self.template_id = template_id  # type: str
        self.template_info = template_info  # type: QueryEventRecordPlanDetailResponseBodyDataTemplateInfo

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryEventRecordPlanDetailResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryEventRecordPlanDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryEventRecordPlanDetailResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEventRecordPlanDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDetailResponse, self).to_map()
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
            temp_model = QueryEventRecordPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDeviceByDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo(TeaModel):
    def __init__(self, all_day=None, default=None, name=None, template_id=None, time_section_list=None):
        self.all_day = all_day  # type: int
        self.default = default  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_section_list = time_section_list  # type: list[QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList]

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBodyData(TeaModel):
    def __init__(self, name=None, plan_id=None, pre_record_duration=None, record_duration=None, template_id=None,
                 template_info=None):
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.record_duration = record_duration  # type: int
        self.template_id = template_id  # type: str
        self.template_info = template_info  # type: QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryEventRecordPlanDeviceByDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryEventRecordPlanDeviceByDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDeviceByDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEventRecordPlanDeviceByDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByDeviceResponse, self).to_map()
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
            temp_model = QueryEventRecordPlanDeviceByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlanDeviceByPlanRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, plan_id=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBodyDataList(TeaModel):
    def __init__(self, iot_id=None, stream_type=None):
        self.iot_id = iot_id  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByPlanResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_count=None, page_size=None, total=None):
        self.list = list  # type: list[QueryEventRecordPlanDeviceByPlanResponseBodyDataList]
        self.page = page  # type: int
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEventRecordPlanDeviceByPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryEventRecordPlanDeviceByPlanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryEventRecordPlanDeviceByPlanResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlanDeviceByPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlanDeviceByPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEventRecordPlanDeviceByPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlanDeviceByPlanResponse, self).to_map()
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
            temp_model = QueryEventRecordPlanDeviceByPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryEventRecordPlansRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryEventRecordPlansResponseBodyDataList(TeaModel):
    def __init__(self, event_type=None, name=None, plan_id=None, pre_record_duration=None, record_duration=None,
                 template_id=None):
        self.event_type = event_type  # type: str
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.record_duration = record_duration  # type: int
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryEventRecordPlansResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryEventRecordPlansResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_count=None, page_size=None, total=None):
        self.list = list  # type: list[QueryEventRecordPlansResponseBodyDataList]
        self.page = page  # type: int
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlansResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryEventRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryEventRecordPlansResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryEventRecordPlansResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryEventRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryEventRecordPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryEventRecordPlansResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryEventRecordPlansResponse, self).to_map()
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
            temp_model = QueryEventRecordPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllDeviceGroupRequest(TeaModel):
    def __init__(self, iot_instance_id=None, isolation_id=None, page_no=None, page_size=None):
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllDeviceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList(TeaModel):
    def __init__(self, device_group_id=None, device_group_name=None, modified_time=None):
        self.device_group_id = device_group_id  # type: str
        self.device_group_name = device_group_name  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class QueryFaceAllDeviceGroupResponseBodyData(TeaModel):
    def __init__(self, device_group_list=None, page_no=None, page_size=None, total=None):
        self.device_group_list = device_group_list  # type: list[QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.device_group_list:
            for k in self.device_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceAllDeviceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceGroupList'] = []
        if self.device_group_list is not None:
            for k in self.device_group_list:
                result['DeviceGroupList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_group_list = []
        if m.get('DeviceGroupList') is not None:
            for k in m.get('DeviceGroupList'):
                temp_model = QueryFaceAllDeviceGroupResponseBodyDataDeviceGroupList()
                self.device_group_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllDeviceGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceAllDeviceGroupResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceAllDeviceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllDeviceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllDeviceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceAllDeviceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceAllDeviceGroupResponse, self).to_map()
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
            temp_model = QueryFaceAllDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserGroupRequest(TeaModel):
    def __init__(self, isolation_id=None, page_no=None, page_size=None):
        self.isolation_id = isolation_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryFaceAllUserGroupResponseBodyDataUserGroupList(TeaModel):
    def __init__(self, modified_time=None, user_group_id=None, user_group_name=None):
        self.modified_time = modified_time  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllUserGroupResponseBodyDataUserGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class QueryFaceAllUserGroupResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total=None, user_group_list=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.user_group_list = user_group_list  # type: list[QueryFaceAllUserGroupResponseBodyDataUserGroupList]

    def validate(self):
        if self.user_group_list:
            for k in self.user_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = QueryFaceAllUserGroupResponseBodyDataUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        return self


class QueryFaceAllUserGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceAllUserGroupResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceAllUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserGroupResponse, self).to_map()
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
            temp_model = QueryFaceAllUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(self, isolation_id=None, page_no=None, page_size=None):
        self.isolation_id = isolation_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllUserGroupAndDeviceGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList(TeaModel):
    def __init__(self, control_id=None, control_type=None, device_group_id=None, modified_time=None,
                 user_group_id=None):
        self.control_id = control_id  # type: str
        self.control_type = control_type  # type: str
        self.device_group_id = device_group_id  # type: str
        self.modified_time = modified_time  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_size=None, total=None):
        self.list = list  # type: list[QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserGroupAndDeviceGroupRelationResponse, self).to_map()
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
            temp_model = QueryFaceAllUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceAllUserIdsByGroupIdRequest(TeaModel):
    def __init__(self, isolation_id=None, page_no=None, page_size=None, user_group_id=None):
        self.isolation_id = isolation_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllUserIdsByGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBodyDataList(TeaModel):
    def __init__(self, custom_user_id=None, name=None, params=None, user_id=None):
        self.custom_user_id = custom_user_id  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceAllUserIdsByGroupIdResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_size=None, total=None):
        self.list = list  # type: list[QueryFaceAllUserIdsByGroupIdResponseBodyDataList]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserIdsByGroupIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceAllUserIdsByGroupIdResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceAllUserIdsByGroupIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceAllUserIdsByGroupIdResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserIdsByGroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceAllUserIdsByGroupIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceAllUserIdsByGroupIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceAllUserIdsByGroupIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceAllUserIdsByGroupIdResponse, self).to_map()
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
            temp_model = QueryFaceAllUserIdsByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceCustomUserIdByUserIdRequest(TeaModel):
    def __init__(self, isolation_id=None, user_id=None):
        self.isolation_id = isolation_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceCustomUserIdByUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceCustomUserIdByUserIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceCustomUserIdByUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceCustomUserIdByUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceCustomUserIdByUserIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceCustomUserIdByUserIdResponse, self).to_map()
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
            temp_model = QueryFaceCustomUserIdByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceDeviceGroupsByDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_instance_id=None, isolation_id=None, page_no=None, page_size=None,
                 product_key=None):
        self.device_name = device_name  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceDeviceGroupsByDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList(TeaModel):
    def __init__(self, device_group_id=None, device_group_name=None, modified_time=None):
        self.device_group_id = device_group_id  # type: str
        self.device_group_name = device_group_name  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_group_name is not None:
            result['DeviceGroupName'] = self.device_group_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceGroupName') is not None:
            self.device_group_name = m.get('DeviceGroupName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBodyData(TeaModel):
    def __init__(self, device_group_list=None, page_no=None, page_size=None, total=None):
        self.device_group_list = device_group_list  # type: list[QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.device_group_list:
            for k in self.device_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceDeviceGroupsByDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceGroupList'] = []
        if self.device_group_list is not None:
            for k in self.device_group_list:
                result['DeviceGroupList'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_group_list = []
        if m.get('DeviceGroupList') is not None:
            for k in m.get('DeviceGroupList'):
                temp_model = QueryFaceDeviceGroupsByDeviceResponseBodyDataDeviceGroupList()
                self.device_group_list.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceDeviceGroupsByDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceDeviceGroupsByDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceDeviceGroupsByDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceDeviceGroupsByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceDeviceGroupsByDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceDeviceGroupsByDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceDeviceGroupsByDeviceResponse, self).to_map()
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
            temp_model = QueryFaceDeviceGroupsByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserRequest(TeaModel):
    def __init__(self, isolation_id=None, user_id=None):
        self.isolation_id = isolation_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserResponseBodyDataFacePicListFeatureDTOList(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, algorithm_version=None, error_code=None,
                 error_message=None, face_md_5=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_version = algorithm_version  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.face_md_5 = face_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserResponseBodyDataFacePicListFeatureDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserResponseBodyDataFacePicList(TeaModel):
    def __init__(self, face_md_5=None, face_url=None, feature_dtolist=None):
        self.face_md_5 = face_md_5  # type: str
        self.face_url = face_url  # type: str
        self.feature_dtolist = feature_dtolist  # type: list[QueryFaceUserResponseBodyDataFacePicListFeatureDTOList]

    def validate(self):
        if self.feature_dtolist:
            for k in self.feature_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserResponseBodyDataFacePicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserResponseBodyDataFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        return self


class QueryFaceUserResponseBodyData(TeaModel):
    def __init__(self, custom_user_id=None, face_pic_list=None, name=None, params=None, user_id=None):
        self.custom_user_id = custom_user_id  # type: str
        self.face_pic_list = face_pic_list  # type: list[QueryFaceUserResponseBodyDataFacePicList]
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.face_pic_list:
            for k in self.face_pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserResponseBodyDataFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceUserResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceUserResponse, self).to_map()
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
            temp_model = QueryFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserBatchRequest(TeaModel):
    def __init__(self, isolation_id=None, user_id_list=None):
        self.isolation_id = isolation_id  # type: str
        self.user_id_list = user_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserBatchRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_id_list is not None:
            result['UserIdList'] = self.user_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserIdList') is not None:
            self.user_id_list = m.get('UserIdList')
        return self


class QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, algorithm_version=None, error_code=None,
                 error_message=None, face_md_5=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_version = algorithm_version  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.face_md_5 = face_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserBatchResponseBodyDataFacePicList(TeaModel):
    def __init__(self, face_md_5=None, face_url=None, feature_dtolist=None):
        self.face_md_5 = face_md_5  # type: str
        self.face_url = face_url  # type: str
        self.feature_dtolist = feature_dtolist  # type: list[QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList]

    def validate(self):
        if self.feature_dtolist:
            for k in self.feature_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserBatchResponseBodyDataFacePicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserBatchResponseBodyDataFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        return self


class QueryFaceUserBatchResponseBodyData(TeaModel):
    def __init__(self, create_time=None, custom_user_id=None, face_pic_list=None, modify_time=None, name=None,
                 params=None, user_id=None):
        self.create_time = create_time  # type: long
        self.custom_user_id = custom_user_id  # type: str
        self.face_pic_list = face_pic_list  # type: list[QueryFaceUserBatchResponseBodyDataFacePicList]
        self.modify_time = modify_time  # type: long
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.face_pic_list:
            for k in self.face_pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserBatchResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserBatchResponseBodyDataFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserBatchResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[QueryFaceUserBatchResponseBodyData]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserBatchResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryFaceUserBatchResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserBatchResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceUserBatchResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceUserBatchResponse, self).to_map()
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
            temp_model = QueryFaceUserBatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserByNameRequest(TeaModel):
    def __init__(self, isolation_id=None, name=None, page_no=None, page_size=None, params=None):
        self.isolation_id = isolation_id  # type: str
        self.name = name  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.params = params  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserByNameRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.name is not None:
            result['Name'] = self.name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.params is not None:
            result['Params'] = self.params
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        return self


class QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList(TeaModel):
    def __init__(self, algorithm_name=None, algorithm_provider=None, algorithm_version=None, error_code=None,
                 error_message=None, face_md_5=None):
        self.algorithm_name = algorithm_name  # type: str
        self.algorithm_provider = algorithm_provider  # type: str
        self.algorithm_version = algorithm_version  # type: str
        self.error_code = error_code  # type: str
        self.error_message = error_message  # type: str
        self.face_md_5 = face_md_5  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name
        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider
        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')
        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')
        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        return self


class QueryFaceUserByNameResponseBodyDataListFacePicList(TeaModel):
    def __init__(self, face_md_5=None, face_url=None, feature_dtolist=None):
        self.face_md_5 = face_md_5  # type: str
        self.face_url = face_url  # type: str
        self.feature_dtolist = feature_dtolist  # type: list[QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList]

    def validate(self):
        if self.feature_dtolist:
            for k in self.feature_dtolist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserByNameResponseBodyDataListFacePicList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_md_5 is not None:
            result['FaceMd5'] = self.face_md_5
        if self.face_url is not None:
            result['FaceUrl'] = self.face_url
        result['FeatureDTOList'] = []
        if self.feature_dtolist is not None:
            for k in self.feature_dtolist:
                result['FeatureDTOList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FaceMd5') is not None:
            self.face_md_5 = m.get('FaceMd5')
        if m.get('FaceUrl') is not None:
            self.face_url = m.get('FaceUrl')
        self.feature_dtolist = []
        if m.get('FeatureDTOList') is not None:
            for k in m.get('FeatureDTOList'):
                temp_model = QueryFaceUserByNameResponseBodyDataListFacePicListFeatureDTOList()
                self.feature_dtolist.append(temp_model.from_map(k))
        return self


class QueryFaceUserByNameResponseBodyDataList(TeaModel):
    def __init__(self, create_time=None, custom_user_id=None, face_pic_list=None, modify_time=None, name=None,
                 params=None, user_id=None):
        self.create_time = create_time  # type: long
        self.custom_user_id = custom_user_id  # type: str
        self.face_pic_list = face_pic_list  # type: list[QueryFaceUserByNameResponseBodyDataListFacePicList]
        self.modify_time = modify_time  # type: long
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        if self.face_pic_list:
            for k in self.face_pic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserByNameResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        result['FacePicList'] = []
        if self.face_pic_list is not None:
            for k in self.face_pic_list:
                result['FacePicList'].append(k.to_map() if k else None)
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        self.face_pic_list = []
        if m.get('FacePicList') is not None:
            for k in m.get('FacePicList'):
                temp_model = QueryFaceUserByNameResponseBodyDataListFacePicList()
                self.face_pic_list.append(temp_model.from_map(k))
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserByNameResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_size=None, total=None):
        self.list = list  # type: list[QueryFaceUserByNameResponseBodyDataList]
        self.page = page  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserByNameResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryFaceUserByNameResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryFaceUserByNameResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceUserByNameResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceUserByNameResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserByNameResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserByNameResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceUserByNameResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceUserByNameResponse, self).to_map()
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
            temp_model = QueryFaceUserByNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserGroupRequest(TeaModel):
    def __init__(self, isolation_id=None, page_no=None, page_size=None, user_id=None):
        self.isolation_id = isolation_id  # type: str
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserGroupResponseBodyDataUserGroupList(TeaModel):
    def __init__(self, modified_time=None, user_group_id=None, user_group_name=None):
        self.modified_time = modified_time  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserGroupResponseBodyDataUserGroupList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class QueryFaceUserGroupResponseBodyData(TeaModel):
    def __init__(self, page_no=None, page_size=None, total=None, user_group_list=None):
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int
        self.user_group_list = user_group_list  # type: list[QueryFaceUserGroupResponseBodyDataUserGroupList]

    def validate(self):
        if self.user_group_list:
            for k in self.user_group_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryFaceUserGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['UserGroupList'] = []
        if self.user_group_list is not None:
            for k in self.user_group_list:
                result['UserGroupList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.user_group_list = []
        if m.get('UserGroupList') is not None:
            for k in m.get('UserGroupList'):
                temp_model = QueryFaceUserGroupResponseBodyDataUserGroupList()
                self.user_group_list.append(temp_model.from_map(k))
        return self


class QueryFaceUserGroupResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceUserGroupResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceUserGroupResponse, self).to_map()
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
            temp_model = QueryFaceUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(self, control_id=None, isolation_id=None):
        self.control_id = control_id  # type: str
        self.isolation_id = isolation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserGroupAndDeviceGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(self, control_id=None, control_type=None, device_group_id=None, modified_time=None,
                 user_group_id=None):
        self.control_id = control_id  # type: str
        self.control_type = control_type  # type: str
        self.device_group_id = device_group_id  # type: str
        self.modified_time = modified_time  # type: str
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.control_type is not None:
            result['ControlType'] = self.control_type
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ControlType') is not None:
            self.control_type = m.get('ControlType')
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceUserGroupAndDeviceGroupRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceUserGroupAndDeviceGroupRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceUserGroupAndDeviceGroupRelationResponse, self).to_map()
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
            temp_model = QueryFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryFaceUserIdByCustomUserIdRequest(TeaModel):
    def __init__(self, custom_user_id=None, isolation_id=None):
        self.custom_user_id = custom_user_id  # type: str
        self.isolation_id = isolation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserIdByCustomUserIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        return self


class QueryFaceUserIdByCustomUserIdResponseBodyData(TeaModel):
    def __init__(self, custom_user_id=None, name=None, params=None, user_id=None):
        self.custom_user_id = custom_user_id  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryFaceUserIdByCustomUserIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class QueryFaceUserIdByCustomUserIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryFaceUserIdByCustomUserIdResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryFaceUserIdByCustomUserIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryFaceUserIdByCustomUserIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryFaceUserIdByCustomUserIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryFaceUserIdByCustomUserIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryFaceUserIdByCustomUserIdResponse, self).to_map()
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
            temp_model = QueryFaceUserIdByCustomUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryGbSubDeviceListRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, page_size=None, page_start=None,
                 product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int
        self.page_start = page_start  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGbSubDeviceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_start is not None:
            result['PageStart'] = self.page_start
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageStart') is not None:
            self.page_start = m.get('PageStart')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryGbSubDeviceListResponseBodyDataGbSubDeviceList(TeaModel):
    def __init__(self, device_enable=None, device_id=None, device_name=None, iot_id=None, product_key=None):
        self.device_enable = device_enable  # type: int
        self.device_id = device_id  # type: str
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryGbSubDeviceListResponseBodyDataGbSubDeviceList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_enable is not None:
            result['DeviceEnable'] = self.device_enable
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceEnable') is not None:
            self.device_enable = m.get('DeviceEnable')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryGbSubDeviceListResponseBodyData(TeaModel):
    def __init__(self, gb_sub_device_list=None, total=None):
        self.gb_sub_device_list = gb_sub_device_list  # type: list[QueryGbSubDeviceListResponseBodyDataGbSubDeviceList]
        self.total = total  # type: int

    def validate(self):
        if self.gb_sub_device_list:
            for k in self.gb_sub_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryGbSubDeviceListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['GbSubDeviceList'] = []
        if self.gb_sub_device_list is not None:
            for k in self.gb_sub_device_list:
                result['GbSubDeviceList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.gb_sub_device_list = []
        if m.get('GbSubDeviceList') is not None:
            for k in m.get('GbSubDeviceList'):
                temp_model = QueryGbSubDeviceListResponseBodyDataGbSubDeviceList()
                self.gb_sub_device_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryGbSubDeviceListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryGbSubDeviceListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryGbSubDeviceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryGbSubDeviceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryGbSubDeviceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryGbSubDeviceListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryGbSubDeviceListResponse, self).to_map()
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
            temp_model = QueryGbSubDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLiveStreamingRequest(TeaModel):
    def __init__(self, cache_duration=None, device_name=None, enable_stun=None, encrypt_type=None,
                 force_iframe=None, iot_id=None, iot_instance_id=None, play_un_limited=None, product_key=None, scheme=None,
                 should_encrypt=None, stream_type=None, url_valid_duration=None):
        self.cache_duration = cache_duration  # type: int
        self.device_name = device_name  # type: str
        self.enable_stun = enable_stun  # type: bool
        self.encrypt_type = encrypt_type  # type: int
        self.force_iframe = force_iframe  # type: bool
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.play_un_limited = play_un_limited  # type: bool
        self.product_key = product_key  # type: str
        self.scheme = scheme  # type: str
        self.should_encrypt = should_encrypt  # type: bool
        self.stream_type = stream_type  # type: int
        self.url_valid_duration = url_valid_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLiveStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cache_duration is not None:
            result['CacheDuration'] = self.cache_duration
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.enable_stun is not None:
            result['EnableStun'] = self.enable_stun
        if self.encrypt_type is not None:
            result['EncryptType'] = self.encrypt_type
        if self.force_iframe is not None:
            result['ForceIFrame'] = self.force_iframe
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.play_un_limited is not None:
            result['PlayUnLimited'] = self.play_un_limited
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        if self.should_encrypt is not None:
            result['ShouldEncrypt'] = self.should_encrypt
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CacheDuration') is not None:
            self.cache_duration = m.get('CacheDuration')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EnableStun') is not None:
            self.enable_stun = m.get('EnableStun')
        if m.get('EncryptType') is not None:
            self.encrypt_type = m.get('EncryptType')
        if m.get('ForceIFrame') is not None:
            self.force_iframe = m.get('ForceIFrame')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PlayUnLimited') is not None:
            self.play_un_limited = m.get('PlayUnLimited')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        if m.get('ShouldEncrypt') is not None:
            self.should_encrypt = m.get('ShouldEncrypt')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryLiveStreamingResponseBodyData(TeaModel):
    def __init__(self, path=None, relay_decrypt_key=None, stun_info=None):
        self.path = path  # type: str
        self.relay_decrypt_key = relay_decrypt_key  # type: str
        self.stun_info = stun_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLiveStreamingResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['Path'] = self.path
        if self.relay_decrypt_key is not None:
            result['RelayDecryptKey'] = self.relay_decrypt_key
        if self.stun_info is not None:
            result['StunInfo'] = self.stun_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')
        if m.get('RelayDecryptKey') is not None:
            self.relay_decrypt_key = m.get('RelayDecryptKey')
        if m.get('StunInfo') is not None:
            self.stun_info = m.get('StunInfo')
        return self


class QueryLiveStreamingResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryLiveStreamingResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryLiveStreamingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryLiveStreamingResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLiveStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryLiveStreamingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryLiveStreamingResponse, self).to_map()
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
            temp_model = QueryLiveStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryLocalFileUploadJobRequest(TeaModel):
    def __init__(self, iot_instance_id=None, job_id=None):
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLocalFileUploadJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryLocalFileUploadJobResponseBodyDataResultListFileList(TeaModel):
    def __init__(self, file_end_time=None, file_name=None, file_start_time=None):
        self.file_end_time = file_end_time  # type: int
        self.file_name = file_name  # type: str
        self.file_start_time = file_start_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryLocalFileUploadJobResponseBodyDataResultListFileList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_end_time is not None:
            result['FileEndTime'] = self.file_end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_start_time is not None:
            result['FileStartTime'] = self.file_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileEndTime') is not None:
            self.file_end_time = m.get('FileEndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileStartTime') is not None:
            self.file_start_time = m.get('FileStartTime')
        return self


class QueryLocalFileUploadJobResponseBodyDataResultList(TeaModel):
    def __init__(self, code=None, device_name=None, file_list=None, iot_id=None, product_key=None,
                 slot_end_time=None, slot_start_time=None, slot_status=None):
        self.code = code  # type: int
        self.device_name = device_name  # type: str
        self.file_list = file_list  # type: list[QueryLocalFileUploadJobResponseBodyDataResultListFileList]
        self.iot_id = iot_id  # type: str
        self.product_key = product_key  # type: str
        self.slot_end_time = slot_end_time  # type: int
        self.slot_start_time = slot_start_time  # type: int
        self.slot_status = slot_status  # type: int

    def validate(self):
        if self.file_list:
            for k in self.file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryLocalFileUploadJobResponseBodyDataResultList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        result['FileList'] = []
        if self.file_list is not None:
            for k in self.file_list:
                result['FileList'].append(k.to_map() if k else None)
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.slot_end_time is not None:
            result['SlotEndTime'] = self.slot_end_time
        if self.slot_start_time is not None:
            result['SlotStartTime'] = self.slot_start_time
        if self.slot_status is not None:
            result['SlotStatus'] = self.slot_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        self.file_list = []
        if m.get('FileList') is not None:
            for k in m.get('FileList'):
                temp_model = QueryLocalFileUploadJobResponseBodyDataResultListFileList()
                self.file_list.append(temp_model.from_map(k))
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SlotEndTime') is not None:
            self.slot_end_time = m.get('SlotEndTime')
        if m.get('SlotStartTime') is not None:
            self.slot_start_time = m.get('SlotStartTime')
        if m.get('SlotStatus') is not None:
            self.slot_status = m.get('SlotStatus')
        return self


class QueryLocalFileUploadJobResponseBodyData(TeaModel):
    def __init__(self, result_list=None, status=None):
        self.result_list = result_list  # type: list[QueryLocalFileUploadJobResponseBodyDataResultList]
        self.status = status  # type: int

    def validate(self):
        if self.result_list:
            for k in self.result_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryLocalFileUploadJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ResultList'] = []
        if self.result_list is not None:
            for k in self.result_list:
                result['ResultList'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.result_list = []
        if m.get('ResultList') is not None:
            for k in m.get('ResultList'):
                temp_model = QueryLocalFileUploadJobResponseBodyDataResultList()
                self.result_list.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class QueryLocalFileUploadJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryLocalFileUploadJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryLocalFileUploadJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryLocalFileUploadJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryLocalFileUploadJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryLocalFileUploadJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryLocalFileUploadJobResponse, self).to_map()
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
            temp_model = QueryLocalFileUploadJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMonthRecordRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, month=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.month = month  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonthRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.month is not None:
            result['Month'] = self.month
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryMonthRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMonthRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryMonthRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMonthRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMonthRecordResponse, self).to_map()
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
            temp_model = QueryMonthRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureFilesRequest(TeaModel):
    def __init__(self, begin_time=None, current_page=None, device_name=None, end_time=None, iot_id=None,
                 iot_instance_id=None, page_size=None, picture_source=None, picture_type=None, product_key=None):
        self.begin_time = begin_time  # type: long
        self.current_page = current_page  # type: int
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: long
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int
        self.picture_source = picture_source  # type: int
        self.picture_type = picture_type  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureFilesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.picture_source is not None:
            result['PictureSource'] = self.picture_source
        if self.picture_type is not None:
            result['PictureType'] = self.picture_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PictureSource') is not None:
            self.picture_source = m.get('PictureSource')
        if m.get('PictureType') is not None:
            self.picture_type = m.get('PictureType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryPictureFilesResponseBodyDataList(TeaModel):
    def __init__(self, iot_id=None, pic_create_time=None, pic_id=None, pic_url=None, thumb_url=None):
        self.iot_id = iot_id  # type: str
        self.pic_create_time = pic_create_time  # type: long
        self.pic_id = pic_id  # type: str
        self.pic_url = pic_url  # type: str
        self.thumb_url = thumb_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureFilesResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_create_time is not None:
            result['PicCreateTime'] = self.pic_create_time
        if self.pic_id is not None:
            result['PicId'] = self.pic_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.thumb_url is not None:
            result['ThumbUrl'] = self.thumb_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicCreateTime') is not None:
            self.pic_create_time = m.get('PicCreateTime')
        if m.get('PicId') is not None:
            self.pic_id = m.get('PicId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('ThumbUrl') is not None:
            self.thumb_url = m.get('ThumbUrl')
        return self


class QueryPictureFilesResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_size=None):
        self.list = list  # type: list[QueryPictureFilesResponseBodyDataList]
        self.page = page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPictureFilesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryPictureFilesResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureFilesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPictureFilesResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPictureFilesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureFilesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureFilesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPictureFilesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPictureFilesResponse, self).to_map()
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
            temp_model = QueryPictureFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAiboxesRequest(TeaModel):
    def __init__(self, app_instance_id=None, current_page=None, iot_instance_id=None, page_size=None):
        self.app_instance_id = app_instance_id  # type: str
        self.current_page = current_page  # type: int
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchAiboxesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchAiboxesResponseBodyDataPageData(TeaModel):
    def __init__(self, iot_id=None, nick_name=None):
        self.iot_id = iot_id  # type: str
        self.nick_name = nick_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchAiboxesResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        return self


class QueryPictureSearchAiboxesResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[QueryPictureSearchAiboxesResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPictureSearchAiboxesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchAiboxesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchAiboxesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPictureSearchAiboxesResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPictureSearchAiboxesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchAiboxesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAiboxesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPictureSearchAiboxesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPictureSearchAiboxesResponse, self).to_map()
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
            temp_model = QueryPictureSearchAiboxesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchAppsRequest(TeaModel):
    def __init__(self, current_page=None, iot_instance_id=None, page_size=None):
        self.current_page = current_page  # type: int
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchAppsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchAppsResponseBodyDataPageData(TeaModel):
    def __init__(self, app_instance_id=None, app_template_id=None, create_time=None, description=None,
                 modified_time=None, name=None, version=None):
        self.app_instance_id = app_instance_id  # type: str
        self.app_template_id = app_template_id  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.modified_time = modified_time  # type: long
        self.name = name  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchAppsResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class QueryPictureSearchAppsResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[QueryPictureSearchAppsResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPictureSearchAppsResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchAppsResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchAppsResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPictureSearchAppsResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPictureSearchAppsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchAppsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchAppsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPictureSearchAppsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPictureSearchAppsResponse, self).to_map()
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
            temp_model = QueryPictureSearchAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchDevicesRequest(TeaModel):
    def __init__(self, app_instance_id=None, current_page=None, page_size=None):
        self.app_instance_id = app_instance_id  # type: str
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchDevicesResponseBodyDataPageData(TeaModel):
    def __init__(self, iot_id=None, nick_name=None):
        self.iot_id = iot_id  # type: str
        self.nick_name = nick_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchDevicesResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        return self


class QueryPictureSearchDevicesResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[QueryPictureSearchDevicesResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPictureSearchDevicesResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchDevicesResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchDevicesResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPictureSearchDevicesResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPictureSearchDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchDevicesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPictureSearchDevicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPictureSearchDevicesResponse, self).to_map()
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
            temp_model = QueryPictureSearchDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchJobRequest(TeaModel):
    def __init__(self, app_instance_id=None, current_page=None, job_status=None, page_size=None):
        self.app_instance_id = app_instance_id  # type: str
        self.current_page = current_page  # type: int
        self.job_status = job_status  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchJobResponseBodyDataPageData(TeaModel):
    def __init__(self, create_time=None, end_time=None, job_id=None, job_status=None, search_pic_url=None,
                 start_time=None, threshold=None):
        self.create_time = create_time  # type: long
        self.end_time = end_time  # type: long
        self.job_id = job_id  # type: str
        self.job_status = job_status  # type: int
        self.search_pic_url = search_pic_url  # type: str
        self.start_time = start_time  # type: long
        self.threshold = threshold  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchJobResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.search_pic_url is not None:
            result['SearchPicUrl'] = self.search_pic_url
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('SearchPicUrl') is not None:
            self.search_pic_url = m.get('SearchPicUrl')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        return self


class QueryPictureSearchJobResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[QueryPictureSearchJobResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPictureSearchJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchJobResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPictureSearchJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPictureSearchJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPictureSearchJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPictureSearchJobResponse, self).to_map()
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
            temp_model = QueryPictureSearchJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryPictureSearchJobResultRequest(TeaModel):
    def __init__(self, app_instance_id=None, current_page=None, job_id=None, page_size=None):
        self.app_instance_id = app_instance_id  # type: str
        self.current_page = current_page  # type: int
        self.job_id = job_id  # type: str
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchJobResultRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryPictureSearchJobResultResponseBodyDataPageData(TeaModel):
    def __init__(self, device_nick_name=None, event_time=None, gateway_iot_id=None, iot_id=None, pic_url=None,
                 threshold=None, vector_id=None):
        self.device_nick_name = device_nick_name  # type: str
        self.event_time = event_time  # type: long
        self.gateway_iot_id = gateway_iot_id  # type: str
        self.iot_id = iot_id  # type: str
        self.pic_url = pic_url  # type: str
        self.threshold = threshold  # type: float
        self.vector_id = vector_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryPictureSearchJobResultResponseBodyDataPageData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_nick_name is not None:
            result['DeviceNickName'] = self.device_nick_name
        if self.event_time is not None:
            result['EventTime'] = self.event_time
        if self.gateway_iot_id is not None:
            result['GatewayIotId'] = self.gateway_iot_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.pic_url is not None:
            result['PicUrl'] = self.pic_url
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.vector_id is not None:
            result['VectorId'] = self.vector_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNickName') is not None:
            self.device_nick_name = m.get('DeviceNickName')
        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')
        if m.get('GatewayIotId') is not None:
            self.gateway_iot_id = m.get('GatewayIotId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('PicUrl') is not None:
            self.pic_url = m.get('PicUrl')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('VectorId') is not None:
            self.vector_id = m.get('VectorId')
        return self


class QueryPictureSearchJobResultResponseBodyData(TeaModel):
    def __init__(self, current_page=None, page_count=None, page_data=None, page_size=None, total=None):
        self.current_page = current_page  # type: int
        self.page_count = page_count  # type: int
        self.page_data = page_data  # type: list[QueryPictureSearchJobResultResponseBodyDataPageData]
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.page_data:
            for k in self.page_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryPictureSearchJobResultResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        result['PageData'] = []
        if self.page_data is not None:
            for k in self.page_data:
                result['PageData'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        self.page_data = []
        if m.get('PageData') is not None:
            for k in m.get('PageData'):
                temp_model = QueryPictureSearchJobResultResponseBodyDataPageData()
                self.page_data.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryPictureSearchJobResultResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryPictureSearchJobResultResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryPictureSearchJobResultResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryPictureSearchJobResultResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryPictureSearchJobResultResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryPictureSearchJobResultResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryPictureSearchJobResultResponse, self).to_map()
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
            temp_model = QueryPictureSearchJobResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordRequest(TeaModel):
    def __init__(self, begin_time=None, current_page=None, device_name=None, end_time=None, iot_id=None,
                 iot_instance_id=None, need_snapshot=None, page_size=None, product_key=None, record_type=None, stream_type=None):
        self.begin_time = begin_time  # type: int
        self.current_page = current_page  # type: int
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.need_snapshot = need_snapshot  # type: bool
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str
        self.record_type = record_type  # type: int
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.need_snapshot is not None:
            result['NeedSnapshot'] = self.need_snapshot
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('NeedSnapshot') is not None:
            self.need_snapshot = m.get('NeedSnapshot')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryRecordResponseBodyDataList(TeaModel):
    def __init__(self, begin_time=None, end_time=None, event_type=None, file_name=None, file_size=None,
                 record_type=None, snapshot_url=None, stream_type=None, video_frame_number=None):
        self.begin_time = begin_time  # type: str
        self.end_time = end_time  # type: str
        self.event_type = event_type  # type: int
        self.file_name = file_name  # type: str
        self.file_size = file_size  # type: int
        self.record_type = record_type  # type: int
        self.snapshot_url = snapshot_url  # type: str
        self.stream_type = stream_type  # type: int
        self.video_frame_number = video_frame_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_size is not None:
            result['FileSize'] = self.file_size
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.snapshot_url is not None:
            result['SnapshotUrl'] = self.snapshot_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.video_frame_number is not None:
            result['VideoFrameNumber'] = self.video_frame_number
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileSize') is not None:
            self.file_size = m.get('FileSize')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('SnapshotUrl') is not None:
            self.snapshot_url = m.get('SnapshotUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('VideoFrameNumber') is not None:
            self.video_frame_number = m.get('VideoFrameNumber')
        return self


class QueryRecordResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_size=None):
        self.list = list  # type: list[QueryRecordResponseBodyDataList]
        self.page = page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordResponse, self).to_map()
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
            temp_model = QueryRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordByRecordIdRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, record_id=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordByRecordIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class QueryRecordByRecordIdResponseBodyData(TeaModel):
    def __init__(self, begin_time=None, end_time=None, file_name=None, vod_url=None):
        self.begin_time = begin_time  # type: str
        self.end_time = end_time  # type: str
        self.file_name = file_name  # type: str
        self.vod_url = vod_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordByRecordIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.vod_url is not None:
            result['VodUrl'] = self.vod_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('VodUrl') is not None:
            self.vod_url = m.get('VodUrl')
        return self


class QueryRecordByRecordIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: list[QueryRecordByRecordIdResponseBodyData]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordByRecordIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
                temp_model = QueryRecordByRecordIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordByRecordIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordByRecordIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordByRecordIdResponse, self).to_map()
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
            temp_model = QueryRecordByRecordIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordDownloadJobByIdRequest(TeaModel):
    def __init__(self, iot_instance_id=None, job_id=None):
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordDownloadJobByIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryRecordDownloadJobByIdResponseBodyData(TeaModel):
    def __init__(self, begin_time=None, end_time=None, file_name=None, iot_id=None, job_error_code=None,
                 progress=None, record_type=None, status=None, stream_type=None, type=None, url=None):
        self.begin_time = begin_time  # type: int
        self.end_time = end_time  # type: int
        self.file_name = file_name  # type: str
        self.iot_id = iot_id  # type: str
        self.job_error_code = job_error_code  # type: int
        self.progress = progress  # type: int
        self.record_type = record_type  # type: int
        self.status = status  # type: int
        self.stream_type = stream_type  # type: int
        self.type = type  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordDownloadJobByIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.job_error_code is not None:
            result['JobErrorCode'] = self.job_error_code
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.status is not None:
            result['Status'] = self.status
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('JobErrorCode') is not None:
            self.job_error_code = m.get('JobErrorCode')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRecordDownloadJobByIdResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordDownloadJobByIdResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadJobByIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordDownloadJobByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordDownloadJobByIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordDownloadJobByIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadJobByIdResponse, self).to_map()
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
            temp_model = QueryRecordDownloadJobByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordDownloadJobListRequest(TeaModel):
    def __init__(self, current_page=None, device_name=None, iot_id=None, iot_instance_id=None, page_size=None,
                 product_key=None):
        self.current_page = current_page  # type: int
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordDownloadJobListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryRecordDownloadJobListResponseBodyDataJobList(TeaModel):
    def __init__(self, begin_time=None, end_time=None, file_name=None, iot_id=None, job_error_code=None, job_id=None,
                 progress=None, record_type=None, status=None, stream_type=None, type=None, url=None):
        self.begin_time = begin_time  # type: int
        self.end_time = end_time  # type: int
        self.file_name = file_name  # type: str
        self.iot_id = iot_id  # type: str
        self.job_error_code = job_error_code  # type: int
        self.job_id = job_id  # type: str
        self.progress = progress  # type: int
        self.record_type = record_type  # type: int
        self.status = status  # type: int
        self.stream_type = stream_type  # type: int
        self.type = type  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordDownloadJobListResponseBodyDataJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.job_error_code is not None:
            result['JobErrorCode'] = self.job_error_code
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.record_type is not None:
            result['RecordType'] = self.record_type
        if self.status is not None:
            result['Status'] = self.status
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('JobErrorCode') is not None:
            self.job_error_code = m.get('JobErrorCode')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRecordDownloadJobListResponseBodyData(TeaModel):
    def __init__(self, job_list=None, total=None):
        self.job_list = job_list  # type: list[QueryRecordDownloadJobListResponseBodyDataJobList]
        self.total = total  # type: int

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadJobListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = QueryRecordDownloadJobListResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRecordDownloadJobListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordDownloadJobListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadJobListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordDownloadJobListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordDownloadJobListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordDownloadJobListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadJobListResponse, self).to_map()
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
            temp_model = QueryRecordDownloadJobListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordDownloadUrlRequest(TeaModel):
    def __init__(self, device_name=None, file_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.file_name = file_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordDownloadUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryRecordDownloadUrlResponseBodyData(TeaModel):
    def __init__(self, progress=None, status=None, url=None):
        self.progress = progress  # type: int
        self.status = status  # type: int
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordDownloadUrlResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryRecordDownloadUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordDownloadUrlResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordDownloadUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordDownloadUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordDownloadUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordDownloadUrlResponse, self).to_map()
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
            temp_model = QueryRecordDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDetailRequest(TeaModel):
    def __init__(self, plan_id=None):
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlanDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryRecordPlanDetailResponseBodyDataTemplateInfo(TeaModel):
    def __init__(self, all_day=None, default=None, name=None, template_id=None, time_section_list=None):
        self.all_day = all_day  # type: int
        self.default = default  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_section_list = time_section_list  # type: list[QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList]

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDetailResponseBodyDataTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryRecordPlanDetailResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryRecordPlanDetailResponseBodyData(TeaModel):
    def __init__(self, name=None, plan_id=None, template_id=None, template_info=None):
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.template_id = template_id  # type: str
        self.template_info = template_info  # type: QueryRecordPlanDetailResponseBodyDataTemplateInfo

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryRecordPlanDetailResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryRecordPlanDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordPlanDetailResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlanDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordPlanDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDetailResponse, self).to_map()
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
            temp_model = QueryRecordPlanDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDeviceByDeviceRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo(TeaModel):
    def __init__(self, all_day=None, default=None, name=None, template_id=None, time_section_list=None):
        self.all_day = all_day  # type: int
        self.default = default  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_section_list = time_section_list  # type: list[QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList]

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfoTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryRecordPlanDeviceByDeviceResponseBodyData(TeaModel):
    def __init__(self, name=None, plan_id=None, template_id=None, template_info=None):
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.template_id = template_id  # type: str
        self.template_info = template_info  # type: QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo

    def validate(self):
        if self.template_info:
            self.template_info.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByDeviceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateInfo') is not None:
            temp_model = QueryRecordPlanDeviceByDeviceResponseBodyDataTemplateInfo()
            self.template_info = temp_model.from_map(m['TemplateInfo'])
        return self


class QueryRecordPlanDeviceByDeviceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordPlanDeviceByDeviceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlanDeviceByDeviceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDeviceByDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordPlanDeviceByDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByDeviceResponse, self).to_map()
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
            temp_model = QueryRecordPlanDeviceByDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlanDeviceByPlanRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None, plan_id=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.plan_id = plan_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        return self


class QueryRecordPlanDeviceByPlanResponseBodyDataList(TeaModel):
    def __init__(self, iot_id=None, stream_type=None):
        self.iot_id = iot_id  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByPlanResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryRecordPlanDeviceByPlanResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_count=None, page_size=None, total=None):
        self.list = list  # type: list[QueryRecordPlanDeviceByPlanResponseBodyDataList]
        self.page = page  # type: int
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByPlanResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordPlanDeviceByPlanResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRecordPlanDeviceByPlanResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordPlanDeviceByPlanResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlanDeviceByPlanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlanDeviceByPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordPlanDeviceByPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordPlanDeviceByPlanResponse, self).to_map()
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
            temp_model = QueryRecordPlanDeviceByPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordPlansRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlansRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryRecordPlansResponseBodyDataList(TeaModel):
    def __init__(self, name=None, plan_id=None, template_id=None):
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordPlansResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryRecordPlansResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_count=None, page_size=None, total=None):
        self.list = list  # type: list[QueryRecordPlansResponseBodyDataList]
        self.page = page  # type: int
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryRecordPlansResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryRecordPlansResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryRecordPlansResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRecordPlansResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRecordPlansResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRecordPlansResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordPlansResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordPlansResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordPlansResponse, self).to_map()
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
            temp_model = QueryRecordPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordUrlRequest(TeaModel):
    def __init__(self, device_name=None, file_name=None, iot_id=None, iot_instance_id=None, product_key=None,
                 seek_time=None, url_valid_duration=None):
        self.device_name = device_name  # type: str
        self.file_name = file_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.seek_time = seek_time  # type: int
        self.url_valid_duration = url_valid_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordUrlRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.seek_time is not None:
            result['SeekTime'] = self.seek_time
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SeekTime') is not None:
            self.seek_time = m.get('SeekTime')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryRecordUrlResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordUrlResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordUrlResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordUrlResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordUrlResponse, self).to_map()
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
            temp_model = QueryRecordUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRecordUrlByTimeRequest(TeaModel):
    def __init__(self, begin_time=None, device_name=None, end_time=None, iot_id=None, iot_instance_id=None,
                 product_key=None, stream_type=None, url_valid_duration=None):
        self.begin_time = begin_time  # type: int
        self.device_name = device_name  # type: str
        self.end_time = end_time  # type: int
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int
        self.url_valid_duration = url_valid_duration  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordUrlByTimeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        if self.url_valid_duration is not None:
            result['UrlValidDuration'] = self.url_valid_duration
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        if m.get('UrlValidDuration') is not None:
            self.url_valid_duration = m.get('UrlValidDuration')
        return self


class QueryRecordUrlByTimeResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRecordUrlByTimeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRecordUrlByTimeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRecordUrlByTimeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRecordUrlByTimeResponse, self).to_map()
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
            temp_model = QueryRecordUrlByTimeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryRtmpKeyRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRtmpKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryRtmpKeyResponseBodyData(TeaModel):
    def __init__(self, pull_auth_key=None, pull_key_expire_time=None, push_auth_key=None,
                 push_key_expire_time=None, stream_name=None):
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_key_expire_time = pull_key_expire_time  # type: int
        self.push_auth_key = push_auth_key  # type: str
        self.push_key_expire_time = push_key_expire_time  # type: int
        self.stream_name = stream_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryRtmpKeyResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        return self


class QueryRtmpKeyResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryRtmpKeyResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryRtmpKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryRtmpKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryRtmpKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryRtmpKeyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryRtmpKeyResponse, self).to_map()
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
            temp_model = QueryRtmpKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStreamPushJobRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, job_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_id = job_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStreamPushJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStreamPushJobResponseBodyData(TeaModel):
    def __init__(self, create_time=None, job_type=None, push_status=None, push_url=None, stream_type=None):
        self.create_time = create_time  # type: int
        self.job_type = job_type  # type: int
        self.push_status = push_status  # type: int
        self.push_url = push_url  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStreamPushJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.push_status is not None:
            result['PushStatus'] = self.push_status
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryStreamPushJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryStreamPushJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryStreamPushJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStreamPushJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStreamPushJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStreamPushJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStreamPushJobResponse, self).to_map()
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
            temp_model = QueryStreamPushJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStreamPushJobListRequest(TeaModel):
    def __init__(self, current_page=None, device_name=None, iot_id=None, iot_instance_id=None, job_type=None,
                 page_size=None, product_key=None):
        self.current_page = current_page  # type: int
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.job_type = job_type  # type: int
        self.page_size = page_size  # type: int
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStreamPushJobListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStreamPushJobListResponseBodyDataJobList(TeaModel):
    def __init__(self, create_time=None, job_id=None, job_type=None, push_status=None, push_url=None,
                 stream_type=None):
        self.create_time = create_time  # type: int
        self.job_id = job_id  # type: str
        self.job_type = job_type  # type: int
        self.push_status = push_status  # type: int
        self.push_url = push_url  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStreamPushJobListResponseBodyDataJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_type is not None:
            result['JobType'] = self.job_type
        if self.push_status is not None:
            result['PushStatus'] = self.push_status
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')
        if m.get('PushStatus') is not None:
            self.push_status = m.get('PushStatus')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryStreamPushJobListResponseBodyData(TeaModel):
    def __init__(self, job_list=None, total=None):
        self.job_list = job_list  # type: list[QueryStreamPushJobListResponseBodyDataJobList]
        self.total = total  # type: int

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryStreamPushJobListResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = QueryStreamPushJobListResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k))
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryStreamPushJobListResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryStreamPushJobListResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryStreamPushJobListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStreamPushJobListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStreamPushJobListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStreamPushJobListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStreamPushJobListResponse, self).to_map()
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
            temp_model = QueryStreamPushJobListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStreamSnapshotJobRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStreamSnapshotJobRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryStreamSnapshotJobResponseBodyDataJobList(TeaModel):
    def __init__(self, snapshot_interval=None, stream_type=None):
        self.snapshot_interval = snapshot_interval  # type: int
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStreamSnapshotJobResponseBodyDataJobList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.snapshot_interval is not None:
            result['SnapshotInterval'] = self.snapshot_interval
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SnapshotInterval') is not None:
            self.snapshot_interval = m.get('SnapshotInterval')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class QueryStreamSnapshotJobResponseBodyData(TeaModel):
    def __init__(self, job_list=None):
        self.job_list = job_list  # type: list[QueryStreamSnapshotJobResponseBodyDataJobList]

    def validate(self):
        if self.job_list:
            for k in self.job_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryStreamSnapshotJobResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['JobList'] = []
        if self.job_list is not None:
            for k in self.job_list:
                result['JobList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.job_list = []
        if m.get('JobList') is not None:
            for k in m.get('JobList'):
                temp_model = QueryStreamSnapshotJobResponseBodyDataJobList()
                self.job_list.append(temp_model.from_map(k))
        return self


class QueryStreamSnapshotJobResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryStreamSnapshotJobResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryStreamSnapshotJobResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryStreamSnapshotJobResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryStreamSnapshotJobResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStreamSnapshotJobResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStreamSnapshotJobResponse, self).to_map()
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
            temp_model = QueryStreamSnapshotJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimeTemplateRequest(TeaModel):
    def __init__(self, current_page=None, page_size=None):
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTimeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryTimeTemplateResponseBodyDataListTimeSectionList(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTimeTemplateResponseBodyDataListTimeSectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryTimeTemplateResponseBodyDataList(TeaModel):
    def __init__(self, all_day=None, default=None, name=None, template_id=None, time_section_list=None):
        self.all_day = all_day  # type: int
        self.default = default  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_section_list = time_section_list  # type: list[QueryTimeTemplateResponseBodyDataListTimeSectionList]

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryTimeTemplateResponseBodyDataListTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryTimeTemplateResponseBodyData(TeaModel):
    def __init__(self, list=None, page=None, page_count=None, page_size=None, total=None):
        self.list = list  # type: list[QueryTimeTemplateResponseBodyDataList]
        self.page = page  # type: int
        self.page_count = page_count  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page is not None:
            result['Page'] = self.page
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryTimeTemplateResponseBodyDataList()
                self.list.append(temp_model.from_map(k))
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryTimeTemplateResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryTimeTemplateResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryTimeTemplateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimeTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTimeTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateResponse, self).to_map()
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
            temp_model = QueryTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTimeTemplateDetailRequest(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTimeTemplateDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class QueryTimeTemplateDetailResponseBodyDataTimeSectionList(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTimeTemplateDetailResponseBodyDataTimeSectionList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class QueryTimeTemplateDetailResponseBodyData(TeaModel):
    def __init__(self, all_day=None, default=None, name=None, template_id=None, time_section_list=None):
        self.all_day = all_day  # type: int
        self.default = default  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_section_list = time_section_list  # type: list[QueryTimeTemplateDetailResponseBodyDataTimeSectionList]

    def validate(self):
        if self.time_section_list:
            for k in self.time_section_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateDetailResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.default is not None:
            result['Default'] = self.default
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k in self.time_section_list:
                result['TimeSectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Default') is not None:
            self.default = m.get('Default')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k in m.get('TimeSectionList'):
                temp_model = QueryTimeTemplateDetailResponseBodyDataTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k))
        return self


class QueryTimeTemplateDetailResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryTimeTemplateDetailResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryTimeTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryTimeTemplateDetailResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTimeTemplateDetailResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTimeTemplateDetailResponse, self).to_map()
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
            temp_model = QueryTimeTemplateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVisionDeviceInfoRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVisionDeviceInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo(TeaModel):
    def __init__(self, device_protocol=None, gb_id=None, net_protocol=None, nick_name=None, password=None,
                 sub_product_key=None):
        self.device_protocol = device_protocol  # type: int
        self.gb_id = gb_id  # type: str
        self.net_protocol = net_protocol  # type: int
        self.nick_name = nick_name  # type: str
        self.password = password  # type: str
        self.sub_product_key = sub_product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_protocol is not None:
            result['DeviceProtocol'] = self.device_protocol
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.net_protocol is not None:
            result['NetProtocol'] = self.net_protocol
        if self.nick_name is not None:
            result['NickName'] = self.nick_name
        if self.password is not None:
            result['Password'] = self.password
        if self.sub_product_key is not None:
            result['SubProductKey'] = self.sub_product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceProtocol') is not None:
            self.device_protocol = m.get('DeviceProtocol')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('NetProtocol') is not None:
            self.net_protocol = m.get('NetProtocol')
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('SubProductKey') is not None:
            self.sub_product_key = m.get('SubProductKey')
        return self


class QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo(TeaModel):
    def __init__(self, pull_auth_key=None, pull_key_expire_time=None, push_auth_key=None,
                 push_key_expire_time=None, push_url_sample=None, stream_name=None, stream_status=None):
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_key_expire_time = pull_key_expire_time  # type: int
        self.push_auth_key = push_auth_key  # type: str
        self.push_key_expire_time = push_key_expire_time  # type: int
        self.push_url_sample = push_url_sample  # type: str
        self.stream_name = stream_name  # type: str
        self.stream_status = stream_status  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        if self.push_url_sample is not None:
            result['PushUrlSample'] = self.push_url_sample
        if self.stream_name is not None:
            result['StreamName'] = self.stream_name
        if self.stream_status is not None:
            result['StreamStatus'] = self.stream_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        if m.get('PushUrlSample') is not None:
            self.push_url_sample = m.get('PushUrlSample')
        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')
        if m.get('StreamStatus') is not None:
            self.stream_status = m.get('StreamStatus')
        return self


class QueryVisionDeviceInfoResponseBodyData(TeaModel):
    def __init__(self, description=None, device_type=None, gb_device_info=None, rtmp_device_info=None):
        self.description = description  # type: str
        self.device_type = device_type  # type: int
        self.gb_device_info = gb_device_info  # type: QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo
        self.rtmp_device_info = rtmp_device_info  # type: QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo

    def validate(self):
        if self.gb_device_info:
            self.gb_device_info.validate()
        if self.rtmp_device_info:
            self.rtmp_device_info.validate()

    def to_map(self):
        _map = super(QueryVisionDeviceInfoResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.gb_device_info is not None:
            result['GbDeviceInfo'] = self.gb_device_info.to_map()
        if self.rtmp_device_info is not None:
            result['RtmpDeviceInfo'] = self.rtmp_device_info.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('GbDeviceInfo') is not None:
            temp_model = QueryVisionDeviceInfoResponseBodyDataGbDeviceInfo()
            self.gb_device_info = temp_model.from_map(m['GbDeviceInfo'])
        if m.get('RtmpDeviceInfo') is not None:
            temp_model = QueryVisionDeviceInfoResponseBodyDataRtmpDeviceInfo()
            self.rtmp_device_info = temp_model.from_map(m['RtmpDeviceInfo'])
        return self


class QueryVisionDeviceInfoResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryVisionDeviceInfoResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryVisionDeviceInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryVisionDeviceInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVisionDeviceInfoResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryVisionDeviceInfoResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVisionDeviceInfoResponse, self).to_map()
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
            temp_model = QueryVisionDeviceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryVoiceIntercomRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, scheme=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.scheme = scheme  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVoiceIntercomRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.scheme is not None:
            result['Scheme'] = self.scheme
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')
        return self


class QueryVoiceIntercomResponseBodyDataCryptoKey(TeaModel):
    def __init__(self, iv=None, key=None):
        self.iv = iv  # type: str
        self.key = key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryVoiceIntercomResponseBodyDataCryptoKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iv is not None:
            result['Iv'] = self.iv
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Iv') is not None:
            self.iv = m.get('Iv')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class QueryVoiceIntercomResponseBodyData(TeaModel):
    def __init__(self, crypto_key=None, url=None):
        self.crypto_key = crypto_key  # type: QueryVoiceIntercomResponseBodyDataCryptoKey
        self.url = url  # type: str

    def validate(self):
        if self.crypto_key:
            self.crypto_key.validate()

    def to_map(self):
        _map = super(QueryVoiceIntercomResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.crypto_key is not None:
            result['CryptoKey'] = self.crypto_key.to_map()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CryptoKey') is not None:
            temp_model = QueryVoiceIntercomResponseBodyDataCryptoKey()
            self.crypto_key = temp_model.from_map(m['CryptoKey'])
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class QueryVoiceIntercomResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: QueryVoiceIntercomResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(QueryVoiceIntercomResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = QueryVoiceIntercomResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryVoiceIntercomResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryVoiceIntercomResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryVoiceIntercomResponse, self).to_map()
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
            temp_model = QueryVoiceIntercomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshGbSubDeviceListRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshGbSubDeviceListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class RefreshGbSubDeviceListResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshGbSubDeviceListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RefreshGbSubDeviceListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshGbSubDeviceListResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshGbSubDeviceListResponse, self).to_map()
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
            temp_model = RefreshGbSubDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceDeviceFromDeviceGroupRequest(TeaModel):
    def __init__(self, device_group_id=None, device_name=None, iot_instance_id=None, isolation_id=None,
                 product_key=None):
        self.device_group_id = device_group_id  # type: str
        self.device_name = device_name  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFaceDeviceFromDeviceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_group_id is not None:
            result['DeviceGroupId'] = self.device_group_id
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceGroupId') is not None:
            self.device_group_id = m.get('DeviceGroupId')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class RemoveFaceDeviceFromDeviceGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFaceDeviceFromDeviceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveFaceDeviceFromDeviceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveFaceDeviceFromDeviceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveFaceDeviceFromDeviceGroupResponse, self).to_map()
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
            temp_model = RemoveFaceDeviceFromDeviceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceUserFromUserGroupRequest(TeaModel):
    def __init__(self, isolation_id=None, user_group_id=None, user_id=None):
        self.isolation_id = isolation_id  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFaceUserFromUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveFaceUserFromUserGroupResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveFaceUserFromUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveFaceUserFromUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveFaceUserFromUserGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveFaceUserFromUserGroupResponse, self).to_map()
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
            temp_model = RemoveFaceUserFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDevicePictureLifeCycleRequest(TeaModel):
    def __init__(self, day=None, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.day = day  # type: int
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDevicePictureLifeCycleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class SetDevicePictureLifeCycleResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDevicePictureLifeCycleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDevicePictureLifeCycleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDevicePictureLifeCycleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDevicePictureLifeCycleResponse, self).to_map()
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
            temp_model = SetDevicePictureLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetDeviceRecordLifeCycleRequest(TeaModel):
    def __init__(self, day=None, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.day = day  # type: int
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeviceRecordLifeCycleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class SetDeviceRecordLifeCycleResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetDeviceRecordLifeCycleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetDeviceRecordLifeCycleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SetDeviceRecordLifeCycleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetDeviceRecordLifeCycleResponse, self).to_map()
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
            temp_model = SetDeviceRecordLifeCycleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveStreamingRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveStreamingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class StopLiveStreamingResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopLiveStreamingResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopLiveStreamingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopLiveStreamingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopLiveStreamingResponse, self).to_map()
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
            temp_model = StopLiveStreamingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopTriggeredRecordRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, record_id=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.record_id = record_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTriggeredRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        return self


class StopTriggeredRecordResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopTriggeredRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StopTriggeredRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopTriggeredRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopTriggeredRecordResponse, self).to_map()
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
            temp_model = StopTriggeredRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TransferDeviceInstanceRequest(TeaModel):
    def __init__(self, device_name_list=None, product_key=None, source_instance_id=None, target_instance_id=None):
        self.device_name_list = device_name_list  # type: list[str]
        self.product_key = product_key  # type: str
        self.source_instance_id = source_instance_id  # type: str
        self.target_instance_id = target_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferDeviceInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name_list is not None:
            result['DeviceNameList'] = self.device_name_list
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceNameList') is not None:
            self.device_name_list = m.get('DeviceNameList')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        return self


class TransferDeviceInstanceResponseBodyDataFailedList(TeaModel):
    def __init__(self, device_name=None, message=None):
        self.device_name = device_name  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferDeviceInstanceResponseBodyDataFailedList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TransferDeviceInstanceResponseBodyDataSuccessList(TeaModel):
    def __init__(self, device_name=None, message=None):
        self.device_name = device_name  # type: str
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TransferDeviceInstanceResponseBodyDataSuccessList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class TransferDeviceInstanceResponseBodyData(TeaModel):
    def __init__(self, failed_list=None, success_list=None):
        self.failed_list = failed_list  # type: list[TransferDeviceInstanceResponseBodyDataFailedList]
        self.success_list = success_list  # type: list[TransferDeviceInstanceResponseBodyDataSuccessList]

    def validate(self):
        if self.failed_list:
            for k in self.failed_list:
                if k:
                    k.validate()
        if self.success_list:
            for k in self.success_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TransferDeviceInstanceResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FailedList'] = []
        if self.failed_list is not None:
            for k in self.failed_list:
                result['FailedList'].append(k.to_map() if k else None)
        result['SuccessList'] = []
        if self.success_list is not None:
            for k in self.success_list:
                result['SuccessList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.failed_list = []
        if m.get('FailedList') is not None:
            for k in m.get('FailedList'):
                temp_model = TransferDeviceInstanceResponseBodyDataFailedList()
                self.failed_list.append(temp_model.from_map(k))
        self.success_list = []
        if m.get('SuccessList') is not None:
            for k in m.get('SuccessList'):
                temp_model = TransferDeviceInstanceResponseBodyDataSuccessList()
                self.success_list.append(temp_model.from_map(k))
        return self


class TransferDeviceInstanceResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: TransferDeviceInstanceResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(TransferDeviceInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = TransferDeviceInstanceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TransferDeviceInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TransferDeviceInstanceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TransferDeviceInstanceResponse, self).to_map()
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
            temp_model = TransferDeviceInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerCapturePictureRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerCapturePictureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class TriggerCapturePictureResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerCapturePictureResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerCapturePictureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerCapturePictureResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerCapturePictureResponse, self).to_map()
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
            temp_model = TriggerCapturePictureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TriggerRecordRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, pre_record_duration=None,
                 product_key=None, record_duration=None, stream_type=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.product_key = product_key  # type: str
        self.record_duration = record_duration  # type: int
        self.stream_type = stream_type  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerRecordRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.stream_type is not None:
            result['StreamType'] = self.stream_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('StreamType') is not None:
            self.stream_type = m.get('StreamType')
        return self


class TriggerRecordResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TriggerRecordResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TriggerRecordResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TriggerRecordResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TriggerRecordResponse, self).to_map()
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
            temp_model = TriggerRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindPictureSearchAppWithDevicesRequest(TeaModel):
    def __init__(self, app_instance_id=None, device_iot_ids=None, iot_instance_id=None):
        self.app_instance_id = app_instance_id  # type: str
        self.device_iot_ids = device_iot_ids  # type: list[str]
        self.iot_instance_id = iot_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindPictureSearchAppWithDevicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.device_iot_ids is not None:
            result['DeviceIotIds'] = self.device_iot_ids
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('DeviceIotIds') is not None:
            self.device_iot_ids = m.get('DeviceIotIds')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        return self


class UnbindPictureSearchAppWithDevicesResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindPictureSearchAppWithDevicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnbindPictureSearchAppWithDevicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindPictureSearchAppWithDevicesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindPictureSearchAppWithDevicesResponse, self).to_map()
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
            temp_model = UnbindPictureSearchAppWithDevicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventRecordPlanRequest(TeaModel):
    def __init__(self, event_types=None, name=None, plan_id=None, pre_record_duration=None, record_duration=None,
                 template_id=None):
        self.event_types = event_types  # type: str
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.pre_record_duration = pre_record_duration  # type: int
        self.record_duration = record_duration  # type: int
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventRecordPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_types is not None:
            result['EventTypes'] = self.event_types
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.pre_record_duration is not None:
            result['PreRecordDuration'] = self.pre_record_duration
        if self.record_duration is not None:
            result['RecordDuration'] = self.record_duration
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EventTypes') is not None:
            self.event_types = m.get('EventTypes')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('PreRecordDuration') is not None:
            self.pre_record_duration = m.get('PreRecordDuration')
        if m.get('RecordDuration') is not None:
            self.record_duration = m.get('RecordDuration')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateEventRecordPlanResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEventRecordPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateEventRecordPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEventRecordPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEventRecordPlanResponse, self).to_map()
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
            temp_model = UpdateEventRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceUserRequest(TeaModel):
    def __init__(self, custom_user_id=None, face_pic_url=None, isolation_id=None, name=None, params=None,
                 user_id=None):
        self.custom_user_id = custom_user_id  # type: str
        self.face_pic_url = face_pic_url  # type: str
        self.isolation_id = isolation_id  # type: str
        self.name = name  # type: str
        self.params = params  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_user_id is not None:
            result['CustomUserId'] = self.custom_user_id
        if self.face_pic_url is not None:
            result['FacePicUrl'] = self.face_pic_url
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.name is not None:
            result['Name'] = self.name
        if self.params is not None:
            result['Params'] = self.params
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomUserId') is not None:
            self.custom_user_id = m.get('CustomUserId')
        if m.get('FacePicUrl') is not None:
            self.face_pic_url = m.get('FacePicUrl')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Params') is not None:
            self.params = m.get('Params')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UpdateFaceUserResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFaceUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFaceUserResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFaceUserResponse, self).to_map()
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
            temp_model = UpdateFaceUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationRequest(TeaModel):
    def __init__(self, control_id=None, isolation_id=None, relation=None):
        self.control_id = control_id  # type: str
        self.isolation_id = isolation_id  # type: str
        self.relation = relation  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceUserGroupAndDeviceGroupRelationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.isolation_id is not None:
            result['IsolationId'] = self.isolation_id
        if self.relation is not None:
            result['Relation'] = self.relation
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('IsolationId') is not None:
            self.isolation_id = m.get('IsolationId')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData(TeaModel):
    def __init__(self, control_id=None, modified_time=None):
        self.control_id = control_id  # type: str
        self.modified_time = modified_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_id is not None:
            result['ControlId'] = self.control_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ControlId') is not None:
            self.control_id = m.get('ControlId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(UpdateFaceUserGroupAndDeviceGroupRelationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
            temp_model = UpdateFaceUserGroupAndDeviceGroupRelationResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateFaceUserGroupAndDeviceGroupRelationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateFaceUserGroupAndDeviceGroupRelationResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateFaceUserGroupAndDeviceGroupRelationResponse, self).to_map()
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
            temp_model = UpdateFaceUserGroupAndDeviceGroupRelationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGbDeviceRequest(TeaModel):
    def __init__(self, description=None, device_name=None, gb_id=None, iot_id=None, iot_instance_id=None,
                 password=None, product_key=None):
        self.description = description  # type: str
        self.device_name = device_name  # type: str
        self.gb_id = gb_id  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.password = password  # type: str
        self.product_key = product_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGbDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.gb_id is not None:
            result['GbId'] = self.gb_id
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.password is not None:
            result['Password'] = self.password
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('GbId') is not None:
            self.gb_id = m.get('GbId')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class UpdateGbDeviceResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateGbDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGbDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateGbDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateGbDeviceResponse, self).to_map()
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
            temp_model = UpdateGbDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceInternetProtocolRequest(TeaModel):
    def __init__(self, iot_instance_id=None, ip_version=None):
        self.iot_instance_id = iot_instance_id  # type: str
        self.ip_version = ip_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceInternetProtocolRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')
        return self


class UpdateInstanceInternetProtocolResponseBody(TeaModel):
    def __init__(self, code=None, data=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.data = data  # type: dict[str, any]
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceInternetProtocolResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
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
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateInstanceInternetProtocolResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceInternetProtocolResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceInternetProtocolResponse, self).to_map()
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
            temp_model = UpdateInstanceInternetProtocolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePictureSearchAppRequest(TeaModel):
    def __init__(self, app_instance_id=None, description=None, name=None):
        self.app_instance_id = app_instance_id  # type: str
        self.description = description  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePictureSearchAppRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdatePictureSearchAppResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdatePictureSearchAppResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdatePictureSearchAppResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdatePictureSearchAppResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdatePictureSearchAppResponse, self).to_map()
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
            temp_model = UpdatePictureSearchAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRecordPlanRequest(TeaModel):
    def __init__(self, name=None, plan_id=None, template_id=None):
        self.name = name  # type: str
        self.plan_id = plan_id  # type: str
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordPlanRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.plan_id is not None:
            result['PlanId'] = self.plan_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class UpdateRecordPlanResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRecordPlanResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRecordPlanResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRecordPlanResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRecordPlanResponse, self).to_map()
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
            temp_model = UpdateRecordPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRtmpKeyRequest(TeaModel):
    def __init__(self, device_name=None, iot_id=None, iot_instance_id=None, product_key=None, pull_auth_key=None,
                 pull_key_expire_time=None, push_auth_key=None, push_key_expire_time=None):
        self.device_name = device_name  # type: str
        self.iot_id = iot_id  # type: str
        self.iot_instance_id = iot_instance_id  # type: str
        self.product_key = product_key  # type: str
        self.pull_auth_key = pull_auth_key  # type: str
        self.pull_key_expire_time = pull_key_expire_time  # type: int
        self.push_auth_key = push_auth_key  # type: str
        self.push_key_expire_time = push_key_expire_time  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRtmpKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.iot_id is not None:
            result['IotId'] = self.iot_id
        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        if self.pull_auth_key is not None:
            result['PullAuthKey'] = self.pull_auth_key
        if self.pull_key_expire_time is not None:
            result['PullKeyExpireTime'] = self.pull_key_expire_time
        if self.push_auth_key is not None:
            result['PushAuthKey'] = self.push_auth_key
        if self.push_key_expire_time is not None:
            result['PushKeyExpireTime'] = self.push_key_expire_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')
        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        if m.get('PullAuthKey') is not None:
            self.pull_auth_key = m.get('PullAuthKey')
        if m.get('PullKeyExpireTime') is not None:
            self.pull_key_expire_time = m.get('PullKeyExpireTime')
        if m.get('PushAuthKey') is not None:
            self.push_auth_key = m.get('PushAuthKey')
        if m.get('PushKeyExpireTime') is not None:
            self.push_key_expire_time = m.get('PushKeyExpireTime')
        return self


class UpdateRtmpKeyResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateRtmpKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateRtmpKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateRtmpKeyResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateRtmpKeyResponse, self).to_map()
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
            temp_model = UpdateRtmpKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTimeTemplateRequestTimeSections(TeaModel):
    def __init__(self, begin=None, day_of_week=None, end=None):
        self.begin = begin  # type: int
        self.day_of_week = day_of_week  # type: int
        self.end = end  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTimeTemplateRequestTimeSections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['Begin'] = self.begin
        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week
        if self.end is not None:
            result['End'] = self.end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')
        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')
        if m.get('End') is not None:
            self.end = m.get('End')
        return self


class UpdateTimeTemplateRequest(TeaModel):
    def __init__(self, all_day=None, name=None, template_id=None, time_sections=None):
        self.all_day = all_day  # type: int
        self.name = name  # type: str
        self.template_id = template_id  # type: str
        self.time_sections = time_sections  # type: list[UpdateTimeTemplateRequestTimeSections]

    def validate(self):
        if self.time_sections:
            for k in self.time_sections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateTimeTemplateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all_day is not None:
            result['AllDay'] = self.all_day
        if self.name is not None:
            result['Name'] = self.name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        result['TimeSections'] = []
        if self.time_sections is not None:
            for k in self.time_sections:
                result['TimeSections'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        self.time_sections = []
        if m.get('TimeSections') is not None:
            for k in m.get('TimeSections'):
                temp_model = UpdateTimeTemplateRequestTimeSections()
                self.time_sections.append(temp_model.from_map(k))
        return self


class UpdateTimeTemplateResponseBody(TeaModel):
    def __init__(self, code=None, error_message=None, request_id=None, success=None):
        self.code = code  # type: str
        self.error_message = error_message  # type: str
        self.request_id = request_id  # type: str
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateTimeTemplateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateTimeTemplateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateTimeTemplateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateTimeTemplateResponse, self).to_map()
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
            temp_model = UpdateTimeTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


