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
        # Id of the request
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


class CreateDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, destination_region_id=None, destination_zone_id=None,
                 group_name=None, rpo=None, region_id=None, source_zone_id=None):
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
        # Id of the request
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
        # Id of the request
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


class DescribeDiskReplicaGroupsRequest(TeaModel):
    def __init__(self, group_ids=None, max_results=None, next_token=None, region_id=None, site=None):
        self.group_ids = group_ids  # type: str
        self.max_results = max_results  # type: long
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        # production或backup，表示数据从主或备站点获取，默认为production。
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Site') is not None:
            self.site = m.get('Site')
        return self


class DescribeDiskReplicaGroupsResponseBodyReplicaGroups(TeaModel):
    def __init__(self, description=None, destination_region_id=None, destination_zone_id=None, group_name=None,
                 last_recover_point=None, pair_ids=None, pair_number=None, rpo=None, replica_group_id=None, site=None,
                 source_region_id=None, source_zone_id=None, status=None):
        self.description = description  # type: str
        self.destination_region_id = destination_region_id  # type: str
        self.destination_zone_id = destination_zone_id  # type: str
        self.group_name = group_name  # type: str
        self.last_recover_point = last_recover_point  # type: long
        self.pair_ids = pair_ids  # type: list[bytes]
        # 复制组中的复制对个数
        self.pair_number = pair_number  # type: long
        self.rpo = rpo  # type: long
        self.replica_group_id = replica_group_id  # type: str
        # pair信息的后端站点来源，production或backup
        self.site = site  # type: str
        self.source_region_id = source_region_id  # type: str
        self.source_zone_id = source_zone_id  # type: str
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeDiskReplicaGroupsResponseBodyReplicaGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class DescribeDiskReplicaGroupsResponseBody(TeaModel):
    def __init__(self, next_token=None, replica_groups=None, request_id=None):
        self.next_token = next_token  # type: str
        self.replica_groups = replica_groups  # type: list[DescribeDiskReplicaGroupsResponseBodyReplicaGroups]
        # Id of the request
        self.request_id = request_id  # type: str

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
        result['ReplicaGroups'] = []
        if self.replica_groups is not None:
            for k in self.replica_groups:
                result['ReplicaGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.replica_groups = []
        if m.get('ReplicaGroups') is not None:
            for k in m.get('ReplicaGroups'):
                temp_model = DescribeDiskReplicaGroupsResponseBodyReplicaGroups()
                self.replica_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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


class DescribeDiskReplicaPairsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, pair_ids=None, region_id=None, replica_group_id=None,
                 site=None):
        # 分页查询时每页的最大条目数。取值范围：1~500
        # 
        # 默认值：10
        self.max_results = max_results  # type: long
        # 查询凭证（Token）。取值为上一次调用该接口返回的NextToken参数值，初次调用接口时无需设置该参数。
        self.next_token = next_token  # type: str
        # 异步复制关系ID列表。您可以指定一个或多个异步复制关系ID进行查询。格式为：pair-cn-dsa****,pair-cn-asd****。
        # 
        # 默认值为空，表示查询当前地域下所有的异步复制关系。
        self.pair_ids = pair_ids  # type: str
        self.region_id = region_id  # type: str
        # 所属复制组id。
        self.replica_group_id = replica_group_id  # type: str
        # production或backup，表示获取本地为主站点或备站点的复制对数据，默认为production。
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
        # 异步复制时使用的带宽。单位为Kbps。
        self.bandwidth = bandwidth  # type: long
        # 付费类型。PREPAY：预付费；POSTPAY：后付费。
        self.charge_type = charge_type  # type: str
        # 创建时间。1970年1月1日0点0分以来的秒数。
        self.create_time = create_time  # type: long
        self.description = description  # type: str
        self.destination_disk_id = destination_disk_id  # type: str
        self.destination_region = destination_region  # type: str
        # 从盘所属的可用区。
        self.destination_zone_id = destination_zone_id  # type: str
        self.expired_time = expired_time  # type: long
        # 最近一次异步复制操作完成的时间。该参数以时间戳的形式提供返回值。单位为秒。
        self.last_recover_point = last_recover_point  # type: long
        self.pair_name = pair_name  # type: str
        # 复制对的初始源地域。
        self.primary_region = primary_region  # type: str
        # 复制对的初始源可用区。
        self.primary_zone = primary_zone  # type: str
        # 复制对的RPO值。单位为秒。
        self.rpo = rpo  # type: long
        # 所属复制组id。
        self.replica_group_id = replica_group_id  # type: str
        # 所属复制组名称。
        self.replica_group_name = replica_group_name  # type: str
        self.replica_pair_id = replica_pair_id  # type: str
        # 复制对信息的后端站点来源，production或backup。
        self.site = site  # type: str
        self.source_disk_id = source_disk_id  # type: str
        self.source_region = source_region  # type: str
        # 主盘所属的可用区。
        self.source_zone_id = source_zone_id  # type: str
        # 复制对的初始目的地域。
        self.standby_region = standby_region  # type: str
        # 复制对的初始目的可用区。
        self.standby_zone = standby_zone  # type: str
        # 异步复制关系的状态。可能值：
        # 
        # - invalid：失效。该状态表示异步复制关系存在异常。
        # - creating：创建中。
        # - created：已创建。
        # - create_failed：创建失败。
        # - initial_syncing：初始同步中。异步复制在创建并启动后，主盘数据初次异步复制到从盘的过程中，将处于该状态。
        # - syncing：同步中。主盘和从盘之间非第一次进行异步复制数据时，将处于该状态。
        # - manual_syncing：单次同步中。单次同步，同步完成后恢复到stopped状态。如果是第一次单次同步，则同步中也显示为状态manual_syncing。
        # - normal：正常。当异步复制的当前周期内数据复制完成时，将处于该状态。
        # - stopping：停止中。
        # - stopped：已停止。
        # - stop_failed：停止失败。
        # - failovering：故障切换中。
        # - failovered：故障切换完成。
        # - failover_failed：故障切换失败。
        # - reprotecting：反向复制操作中。
        # - reprotect_failed：反向复制失败。
        # - deleting：删除中。
        # - delete_failed：删除失败。
        # - deleted：已删除。
        self.status = status  # type: str
        # 复制对的状态提示信息。比如invalid时，可能值：DeviceRemoved：主盘或者从盘被删除。DeviceKeyChanged：主盘或从盘的DeviceKey映射发生变化。
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
    def __init__(self, next_token=None, replica_pairs=None, request_id=None):
        self.next_token = next_token  # type: str
        self.replica_pairs = replica_pairs  # type: list[DescribeDiskReplicaPairsResponseBodyReplicaPairs]
        # Id of the request
        self.request_id = request_id  # type: str

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
        result['ReplicaPairs'] = []
        if self.replica_pairs is not None:
            for k in self.replica_pairs:
                result['ReplicaPairs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.replica_pairs = []
        if m.get('ReplicaPairs') is not None:
            for k in m.get('ReplicaPairs'):
                temp_model = DescribeDiskReplicaPairsResponseBodyReplicaPairs()
                self.replica_pairs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
    def __init__(self, local_name=None, zone_id=None):
        self.local_name = local_name  # type: str
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
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
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
        # Id of the request
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
        # Id of the request
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
        # Id of the request
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


class ModifyDiskReplicaGroupRequest(TeaModel):
    def __init__(self, client_token=None, description=None, group_name=None, rpo=None, region_id=None,
                 replica_group_id=None):
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
        # Id of the request
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
        # Id of the request
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
        # Id of the request
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
    def __init__(self, client_token=None, region_id=None, replica_group_id=None, source_region_id=None,
                 source_zone_id=None):
        self.client_token = client_token  # type: str
        self.region_id = region_id  # type: str
        self.replica_group_id = replica_group_id  # type: str
        self.source_region_id = source_region_id  # type: str
        self.source_zone_id = source_zone_id  # type: str

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
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id
        if self.source_zone_id is not None:
            result['SourceZoneId'] = self.source_zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplicaGroupId') is not None:
            self.replica_group_id = m.get('ReplicaGroupId')
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')
        if m.get('SourceZoneId') is not None:
            self.source_zone_id = m.get('SourceZoneId')
        return self


class ReprotectDiskReplicaGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
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
        # Id of the request
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
        # Id of the request
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
        # Id of the request
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
        # Id of the request
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
        # Id of the request
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


