# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class EndpointStatus(TeaModel):
    def __init__(self, code=None, detail=None, message=None, phase=None):
        self.code = code  # type: str
        self.detail = detail  # type: EndpointStatusDetail
        self.message = message  # type: str
        self.phase = phase  # type: str

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super(EndpointStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            temp_model = EndpointStatusDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        return self


class EndpointStatusDetail(TeaModel):
    def __init__(self, ip_port_mapping=None):
        self.ip_port_mapping = ip_port_mapping  # type: dict[str, IpPort]

    def validate(self):
        if self.ip_port_mapping:
            for v in self.ip_port_mapping.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super(EndpointStatusDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpPortMapping'] = {}
        if self.ip_port_mapping is not None:
            for k, v in self.ip_port_mapping.items():
                result['IpPortMapping'][k] = v.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ip_port_mapping = {}
        if m.get('IpPortMapping') is not None:
            for k, v in m.get('IpPortMapping').items():
                temp_model = IpPort()
                self.ip_port_mapping[k] = temp_model.from_map(v)
        return self


class InstanceLifeCycle(TeaModel):
    def __init__(self, config=None, type=None):
        self.config = config  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceLifeCycle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class InstanceStatus(TeaModel):
    def __init__(self, code=None, message=None, phase=None, slot_num=None, used_capacity=None):
        self.code = code  # type: str
        self.message = message  # type: str
        self.phase = phase  # type: str
        self.slot_num = slot_num  # type: int
        self.used_capacity = used_capacity  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InstanceStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.slot_num is not None:
            result['SlotNum'] = self.slot_num
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SlotNum') is not None:
            self.slot_num = m.get('SlotNum')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        return self


class IpPort(TeaModel):
    def __init__(self, ip=None, port=None):
        self.ip = ip  # type: str
        self.port = port  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(IpPort, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.port is not None:
            result['Port'] = self.port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        return self


class Metric(TeaModel):
    def __init__(self, timestamp=None, value=None):
        self.timestamp = timestamp  # type: str
        self.value = value  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(Metric, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SlotLifeCycle(TeaModel):
    def __init__(self, config=None, type=None):
        self.config = config  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SlotLifeCycle, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SlotStatus(TeaModel):
    def __init__(self, code=None, detail=None, message=None, phase=None):
        self.code = code  # type: str
        self.detail = detail  # type: SlotStatusDetail
        self.message = message  # type: str
        self.phase = phase  # type: str

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super(SlotStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.detail is not None:
            result['Detail'] = self.detail.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.phase is not None:
            result['Phase'] = self.phase
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Detail') is not None:
            temp_model = SlotStatusDetail()
            self.detail = temp_model.from_map(m['Detail'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        return self


class SlotStatusDetail(TeaModel):
    def __init__(self, loaded_file_num=None, loaded_file_size=None, loading_time_cost=None):
        self.loaded_file_num = loaded_file_num  # type: long
        self.loaded_file_size = loaded_file_size  # type: str
        self.loading_time_cost = loading_time_cost  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(SlotStatusDetail, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loaded_file_num is not None:
            result['LoadedFileNum'] = self.loaded_file_num
        if self.loaded_file_size is not None:
            result['LoadedFileSize'] = self.loaded_file_size
        if self.loading_time_cost is not None:
            result['LoadingTimeCost'] = self.loading_time_cost
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoadedFileNum') is not None:
            self.loaded_file_num = m.get('LoadedFileNum')
        if m.get('LoadedFileSize') is not None:
            self.loaded_file_size = m.get('LoadedFileSize')
        if m.get('LoadingTimeCost') is not None:
            self.loading_time_cost = m.get('LoadingTimeCost')
        return self


class BindEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindEndpointResponseBody, self).to_map()
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


class BindEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEndpointRequest(TeaModel):
    def __init__(self, instance_id=None, name=None, type=None, vpc_id=None, vswitch_id=None):
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateEndpointResponseBody(TeaModel):
    def __init__(self, endpoint_id=None, request_id=None):
        self.endpoint_id = endpoint_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceRequestTags, self).to_map()
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


class CreateInstanceRequest(TeaModel):
    def __init__(self, capacity=None, description=None, max_endpoint=None, max_slot=None, name=None,
                 payment_type=None, provider_type=None, storage_type=None, tags=None, type=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.max_endpoint = max_endpoint  # type: str
        self.max_slot = max_slot  # type: str
        self.name = name  # type: str
        self.payment_type = payment_type  # type: str
        self.provider_type = provider_type  # type: str
        self.storage_type = storage_type  # type: str
        self.tags = tags  # type: list[CreateInstanceRequestTags]
        self.type = type  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.max_endpoint is not None:
            result['MaxEndpoint'] = self.max_endpoint
        if self.max_slot is not None:
            result['MaxSlot'] = self.max_slot
        if self.name is not None:
            result['Name'] = self.name
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxEndpoint') is not None:
            self.max_endpoint = m.get('MaxEndpoint')
        if m.get('MaxSlot') is not None:
            self.max_slot = m.get('MaxSlot')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateInstanceRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlotRequestEndpoints(TeaModel):
    def __init__(self, name=None, type=None, vpc_id=None, vswitch_id=None):
        self.name = name  # type: str
        self.type = type  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlotRequestEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class CreateSlotRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlotRequestTags, self).to_map()
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


class CreateSlotRequest(TeaModel):
    def __init__(self, capacity=None, description=None, endpoint_ids=None, endpoints=None, instance_id=None,
                 life_cycle=None, name=None, storage_type=None, storage_uri=None, tags=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.endpoint_ids = endpoint_ids  # type: str
        self.endpoints = endpoints  # type: list[CreateSlotRequestEndpoints]
        self.instance_id = instance_id  # type: str
        self.life_cycle = life_cycle  # type: SlotLifeCycle
        self.name = name  # type: str
        self.storage_type = storage_type  # type: str
        self.storage_uri = storage_uri  # type: str
        self.tags = tags  # type: list[CreateSlotRequestTags]

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.life_cycle:
            self.life_cycle.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSlotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = CreateSlotRequestEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LifeCycle') is not None:
            temp_model = SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m['LifeCycle'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateSlotRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateSlotResponseBody(TeaModel):
    def __init__(self, endpoint_ids=None, request_id=None, slot_id=None):
        self.endpoint_ids = endpoint_ids  # type: str
        self.request_id = request_id  # type: str
        self.slot_id = slot_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slot_id is not None:
            result['SlotId'] = self.slot_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlotId') is not None:
            self.slot_id = m.get('SlotId')
        return self


class CreateSlotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSlotsRequestSlotsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlotsRequestSlotsTags, self).to_map()
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


class CreateSlotsRequestSlots(TeaModel):
    def __init__(self, capacity=None, description=None, endpoint_ids=None, instance_id=None, life_cycle=None,
                 name=None, storage_type=None, storage_uri=None, tags=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.endpoint_ids = endpoint_ids  # type: str
        self.instance_id = instance_id  # type: str
        self.life_cycle = life_cycle  # type: SlotLifeCycle
        self.name = name  # type: str
        self.storage_type = storage_type  # type: str
        self.storage_uri = storage_uri  # type: str
        self.tags = tags  # type: list[CreateSlotsRequestSlotsTags]

    def validate(self):
        if self.life_cycle:
            self.life_cycle.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSlotsRequestSlots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('LifeCycle') is not None:
            temp_model = SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m['LifeCycle'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = CreateSlotsRequestSlotsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class CreateSlotsRequest(TeaModel):
    def __init__(self, dry_run=None, slots=None):
        self.dry_run = dry_run  # type: bool
        self.slots = slots  # type: list[CreateSlotsRequestSlots]

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSlotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = CreateSlotsRequestSlots()
                self.slots.append(temp_model.from_map(k))
        return self


class CreateSlotsResponseBody(TeaModel):
    def __init__(self, request_id=None, slot_ids=None, summary=None):
        self.request_id = request_id  # type: str
        self.slot_ids = slot_ids  # type: str
        self.summary = summary  # type: dict[str, str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSlotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slot_ids is not None:
            result['SlotIds'] = self.slot_ids
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlotIds') is not None:
            self.slot_ids = m.get('SlotIds')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class CreateSlotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSlotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSlotsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSlotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(self, key=None, resource_id=None, resource_type=None, value=None):
        self.key = key  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateTagResponseBody, self).to_map()
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


class CreateTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEndpointResponseBody, self).to_map()
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


class DeleteEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteInstanceResponseBody, self).to_map()
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


class DeleteInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSlotRequest(TeaModel):
    def __init__(self, force=None):
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSlotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteSlotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSlotResponseBody, self).to_map()
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


class DeleteSlotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTagRequest(TeaModel):
    def __init__(self, key=None, resource_id=None, resource_type=None):
        self.key = key  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DeleteTagResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteTagResponseBody, self).to_map()
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


class DeleteTagResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteTagResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteTagResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeComponentRequest(TeaModel):
    def __init__(self, render_template=None, values=None):
        self.render_template = render_template  # type: bool
        self.values = values  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.render_template is not None:
            result['RenderTemplate'] = self.render_template
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenderTemplate') is not None:
            self.render_template = m.get('RenderTemplate')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class DescribeComponentShrinkRequest(TeaModel):
    def __init__(self, render_template=None, values_shrink=None):
        self.render_template = render_template  # type: bool
        self.values_shrink = values_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.render_template is not None:
            result['RenderTemplate'] = self.render_template
        if self.values_shrink is not None:
            result['Values'] = self.values_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RenderTemplate') is not None:
            self.render_template = m.get('RenderTemplate')
        if m.get('Values') is not None:
            self.values_shrink = m.get('Values')
        return self


class DescribeComponentResponseBodyTemplate(TeaModel):
    def __init__(self, type=None, uri=None):
        self.type = type  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeComponentResponseBodyTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class DescribeComponentResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, name=None, owner_id=None,
                 rendered_content=None, request_id=None, template=None, user_id=None, uuid=None, version=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.rendered_content = rendered_content  # type: str
        self.request_id = request_id  # type: str
        self.template = template  # type: DescribeComponentResponseBodyTemplate
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(DescribeComponentResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.rendered_content is not None:
            result['RenderedContent'] = self.rendered_content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RenderedContent') is not None:
            self.rendered_content = m.get('RenderedContent')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Template') is not None:
            temp_model = DescribeComponentResponseBodyTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeComponentResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeComponentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeComponentResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeComponentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEndpointResponseBody(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, name=None, owner_id=None, request_id=None,
                 status=None, type=None, user_id=None, uuid=None, vpc_id=None, vswitch_id=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: EndpointStatus
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(DescribeEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = EndpointStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceResponseBodyTags, self).to_map()
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


class DescribeInstanceResponseBody(TeaModel):
    def __init__(self, capacity=None, description=None, gmt_create_time=None, gmt_modified_time=None, io_type=None,
                 max_endpoint=None, max_slot=None, name=None, owner_id=None, payment_type=None, provider_type=None,
                 request_id=None, status=None, storage_type=None, tags=None, type=None, user_id=None, uuid=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.io_type = io_type  # type: str
        # 数据集加速实例的最大挂载点个数。
        self.max_endpoint = max_endpoint  # type: int
        self.max_slot = max_slot  # type: int
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.payment_type = payment_type  # type: str
        # 数据集加速实例的资源提供者类型。
        self.provider_type = provider_type  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: InstanceStatus
        # 数据集加速实例的存储类型。
        self.storage_type = storage_type  # type: str
        self.tags = tags  # type: list[DescribeInstanceResponseBodyTags]
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.status:
            self.status.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.io_type is not None:
            result['IoType'] = self.io_type
        if self.max_endpoint is not None:
            result['MaxEndpoint'] = self.max_endpoint
        if self.max_slot is not None:
            result['MaxSlot'] = self.max_slot
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')
        if m.get('MaxEndpoint') is not None:
            self.max_endpoint = m.get('MaxEndpoint')
        if m.get('MaxSlot') is not None:
            self.max_slot = m.get('MaxSlot')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = InstanceStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSlotResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeSlotResponseBodyTags, self).to_map()
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


class DescribeSlotResponseBody(TeaModel):
    def __init__(self, capacity=None, description=None, gmt_create_time=None, gmt_modified_time=None,
                 instance_id=None, io_type=None, life_cycle=None, name=None, owner_id=None, request_id=None, status=None,
                 storage_type=None, storage_uri=None, tags=None, user_id=None, uuid=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
        # 数据集加速槽的读写类型。
        self.io_type = io_type  # type: str
        self.life_cycle = life_cycle  # type: SlotLifeCycle
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.request_id = request_id  # type: str
        self.status = status  # type: SlotStatus
        self.storage_type = storage_type  # type: str
        self.storage_uri = storage_uri  # type: str
        self.tags = tags  # type: list[DescribeSlotResponseBodyTags]
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.life_cycle:
            self.life_cycle.validate()
        if self.status:
            self.status.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeSlotResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_type is not None:
            result['IoType'] = self.io_type
        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')
        if m.get('LifeCycle') is not None:
            temp_model = SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m['LifeCycle'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            temp_model = SlotStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeSlotResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class DescribeSlotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(self, component_ids=None, name=None, order=None, page_number=None, page_size=None, sort_by=None,
                 version=None):
        self.component_ids = component_ids  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.sort_by = sort_by  # type: str
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ComponentIds') is not None:
            self.component_ids = m.get('ComponentIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListComponentsResponseBodyComponentsTemplate(TeaModel):
    def __init__(self, type=None, uri=None):
        self.type = type  # type: str
        self.uri = uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListComponentsResponseBodyComponentsTemplate, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.uri is not None:
            result['Uri'] = self.uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')
        return self


class ListComponentsResponseBodyComponents(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, name=None, owner_id=None, template=None,
                 user_id=None, uuid=None, version=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.template = template  # type: ListComponentsResponseBodyComponentsTemplate
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str
        self.version = version  # type: str

    def validate(self):
        if self.template:
            self.template.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBodyComponents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.template is not None:
            result['Template'] = self.template.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Template') is not None:
            temp_model = ListComponentsResponseBodyComponentsTemplate()
            self.template = temp_model.from_map(m['Template'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(self, components=None, request_id=None, total_count=None):
        self.components = components  # type: list[ListComponentsResponseBodyComponents]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListComponentsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = ListComponentsResponseBodyComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListComponentsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListComponentsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListComponentsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEndpointsRequest(TeaModel):
    def __init__(self, endpoint_ids=None, instance_ids=None, name=None, order=None, page_number=None, page_size=None,
                 slot_ids=None, sort_by=None, type=None):
        self.endpoint_ids = endpoint_ids  # type: str
        # 所属加速实例的ID。
        self.instance_ids = instance_ids  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.slot_ids = slot_ids  # type: str
        self.sort_by = sort_by  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.slot_ids is not None:
            result['SlotIds'] = self.slot_ids
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SlotIds') is not None:
            self.slot_ids = m.get('SlotIds')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, instance_id=None, name=None, owner_id=None,
                 status=None, type=None, user_id=None, uuid=None, vpc_id=None, vswitch_id=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        # 所属加速实例的ID。
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.status = status  # type: EndpointStatus
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(ListEndpointsResponseBodyEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            temp_model = EndpointStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class ListEndpointsResponseBody(TeaModel):
    def __init__(self, endpoints=None, request_id=None, total_count=None):
        self.endpoints = endpoints  # type: list[ListEndpointsResponseBodyEndpoints]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListEndpointsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(self, instance_ids=None, name=None, order=None, page_number=None, page_size=None, payment_type=None,
                 phase=None, sort_by=None, type=None):
        self.instance_ids = instance_ids  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.payment_type = payment_type  # type: str
        self.phase = phase  # type: str
        self.sort_by = sort_by  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListInstancesResponseBodyInstancesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstancesTags, self).to_map()
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


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(self, capacity=None, description=None, gmt_create_time=None, gmt_modified_time=None, io_type=None,
                 max_endpoint=None, max_slot=None, name=None, owner_id=None, payment_type=None, provider_type=None, status=None,
                 storage_type=None, tags=None, type=None, user_id=None, uuid=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.io_type = io_type  # type: str
        # 数据集加速实例的最大挂载点个数。
        self.max_endpoint = max_endpoint  # type: int
        self.max_slot = max_slot  # type: int
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.payment_type = payment_type  # type: str
        # 数据集加速实例的资源提供者类型。
        self.provider_type = provider_type  # type: str
        self.status = status  # type: InstanceStatus
        # 数据集加速实例的存储类型。
        self.storage_type = storage_type  # type: str
        self.tags = tags  # type: list[ListInstancesResponseBodyInstancesTags]
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.status:
            self.status.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.io_type is not None:
            result['IoType'] = self.io_type
        if self.max_endpoint is not None:
            result['MaxEndpoint'] = self.max_endpoint
        if self.max_slot is not None:
            result['MaxSlot'] = self.max_slot
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type
        if self.provider_type is not None:
            result['ProviderType'] = self.provider_type
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')
        if m.get('MaxEndpoint') is not None:
            self.max_endpoint = m.get('MaxEndpoint')
        if m.get('MaxSlot') is not None:
            self.max_slot = m.get('MaxSlot')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')
        if m.get('ProviderType') is not None:
            self.provider_type = m.get('ProviderType')
        if m.get('Status') is not None:
            temp_model = InstanceStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstancesResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        self.instances = instances  # type: list[ListInstancesResponseBodyInstances]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListInstancesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSlotsRequest(TeaModel):
    def __init__(self, endpoint_ids=None, instance_ids=None, name=None, order=None, page_number=None, page_size=None,
                 phase=None, slot_ids=None, sort_by=None, storage_type=None, storage_uri=None):
        # 加速槽所对应的数据集加速挂载点的唯一标识符。
        self.endpoint_ids = endpoint_ids  # type: str
        self.instance_ids = instance_ids  # type: str
        self.name = name  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.phase = phase  # type: str
        self.slot_ids = slot_ids  # type: str
        self.sort_by = sort_by  # type: str
        self.storage_type = storage_type  # type: str
        # 数据集加速槽的数据存储路径（URI）。
        self.storage_uri = storage_uri  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSlotsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_ids is not None:
            result['EndpointIds'] = self.endpoint_ids
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.name is not None:
            result['Name'] = self.name
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.phase is not None:
            result['Phase'] = self.phase
        if self.slot_ids is not None:
            result['SlotIds'] = self.slot_ids
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointIds') is not None:
            self.endpoint_ids = m.get('EndpointIds')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Phase') is not None:
            self.phase = m.get('Phase')
        if m.get('SlotIds') is not None:
            self.slot_ids = m.get('SlotIds')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')
        return self


class ListSlotsResponseBodySlotsEndpoints(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, name=None, owner_id=None, status=None,
                 type=None, user_id=None, uuid=None, vpc_id=None, vswitch_id=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.status = status  # type: EndpointStatus
        self.type = type  # type: str
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(ListSlotsResponseBodySlotsEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            temp_model = EndpointStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class ListSlotsResponseBodySlotsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSlotsResponseBodySlotsTags, self).to_map()
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


class ListSlotsResponseBodySlots(TeaModel):
    def __init__(self, capacity=None, description=None, endpoints=None, gmt_create_time=None,
                 gmt_modified_time=None, instance_id=None, io_type=None, life_cycle=None, name=None, owner_id=None, status=None,
                 storage_type=None, storage_uri=None, tags=None, user_id=None, uuid=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.endpoints = endpoints  # type: list[ListSlotsResponseBodySlotsEndpoints]
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.instance_id = instance_id  # type: str
        # 数据集加速槽的读写类型。
        self.io_type = io_type  # type: str
        self.life_cycle = life_cycle  # type: SlotLifeCycle
        self.name = name  # type: str
        self.owner_id = owner_id  # type: str
        self.status = status  # type: SlotStatus
        self.storage_type = storage_type  # type: str
        self.storage_uri = storage_uri  # type: str
        self.tags = tags  # type: list[ListSlotsResponseBodySlotsTags]
        self.user_id = user_id  # type: str
        self.uuid = uuid  # type: str

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()
        if self.life_cycle:
            self.life_cycle.validate()
        if self.status:
            self.status.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSlotsResponseBodySlots, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.io_type is not None:
            result['IoType'] = self.io_type
        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.status is not None:
            result['Status'] = self.status.to_map()
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListSlotsResponseBodySlotsEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IoType') is not None:
            self.io_type = m.get('IoType')
        if m.get('LifeCycle') is not None:
            temp_model = SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m['LifeCycle'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('Status') is not None:
            temp_model = SlotStatus()
            self.status = temp_model.from_map(m['Status'])
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListSlotsResponseBodySlotsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListSlotsResponseBody(TeaModel):
    def __init__(self, request_id=None, slots=None, total_count=None):
        self.request_id = request_id  # type: str
        self.slots = slots  # type: list[ListSlotsResponseBodySlots]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.slots:
            for k in self.slots:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSlotsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Slots'] = []
        if self.slots is not None:
            for k in self.slots:
                result['Slots'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.slots = []
        if m.get('Slots') is not None:
            for k in m.get('Slots'):
                temp_model = ListSlotsResponseBodySlots()
                self.slots.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSlotsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSlotsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSlotsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSlotsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(self, key=None, order=None, page_number=None, page_size=None, resource_id=None, resource_type=None,
                 sort_by=None, value=None):
        self.key = key  # type: str
        self.order = order  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.sort_by = sort_by  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.order is not None:
            result['Order'] = self.order
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagsResponseBodyTags(TeaModel):
    def __init__(self, gmt_create_time=None, gmt_modified_time=None, key=None, owner_id=None, resource_id=None,
                 resource_type=None, user_id=None, value=None):
        self.gmt_create_time = gmt_create_time  # type: str
        self.gmt_modified_time = gmt_modified_time  # type: str
        self.key = key  # type: str
        self.owner_id = owner_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.user_id = user_id  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagsResponseBodyTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time
        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time
        if self.key is not None:
            result['Key'] = self.key
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')
        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(self, request_id=None, tags=None, total_count=None):
        self.request_id = request_id  # type: str
        self.tags = tags  # type: list[ListTagsResponseBodyTags]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInstanceMetricsRequest(TeaModel):
    def __init__(self, dimensions=None, end_time=None, metric_type=None, start_time=None, time_step=None):
        self.dimensions = dimensions  # type: dict[str, any]
        self.end_time = end_time  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInstanceMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        return self


class QueryInstanceMetricsShrinkRequest(TeaModel):
    def __init__(self, dimensions_shrink=None, end_time=None, metric_type=None, start_time=None, time_step=None):
        self.dimensions_shrink = dimensions_shrink  # type: str
        self.end_time = end_time  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryInstanceMetricsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions_shrink is not None:
            result['Dimensions'] = self.dimensions_shrink
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions_shrink = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        return self


class QueryInstanceMetricsResponseBody(TeaModel):
    def __init__(self, metrics=None, period=None, request_id=None):
        self.metrics = metrics  # type: list[Metric]
        self.period = period  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QueryInstanceMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryInstanceMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryInstanceMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryInstanceMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryInstanceMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QuerySlotMetricsRequest(TeaModel):
    def __init__(self, dimensions=None, end_time=None, metric_type=None, start_time=None, time_step=None):
        self.dimensions = dimensions  # type: dict[str, any]
        self.end_time = end_time  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySlotMetricsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        return self


class QuerySlotMetricsShrinkRequest(TeaModel):
    def __init__(self, dimensions_shrink=None, end_time=None, metric_type=None, start_time=None, time_step=None):
        self.dimensions_shrink = dimensions_shrink  # type: str
        self.end_time = end_time  # type: str
        self.metric_type = metric_type  # type: str
        self.start_time = start_time  # type: str
        self.time_step = time_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QuerySlotMetricsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions_shrink is not None:
            result['Dimensions'] = self.dimensions_shrink
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_type is not None:
            result['MetricType'] = self.metric_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.time_step is not None:
            result['TimeStep'] = self.time_step
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions_shrink = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricType') is not None:
            self.metric_type = m.get('MetricType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TimeStep') is not None:
            self.time_step = m.get('TimeStep')
        return self


class QuerySlotMetricsResponseBody(TeaModel):
    def __init__(self, metrics=None, period=None, request_id=None):
        self.metrics = metrics  # type: list[Metric]
        self.period = period  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(QuerySlotMetricsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Metrics'] = []
        if self.metrics is not None:
            for k in self.metrics:
                result['Metrics'].append(k.to_map() if k else None)
        if self.period is not None:
            result['Period'] = self.period
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.metrics = []
        if m.get('Metrics') is not None:
            for k in m.get('Metrics'):
                temp_model = Metric()
                self.metrics.append(temp_model.from_map(k))
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QuerySlotMetricsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QuerySlotMetricsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QuerySlotMetricsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QuerySlotMetricsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryStatisticRequest(TeaModel):
    def __init__(self, end_time=None, fields=None, start_time=None):
        self.end_time = end_time  # type: str
        self.fields = fields  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStatisticRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.fields is not None:
            result['Fields'] = self.fields
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class QueryStatisticResponseBody(TeaModel):
    def __init__(self, instance_capacity_each_type=None, instance_num_each_type=None, request_id=None,
                 slot_num_each_type=None):
        self.instance_capacity_each_type = instance_capacity_each_type  # type: dict[str, any]
        self.instance_num_each_type = instance_num_each_type  # type: dict[str, any]
        self.request_id = request_id  # type: str
        self.slot_num_each_type = slot_num_each_type  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(QueryStatisticResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_capacity_each_type is not None:
            result['InstanceCapacityEachType'] = self.instance_capacity_each_type
        if self.instance_num_each_type is not None:
            result['InstanceNumEachType'] = self.instance_num_each_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.slot_num_each_type is not None:
            result['SlotNumEachType'] = self.slot_num_each_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceCapacityEachType') is not None:
            self.instance_capacity_each_type = m.get('InstanceCapacityEachType')
        if m.get('InstanceNumEachType') is not None:
            self.instance_num_each_type = m.get('InstanceNumEachType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SlotNumEachType') is not None:
            self.slot_num_each_type = m.get('SlotNumEachType')
        return self


class QueryStatisticResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: QueryStatisticResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(QueryStatisticResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = QueryStatisticResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReloadSlotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReloadSlotResponseBody, self).to_map()
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


class ReloadSlotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReloadSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReloadSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReloadSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopSlotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopSlotResponseBody, self).to_map()
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


class StopSlotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindEndpointResponseBody, self).to_map()
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


class UnbindEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindEndpointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceRequest(TeaModel):
    def __init__(self, description=None, max_slot=None, name=None):
        self.description = description  # type: str
        self.max_slot = max_slot  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.max_slot is not None:
            result['MaxSlot'] = self.max_slot
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('MaxSlot') is not None:
            self.max_slot = m.get('MaxSlot')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateInstanceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateInstanceResponseBody, self).to_map()
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


class UpdateInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateInstanceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSlotRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSlotRequestTags, self).to_map()
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


class UpdateSlotRequest(TeaModel):
    def __init__(self, capacity=None, description=None, life_cycle=None, name=None, storage_type=None,
                 storage_uri=None, tags=None):
        self.capacity = capacity  # type: str
        self.description = description  # type: str
        self.life_cycle = life_cycle  # type: SlotLifeCycle
        self.name = name  # type: str
        self.storage_type = storage_type  # type: str
        self.storage_uri = storage_uri  # type: str
        self.tags = tags  # type: list[UpdateSlotRequestTags]

    def validate(self):
        if self.life_cycle:
            self.life_cycle.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateSlotRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.description is not None:
            result['Description'] = self.description
        if self.life_cycle is not None:
            result['LifeCycle'] = self.life_cycle.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.storage_uri is not None:
            result['StorageUri'] = self.storage_uri
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('LifeCycle') is not None:
            temp_model = SlotLifeCycle()
            self.life_cycle = temp_model.from_map(m['LifeCycle'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('StorageUri') is not None:
            self.storage_uri = m.get('StorageUri')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = UpdateSlotRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class UpdateSlotResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSlotResponseBody, self).to_map()
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


class UpdateSlotResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSlotResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSlotResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSlotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


