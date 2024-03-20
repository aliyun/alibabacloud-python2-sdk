# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class ActiveCaCertificateRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None, sn=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActiveCaCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class ActiveCaCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, sn=None):
        self.request_id = request_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActiveCaCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class ActiveCaCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ActiveCaCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActiveCaCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActiveCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ActiveDeviceCertificateRequest(TeaModel):
    def __init__(self, ca_sn=None, device_sn=None, mqtt_instance_id=None):
        self.ca_sn = ca_sn  # type: str
        self.device_sn = device_sn  # type: str
        self.mqtt_instance_id = mqtt_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActiveDeviceCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class ActiveDeviceCertificateResponseBody(TeaModel):
    def __init__(self, device_sn=None, request_id=None):
        self.device_sn = device_sn  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ActiveDeviceCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ActiveDeviceCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ActiveDeviceCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ActiveDeviceCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ActiveDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyTokenRequest(TeaModel):
    def __init__(self, actions=None, expire_time=None, instance_id=None, resources=None):
        # The permission type of the token. Valid values:
        # 
        # *   **R**: read-only. You can only subscribe to the specified topics.
        # *   **W**: write-only. You can only send messages to the specified topics.
        # *   **R,W**: read and write. You can send messages to and subscribe to the specified topics. Separate **R** and **W** with a comma (,).
        self.actions = actions  # type: str
        # The timestamp that indicates the point in time when the token expires. Unit: milliseconds. The minimum validity period of a token is 60 seconds, and the maximum validity period of a token is 30 days. If you specify a validity period of more than 30 days for a token, no errors are returned. However, the token is valid only for 30 days.
        # 
        # For example, you want to specify a validity period of 60 seconds for a token. If the current system timestamp is 1609434061000, you must set this parameter to **1609434121000**. The value is calculated by using the following formula: 1609434061000 + 60 x 1000 = 1609434121000.
        self.expire_time = expire_time  # type: long
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com/).
        self.instance_id = instance_id  # type: str
        # The topics on the ApsaraMQ for MQTT instance. Separate multiple topics with commas (,). Each token can be used to access up to 100 topics. Multiple topics are sorted in alphabetic order. MQTT wildcards, including single-level wildcards represented by plus signs (+) and multi-level wildcards represented by number signs (#), can be used for the Resources parameter that you register to apply for a token.
        # 
        # For example, if you set the **Resources** parameter to Topic1/+ when you apply for a token, the ApsaraMQ for MQTT client can manage the topics in Topic1/xxx. If you set the **Resources** parameter to Topic1/# when you apply for a token, the ApsaraMQ for MQTT client can manage topics of any level in Topic1/xxx/xxx/xxx.
        # 
        # >  ApsaraMQ for MQTT supports subtopics. You can specify subtopics in the code for messaging instead of configuring them in the ApsaraMQ for MQTT console. Forward slashes (/) are used to separate topics of different levels. For more information, see [Terms](~~42420~~).
        self.resources = resources  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['Actions'] = self.actions
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resources is not None:
            result['Resources'] = self.resources
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Actions') is not None:
            self.actions = m.get('Actions')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Resources') is not None:
            self.resources = m.get('Resources')
        return self


class ApplyTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id  # type: str
        # The token that is returned by the ApsaraMQ for MQTT broker.
        # 
        # >  Do not assume the length, format, or rule of the token to return. The actual returned token shall prevail.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchQuerySessionByClientIdsRequest(TeaModel):
    def __init__(self, client_id_list=None, instance_id=None):
        # The ApsaraMQ for MQTT clients.
        self.client_id_list = client_id_list  # type: list[str]
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class BatchQuerySessionByClientIdsResponseBodyOnlineStatusList(TeaModel):
    def __init__(self, client_id=None, online_status=None):
        # The ID of the ApsaraMQ for MQTT client. For more information about client IDs, see [Terms](~~42420~~).
        self.client_id = client_id  # type: str
        # Indicates whether the ApsaraMQ for MQTT client is online. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.online_status = online_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsResponseBodyOnlineStatusList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')
        return self


