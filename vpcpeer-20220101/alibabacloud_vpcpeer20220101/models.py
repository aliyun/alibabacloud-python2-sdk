# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, resource_group_id=None,
                 resource_owner_account=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the VPC peering connection to be accepted by the accepter VPC.
        self.instance_id = instance_id  # type: str
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [What is a resource group?](~~94475~~)
        self.resource_group_id = resource_group_id  # type: str
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class AcceptVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptVpcPeerConnectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptVpcPeerConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AcceptVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcPeerConnectionRequest(TeaModel):
    def __init__(self, accepting_ali_uid=None, accepting_region_id=None, accepting_vpc_id=None, bandwidth=None,
                 client_token=None, description=None, dry_run=None, name=None, region_id=None, resource_group_id=None,
                 vpc_id=None):
        # The ID of the Alibaba Cloud account to which the accepter VPC belongs.
        # 
        # *   To create a VPC peering connection within your Alibaba Cloud account, enter the ID of your Alibaba Cloud account.
        # *   To create a VPC peering connection between your Alibaba Cloud account and another Alibaba Cloud account, enter the ID of the peer Alibaba Cloud account.
        # 
        # >  If the accepter is a RAM user, set **AcceptingAliUid** to the ID of the Alibaba Cloud account that created the RAM user.
        self.accepting_ali_uid = accepting_ali_uid  # type: long
        # The region ID of the accepter VPC of the VPC peering connection that you want to create.
        # 
        # *   To create an intra-region VPC peering connection, enter a region ID that is the same as that of the requester VPC.
        # *   To create an inter-region VPC peering connection, enter a region ID that is different from that of the requester VPC.
        self.accepting_region_id = accepting_region_id  # type: str
        # The ID of the accepter VPC.
        self.accepting_vpc_id = accepting_vpc_id  # type: str
        # The bandwidth of the VPC peering connection. Unit: Mbit/s. The value must be an integer greater than 0. Before you specify this parameter, make sure that you create an inter-region VPC peering connection.
        self.bandwidth = bandwidth  # type: int
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # The description of the VPC peering connection.
        # 
        # The description must be 2 to 256 characters in length. The description must start with a letter but cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The name of the VPC peering connection.
        # 
        # The name must be 2 to 128 characters in length, and can contain digits, underscores (\_), and hyphens (-). It must start with a letter.
        self.name = name  # type: str
        # The ID of the region where you want to create a VPC peering connection.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [Resource groups](~~94475~~).
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the requester VPC.
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
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateVpcPeerConnectionResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # The ID of the instance on which the VPC peering connection is created.
        self.instance_id = instance_id  # type: str
        # The request ID.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpcPeerConnectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcPeerConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, force=None, instance_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request syntax, and limits. If the request fails to pass the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # Specifies whether to forcefully delete the VPC peering connection. Valid values:
        # 
        # *   **false** (default): no.
        # *   **true**: yes. If you forcefully delete the VPC peering connection, the system deletes the routes that point to the VPC peering connection from the VPC route table.
        self.force = force  # type: bool
        # The ID of the VPC peering connection that you want to delete.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpcPeerConnectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcPeerConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcPeerConnectionAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, resource_owner_account=None):
        # The ID of the VPC peering connection that you want to query.
        self.instance_id = instance_id  # type: str
        self.resource_owner_account = resource_owner_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')
        return self


class GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        # The CIDR block of the accepter VPC.
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        # The IPv6 CIDR block of the accepter VPC.
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        # The ID of the accepter VPC.
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


class GetVpcPeerConnectionAttributeResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeResponseBodyTags, self).to_map()
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


