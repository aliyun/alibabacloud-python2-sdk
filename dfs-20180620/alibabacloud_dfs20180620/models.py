# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachVscMountPointRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, input_region_id=None, instance_ids=None,
                 mount_point_id=None, vsc_ids=None, vsc_type=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_ids = instance_ids  # type: list[str]
        self.mount_point_id = mount_point_id  # type: str
        self.vsc_ids = vsc_ids  # type: list[str]
        self.vsc_type = vsc_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachVscMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.vsc_ids is not None:
            result['VscIds'] = self.vsc_ids
        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('VscIds') is not None:
            self.vsc_ids = m.get('VscIds')
        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')
        return self


class AttachVscMountPointShrinkRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, input_region_id=None, instance_ids_shrink=None,
                 mount_point_id=None, vsc_ids_shrink=None, vsc_type=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_ids_shrink = instance_ids_shrink  # type: str
        self.mount_point_id = mount_point_id  # type: str
        self.vsc_ids_shrink = vsc_ids_shrink  # type: str
        self.vsc_type = vsc_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachVscMountPointShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.vsc_ids_shrink is not None:
            result['VscIds'] = self.vsc_ids_shrink
        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('VscIds') is not None:
            self.vsc_ids_shrink = m.get('VscIds')
        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')
        return self


class AttachVscMountPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachVscMountPointResponseBody, self).to_map()
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


class AttachVscMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachVscMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachVscMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachVscMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindVscMountPointAliasRequest(TeaModel):
    def __init__(self, alias_prefix=None, file_system_id=None, input_region_id=None, mount_point_id=None):
        self.alias_prefix = alias_prefix  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.mount_point_id = mount_point_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindVscMountPointAliasRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_prefix is not None:
            result['AliasPrefix'] = self.alias_prefix
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliasPrefix') is not None:
            self.alias_prefix = m.get('AliasPrefix')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class BindVscMountPointAliasResponseBody(TeaModel):
    def __init__(self, mount_point_alias=None, request_id=None):
        self.mount_point_alias = mount_point_alias  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindVscMountPointAliasResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point_alias is not None:
            result['MountPointAlias'] = self.mount_point_alias
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPointAlias') is not None:
            self.mount_point_alias = m.get('MountPointAlias')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindVscMountPointAliasResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindVscMountPointAliasResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindVscMountPointAliasResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindVscMountPointAliasResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessGroupRequest(TeaModel):
    def __init__(self, access_group_name=None, description=None, input_region_id=None, network_type=None):
        self.access_group_name = access_group_name  # type: str
        self.description = description  # type: str
        self.input_region_id = input_region_id  # type: str
        self.network_type = network_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        return self


class CreateAccessGroupResponseBody(TeaModel):
    def __init__(self, access_group_id=None, request_id=None):
        self.access_group_id = access_group_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAccessRuleRequest(TeaModel):
    def __init__(self, access_group_id=None, description=None, input_region_id=None, network_segment=None,
                 priority=None, rwaccess_type=None):
        self.access_group_id = access_group_id  # type: str
        self.description = description  # type: str
        self.input_region_id = input_region_id  # type: str
        self.network_segment = network_segment  # type: str
        self.priority = priority  # type: int
        self.rwaccess_type = rwaccess_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        return self


