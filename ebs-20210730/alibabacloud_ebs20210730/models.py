# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddDiskReplicaPairRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None, replica_pair_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.replica_group_id = replica_group_id  # type: str
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


class CancelLensServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
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


class CreateDedicatedBlockStorageClusterRequest(TeaModel):
    def __init__(self, azone=None, capacity=None, dbsc_id=None, dbsc_name=None, region_id=None,
                 resource_group_id=None, type=None):
        self.azone = azone  # type: str
        self.capacity = capacity  # type: long
        self.dbsc_id = dbsc_id  # type: str
        self.dbsc_name = dbsc_name  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.type = type  # type: str

    def validate(self):
        pass

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateDedicatedBlockStorageClusterResponseBody(TeaModel):
    def __init__(self, dbsc_id=None, order_id=None, request_id=None):
        self.dbsc_id = dbsc_id  # type: str
        self.order_id = order_id  # type: str
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


class CreateDiskReplicaGroupRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, destination_region_id=None,
                 destination_zone_id=None, group_name=None, rpo=None, region_id=None, source_zone_id=None):
        self.bandwidth = bandwidth  # type: long
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination_region_id = destination_region_id  # type: str
        self.destination_zone_id = destination_zone_id  # type: str
        self.group_name = group_name  # type: str
        self.rpo = rpo  # type: long
        self.region_id = region_id  # type: str
        self.source_zone_id = source_zone_id  # type: str

    def validate(self):
        pass

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
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
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
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        return self


class CreateDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, replica_group_id=None, request_id=None):
        self.replica_group_id = replica_group_id  # type: str
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


class CreateDiskReplicaPairRequest(TeaModel):
    def __init__(self, bandwidth=None, charge_type=None, client_token=None, description=None,
                 destination_disk_id=None, destination_region_id=None, destination_zone_id=None, disk_id=None, pair_name=None,
                 period=None, period_unit=None, rpo=None, region_id=None, source_zone_id=None):
        self.bandwidth = bandwidth  # type: long
        self.charge_type = charge_type  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.destination_disk_id = destination_disk_id  # type: str
        self.destination_region_id = destination_region_id  # type: str
        self.destination_zone_id = destination_zone_id  # type: str
        self.disk_id = disk_id  # type: str
        self.pair_name = pair_name  # type: str
        self.period = period  # type: long
        self.period_unit = period_unit  # type: str
        self.rpo = rpo  # type: long
        self.region_id = region_id  # type: str
        self.source_zone_id = source_zone_id  # type: str

    def validate(self):
        pass

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
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
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
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        return self


class CreateDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, order_id=None, replica_pair_id=None, request_id=None):
        self.order_id = order_id  # type: str
        self.replica_pair_id = replica_pair_id  # type: str
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


class DeleteDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
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
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
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


