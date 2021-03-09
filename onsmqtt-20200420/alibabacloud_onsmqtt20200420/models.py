# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from Tea.converter import TeaConverter


class ApplyTokenRequest(TeaModel):
    def __init__(self, resources=None, instance_id=None, expire_time=None, actions=None):
        self.resources = TeaConverter.to_unicode(resources)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.expire_time = expire_time  # type: long
        self.actions = TeaConverter.to_unicode(actions)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, token=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.token = TeaConverter.to_unicode(token)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ApplyTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ApplyTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.client_id_list = client_id_list  # type: list[unicode]

    def validate(self):
        pass

    def to_map(self):
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
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.online_status_list = online_status_list  # type: list[BatchQuerySessionByClientIdsResponseBodyOnlineStatusList]

    def validate(self):
        if self.online_status_list:
            for k in self.online_status_list:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: BatchQuerySessionByClientIdsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.group_id = TeaConverter.to_unicode(group_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: CreateGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.group_id = TeaConverter.to_unicode(group_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: DeleteGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.device_access_key_id = TeaConverter.to_unicode(device_access_key_id)  # type: unicode
        self.create_time = create_time  # type: long
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.device_access_key_secret = TeaConverter.to_unicode(device_access_key_secret)  # type: unicode
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.device_credential = device_credential  # type: GetDeviceCredentialResponseBodyDeviceCredential

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: GetDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, update_time=None, independent_naming=None, group_id=None, create_time=None, instance_id=None):
        self.update_time = update_time  # type: long
        self.independent_naming = independent_naming  # type: bool
        self.group_id = TeaConverter.to_unicode(group_id)  # type: unicode
        self.create_time = create_time  # type: long
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class ListGroupIdResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.data = data  # type: list[ListGroupIdResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: ListGroupIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


class QuerySessionByClientIdRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, online_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.online_status = online_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        return self


class QuerySessionByClientIdResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: QuerySessionByClientIdResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.token = TeaConverter.to_unicode(token)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, token_status=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.token_status = token_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token_status is not None:
            result['TokenStatus'] = self.token_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TokenStatus') is not None:
            self.token_status = m.get('TokenStatus')
        return self


class QueryTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: QueryTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.device_access_key_id = TeaConverter.to_unicode(device_access_key_id)  # type: unicode
        self.create_time = create_time  # type: long
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.device_access_key_secret = TeaConverter.to_unicode(device_access_key_secret)  # type: unicode
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.device_credential = device_credential  # type: RefreshDeviceCredentialResponseBodyDeviceCredential

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RefreshDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.device_access_key_id = TeaConverter.to_unicode(device_access_key_id)  # type: unicode
        self.create_time = create_time  # type: long
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.device_access_key_secret = TeaConverter.to_unicode(device_access_key_secret)  # type: unicode
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.device_credential = device_credential  # type: RegisterDeviceCredentialResponseBodyDeviceCredential

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RegisterDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.token = TeaConverter.to_unicode(token)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: RevokeTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.mqtt_topic = TeaConverter.to_unicode(mqtt_topic)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode
        self.payload = TeaConverter.to_unicode(payload)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
    def __init__(self, request_id=None, msg_id=None):
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode
        self.msg_id = TeaConverter.to_unicode(msg_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendMessageResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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
        self.client_id = TeaConverter.to_unicode(client_id)  # type: unicode
        self.instance_id = TeaConverter.to_unicode(instance_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.request_id = TeaConverter.to_unicode(request_id)  # type: unicode

    def validate(self):
        pass

    def to_map(self):
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
        self.headers = headers  # type: dict[unicode, unicode]
        self.body = body  # type: UnRegisterDeviceCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
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


