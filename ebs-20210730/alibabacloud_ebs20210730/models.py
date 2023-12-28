# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None, replica_pair_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group.
        self.replica_group_id = replica_group_id  # type: str
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query the IDs of existing replication pairs.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class AddDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddDiskReplicaPairResponseBody, self).to_map()
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


class AddDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyLensServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ApplyLensServiceResponseBody, self).to_map()
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


class ApplyLensServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ApplyLensServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ApplyLensServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApplyLensServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindEnterpriseSnapshotPolicyRequest(TeaModel):
    def __init__(self, client_token=None, disk_targets=None, policy_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.disk_targets = disk_targets  # type: list[str]
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindEnterpriseSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disk_targets is not None:
            result['DiskTargets'] = self.disk_targets
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DiskTargets') is not None:
            self.disk_targets = m.get('DiskTargets')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class BindEnterpriseSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(BindEnterpriseSnapshotPolicyResponseBody, self).to_map()
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


class BindEnterpriseSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: BindEnterpriseSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(BindEnterpriseSnapshotPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = BindEnterpriseSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelLensServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelLensServiceResponseBody, self).to_map()
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


class CancelLensServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelLensServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelLensServiceResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelLensServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, client_token=None, new_resource_group_id=None, region_id=None, resource_id=None,
                 resource_type=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the new resource group. You can view the available resource groups in the Resource Management console. For more information, see [View basic information of a resource group](https://help.aliyun.com/document_detail/151181.htm?spm=a2c4g.11186623.0.0.15ef75c87zvMhL).
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The region ID of the resource. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource. For example, if you set ResourceType to diskreplicapair, set this parameter to the ID of a replication pair.
        self.resource_id = resource_id  # type: str
        # The type of the resource. Valid values:
        # 
        # *   dedicatedblockstoragecluster: dedicated block storage cluster.
        # *   diskreplicapair: replication pair.
        # *   diskreplicagroup: replication pair-consistent group.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
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


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearPairDrillRequest(TeaModel):
    def __init__(self, drill_id=None, pair_id=None, region_id=None):
        # The ID of the drill. You can call the [DescribePairDrills](~~2584480~~) operation to query the disaster recovery drills that were performed on replication pairs in a specific region.
        self.drill_id = drill_id  # type: str
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query the most recent list of replication pairs, including replication pair IDs.
        self.pair_id = pair_id  # type: str
        # The region ID. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearPairDrillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.pair_id is not None:
            result['PairId'] = self.pair_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('PairId') is not None:
            self.pair_id = m.get('PairId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ClearPairDrillResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearPairDrillResponseBody, self).to_map()
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


class ClearPairDrillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClearPairDrillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearPairDrillResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ClearPairDrillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearReplicaGroupDrillRequest(TeaModel):
    def __init__(self, drill_id=None, group_id=None, region_id=None):
        # The ID of the drill. You can call the [DescribeReplicaGroupDrills](~~2584481~~) operation to query disaster recovery drills that were performed on replication pairs in a specific region.
        self.drill_id = drill_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the most recent list of replication pair-consistent groups, including group IDs.
        self.group_id = group_id  # type: str
        # The region ID. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearReplicaGroupDrillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ClearReplicaGroupDrillResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ClearReplicaGroupDrillResponseBody, self).to_map()
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


class ClearReplicaGroupDrillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ClearReplicaGroupDrillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ClearReplicaGroupDrillResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ClearReplicaGroupDrillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDedicatedBlockStorageClusterRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedBlockStorageClusterRequestTag, self).to_map()
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


class CreateDedicatedBlockStorageClusterRequest(TeaModel):
    def __init__(self, azone=None, capacity=None, dbsc_id=None, dbsc_name=None, period=None, period_unit=None,
                 region_id=None, resource_group_id=None, tag=None, type=None):
        # The ID of the zone in which to create the dedicated block storage cluster. You can call the [DescribeZones](~~25610~~) operation to query the most recent zone list.
        self.azone = azone  # type: str
        # The capacity of the dedicated block storage cluster. Valid values: 61440 to 2334720. Unit: GiB. 2,334,720 GiB is equal to 2,280 TiB. The capacity increases in a minimum increment of 12,288 GB.
        # 
        # >  If the capacity of a dedicated block storage cluster is less than 576 TiB, the maximum throughput supported per TiB does not exceed 52 MB/s. If the capacity of a dedicated block storage cluster is greater than 576 TiB, the maximum throughput supported per TiB does not exceed 26 MB/s.
        self.capacity = capacity  # type: long
        self.dbsc_id = dbsc_id  # type: str
        # The name of the dedicated block storage cluster.
        self.dbsc_name = dbsc_name  # type: str
        self.period = period  # type: int
        self.period_unit = period_unit  # type: str
        # The ID of the region in which to create the dedicated block storage cluster. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[CreateDedicatedBlockStorageClusterRequestTag]
        # The type of the dedicated block storage cluster. Valid values:
        # 
        # *   Standard: basic type. When you set Type to Standard, enhanced SSDs (ESSDs) at performance level 0 (PL0 ESSDs) can be created in the dedicated block storage cluster.
        # *   Premium: performance type. When you set Type to Premium, ESSDs at performance level 1 (PL1 ESSDs) can be created in the dedicated block storage cluster.
        # 
        # Default value: Premium.
        # 
        # For more information about ESSDs, see [ESSDs](~~122389~~).
        self.type = type  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDedicatedBlockStorageClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.azone is not None:
            result['Azone'] = self.azone
        if self.capacity is not None:
            result['Capacity'] = self.capacity
        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id
        if self.dbsc_name is not None:
            result['DbscName'] = self.dbsc_name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Azone') is not None:
            self.azone = m.get('Azone')
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')
        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')
        if m.get('DbscName') is not None:
            self.dbsc_name = m.get('DbscName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDedicatedBlockStorageClusterRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDedicatedBlockStorageClusterResponseBody(TeaModel):
    def __init__(self, dbsc_id=None, order_id=None, request_id=None):
        # The ID of the dedicated block storage cluster.
        self.dbsc_id = dbsc_id  # type: str
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDedicatedBlockStorageClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDedicatedBlockStorageClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDedicatedBlockStorageClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDedicatedBlockStorageClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDedicatedBlockStorageClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiskReplicaGroupRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N of the replication pair-consistent group.
        self.key = key  # type: str
        # The value of tag N of the replication pair-consistent group.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDiskReplicaGroupRequestTag, self).to_map()
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


class CreateDiskReplicaGroupRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, destination_region_id=None,
                 destination_zone_id=None, group_name=None, rpo=None, region_id=None, resource_group_id=None, source_zone_id=None,
                 tag=None):
        # The bandwidth value. Unit: Mbit/s.
        # 
        # >  This parameter is not publicly available.
        self.bandwidth = bandwidth  # type: long
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The description of the replication pair-consistent group. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The region ID of the secondary site.
        self.destination_region_id = destination_region_id  # type: str
        # The zone ID of the secondary site.
        self.destination_zone_id = destination_zone_id  # type: str
        # The name of the replication pair-consistent group. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.group_name = group_name  # type: str
        # The RPO of the replication pair-consistent group. Unit: seconds. Valid value: 900.
        self.rpo = rpo  # type: long
        # The ID of the region in which to create the replication pair-consistent group. The primary site is deployed in the specified region.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the replication pair-consistent group belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The zone ID of the primary site.
        self.source_zone_id = source_zone_id  # type: str
        # The tags. Up to 20 tags are supported.
        self.tag = tag  # type: list[CreateDiskReplicaGroupRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.rpo is not None:
            result['RPO'] = self.rpo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDiskReplicaGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, replica_group_id=None, request_id=None):
        # The ID of the replication pair-consistent group.
        self.replica_group_id = replica_group_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDiskReplicaGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiskReplicaPairRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the resource. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The value of tag N to add to the resource. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:` or contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDiskReplicaPairRequestTag, self).to_map()
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


class CreateDiskReplicaPairRequest(TeaModel):
    def __init__(self, bandwidth=None, charge_type=None, client_token=None, description=None,
                 destination_disk_id=None, destination_region_id=None, destination_zone_id=None, disk_id=None, pair_name=None,
                 period=None, period_unit=None, rpo=None, region_id=None, resource_group_id=None, source_zone_id=None,
                 tag=None):
        # The bandwidth to use to asynchronously replicate data between the primary disk and secondary disk. Unit: Kbit/s. Valid values:
        # 
        # *   10240 : equal to 10 Mbit/s
        # *   20480 : equal to 20 Mbit/s
        # *   51200 : equal to 50 Mbit/s
        # *   102400 : equal to 100 Mbit/s
        # 
        # Default value: 10240.
        # 
        # When you set the ChargeType parameter to POSTPAY, the Bandwidth parameter is automatically set to 0 and cannot be modified. The value 0 indicates that bandwidth is dynamically allocated based on the volume of data that is asynchronously replicated from the primary disk to the secondary disk.
        self.bandwidth = bandwidth  # type: long
        # The billing method of the replication pair. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        # 
        # Default value: POSTPAY.
        self.charge_type = charge_type  # type: str
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The description of the replication pair. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The ID of the secondary disk.
        self.destination_disk_id = destination_disk_id  # type: str
        # The region ID of the secondary disk. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.destination_region_id = destination_region_id  # type: str
        # The zone ID of the secondary disk.
        self.destination_zone_id = destination_zone_id  # type: str
        # The ID of the primary disk.
        self.disk_id = disk_id  # type: str
        # The name of the replication pair. The name must be 2 to 128 characters in length. It must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (\_), periods (.), and hyphens (-).
        self.pair_name = pair_name  # type: str
        # The subscription duration of the replication pair. This parameter is required when the `ChargeType` parameter is set to PREPAY. The unit of the subscription duration is specified by the `PeriodUnit` parameter.
        # 
        # *   Valid values when the `PeriodUnit` parameter is set to Week: 1, 2, 3, and 4.
        # *   Valid values when the `PeriodUnit` parameter is set to Month: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period  # type: long
        # The unit of the subscription duration of the replication pair. Valid values:
        # 
        # *   Week.
        # *   Month
        # 
        # Default value: Month.
        self.period_unit = period_unit  # type: str
        # The recovery point objective (RPO) of the replication pair. Unit: seconds. Set the value to 900.
        self.rpo = rpo  # type: long
        # The ID of the region in which to create the replication pair.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which to assign the replication group.
        self.resource_group_id = resource_group_id  # type: str
        # The zone ID of the primary disk.
        self.source_zone_id = source_zone_id  # type: str
        # The resource tags. You can specify up to 20 tags.
        self.tag = tag  # type: list[CreateDiskReplicaPairRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_disk_id is not None:
            result['DestinationDiskId'] = self.destination_disk_id
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.pair_name is not None:
            result['PairName'] = self.pair_name
        if self.period is not None:
            result['Period'] = self.period
        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit
        if self.rpo is not None:
            result['RPO'] = self.rpo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationDiskId') is not None:
            self.destination_disk_id = m.get('DestinationDiskId')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')
        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateDiskReplicaPairRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, order_id=None, replica_pair_id=None, request_id=None):
        # The ID of the order.
        self.order_id = order_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateDiskReplicaPairResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions(TeaModel):
    def __init__(self, region_id=None, retain_days=None):
        self.region_id = region_id  # type: str
        self.retain_days = retain_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_days is not None:
            result['RetainDays'] = self.retain_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainDays') is not None:
            self.retain_days = m.get('RetainDays')
        return self


class CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo(TeaModel):
    def __init__(self, enabled=None, regions=None):
        self.enabled = enabled  # type: bool
        self.regions = regions  # type: list[CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class CreateEnterpriseSnapshotPolicyRequestRetainRule(TeaModel):
    def __init__(self, number=None, time_interval=None, time_unit=None):
        self.number = number  # type: int
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestRetainRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class CreateEnterpriseSnapshotPolicyRequestSchedule(TeaModel):
    def __init__(self, cron_expression=None):
        self.cron_expression = cron_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestSchedule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        return self


class CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules(TeaModel):
    def __init__(self, special_period_unit=None, time_interval=None, time_unit=None):
        self.special_period_unit = special_period_unit  # type: str
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_period_unit is not None:
            result['SpecialPeriodUnit'] = self.special_period_unit
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecialPeriodUnit') is not None:
            self.special_period_unit = m.get('SpecialPeriodUnit')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules(TeaModel):
    def __init__(self, enabled=None, rules=None):
        self.enabled = enabled  # type: bool
        self.rules = rules  # type: list[CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = CreateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules()
                self.rules.append(temp_model.from_map(k))
        return self


class CreateEnterpriseSnapshotPolicyRequestStorageRule(TeaModel):
    def __init__(self, enable_immediate_access=None):
        self.enable_immediate_access = enable_immediate_access  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestStorageRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_immediate_access is not None:
            result['EnableImmediateAccess'] = self.enable_immediate_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableImmediateAccess') is not None:
            self.enable_immediate_access = m.get('EnableImmediateAccess')
        return self


class CreateEnterpriseSnapshotPolicyRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequestTag, self).to_map()
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


class CreateEnterpriseSnapshotPolicyRequest(TeaModel):
    def __init__(self, client_token=None, cross_region_copy_info=None, desc=None, name=None, region_id=None,
                 resource_group_id=None, retain_rule=None, schedule=None, special_retain_rules=None, state=None, storage_rule=None,
                 tag=None, target_type=None):
        self.client_token = client_token  # type: str
        self.cross_region_copy_info = cross_region_copy_info  # type: CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.retain_rule = retain_rule  # type: CreateEnterpriseSnapshotPolicyRequestRetainRule
        self.schedule = schedule  # type: CreateEnterpriseSnapshotPolicyRequestSchedule
        self.special_retain_rules = special_retain_rules  # type: CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules
        self.state = state  # type: str
        self.storage_rule = storage_rule  # type: CreateEnterpriseSnapshotPolicyRequestStorageRule
        self.tag = tag  # type: list[CreateEnterpriseSnapshotPolicyRequestTag]
        self.target_type = target_type  # type: str

    def validate(self):
        if self.cross_region_copy_info:
            self.cross_region_copy_info.validate()
        if self.retain_rule:
            self.retain_rule.validate()
        if self.schedule:
            self.schedule.validate()
        if self.special_retain_rules:
            self.special_retain_rules.validate()
        if self.storage_rule:
            self.storage_rule.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cross_region_copy_info is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info.to_map()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retain_rule is not None:
            result['RetainRule'] = self.retain_rule.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        if self.special_retain_rules is not None:
            result['SpecialRetainRules'] = self.special_retain_rules.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.storage_rule is not None:
            result['StorageRule'] = self.storage_rule.to_map()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CrossRegionCopyInfo') is not None:
            temp_model = CreateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo()
            self.cross_region_copy_info = temp_model.from_map(m['CrossRegionCopyInfo'])
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetainRule') is not None:
            temp_model = CreateEnterpriseSnapshotPolicyRequestRetainRule()
            self.retain_rule = temp_model.from_map(m['RetainRule'])
        if m.get('Schedule') is not None:
            temp_model = CreateEnterpriseSnapshotPolicyRequestSchedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        if m.get('SpecialRetainRules') is not None:
            temp_model = CreateEnterpriseSnapshotPolicyRequestSpecialRetainRules()
            self.special_retain_rules = temp_model.from_map(m['SpecialRetainRules'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StorageRule') is not None:
            temp_model = CreateEnterpriseSnapshotPolicyRequestStorageRule()
            self.storage_rule = temp_model.from_map(m['StorageRule'])
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateEnterpriseSnapshotPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateEnterpriseSnapshotPolicyShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyShrinkRequestTag, self).to_map()
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


class CreateEnterpriseSnapshotPolicyShrinkRequest(TeaModel):
    def __init__(self, client_token=None, cross_region_copy_info_shrink=None, desc=None, name=None, region_id=None,
                 resource_group_id=None, retain_rule_shrink=None, schedule_shrink=None, special_retain_rules_shrink=None, state=None,
                 storage_rule_shrink=None, tag=None, target_type=None):
        self.client_token = client_token  # type: str
        self.cross_region_copy_info_shrink = cross_region_copy_info_shrink  # type: str
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.retain_rule_shrink = retain_rule_shrink  # type: str
        self.schedule_shrink = schedule_shrink  # type: str
        self.special_retain_rules_shrink = special_retain_rules_shrink  # type: str
        self.state = state  # type: str
        self.storage_rule_shrink = storage_rule_shrink  # type: str
        self.tag = tag  # type: list[CreateEnterpriseSnapshotPolicyShrinkRequestTag]
        self.target_type = target_type  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cross_region_copy_info_shrink is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info_shrink
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retain_rule_shrink is not None:
            result['RetainRule'] = self.retain_rule_shrink
        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink
        if self.special_retain_rules_shrink is not None:
            result['SpecialRetainRules'] = self.special_retain_rules_shrink
        if self.state is not None:
            result['State'] = self.state
        if self.storage_rule_shrink is not None:
            result['StorageRule'] = self.storage_rule_shrink
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CrossRegionCopyInfo') is not None:
            self.cross_region_copy_info_shrink = m.get('CrossRegionCopyInfo')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetainRule') is not None:
            self.retain_rule_shrink = m.get('RetainRule')
        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')
        if m.get('SpecialRetainRules') is not None:
            self.special_retain_rules_shrink = m.get('SpecialRetainRules')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StorageRule') is not None:
            self.storage_rule_shrink = m.get('StorageRule')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateEnterpriseSnapshotPolicyShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateEnterpriseSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, policy_id=None, request_id=None):
        # snapshot policy instance id
        self.policy_id = policy_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateEnterpriseSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateEnterpriseSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateEnterpriseSnapshotPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEnterpriseSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.replica_group_id = replica_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        return self


class DeleteDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDiskReplicaGroupResponseBody, self).to_map()
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


class DeleteDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_pair_id=None):
        # The client token that is used to ensure the idempotency of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the primary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query the region information of replication pairs.
        self.region_id = region_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class DeleteDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteDiskReplicaPairResponseBody, self).to_map()
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


class DeleteDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEnterpriseSnapshotPolicyRequest(TeaModel):
    def __init__(self, client_token=None, policy_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteEnterpriseSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteEnterpriseSnapshotPolicyResponseBody, self).to_map()
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


class DeleteEnterpriseSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteEnterpriseSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteEnterpriseSnapshotPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteEnterpriseSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedBlockStorageClusterDisksRequest(TeaModel):
    def __init__(self, dbsc_id=None, max_results=None, next_token=None, region_id=None):
        # The ID of the dedicated block storage cluster.
        self.dbsc_id = dbsc_id  # type: str
        # The maximum number of entries to return on each page. Maximum value: 500.
        # 
        # Default value: 10.
        self.max_results = max_results  # type: long
        # The query token. Set the value to the NextToken value returned in the previous call to the DescribeDedicatedBlockStorageClusterDisks operation. Leave this parameter empty the first time you call this operation.
        self.next_token = next_token  # type: str
        # The ID of the region where the dedicated block storage cluster resides. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClusterDisksRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key of the cloud disk.
        self.tag_key = tag_key  # type: str
        # The tag value of the cloud disk.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk(TeaModel):
    def __init__(self, attached_time=None, bdf_id=None, bursting_enabled=None, category=None,
                 delete_auto_snapshot=None, delete_with_instance=None, description=None, detached_time=None, device=None,
                 disk_charge_type=None, disk_id=None, disk_name=None, enable_auto_snapshot=None, encrypted=None, iops=None,
                 image_id=None, instance_id=None, kmskey_id=None, mount_instance_num=None, multi_attach=None,
                 performance_level=None, portable=None, provisioned_iops=None, region_id=None, size=None, source_snapshot_id=None,
                 status=None, storage_cluster_id=None, storage_set_id=None, storage_set_partition_number=None, tags=None,
                 throughput=None, type=None, zone_id=None):
        # The time when the cloud disk was last attached. The time follows the ISO 8601 standard in the yyyy-MM-ddThh:mmZ format. The time is displayed in UTC.
        self.attached_time = attached_time  # type: str
        # This parameter is currently in invitational preview and unavailable for general users.
        self.bdf_id = bdf_id  # type: str
        self.bursting_enabled = bursting_enabled  # type: bool
        # The category of the disk. A value of cloud_essd indicates that the disk is an ESSD.
        self.category = category  # type: str
        # Indicates whether the automatic snapshots of the cloud disk are deleted when the disk is released. Valid values:
        # 
        # *   true: The automatic snapshots of the cloud disk are deleted when the disk is released.
        # *   false: The automatic snapshots of the cloud disk are retained when the disk is released.
        # 
        # Snapshots that are created by calling the [CreateSnapshot](~~25524~~) operation or by using the Elastic Compute Service (ECS) console are retained and not affected by this parameter.
        self.delete_auto_snapshot = delete_auto_snapshot  # type: bool
        # Indicates whether the cloud disk is released when its associated instance is released. Valid values:
        # 
        # *   true: The cloud disk is released when its associated instance is released.
        # *   false: The cloud disk is retained when its associated instance is released.
        self.delete_with_instance = delete_with_instance  # type: bool
        # The description of the cloud disk.
        self.description = description  # type: str
        # The time when the cloud disk was last detached.
        self.detached_time = detached_time  # type: str
        # The device name of the cloud disk on its associated instance. Example: /dev/xvdb. Take note of the following items:
        # 
        # *   This parameter has a value only when the `Status` value is `In_use`.
        # *   This parameter is empty for cloud disks that have the multi-attach feature enabled. You can query the attachment information of the cloud disk based on the `Attachment` values.
        # 
        # >  This parameter will be removed in the future. We recommend that you use other parameters to ensure future compatibility.
        self.device = device  # type: str
        # The billing method of the cloud disk. Valid values:
        # 
        # *   PrePaid: subscription
        # *   PostPaid: pay-as-you-go
        self.disk_charge_type = disk_charge_type  # type: str
        # The ID of the cloud disk.
        self.disk_id = disk_id  # type: str
        # The name of the cloud disk.
        self.disk_name = disk_name  # type: str
        # Indicates whether the automatic snapshot policy feature is enabled for the cloud disk.
        self.enable_auto_snapshot = enable_auto_snapshot  # type: bool
        # Indicates whether the cloud disk is encrypted.
        self.encrypted = encrypted  # type: bool
        # The maximum number of IOPS.
        self.iops = iops  # type: long
        # The ID of the image that was used to create the instance. This parameter is empty unless the cloud disk was created from an image. The value of this parameter remains unchanged throughout the lifecycle of the cloud disk.
        self.image_id = image_id  # type: str
        # The ID of the instance to which the cloud disk is attached. Take note of the following items:
        # 
        # *   This parameter has a value only when the `Status` value is `In_use`.
        # *   This parameter is empty for cloud disks that have the multi-attach feature enabled. You can query the attachment information of the cloud disk based on the `Attachment` values.
        self.instance_id = instance_id  # type: str
        # The ID of the Key Management Service (KMS) key used by the cloud disk.
        self.kmskey_id = kmskey_id  # type: str
        # The number of instances to which the Shared Block Storage device is attached.
        self.mount_instance_num = mount_instance_num  # type: int
        # Indicates whether the multi-attach feature was enabled for the cloud disk.
        self.multi_attach = multi_attach  # type: str
        # The performance level of the enhanced SSD (ESSD). Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        self.performance_level = performance_level  # type: str
        # Indicates whether the cloud disk is removable.
        self.portable = portable  # type: bool
        self.provisioned_iops = provisioned_iops  # type: long
        # The region ID of cloud disk.
        self.region_id = region_id  # type: str
        # The size of the disk. Unit: GiB.
        self.size = size  # type: int
        # The ID of the snapshot that was used to create the cloud disk.
        # 
        # This parameter is empty unless the cloud disk was created from a snapshot. The value of this parameter remains unchanged throughout the lifecycle of the cloud disk.
        self.source_snapshot_id = source_snapshot_id  # type: str
        # The state of the cloud disk. For more information, see [Disk states](~~25689~~). Valid values:
        # 
        # *   In_use
        # *   Available
        # *   Attaching
        # *   Detaching
        # *   Creating
        # *   ReIniting
        self.status = status  # type: str
        # The ID of the dedicated block storage cluster to which the cloud disk belongs. If your cloud disk belongs to the public block storage cluster, an empty value is returned.
        self.storage_cluster_id = storage_cluster_id  # type: str
        # The ID of the storage set.
        self.storage_set_id = storage_set_id  # type: str
        # The maximum number of partitions in the storage set.
        self.storage_set_partition_number = storage_set_partition_number  # type: int
        # The tags of the cloud disk.
        self.tags = tags  # type: list[DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags]
        self.throughput = throughput  # type: long
        # The type of the disk. Valid values:
        # 
        # *   system: system disk
        # *   data: data disk
        self.type = type  # type: str
        # The zone ID of cloud disk.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attached_time is not None:
            result['AttachedTime'] = self.attached_time
        if self.bdf_id is not None:
            result['BdfId'] = self.bdf_id
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_auto_snapshot is not None:
            result['DeleteAutoSnapshot'] = self.delete_auto_snapshot
        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance
        if self.description is not None:
            result['Description'] = self.description
        if self.detached_time is not None:
            result['DetachedTime'] = self.detached_time
        if self.device is not None:
            result['Device'] = self.device
        if self.disk_charge_type is not None:
            result['DiskChargeType'] = self.disk_charge_type
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.disk_name is not None:
            result['DiskName'] = self.disk_name
        if self.enable_auto_snapshot is not None:
            result['EnableAutoSnapshot'] = self.enable_auto_snapshot
        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted
        if self.iops is not None:
            result['IOPS'] = self.iops
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id
        if self.mount_instance_num is not None:
            result['MountInstanceNum'] = self.mount_instance_num
        if self.multi_attach is not None:
            result['MultiAttach'] = self.multi_attach
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.portable is not None:
            result['Portable'] = self.portable
        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.size is not None:
            result['Size'] = self.size
        if self.source_snapshot_id is not None:
            result['SourceSnapshotId'] = self.source_snapshot_id
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_cluster_id is not None:
            result['StorageClusterId'] = self.storage_cluster_id
        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id
        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.throughput is not None:
            result['Throughput'] = self.throughput
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachedTime') is not None:
            self.attached_time = m.get('AttachedTime')
        if m.get('BdfId') is not None:
            self.bdf_id = m.get('BdfId')
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('DeleteAutoSnapshot')
        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DetachedTime') is not None:
            self.detached_time = m.get('DetachedTime')
        if m.get('Device') is not None:
            self.device = m.get('Device')
        if m.get('DiskChargeType') is not None:
            self.disk_charge_type = m.get('DiskChargeType')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')
        if m.get('EnableAutoSnapshot') is not None:
            self.enable_auto_snapshot = m.get('EnableAutoSnapshot')
        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')
        if m.get('IOPS') is not None:
            self.iops = m.get('IOPS')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')
        if m.get('MountInstanceNum') is not None:
            self.mount_instance_num = m.get('MountInstanceNum')
        if m.get('MultiAttach') is not None:
            self.multi_attach = m.get('MultiAttach')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Portable') is not None:
            self.portable = m.get('Portable')
        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SourceSnapshotId') is not None:
            self.source_snapshot_id = m.get('SourceSnapshotId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageClusterId') is not None:
            self.storage_cluster_id = m.get('StorageClusterId')
        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')
        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Throughput') is not None:
            self.throughput = m.get('Throughput')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks(TeaModel):
    def __init__(self, disk=None):
        # Details about the cloud disks.
        self.disk = disk  # type: list[DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk]

    def validate(self):
        if self.disk:
            for k in self.disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Disk'] = []
        if self.disk is not None:
            for k in self.disk:
                result['Disk'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.disk = []
        if m.get('Disk') is not None:
            for k in m.get('Disk'):
                temp_model = DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDisk()
                self.disk.append(temp_model.from_map(k))
        return self


class DescribeDedicatedBlockStorageClusterDisksResponseBody(TeaModel):
    def __init__(self, disks=None, next_token=None, request_id=None):
        # Details about the cloud disks.
        self.disks = disks  # type: DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks
        # The query token returned in this call.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.disks:
            self.disks.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClusterDisksResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disks is not None:
            result['Disks'] = self.disks.to_map()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Disks') is not None:
            temp_model = DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks()
            self.disks = temp_model.from_map(m['Disks'])
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDedicatedBlockStorageClusterDisksResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedBlockStorageClusterDisksResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClusterDisksResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedBlockStorageClusterDisksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDedicatedBlockStorageClustersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key of the dedicated block storage cluster.
        self.key = key  # type: str
        # The tag value of the dedicated block storage cluster.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersRequestTag, self).to_map()
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


class DescribeDedicatedBlockStorageClustersRequest(TeaModel):
    def __init__(self, azone_id=None, category=None, client_token=None, dedicated_block_storage_cluster_id=None,
                 max_results=None, next_token=None, page_number=None, page_size=None, region_id=None, resource_group_id=None,
                 status=None, tag=None):
        # The zone ID of the dedicated block storage cluster. You can call the [DescribeZones](~~25610~~) operation to query the most recent zone list.
        self.azone_id = azone_id  # type: str
        # The category of disks that can be created in the dedicated block storage cluster.
        # 
        # Set the value to cloud_essd. Only enhanced SSDs (ESSDs) can be created in dedicated block storage clusters.
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.dedicated_block_storage_cluster_id = dedicated_block_storage_cluster_id  # type: list[str]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The region ID of the dedicated block storage cluster. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the dedicated block storage cluster belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The states of dedicated block storage clusters. Valid values:
        # 
        # *   Preparing
        # *   Running
        # *   Expired
        # *   Offline
        # 
        # Multiple states can be specified. Valid values of N: 1, 2, 3, and 4.
        self.status = status  # type: list[str]
        # The tags. Up to 20 tags are supported.
        self.tag = tag  # type: list[DescribeDedicatedBlockStorageClustersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.azone_id is not None:
            result['AzoneId'] = self.azone_id
        if self.category is not None:
            result['Category'] = self.category
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dedicated_block_storage_cluster_id is not None:
            result['DedicatedBlockStorageClusterId'] = self.dedicated_block_storage_cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AzoneId') is not None:
            self.azone_id = m.get('AzoneId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DedicatedBlockStorageClusterId') is not None:
            self.dedicated_block_storage_cluster_id = m.get('DedicatedBlockStorageClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDedicatedBlockStorageClustersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity(TeaModel):
    def __init__(self, available_capacity=None, available_device_capacity=None, available_space_capacity=None,
                 cluster_available_capacity=None, cluster_delivery_capacity=None, delivery_capacity=None, total_capacity=None,
                 total_device_capacity=None, total_space_capacity=None, used_capacity=None, used_device_capacity=None,
                 used_space_capacity=None):
        # The available capacity of the dedicated block storage cluster. Unit: GiB.
        self.available_capacity = available_capacity  # type: long
        # The total capacity of the dedicated block storage cluster that was delivered in disk creation orders. Unit: GB.
        self.available_device_capacity = available_device_capacity  # type: long
        # This parameter is displayed only if Thin Provision is enabled.
        self.available_space_capacity = available_space_capacity  # type: float
        # The capacity of the dedicated block storage cluster that was delivered in orders. Unit: GB.
        self.cluster_available_capacity = cluster_available_capacity  # type: long
        # The capacity of the dedicated block storage cluster that is to be delivered in orders. Unit: GB.
        self.cluster_delivery_capacity = cluster_delivery_capacity  # type: long
        # The to-be-delivered capacity of the dedicated block storage cluster. Unit: GB.
        self.delivery_capacity = delivery_capacity  # type: long
        # The total capacity of the dedicated block storage cluster. Unit: GiB.
        self.total_capacity = total_capacity  # type: long
        # The total capacity of the dedicated block storage cluster that is to be delivered in disk creation orders. Unit: GB.
        self.total_device_capacity = total_device_capacity  # type: long
        # This parameter is displayed only if Thin Provision is enabled.
        self.total_space_capacity = total_space_capacity  # type: long
        # The used capacity of the dedicated block storage cluster. Unit: GB.
        self.used_capacity = used_capacity  # type: long
        # The capacity of the dedicated block storage cluster that was used to create disks. Unit: GB.
        self.used_device_capacity = used_device_capacity  # type: long
        # This parameter is displayed only if Thin Provision is enabled.
        self.used_space_capacity = used_space_capacity  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_capacity is not None:
            result['AvailableCapacity'] = self.available_capacity
        if self.available_device_capacity is not None:
            result['AvailableDeviceCapacity'] = self.available_device_capacity
        if self.available_space_capacity is not None:
            result['AvailableSpaceCapacity'] = self.available_space_capacity
        if self.cluster_available_capacity is not None:
            result['ClusterAvailableCapacity'] = self.cluster_available_capacity
        if self.cluster_delivery_capacity is not None:
            result['ClusterDeliveryCapacity'] = self.cluster_delivery_capacity
        if self.delivery_capacity is not None:
            result['DeliveryCapacity'] = self.delivery_capacity
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.total_device_capacity is not None:
            result['TotalDeviceCapacity'] = self.total_device_capacity
        if self.total_space_capacity is not None:
            result['TotalSpaceCapacity'] = self.total_space_capacity
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        if self.used_device_capacity is not None:
            result['UsedDeviceCapacity'] = self.used_device_capacity
        if self.used_space_capacity is not None:
            result['UsedSpaceCapacity'] = self.used_space_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableCapacity') is not None:
            self.available_capacity = m.get('AvailableCapacity')
        if m.get('AvailableDeviceCapacity') is not None:
            self.available_device_capacity = m.get('AvailableDeviceCapacity')
        if m.get('AvailableSpaceCapacity') is not None:
            self.available_space_capacity = m.get('AvailableSpaceCapacity')
        if m.get('ClusterAvailableCapacity') is not None:
            self.cluster_available_capacity = m.get('ClusterAvailableCapacity')
        if m.get('ClusterDeliveryCapacity') is not None:
            self.cluster_delivery_capacity = m.get('ClusterDeliveryCapacity')
        if m.get('DeliveryCapacity') is not None:
            self.delivery_capacity = m.get('DeliveryCapacity')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('TotalDeviceCapacity') is not None:
            self.total_device_capacity = m.get('TotalDeviceCapacity')
        if m.get('TotalSpaceCapacity') is not None:
            self.total_space_capacity = m.get('TotalSpaceCapacity')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        if m.get('UsedDeviceCapacity') is not None:
            self.used_device_capacity = m.get('UsedDeviceCapacity')
        if m.get('UsedSpaceCapacity') is not None:
            self.used_space_capacity = m.get('UsedSpaceCapacity')
        return self


class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key of the dedicated block storage cluster.
        self.tag_key = tag_key  # type: str
        # The tag value of the dedicated block storage cluster.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters(TeaModel):
    def __init__(self, ali_uid=None, category=None, create_time=None,
                 dedicated_block_storage_cluster_capacity=None, dedicated_block_storage_cluster_id=None, dedicated_block_storage_cluster_name=None,
                 description=None, enable_thin_provision=None, expired_time=None, performance_level=None, region_id=None,
                 resource_group_id=None, size_over_sold_ratio=None, status=None, storage_domain=None, supported_category=None,
                 tags=None, type=None, zone_id=None):
        self.ali_uid = ali_uid  # type: str
        # The category of disks that can be created in the dedicated block storage cluster.
        self.category = category  # type: str
        # The time when the dedicated block storage cluster was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time  # type: str
        # The storage capacity of the dedicated block storage cluster.
        self.dedicated_block_storage_cluster_capacity = dedicated_block_storage_cluster_capacity  # type: DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity
        # The ID of the dedicated block storage cluster.
        self.dedicated_block_storage_cluster_id = dedicated_block_storage_cluster_id  # type: str
        # The name of the dedicated block storage cluster.
        self.dedicated_block_storage_cluster_name = dedicated_block_storage_cluster_name  # type: str
        # The description of the dedicated block storage cluster.
        self.description = description  # type: str
        self.enable_thin_provision = enable_thin_provision  # type: bool
        # The time when the dedicated block storage cluster expires. The value is a UNIX timestamp. Unit: seconds.
        self.expired_time = expired_time  # type: str
        # The performance level of disks. Valid values:
        # 
        # *   PL0
        # *   PL1
        # *   PL2
        # *   PL3
        # 
        # >  This parameter takes effect only if Category is set to cloud_essd.
        self.performance_level = performance_level  # type: str
        # The region ID of the dedicated block storage cluster.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the dedicated block storage cluster belongs.
        self.resource_group_id = resource_group_id  # type: str
        self.size_over_sold_ratio = size_over_sold_ratio  # type: float
        # The state of the dedicated block storage cluster. Valid values:
        # 
        # *   Preparing
        # *   Running
        # *   Expired
        # *   Offline
        self.status = status  # type: str
        self.storage_domain = storage_domain  # type: str
        # This parameter is not supported.
        self.supported_category = supported_category  # type: str
        # The tags of the dedicated block storage cluster.
        self.tags = tags  # type: list[DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags]
        # The type of the dedicated block storage cluster. Valid values:
        # 
        # *   Standard: basic dedicated block storage cluster. ESSDs at performance level 0 (PL0 ESSDs) can be created in basic dedicated block storage clusters.
        # *   Premium: performance dedicated block storage cluster. ESSDs at performance level 1 (PL1 ESSDs) can be created in performance dedicated block storage clusters.
        self.type = type  # type: str
        # The zone ID of the dedicated block storage cluster.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.dedicated_block_storage_cluster_capacity:
            self.dedicated_block_storage_cluster_capacity.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.dedicated_block_storage_cluster_capacity is not None:
            result['DedicatedBlockStorageClusterCapacity'] = self.dedicated_block_storage_cluster_capacity.to_map()
        if self.dedicated_block_storage_cluster_id is not None:
            result['DedicatedBlockStorageClusterId'] = self.dedicated_block_storage_cluster_id
        if self.dedicated_block_storage_cluster_name is not None:
            result['DedicatedBlockStorageClusterName'] = self.dedicated_block_storage_cluster_name
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_thin_provision is not None:
            result['EnableThinProvision'] = self.enable_thin_provision
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.size_over_sold_ratio is not None:
            result['SizeOverSoldRatio'] = self.size_over_sold_ratio
        if self.status is not None:
            result['Status'] = self.status
        if self.storage_domain is not None:
            result['StorageDomain'] = self.storage_domain
        if self.supported_category is not None:
            result['SupportedCategory'] = self.supported_category
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.type is not None:
            result['Type'] = self.type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DedicatedBlockStorageClusterCapacity') is not None:
            temp_model = DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity()
            self.dedicated_block_storage_cluster_capacity = temp_model.from_map(m['DedicatedBlockStorageClusterCapacity'])
        if m.get('DedicatedBlockStorageClusterId') is not None:
            self.dedicated_block_storage_cluster_id = m.get('DedicatedBlockStorageClusterId')
        if m.get('DedicatedBlockStorageClusterName') is not None:
            self.dedicated_block_storage_cluster_name = m.get('DedicatedBlockStorageClusterName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableThinProvision') is not None:
            self.enable_thin_provision = m.get('EnableThinProvision')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SizeOverSoldRatio') is not None:
            self.size_over_sold_ratio = m.get('SizeOverSoldRatio')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StorageDomain') is not None:
            self.storage_domain = m.get('StorageDomain')
        if m.get('SupportedCategory') is not None:
            self.supported_category = m.get('SupportedCategory')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedBlockStorageClustersResponseBody(TeaModel):
    def __init__(self, dedicated_block_storage_clusters=None, next_token=None, page_number=None, page_size=None,
                 request_id=None, total_count=None):
        # The queried dedicated block storage clusters.
        self.dedicated_block_storage_clusters = dedicated_block_storage_clusters  # type: list[DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters]
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.dedicated_block_storage_clusters:
            for k in self.dedicated_block_storage_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DedicatedBlockStorageClusters'] = []
        if self.dedicated_block_storage_clusters is not None:
            for k in self.dedicated_block_storage_clusters:
                result['DedicatedBlockStorageClusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.dedicated_block_storage_clusters = []
        if m.get('DedicatedBlockStorageClusters') is not None:
            for k in m.get('DedicatedBlockStorageClusters'):
                temp_model = DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters()
                self.dedicated_block_storage_clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDedicatedBlockStorageClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDedicatedBlockStorageClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDedicatedBlockStorageClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskEventsRequest(TeaModel):
    def __init__(self, disk_category=None, disk_id=None, end_time=None, max_results=None, next_token=None,
                 region_id=None, start_time=None, type=None):
        # The type of the disk. Valid values:
        # 
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: enhanced SSD (ESSD).
        self.disk_category = disk_category  # type: str
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The end of the time range to query. Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The maximum number of entries per page. Valid values: 1 to 100.
        # 
        # Default values:
        # 
        # *   If this parameter is not specified or is set to a value smaller than 10, the default value is 10.
        # *   If this parameter is set to a value greater than 100, the default value is 100.
        self.max_results = max_results  # type: long
        # The pagination token that is used in this request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token  # type: str
        # The region ID of the disk. You can call the [DescribeRegions](~~354276~~) operation to query the list of regions that support CloudLens for EBS.
        self.region_id = region_id  # type: str
        # The beginning of the time range to query. Specify the time in the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The event type. Set the value to DataNeedProtect, which indicates that the disk data needs to be protected.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskEventsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDiskEventsResponseBodyDiskEvents(TeaModel):
    def __init__(self, description=None, disk_id=None, recommend_action=None, region_id=None, status=None,
                 timestamp=None, type=None):
        # The description of the event.
        self.description = description  # type: str
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The recommended action after the event occurred. Valid values:
        # 
        # *   Resize: resizes the disk.
        # *   ModifyDiskSpec: changes the category of the disk.
        # *   NoAction: performs no operation.
        self.recommend_action = recommend_action  # type: str
        # The region ID of the disk.
        self.region_id = region_id  # type: str
        # The state of the event. Valid values:
        # 
        # *   Solved
        # *   UnSolved
        self.status = status  # type: str
        # The time when the event occurred. The time follows the [ISO 8601](~~25696~~) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.timestamp = timestamp  # type: str
        # The type of the event. Only DataNeedProtect can be returned.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskEventsResponseBodyDiskEvents, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.recommend_action is not None:
            result['RecommendAction'] = self.recommend_action
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('RecommendAction') is not None:
            self.recommend_action = m.get('RecommendAction')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDiskEventsResponseBody(TeaModel):
    def __init__(self, disk_events=None, next_token=None, request_id=None, total_count=None):
        # The risk events of the disk.
        self.disk_events = disk_events  # type: list[DescribeDiskEventsResponseBodyDiskEvents]
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.disk_events:
            for k in self.disk_events:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskEventsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiskEvents'] = []
        if self.disk_events is not None:
            for k in self.disk_events:
                result['DiskEvents'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.disk_events = []
        if m.get('DiskEvents') is not None:
            for k in m.get('DiskEvents'):
                temp_model = DescribeDiskEventsResponseBodyDiskEvents()
                self.disk_events.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiskEventsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiskEventsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskEventsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiskEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskMonitorDataRequest(TeaModel):
    def __init__(self, disk_id=None, end_time=None, period=None, region_id=None, start_time=None, type=None):
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The end of the time range during which you want to query the near real-time monitoring data of the disk. Specify the time in the [ISO 8601](~~25696~~) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The interval at which the near real-time monitoring data is collected. Unit: seconds. Valid values:
        # 
        # *   5
        # *   60
        # 
        # Default value: 5.
        self.period = period  # type: long
        # The region ID of the disk.
        self.region_id = region_id  # type: str
        # The beginning of the time range during which you want to query the near real-time monitoring data of the disk. Specify the time in the [ISO 8601](~~25696~~) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The type of the monitoring data. Valid values:
        # 
        # *   basic: baseline performance data.
        # *   pro: burst performance data, such as burst I/O operations.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskMonitorDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDiskMonitorDataResponseBodyMonitorData(TeaModel):
    def __init__(self, bpspercent=None, burst_iocount=None, disk_id=None, iopspercent=None, read_bps=None,
                 read_iops=None, timestamp=None, write_bps=None, write_iops=None):
        # The percentage of BPS.
        self.bpspercent = bpspercent  # type: long
        # The number of burst I/O operations.
        self.burst_iocount = burst_iocount  # type: long
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The percentage of IOPS.
        self.iopspercent = iopspercent  # type: long
        # The read bandwidth of the disk. Unit: Mbit/s.
        self.read_bps = read_bps  # type: long
        # The maximum number of read IOPS.
        self.read_iops = read_iops  # type: long
        # The timestamp that is used to query the near real-time monitoring data of the disk. The time follows the [ISO 8601](~~25696~~) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.timestamp = timestamp  # type: str
        # The write bandwidth of the disk. Unit: Mbit/s.
        self.write_bps = write_bps  # type: long
        # The maximum number of write IOPS.
        self.write_iops = write_iops  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskMonitorDataResponseBodyMonitorData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bpspercent is not None:
            result['BPSPercent'] = self.bpspercent
        if self.burst_iocount is not None:
            result['BurstIOCount'] = self.burst_iocount
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.iopspercent is not None:
            result['IOPSPercent'] = self.iopspercent
        if self.read_bps is not None:
            result['ReadBPS'] = self.read_bps
        if self.read_iops is not None:
            result['ReadIOPS'] = self.read_iops
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.write_bps is not None:
            result['WriteBPS'] = self.write_bps
        if self.write_iops is not None:
            result['WriteIOPS'] = self.write_iops
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BPSPercent') is not None:
            self.bpspercent = m.get('BPSPercent')
        if m.get('BurstIOCount') is not None:
            self.burst_iocount = m.get('BurstIOCount')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('IOPSPercent') is not None:
            self.iopspercent = m.get('IOPSPercent')
        if m.get('ReadBPS') is not None:
            self.read_bps = m.get('ReadBPS')
        if m.get('ReadIOPS') is not None:
            self.read_iops = m.get('ReadIOPS')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('WriteBPS') is not None:
            self.write_bps = m.get('WriteBPS')
        if m.get('WriteIOPS') is not None:
            self.write_iops = m.get('WriteIOPS')
        return self


class DescribeDiskMonitorDataResponseBody(TeaModel):
    def __init__(self, monitor_data=None, request_id=None, total_count=None):
        # The near real-time monitoring data of the disk.
        self.monitor_data = monitor_data  # type: list[DescribeDiskMonitorDataResponseBodyMonitorData]
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.monitor_data:
            for k in self.monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskMonitorDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorData'] = []
        if self.monitor_data is not None:
            for k in self.monitor_data:
                result['MonitorData'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.monitor_data = []
        if m.get('MonitorData') is not None:
            for k in m.get('MonitorData'):
                temp_model = DescribeDiskMonitorDataResponseBodyMonitorData()
                self.monitor_data.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiskMonitorDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiskMonitorDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskMonitorDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiskMonitorDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskMonitorDataListRequest(TeaModel):
    def __init__(self, disk_ids=None, end_time=None, max_results=None, next_token=None, region_id=None,
                 start_time=None, type=None):
        # The IDs of the disks. The value is a JSON array that contains multiple disk IDs. Separate the IDs with commas (,).
        self.disk_ids = disk_ids  # type: str
        # The end of the time range during which you want to query the near real-time monitoring data of the disks. Specify the time in the [ISO 8601](~~25696~~) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.end_time = end_time  # type: str
        # The number of entries per page. If you specify this parameter, both `MaxResults` and `NextToken` are used for a paged query.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.max_results = max_results  # type: str
        # The pagination token that is used in this request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The region ID. You can call the [DescribeRegions](~~354276~~) operation to query the list of regions that support CloudLens for EBS.
        self.region_id = region_id  # type: str
        # The beginning of the time range during which you want to query the near real-time monitoring data of the disks. Specify the time in the [ISO 8601](~~25696~~) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in UTC.
        self.start_time = start_time  # type: str
        # The type of the monitoring data. Set the value to pro.
        # 
        # pro: burst performance data, such as burst I/O operations.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskMonitorDataListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeDiskMonitorDataListResponseBodyMonitorData(TeaModel):
    def __init__(self, burst_iocount=None, disk_id=None, timestamp=None):
        # The number of burst I/O operations.
        self.burst_iocount = burst_iocount  # type: long
        # The ID of the disk.
        self.disk_id = disk_id  # type: str
        # The beginning of the time range during which the performance of the disk bursts. The time follows the [ISO 8601](~~25696~~) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.timestamp = timestamp  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskMonitorDataListResponseBodyMonitorData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.burst_iocount is not None:
            result['BurstIOCount'] = self.burst_iocount
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BurstIOCount') is not None:
            self.burst_iocount = m.get('BurstIOCount')
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class DescribeDiskMonitorDataListResponseBody(TeaModel):
    def __init__(self, monitor_data=None, next_token=None, request_id=None, total_count=None):
        # The near real-time monitoring data of the disks.
        self.monitor_data = monitor_data  # type: list[DescribeDiskMonitorDataListResponseBodyMonitorData]
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.monitor_data:
            for k in self.monitor_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskMonitorDataListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MonitorData'] = []
        if self.monitor_data is not None:
            for k in self.monitor_data:
                result['MonitorData'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.monitor_data = []
        if m.get('MonitorData') is not None:
            for k in m.get('MonitorData'):
                temp_model = DescribeDiskMonitorDataListResponseBodyMonitorData()
                self.monitor_data.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiskMonitorDataListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiskMonitorDataListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskMonitorDataListResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiskMonitorDataListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskReplicaGroupsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N of the replication group.
        self.key = key  # type: str
        # The value of tag N to add to the replication group.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsRequestTag, self).to_map()
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


class DescribeDiskReplicaGroupsRequest(TeaModel):
    def __init__(self, group_ids=None, max_results=None, next_token=None, page_number=None, page_size=None,
                 region_id=None, resource_group_id=None, site=None, tag=None):
        # The IDs of replication pair-consistent groups. You can specify the IDs of one or more replication pair-consistent groups. Separate the IDs with commas (,).
        # 
        # This parameter is empty by default, which indicates that all replication pair-consistent groups in the specified region are queried.
        self.group_ids = group_ids  # type: str
        # The maximum number of entries to return on each page. Valid values: 1 to 500.
        # 
        # Default value: 10.
        self.max_results = max_results  # type: long
        # The query token. Set the value to the NextToken value returned in the previous call to the DescribeDiskReplicaGroups operation. Leave this parameter empty the first time you call this operation. When NextToken is specified, the PageSize and PageNumber request parameters do not take effect and the TotalCount response parameter is invalid.
        self.next_token = next_token  # type: str
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The region ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the replication group belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the site from which the information of replication pair-consistent groups is retrieved. This parameter is used for scenarios where data is replicated across zones in replication pairs.
        # 
        # *   If the Site parameter is not specified, information such as the state of replication pair-consistent groups at the primary site is queried and returned.
        # 
        # *   Otherwise, information such as the state of replication pair-consistent groups at the site specified by the Site parameter is queried and returned. Valid values:
        # 
        #     *   production: primary site
        #     *   backup: secondary site
        self.site = site  # type: str
        # The resource tags. You can specify up to 20 tags.
        self.tag = tag  # type: list[DescribeDiskReplicaGroupsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_ids is not None:
            result['GroupIds'] = self.group_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site is not None:
            result['Site'] = self.site
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GroupIds') is not None:
            self.group_ids = m.get('GroupIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDiskReplicaGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key of the replication group.
        self.tag_key = tag_key  # type: str
        # The tag value of the replication group.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDiskReplicaGroupsResponseBodyReplicaGroups(TeaModel):
    def __init__(self, bandwidth=None, description=None, destination_region_id=None, destination_zone_id=None,
                 group_name=None, last_recover_point=None, pair_ids=None, pair_number=None, primary_region=None,
                 primary_zone=None, rpo=None, replica_group_id=None, resource_group_id=None, site=None, source_region_id=None,
                 source_zone_id=None, standby_region=None, standby_zone=None, status=None, tags=None):
        # The bandwidth value. Unit: Mbit/s. This parameter is unavailable and has a system-preset value.
        self.bandwidth = bandwidth  # type: long
        # The description of the replication pair-consistent group.
        self.description = description  # type: str
        # The ID of the region in which the secondary site is deployed.
        self.destination_region_id = destination_region_id  # type: str
        # The ID of the zone in which the secondary site is deployed.
        self.destination_zone_id = destination_zone_id  # type: str
        # The name of the replication pair-consistent group.
        self.group_name = group_name  # type: str
        # The time when data was last replicated from the primary disks to the secondary disks in the replication pair-consistent group. The value of this parameter is a timestamp. Unit: seconds.
        self.last_recover_point = last_recover_point  # type: long
        # The IDs of the replications pairs that belong to the replication pair-consistent group.
        self.pair_ids = pair_ids  # type: list[bytes]
        # The number of replications pairs that belong to the replication pair-consistent group.
        self.pair_number = pair_number  # type: long
        # The initial source region (primary region) of the replication pair-consistent group.
        self.primary_region = primary_region  # type: str
        # The initial source zone (primary zone) of the replication pair-consistent group.
        self.primary_zone = primary_zone  # type: str
        # The recovery point objective (RPO) of the replication pair-consistent group. Unit: seconds.
        self.rpo = rpo  # type: long
        # The ID of the replication pair-consistent group.
        self.replica_group_id = replica_group_id  # type: str
        # The ID of the resource group to which the replication group belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the site from which the information of the replication pair and replication pair-consistent group is obtained. Valid values:
        # 
        # *   production: primary site
        # *   backup: secondary site
        self.site = site  # type: str
        # The ID of the region in which the primary site is deployed.
        self.source_region_id = source_region_id  # type: str
        # The ID of the zone in which the primary site is deployed.
        self.source_zone_id = source_zone_id  # type: str
        # The initial destination region (secondary region) of the replication pair-consistent group.
        self.standby_region = standby_region  # type: str
        # The initial destination zone (secondary zone) of the replication pair-consistent group.
        self.standby_zone = standby_zone  # type: str
        # The state of the replication pair-consistent group. Valid values:
        # 
        # *   invalid: The replication pair-consistent group is invalid, which indicates that abnormal replication pairs are present in the replication pair-consistent group.
        # *   creating: The replication pair-consistent group is being created.
        # *   created: The replication pair-consistent group is created.
        # *   create_failed: The replication pair-consistent group cannot be created.
        # *   manual_syncing: Data is being manually synchronized between the disks in the replication pair-consistent group. The first time data is being manually synchronized between the disks in a replication pair-consistent group, the replication pair-consistent group is in this state.
        # *   syncing: Data is being synchronized between the disks in the replication pair-consistent group. While data is being asynchronously replicated from the primary disks to the secondary disks not for the first time, the replication pair-consistent group is in this state.
        # *   normal: The replication pair-consistent group is working as expected. When the system finishes replicating data from the primary disks to the secondary disks within the current replication cycle, the replication pair-consistent group enters this state.
        # *   stopping: The replication pair-consistent group is being stopped.
        # *   stopped: The replication pair-consistent group is stopped.
        # *   stop_failed: The replication pair-consistent group cannot be stopped.
        # *   failovering: A failover is being performed.
        # *   failovered: A failover is performed.
        # *   failover_failed: A failover cannot be performed.
        # *   reprotecting: A reverse replication is being performed.
        # *   reprotect_failed: A reverse replication cannot be performed.
        # *   deleting: The replication pair-consistent group is being deleted.
        # *   delete_failed: The replication pair-consistent group cannot be deleted.
        # *   deleted: The replication pair-consistent group is deleted.
        self.status = status  # type: str
        # The tags of the replication pair.
        self.tags = tags  # type: list[DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsResponseBodyReplicaGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id
        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.last_recover_point is not None:
            result['LastRecoverPoint'] = self.last_recover_point
        if self.pair_ids is not None:
            result['PairIds'] = self.pair_ids
        if self.pair_number is not None:
            result['PairNumber'] = self.pair_number
        if self.primary_region is not None:
            result['PrimaryRegion'] = self.primary_region
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.rpo is not None:
            result['RPO'] = self.rpo
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site is not None:
            result['Site'] = self.site
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
        if self.standby_region is not None:
            result['StandbyRegion'] = self.standby_region
        if self.standby_zone is not None:
            result['StandbyZone'] = self.standby_zone
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')
        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('LastRecoverPoint') is not None:
            self.last_recover_point = m.get('LastRecoverPoint')
        if m.get('PairIds') is not None:
            self.pair_ids = m.get('PairIds')
        if m.get('PairNumber') is not None:
            self.pair_number = m.get('PairNumber')
        if m.get('PrimaryRegion') is not None:
            self.primary_region = m.get('PrimaryRegion')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        if m.get('StandbyRegion') is not None:
            self.standby_region = m.get('StandbyRegion')
        if m.get('StandbyZone') is not None:
            self.standby_zone = m.get('StandbyZone')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDiskReplicaGroupsResponseBodyReplicaGroupsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeDiskReplicaGroupsResponseBody(TeaModel):
    def __init__(self, next_token=None, page_number=None, page_size=None, replica_groups=None, request_id=None,
                 total_count=None):
        # The query token returned in this call.
        self.next_token = next_token  # type: str
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # Details about the replication pair-consistent groups.
        self.replica_groups = replica_groups  # type: list[DescribeDiskReplicaGroupsResponseBodyReplicaGroups]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.replica_groups:
            for k in self.replica_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ReplicaGroups'] = []
        if self.replica_groups is not None:
            for k in self.replica_groups:
                result['ReplicaGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.replica_groups = []
        if m.get('ReplicaGroups') is not None:
            for k in m.get('ReplicaGroups'):
                temp_model = DescribeDiskReplicaGroupsResponseBodyReplicaGroups()
                self.replica_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiskReplicaGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiskReplicaGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiskReplicaGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskReplicaPairProgressRequest(TeaModel):
    def __init__(self, region_id=None, replica_pair_id=None):
        # The region ID of the replication pair.
        self.region_id = region_id  # type: str
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~)operation to query the IDs of existing replication pairs.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaPairProgressRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class DescribeDiskReplicaPairProgressResponseBody(TeaModel):
    def __init__(self, progress=None, recover_point=None, request_id=None):
        # The replication progress of the replication pair.
        self.progress = progress  # type: int
        # The timestamp that indicates the last recovery point in time. The value is returned only after the replication pair works for replicating data.
        self.recover_point = recover_point  # type: long
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaPairProgressResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.recover_point is not None:
            result['RecoverPoint'] = self.recover_point
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RecoverPoint') is not None:
            self.recover_point = m.get('RecoverPoint')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDiskReplicaPairProgressResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiskReplicaPairProgressResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaPairProgressResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiskReplicaPairProgressResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeDiskReplicaPairsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaPairsRequestTag, self).to_map()
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


class DescribeDiskReplicaPairsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, page_number=None, page_size=None, pair_ids=None,
                 region_id=None, replica_group_id=None, resource_group_id=None, site=None, tag=None):
        # The maximum number of entries per page. You can use this parameter together with NextToken.
        # 
        # Valid values: 1 to 500.
        # 
        # Default value: 10.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken. If you specify NextToken, the PageSize and PageNumber request parameters do not take effect, and the TotalCount response parameter is invalid.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The IDs of replication pairs. You can specify the IDs of one or more replication pairs and separate the IDs with commas (,). Example: `pair-cn-dsa****,pair-cn-asd****`.
        # 
        # This parameter is empty by default, which indicates that all replication pairs in the specified region are queried. You can specify a maximum of 100 replication pair IDs.
        self.pair_ids = pair_ids  # type: str
        # The region ID of the primary or secondary disk in the replication pair. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group. You can specify the ID of a replication pair-consistent group to query the replication pairs in the group. Example: `pg-****`.
        # 
        # This parameter is empty by default, which indicates that all replication pairs in the specified region are queried.
        # 
        # >  If this parameter is set to`-`, replication pairs that are not added to any replication pair-consistent groups are returned.
        self.replica_group_id = replica_group_id  # type: str
        # The ID of the resource group to which the replication pair belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the site from which the information of replication pairs is retrieved. Valid value:
        # 
        # *   production: primary site
        # *   backup: secondary site
        # 
        # Default value: production.
        self.site = site  # type: str
        # The tags. Up to 20 tags are supported.
        self.tag = tag  # type: list[DescribeDiskReplicaPairsRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaPairsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pair_ids is not None:
            result['PairIds'] = self.pair_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site is not None:
            result['Site'] = self.site
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PairIds') is not None:
            self.pair_ids = m.get('PairIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeDiskReplicaPairsRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeDiskReplicaPairsResponseBodyReplicaPairsTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The key of the tag.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaPairsResponseBodyReplicaPairsTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeDiskReplicaPairsResponseBodyReplicaPairs(TeaModel):
    def __init__(self, bandwidth=None, charge_type=None, create_time=None, description=None,
                 destination_disk_id=None, destination_region=None, destination_zone_id=None, expired_time=None,
                 last_recover_point=None, pair_name=None, primary_region=None, primary_zone=None, rpo=None, replica_group_id=None,
                 replica_group_name=None, replica_pair_id=None, resource_group_id=None, site=None, source_disk_id=None,
                 source_region=None, source_zone_id=None, standby_region=None, standby_zone=None, status=None,
                 status_message=None, tags=None):
        # The bandwidth used to asynchronously replicate data from the primary disk to the secondary disk. Unit: Kbit/s.
        self.bandwidth = bandwidth  # type: long
        # The billing method of the replication pair. Valid values:
        # 
        # *   PREPAY: subscription
        # *   POSTPAY: pay-as-you-go
        self.charge_type = charge_type  # type: str
        # The time when the replication pair was created. The value of this parameter is a timestamp. Unit: seconds.
        self.create_time = create_time  # type: long
        # The description of the replication pair.
        self.description = description  # type: str
        # The ID of the secondary disk.
        self.destination_disk_id = destination_disk_id  # type: str
        # The region ID of the secondary disk.
        self.destination_region = destination_region  # type: str
        # The zone ID of the secondary disk.
        self.destination_zone_id = destination_zone_id  # type: str
        # The time when the replication pair expires. The value of this parameter is a timestamp. Unit: seconds.
        self.expired_time = expired_time  # type: long
        # The time when data was last replicated from the primary disk to the secondary disk in the replication pair. The value of this parameter is a timestamp. Unit: seconds. 86,400 seconds is equivalent to 24 hours.
        self.last_recover_point = last_recover_point  # type: long
        # The name of the replication pair.
        self.pair_name = pair_name  # type: str
        # The initial source region (primary region) of the replication pair.
        self.primary_region = primary_region  # type: str
        # The initial source zone (primary zone) of the replication pair.
        self.primary_zone = primary_zone  # type: str
        # The recovery point objective (RPO) of the replication pair. Unit: seconds.
        self.rpo = rpo  # type: long
        # The ID of the replication pair-consistent group to which the replication pair belongs.
        self.replica_group_id = replica_group_id  # type: str
        # The name of the replication pair-consistent group to which the replication pair belongs.
        self.replica_group_name = replica_group_name  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str
        # The ID of the resource group to which the replication pair belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The type of the site from which the information about the replication pairs and replication pair-consistent group was obtained. Valid values:
        # 
        # *   production: primary site
        # *   backup: secondary site
        self.site = site  # type: str
        # The ID of the primary disk.
        self.source_disk_id = source_disk_id  # type: str
        # The region ID of the primary disk.
        self.source_region = source_region  # type: str
        # The zone ID of the primary disk.
        self.source_zone_id = source_zone_id  # type: str
        # The initial destination region (secondary region) of the replication pair.
        self.standby_region = standby_region  # type: str
        # The initial destination zone (secondary zone) of the replication pair.
        self.standby_zone = standby_zone  # type: str
        # The status of the replication pair. Valid values:
        # 
        # *   invalid: The replication pair was invalid. When a replication pair becomes abnormal, it enters this state.
        # *   creating: The replication pair was being created.
        # *   created: The replication pair was created.
        # *   create_failed: The replication pair failed to be created.
        # *   initial_syncing: Data was synchronized from the primary disk to the secondary disk for the first time. After a replication pair is created and activated, the replication pair is in this state the first time data is synchronized from the primary disk to the secondary disk.
        # *   manual_syncing: Data was being manually synchronized from the primary disk to the secondary disk. After data is manually synchronized from the primary disk to the secondary disk, the replication pair returns to the stopped state. The first time data is manually synchronized from the primary disk to the secondary disk, the replication pair is in the manual_syncing state during the synchronization.
        # *   syncing: Data was being synchronized from the primary disk to the secondary disk. When data is being asynchronously replicated from the primary disk to the secondary disk again in subsequent operations, the replication pair is in this state.
        # *   normal: The replication pair was working as expected. When the system finishes replicating data from the primary disk to the secondary disk within the current replication cycle, the replication pair enters this state.
        # *   stopping: The replication pair was being stopped.
        # *   stopped: The replication pair was stopped.
        # *   stop_failed: The replication pair failed to be stopped.
        # *   failovering: A failover was being performed.
        # *   failovered: A failover was performed.
        # *   failover_failed: A failover failed to be performed.
        # *   reprotecting: A reverse replication was being performed.
        # *   reprotect_failed: A reverse replication failed to be performed.
        # *   deleting: The replication pair was being deleted.
        # *   delete_failed: The replication pair failed to be deleted.
        # *   deleted: The replication pair was deleted.
        self.status = status  # type: str
        # The message that describes the state of the replication pair. This parameter has a value when `Status` has a value of invalid or `create_failed`. Valid values:
        # 
        # *   PrePayOrderExpired: The replication pair has expired.
        # *   PostPayOrderCeaseService: The pay-as-you-go replication pair has been stopped due to an overdue payment.
        # *   DeviceRemoved: The primary or secondary disk has been deleted.
        # *   DeviceKeyChanged: The `DeviceKey` mapping of the primary or secondary disk has changed.
        # *   DeviceSizeChanged: The `DeviceSize` value of the primary or secondary disk has changed.
        # *   OperationDenied.QuotaExceed: The maximum number of replication pairs that can be created has been reached.
        self.status_message = status_message  # type: str
        # The tags of the replication pair.
        self.tags = tags  # type: list[DescribeDiskReplicaPairsResponseBodyReplicaPairsTags]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaPairsResponseBodyReplicaPairs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.destination_disk_id is not None:
            result['DestinationDiskId'] = self.destination_disk_id
        if self.destination_region is not None:
            result['DestinationRegion'] = self.destination_region
        if self.destination_zone_id is not None:
            result['DestinationZoneId'] = self.destination_zone_id
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.last_recover_point is not None:
            result['LastRecoverPoint'] = self.last_recover_point
        if self.pair_name is not None:
            result['PairName'] = self.pair_name
        if self.primary_region is not None:
            result['PrimaryRegion'] = self.primary_region
        if self.primary_zone is not None:
            result['PrimaryZone'] = self.primary_zone
        if self.rpo is not None:
            result['RPO'] = self.rpo
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.replica_group_name is not None:
            result['ReplicaGroupName'] = self.replica_group_name
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.site is not None:
            result['Site'] = self.site
        if self.source_disk_id is not None:
            result['SourceDiskId'] = self.source_disk_id
        if self.source_region is not None:
            result['SourceRegion'] = self.source_region
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
        if self.standby_region is not None:
            result['StandbyRegion'] = self.standby_region
        if self.standby_zone is not None:
            result['StandbyZone'] = self.standby_zone
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DestinationDiskId') is not None:
            self.destination_disk_id = m.get('DestinationDiskId')
        if m.get('DestinationRegion') is not None:
            self.destination_region = m.get('DestinationRegion')
        if m.get('DestinationZoneId') is not None:
            self.destination_zone_id = m.get('DestinationZoneId')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('LastRecoverPoint') is not None:
            self.last_recover_point = m.get('LastRecoverPoint')
        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')
        if m.get('PrimaryRegion') is not None:
            self.primary_region = m.get('PrimaryRegion')
        if m.get('PrimaryZone') is not None:
            self.primary_zone = m.get('PrimaryZone')
        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('ReplicaGroupName') is not None:
            self.replica_group_name = m.get('ReplicaGroupName')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        if m.get('SourceDiskId') is not None:
            self.source_disk_id = m.get('SourceDiskId')
        if m.get('SourceRegion') is not None:
            self.source_region = m.get('SourceRegion')
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        if m.get('StandbyRegion') is not None:
            self.standby_region = m.get('StandbyRegion')
        if m.get('StandbyZone') is not None:
            self.standby_zone = m.get('StandbyZone')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeDiskReplicaPairsResponseBodyReplicaPairsTags()
                self.tags.append(temp_model.from_map(k))
        return self


class DescribeDiskReplicaPairsResponseBody(TeaModel):
    def __init__(self, next_token=None, page_number=None, page_size=None, replica_pairs=None, request_id=None,
                 total_count=None):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # Details about the replication pairs.
        self.replica_pairs = replica_pairs  # type: list[DescribeDiskReplicaPairsResponseBodyReplicaPairs]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.replica_pairs:
            for k in self.replica_pairs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaPairsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ReplicaPairs'] = []
        if self.replica_pairs is not None:
            for k in self.replica_pairs:
                result['ReplicaPairs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.replica_pairs = []
        if m.get('ReplicaPairs') is not None:
            for k in m.get('ReplicaPairs'):
                temp_model = DescribeDiskReplicaPairsResponseBodyReplicaPairs()
                self.replica_pairs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeDiskReplicaPairsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeDiskReplicaPairsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeDiskReplicaPairsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeDiskReplicaPairsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEnterpriseSnapshotPolicyRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyRequestTag, self).to_map()
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


class DescribeEnterpriseSnapshotPolicyRequest(TeaModel):
    def __init__(self, client_token=None, max_results=None, next_token=None, page_number=None, page_size=None,
                 policy_ids=None, region_id=None, resource_group_id=None, tag=None):
        self.client_token = client_token  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policy_ids = policy_ids  # type: list[str]
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.tag = tag  # type: list[DescribeEnterpriseSnapshotPolicyRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeEnterpriseSnapshotPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions(TeaModel):
    def __init__(self, region_id=None, retain_days=None):
        self.region_id = region_id  # type: str
        self.retain_days = retain_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_days is not None:
            result['RetainDays'] = self.retain_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainDays') is not None:
            self.retain_days = m.get('RetainDays')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo(TeaModel):
    def __init__(self, enabled=None, regions=None):
        self.enabled = enabled  # type: bool
        self.regions = regions  # type: list[DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfoRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule(TeaModel):
    def __init__(self, number=None, time_interval=None, time_unit=None):
        self.number = number  # type: int
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule(TeaModel):
    def __init__(self, cron_expression=None):
        self.cron_expression = cron_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules(TeaModel):
    def __init__(self, special_period_unit=None, time_interval=None, time_unit=None):
        self.special_period_unit = special_period_unit  # type: str
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_period_unit is not None:
            result['SpecialPeriodUnit'] = self.special_period_unit
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecialPeriodUnit') is not None:
            self.special_period_unit = m.get('SpecialPeriodUnit')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules(TeaModel):
    def __init__(self, enabled=None, rules=None):
        self.enabled = enabled  # type: bool
        self.rules = rules  # type: list[DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRulesRules()
                self.rules.append(temp_model.from_map(k))
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule(TeaModel):
    def __init__(self, enable_immediate_access=None):
        self.enable_immediate_access = enable_immediate_access  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_immediate_access is not None:
            result['EnableImmediateAccess'] = self.enable_immediate_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableImmediateAccess') is not None:
            self.enable_immediate_access = m.get('EnableImmediateAccess')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBodyPolicies(TeaModel):
    def __init__(self, create_time=None, cross_region_copy_info=None, desc=None, managed_for_ecs=None, name=None,
                 policy_id=None, resource_group_id=None, retain_rule=None, schedule=None, special_retain_rules=None,
                 state=None, storage_rule=None, tags=None, target_count=None, target_type=None):
        self.create_time = create_time  # type: str
        self.cross_region_copy_info = cross_region_copy_info  # type: DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo
        self.desc = desc  # type: str
        self.managed_for_ecs = managed_for_ecs  # type: bool
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        # the resource group
        self.resource_group_id = resource_group_id  # type: str
        self.retain_rule = retain_rule  # type: DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule
        self.schedule = schedule  # type: DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule
        self.special_retain_rules = special_retain_rules  # type: DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules
        self.state = state  # type: str
        self.storage_rule = storage_rule  # type: DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule
        # the pair tags
        self.tags = tags  # type: list[DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags]
        self.target_count = target_count  # type: int
        self.target_type = target_type  # type: str

    def validate(self):
        if self.cross_region_copy_info:
            self.cross_region_copy_info.validate()
        if self.retain_rule:
            self.retain_rule.validate()
        if self.schedule:
            self.schedule.validate()
        if self.special_retain_rules:
            self.special_retain_rules.validate()
        if self.storage_rule:
            self.storage_rule.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBodyPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_region_copy_info is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info.to_map()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.managed_for_ecs is not None:
            result['ManagedForEcs'] = self.managed_for_ecs
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retain_rule is not None:
            result['RetainRule'] = self.retain_rule.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        if self.special_retain_rules is not None:
            result['SpecialRetainRules'] = self.special_retain_rules.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.storage_rule is not None:
            result['StorageRule'] = self.storage_rule.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.target_count is not None:
            result['TargetCount'] = self.target_count
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossRegionCopyInfo') is not None:
            temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesCrossRegionCopyInfo()
            self.cross_region_copy_info = temp_model.from_map(m['CrossRegionCopyInfo'])
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('ManagedForEcs') is not None:
            self.managed_for_ecs = m.get('ManagedForEcs')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetainRule') is not None:
            temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesRetainRule()
            self.retain_rule = temp_model.from_map(m['RetainRule'])
        if m.get('Schedule') is not None:
            temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSchedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        if m.get('SpecialRetainRules') is not None:
            temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesSpecialRetainRules()
            self.special_retain_rules = temp_model.from_map(m['SpecialRetainRules'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StorageRule') is not None:
            temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesStorageRule()
            self.storage_rule = temp_model.from_map(m['StorageRule'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPoliciesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TargetCount') is not None:
            self.target_count = m.get('TargetCount')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class DescribeEnterpriseSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, next_token=None, page_number=None, page_size=None, policies=None, request_id=None,
                 total_count=None):
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.policies = policies  # type: list[DescribeEnterpriseSnapshotPolicyResponseBodyPolicies]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = DescribeEnterpriseSnapshotPolicyResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeEnterpriseSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeEnterpriseSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeEnterpriseSnapshotPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEnterpriseSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeLensServiceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The state of CloudLens for EBS. Valid values:
        # 
        # *   Applying
        # *   UnAvailable
        # *   Available
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeLensServiceStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeLensServiceStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeLensServiceStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeLensServiceStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeLensServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeMetricDataRequest(TeaModel):
    def __init__(self, dimensions=None, end_time=None, metric_name=None, period=None, region_id=None,
                 start_time=None):
        self.dimensions = dimensions  # type: str
        self.end_time = end_time  # type: str
        self.metric_name = metric_name  # type: str
        self.period = period  # type: int
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMetricDataRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dimensions is not None:
            result['Dimensions'] = self.dimensions
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.metric_name is not None:
            result['MetricName'] = self.metric_name
        if self.period is not None:
            result['Period'] = self.period
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Dimensions') is not None:
            self.dimensions = m.get('Dimensions')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class DescribeMetricDataResponseBodyDataList(TeaModel):
    def __init__(self, datapoints=None, labels=None):
        self.datapoints = datapoints  # type: any
        self.labels = labels  # type: any

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeMetricDataResponseBodyDataList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints
        if self.labels is not None:
            result['Labels'] = self.labels
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        return self


class DescribeMetricDataResponseBody(TeaModel):
    def __init__(self, data_list=None, request_id=None, total_count=None):
        self.data_list = data_list  # type: list[DescribeMetricDataResponseBodyDataList]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeMetricDataResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = DescribeMetricDataResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeMetricDataResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeMetricDataResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeMetricDataResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeMetricDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePairDrillsRequest(TeaModel):
    def __init__(self, drill_id=None, max_results=None, next_token=None, page_number=None, page_size=None,
                 pair_id=None, region_id=None):
        # The ID of the drill.
        self.drill_id = drill_id  # type: str
        # The maximum number of entries to be returned. You can use this parameter together with NextToken.
        # 
        # Valid values: 1 to 500.
        # 
        # Default value: 10.
        self.max_results = max_results  # type: long
        # The pagination token that is used in the next request to retrieve a new page of results. Set the value to the NextToken value returned in the previous call to the DescribeDiskReplicaPairs operation. Leave this parameter empty the first time you call this operation. When you specify NextToken, the PageSize and PageNumber request parameters do not take effect and the TotalCount response parameter is invalid.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query a list of asynchronous replication pairs, including replication pair IDs.
        self.pair_id = pair_id  # type: str
        # The region ID of the primary or secondary disk in the async replication pair. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePairDrillsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.pair_id is not None:
            result['PairId'] = self.pair_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PairId') is not None:
            self.pair_id = m.get('PairId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribePairDrillsResponseBodyDrills(TeaModel):
    def __init__(self, drill_disk_id=None, drill_disk_status=None, drill_id=None, recover_point=None, start_at=None,
                 status=None, status_message=None):
        # The ID of the drill disk.
        self.drill_disk_id = drill_disk_id  # type: str
        # The status of the drill disk. Valid values:
        # 
        # *   created
        # *   deleted
        # *   creating
        # *   deleting
        # 
        # >  This parameter can also display error code details if your drill disk fails to be created or deleted.
        self.drill_disk_status = drill_disk_status  # type: str
        # The ID of the drill.
        self.drill_id = drill_id  # type: str
        # The recovery point of the drill. The value of this parameter is a timestamp. Unit: seconds.
        self.recover_point = recover_point  # type: long
        # The beginning time of the drill. The value of this parameter is a timestamp. Unit: seconds.
        self.start_at = start_at  # type: long
        # The status of the drill. Valid values:
        # 
        # *   execute_failed
        # *   executed
        # *   executing
        # *   clear_failed
        # *   clearing
        self.status = status  # type: str
        # The error message that was displayed if the drill failed to be executed.
        self.status_message = status_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribePairDrillsResponseBodyDrills, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_disk_id is not None:
            result['DrillDiskId'] = self.drill_disk_id
        if self.drill_disk_status is not None:
            result['DrillDiskStatus'] = self.drill_disk_status
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.recover_point is not None:
            result['RecoverPoint'] = self.recover_point
        if self.start_at is not None:
            result['StartAt'] = self.start_at
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillDiskId') is not None:
            self.drill_disk_id = m.get('DrillDiskId')
        if m.get('DrillDiskStatus') is not None:
            self.drill_disk_status = m.get('DrillDiskStatus')
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('RecoverPoint') is not None:
            self.recover_point = m.get('RecoverPoint')
        if m.get('StartAt') is not None:
            self.start_at = m.get('StartAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class DescribePairDrillsResponseBody(TeaModel):
    def __init__(self, drills=None, next_token=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        # The information of disaster recovery drills that were performed on the replication pair.
        self.drills = drills  # type: list[DescribePairDrillsResponseBodyDrills]
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.drills:
            for k in self.drills:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribePairDrillsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Drills'] = []
        if self.drills is not None:
            for k in self.drills:
                result['Drills'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.drills = []
        if m.get('Drills') is not None:
            for k in m.get('Drills'):
                temp_model = DescribePairDrillsResponseBodyDrills()
                self.drills.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribePairDrillsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribePairDrillsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribePairDrillsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePairDrillsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, region_id=None, resource_type=None):
        # The language in which the regions and zones are named. This parameter corresponds to the `LocalName` response parameter. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        # *   ja: Japanese
        # 
        # Default value: zh-CN.
        self.accept_language = accept_language  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # The type of resource. Valid values:
        # 
        # *   ear: async replication
        # *   lens: CloudLens for EBS
        # *   dbsc: Dedicated Block Storage Cluster
        # 
        # Default value: ear.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DescribeRegionsResponseBodyRegionsZones(TeaModel):
    def __init__(self, local_name=None, resource_types=None, zone_id=None):
        # The name of the zone.
        self.local_name = local_name  # type: str
        # The type of resource list.
        self.resource_types = resource_types  # type: list[str]
        # The ID of the zone.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegionsZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None, zones=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the region.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str
        # Details about the zones.
        self.zones = zones  # type: list[DescribeRegionsResponseBodyRegionsZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeRegionsResponseBodyRegionsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # Details about the regions.
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class DescribeReplicaGroupDrillsRequest(TeaModel):
    def __init__(self, drill_id=None, group_id=None, max_results=None, next_token=None, page_number=None,
                 page_size=None, region_id=None):
        # The ID of the drill.
        self.drill_id = drill_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query a list of async replication pair-consistent groups, including group IDs.
        self.group_id = group_id  # type: str
        # The maximum number of entries to be returned. You can use this parameter together with NextToken.
        # 
        # Valid values: 1 to 500.
        # 
        # Default value: 10.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken. When you specify NextToken, the PageSize and PageNumber request parameters do not take effect and the TotalCount response parameter is invalid.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page. Valid values: 1 to 100.
        self.page_size = page_size  # type: int
        # The region ID of the primary or secondary disk in the async replication pair-consistent group. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicaGroupDrillsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo(TeaModel):
    def __init__(self, drill_disk_id=None, drill_disk_status=None, pair_id=None):
        # The ID of the drill disk.
        self.drill_disk_id = drill_disk_id  # type: str
        # The status of the drill disk. Valid values:
        # 
        # *   created
        # *   deleted
        # *   creating
        # *   deleting
        # 
        # >  This parameter can also display error code details if your drill disk fails to be created or deleted.
        self.drill_disk_status = drill_disk_status  # type: str
        # The ID of the replication pair.
        self.pair_id = pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_disk_id is not None:
            result['DrillDiskId'] = self.drill_disk_id
        if self.drill_disk_status is not None:
            result['DrillDiskStatus'] = self.drill_disk_status
        if self.pair_id is not None:
            result['PairId'] = self.pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillDiskId') is not None:
            self.drill_disk_id = m.get('DrillDiskId')
        if m.get('DrillDiskStatus') is not None:
            self.drill_disk_status = m.get('DrillDiskStatus')
        if m.get('PairId') is not None:
            self.pair_id = m.get('PairId')
        return self


class DescribeReplicaGroupDrillsResponseBodyDrills(TeaModel):
    def __init__(self, drill_id=None, group_id=None, pairs_info=None, recover_point=None, start_at=None, status=None,
                 status_message=None):
        # The ID of the drill.
        self.drill_id = drill_id  # type: str
        # The ID of the replication pair-consistent group.
        self.group_id = group_id  # type: str
        # The information of replication pairs.
        self.pairs_info = pairs_info  # type: list[DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo]
        # The recovery point of the drill. The value of this parameter is a timestamp. Unit: seconds.
        self.recover_point = recover_point  # type: long
        # The beginning time of the drill. The value of this parameter is a timestamp. Unit: seconds.
        self.start_at = start_at  # type: long
        # The status of the drill. Valid values:
        # 
        # *   execute_failed
        # *   executed
        # *   executing
        # *   clear_failed
        # *   clearing
        self.status = status  # type: str
        # The error message that appears if the drill fails to be executed.
        self.status_message = status_message  # type: str

    def validate(self):
        if self.pairs_info:
            for k in self.pairs_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicaGroupDrillsResponseBodyDrills, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        result['PairsInfo'] = []
        if self.pairs_info is not None:
            for k in self.pairs_info:
                result['PairsInfo'].append(k.to_map() if k else None)
        if self.recover_point is not None:
            result['RecoverPoint'] = self.recover_point
        if self.start_at is not None:
            result['StartAt'] = self.start_at
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        self.pairs_info = []
        if m.get('PairsInfo') is not None:
            for k in m.get('PairsInfo'):
                temp_model = DescribeReplicaGroupDrillsResponseBodyDrillsPairsInfo()
                self.pairs_info.append(temp_model.from_map(k))
        if m.get('RecoverPoint') is not None:
            self.recover_point = m.get('RecoverPoint')
        if m.get('StartAt') is not None:
            self.start_at = m.get('StartAt')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class DescribeReplicaGroupDrillsResponseBody(TeaModel):
    def __init__(self, drills=None, next_token=None, page_number=None, page_size=None, request_id=None,
                 total_count=None):
        # The information of disaster recovery drills that were performed on the replication pair-consistent group.
        self.drills = drills  # type: list[DescribeReplicaGroupDrillsResponseBodyDrills]
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token  # type: str
        # The page number.
        self.page_number = page_number  # type: int
        # The number of entries per page.
        self.page_size = page_size  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.drills:
            for k in self.drills:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeReplicaGroupDrillsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Drills'] = []
        if self.drills is not None:
            for k in self.drills:
                result['Drills'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.drills = []
        if m.get('Drills') is not None:
            for k in m.get('Drills'):
                temp_model = DescribeReplicaGroupDrillsResponseBodyDrills()
                self.drills.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeReplicaGroupDrillsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeReplicaGroupDrillsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeReplicaGroupDrillsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeReplicaGroupDrillsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailoverDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the secondary site of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group.
        self.replica_group_id = replica_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailoverDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        return self


class FailoverDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailoverDiskReplicaGroupResponseBody, self).to_map()
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


class FailoverDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FailoverDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FailoverDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FailoverDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FailoverDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_pair_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the secondary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query region IDs of secondary disks in replication pairs.
        # 
        # >  The failover feature must be enabled for the region where the secondary disk is located.
        self.region_id = region_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailoverDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class FailoverDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(FailoverDiskReplicaPairResponseBody, self).to_map()
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


class FailoverDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: FailoverDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(FailoverDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FailoverDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N used for exact search of EBS resources. The tag key must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        # 
        # The `Tag.N` parameter pair (Tag.N.Key and Tag.N.Value) is used for exact search of EBS resources that have specified tags added. Each tag is a key-value pair.
        # 
        # *   If you specify only `Tag.N.Key`, all EBS resources whose tags contain the specified tag key are returned.
        # *   If you specify only `Tag.N.Value`, the `InvalidParameter.TagValue` error is returned.
        # *   If you specify multiple tag key-value pairs at the same time, only EBS resources that match all tag key-value pairs are returned.
        self.key = key  # type: str
        # The value of tag N used for exact search of EBS resources. The tag value must be 1 to 128 characters in length. Valid values of N: 1 to 20.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(self, client_token=None, next_token=None, region_id=None, resource_id=None, resource_type=None,
                 tag=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The token used to start the next query.
        self.next_token = next_token  # type: str
        # The region ID of the resource. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID list of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Valid values:
        # 
        # *   dedicatedblockstoragecluster: dedicated block storage cluster
        # *   diskreplicapair: replication pair
        # *   diskreplicagroup: replication pair-consistent group
        self.resource_type = resource_type  # type: str
        # The information about the tags.
        # 
        # You can specify at most 20 tags in each call.
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The type of the resource. Valid values:
        # 
        # *   dedicatedblockstoragecluster: dedicated block storage cluster
        # *   diskreplicapair: replication pair
        # *   diskreplicagroup: replication pair-consistent group
        self.resource_type = resource_type  # type: str
        # The tag key of the resource.
        self.tag_key = tag_key  # type: str
        # The tag value of the resource.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # The token used to start the next query.
        self.next_token = next_token  # type: str
        # The ID of the request. The request ID is returned regardless of whether the call is successful.
        self.request_id = request_id  # type: str
        # Details about the resources and tags, including resource IDs, resource types, and tag key-value pairs.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDedicatedBlockStorageClusterAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dbsc_id=None, dbsc_name=None, description=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests.
        # 
        # The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How do I ensure idempotence ](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the dedicated block storage cluster.
        self.dbsc_id = dbsc_id  # type: str
        # The new name of the dedicated block storage cluster.
        self.dbsc_name = dbsc_name  # type: str
        # The new description of dedicated block storage cluster.
        self.description = description  # type: str
        # The region ID of the dedicated block storage cluster. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedBlockStorageClusterAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dbsc_id is not None:
            result['DbscId'] = self.dbsc_id
        if self.dbsc_name is not None:
            result['DbscName'] = self.dbsc_name
        if self.description is not None:
            result['Description'] = self.description
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DbscId') is not None:
            self.dbsc_id = m.get('DbscId')
        if m.get('DbscName') is not None:
            self.dbsc_name = m.get('DbscName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyDedicatedBlockStorageClusterAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDedicatedBlockStorageClusterAttributeResponseBody, self).to_map()
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


class ModifyDedicatedBlockStorageClusterAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDedicatedBlockStorageClusterAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDedicatedBlockStorageClusterAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDedicatedBlockStorageClusterAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskReplicaGroupRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, group_name=None, rpo=None,
                 region_id=None, replica_group_id=None):
        # The bandwidth value. Unit: Kbit/s.
        # 
        # >  This parameter is not publicly available.
        self.bandwidth = bandwidth  # type: long
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The description of the replication pair-consistent group. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # The name of the replication pair-consistent group. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. It can contain letters, digits, colons (:), underscores (\_), and hyphens (-).
        self.group_name = group_name  # type: str
        # The RPO of the replication pair-consistent group. Unit: seconds. Valid value: 900.
        self.rpo = rpo  # type: long
        # The region ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.replica_group_id = replica_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.rpo is not None:
            result['RPO'] = self.rpo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        return self


class ModifyDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDiskReplicaGroupResponseBody, self).to_map()
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


class ModifyDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDiskReplicaPairRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, pair_name=None, rpo=None, region_id=None,
                 replica_pair_id=None):
        # The bandwidth value. Unit: Kbit/s.
        # 
        # >  This parameter is not publicly available.
        self.bandwidth = bandwidth  # type: long
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The description of the replication pair.
        self.description = description  # type: str
        # The name of the replication pair.
        self.pair_name = pair_name  # type: str
        # The recovery point objective (RPO) of the replication pair-consistent group. Unit: seconds. Valid value: 900.
        self.rpo = rpo  # type: long
        # The region ID of the primary or secondary disk in the replication pair. You can call the [DescribeRegions](~~354276~~) operation to query the most recent list of regions in which async replication is supported.
        self.region_id = region_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.pair_name is not None:
            result['PairName'] = self.pair_name
        if self.rpo is not None:
            result['RPO'] = self.rpo
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PairName') is not None:
            self.pair_name = m.get('PairName')
        if m.get('RPO') is not None:
            self.rpo = m.get('RPO')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class ModifyDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyDiskReplicaPairResponseBody, self).to_map()
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


class ModifyDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None, replica_pair_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group.
        # 
        # You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.replica_group_id = replica_group_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class RemoveDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveDiskReplicaPairResponseBody, self).to_map()
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


class RemoveDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReprotectDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None, reverse_replicate=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.replica_group_id = replica_group_id  # type: str
        # Specifies whether to enable the reverse replication sub-feature. Valid values: true and false. Default value: true.
        self.reverse_replicate = reverse_replicate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReprotectDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        if self.reverse_replicate is not None:
            result['ReverseReplicate'] = self.reverse_replicate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('ReverseReplicate') is not None:
            self.reverse_replicate = m.get('ReverseReplicate')
        return self


class ReprotectDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReprotectDiskReplicaGroupResponseBody, self).to_map()
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


class ReprotectDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReprotectDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReprotectDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReprotectDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReprotectDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_pair_id=None, reverse_replicate=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the secondary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query region IDs of secondary disks in replication pairs.
        # 
        # >  The reverse replication feature must be enabled from the region where the secondary disk is located.
        self.region_id = region_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str
        # Specifies whether to enable the reverse replication sub-feature. Valid values: true and false. Default value: true.
        self.reverse_replicate = reverse_replicate  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReprotectDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        if self.reverse_replicate is not None:
            result['ReverseReplicate'] = self.reverse_replicate
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        if m.get('ReverseReplicate') is not None:
            self.reverse_replicate = m.get('ReverseReplicate')
        return self


class ReprotectDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ReprotectDiskReplicaPairResponseBody, self).to_map()
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


class ReprotectDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ReprotectDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ReprotectDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReprotectDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDiskMonitorRequest(TeaModel):
    def __init__(self, disk_ids=None, region_id=None):
        # The IDs of the disks for which you want to enable near real-time monitoring.
        self.disk_ids = disk_ids  # type: list[str]
        # The ID of the region in which you want to enable near real-time monitoring for disks. You can call the [DescribeRegions](~~354276~~) operation to query the list of regions that support CloudLens for EBS.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartDiskMonitorShrinkRequest(TeaModel):
    def __init__(self, disk_ids_shrink=None, region_id=None):
        # The IDs of the disks for which you want to enable near real-time monitoring.
        self.disk_ids_shrink = disk_ids_shrink  # type: str
        # The ID of the region in which you want to enable near real-time monitoring for disks. You can call the [DescribeRegions](~~354276~~) operation to query the list of regions that support CloudLens for EBS.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskMonitorShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_ids_shrink is not None:
            result['DiskIds'] = self.disk_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids_shrink = m.get('DiskIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartDiskMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskMonitorResponseBody, self).to_map()
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


class StartDiskMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartDiskMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDiskMonitorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDiskMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, one_shot=None, region_id=None, replica_group_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The ClientToken value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # Specifies whether to immediately synchronize data once. Valid values:
        # 
        # *   true: immediately synchronizes data once.
        # *   false: synchronizes data based on the RPO of the replication pair-consistent group.
        # 
        # Default value: false.
        self.one_shot = one_shot  # type: bool
        # The ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.replica_group_id = replica_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.one_shot is not None:
            result['OneShot'] = self.one_shot
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OneShot') is not None:
            self.one_shot = m.get('OneShot')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        return self


class StartDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskReplicaGroupResponseBody, self).to_map()
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


class StartDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, one_shot=None, region_id=None, replica_pair_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # Specifies whether to immediately synchronize data. Valid values:
        # 
        # *   true: immediately synchronizes data.
        # *   false: synchronizes data based on the recovery point objective (RPO).
        # 
        # Default value: false.
        self.one_shot = one_shot  # type: bool
        # The region ID of the primary or secondary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query the region information of replication pairs.
        self.region_id = region_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.one_shot is not None:
            result['OneShot'] = self.one_shot
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('OneShot') is not None:
            self.one_shot = m.get('OneShot')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class StartDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartDiskReplicaPairResponseBody, self).to_map()
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


class StartDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartPairDrillRequest(TeaModel):
    def __init__(self, client_token=None, pair_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query a list of replication pairs, including replication pair IDs.
        self.pair_id = pair_id  # type: str
        # The region ID of the secondary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query the region in which the secondary disk of the replication pair resides.
        # 
        # >  You must enable the disaster recovery drill feature in the region in which the secondary site resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartPairDrillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.pair_id is not None:
            result['PairId'] = self.pair_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('PairId') is not None:
            self.pair_id = m.get('PairId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartPairDrillResponseBody(TeaModel):
    def __init__(self, drill_id=None, request_id=None):
        # The drill ID.
        self.drill_id = drill_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartPairDrillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartPairDrillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartPairDrillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartPairDrillResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartPairDrillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartReplicaGroupDrillRequest(TeaModel):
    def __init__(self, client_token=None, group_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The ID of the replication pair-consistent group ID. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation the most recent list of async replication pair-consistent groups, including group IDs.
        self.group_id = group_id  # type: str
        # The ID of the region where the secondary site in the replication pair-consistent group is located. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the region where the secondary site in the replication pair-consistent group is located.
        # 
        # >  You must enable the disaster recovery drill feature in the region in which the secondary site resides.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartReplicaGroupDrillRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartReplicaGroupDrillResponseBody(TeaModel):
    def __init__(self, drill_id=None, request_id=None):
        # The drill ID.
        self.drill_id = drill_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartReplicaGroupDrillResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drill_id is not None:
            result['DrillId'] = self.drill_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DrillId') is not None:
            self.drill_id = m.get('DrillId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartReplicaGroupDrillResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartReplicaGroupDrillResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartReplicaGroupDrillResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartReplicaGroupDrillResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDiskMonitorRequest(TeaModel):
    def __init__(self, disk_ids=None, region_id=None):
        # The IDs of the disks for which you want to disable near real-time monitoring.
        self.disk_ids = disk_ids  # type: list[str]
        # The ID of the region in which you want to disable near real-time monitoring for disks. You can call the [DescribeRegions](~~354276~~) operation to query the list of regions that support CloudLens for EBS.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskMonitorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_ids is not None:
            result['DiskIds'] = self.disk_ids
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids = m.get('DiskIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopDiskMonitorShrinkRequest(TeaModel):
    def __init__(self, disk_ids_shrink=None, region_id=None):
        # The IDs of the disks for which you want to disable near real-time monitoring.
        self.disk_ids_shrink = disk_ids_shrink  # type: str
        # The ID of the region in which you want to disable near real-time monitoring for disks. You can call the [DescribeRegions](~~354276~~) operation to query the list of regions that support CloudLens for EBS.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskMonitorShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disk_ids_shrink is not None:
            result['DiskIds'] = self.disk_ids_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DiskIds') is not None:
            self.disk_ids_shrink = m.get('DiskIds')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopDiskMonitorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskMonitorResponseBody, self).to_map()
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


class StopDiskMonitorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopDiskMonitorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDiskMonitorResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDiskMonitorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the replication pair-consistent group.
        self.region_id = region_id  # type: str
        # The ID of the replication pair-consistent group. You can call the [DescribeDiskReplicaGroups](~~426614~~) operation to query the IDs of replication pair-consistent groups.
        self.replica_group_id = replica_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskReplicaGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_group_id is not None:
            result['ReplicaGroupId'] = self.replica_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        return self


class StopDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskReplicaGroupResponseBody, self).to_map()
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


class StopDiskReplicaGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopDiskReplicaGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDiskReplicaGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDiskReplicaGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_pair_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the primary or secondary disk in the replication pair. You can call the [DescribeDiskReplicaPairs](~~354206~~) operation to query the region information of replication pairs.
        self.region_id = region_id  # type: str
        # The ID of the replication pair.
        self.replica_pair_id = replica_pair_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskReplicaPairRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replica_pair_id is not None:
            result['ReplicaPairId'] = self.replica_pair_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaPairId') is not None:
            self.replica_pair_id = m.get('ReplicaPairId')
        return self


class StopDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopDiskReplicaPairResponseBody, self).to_map()
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


class StopDiskReplicaPairResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopDiskReplicaPairResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopDiskReplicaPairResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopDiskReplicaPairResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N to add to the resource. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.key = key  # type: str
        # The value of tag N to add to the resource. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot start with `acs:` or contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
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


class TagResourcesRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, resource_id=None, resource_type=None, tag=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the resource. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID list of the resources. You can specify up to 50 IDs in each request.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Valid values:
        # 
        # *   dedicatedblockstoragecluster: dedicated block storage cluster
        # *   diskreplicapair: replication pair
        # *   diskreplicagroup: replication pair-consistent group
        self.resource_type = resource_type  # type: str
        # The resource tags. You can specify up to 20 tags.
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request. The request ID is returned regardless of whether the call is successful.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindEnterpriseSnapshotPolicyRequest(TeaModel):
    def __init__(self, client_token=None, disk_targets=None, policy_id=None, region_id=None):
        self.client_token = client_token  # type: str
        self.disk_targets = disk_targets  # type: list[str]
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindEnterpriseSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.disk_targets is not None:
            result['DiskTargets'] = self.disk_targets
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DiskTargets') is not None:
            self.disk_targets = m.get('DiskTargets')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UnbindEnterpriseSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnbindEnterpriseSnapshotPolicyResponseBody, self).to_map()
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


class UnbindEnterpriseSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnbindEnterpriseSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnbindEnterpriseSnapshotPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnbindEnterpriseSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, client_token=None, region_id=None, resource_id=None, resource_type=None,
                 tag_key=None):
        # Specifies whether to remove all tags from the resource. This parameter is valid only when the TagKey.N parameter is not specified. Valid values:
        # 
        # *   true: removes all tags from the resource.
        # *   false: does not remove all tags from the resource.
        # 
        # Default value: false.
        self.all = all  # type: bool
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](~~25693~~).
        self.client_token = client_token  # type: str
        # The region ID of the resource. You can call the [DescribeRegions](~~25609~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID list of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Valid values:
        # 
        # *   dedicatedblockstoragecluster: dedicated block storage cluster
        # *   diskreplicapair: the replication pair.
        # *   diskreplicagroup: replication pair-consistent group
        self.resource_type = resource_type  # type: str
        # The list of tag keys. You can specify up to 20 tag keys in the list.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request. The request ID is returned regardless of whether the call is successful.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions(TeaModel):
    def __init__(self, region_id=None, retain_days=None):
        self.region_id = region_id  # type: str
        self.retain_days = retain_days  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_days is not None:
            result['RetainDays'] = self.retain_days
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainDays') is not None:
            self.retain_days = m.get('RetainDays')
        return self


class UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo(TeaModel):
    def __init__(self, enabled=None, regions=None):
        self.enabled = enabled  # type: bool
        self.regions = regions  # type: list[UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions]

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfoRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class UpdateEnterpriseSnapshotPolicyRequestRetainRule(TeaModel):
    def __init__(self, number=None, time_interval=None, time_unit=None):
        self.number = number  # type: int
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestRetainRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.number is not None:
            result['Number'] = self.number
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class UpdateEnterpriseSnapshotPolicyRequestSchedule(TeaModel):
    def __init__(self, cron_expression=None):
        self.cron_expression = cron_expression  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestSchedule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cron_expression is not None:
            result['CronExpression'] = self.cron_expression
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CronExpression') is not None:
            self.cron_expression = m.get('CronExpression')
        return self


class UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules(TeaModel):
    def __init__(self, special_period_unit=None, time_interval=None, time_unit=None):
        self.special_period_unit = special_period_unit  # type: str
        self.time_interval = time_interval  # type: int
        self.time_unit = time_unit  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.special_period_unit is not None:
            result['SpecialPeriodUnit'] = self.special_period_unit
        if self.time_interval is not None:
            result['TimeInterval'] = self.time_interval
        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SpecialPeriodUnit') is not None:
            self.special_period_unit = m.get('SpecialPeriodUnit')
        if m.get('TimeInterval') is not None:
            self.time_interval = m.get('TimeInterval')
        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')
        return self


class UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules(TeaModel):
    def __init__(self, enabled=None, rules=None):
        self.enabled = enabled  # type: bool
        self.rules = rules  # type: list[UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules]

    def validate(self):
        if self.rules:
            for k in self.rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRulesRules()
                self.rules.append(temp_model.from_map(k))
        return self


class UpdateEnterpriseSnapshotPolicyRequestStorageRule(TeaModel):
    def __init__(self, enable_immediate_access=None):
        self.enable_immediate_access = enable_immediate_access  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequestStorageRule, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_immediate_access is not None:
            result['EnableImmediateAccess'] = self.enable_immediate_access
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableImmediateAccess') is not None:
            self.enable_immediate_access = m.get('EnableImmediateAccess')
        return self


class UpdateEnterpriseSnapshotPolicyRequest(TeaModel):
    def __init__(self, client_token=None, cross_region_copy_info=None, desc=None, name=None, policy_id=None,
                 region_id=None, retain_rule=None, schedule=None, special_retain_rules=None, state=None, storage_rule=None):
        self.client_token = client_token  # type: str
        self.cross_region_copy_info = cross_region_copy_info  # type: UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str
        self.retain_rule = retain_rule  # type: UpdateEnterpriseSnapshotPolicyRequestRetainRule
        self.schedule = schedule  # type: UpdateEnterpriseSnapshotPolicyRequestSchedule
        self.special_retain_rules = special_retain_rules  # type: UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules
        self.state = state  # type: str
        self.storage_rule = storage_rule  # type: UpdateEnterpriseSnapshotPolicyRequestStorageRule

    def validate(self):
        if self.cross_region_copy_info:
            self.cross_region_copy_info.validate()
        if self.retain_rule:
            self.retain_rule.validate()
        if self.schedule:
            self.schedule.validate()
        if self.special_retain_rules:
            self.special_retain_rules.validate()
        if self.storage_rule:
            self.storage_rule.validate()

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cross_region_copy_info is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info.to_map()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_rule is not None:
            result['RetainRule'] = self.retain_rule.to_map()
        if self.schedule is not None:
            result['Schedule'] = self.schedule.to_map()
        if self.special_retain_rules is not None:
            result['SpecialRetainRules'] = self.special_retain_rules.to_map()
        if self.state is not None:
            result['State'] = self.state
        if self.storage_rule is not None:
            result['StorageRule'] = self.storage_rule.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CrossRegionCopyInfo') is not None:
            temp_model = UpdateEnterpriseSnapshotPolicyRequestCrossRegionCopyInfo()
            self.cross_region_copy_info = temp_model.from_map(m['CrossRegionCopyInfo'])
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainRule') is not None:
            temp_model = UpdateEnterpriseSnapshotPolicyRequestRetainRule()
            self.retain_rule = temp_model.from_map(m['RetainRule'])
        if m.get('Schedule') is not None:
            temp_model = UpdateEnterpriseSnapshotPolicyRequestSchedule()
            self.schedule = temp_model.from_map(m['Schedule'])
        if m.get('SpecialRetainRules') is not None:
            temp_model = UpdateEnterpriseSnapshotPolicyRequestSpecialRetainRules()
            self.special_retain_rules = temp_model.from_map(m['SpecialRetainRules'])
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StorageRule') is not None:
            temp_model = UpdateEnterpriseSnapshotPolicyRequestStorageRule()
            self.storage_rule = temp_model.from_map(m['StorageRule'])
        return self


class UpdateEnterpriseSnapshotPolicyShrinkRequest(TeaModel):
    def __init__(self, client_token=None, cross_region_copy_info_shrink=None, desc=None, name=None, policy_id=None,
                 region_id=None, retain_rule_shrink=None, schedule_shrink=None, special_retain_rules_shrink=None, state=None,
                 storage_rule_shrink=None):
        self.client_token = client_token  # type: str
        self.cross_region_copy_info_shrink = cross_region_copy_info_shrink  # type: str
        self.desc = desc  # type: str
        self.name = name  # type: str
        self.policy_id = policy_id  # type: str
        self.region_id = region_id  # type: str
        self.retain_rule_shrink = retain_rule_shrink  # type: str
        self.schedule_shrink = schedule_shrink  # type: str
        self.special_retain_rules_shrink = special_retain_rules_shrink  # type: str
        self.state = state  # type: str
        self.storage_rule_shrink = storage_rule_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cross_region_copy_info_shrink is not None:
            result['CrossRegionCopyInfo'] = self.cross_region_copy_info_shrink
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.retain_rule_shrink is not None:
            result['RetainRule'] = self.retain_rule_shrink
        if self.schedule_shrink is not None:
            result['Schedule'] = self.schedule_shrink
        if self.special_retain_rules_shrink is not None:
            result['SpecialRetainRules'] = self.special_retain_rules_shrink
        if self.state is not None:
            result['State'] = self.state
        if self.storage_rule_shrink is not None:
            result['StorageRule'] = self.storage_rule_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CrossRegionCopyInfo') is not None:
            self.cross_region_copy_info_shrink = m.get('CrossRegionCopyInfo')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RetainRule') is not None:
            self.retain_rule_shrink = m.get('RetainRule')
        if m.get('Schedule') is not None:
            self.schedule_shrink = m.get('Schedule')
        if m.get('SpecialRetainRules') is not None:
            self.special_retain_rules_shrink = m.get('SpecialRetainRules')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('StorageRule') is not None:
            self.storage_rule_shrink = m.get('StorageRule')
        return self


class UpdateEnterpriseSnapshotPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyResponseBody, self).to_map()
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


class UpdateEnterpriseSnapshotPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateEnterpriseSnapshotPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateEnterpriseSnapshotPolicyResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateEnterpriseSnapshotPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