class DescribeDedicatedBlockStorageClusterDisksRequest(TeaModel):
    def __init__(self, dbsc_id=None, max_results=None, next_token=None, region_id=None):
        self.dbsc_id = dbsc_id  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
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
        self.tag_key = tag_key  # type: str
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
    def __init__(self, attached_time=None, bdf_id=None, category=None, delete_auto_snapshot=None,
                 delete_with_instance=None, description=None, detached_time=None, device=None, disk_charge_type=None, disk_id=None,
                 disk_name=None, enable_auto_snapshot=None, encrypted=None, iops=None, image_id=None, instance_id=None,
                 kmskey_id=None, mount_instance_num=None, multi_attach=None, performance_level=None, portable=None,
                 region_id=None, size=None, source_snapshot_id=None, status=None, storage_cluster_id=None,
                 storage_set_id=None, storage_set_partition_number=None, tags=None, type=None, zone_id=None):
        self.attached_time = attached_time  # type: str
        self.bdf_id = bdf_id  # type: str
        self.category = category  # type: str
        self.delete_auto_snapshot = delete_auto_snapshot  # type: bool
        self.delete_with_instance = delete_with_instance  # type: bool
        self.description = description  # type: str
        self.detached_time = detached_time  # type: str
        self.device = device  # type: str
        self.disk_charge_type = disk_charge_type  # type: str
        self.disk_id = disk_id  # type: str
        self.disk_name = disk_name  # type: str
        self.enable_auto_snapshot = enable_auto_snapshot  # type: bool
        self.encrypted = encrypted  # type: bool
        self.iops = iops  # type: long
        self.image_id = image_id  # type: str
        self.instance_id = instance_id  # type: str
        self.kmskey_id = kmskey_id  # type: str
        self.mount_instance_num = mount_instance_num  # type: int
        self.multi_attach = multi_attach  # type: str
        self.performance_level = performance_level  # type: str
        self.portable = portable  # type: bool
        self.region_id = region_id  # type: str
        self.size = size  # type: int
        self.source_snapshot_id = source_snapshot_id  # type: str
        self.status = status  # type: str
        self.storage_cluster_id = storage_cluster_id  # type: str
        self.storage_set_id = storage_set_id  # type: str
        self.storage_set_partition_number = storage_set_partition_number  # type: int
        self.tags = tags  # type: list[DescribeDedicatedBlockStorageClusterDisksResponseBodyDisksDiskTags]
        self.type = type  # type: str
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
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks(TeaModel):
    def __init__(self, disk=None):
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
        self.disks = disks  # type: DescribeDedicatedBlockStorageClusterDisksResponseBodyDisks
        self.next_token = next_token  # type: str
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
        self.key = key  # type: str
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
        self.azone_id = azone_id  # type: str
        self.category = category  # type: str
        self.client_token = client_token  # type: str
        self.dedicated_block_storage_cluster_id = dedicated_block_storage_cluster_id  # type: list[str]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: list[str]
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
    def __init__(self, available_capacity=None, delivery_capacity=None, total_capacity=None, used_capacity=None):
        self.available_capacity = available_capacity  # type: long
        self.delivery_capacity = delivery_capacity  # type: long
        self.total_capacity = total_capacity  # type: long
        self.used_capacity = used_capacity  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.available_capacity is not None:
            result['AvailableCapacity'] = self.available_capacity
        if self.delivery_capacity is not None:
            result['DeliveryCapacity'] = self.delivery_capacity
        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity
        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AvailableCapacity') is not None:
            self.available_capacity = m.get('AvailableCapacity')
        if m.get('DeliveryCapacity') is not None:
            self.delivery_capacity = m.get('DeliveryCapacity')
        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')
        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')
        return self


class DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        self.tag_key = tag_key  # type: str
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
    def __init__(self, category=None, create_time=None, dedicated_block_storage_cluster_capacity=None,
                 dedicated_block_storage_cluster_id=None, dedicated_block_storage_cluster_name=None, description=None, expired_time=None,
                 performance_level=None, region_id=None, resource_group_id=None, status=None, supported_category=None, tags=None,
                 type=None, zone_id=None):
        self.category = category  # type: str
        self.create_time = create_time  # type: str
        self.dedicated_block_storage_cluster_capacity = dedicated_block_storage_cluster_capacity  # type: DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersDedicatedBlockStorageClusterCapacity
        self.dedicated_block_storage_cluster_id = dedicated_block_storage_cluster_id  # type: str
        self.dedicated_block_storage_cluster_name = dedicated_block_storage_cluster_name  # type: str
        self.description = description  # type: str
        self.expired_time = expired_time  # type: str
        self.performance_level = performance_level  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.supported_category = supported_category  # type: str
        self.tags = tags  # type: list[DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClustersTags]
        self.type = type  # type: str
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
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
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
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
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
        self.dedicated_block_storage_clusters = dedicated_block_storage_clusters  # type: list[DescribeDedicatedBlockStorageClustersResponseBodyDedicatedBlockStorageClusters]
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
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
        self.disk_category = disk_category  # type: str
        self.disk_id = disk_id  # type: str
        self.end_time = end_time  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str
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
        self.description = description  # type: str
        self.disk_id = disk_id  # type: str
        self.recommend_action = recommend_action  # type: str
        self.region_id = region_id  # type: str
        self.status = status  # type: str
        self.timestamp = timestamp  # type: str
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
        self.disk_events = disk_events  # type: list[DescribeDiskEventsResponseBodyDiskEvents]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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
        self.disk_id = disk_id  # type: str
        self.end_time = end_time  # type: str
        self.period = period  # type: long
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str
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
        self.bpspercent = bpspercent  # type: long
        self.burst_iocount = burst_iocount  # type: long
        self.disk_id = disk_id  # type: str
        self.iopspercent = iopspercent  # type: long
        self.read_bps = read_bps  # type: long
        self.read_iops = read_iops  # type: long
        self.timestamp = timestamp  # type: str
        self.write_bps = write_bps  # type: long
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
        self.monitor_data = monitor_data  # type: list[DescribeDiskMonitorDataResponseBodyMonitorData]
        self.request_id = request_id  # type: str
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
        self.disk_ids = disk_ids  # type: str
        self.end_time = end_time  # type: str
        self.max_results = max_results  # type: str
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.start_time = start_time  # type: str
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
        self.burst_iocount = burst_iocount  # type: long
        self.disk_id = disk_id  # type: str
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
        self.monitor_data = monitor_data  # type: list[DescribeDiskMonitorDataListResponseBodyMonitorData]
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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


