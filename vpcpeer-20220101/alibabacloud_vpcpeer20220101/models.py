# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, resource_owner_account=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.instance_id = instance_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptVpcPeerConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class AcceptVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptVpcPeerConnectionResponseBody, self).to_map()
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


class AcceptVpcPeerConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AcceptVpcPeerConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptVpcPeerConnectionResponse, self).to_map()
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
            temp_model = AcceptVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcPeerConnectionRequest(TeaModel):
    def __init__(self, accepting_ali_uid=None, accepting_region_id=None, accepting_vpc_id=None, client_token=None,
                 description=None, dry_run=None, name=None, region_id=None, vpc_id=None):
        self.accepting_ali_uid = accepting_ali_uid  # type: long
        self.accepting_region_id = accepting_region_id  # type: str
        self.accepting_vpc_id = accepting_vpc_id  # type: str
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcPeerConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepting_ali_uid is not None:
            result['AcceptingAliUid'] = self.accepting_ali_uid
        if self.accepting_region_id is not None:
            result['AcceptingRegionId'] = self.accepting_region_id
        if self.accepting_vpc_id is not None:
            result['AcceptingVpcId'] = self.accepting_vpc_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptingAliUid') is not None:
            self.accepting_ali_uid = m.get('AcceptingAliUid')
        if m.get('AcceptingRegionId') is not None:
            self.accepting_region_id = m.get('AcceptingRegionId')
        if m.get('AcceptingVpcId') is not None:
            self.accepting_vpc_id = m.get('AcceptingVpcId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcPeerConnectionResponseBody, self).to_map()
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


class CreateVpcPeerConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateVpcPeerConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcPeerConnectionResponse, self).to_map()
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
            temp_model = CreateVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, force=None, instance_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        # 是否强删
        self.force = force  # type: bool
        self.instance_id = instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcPeerConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.force is not None:
            result['Force'] = self.force
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcPeerConnectionResponseBody, self).to_map()
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


class DeleteVpcPeerConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteVpcPeerConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcPeerConnectionResponse, self).to_map()
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
            temp_model = DeleteVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcPeerConnectionAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, resource_owner_account=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.instance_id = instance_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs
        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')
        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetVpcPeerConnectionAttributeResponseBodyVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeResponseBodyVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs
        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')
        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class GetVpcPeerConnectionAttributeResponseBody(TeaModel):
    def __init__(self, accepting_owner_uid=None, accepting_region_id=None, accepting_vpc=None, bandwidth=None,
                 biz_status=None, description=None, gmt_create=None, gmt_expired=None, gmt_modified=None, instance_id=None,
                 name=None, owner_id=None, region_id=None, request_id=None, resource_group_id=None, status=None, vpc=None):
        self.accepting_owner_uid = accepting_owner_uid  # type: long
        self.accepting_region_id = accepting_region_id  # type: str
        self.accepting_vpc = accepting_vpc  # type: GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc
        self.bandwidth = bandwidth  # type: int
        self.biz_status = biz_status  # type: str
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_expired = gmt_expired  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: long
        self.region_id = region_id  # type: str
        self.request_id = request_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.vpc = vpc  # type: GetVpcPeerConnectionAttributeResponseBodyVpc

    def validate(self):
        if self.accepting_vpc:
            self.accepting_vpc.validate()
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepting_owner_uid is not None:
            result['AcceptingOwnerUid'] = self.accepting_owner_uid
        if self.accepting_region_id is not None:
            result['AcceptingRegionId'] = self.accepting_region_id
        if self.accepting_vpc is not None:
            result['AcceptingVpc'] = self.accepting_vpc.to_map()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc is not None:
            result['Vpc'] = self.vpc.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptingOwnerUid') is not None:
            self.accepting_owner_uid = m.get('AcceptingOwnerUid')
        if m.get('AcceptingRegionId') is not None:
            self.accepting_region_id = m.get('AcceptingRegionId')
        if m.get('AcceptingVpc') is not None:
            temp_model = GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc()
            self.accepting_vpc = temp_model.from_map(m['AcceptingVpc'])
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vpc') is not None:
            temp_model = GetVpcPeerConnectionAttributeResponseBodyVpc()
            self.vpc = temp_model.from_map(m['Vpc'])
        return self


class GetVpcPeerConnectionAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVpcPeerConnectionAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeResponse, self).to_map()
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
            temp_model = GetVpcPeerConnectionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcPeerConnectionsRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, max_results=None, name=None,
                 next_token=None, region_id=None, vpc_id=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.instance_id = instance_id  # type: str
        self.max_results = max_results  # type: int
        self.name = name  # type: str
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        # 根据两端vpcid过滤，不区分发起端和接收端。如果只传入一个，则根据一端过滤
        self.vpc_id = vpc_id  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcPeerConnectionsShrinkRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, max_results=None, name=None,
                 next_token=None, region_id=None, vpc_id_shrink=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.instance_id = instance_id  # type: str
        self.max_results = max_results  # type: int
        self.name = name  # type: str
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        # 根据两端vpcid过滤，不区分发起端和接收端。如果只传入一个，则根据一端过滤
        self.vpc_id_shrink = vpc_id_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.name is not None:
            result['Name'] = self.name
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id_shrink is not None:
            result['VpcId'] = self.vpc_id_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id_shrink = m.get('VpcId')
        return self