class BatchQuerySessionByClientIdsResponseBody(TeaModel):
    def __init__(self, online_status_list=None, request_id=None):
        # The status list of all queried ApsaraMQ for MQTT clients.
        self.online_status_list = online_status_list  # type: list[BatchQuerySessionByClientIdsResponseBodyOnlineStatusList]
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id  # type: str

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
        result['OnlineStatusList'] = []
        if self.online_status_list is not None:
            for k in self.online_status_list:
                result['OnlineStatusList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.online_status_list = []
        if m.get('OnlineStatusList') is not None:
            for k in m.get('OnlineStatusList'):
                temp_model = BatchQuerySessionByClientIdsResponseBodyOnlineStatusList()
                self.online_status_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchQuerySessionByClientIdsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BatchQuerySessionByClientIdsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BatchQuerySessionByClientIdsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BatchQuerySessionByClientIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupIdRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None):
        # The ID of the group that you want to create. The group ID must meet the following conventions:
        # 
        # *   The ID must be 7 to 64 characters in length. It must start with GID\_ or GID- and can contain only letters, digits, hyphens (-), and underscores (\_).
        # *   The ID cannot be changed after the group is created. For more information, see [Terms](~~42420~~).
        self.group_id = group_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance to which the group belongs.
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
        # The request ID. This parameter is a common parameter.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateGroupIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateGroupIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCaCertificateRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None, sn=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCaCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class DeleteCaCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, sn=None):
        self.request_id = request_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteCaCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class DeleteCaCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteCaCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteCaCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeviceCertificateRequest(TeaModel):
    def __init__(self, ca_sn=None, device_sn=None, mqtt_instance_id=None):
        self.ca_sn = ca_sn  # type: str
        self.device_sn = device_sn  # type: str
        self.mqtt_instance_id = mqtt_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeviceCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class DeleteDeviceCertificateResponseBody(TeaModel):
    def __init__(self, device_sn=None, request_id=None):
        self.device_sn = device_sn  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDeviceCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeviceCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDeviceCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDeviceCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupIdRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None):
        # The ID of the group that you want to delete.
        self.group_id = group_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance from which you want to delete a group.
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
        # The request ID. This parameter is a common parameter.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteGroupIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteGroupIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCaCertificateRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None, sn=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCaCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class GetCaCertificateResponseBodyData(TeaModel):
    def __init__(self, ca_content=None, ca_name=None, registration_code=None, sn=None, status=None, valid_begin=None,
                 valid_end=None, verification_content=None):
        self.ca_content = ca_content  # type: str
        self.ca_name = ca_name  # type: str
        self.registration_code = registration_code  # type: str
        self.sn = sn  # type: str
        self.status = status  # type: str
        self.valid_begin = valid_begin  # type: str
        self.valid_end = valid_end  # type: str
        self.verification_content = verification_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCaCertificateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content
        if self.ca_name is not None:
            result['CaName'] = self.ca_name
        if self.registration_code is not None:
            result['RegistrationCode'] = self.registration_code
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')
        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')
        if m.get('RegistrationCode') is not None:
            self.registration_code = m.get('RegistrationCode')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')
        return self


class GetCaCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetCaCertificateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetCaCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetCaCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetCaCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetCaCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCaCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceCertificateRequest(TeaModel):
    def __init__(self, ca_sn=None, device_sn=None, mqtt_instance_id=None):
        self.ca_sn = ca_sn  # type: str
        self.device_sn = device_sn  # type: str
        self.mqtt_instance_id = mqtt_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class GetDeviceCertificateResponseBodyData(TeaModel):
    def __init__(self, ca_sn=None, device_content=None, device_name=None, device_sn=None, status=None,
                 valid_begin=None, valid_end=None):
        self.ca_sn = ca_sn  # type: str
        self.device_content = device_content  # type: str
        self.device_name = device_name  # type: str
        self.device_sn = device_sn  # type: str
        self.status = status  # type: str
        self.valid_begin = valid_begin  # type: str
        self.valid_end = valid_end  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceCertificateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_content is not None:
            result['DeviceContent'] = self.device_content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        return self


class GetDeviceCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: GetDeviceCertificateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(GetDeviceCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = GetDeviceCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        # The client ID of the device whose access credential you want to query.
        self.client_id = client_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
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
    def __init__(self, client_id=None, create_time=None, device_access_key_id=None, device_access_key_secret=None,
                 instance_id=None, update_time=None):
        # The client ID of the device.
        self.client_id = client_id  # type: str
        # The timestamp that indicates when the access credential of the device was created. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id  # type: str
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret  # type: str
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id  # type: str
        # The timestamp that indicates when the access credential of the device was last updated. The value of this parameter is a UNIX timestamp in milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDeviceCredentialResponseBodyDeviceCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetDeviceCredentialResponseBody(TeaModel):
    def __init__(self, device_credential=None, request_id=None):
        # The information about the access credential of the device.
        self.device_credential = device_credential  # type: GetDeviceCredentialResponseBodyDeviceCredential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super(GetDeviceCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = GetDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetDeviceCredentialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDeviceCredentialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisterCodeRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisterCodeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class GetRegisterCodeResponseBody(TeaModel):
    def __init__(self, register_code=None, request_id=None):
        self.register_code = register_code  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisterCodeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.register_code is not None:
            result['RegisterCode'] = self.register_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegisterCode') is not None:
            self.register_code = m.get('RegisterCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisterCodeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRegisterCodeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegisterCodeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegisterCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InactivateCaCertificateRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None, sn=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InactivateCaCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class InactivateCaCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, sn=None):
        self.request_id = request_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InactivateCaCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class InactivateCaCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InactivateCaCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InactivateCaCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InactivateCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InactivateDeviceCertificateRequest(TeaModel):
    def __init__(self, ca_sn=None, device_sn=None, mqtt_instance_id=None):
        self.ca_sn = ca_sn  # type: str
        self.device_sn = device_sn  # type: str
        self.mqtt_instance_id = mqtt_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InactivateDeviceCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        return self


class InactivateDeviceCertificateResponseBody(TeaModel):
    def __init__(self, device_sn=None, request_id=None):
        self.device_sn = device_sn  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InactivateDeviceCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InactivateDeviceCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: InactivateDeviceCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InactivateDeviceCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = InactivateDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCaCertificateRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None, page_no=None, page_size=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCaCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListCaCertificateResponseBodyDataCaCertificateVOS(TeaModel):
    def __init__(self, ca_content=None, ca_name=None, registration_code=None, sn=None, status=None, valid_begin=None,
                 valid_end=None, verification_content=None):
        self.ca_content = ca_content  # type: str
        self.ca_name = ca_name  # type: str
        self.registration_code = registration_code  # type: str
        self.sn = sn  # type: str
        self.status = status  # type: str
        self.valid_begin = valid_begin  # type: str
        self.valid_end = valid_end  # type: str
        self.verification_content = verification_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListCaCertificateResponseBodyDataCaCertificateVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content
        if self.ca_name is not None:
            result['CaName'] = self.ca_name
        if self.registration_code is not None:
            result['RegistrationCode'] = self.registration_code
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')
        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')
        if m.get('RegistrationCode') is not None:
            self.registration_code = m.get('RegistrationCode')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')
        return self


class ListCaCertificateResponseBodyData(TeaModel):
    def __init__(self, ca_certificate_vos=None, page_no=None, page_size=None, total=None):
        self.ca_certificate_vos = ca_certificate_vos  # type: list[ListCaCertificateResponseBodyDataCaCertificateVOS]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.ca_certificate_vos:
            for k in self.ca_certificate_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListCaCertificateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['CaCertificateVOS'] = []
        if self.ca_certificate_vos is not None:
            for k in self.ca_certificate_vos:
                result['CaCertificateVOS'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ca_certificate_vos = []
        if m.get('CaCertificateVOS') is not None:
            for k in m.get('CaCertificateVOS'):
                temp_model = ListCaCertificateResponseBodyDataCaCertificateVOS()
                self.ca_certificate_vos.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListCaCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListCaCertificateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListCaCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListCaCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListCaCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListCaCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListCaCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceCertificateRequest(TeaModel):
    def __init__(self, mqtt_instance_id=None, page_no=None, page_size=None):
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceCertificateResponseBodyDataDeviceCertificateVOS(TeaModel):
    def __init__(self, ca_sn=None, device_content=None, device_name=None, device_sn=None, status=None,
                 valid_begin=None, valid_end=None):
        self.ca_sn = ca_sn  # type: str
        self.device_content = device_content  # type: str
        self.device_name = device_name  # type: str
        self.device_sn = device_sn  # type: str
        self.status = status  # type: str
        self.valid_begin = valid_begin  # type: str
        self.valid_end = valid_end  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceCertificateResponseBodyDataDeviceCertificateVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_content is not None:
            result['DeviceContent'] = self.device_content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        return self


class ListDeviceCertificateResponseBodyData(TeaModel):
    def __init__(self, device_certificate_vos=None, page_no=None, page_size=None, total=None):
        self.device_certificate_vos = device_certificate_vos  # type: list[ListDeviceCertificateResponseBodyDataDeviceCertificateVOS]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.device_certificate_vos:
            for k in self.device_certificate_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceCertificateResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceCertificateVOS'] = []
        if self.device_certificate_vos is not None:
            for k in self.device_certificate_vos:
                result['DeviceCertificateVOS'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_certificate_vos = []
        if m.get('DeviceCertificateVOS') is not None:
            for k in m.get('DeviceCertificateVOS'):
                temp_model = ListDeviceCertificateResponseBodyDataDeviceCertificateVOS()
                self.device_certificate_vos.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceCertificateResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListDeviceCertificateResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDeviceCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDeviceCertificateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeviceCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceCertificateByCaSnRequest(TeaModel):
    def __init__(self, ca_sn=None, mqtt_instance_id=None, page_no=None, page_size=None):
        self.ca_sn = ca_sn  # type: str
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceCertificateByCaSnRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS(TeaModel):
    def __init__(self, ca_sn=None, device_content=None, device_name=None, device_sn=None, status=None,
                 valid_begin=None, valid_end=None):
        self.ca_sn = ca_sn  # type: str
        self.device_content = device_content  # type: str
        self.device_name = device_name  # type: str
        self.device_sn = device_sn  # type: str
        self.status = status  # type: str
        self.valid_begin = valid_begin  # type: str
        self.valid_end = valid_end  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_sn is not None:
            result['CaSn'] = self.ca_sn
        if self.device_content is not None:
            result['DeviceContent'] = self.device_content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_sn is not None:
            result['DeviceSn'] = self.device_sn
        if self.status is not None:
            result['Status'] = self.status
        if self.valid_begin is not None:
            result['ValidBegin'] = self.valid_begin
        if self.valid_end is not None:
            result['ValidEnd'] = self.valid_end
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaSn') is not None:
            self.ca_sn = m.get('CaSn')
        if m.get('DeviceContent') is not None:
            self.device_content = m.get('DeviceContent')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceSn') is not None:
            self.device_sn = m.get('DeviceSn')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ValidBegin') is not None:
            self.valid_begin = m.get('ValidBegin')
        if m.get('ValidEnd') is not None:
            self.valid_end = m.get('ValidEnd')
        return self


class ListDeviceCertificateByCaSnResponseBodyData(TeaModel):
    def __init__(self, device_certificate_vos=None, page_no=None, page_size=None, total=None):
        self.device_certificate_vos = device_certificate_vos  # type: list[ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS]
        self.page_no = page_no  # type: int
        self.page_size = page_size  # type: int
        self.total = total  # type: int

    def validate(self):
        if self.device_certificate_vos:
            for k in self.device_certificate_vos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListDeviceCertificateByCaSnResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceCertificateVOS'] = []
        if self.device_certificate_vos is not None:
            for k in self.device_certificate_vos:
                result['DeviceCertificateVOS'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.device_certificate_vos = []
        if m.get('DeviceCertificateVOS') is not None:
            for k in m.get('DeviceCertificateVOS'):
                temp_model = ListDeviceCertificateByCaSnResponseBodyDataDeviceCertificateVOS()
                self.device_certificate_vos.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceCertificateByCaSnResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        self.data = data  # type: ListDeviceCertificateByCaSnResponseBodyData
        self.request_id = request_id  # type: str

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(ListDeviceCertificateByCaSnResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = ListDeviceCertificateByCaSnResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceCertificateByCaSnResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceCertificateByCaSnResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceCertificateByCaSnResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeviceCertificateByCaSnResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceCredentialClientIdRequest(TeaModel):
    def __init__(self, group_id=None, instance_id=None, next_token=None, page_no=None, page_size=None):
        self.group_id = group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.next_token = next_token  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceCredentialClientIdRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList(TeaModel):
    def __init__(self, client_id_list=None, next_token=None, page_no=None, page_size=None, total=None):
        self.client_id_list = client_id_list  # type: list[str]
        self.next_token = next_token  # type: str
        self.page_no = page_no  # type: str
        self.page_size = page_size  # type: str
        self.total = total  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id_list is not None:
            result['ClientIdList'] = self.client_id_list
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientIdList') is not None:
            self.client_id_list = m.get('ClientIdList')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDeviceCredentialClientIdResponseBody(TeaModel):
    def __init__(self, device_credential_client_id_list=None, request_id=None):
        self.device_credential_client_id_list = device_credential_client_id_list  # type: ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList
        self.request_id = request_id  # type: str

    def validate(self):
        if self.device_credential_client_id_list:
            self.device_credential_client_id_list.validate()

    def to_map(self):
        _map = super(ListDeviceCredentialClientIdResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential_client_id_list is not None:
            result['DeviceCredentialClientIdList'] = self.device_credential_client_id_list.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCredentialClientIdList') is not None:
            temp_model = ListDeviceCredentialClientIdResponseBodyDeviceCredentialClientIdList()
            self.device_credential_client_id_list = temp_model.from_map(m['DeviceCredentialClientIdList'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeviceCredentialClientIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListDeviceCredentialClientIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListDeviceCredentialClientIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeviceCredentialClientIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupIdRequest(TeaModel):
    def __init__(self, instance_id=None):
        # The ID of the ApsaraMQ for MQTT instance whose groups you want to query.
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
    def __init__(self, create_time=None, group_id=None, independent_naming=None, instance_id=None, update_time=None):
        # The time when the group was created.
        self.create_time = create_time  # type: long
        # The queried group that belongs to the ApsaraMQ for MQTT instance.
        self.group_id = group_id  # type: str
        # Indicates whether a separate namespace is configured for the ApsaraMQ for MQTT instance. Valid values:
        # 
        # *   **true**: A separate namespace is configured for the ApsaraMQ for MQTT instance. Resource names must be unique within an ApsaraMQ for MQTT instance but can be the same across ApsaraMQ for MQTT instances.
        # *   **false**: No separate namespace is configured for the ApsaraMQ for MQTT instance. Resource names must be globally unique within an ApsaraMQ for MQTT instance and across ApsaraMQ for MQTT instances.
        self.independent_naming = independent_naming  # type: bool
        # The ID of the ApsaraMQ for MQTT instance to which the group belongs.
        self.instance_id = instance_id  # type: str
        # The time when the group was last updated.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListGroupIdResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListGroupIdResponseBody(TeaModel):
    def __init__(self, data=None, request_id=None):
        # The details of a queried group.
        self.data = data  # type: list[ListGroupIdResponseBodyData]
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id  # type: str

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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGroupIdResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListGroupIdResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListGroupIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListGroupIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceDeviceRequest(TeaModel):
    def __init__(self, begin_time=None, client_id=None, current_page=None, end_time=None, instance_id=None,
                 mqtt_region_id=None, page_size=None, reverse=None):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.begin_time = begin_time  # type: long
        # The client ID of the device whose trace you want to query.
        self.client_id = client_id  # type: str
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        self.current_page = current_page  # type: int
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](~~181438~~).
        self.mqtt_region_id = mqtt_region_id  # type: str
        # The number of entries to return on each page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse time order of actions on the device. This means that the information about the latest action on the device is displayed as the first entry and the information about the earliest action on the device is displayed as the last entry.
        # *   **false**: The returned results are displayed in time order of actions on the device. This means that the information about the earliest action on the device is displayed as the first entry and the information about the latest action on the device is displayed as the last entry.
        # 
        # If you do not specify this parameter, the returned results are displayed in time order of actions on the device by default.
        self.reverse = reverse  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceDeviceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceDeviceResponseBodyDeviceInfoList(TeaModel):
    def __init__(self, action=None, action_code=None, action_info=None, channel_id=None, time=None):
        # The action on the device. Valid values:
        # 
        # *   **connect**: The ApsaraMQ for MQTT client requests a connection to the ApsaraMQ for MQTT broker.
        # *   **close**: The TCP connection is closed.
        # *   **disconnect**: The ApsaraMQ for MQTT client requests a disconnection from the ApsaraMQ for MQTT broker.
        self.action = action  # type: str
        # The returned code for the action on the device. Valid values:
        # 
        # *   **mqtt.trace.action.connect**: This value is returned if the value of Action is **connect**.
        # *   **mqtt.trace.action.close**: This value is returned if the value of Action is **close**.
        # *   **mqtt.trace.action.disconnect**: This value is returned if the value of Action is **disconnect**.
        self.action_code = action_code  # type: str
        # The returned information for the action on the device. Valid values:
        # 
        # *   **accepted**: The ApsaraMQ for MQTT broker accepts the connection request from the ApsaraMQ for MQTT client.
        # *   **not authorized**: The TCP connection is closed because the permission verification of the client to access the instance fails.
        # *   **clientId conflict**: The TCP connection is closed due to a conflict in the ID of the ApsaraMQ for MQTT client.
        # *   **resource auth failed**: The TCP connection is closed because the permission verification for the ApsaraMQ for MQTT client to access the topic or group fails.
        # *   **no heart**: The TCP connection is closed because no heartbeat is detected on the client.
        # *   **closed by client**: The TCP connection is closed because an exception occurs on the client.
        # *   **disconnected by client**: The client requests a disconnection.
        # *   **invalid param**: The TCP connection is closed due to invalid request parameters.
        # *   **Socket IOException**: The TCP connection is closed due to network jitter or packet loss.
        self.action_info = action_info  # type: str
        # The connection ID.
        self.channel_id = channel_id  # type: str
        # The time when the action occurred on the device.
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceDeviceResponseBodyDeviceInfoList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceDeviceResponseBody(TeaModel):
    def __init__(self, current_page=None, device_info_list=None, page_size=None, request_id=None, total=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The details of the action on the device.
        self.device_info_list = device_info_list  # type: list[QueryMqttTraceDeviceResponseBodyDeviceInfoList]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id  # type: str
        # The total number of returned actions on the device.
        self.total = total  # type: long

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
        result['DeviceInfoList'] = []
        if self.device_info_list is not None:
            for k in self.device_info_list:
                result['DeviceInfoList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.device_info_list = []
        if m.get('DeviceInfoList') is not None:
            for k in m.get('DeviceInfoList'):
                temp_model = QueryMqttTraceDeviceResponseBodyDeviceInfoList()
                self.device_info_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMqttTraceDeviceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMqttTraceDeviceResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceDeviceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMqttTraceDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessageOfClientRequest(TeaModel):
    def __init__(self, begin_time=None, client_id=None, current_page=None, end_time=None, instance_id=None,
                 mqtt_region_id=None, page_size=None, reverse=None):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.begin_time = begin_time  # type: long
        # The client ID of the device whose messages you want to query.
        self.client_id = client_id  # type: str
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        self.current_page = current_page  # type: int
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section of the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](~~181438~~).
        self.mqtt_region_id = mqtt_region_id  # type: str
        # The number of entries to return on each page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse order of the time when messages are sent or received. This means that the latest sent or received message is displayed as the first entry and the earliest sent or received message is displayed as the last entry.
        # *   **false**: The returned results are displayed in order of the time when messages are sent or received. This means that the earliest sent or received message is displayed as the first entry and the latest sent or received message is displayed as the last entry.
        # 
        # If this parameter is not specified, the returned results are displayed in order of the time when messages are sent or received.
        self.reverse = reverse  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList(TeaModel):
    def __init__(self, action=None, action_code=None, action_info=None, client_id=None, msg_id=None, time=None):
        # The action on the message. Valid values:
        # 
        # *   **pub_mqtt**: The ApsaraMQ for MQTT client sends the message.
        # *   **sub**: The ApsaraMQ for MQTT client subscribes to the message.
        # *   **push_offline**: The ApsaraMQ for MQTT broker pushes the offline message to the ApsaraMQ for MQTT client.
        self.action = action  # type: str
        # The returned code for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.pub.mqtt**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **mqtt.trace.action.msg.sub**: This value is returned if the value of Action is **sub**.
        # *   **mqtt.trace.action.msg.push.offline**: This value is returned if the value of Action is **push_offline**.
        self.action_code = action_code  # type: str
        # The information returned for the action on the message. Valid values:
        # 
        # *   **Pub From Mqtt Client**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **Push To Mqtt Client**: This value is returned if the value of Action is **sub**.
        # *   **Push Offline Msg To Mqtt Client**: This value is returned if the value of Action is **push_offline**.
        self.action_info = action_info  # type: str
        # The client ID of the device.
        self.client_id = client_id  # type: str
        # The message ID.
        self.msg_id = msg_id  # type: str
        # The time when the message was sent or received.
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceMessageOfClientResponseBody(TeaModel):
    def __init__(self, current_page=None, message_of_client_list=None, page_size=None, request_id=None, total=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The returned messages.
        self.message_of_client_list = message_of_client_list  # type: list[QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id  # type: str
        # The total number of messages returned.
        self.total = total  # type: long

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
        result['MessageOfClientList'] = []
        if self.message_of_client_list is not None:
            for k in self.message_of_client_list:
                result['MessageOfClientList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.message_of_client_list = []
        if m.get('MessageOfClientList') is not None:
            for k in m.get('MessageOfClientList'):
                temp_model = QueryMqttTraceMessageOfClientResponseBodyMessageOfClientList()
                self.message_of_client_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMqttTraceMessageOfClientResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMqttTraceMessageOfClientResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessageOfClientResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMqttTraceMessageOfClientResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessagePublishRequest(TeaModel):
    def __init__(self, begin_time=None, end_time=None, instance_id=None, mqtt_region_id=None, msg_id=None):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.begin_time = begin_time  # type: long
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](~~181438~~).
        self.mqtt_region_id = mqtt_region_id  # type: str
        # The message ID.
        self.msg_id = msg_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class QueryMqttTraceMessagePublishResponseBodyMessageTraceLists(TeaModel):
    def __init__(self, action=None, action_code=None, action_info=None, client_id=None, msg_id=None, time=None):
        # The action on the message. Valid values:
        # 
        # *   **pub_mqtt**: indicates that the message was sent by an ApsaraMQ for MQTT client.
        # *   **pub_mq**: indicates that the message was sent by an ApsaraMQ for RocketMQ client.
        self.action = action  # type: str
        # The returned code for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.pub.mqtt**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **mqtt.trace.action.msg.pub.mq**: This value is returned if the value of Action is **pub_mq**.
        self.action_code = action_code  # type: str
        # The returned information for the action on the message. Valid values:
        # 
        # *   **Pub From Mqtt Client**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **Pub From MQ**: This value is returned if the value of Action is **pub_mq**.
        self.action_info = action_info  # type: str
        # The ID of the client that sends the message.
        self.client_id = client_id  # type: str
        # The message ID.
        self.msg_id = msg_id  # type: str
        # The time when the message was sent.
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishResponseBodyMessageTraceLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceMessagePublishResponseBody(TeaModel):
    def __init__(self, message_trace_lists=None, request_id=None):
        # The message traces.
        self.message_trace_lists = message_trace_lists  # type: list[QueryMqttTraceMessagePublishResponseBodyMessageTraceLists]
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id  # type: str

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
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k in self.message_trace_lists:
                result['MessageTraceLists'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k in m.get('MessageTraceLists'):
                temp_model = QueryMqttTraceMessagePublishResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryMqttTraceMessagePublishResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMqttTraceMessagePublishResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessagePublishResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMqttTraceMessagePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMqttTraceMessageSubscribeRequest(TeaModel):
    def __init__(self, begin_time=None, client_id=None, current_page=None, end_time=None, instance_id=None,
                 mqtt_region_id=None, msg_id=None, page_size=None, reverse=None):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.begin_time = begin_time  # type: long
        # The ID of the client that subscribes to the message. If you do not specify this parameter, the IDs of all clients that subscribe to the message are returned.
        self.client_id = client_id  # type: str
        # The number of the page to return. Pages start from page 1. If the input parameter value is greater than the total number of pages, the returned result is empty.
        self.current_page = current_page  # type: int
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        self.end_time = end_time  # type: long
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section of the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
        self.instance_id = instance_id  # type: str
        # The ID of the region where the ApsaraMQ for MQTT instance resides. For more information, see [Endpoints](~~181438~~).
        self.mqtt_region_id = mqtt_region_id  # type: str
        # The message ID.
        self.msg_id = msg_id  # type: str
        # The number of entries to return on each page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # Specifies whether the returned results are displayed in reverse chronological order. Valid values:
        # 
        # *   **true**: The returned results are displayed in reverse order of the time when messages are delivered. This means that the latest consumed message is displayed as the first entry and the earliest consumed message is displayed as the last entry.
        # *   **false**: The returned results are displayed in order of the time when messages are delivered. This means that the earliest consumed message is displayed as the first entry and the latest consumed message is displayed as the last entry.
        # 
        # If you do not specify this parameter, the returned results are displayed in order of time when messages are delivered.
        self.reverse = reverse  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_region_id is not None:
            result['MqttRegionId'] = self.mqtt_region_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.reverse is not None:
            result['Reverse'] = self.reverse
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttRegionId') is not None:
            self.mqtt_region_id = m.get('MqttRegionId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Reverse') is not None:
            self.reverse = m.get('Reverse')
        return self


class QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists(TeaModel):
    def __init__(self, action=None, action_code=None, action_info=None, client_id=None, msg_id=None, time=None):
        # The action on the message. Valid values:
        # 
        # *   **sub**: The ApsaraMQ for MQTT client subscribes to the message.
        # *   **push_offline**: The ApsaraMQ for MQTT broker pushes the offline message to the ApsaraMQ for MQTT client.
        self.action = action  # type: str
        # The code returned for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.sub**: The value that is returned if the value of Action is **sub**.
        # *   **mqtt.trace.action.msg.push.offline**: The value that is returned if the value of Action is **push_offline**.
        self.action_code = action_code  # type: str
        # The returned information for the action on the message. Valid values:
        # 
        # *   **Push To Mqtt Client**: The value that is returned if the value of Action is **sub**.
        # *   **Push Offline Msg To Mqtt Client**: The value that is returned if the value of Action is **push_offline**.
        self.action_info = action_info  # type: str
        # The ID of the client that subscribes to the message.
        self.client_id = client_id  # type: str
        # The message ID.
        self.msg_id = msg_id  # type: str
        # The time when the message was delivered.
        self.time = time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.action_code is not None:
            result['ActionCode'] = self.action_code
        if self.action_info is not None:
            result['ActionInfo'] = self.action_info
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.time is not None:
            result['Time'] = self.time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')
        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Time') is not None:
            self.time = m.get('Time')
        return self


class QueryMqttTraceMessageSubscribeResponseBody(TeaModel):
    def __init__(self, current_page=None, message_trace_lists=None, page_size=None, request_id=None, total=None):
        # The page number of the returned page.
        self.current_page = current_page  # type: int
        # The delivery trace of the queried message.
        self.message_trace_lists = message_trace_lists  # type: list[QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists]
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The unique ID that the system generates for the request. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id  # type: str
        # The returned delivery traces.
        self.total = total  # type: long

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
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k in self.message_trace_lists:
                result['MessageTraceLists'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k in m.get('MessageTraceLists'):
                temp_model = QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class QueryMqttTraceMessageSubscribeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryMqttTraceMessageSubscribeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryMqttTraceMessageSubscribeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryMqttTraceMessageSubscribeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySessionByClientIdRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        # The ID of the ApsaraMQ for MQTT client that you want to query.
        self.client_id = client_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
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
        # Indicates whether the ApsaraMQ for MQTT client is connected to the ApsaraMQ for MQTT broker. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.online_status = online_status  # type: bool
        # The request ID. This parameter is a common parameter.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySessionByClientIdResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySessionByClientIdResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySessionByClientIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryTokenRequest(TeaModel):
    def __init__(self, instance_id=None, token=None):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com/).
        self.instance_id = instance_id  # type: str
        # The token that you want to query.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class QueryTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token_status=None):
        # The unique ID that the system generates for the request. This parameter is a common parameter.
        self.request_id = request_id  # type: str
        # The status of the queried token. Valid values:
        # 
        # *   **true**: indicates the token is valid.
        # *   **false**: indicates the token is invalid.
        self.token_status = token_status  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RefreshDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        # The client ID of the device whose access credential you want to update.
        self.client_id = client_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
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
    def __init__(self, client_id=None, create_time=None, device_access_key_id=None, device_access_key_secret=None,
                 instance_id=None, update_time=None):
        # The client ID of the device.
        self.client_id = client_id  # type: str
        # The timestamp that indicates when the access credential of the device was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.create_time = create_time  # type: long
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id  # type: str
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret  # type: str
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id  # type: str
        # The timestamp that indicates when the access credential of the device was last updated. The value of this parameter is a UNIX timestamp in milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RefreshDeviceCredentialResponseBodyDeviceCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class RefreshDeviceCredentialResponseBody(TeaModel):
    def __init__(self, device_credential=None, request_id=None):
        # The access credential of the device.
        self.device_credential = device_credential  # type: RefreshDeviceCredentialResponseBodyDeviceCredential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super(RefreshDeviceCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = RefreshDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RefreshDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RefreshDeviceCredentialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RefreshDeviceCredentialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RefreshDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterCaCertificateRequest(TeaModel):
    def __init__(self, ca_content=None, ca_name=None, mqtt_instance_id=None, verification_content=None):
        self.ca_content = ca_content  # type: str
        self.ca_name = ca_name  # type: str
        self.mqtt_instance_id = mqtt_instance_id  # type: str
        self.verification_content = verification_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterCaCertificateRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ca_content is not None:
            result['CaContent'] = self.ca_content
        if self.ca_name is not None:
            result['CaName'] = self.ca_name
        if self.mqtt_instance_id is not None:
            result['MqttInstanceId'] = self.mqtt_instance_id
        if self.verification_content is not None:
            result['VerificationContent'] = self.verification_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CaContent') is not None:
            self.ca_content = m.get('CaContent')
        if m.get('CaName') is not None:
            self.ca_name = m.get('CaName')
        if m.get('MqttInstanceId') is not None:
            self.mqtt_instance_id = m.get('MqttInstanceId')
        if m.get('VerificationContent') is not None:
            self.verification_content = m.get('VerificationContent')
        return self


class RegisterCaCertificateResponseBody(TeaModel):
    def __init__(self, request_id=None, sn=None):
        self.request_id = request_id  # type: str
        self.sn = sn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterCaCertificateResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class RegisterCaCertificateResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterCaCertificateResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterCaCertificateResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegisterCaCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        # The client ID of the device for which you want to create an access credential.
        self.client_id = client_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
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
    def __init__(self, client_id=None, create_time=None, device_access_key_id=None, device_access_key_secret=None,
                 instance_id=None, update_time=None):
        # The client ID of the device.
        self.client_id = client_id  # type: str
        # The timestamp that indicates when the access credential of the device was created. Unit: milliseconds.
        self.create_time = create_time  # type: long
        # The AccessKey ID of the device.
        self.device_access_key_id = device_access_key_id  # type: str
        # The AccessKey secret of the device.
        self.device_access_key_secret = device_access_key_secret  # type: str
        # The ID of the ApsaraMQ for MQTT instance.
        self.instance_id = instance_id  # type: str
        # The timestamp that indicates when the access credential of the device was last updated. Unit: milliseconds.
        self.update_time = update_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RegisterDeviceCredentialResponseBodyDeviceCredential, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.device_access_key_id is not None:
            result['DeviceAccessKeyId'] = self.device_access_key_id
        if self.device_access_key_secret is not None:
            result['DeviceAccessKeySecret'] = self.device_access_key_secret
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeviceAccessKeyId') is not None:
            self.device_access_key_id = m.get('DeviceAccessKeyId')
        if m.get('DeviceAccessKeySecret') is not None:
            self.device_access_key_secret = m.get('DeviceAccessKeySecret')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class RegisterDeviceCredentialResponseBody(TeaModel):
    def __init__(self, device_credential=None, request_id=None):
        # The access credential of the device.
        self.device_credential = device_credential  # type: RegisterDeviceCredentialResponseBodyDeviceCredential
        # The request ID. This parameter is a common parameter.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.device_credential:
            self.device_credential.validate()

    def to_map(self):
        _map = super(RegisterDeviceCredentialResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_credential is not None:
            result['DeviceCredential'] = self.device_credential.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DeviceCredential') is not None:
            temp_model = RegisterDeviceCredentialResponseBodyDeviceCredential()
            self.device_credential = temp_model.from_map(m['DeviceCredential'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RegisterDeviceCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RegisterDeviceCredentialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RegisterDeviceCredentialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RegisterDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RevokeTokenRequest(TeaModel):
    def __init__(self, instance_id=None, token=None):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com/).
        self.instance_id = instance_id  # type: str
        # The token that you want to revoke.
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RevokeTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class RevokeTokenResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID. This parameter is a common parameter.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RevokeTokenResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RevokeTokenResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RevokeTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(self, instance_id=None, mqtt_topic=None, payload=None):
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can view the instance ID in the **Basic Information** section on the **Instance Details** page that corresponds to the instance in the [ApsaraMQ for MQTT console](https://mqtt.console.aliyun.com).
        self.instance_id = instance_id  # type: str
        # The topic to which you want to send a message on the ApsaraMQ for MQTT instance.
        self.mqtt_topic = mqtt_topic  # type: str
        # The message content, which is the payload of the message. We recommend that you encode the content in Base64 to prevent non-printable characters from being transmitted.
        self.payload = payload  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SendMessageRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mqtt_topic is not None:
            result['MqttTopic'] = self.mqtt_topic
        if self.payload is not None:
            result['Payload'] = self.payload
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MqttTopic') is not None:
            self.mqtt_topic = m.get('MqttTopic')
        if m.get('Payload') is not None:
            self.payload = m.get('Payload')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(self, msg_id=None, request_id=None):
        # The unique message ID that is returned by the ApsaraMQ for MQTT broker after the message is sent.
        self.msg_id = msg_id  # type: str
        # The unique ID that the system generates for the request. This parameter is a common parameter.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: SendMessageResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SendMessageResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnRegisterDeviceCredentialRequest(TeaModel):
    def __init__(self, client_id=None, instance_id=None):
        # The client ID of the device whose access credential you want to deregister.
        self.client_id = client_id  # type: str
        # The ID of the ApsaraMQ for MQTT instance. The ID must be consistent with the ID of the instance that the ApsaraMQ for MQTT client uses. You can obtain the instance ID on the **Instance Details** page that corresponds to the instance in the ApsaraMQ for MQTT console.
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
        # The unique ID that the system generates for the request. This parameter is a common parameter.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnRegisterDeviceCredentialResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnRegisterDeviceCredentialResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnRegisterDeviceCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