class DescribeDiskReplicaGroupsRequest(TeaModel):
    def __init__(self, group_ids=None, max_results=None, next_token=None, page_number=None, page_size=None,
                 region_id=None, site=None):
        self.group_ids = group_ids  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.site = site  # type: str

    def validate(self):
        pass

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
        if self.site is not None:
            result['Site'] = self.site
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
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class DescribeDiskReplicaGroupsResponseBodyReplicaGroups(TeaModel):
    def __init__(self, bandwidth=None, description=None, destination_region_id=None, destination_zone_id=None,
                 group_name=None, last_recover_point=None, pair_ids=None, pair_number=None, primary_region=None,
                 primary_zone=None, rpo=None, replica_group_id=None, site=None, source_region_id=None, source_zone_id=None,
                 standby_region=None, standby_zone=None, status=None):
        self.bandwidth = bandwidth  # type: long
        self.description = description  # type: str
        self.destination_region_id = destination_region_id  # type: str
        self.destination_zone_id = destination_zone_id  # type: str
        self.group_name = group_name  # type: str
        self.last_recover_point = last_recover_point  # type: long
        self.pair_ids = pair_ids  # type: list[bytes]
        self.pair_number = pair_number  # type: long
        self.primary_region = primary_region  # type: str
        self.primary_zone = primary_zone  # type: str
        self.rpo = rpo  # type: long
        self.replica_group_id = replica_group_id  # type: str
        self.site = site  # type: str
        self.source_region_id = source_region_id  # type: str
        self.source_zone_id = source_zone_id  # type: str
        self.standby_region = standby_region  # type: str
        self.standby_zone = standby_zone  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

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
        return self


class DescribeDiskReplicaGroupsResponseBody(TeaModel):
    def __init__(self, next_token=None, page_number=None, page_size=None, replica_groups=None, request_id=None,
                 total_count=None):
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.replica_groups = replica_groups  # type: list[DescribeDiskReplicaGroupsResponseBodyReplicaGroups]
        self.request_id = request_id  # type: str
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
        self.region_id = region_id  # type: str
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
        self.progress = progress  # type: int
        self.recover_point = recover_point  # type: long
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


class DescribeDiskReplicaPairsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, page_number=None, page_size=None, pair_ids=None,
                 region_id=None, replica_group_id=None, site=None):
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.pair_ids = pair_ids  # type: str
        self.region_id = region_id  # type: str
        self.replica_group_id = replica_group_id  # type: str
        self.site = site  # type: str

    def validate(self):
        pass

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
        if self.site is not None:
            result['Site'] = self.site
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
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class DescribeDiskReplicaPairsResponseBodyReplicaPairs(TeaModel):
    def __init__(self, bandwidth=None, charge_type=None, create_time=None, description=None,
                 destination_disk_id=None, destination_region=None, destination_zone_id=None, expired_time=None,
                 last_recover_point=None, pair_name=None, primary_region=None, primary_zone=None, rpo=None, replica_group_id=None,
                 replica_group_name=None, replica_pair_id=None, site=None, source_disk_id=None, source_region=None,
                 source_zone_id=None, standby_region=None, standby_zone=None, status=None, status_message=None):
        self.bandwidth = bandwidth  # type: long
        self.charge_type = charge_type  # type: str
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.destination_disk_id = destination_disk_id  # type: str
        self.destination_region = destination_region  # type: str
        self.destination_zone_id = destination_zone_id  # type: str
        self.expired_time = expired_time  # type: long
        self.last_recover_point = last_recover_point  # type: long
        self.pair_name = pair_name  # type: str
        self.primary_region = primary_region  # type: str
        self.primary_zone = primary_zone  # type: str
        self.rpo = rpo  # type: long
        self.replica_group_id = replica_group_id  # type: str
        self.replica_group_name = replica_group_name  # type: str
        self.replica_pair_id = replica_pair_id  # type: str
        self.site = site  # type: str
        self.source_disk_id = source_disk_id  # type: str
        self.source_region = source_region  # type: str
        self.source_zone_id = source_zone_id  # type: str
        self.standby_region = standby_region  # type: str
        self.standby_zone = standby_zone  # type: str
        self.status = status  # type: str
        self.status_message = status_message  # type: str

    def validate(self):
        pass

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
        return self


class DescribeDiskReplicaPairsResponseBody(TeaModel):
    def __init__(self, next_token=None, page_number=None, page_size=None, replica_pairs=None, request_id=None,
                 total_count=None):
        self.next_token = next_token  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.replica_pairs = replica_pairs  # type: list[DescribeDiskReplicaPairsResponseBodyReplicaPairs]
        self.request_id = request_id  # type: str
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


class DescribeLensServiceStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        self.request_id = request_id  # type: str
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


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, region_id=None, resource_type=None):
        self.accept_language = accept_language  # type: str
        self.region_id = region_id  # type: str
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
        self.local_name = local_name  # type: str
        self.resource_types = resource_types  # type: list[str]
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
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str
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
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
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


class FailoverDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, region_id=None, replica_group_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
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
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
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
        self.key = key  # type: str
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
        self.client_token = client_token  # type: str
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
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
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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
        self.client_token = client_token  # type: str
        self.dbsc_id = dbsc_id  # type: str
        self.dbsc_name = dbsc_name  # type: str
        self.description = description  # type: str
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
        self.bandwidth = bandwidth  # type: long
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.group_name = group_name  # type: str
        self.rpo = rpo  # type: long
        self.region_id = region_id  # type: str
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
        self.bandwidth = bandwidth  # type: long
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.pair_name = pair_name  # type: str
        self.rpo = rpo  # type: long
        self.region_id = region_id  # type: str
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
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.replica_group_id = replica_group_id  # type: str
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
    def __init__(self, client_token=None, region_id=None, replica_group_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.replica_group_id = replica_group_id  # type: str

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


class ReprotectDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
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
    def __init__(self, client_token=None, region_id=None, replica_pair_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.replica_pair_id = replica_pair_id  # type: str

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


class ReprotectDiskReplicaPairResponseBody(TeaModel):
    def __init__(self, request_id=None):
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
        self.disk_ids = disk_ids  # type: list[str]
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
        self.disk_ids_shrink = disk_ids_shrink  # type: str
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
        self.client_token = client_token  # type: str
        self.one_shot = one_shot  # type: bool
        self.region_id = region_id  # type: str
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
        self.client_token = client_token  # type: str
        self.one_shot = one_shot  # type: bool
        self.region_id = region_id  # type: str
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


class StopDiskMonitorRequest(TeaModel):
    def __init__(self, disk_ids=None, region_id=None):
        self.disk_ids = disk_ids  # type: list[str]
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
        self.disk_ids_shrink = disk_ids_shrink  # type: str
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
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
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
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
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
        self.key = key  # type: str
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
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, client_token=None, region_id=None, resource_id=None, resource_type=None,
                 tag_key=None):
        self.all = all  # type: bool
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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