class GetVpcPeerConnectionAttributeResponseBodyVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        # The CIDR block of the requester VPC.
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        # The IPv6 CIDR block of the requester VPC.
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        # The ID of the requester VPC.
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
                 name=None, owner_id=None, region_id=None, request_id=None, resource_group_id=None, status=None,
                 tags=None, vpc=None):
        # The ID of the Alibaba Cloud account to which the accepter VPC belongs.
        self.accepting_owner_uid = accepting_owner_uid  # type: long
        # The region ID of the accepter VPC.
        self.accepting_region_id = accepting_region_id  # type: str
        # The details of the accepter VPC.
        self.accepting_vpc = accepting_vpc  # type: GetVpcPeerConnectionAttributeResponseBodyAcceptingVpc
        # The bandwidth of the VPC peering connection. Unit: Mbit/s. The value must be an integer greater than 0.
        # 
        # >  If the value is set to **-1**, it indicates that no limit is imposed on the bandwidth.
        # 
        # Default value:
        # 
        # *   The default bandwidth of an inter-region VPC peering connection is **1024** Mbit/s.
        # *   The default bandwidth of an intra-region VPC peering connection is **-1** Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The business status of the VPC peering connection. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.biz_status = biz_status  # type: str
        # The description of the VPC peering connection.
        self.description = description  # type: str
        # The time when the VPC peering connection was created. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        self.gmt_create = gmt_create  # type: str
        # The expiration time of the VPC peering connection.
        # 
        # The expiration time is returned only when the **Status** of the VPC peering connection is **Accepting** or **Expired**. Otherwise, **null** is returned.
        self.gmt_expired = gmt_expired  # type: str
        # The time when the VPC peering connection was modified. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the VPC peering connection.
        self.instance_id = instance_id  # type: str
        # The name of the VPC peering connection.
        self.name = name  # type: str
        # The ID of the Alibaba Cloud account to which the requester VPC belongs.
        self.owner_id = owner_id  # type: long
        # The region ID of the requester VPC.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the VPC peering connection. Valid values:
        # 
        # *   **Creating**\
        # *   **Accepting**\
        # *   **Updating**\
        # *   **Rejected**\
        # *   **Expired**\
        # *   **Activated**\
        # *   **Deleting**\
        # *   **Deleted**\
        # 
        # For more information about the status of VPC peering connections, see [Overview of VPC peering connections](~~418507~~).
        self.status = status  # type: str
        # The tag list.
        self.tags = tags  # type: list[GetVpcPeerConnectionAttributeResponseBodyTags]
        # The details of the requester VPC.
        self.vpc = vpc  # type: GetVpcPeerConnectionAttributeResponseBodyVpc

    def validate(self):
        if self.accepting_vpc:
            self.accepting_vpc.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetVpcPeerConnectionAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Vpc') is not None:
            temp_model = GetVpcPeerConnectionAttributeResponseBodyVpc()
            self.vpc = temp_model.from_map(m['Vpc'])
        return self


class GetVpcPeerConnectionAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVpcPeerConnectionAttributeResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVpcPeerConnectionAttributeResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetVpcPeerConnectionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag that is added to the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The key can be up to 64 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        # 
        # >  Specify at least one of the **ResourceId.N** and **Tag.N** parameters (**Tag.N.Key** and **Tag.N.Value**).
        self.key = key  # type: str
        # The value of the tag that is added to the resource. You can specify up to 20 tag values. It can be an empty string.
        # 
        # The value can be up to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter but cannot start with `aliyun` or `acs:`. The value cannot contain `http://` or `https://`.
        # 
        # >  Specify at least one of the **ResourceId.N** and **Tag.N** parameters (**Tag.N.Key** and **Tag.N.Value**).
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
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_id=None, resource_type=None,
                 tag=None):
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no subsequent query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the value to the value of **NextToken** that is returned in the last call.
        self.next_token = next_token  # type: str
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The resource ID.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Set the value to **PeerConnection**, which specifies a VPC peering connection.
        self.resource_type = resource_type  # type: str
        # The tags.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
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
    def __init__(self, region_no=None, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        # The region of the requester VPC.
        self.region_no = region_no  # type: str
        # The ID of the resource.
        self.resource_id = resource_id  # type: str
        # The type of the resource. The value is set to **PeerConnection**, which indicates a VPC peering connection.
        self.resource_type = resource_type  # type: str
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
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
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
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
    def __init__(self, max_results=None, next_token=None, request_id=None, tag_resources=None):
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no next query is to be sent.
        # *   If **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The resources to which the tags are added.
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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
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
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
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


class ListVpcPeerConnectionsRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The key cannot exceed 64 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The tag value. You can specify at most 20 tag values. The tag key can be an empty string.
        # 
        # The tag value cannot exceed 128 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsRequestTags, self).to_map()
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


class ListVpcPeerConnectionsRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, name=None, next_token=None, region_id=None,
                 resource_group_id=None, tags=None, vpc_id=None):
        # The ID of the VPC peering connection that you want to query.
        self.instance_id = instance_id  # type: str
        # The number of entries to return per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The name of the VPC peering connection that you want to query.
        self.name = name  # type: str
        # The token that is used for the next query. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The ID of the region where you want to query VPC peering connections.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [What is a resource group?](~~94475~~)
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: list[ListVpcPeerConnectionsRequestTags]
        # The ID of the requester VPC or accepter VPC of the VPC peering connection that you want to query.
        self.vpc_id = vpc_id  # type: list[str]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcPeerConnectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpcPeerConnectionsRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcPeerConnectionsShrinkRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. You can specify at most 20 tag keys. It cannot be an empty string.
        # 
        # The key cannot exceed 64 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The tag value. You can specify at most 20 tag values. The tag key can be an empty string.
        # 
        # The tag value cannot exceed 128 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsShrinkRequestTags, self).to_map()
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


