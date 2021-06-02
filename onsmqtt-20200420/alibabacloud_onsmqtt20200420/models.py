# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ApplyTokenRequest(TeaModel):
    def __init__(self, resources=None, instance_id=None, expire_time=None, actions=None):
        self.resources = resources  # type: str
        self.instance_id = instance_id  # type: str
        self.expire_time = expire_time  # type: long
        self.actions = actions  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resources is not None:
            result['Resources'] = self.resources
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.actions is not None:
            result['Actions'] = self.actions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')
        return self


class ApplyTokenResponseBody(TeaModel):
    def __init__(self, token=None, request_id=None):
        self.token = token  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ApplyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyTokenResponse, self).to_map()
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
            temp_model = ApplyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQuerySessionByClientIdsRequest(TeaModel):
    def __init__(self, instance_id=None, client_id_list=None):
        self.instance_id = instance_id  # type: str
        self.client_id_list = client_id_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')
        return self


class BatchQuerySessionByClientIdsResponseBodyOnlineStatusList(TeaModel):
    def __init__(self, online_status=None, client_id=None):
        self.online_status = online_status  # type: bool
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsResponseBodyOnlineStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class BatchQuerySessionByClientIdsResponseBody(TeaModel):
    def __init__(self, request_id=None, online_status_list=None):
        self.request_id = request_id  # type: str
        self.online_status_list = online_status_list  # type: list[BatchQuerySessionByClientIdsResponseBodyOnlineStatusList]

    def validate(self):
        if self.online_status_list:
            for k in self.online_status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['OnlineStatusList'] = []
        if self.online_status_list is not None:
            for k in self.online_status_list:
                result['OnlineStatusList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.online_status_list = []
        if m.get('OnlineStatusList') is not None:
            for k in m.get('OnlineStatusList'):
                temp_model = BatchQuerySessionByClientIdsResponseBodyOnlineStatusList()
                self.online_status_list.append(temp_model.from_map(k))
        return self


class BatchQuerySessionByClientIdsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: BatchQuerySessionByClientIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsResponse, self).to_map()
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
            temp_model = BatchQuerySessionByClientIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupIdRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None):
        self.group_id = group_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class CreateGroupIdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateGroupIdResponseBody, self).to_map()
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


class CreateGroupIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupIdResponse, self).to_map()
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
            temp_model = CreateGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupIdRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None):
        self.group_id = group_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteGroupIdResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteGroupIdResponseBody, self).to_map()
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


class DeleteGroupIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupIdResponse, self).to_map()
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
            temp_model = DeleteGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        self.client_id = client_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetDeviceCredentialResponseBodyDeviceCredential(TeaModel):
    def __init__(self, update_time=None, device_access_key_id=None, create_time=None, instance_id=None,
                 device_access_key_secret=None, client_id=None):
        self.update_time = update_time  # type: long
        self.device_access_key_id = device_access_key_id  # type: str
        self.create_time = create_time  # type: long
        self.instance_id = instance_id  # type: str
        self.device_access_key_secret = device_access_key_secret  # type: str
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceCredentialResponseBodyDeviceCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class GetDeviceCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None, device_credential=None):
        self.request_id = request_id  # type: str
        self.device_credential = device_credential  # type: GetDeviceCredentialResponseBodyDeviceCredential

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super(GetDeviceCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceCredential') is not None:
            temp_model = GetDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        return self


class GetDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceCredentialResponse, self).to_map()
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
            temp_model = GetDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupIdRequest(TeaModel):
    def __init__(self, instance_id=None):
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupIdRequest, self).to_map()
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


class ListGroupIdResponseBodyData(TeaModel):
    def __init__(self, update_time=None, instance_id=None, independent_naming=None, group_id=None, create_time=None):
        self.update_time = update_time  # type: long
        self.instance_id = instance_id  # type: str
        self.independent_naming = independent_naming  # type: bool
        self.group_id = group_id  # type: str
        self.create_time = create_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListGroupIdResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[ListGroupIdResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListGroupIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGroupIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListGroupIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupIdResponse, self).to_map()
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
            temp_model = ListGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceDeviceRequest(TeaModel):
    def __init__(self, mqtt_region_id=None, instance_id=None, reverse=None, client_id=None, begin_time=None,
                 end_time=None, current_page=None, page_size=None):
        self.mqtt_region_id = mqtt_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.reverse = reverse  # type: bool
        self.client_id = client_id  # type: str
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryMqttTraceDeviceResponseBodyDeviceInfoList(TeaModel):
    def __init__(self, channel_id=None, time=None, action_code=None, action=None, action_info=None):
        self.channel_id = channel_id  # type: str
        self.time = time  # type: str
        self.action_code = action_code  # type: str
        self.action = action  # type: str
        self.action_info = action_info  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceDeviceResponseBodyDeviceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.time is not None:
            result['Time'] = self.time
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action is not None:
            result['Action'] = self.action
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        return self


class QueryMqttTraceDeviceResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total=None, device_info_list=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total = total  # type: long
        self.device_info_list = device_info_list  # type: list[QueryMqttTraceDeviceResponseBodyDeviceInfoList]

    def validate(self):
        if self.device_info_list:
            for k in self.device_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMqttTraceDeviceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k in self.device_info_list:
                result['DeviceInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k in m.get('DeviceInfoList'):
                temp_model = QueryMqttTraceDeviceResponseBodyDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k))
        return self


class QueryMqttTraceDeviceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMqttTraceDeviceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceDeviceResponse, self).to_map()
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
            temp_model = QueryMqttTraceDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessageOfClientRequest(TeaModel):
    def __init__(self, mqtt_region_id=None, instance_id=None, client_id=None, begin_time=None, end_time=None,
                 current_page=None, page_size=None, reverse=None):
        self.mqtt_region_id = mqtt_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.client_id = client_id  # type: str
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.reverse = reverse  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList(TeaModel):
    def __init__(self, time=None, action=None, action_code=None, action_info=None, msg_id=None, client_id=None):
        self.time = time  # type: str
        self.action = action  # type: str
        self.action_code = action_code  # type: str
        self.action_info = action_info  # type: str
        self.msg_id = msg_id  # type: str
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class QueryMqttTraceMessageOfClientResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total=None, message_of_client_list=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total = total  # type: long
        self.message_of_client_list = message_of_client_list  # type: list[QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList]

    def validate(self):
        if self.message_of_client_list:
            for k in self.message_of_client_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['MessageOfClientList'] = []
        if self.message_of_client_list is not None:
            for k in self.message_of_client_list:
                result['MessageOfClientList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.message_of_client_list = []
        if m.get('MessageOfClientList') is not None:
            for k in m.get('MessageOfClientList'):
                temp_model = QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList()
                self.message_of_client_list.append(temp_model.from_map(k))
        return self


class QueryMqttTraceMessageOfClientResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMqttTraceMessageOfClientResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientResponse, self).to_map()
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
            temp_model = QueryMqttTraceMessageOfClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessagePublishRequest(TeaModel):
    def __init__(self, mqtt_region_id=None, instance_id=None, msg_id=None, begin_time=None, end_time=None):
        self.mqtt_region_id = mqtt_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.msg_id = msg_id  # type: str
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        return self


class QueryMqttTraceMessagePublishResponseBodyMessageTraceLists(TeaModel):
    def __init__(self, time=None, action=None, action_code=None, action_info=None, msg_id=None, client_id=None):
        self.time = time  # type: str
        self.action = action  # type: str
        self.action_code = action_code  # type: str
        self.action_info = action_info  # type: str
        self.msg_id = msg_id  # type: str
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishResponseBodyMessageTraceLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class QueryMqttTraceMessagePublishResponseBody(TeaModel):
    def __init__(self, request_id=None, message_trace_lists=None):
        self.request_id = request_id  # type: str
        self.message_trace_lists = message_trace_lists  # type: list[QueryMqttTraceMessagePublishResponseBodyMessageTraceLists]

    def validate(self):
        if self.message_trace_lists:
            for k in self.message_trace_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k in self.message_trace_lists:
                result['MessageTraceLists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k in m.get('MessageTraceLists'):
                temp_model = QueryMqttTraceMessagePublishResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k))
        return self


class QueryMqttTraceMessagePublishResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMqttTraceMessagePublishResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishResponse, self).to_map()
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
            temp_model = QueryMqttTraceMessagePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessageSubscribeRequest(TeaModel):
    def __init__(self, mqtt_region_id=None, instance_id=None, reverse=None, client_id=None, begin_time=None,
                 end_time=None, current_page=None, page_size=None, msg_id=None):
        self.mqtt_region_id = mqtt_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.reverse = reverse  # type: bool
        self.client_id = client_id  # type: str
        self.begin_time = begin_time  # type: long
        self.end_time = end_time  # type: long
        self.current_page = current_page  # type: int
        self.page_size = page_size  # type: int
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists(TeaModel):
    def __init__(self, time=None, action=None, action_code=None, action_info=None, msg_id=None, client_id=None):
        self.time = time  # type: str
        self.action = action  # type: str
        self.action_code = action_code  # type: str
        self.action_info = action_info  # type: str
        self.msg_id = msg_id  # type: str
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['Time'] = self.time
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Time') is not None:
            self.time = m.get('Time')
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class QueryMqttTraceMessageSubscribeResponseBody(TeaModel):
    def __init__(self, current_page=None, request_id=None, page_size=None, total=None, message_trace_lists=None):
        self.current_page = current_page  # type: int
        self.request_id = request_id  # type: str
        self.page_size = page_size  # type: int
        self.total = total  # type: long
        self.message_trace_lists = message_trace_lists  # type: list[QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists]

    def validate(self):
        if self.message_trace_lists:
            for k in self.message_trace_lists:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k in self.message_trace_lists:
                result['MessageTraceLists'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k in m.get('MessageTraceLists'):
                temp_model = QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k))
        return self


class QueryMqttTraceMessageSubscribeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryMqttTraceMessageSubscribeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeResponse, self).to_map()
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
            temp_model = QueryMqttTraceMessageSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySessionByClientIdRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        self.client_id = client_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySessionByClientIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QuerySessionByClientIdResponseBody(TeaModel):
    def __init__(self, online_status=None, request_id=None):
        self.online_status = online_status  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySessionByClientIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySessionByClientIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QuerySessionByClientIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySessionByClientIdResponse, self).to_map()
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
            temp_model = QuerySessionByClientIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTokenRequest(TeaModel):
    def __init__(self, token=None, instance_id=None):
        self.token = token  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class QueryTokenResponseBody(TeaModel):
    def __init__(self, token_status=None, request_id=None):
        self.token_status = token_status  # type: bool
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token_status is not None:
            result['TokenStatus'] = self.token_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TokenStatus') is not None:
            self.token_status = m.get('TokenStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: QueryTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTokenResponse, self).to_map()
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
            temp_model = QueryTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        self.client_id = client_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDeviceCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RefreshDeviceCredentialResponseBodyDeviceCredential(TeaModel):
    def __init__(self, update_time=None, device_access_key_id=None, create_time=None, instance_id=None,
                 device_access_key_secret=None, client_id=None):
        self.update_time = update_time  # type: long
        self.device_access_key_id = device_access_key_id  # type: str
        self.create_time = create_time  # type: long
        self.instance_id = instance_id  # type: str
        self.device_access_key_secret = device_access_key_secret  # type: str
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDeviceCredentialResponseBodyDeviceCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class RefreshDeviceCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None, device_credential=None):
        self.request_id = request_id  # type: str
        self.device_credential = device_credential  # type: RefreshDeviceCredentialResponseBodyDeviceCredential

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super(RefreshDeviceCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceCredential') is not None:
            temp_model = RefreshDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        return self


class RefreshDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RefreshDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshDeviceCredentialResponse, self).to_map()
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
            temp_model = RefreshDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        self.client_id = client_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDeviceCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RegisterDeviceCredentialResponseBodyDeviceCredential(TeaModel):
    def __init__(self, update_time=None, device_access_key_id=None, create_time=None, instance_id=None,
                 device_access_key_secret=None, client_id=None):
        self.update_time = update_time  # type: long
        self.device_access_key_id = device_access_key_id  # type: str
        self.create_time = create_time  # type: long
        self.instance_id = instance_id  # type: str
        self.device_access_key_secret = device_access_key_secret  # type: str
        self.client_id = client_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDeviceCredentialResponseBodyDeviceCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class RegisterDeviceCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None, device_credential=None):
        self.request_id = request_id  # type: str
        self.device_credential = device_credential  # type: RegisterDeviceCredentialResponseBodyDeviceCredential

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super(RegisterDeviceCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DeviceCredential') is not None:
            temp_model = RegisterDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        return self


class RegisterDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RegisterDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterDeviceCredentialResponse, self).to_map()
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
            temp_model = RegisterDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeTokenRequest(TeaModel):
    def __init__(self, token=None, instance_id=None):
        self.token = token  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class RevokeTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeTokenResponseBody, self).to_map()
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


class RevokeTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RevokeTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeTokenResponse, self).to_map()
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
            temp_model = RevokeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, mqtt_topic=None, instance_id=None, payload=None):
        self.mqtt_topic = mqtt_topic  # type: str
        self.instance_id = instance_id  # type: str
        self.payload = payload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_topic is not None:
            result['MqttTopic'] = self.mqtt_topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.payload is not None:
            result['Payload'] = self.payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttTopic') is not None:
            self.mqtt_topic = m.get('MqttTopic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, msg_id=None, request_id=None):
        self.msg_id = msg_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnRegisterDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        self.client_id = client_id  # type: str
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnRegisterDeviceCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class UnRegisterDeviceCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnRegisterDeviceCredentialResponseBody, self).to_map()
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


class UnRegisterDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnRegisterDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnRegisterDeviceCredentialResponse, self).to_map()
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
            temp_model = UnRegisterDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