class ListVpcPeerConnectionsResponseBodyVpcPeerConnectsAcceptingVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponseBodyVpcPeerConnectsAcceptingVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs
        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')
        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ipv_4cidrs is not None:
            result['Ipv4Cidrs'] = self.ipv_4cidrs
        if self.ipv_6cidrs is not None:
            result['Ipv6Cidrs'] = self.ipv_6cidrs
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ipv4Cidrs') is not None:
            self.ipv_4cidrs = m.get('Ipv4Cidrs')
        if m.get('Ipv6Cidrs') is not None:
            self.ipv_6cidrs = m.get('Ipv6Cidrs')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcPeerConnectionsResponseBodyVpcPeerConnects(TeaModel):
    def __init__(self, accepting_owner_uid=None, accepting_region_id=None, accepting_vpc=None, bandwidth=None,
                 biz_status=None, description=None, gmt_create=None, gmt_expired=None, gmt_modified=None, instance_id=None,
                 name=None, owner_id=None, region_id=None, resource_group_id=None, status=None, vpc=None):
        self.accepting_owner_uid = accepting_owner_uid  # type: int
        self.accepting_region_id = accepting_region_id  # type: str
        self.accepting_vpc = accepting_vpc  # type: ListVpcPeerConnectionsResponseBodyVpcPeerConnectsAcceptingVpc
        self.bandwidth = bandwidth  # type: int
        self.biz_status = biz_status  # type: str
        self.description = description  # type: str
        self.gmt_create = gmt_create  # type: str
        self.gmt_expired = gmt_expired  # type: str
        self.gmt_modified = gmt_modified  # type: str
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str
        self.owner_id = owner_id  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.status = status  # type: str
        self.vpc = vpc  # type: ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc

    def validate(self):
        if self.accepting_vpc:
            self.accepting_vpc.validate()
        if self.vpc:
            self.vpc.validate()

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponseBodyVpcPeerConnects, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accepting_owner_uid is not None:
            result['AcceptingOwnerUid'] = self.accepting_owner_uid
        if self.accepting_region_id is not None:
            result['AcceptingRegionId'] = self.accepting_region_id
        if self.accepting_vpc is not None:
            result['AcceptingVpc'] = self.accepting_vpc.to_map()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.biz_status is not None:
            result['BizStatus'] = self.biz_status
        if self.description is not None:
            result['Description'] = self.description
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_expired is not None:
            result['GmtExpired'] = self.gmt_expired
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc is not None:
            result['Vpc'] = self.vpc.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptingOwnerUid') is not None:
            self.accepting_owner_uid = m.get('AcceptingOwnerUid')
        if m.get('AcceptingRegionId') is not None:
            self.accepting_region_id = m.get('AcceptingRegionId')
        if m.get('AcceptingVpc') is not None:
            temp_model = ListVpcPeerConnectionsResponseBodyVpcPeerConnectsAcceptingVpc()
            self.accepting_vpc = temp_model.from_map(m['AcceptingVpc'])
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BizStatus') is not None:
            self.biz_status = m.get('BizStatus')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtExpired') is not None:
            self.gmt_expired = m.get('GmtExpired')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Vpc') is not None:
            temp_model = ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc()
            self.vpc = temp_model.from_map(m['Vpc'])
        return self


class ListVpcPeerConnectionsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None, vpc_peer_connects=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.vpc_peer_connects = vpc_peer_connects  # type: list[ListVpcPeerConnectionsResponseBodyVpcPeerConnects]

    def validate(self):
        if self.vpc_peer_connects:
            for k in self.vpc_peer_connects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['VpcPeerConnects'] = []
        if self.vpc_peer_connects is not None:
            for k in self.vpc_peer_connects:
                result['VpcPeerConnects'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vpc_peer_connects = []
        if m.get('VpcPeerConnects') is not None:
            for k in m.get('VpcPeerConnects'):
                temp_model = ListVpcPeerConnectionsResponseBodyVpcPeerConnects()
                self.vpc_peer_connects.append(temp_model.from_map(k))
        return self


class ListVpcPeerConnectionsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListVpcPeerConnectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponse, self).to_map()
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
            temp_model = ListVpcPeerConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, description=None, dry_run=None, instance_id=None, name=None):
        self.client_token = client_token  # type: str
        self.description = description  # type: str
        self.dry_run = dry_run  # type: bool
        self.instance_id = instance_id  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcPeerConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.description is not None:
            result['Description'] = self.description
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ModifyVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcPeerConnectionResponseBody, self).to_map()
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


class ModifyVpcPeerConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyVpcPeerConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcPeerConnectionResponse, self).to_map()
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
            temp_model = ModifyVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, resource_owner_account=None):
        self.client_token = client_token  # type: str
        self.dry_run = dry_run  # type: bool
        self.instance_id = instance_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectVpcPeerConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class RejectVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectVpcPeerConnectionResponseBody, self).to_map()
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


class RejectVpcPeerConnectionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RejectVpcPeerConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectVpcPeerConnectionResponse, self).to_map()
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
            temp_model = RejectVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