class ListVpcPeerConnectionsShrinkRequest(TeaModel):
    def __init__(self, instance_id=None, max_results=None, name=None, next_token=None, region_id=None,
                 resource_group_id=None, tags=None, vpc_id_shrink=None):
        # The ID of the VPC peering connection that you want to query.
        self.instance_id = instance_id  # type: str
        # The number of entries to return per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The name of the VPC peering connection that you want to query.
        self.name = name  # type: str
        # The token that is used for the next query. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The ID of the region where you want to query VPC peering connections.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        # 
        # For more information about resource groups, see [What is a resource group?](~~94475~~)
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tags = tags  # type: list[ListVpcPeerConnectionsShrinkRequestTags]
        # The ID of the requester VPC or accepter VPC of the VPC peering connection that you want to query.
        self.vpc_id_shrink = vpc_id_shrink  # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcPeerConnectionsShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id_shrink is not None:
            result['VpcId'] = self.vpc_id_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpcPeerConnectionsShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id_shrink = m.get('VpcId')
        return self


class ListVpcPeerConnectionsResponseBodyVpcPeerConnectsAcceptingVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        # The CIDR block of the accepter VPC.
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        # The IPv6 CIDR block of the accepter VPC.
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        # The ID of the accepter VPC.
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


class ListVpcPeerConnectionsResponseBodyVpcPeerConnectsTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponseBodyVpcPeerConnectsTags, self).to_map()
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


class ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc(TeaModel):
    def __init__(self, ipv_4cidrs=None, ipv_6cidrs=None, vpc_id=None):
        # The CIDR block of the requester VPC.
        self.ipv_4cidrs = ipv_4cidrs  # type: list[str]
        # The IPv6 CIDR block of the requester VPC.
        self.ipv_6cidrs = ipv_6cidrs  # type: list[str]
        # The ID of the requester VPC.
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
                 name=None, owner_id=None, region_id=None, resource_group_id=None, status=None, tags=None, vpc=None):
        # The ID of the Alibaba Cloud account to which the accepter VPC belongs.
        self.accepting_owner_uid = accepting_owner_uid  # type: long
        # The region ID of the accepter VPC.
        self.accepting_region_id = accepting_region_id  # type: str
        # The details of the accepter VPC.
        self.accepting_vpc = accepting_vpc  # type: ListVpcPeerConnectionsResponseBodyVpcPeerConnectsAcceptingVpc
        # The bandwidth of the VPC peering connection. Unit: Mbit/s. The value is an integer greater than 0.
        # 
        # >  If the value is set to -1, it indicates that no limit is imposed on the bandwidth.
        # 
        # Default value:
        # 
        # *   The default bandwidth of an inter-region VPC peering connection is **1024** Mbit/s.
        # *   The default bandwidth of an intra-region VPC peering connection is **-1** Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The business status of the VPC peering connection. Valid values:
        # 
        # *   **Normal**\
        # *   **FinancialLocked**\
        self.biz_status = biz_status  # type: str
        # The description of the VPC peering connection.
        self.description = description  # type: str
        # The time when the VPC peering connection was created. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        self.gmt_create = gmt_create  # type: str
        # The expiration time of the VPC peering connection. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        # 
        # The expiration time is returned only when the **Status** of the VPC peering connection is **Accepting** or **Expired**. Otherwise, **null** is returned.
        self.gmt_expired = gmt_expired  # type: str
        # The time when the VPC peering connection was modified. The time is displayed in the `YYYY-MM-DDThh:mm:ssZ` format in UTC.
        self.gmt_modified = gmt_modified  # type: str
        # The ID of the VPC peering connection.
        self.instance_id = instance_id  # type: str
        # The name of the VPC peering connection.
        self.name = name  # type: str
        # The ID of the Alibaba Cloud account to which the requester VPC belongs.
        self.owner_id = owner_id  # type: long
        # The region ID of the requester VPC.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the VPC peering connection. Valid values:
        # 
        # *   **Creating**\
        # *   **Accepting**\
        # *   **Updating**\
        # *   **Rejected**\
        # *   **Expired**\
        # *   **Activated**\
        # *   **Deleting**\
        # *   **Deleted**\
        # 
        # For more information about the status of VPC peering connections, see [Overview of VPC peering connections](~~418507~~).
        self.status = status  # type: str
        # The tag list.
        self.tags = tags  # type: list[ListVpcPeerConnectionsResponseBodyVpcPeerConnectsTags]
        # The details of the requester VPC.
        self.vpc = vpc  # type: ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc

    def validate(self):
        if self.accepting_vpc:
            self.accepting_vpc.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpcPeerConnectionsResponseBodyVpcPeerConnectsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Vpc') is not None:
            temp_model = ListVpcPeerConnectionsResponseBodyVpcPeerConnectsVpc()
            self.vpc = temp_model.from_map(m['Vpc'])
        return self


class ListVpcPeerConnectionsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None, vpc_peer_connects=None):
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next queries are sent.
        # *   If the value of **NextToken** is returned, the value indicates the token that is used for the next query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The number of entries returned.
        self.total_count = total_count  # type: int
        # The details of the VPC peering connections.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcPeerConnectionsResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcPeerConnectionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListVpcPeerConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyVpcPeerConnectionRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, description=None, dry_run=None, instance_id=None,
                 name=None):
        # The new bandwidth of the VPC peering connection. Unit: Mbit/s. The value must be an integer greater than 0.
        self.bandwidth = bandwidth  # type: int
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # The new description of the VPC peering connection.
        # 
        # The description must be 1 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.description = description  # type: str
        # Specifies whether to only precheck the request. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the VPC peering connection whose name or description you want to modify.
        self.instance_id = instance_id  # type: str
        # The new name of the VPC peering connection.
        # 
        # The name must be 1 to 128 characters in length, and cannot start with `http://` or `https://`.
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyVpcPeerConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
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
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyVpcPeerConnectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyVpcPeerConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, region_id=None, resource_id=None, resource_type=None):
        # The ID of the new resource group.
        # 
        # >  You can use resource groups to manage resources owned by your Alibaba Cloud account. Resource groups simplify the resource and permission management of your Alibaba Cloud account. For more information, see [What is resource management?](~~94475~~).
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The ID of the region to which the resource belongs.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the VPC peering connection.
        self.resource_id = resource_id  # type: str
        # The resource type. Set the value to **PeerConnection**, which specifies a VPC peering connection.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectVpcPeerConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, instance_id=None, resource_owner_account=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether to check the request without performing the operation. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the required parameters, request syntax, and limits. If the request fails to pass the check, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the VPC peering connection to be rejected by the acceptor VPC.
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
        # The ID of the request.
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
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectVpcPeerConnectionResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectVpcPeerConnectionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RejectVpcPeerConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You must enter at least one tag key and at most 20 tag keys. The tag key cannot be an empty string.
        # 
        # The key cannot exceed 64 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). The key must start with a letter but cannot start with `aliyun` or `acs:`. The key cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the tag. You must enter at least one tag value and at most 20 tag values. It can be an empty string.
        # 
        # The tag value cannot exceed 128 characters in length, and can contain digits, periods (.), underscores (\_), and hyphens (-). It must start with a letter but cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
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
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among all requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # The region ID of the resource to which you want to create and add tags.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The IDs of resources.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Set the value to **PeerConnection**, which specifies a VPC peering connection.
        self.resource_type = resource_type  # type: str
        # The tags.
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
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the operation is successful. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
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


class UnTagResourcesRequest(TeaModel):
    def __init__(self, all=None, client_token=None, region_id=None, resource_id=None, resource_type=None,
                 tag_key=None):
        # Specifies whether to remove all tags from the specified resource. Valid values:
        # 
        # *   **true**: removes all tags from the specified resource.
        # *   **false**: does not remove all tags from the specified resource. This is the default value.
        self.all = all  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among all requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # The region ID of the tag.
        # 
        # You can call the [DescribeRegions](~~36063~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The IDs of resources.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Set the value to **PeerConnection**, which specifies a VPC peering connection.
        self.resource_type = resource_type  # type: str
        # The tags.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesRequest, self).to_map()
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


class UnTagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether the tags are removed. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UnTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnTagResourcesResponseBody

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnTagResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