class CreateAccessRuleResponseBody(TeaModel):
    def __init__(self, access_rule_id=None, request_id=None):
        self.access_rule_id = access_rule_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateAccessRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateAccessRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateAccessRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileSystemRequest(TeaModel):
    def __init__(self, data_redundancy_type=None, description=None, file_system_name=None, input_region_id=None,
                 partition_number=None, protocol_type=None, provisioned_throughput_in_mi_bps=None, space_capacity=None,
                 storage_set_name=None, storage_type=None, throughput_mode=None, zone_id=None):
        self.data_redundancy_type = data_redundancy_type  # type: str
        self.description = description  # type: str
        self.file_system_name = file_system_name  # type: str
        self.input_region_id = input_region_id  # type: str
        self.partition_number = partition_number  # type: int
        self.protocol_type = protocol_type  # type: str
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps  # type: long
        self.space_capacity = space_capacity  # type: long
        self.storage_set_name = storage_set_name  # type: str
        self.storage_type = storage_type  # type: str
        self.throughput_mode = throughput_mode  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_redundancy_type is not None:
            result['DataRedundancyType'] = self.data_redundancy_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.partition_number is not None:
            result['PartitionNumber'] = self.partition_number
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.storage_set_name is not None:
            result['StorageSetName'] = self.storage_set_name
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DataRedundancyType') is not None:
            self.data_redundancy_type = m.get('DataRedundancyType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('PartitionNumber') is not None:
            self.partition_number = m.get('PartitionNumber')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('StorageSetName') is not None:
            self.storage_set_name = m.get('StorageSetName')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateFileSystemResponseBody(TeaModel):
    def __init__(self, file_system_id=None, request_id=None):
        self.file_system_id = file_system_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateFileSystemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateFileSystemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMountPointRequest(TeaModel):
    def __init__(self, access_group_id=None, description=None, file_system_id=None, input_region_id=None,
                 network_type=None, v_switch_id=None, vpc_id=None):
        self.access_group_id = access_group_id  # type: str
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.network_type = network_type  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateMountPointResponseBody(TeaModel):
    def __init__(self, mount_point_id=None, request_id=None):
        self.mount_point_id = mount_point_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateMountPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupsMappingRequest(TeaModel):
    def __init__(self, file_system_id=None, group_names=None, input_region_id=None, user_name=None):
        self.file_system_id = file_system_id  # type: str
        self.group_names = group_names  # type: list[str]
        self.input_region_id = input_region_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupsMappingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserGroupsMappingShrinkRequest(TeaModel):
    def __init__(self, file_system_id=None, group_names_shrink=None, input_region_id=None, user_name=None):
        self.file_system_id = file_system_id  # type: str
        self.group_names_shrink = group_names_shrink  # type: str
        self.input_region_id = input_region_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupsMappingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names_shrink is not None:
            result['GroupNames'] = self.group_names_shrink
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names_shrink = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserGroupsMappingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupsMappingResponseBody, self).to_map()
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


class CreateUserGroupsMappingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserGroupsMappingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserGroupsMappingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateUserGroupsMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVscMountPointRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, input_region_id=None, instance_ids=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_ids = instance_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVscMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        return self


class CreateVscMountPointShrinkRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, input_region_id=None, instance_ids_shrink=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_ids_shrink = instance_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVscMountPointShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        return self


class CreateVscMountPointResponseBody(TeaModel):
    def __init__(self, mount_point_id=None, request_id=None):
        self.mount_point_id = mount_point_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVscMountPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateVscMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVscMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVscMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVscMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessGroupRequest(TeaModel):
    def __init__(self, access_group_id=None, input_region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DeleteAccessGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessGroupResponseBody, self).to_map()
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


class DeleteAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAccessRuleRequest(TeaModel):
    def __init__(self, access_group_id=None, access_rule_id=None, input_region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.access_rule_id = access_rule_id  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DeleteAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteAccessRuleResponseBody, self).to_map()
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


class DeleteAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteAccessRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteAccessRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileSystemRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DeleteFileSystemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteFileSystemResponseBody, self).to_map()
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


class DeleteFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteFileSystemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMountPointRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None, mount_point_id=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.mount_point_id = mount_point_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class DeleteMountPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteMountPointResponseBody, self).to_map()
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


class DeleteMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupsMappingRequest(TeaModel):
    def __init__(self, file_system_id=None, group_names=None, input_region_id=None, user_name=None):
        self.file_system_id = file_system_id  # type: str
        self.group_names = group_names  # type: dict[str, any]
        self.input_region_id = input_region_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupsMappingRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteUserGroupsMappingShrinkRequest(TeaModel):
    def __init__(self, file_system_id=None, group_names_shrink=None, input_region_id=None, user_name=None):
        self.file_system_id = file_system_id  # type: str
        self.group_names_shrink = group_names_shrink  # type: str
        self.input_region_id = input_region_id  # type: str
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupsMappingShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.group_names_shrink is not None:
            result['GroupNames'] = self.group_names_shrink
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('GroupNames') is not None:
            self.group_names_shrink = m.get('GroupNames')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class DeleteUserGroupsMappingResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupsMappingResponseBody, self).to_map()
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


class DeleteUserGroupsMappingResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserGroupsMappingResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserGroupsMappingResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupsMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVscMountPointRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None, mount_point_id=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.mount_point_id = mount_point_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVscMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class DeleteVscMountPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVscMountPointResponseBody, self).to_map()
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


class DeleteVscMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVscMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVscMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVscMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, input_region_id=None):
        self.accept_language = accept_language  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsRegion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, region=None):
        self.region = region  # type: list[DescribeRegionsResponseBodyRegionsRegion]

    def validate(self):
        if self.region:
            for k in self.region:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Region'] = []
        if self.region is not None:
            for k in self.region:
                result['Region'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k in m.get('Region'):
                temp_model = DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m['Regions'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVscMountPointsRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None, instance_id=None, mount_point_id=None,
                 status=None, vsc_id=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_id = instance_id  # type: str
        self.mount_point_id = mount_point_id  # type: str
        self.status = status  # type: str
        self.vsc_id = vsc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVscMountPointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        return self


class DescribeVscMountPointsResponseBodyMountPointsInstancesVscs(TeaModel):
    def __init__(self, vsc_id=None, vsc_status=None, vsc_type=None):
        self.vsc_id = vsc_id  # type: str
        self.vsc_status = vsc_status  # type: str
        self.vsc_type = vsc_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVscMountPointsResponseBodyMountPointsInstancesVscs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        if self.vsc_status is not None:
            result['VscStatus'] = self.vsc_status
        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        if m.get('VscStatus') is not None:
            self.vsc_status = m.get('VscStatus')
        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')
        return self


class DescribeVscMountPointsResponseBodyMountPointsInstances(TeaModel):
    def __init__(self, instance_id=None, status=None, vscs=None):
        self.instance_id = instance_id  # type: str
        self.status = status  # type: str
        self.vscs = vscs  # type: list[DescribeVscMountPointsResponseBodyMountPointsInstancesVscs]

    def validate(self):
        if self.vscs:
            for k in self.vscs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVscMountPointsResponseBodyMountPointsInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.status is not None:
            result['Status'] = self.status
        result['Vscs'] = []
        if self.vscs is not None:
            for k in self.vscs:
                result['Vscs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.vscs = []
        if m.get('Vscs') is not None:
            for k in m.get('Vscs'):
                temp_model = DescribeVscMountPointsResponseBodyMountPointsInstancesVscs()
                self.vscs.append(temp_model.from_map(k))
        return self


class DescribeVscMountPointsResponseBodyMountPoints(TeaModel):
    def __init__(self, description=None, instance_total_count=None, instances=None, mount_point_alias=None,
                 mount_point_id=None):
        self.description = description  # type: str
        self.instance_total_count = instance_total_count  # type: int
        self.instances = instances  # type: list[DescribeVscMountPointsResponseBodyMountPointsInstances]
        self.mount_point_alias = mount_point_alias  # type: str
        self.mount_point_id = mount_point_id  # type: str

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVscMountPointsResponseBodyMountPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_total_count is not None:
            result['InstanceTotalCount'] = self.instance_total_count
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.mount_point_alias is not None:
            result['MountPointAlias'] = self.mount_point_alias
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceTotalCount') is not None:
            self.instance_total_count = m.get('InstanceTotalCount')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeVscMountPointsResponseBodyMountPointsInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('MountPointAlias') is not None:
            self.mount_point_alias = m.get('MountPointAlias')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class DescribeVscMountPointsResponseBody(TeaModel):
    def __init__(self, mount_points=None, request_id=None, total_count=None):
        self.mount_points = mount_points  # type: list[DescribeVscMountPointsResponseBodyMountPoints]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVscMountPointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = DescribeVscMountPointsResponseBodyMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeVscMountPointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeVscMountPointsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVscMountPointsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeVscMountPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachVscMountPointRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, input_region_id=None, instance_ids=None,
                 mount_point_id=None, vsc_ids=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_ids = instance_ids  # type: list[str]
        self.mount_point_id = mount_point_id  # type: str
        self.vsc_ids = vsc_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachVscMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.vsc_ids is not None:
            result['VscIds'] = self.vsc_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('VscIds') is not None:
            self.vsc_ids = m.get('VscIds')
        return self


class DetachVscMountPointShrinkRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, input_region_id=None, instance_ids_shrink=None,
                 mount_point_id=None, vsc_ids_shrink=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.instance_ids_shrink = instance_ids_shrink  # type: str
        self.mount_point_id = mount_point_id  # type: str
        self.vsc_ids_shrink = vsc_ids_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachVscMountPointShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.instance_ids_shrink is not None:
            result['InstanceIds'] = self.instance_ids_shrink
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.vsc_ids_shrink is not None:
            result['VscIds'] = self.vsc_ids_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('InstanceIds') is not None:
            self.instance_ids_shrink = m.get('InstanceIds')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('VscIds') is not None:
            self.vsc_ids_shrink = m.get('VscIds')
        return self


class DetachVscMountPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachVscMountPointResponseBody, self).to_map()
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


class DetachVscMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachVscMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachVscMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachVscMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessGroupRequest(TeaModel):
    def __init__(self, access_group_id=None, input_region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetAccessGroupResponseBodyAccessGroup(TeaModel):
    def __init__(self, access_group_id=None, access_group_name=None, create_time=None, description=None,
                 is_default=None, mount_point_count=None, network_type=None, region_id=None, rule_count=None):
        self.access_group_id = access_group_id  # type: str
        self.access_group_name = access_group_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.is_default = is_default  # type: bool
        self.mount_point_count = mount_point_count  # type: int
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.rule_count = rule_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessGroupResponseBodyAccessGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class GetAccessGroupResponseBody(TeaModel):
    def __init__(self, access_group=None, request_id=None):
        self.access_group = access_group  # type: GetAccessGroupResponseBodyAccessGroup
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_group:
            self.access_group.validate()

    def to_map(self):
        _map = super(GetAccessGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            temp_model = GetAccessGroupResponseBodyAccessGroup()
            self.access_group = temp_model.from_map(m['AccessGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccessGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccessGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAccessRuleRequest(TeaModel):
    def __init__(self, access_group_id=None, access_rule_id=None, input_region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.access_rule_id = access_rule_id  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetAccessRuleResponseBodyAccessRule(TeaModel):
    def __init__(self, access_group_id=None, access_rule_id=None, create_time=None, description=None,
                 network_segment=None, priority=None, rwaccess_type=None, region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.access_rule_id = access_rule_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.network_segment = network_segment  # type: str
        self.priority = priority  # type: int
        self.rwaccess_type = rwaccess_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAccessRuleResponseBodyAccessRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetAccessRuleResponseBody(TeaModel):
    def __init__(self, access_rule=None, request_id=None):
        self.access_rule = access_rule  # type: GetAccessRuleResponseBodyAccessRule
        self.request_id = request_id  # type: str

    def validate(self):
        if self.access_rule:
            self.access_rule.validate()

    def to_map(self):
        _map = super(GetAccessRuleResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_rule is not None:
            result['AccessRule'] = self.access_rule.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessRule') is not None:
            temp_model = GetAccessRuleResponseBodyAccessRule()
            self.access_rule = temp_model.from_map(m['AccessRule'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetAccessRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAccessRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileSystemRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetFileSystemResponseBodyFileSystem(TeaModel):
    def __init__(self, create_time=None, description=None, file_system_id=None, file_system_name=None,
                 metering_space_size=None, mount_point_count=None, number_of_directories=None, number_of_files=None,
                 protocol_type=None, provisioned_throughput_in_mi_bps=None, region_id=None, space_capacity=None,
                 storage_package_id=None, storage_type=None, throughput_mode=None, used_space_size=None, version=None, zone_id=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.file_system_name = file_system_name  # type: str
        self.metering_space_size = metering_space_size  # type: float
        self.mount_point_count = mount_point_count  # type: long
        self.number_of_directories = number_of_directories  # type: long
        self.number_of_files = number_of_files  # type: long
        self.protocol_type = protocol_type  # type: str
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps  # type: long
        self.region_id = region_id  # type: str
        self.space_capacity = space_capacity  # type: long
        self.storage_package_id = storage_package_id  # type: str
        self.storage_type = storage_type  # type: str
        self.throughput_mode = throughput_mode  # type: str
        self.used_space_size = used_space_size  # type: float
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetFileSystemResponseBodyFileSystem, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.metering_space_size is not None:
            result['MeteringSpaceSize'] = self.metering_space_size
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.number_of_directories is not None:
            result['NumberOfDirectories'] = self.number_of_directories
        if self.number_of_files is not None:
            result['NumberOfFiles'] = self.number_of_files
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.storage_package_id is not None:
            result['StoragePackageId'] = self.storage_package_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        if self.used_space_size is not None:
            result['UsedSpaceSize'] = self.used_space_size
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MeteringSpaceSize') is not None:
            self.metering_space_size = m.get('MeteringSpaceSize')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NumberOfDirectories') is not None:
            self.number_of_directories = m.get('NumberOfDirectories')
        if m.get('NumberOfFiles') is not None:
            self.number_of_files = m.get('NumberOfFiles')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('StoragePackageId') is not None:
            self.storage_package_id = m.get('StoragePackageId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        if m.get('UsedSpaceSize') is not None:
            self.used_space_size = m.get('UsedSpaceSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetFileSystemResponseBody(TeaModel):
    def __init__(self, file_system=None, request_id=None):
        self.file_system = file_system  # type: GetFileSystemResponseBodyFileSystem
        self.request_id = request_id  # type: str

    def validate(self):
        if self.file_system:
            self.file_system.validate()

    def to_map(self):
        _map = super(GetFileSystemResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system is not None:
            result['FileSystem'] = self.file_system.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystem') is not None:
            temp_model = GetFileSystemResponseBodyFileSystem()
            self.file_system = temp_model.from_map(m['FileSystem'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetFileSystemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMountPointRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None, mount_point_id=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.mount_point_id = mount_point_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        return self


class GetMountPointResponseBodyMountPoint(TeaModel):
    def __init__(self, access_group_id=None, create_time=None, description=None, file_system_id=None,
                 mount_point_domain=None, mount_point_id=None, network_type=None, region_id=None, status=None, v_switch_id=None,
                 vpc_id=None):
        self.access_group_id = access_group_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.mount_point_domain = mount_point_domain  # type: str
        self.mount_point_id = mount_point_id  # type: str
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetMountPointResponseBodyMountPoint, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_point_domain is not None:
            result['MountPointDomain'] = self.mount_point_domain
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountPointDomain') is not None:
            self.mount_point_domain = m.get('MountPointDomain')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetMountPointResponseBody(TeaModel):
    def __init__(self, mount_point=None, request_id=None):
        self.mount_point = mount_point  # type: GetMountPointResponseBodyMountPoint
        self.request_id = request_id  # type: str

    def validate(self):
        if self.mount_point:
            self.mount_point.validate()

    def to_map(self):
        _map = super(GetMountPointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mount_point is not None:
            result['MountPoint'] = self.mount_point.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MountPoint') is not None:
            temp_model = GetMountPointResponseBodyMountPoint()
            self.mount_point = temp_model.from_map(m['MountPoint'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegionRequest(TeaModel):
    def __init__(self, input_region_id=None):
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class GetRegionResponseBodyAvailableZonesOptions(TeaModel):
    def __init__(self, protocol_type=None, storage_type=None):
        self.protocol_type = protocol_type  # type: str
        self.storage_type = storage_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegionResponseBodyAvailableZonesOptions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        return self


class GetRegionResponseBodyAvailableZones(TeaModel):
    def __init__(self, options=None, zone_id=None):
        self.options = options  # type: list[GetRegionResponseBodyAvailableZonesOptions]
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.options:
            for k in self.options:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRegionResponseBodyAvailableZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Options'] = []
        if self.options is not None:
            for k in self.options:
                result['Options'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.options = []
        if m.get('Options') is not None:
            for k in m.get('Options'):
                temp_model = GetRegionResponseBodyAvailableZonesOptions()
                self.options.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetRegionResponseBody(TeaModel):
    def __init__(self, available_zones=None, request_id=None):
        self.available_zones = available_zones  # type: list[GetRegionResponseBodyAvailableZones]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.available_zones:
            for k in self.available_zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRegionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k in self.available_zones:
                result['AvailableZones'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k in m.get('AvailableZones'):
                temp_model = GetRegionResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetRegionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessGroupsRequest(TeaModel):
    def __init__(self, input_region_id=None, limit=None, order_by=None, order_type=None, start_offset=None):
        self.input_region_id = input_region_id  # type: str
        self.limit = limit  # type: int
        self.order_by = order_by  # type: str
        self.order_type = order_type  # type: str
        self.start_offset = start_offset  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListAccessGroupsResponseBodyAccessGroups(TeaModel):
    def __init__(self, access_group_id=None, access_group_name=None, create_time=None, description=None,
                 is_default=None, mount_point_count=None, network_type=None, region_id=None, rule_count=None):
        self.access_group_id = access_group_id  # type: str
        self.access_group_name = access_group_name  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.is_default = is_default  # type: bool
        self.mount_point_count = mount_point_count  # type: int
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.rule_count = rule_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessGroupsResponseBodyAccessGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')
        return self


class ListAccessGroupsResponseBody(TeaModel):
    def __init__(self, access_groups=None, request_id=None, total_count=None):
        self.access_groups = access_groups  # type: list[ListAccessGroupsResponseBodyAccessGroups]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.access_groups:
            for k in self.access_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccessGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessGroups'] = []
        if self.access_groups is not None:
            for k in self.access_groups:
                result['AccessGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.access_groups = []
        if m.get('AccessGroups') is not None:
            for k in m.get('AccessGroups'):
                temp_model = ListAccessGroupsResponseBodyAccessGroups()
                self.access_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccessGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccessGroupsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccessGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccessGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAccessRulesRequest(TeaModel):
    def __init__(self, access_group_id=None, input_region_id=None, limit=None, order_by=None, order_type=None,
                 start_offset=None):
        self.access_group_id = access_group_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.limit = limit  # type: int
        self.order_by = order_by  # type: str
        self.order_type = order_type  # type: str
        self.start_offset = start_offset  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessRulesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListAccessRulesResponseBodyAccessRules(TeaModel):
    def __init__(self, access_group_id=None, access_rule_id=None, create_time=None, description=None,
                 network_segment=None, priority=None, rwaccess_type=None, region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.access_rule_id = access_rule_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.network_segment = network_segment  # type: str
        self.priority = priority  # type: int
        self.rwaccess_type = rwaccess_type  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListAccessRulesResponseBodyAccessRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.network_segment is not None:
            result['NetworkSegment'] = self.network_segment
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('NetworkSegment') is not None:
            self.network_segment = m.get('NetworkSegment')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListAccessRulesResponseBody(TeaModel):
    def __init__(self, access_rules=None, request_id=None, total_count=None):
        self.access_rules = access_rules  # type: list[ListAccessRulesResponseBodyAccessRules]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.access_rules:
            for k in self.access_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListAccessRulesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AccessRules'] = []
        if self.access_rules is not None:
            for k in self.access_rules:
                result['AccessRules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.access_rules = []
        if m.get('AccessRules') is not None:
            for k in m.get('AccessRules'):
                temp_model = ListAccessRulesResponseBodyAccessRules()
                self.access_rules.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAccessRulesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListAccessRulesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListAccessRulesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAccessRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileSystemsRequest(TeaModel):
    def __init__(self, input_region_id=None, limit=None, order_by=None, order_type=None, start_offset=None):
        self.input_region_id = input_region_id  # type: str
        self.limit = limit  # type: int
        self.order_by = order_by  # type: str
        self.order_type = order_type  # type: str
        self.start_offset = start_offset  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileSystemsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListFileSystemsResponseBodyFileSystems(TeaModel):
    def __init__(self, create_time=None, description=None, file_system_id=None, file_system_name=None,
                 metering_space_size=None, mount_point_count=None, number_of_directories=None, number_of_files=None,
                 protocol_type=None, provisioned_throughput_in_mi_bps=None, region_id=None, space_capacity=None,
                 storage_package_id=None, storage_type=None, throughput_mode=None, used_space_size=None, version=None, zone_id=None):
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.file_system_name = file_system_name  # type: str
        self.metering_space_size = metering_space_size  # type: float
        self.mount_point_count = mount_point_count  # type: long
        self.number_of_directories = number_of_directories  # type: long
        self.number_of_files = number_of_files  # type: long
        self.protocol_type = protocol_type  # type: str
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps  # type: long
        self.region_id = region_id  # type: str
        self.space_capacity = space_capacity  # type: long
        self.storage_package_id = storage_package_id  # type: str
        self.storage_type = storage_type  # type: str
        self.throughput_mode = throughput_mode  # type: str
        self.used_space_size = used_space_size  # type: float
        self.version = version  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListFileSystemsResponseBodyFileSystems, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.metering_space_size is not None:
            result['MeteringSpaceSize'] = self.metering_space_size
        if self.mount_point_count is not None:
            result['MountPointCount'] = self.mount_point_count
        if self.number_of_directories is not None:
            result['NumberOfDirectories'] = self.number_of_directories
        if self.number_of_files is not None:
            result['NumberOfFiles'] = self.number_of_files
        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.storage_package_id is not None:
            result['StoragePackageId'] = self.storage_package_id
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        if self.used_space_size is not None:
            result['UsedSpaceSize'] = self.used_space_size
        if self.version is not None:
            result['Version'] = self.version
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('MeteringSpaceSize') is not None:
            self.metering_space_size = m.get('MeteringSpaceSize')
        if m.get('MountPointCount') is not None:
            self.mount_point_count = m.get('MountPointCount')
        if m.get('NumberOfDirectories') is not None:
            self.number_of_directories = m.get('NumberOfDirectories')
        if m.get('NumberOfFiles') is not None:
            self.number_of_files = m.get('NumberOfFiles')
        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('StoragePackageId') is not None:
            self.storage_package_id = m.get('StoragePackageId')
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        if m.get('UsedSpaceSize') is not None:
            self.used_space_size = m.get('UsedSpaceSize')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListFileSystemsResponseBody(TeaModel):
    def __init__(self, file_systems=None, request_id=None, total_count=None):
        self.file_systems = file_systems  # type: list[ListFileSystemsResponseBodyFileSystems]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.file_systems:
            for k in self.file_systems:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListFileSystemsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['FileSystems'] = []
        if self.file_systems is not None:
            for k in self.file_systems:
                result['FileSystems'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.file_systems = []
        if m.get('FileSystems') is not None:
            for k in m.get('FileSystems'):
                temp_model = ListFileSystemsResponseBodyFileSystems()
                self.file_systems.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFileSystemsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListFileSystemsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListFileSystemsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFileSystemsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMountPointsRequest(TeaModel):
    def __init__(self, file_system_id=None, input_region_id=None, limit=None, order_by=None, order_type=None,
                 start_offset=None):
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.limit = limit  # type: int
        self.order_by = order_by  # type: str
        self.order_type = order_type  # type: str
        self.start_offset = start_offset  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMountPointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.order_by is not None:
            result['OrderBy'] = self.order_by
        if self.order_type is not None:
            result['OrderType'] = self.order_type
        if self.start_offset is not None:
            result['StartOffset'] = self.start_offset
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')
        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')
        if m.get('StartOffset') is not None:
            self.start_offset = m.get('StartOffset')
        return self


class ListMountPointsResponseBodyMountPoints(TeaModel):
    def __init__(self, access_group_id=None, create_time=None, description=None, file_system_id=None,
                 mount_point_domain=None, mount_point_id=None, network_type=None, region_id=None, status=None, v_switch_id=None,
                 vpc_id=None):
        self.access_group_id = access_group_id  # type: str
        self.create_time = create_time  # type: str
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.mount_point_domain = mount_point_domain  # type: str
        self.mount_point_id = mount_point_id  # type: str
        self.network_type = network_type  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListMountPointsResponseBodyMountPoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.mount_point_domain is not None:
            result['MountPointDomain'] = self.mount_point_domain
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('MountPointDomain') is not None:
            self.mount_point_domain = m.get('MountPointDomain')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListMountPointsResponseBody(TeaModel):
    def __init__(self, mount_points=None, request_id=None, total_count=None):
        self.mount_points = mount_points  # type: list[ListMountPointsResponseBodyMountPoints]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.mount_points:
            for k in self.mount_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListMountPointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MountPoints'] = []
        if self.mount_points is not None:
            for k in self.mount_points:
                result['MountPoints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.mount_points = []
        if m.get('MountPoints') is not None:
            for k in m.get('MountPoints'):
                temp_model = ListMountPointsResponseBodyMountPoints()
                self.mount_points.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMountPointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListMountPointsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListMountPointsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMountPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsMappingsRequest(TeaModel):
    def __init__(self, filesystem_id=None, input_region_id=None, limit=None, next_token=None):
        self.filesystem_id = filesystem_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.limit = limit  # type: int
        self.next_token = next_token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsMappingsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filesystem_id is not None:
            result['FilesystemId'] = self.filesystem_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilesystemId') is not None:
            self.filesystem_id = m.get('FilesystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListUserGroupsMappingsResponseBodyUserGroupsMappings(TeaModel):
    def __init__(self, group_names=None, user_name=None):
        self.group_names = group_names  # type: list[str]
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsMappingsResponseBodyUserGroupsMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_names is not None:
            result['GroupNames'] = self.group_names
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupNames') is not None:
            self.group_names = m.get('GroupNames')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class ListUserGroupsMappingsResponseBody(TeaModel):
    def __init__(self, has_more=None, next_token=None, request_id=None, user_groups_mappings=None):
        self.has_more = has_more  # type: bool
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.user_groups_mappings = user_groups_mappings  # type: list[ListUserGroupsMappingsResponseBodyUserGroupsMappings]

    def validate(self):
        if self.user_groups_mappings:
            for k in self.user_groups_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsMappingsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UserGroupsMappings'] = []
        if self.user_groups_mappings is not None:
            for k in self.user_groups_mappings:
                result['UserGroupsMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.user_groups_mappings = []
        if m.get('UserGroupsMappings') is not None:
            for k in m.get('UserGroupsMappings'):
                temp_model = ListUserGroupsMappingsResponseBodyUserGroupsMappings()
                self.user_groups_mappings.append(temp_model.from_map(k))
        return self


class ListUserGroupsMappingsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserGroupsMappingsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserGroupsMappingsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListUserGroupsMappingsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessGroupRequest(TeaModel):
    def __init__(self, access_group_id=None, access_group_name=None, description=None, input_region_id=None):
        self.access_group_id = access_group_id  # type: str
        self.access_group_name = access_group_name  # type: str
        self.description = description  # type: str
        self.input_region_id = input_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        return self


class ModifyAccessGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessGroupResponseBody, self).to_map()
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


class ModifyAccessGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccessGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccessGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccessGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyAccessRuleRequest(TeaModel):
    def __init__(self, access_group_id=None, access_rule_id=None, description=None, input_region_id=None,
                 priority=None, rwaccess_type=None):
        self.access_group_id = access_group_id  # type: str
        self.access_rule_id = access_rule_id  # type: str
        self.description = description  # type: str
        self.input_region_id = input_region_id  # type: str
        self.priority = priority  # type: int
        self.rwaccess_type = rwaccess_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessRuleRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.access_rule_id is not None:
            result['AccessRuleId'] = self.access_rule_id
        if self.description is not None:
            result['Description'] = self.description
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.rwaccess_type is not None:
            result['RWAccessType'] = self.rwaccess_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('AccessRuleId') is not None:
            self.access_rule_id = m.get('AccessRuleId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('RWAccessType') is not None:
            self.rwaccess_type = m.get('RWAccessType')
        return self


class ModifyAccessRuleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyAccessRuleResponseBody, self).to_map()
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


class ModifyAccessRuleResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyAccessRuleResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyAccessRuleResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyAccessRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyFileSystemRequest(TeaModel):
    def __init__(self, description=None, file_system_id=None, file_system_name=None, input_region_id=None,
                 provisioned_throughput_in_mi_bps=None, space_capacity=None, throughput_mode=None):
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.file_system_name = file_system_name  # type: str
        self.input_region_id = input_region_id  # type: str
        self.provisioned_throughput_in_mi_bps = provisioned_throughput_in_mi_bps  # type: long
        self.space_capacity = space_capacity  # type: long
        self.throughput_mode = throughput_mode  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFileSystemRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.file_system_name is not None:
            result['FileSystemName'] = self.file_system_name
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.provisioned_throughput_in_mi_bps is not None:
            result['ProvisionedThroughputInMiBps'] = self.provisioned_throughput_in_mi_bps
        if self.space_capacity is not None:
            result['SpaceCapacity'] = self.space_capacity
        if self.throughput_mode is not None:
            result['ThroughputMode'] = self.throughput_mode
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('FileSystemName') is not None:
            self.file_system_name = m.get('FileSystemName')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('ProvisionedThroughputInMiBps') is not None:
            self.provisioned_throughput_in_mi_bps = m.get('ProvisionedThroughputInMiBps')
        if m.get('SpaceCapacity') is not None:
            self.space_capacity = m.get('SpaceCapacity')
        if m.get('ThroughputMode') is not None:
            self.throughput_mode = m.get('ThroughputMode')
        return self


class ModifyFileSystemResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyFileSystemResponseBody, self).to_map()
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


class ModifyFileSystemResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyFileSystemResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyFileSystemResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyFileSystemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyMountPointRequest(TeaModel):
    def __init__(self, access_group_id=None, description=None, file_system_id=None, input_region_id=None,
                 mount_point_id=None, status=None):
        self.access_group_id = access_group_id  # type: str
        self.description = description  # type: str
        self.file_system_id = file_system_id  # type: str
        self.input_region_id = input_region_id  # type: str
        self.mount_point_id = mount_point_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMountPointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id
        if self.description is not None:
            result['Description'] = self.description
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id
        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id
        if self.mount_point_id is not None:
            result['MountPointId'] = self.mount_point_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')
        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')
        if m.get('MountPointId') is not None:
            self.mount_point_id = m.get('MountPointId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ModifyMountPointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyMountPointResponseBody, self).to_map()
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


class ModifyMountPointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyMountPointResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyMountPointResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyMountPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


