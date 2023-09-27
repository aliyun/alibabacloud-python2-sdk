# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddUserToVpcEndpointServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, service_id=None, user_arn=None, user_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the endpoint service. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The whitelist in the format of Aliyun Resource Name (ARN).
        self.user_arn = user_arn  # type: str
        # The account ID that you want to add to the whitelist.
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToVpcEndpointServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_arn is not None:
            result['UserARN'] = self.user_arn
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserARN') is not None:
            self.user_arn = m.get('UserARN')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUserToVpcEndpointServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUserToVpcEndpointServiceResponseBody, self).to_map()
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


class AddUserToVpcEndpointServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUserToVpcEndpointServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUserToVpcEndpointServiceResponse, self).to_map()
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
            temp_model = AddUserToVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddZoneToVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, v_switch_id=None,
                 zone_id=None, ip=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the endpoint to which you want to add the zone.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the vSwitch in the zone that you want to add. The system automatically creates an endpoint ENI in the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the zone that you want to add.
        self.zone_id = zone_id  # type: str
        # The IP address of the endpoint ENI in the zone that you want to add.
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddZoneToVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class AddZoneToVpcEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddZoneToVpcEndpointResponseBody, self).to_map()
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


class AddZoneToVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddZoneToVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddZoneToVpcEndpointResponse, self).to_map()
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
            temp_model = AddZoneToVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachResourceToVpcEndpointServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, resource_id=None, resource_type=None,
                 service_id=None, zone_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the endpoint service to which you want to add the service resource.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The service resource ID.
        self.resource_id = resource_id  # type: str
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: a Classic Load Balancer (CLB) instance that supports PrivateLink. In addition, the CLB instance is deployed in a virtual private cloud (VPC).
        # *   **alb**: an Application Load Balancer (ALB) instance that supports PrivateLink. In addition, the ALB instance is deployed in a VPC.
        self.resource_type = resource_type  # type: str
        # The ID of the endpoint service to which you want to add the service resource.
        self.service_id = service_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachResourceToVpcEndpointServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class AttachResourceToVpcEndpointServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachResourceToVpcEndpointServiceResponseBody, self).to_map()
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


class AttachResourceToVpcEndpointServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachResourceToVpcEndpointServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachResourceToVpcEndpointServiceResponse, self).to_map()
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
            temp_model = AttachResourceToVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachSecurityGroupToVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, security_group_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the endpoint with which you want to associate the security group.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint with which you want to associate with the security group. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the security group with which you want to associate the endpoint.
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachSecurityGroupToVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class AttachSecurityGroupToVpcEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachSecurityGroupToVpcEndpointResponseBody, self).to_map()
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


class AttachSecurityGroupToVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachSecurityGroupToVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachSecurityGroupToVpcEndpointResponse, self).to_map()
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
            temp_model = AttachSecurityGroupToVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, resource_group_id=None, resource_id=None, resource_region_id=None):
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.resource_region_id = resource_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
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


class CheckProductOpenResponseBody(TeaModel):
    def __init__(self, request_id=None, success=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether PrivateLink is activated.
        # 
        # Only **true** is returned. The value indicates that PrivateLink is activated.
        self.success = success  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckProductOpenResponseBody, self).to_map()
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


class CheckProductOpenResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckProductOpenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckProductOpenResponse, self).to_map()
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
            temp_model = CheckProductOpenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointRequestTag, self).to_map()
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


class CreateVpcEndpointRequestZone(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None, ip=None):
        # The ID of the vSwitch where you want to create the endpoint ENI in the zone. You can specify up to 10 vSwitch IDs.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the zone in which the endpoint is deployed.
        # 
        # You can specify up to 10 zone IDs.
        self.zone_id = zone_id  # type: str
        # The IP address of the zone in which the endpoint is deployed.
        # 
        # You can specify up to 10 IP addresses.
        self.ip = ip  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointRequestZone, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.ip is not None:
            result['ip'] = self.ip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        return self


class CreateVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_description=None, endpoint_name=None,
                 endpoint_type=None, protected_enabled=None, region_id=None, resource_group_id=None, security_group_id=None,
                 service_id=None, service_name=None, tag=None, vpc_id=None, zone=None, zone_private_ip_address_count=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The description of the endpoint.
        # 
        # The description must be 2 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.endpoint_description = endpoint_description  # type: str
        # The name of the endpoint.
        # 
        # The name must be 2 to 128 characters in length, and can contain digits, underscores (\_), and hyphens (-). The name must start with a letter.
        self.endpoint_name = endpoint_name  # type: str
        # The type of the endpoint.
        # 
        # Set the value to **Interface**. Then, you can specify Application Load Balancer (ALB) and Classic Load Balancer (CLB) instances as service resources for the endpoint service.
        self.endpoint_type = endpoint_type  # type: str
        # Specifies whether to enable user authentication. This parameter is available in Security Token Service (STS) mode. Valid values:
        # 
        # *   **true**: enables user authentication. After user authentication is enabled, only the user who creates the endpoint can modify or delete the endpoint in STS mode.
        # *   **false** (default): disables user authentication.
        self.protected_enabled = protected_enabled  # type: bool
        # The region ID of the endpoint.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the security group that is associated with the endpoint ENI. The security group can be used to control data transfer between the VPC and the endpoint ENI.
        # 
        # The endpoint can be associated with up to 10 security groups.
        self.security_group_id = security_group_id  # type: list[str]
        # The ID of the endpoint service with which the endpoint is associated.
        self.service_id = service_id  # type: str
        # The name of the endpoint service with which the endpoint is associated.
        self.service_name = service_name  # type: str
        # The list of tags.
        self.tag = tag  # type: list[CreateVpcEndpointRequestTag]
        # The ID of the virtual private cloud (VPC) to which the endpoint belongs.
        self.vpc_id = vpc_id  # type: str
        # The zones where the endpoint is deployed.
        self.zone = zone  # type: list[CreateVpcEndpointRequestZone]
        # The number of private IP addresses that are assigned to an elastic network interface (ENI) in each zone. Set the value to **1**.
        self.zone_private_ip_address_count = zone_private_ip_address_count  # type: long

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.protected_enabled is not None:
            result['ProtectedEnabled'] = self.protected_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        if self.zone_private_ip_address_count is not None:
            result['ZonePrivateIpAddressCount'] = self.zone_private_ip_address_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('ProtectedEnabled') is not None:
            self.protected_enabled = m.get('ProtectedEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVpcEndpointRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = CreateVpcEndpointRequestZone()
                self.zone.append(temp_model.from_map(k))
        if m.get('ZonePrivateIpAddressCount') is not None:
            self.zone_private_ip_address_count = m.get('ZonePrivateIpAddressCount')
        return self


class CreateVpcEndpointResponseBody(TeaModel):
    def __init__(self, bandwidth=None, connection_status=None, create_time=None, endpoint_business_status=None,
                 endpoint_description=None, endpoint_domain=None, endpoint_id=None, endpoint_name=None, endpoint_status=None,
                 request_id=None, service_id=None, service_name=None, vpc_id=None):
        # The bandwidth of the endpoint connection. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: long
        # The state of the endpoint connection. Valid values:
        # 
        # *   **Pending**: The connection is being modified.
        # *   **Connecting**: The connection is being established.
        # *   **Connected**: The connection is established.
        # *   **Disconnecting**: The endpoint is being disconnected from the endpoint service.
        # *   **Disconnected**: The endpoint is disconnected from the endpoint service.
        # *   **Deleting**: The connection is being deleted.
        self.connection_status = connection_status  # type: str
        # The time when the endpoint was created.
        self.create_time = create_time  # type: str
        # The service state of the endpoint. Valid values:
        # 
        # *   **Normal**: The endpoint runs as expected.
        # *   **FinacialLocked**: The endpoint is locked due to overdue payments.
        self.endpoint_business_status = endpoint_business_status  # type: str
        # The description of the endpoint.
        self.endpoint_description = endpoint_description  # type: str
        # The domain name of the endpoint.
        self.endpoint_domain = endpoint_domain  # type: str
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The name of the endpoint.
        self.endpoint_name = endpoint_name  # type: str
        # The state of the endpoint. Valid values:
        # 
        # *   **Creating**: The endpoint is being created.
        # *   **Active**: The endpoint is available.
        # *   **Pending**: The endpoint is being modified.
        # *   **Deleting**: The endpoint is being deleted.
        self.endpoint_status = endpoint_status  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the endpoint service with which the endpoint is associated.
        self.service_id = service_id  # type: str
        # The name of the endpoint service with which the endpoint is associated.
        self.service_name = service_name  # type: str
        # The ID of the VPC to which the endpoint belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcEndpointResponse, self).to_map()
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
            temp_model = CreateVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateVpcEndpointServiceRequestResource(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, zone_id=None):
        # The ID of the service resource that is added to the endpoint service. You can specify up to 20 service resource IDs.
        self.resource_id = resource_id  # type: str
        # The type of the service resource that is added to the endpoint service. You can add up to 20 service resources to the endpoint service. Valid values:
        # 
        # *   **slb**: a CLB instance
        # *   **alb**: an ALB instance
        # *   **nlb**: a NLB instance
        # 
        # >  In regions where PrivateLink is supported, CLB instances deployed in virtual private clouds (VPCs) can serve as service resources of the endpoint service.
        self.resource_type = resource_type  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointServiceRequestResource, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateVpcEndpointServiceRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value must be 1 to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointServiceRequestTag, self).to_map()
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


class CreateVpcEndpointServiceRequest(TeaModel):
    def __init__(self, auto_accept_enabled=None, client_token=None, dry_run=None, payer=None, region_id=None,
                 resource=None, resource_group_id=None, service_description=None, service_resource_type=None,
                 service_support_ipv_6=None, tag=None, zone_affinity_enabled=None):
        # Specifies whether to automatically accept endpoint connection requests. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.auto_accept_enabled = auto_accept_enabled  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request.
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The payer of the endpoint service. Valid values:
        # 
        # *   **Endpoint**: the service consumer
        # *   **EndpointService**: the service provider
        # 
        # > By default, the feature of allowing the service provider to pay is unavailable. To use this feature, log on to the [Quota Center console](https://quotas.console.aliyun.com/white-list-products/privatelink/quotas) and click Privileges in the left-side navigation pane. On the **Privileges** page, enter the quota ID `privatelink_whitelist/epsvc_payer_mode`, and click Apply in the Actions column.
        self.payer = payer  # type: str
        # The region ID of the endpoint service.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The service resources of the endpoint service.
        self.resource = resource  # type: list[CreateVpcEndpointServiceRequestResource]
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The description of the endpoint service.
        self.service_description = service_description  # type: str
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: a Classic Load Balancer (CLB) instance
        # *   **alb**: an Application Load Balancer (ALB) instance
        # *   **nlb**: a Network Load Balancer (NLB) instance
        self.service_resource_type = service_resource_type  # type: str
        # Specifies whether to enable IPv6 for the endpoint service. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.service_support_ipv_6 = service_support_ipv_6  # type: bool
        # The list of tags.
        self.tag = tag  # type: list[CreateVpcEndpointServiceRequestTag]
        # Specifies whether to first resolve the domain name of the nearest endpoint that is associated with the endpoint service. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool

    def validate(self):
        if self.resource:
            for k in self.resource:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateVpcEndpointServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Resource'] = []
        if self.resource is not None:
            for k in self.resource:
                result['Resource'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.resource = []
        if m.get('Resource') is not None:
            for k in m.get('Resource'):
                temp_model = CreateVpcEndpointServiceRequestResource()
                self.resource.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVpcEndpointServiceRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class CreateVpcEndpointServiceResponseBody(TeaModel):
    def __init__(self, auto_accept_enabled=None, create_time=None, request_id=None, resource_group_id=None,
                 service_business_status=None, service_description=None, service_domain=None, service_id=None, service_name=None,
                 service_status=None, service_support_ipv_6=None, zone_affinity_enabled=None):
        # Indicates whether the endpoint service automatically accepts endpoint connection requests. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_accept_enabled = auto_accept_enabled  # type: bool
        # The time when the endpoint service was created.
        self.create_time = create_time  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The service state of the endpoint service. Valid values:
        # 
        # *   **Normal**: The endpoint service runs as expected.
        # *   **FinacialLocked**: The endpoint service is locked due to overdue payments.
        self.service_business_status = service_business_status  # type: str
        # The description of the endpoint service.
        self.service_description = service_description  # type: str
        # The domain name of the endpoint service.
        self.service_domain = service_domain  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The name of the endpoint service.
        self.service_name = service_name  # type: str
        # The state of the endpoint service. Valid values:
        # 
        # *   **Creating**: The endpoint service is being created.
        # *   **Pending**: The endpoint service is being modified.
        # *   **Active**: The endpoint service is available.
        # *   **Deleting**: The endpoint service is being deleted.
        # *   **Inactive**: The endpoint service is unavailable.
        self.service_status = service_status  # type: str
        # Indicates whether IPv6 was enabled for the endpoint service. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.service_support_ipv_6 = service_support_ipv_6  # type: bool
        # Indicates whether the domain name of the nearest endpoint that is associated with the endpoint service is resolved first. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateVpcEndpointServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class CreateVpcEndpointServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateVpcEndpointServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateVpcEndpointServiceResponse, self).to_map()
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
            temp_model = CreateVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the endpoint that you want to delete.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint that you want to delete. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteVpcEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcEndpointResponseBody, self).to_map()
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


class DeleteVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcEndpointResponse, self).to_map()
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
            temp_model = DeleteVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteVpcEndpointServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, service_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the endpoint service. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the endpoint service that you want to delete.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcEndpointServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DeleteVpcEndpointServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteVpcEndpointServiceResponseBody, self).to_map()
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


class DeleteVpcEndpointServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteVpcEndpointServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteVpcEndpointServiceResponse, self).to_map()
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
            temp_model = DeleteVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region ID.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegionsRegion(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the region.
        self.region_endpoint = region_endpoint  # type: str
        # The region ID.
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
        # The available regions.
        self.regions = regions  # type: DescribeRegionsResponseBodyRegions
        # The request ID.
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


class DescribeZonesRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region ID of the zone. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeZonesResponseBodyZonesZone(TeaModel):
    def __init__(self, local_name=None, zone_id=None):
        # The name of the zone.
        self.local_name = local_name  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZonesZone, self).to_map()
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


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, zone=None):
        self.zone = zone  # type: list[DescribeZonesResponseBodyZonesZone]

    def validate(self):
        if self.zone:
            for k in self.zone:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Zone'] = []
        if self.zone is not None:
            for k in self.zone:
                result['Zone'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k in m.get('Zone'):
                temp_model = DescribeZonesResponseBodyZonesZone()
                self.zone.append(temp_model.from_map(k))
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The returned zones.
        self.zones = zones  # type: DescribeZonesResponseBodyZones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.zones is not None:
            result['Zones'] = self.zones.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Zones') is not None:
            temp_model = DescribeZonesResponseBodyZones()
            self.zones = temp_model.from_map(m['Zones'])
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeZonesResponse, self).to_map()
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
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachResourceFromVpcEndpointServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, resource_id=None, resource_type=None,
                 service_id=None, zone_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a value, but you must make sure that the value is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the endpoint.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The service resource ID.
        self.resource_id = resource_id  # type: str
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: a Classic Load Balancer (CLB) instance that supports PrivateLink. In addition, the CLB instance is deployed in a virtual private cloud (VPC).
        # *   **alb**: an Application Load Balancer (ALB) instance that supports PrivateLink. In addition, the ALB instance is deployed in a VPC.
        self.resource_type = resource_type  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The ID of the zone that you want to remove.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachResourceFromVpcEndpointServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DetachResourceFromVpcEndpointServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachResourceFromVpcEndpointServiceResponseBody, self).to_map()
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


class DetachResourceFromVpcEndpointServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachResourceFromVpcEndpointServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachResourceFromVpcEndpointServiceResponse, self).to_map()
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
            temp_model = DetachResourceFromVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachSecurityGroupFromVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, security_group_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the endpoint that you want to disassociate from the security group.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint that you want to disassociate from the security group. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the security group from which you want to disassociate the endpoint.
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachSecurityGroupFromVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class DetachSecurityGroupFromVpcEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachSecurityGroupFromVpcEndpointResponseBody, self).to_map()
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


class DetachSecurityGroupFromVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachSecurityGroupFromVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachSecurityGroupFromVpcEndpointResponse, self).to_map()
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
            temp_model = DetachSecurityGroupFromVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVpcEndpointConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, service_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The ID of the region where the connection request from the endpoint is rejected. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableVpcEndpointConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class DisableVpcEndpointConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableVpcEndpointConnectionResponseBody, self).to_map()
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


class DisableVpcEndpointConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableVpcEndpointConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableVpcEndpointConnectionResponse, self).to_map()
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
            temp_model = DisableVpcEndpointConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableVpcEndpointZoneConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, replaced_resource=None,
                 service_id=None, zone_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the AccessKey pair, the permissions of the RAM user, and the required parameters. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The ID of the region where the connection request from the endpoint is rejected.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # Specifies whether to disconnect the endpoint from the previous connection after the service resource is smoothly migrated. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        # 
        # > Set the value to true if you want to disconnect the endpoint from the previous connection in the zone after the service resource is smoothly migrated.
        self.replaced_resource = replaced_resource  # type: bool
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The ID of the zone that is associated with the endpoint.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableVpcEndpointZoneConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replaced_resource is not None:
            result['ReplacedResource'] = self.replaced_resource
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplacedResource') is not None:
            self.replaced_resource = m.get('ReplacedResource')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DisableVpcEndpointZoneConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableVpcEndpointZoneConnectionResponseBody, self).to_map()
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


class DisableVpcEndpointZoneConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableVpcEndpointZoneConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableVpcEndpointZoneConnectionResponse, self).to_map()
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
            temp_model = DisableVpcEndpointZoneConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableVpcEndpointConnectionRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, dry_run=None, endpoint_id=None, region_id=None,
                 service_id=None):
        # The bandwidth of the endpoint connection. Valid values: **1024 to 10240**. Unit: Mbit/s.
        # 
        # > The bandwidth of an endpoint connection is in the range of **100 to 10,240** Mbit/s. The default bandwidth is **1,024** Mbit/s. When the endpoint is connected to the endpoint service, the default bandwidth is the minimum bandwidth. In this case, the connection bandwidth range is **1,024 to 10,240** Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the check, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The ID of the region where the connection request is accepted.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableVpcEndpointConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class EnableVpcEndpointConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableVpcEndpointConnectionResponseBody, self).to_map()
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


class EnableVpcEndpointConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableVpcEndpointConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableVpcEndpointConnectionResponse, self).to_map()
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
            temp_model = EnableVpcEndpointConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableVpcEndpointZoneConnectionRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, service_id=None,
                 zone_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The ID of the region where the endpoint connection request is accepted. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The ID of the zone that is associated with the endpoint.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableVpcEndpointZoneConnectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class EnableVpcEndpointZoneConnectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableVpcEndpointZoneConnectionResponseBody, self).to_map()
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


class EnableVpcEndpointZoneConnectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableVpcEndpointZoneConnectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableVpcEndpointZoneConnectionResponse, self).to_map()
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
            temp_model = EnableVpcEndpointZoneConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcEndpointAttributeRequest(TeaModel):
    def __init__(self, endpoint_id=None, region_id=None):
        # The ID of the endpoint whose attributes you want to query.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint whose attributes you want to query.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcEndpointAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetVpcEndpointAttributeResponseBody(TeaModel):
    def __init__(self, bandwidth=None, connection_status=None, create_time=None, endpoint_business_status=None,
                 endpoint_description=None, endpoint_domain=None, endpoint_id=None, endpoint_name=None, endpoint_status=None,
                 endpoint_type=None, payer=None, region_id=None, request_id=None, resource_group_id=None, resource_owner=None,
                 service_id=None, service_name=None, vpc_id=None, zone_affinity_enabled=None,
                 zone_private_ip_address_count=None):
        # The bandwidth of the endpoint connection. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The state of the endpoint connection. Valid values:
        # 
        # *   **Pending**: The connection is being modified.
        # *   **Connecting**: The connection is being established.
        # *   **Connected**: The connection is established.
        # *   **Disconnecting**: The endpoint is being disconnected from the endpoint service.
        # *   **Disconnected**: The endpoint is disconnected from the endpoint service.
        # *   **Deleting**: The connection is being deleted.
        self.connection_status = connection_status  # type: str
        # The time when the endpoint was created.
        self.create_time = create_time  # type: str
        # The service state of the endpoint. Valid values:
        # 
        # *   **Normal**: The endpoint runs as expected.
        # *   **FinacialLocked**: The endpoint is locked due to overdue payments.
        self.endpoint_business_status = endpoint_business_status  # type: str
        # The description of the endpoint.
        self.endpoint_description = endpoint_description  # type: str
        # The domain name of the endpoint.
        self.endpoint_domain = endpoint_domain  # type: str
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The name of the endpoint.
        self.endpoint_name = endpoint_name  # type: str
        # The state of the endpoint. Valid values:
        # 
        # *   **Creating**: The endpoint is being created.
        # *   **Active**: The endpoint is available.
        # *   **Pending**: The endpoint is being modified.
        # *   **Deleting**: The endpoint is being deleted.
        self.endpoint_status = endpoint_status  # type: str
        # The type of the endpoint.
        # 
        # **Interface** is returned. The value indicates the interface endpoint with which the Classic Load Balancer (CLB) instances are associated.
        self.endpoint_type = endpoint_type  # type: str
        # The payer. Valid values:
        # 
        # *   **Endpoint**: the service consumer.
        # *   **EndpointService**: the service provider.
        self.payer = payer  # type: str
        # The region ID of the endpoint.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # Indicates whether the endpoint and the endpoint service belong to the same Alibaba Cloud account. Valid values:
        # 
        # *   **true**: The endpoint and the endpoint service belong to the same Alibaba Cloud account.
        # *   **false**: The endpoint and the endpoint service do not belong to the same Alibaba Cloud account.
        self.resource_owner = resource_owner  # type: bool
        # The ID of the endpoint service with which the endpoint is associated.
        self.service_id = service_id  # type: str
        # The name of the endpoint service with which the endpoint is associated.
        self.service_name = service_name  # type: str
        # The ID of the virtual private cloud (VPC) to which the endpoint belongs.
        self.vpc_id = vpc_id  # type: str
        # Indicates whether zone affinity is enabled. Valid values:
        # 
        # *   **true**: Zone affinity is enabled.
        # *   **false**: Zone affinity is disabled.
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool
        # The number of private IP addresses that are assigned to an elastic network interface (ENI) in each zone. Only **1** is returned.
        self.zone_private_ip_address_count = zone_private_ip_address_count  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcEndpointAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        if self.zone_private_ip_address_count is not None:
            result['ZonePrivateIpAddressCount'] = self.zone_private_ip_address_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        if m.get('ZonePrivateIpAddressCount') is not None:
            self.zone_private_ip_address_count = m.get('ZonePrivateIpAddressCount')
        return self


class GetVpcEndpointAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVpcEndpointAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVpcEndpointAttributeResponse, self).to_map()
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
            temp_model = GetVpcEndpointAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVpcEndpointServiceAttributeRequest(TeaModel):
    def __init__(self, region_id=None, service_id=None):
        # The region ID of the endpoint service.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcEndpointServiceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class GetVpcEndpointServiceAttributeResponseBody(TeaModel):
    def __init__(self, auto_accept_enabled=None, connect_bandwidth=None, create_time=None, max_bandwidth=None,
                 min_bandwidth=None, payer=None, region_id=None, request_id=None, resource_group_id=None,
                 service_business_status=None, service_description=None, service_domain=None, service_id=None, service_name=None,
                 service_resource_type=None, service_status=None, service_support_ipv_6=None, service_type=None,
                 zone_affinity_enabled=None, zones=None):
        # Indicates whether endpoint connection requests are automatically accepted. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_accept_enabled = auto_accept_enabled  # type: bool
        # The default bandwidth of the endpoint connection. Valid values: **100** to 10240. Unit: Mbit/s.
        self.connect_bandwidth = connect_bandwidth  # type: int
        # The time when the endpoint service was created.
        self.create_time = create_time  # type: str
        # The maximum bandwidth of the endpoint connection. Unit: Mbit/s.
        self.max_bandwidth = max_bandwidth  # type: int
        # The minimum bandwidth of the endpoint connection. Unit: Mbit/s.
        self.min_bandwidth = min_bandwidth  # type: int
        # The payer of the endpoint service. Valid values:
        # 
        # *   **Endpoint**: the service consumer.
        # *   **EndpointService**: the service provider.
        self.payer = payer  # type: str
        # The region ID of the endpoint service.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The service state of the endpoint service. Valid values:
        # 
        # *   **Normal**: The endpoint service runs as expected.
        # *   **FinacialLocked**: The endpoint service is locked due to overdue payments.
        self.service_business_status = service_business_status  # type: str
        # The description of the endpoint service.
        self.service_description = service_description  # type: str
        # The domain name of the endpoint service.
        self.service_domain = service_domain  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The name of the endpoint service.
        self.service_name = service_name  # type: str
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: a CLB instance.
        # *   **alb**: an ALB instance.
        self.service_resource_type = service_resource_type  # type: str
        # The state of the endpoint service. Valid values:
        # 
        # *   **Creating**: The endpoint service is being created.
        # *   **Pending**: The endpoint service is being modified.
        # *   **Active**: The endpoint service is available.
        # *   **Deleting**: The endpoint service is being deleted.
        # *   **Inactive**: The endpoint service is unavailable.
        self.service_status = service_status  # type: str
        # Indicates whether IPv6 is enabled for the endpoint service. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.service_support_ipv_6 = service_support_ipv_6  # type: bool
        # The type of the endpoint.
        # 
        # Only **Interface** is returned. The value indicates the interface endpoint. Then, you can specify ALB and CLB instances as service resources for the endpoint service.
        self.service_type = service_type  # type: str
        # Indicates whether zone affinity is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool
        # The zones to which the service resources belong.
        self.zones = zones  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVpcEndpointServiceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth
        if self.min_bandwidth is not None:
            result['MinBandwidth'] = self.min_bandwidth
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')
        if m.get('MinBandwidth') is not None:
            self.min_bandwidth = m.get('MinBandwidth')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class GetVpcEndpointServiceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetVpcEndpointServiceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVpcEndpointServiceAttributeResponse, self).to_map()
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
            temp_model = GetVpcEndpointServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointConnectionsRequest(TeaModel):
    def __init__(self, connection_status=None, endpoint_id=None, endpoint_owner_id=None, eni_id=None,
                 max_results=None, next_token=None, region_id=None, replaced_resource_id=None, resource_group_id=None,
                 resource_id=None, service_id=None):
        # The state of the endpoint connection. Valid values:
        # 
        # *   **Pending**: The endpoint connection is being modified.
        # *   **Connecting**: The endpoint connection is being established.
        # *   **Connected**: The endpoint connection is established.
        # *   **Disconnecting**: The endpoint is being disconnected from the endpoint service.
        # *   **Disconnected**: The endpoint is disconnected from the endpoint service.
        # *   **Deleting**: The connection is being deleted.
        # *   **ServiceDeleted**: The corresponding endpoint service has been deleted.
        self.connection_status = connection_status  # type: str
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The ID of the Alibaba Cloud account to which the endpoint belongs.
        self.endpoint_owner_id = endpoint_owner_id  # type: long
        # The ID of the endpoint elastic network interface (ENI).
        self.eni_id = eni_id  # type: str
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   If a next request is to be performed, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token  # type: str
        # The region ID of the endpoint connection.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the replaced service resource in smooth migration scenarios.
        self.replaced_resource_id = replaced_resource_id  # type: str
        # The ID of the resource group to which the endpoint belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The service resource ID.
        self.resource_id = resource_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointConnectionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_owner_id is not None:
            result['EndpointOwnerId'] = self.endpoint_owner_id
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.replaced_resource_id is not None:
            result['ReplacedResourceId'] = self.replaced_resource_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointOwnerId') is not None:
            self.endpoint_owner_id = m.get('EndpointOwnerId')
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ReplacedResourceId') is not None:
            self.replaced_resource_id = m.get('ReplacedResourceId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListVpcEndpointConnectionsResponseBodyConnectionsZones(TeaModel):
    def __init__(self, eni_id=None, replaced_eni_id=None, replaced_resource_id=None, resource_id=None,
                 v_switch_id=None, zone_domain=None, zone_id=None, zone_status=None):
        # The endpoint ENI ID.
        self.eni_id = eni_id  # type: str
        # The ID of the replaced endpoint ENI in smooth migration scenarios.
        self.replaced_eni_id = replaced_eni_id  # type: str
        # The ID of the replaced service resource in smooth migration scenarios.
        self.replaced_resource_id = replaced_resource_id  # type: str
        # The service resource ID.
        self.resource_id = resource_id  # type: str
        # The ID of the vSwitch to which the endpoint belongs.
        self.v_switch_id = v_switch_id  # type: str
        # The domain name of the zone.
        self.zone_domain = zone_domain  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str
        # The state of the zone. Valid values:
        # 
        # *   **Creating**: The zone is being created.
        # *   **Wait**: The zone is to be connected.
        # *   **Connected**: The zone is connected.
        # *   **Deleting**: The zone is being deleted.
        # *   **Disconnecting**: The zone is being disconnected.
        # *   **Disconnected**: The zone is disconnected.
        # *   **Connecting**: The zone is being connected.
        # *   **Migrating**: The zone is being migrated.
        # *   **Migrated**: The zone is migrated.
        self.zone_status = zone_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointConnectionsResponseBodyConnectionsZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.replaced_eni_id is not None:
            result['ReplacedEniId'] = self.replaced_eni_id
        if self.replaced_resource_id is not None:
            result['ReplacedResourceId'] = self.replaced_resource_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_domain is not None:
            result['ZoneDomain'] = self.zone_domain
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_status is not None:
            result['ZoneStatus'] = self.zone_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('ReplacedEniId') is not None:
            self.replaced_eni_id = m.get('ReplacedEniId')
        if m.get('ReplacedResourceId') is not None:
            self.replaced_resource_id = m.get('ReplacedResourceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneDomain') is not None:
            self.zone_domain = m.get('ZoneDomain')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneStatus') is not None:
            self.zone_status = m.get('ZoneStatus')
        return self


class ListVpcEndpointConnectionsResponseBodyConnections(TeaModel):
    def __init__(self, bandwidth=None, connection_status=None, endpoint_id=None, endpoint_owner_id=None,
                 endpoint_vpc_id=None, modified_time=None, resource_group_id=None, resource_owner=None, service_id=None, zones=None):
        # The bandwidth of the endpoint connection. Valid values: **1024 to 10240**. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The state of the endpoint connection. Valid values:
        # 
        # *   **Pending**: The connection is being modified.
        # *   **Connecting**: The connection is being established.
        # *   **Connected**: The connection is established.
        # *   **Disconnecting**: The endpoint is being disconnected from the endpoint service.
        # *   **Disconnected**: The endpoint is disconnected from the endpoint service.
        # *   **Deleting**: The connection is being deleted.
        # *   **ServiceDeleted**: The corresponding endpoint service has been deleted.
        self.connection_status = connection_status  # type: str
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The ID of the Alibaba Cloud account to which the endpoint belongs.
        self.endpoint_owner_id = endpoint_owner_id  # type: long
        # The ID of the virtual private cloud (VPC) to which the endpoint belongs.
        self.endpoint_vpc_id = endpoint_vpc_id  # type: str
        # The time when the endpoint connection was modified.
        self.modified_time = modified_time  # type: str
        # The ID of the resource group to which the endpoint belongs.
        self.resource_group_id = resource_group_id  # type: str
        # Indicates whether the endpoint and the endpoint service belong to the same Alibaba Cloud account. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.resource_owner = resource_owner  # type: bool
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The zones.
        self.zones = zones  # type: list[ListVpcEndpointConnectionsResponseBodyConnectionsZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointConnectionsResponseBodyConnections, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_owner_id is not None:
            result['EndpointOwnerId'] = self.endpoint_owner_id
        if self.endpoint_vpc_id is not None:
            result['EndpointVpcId'] = self.endpoint_vpc_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointOwnerId') is not None:
            self.endpoint_owner_id = m.get('EndpointOwnerId')
        if m.get('EndpointVpcId') is not None:
            self.endpoint_vpc_id = m.get('EndpointVpcId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListVpcEndpointConnectionsResponseBodyConnectionsZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListVpcEndpointConnectionsResponseBody(TeaModel):
    def __init__(self, connections=None, max_results=None, next_token=None, request_id=None, total_count=None):
        # The endpoint connections.
        self.connections = connections  # type: list[ListVpcEndpointConnectionsResponseBodyConnections]
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str

    def validate(self):
        if self.connections:
            for k in self.connections:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointConnectionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Connections'] = []
        if self.connections is not None:
            for k in self.connections:
                result['Connections'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k in m.get('Connections'):
                temp_model = ListVpcEndpointConnectionsResponseBodyConnections()
                self.connections.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListVpcEndpointConnectionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointConnectionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointConnectionsResponse, self).to_map()
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
            temp_model = ListVpcEndpointConnectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointSecurityGroupsRequest(TeaModel):
    def __init__(self, endpoint_id=None, max_results=None, next_token=None, region_id=None):
        # The ID of the endpoint that you want to query.
        self.endpoint_id = endpoint_id  # type: str
        # The number of entries to return on each page. Valid values:**1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   If a next request is to be performed, set the parameter to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token  # type: str
        # The region ID of the endpoint that you want to query.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointSecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcEndpointSecurityGroupsResponseBodySecurityGroups(TeaModel):
    def __init__(self, security_group_id=None):
        # The ID of the security group that is associated with the endpoint.
        self.security_group_id = security_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointSecurityGroupsResponseBodySecurityGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        return self


class ListVpcEndpointSecurityGroupsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, security_groups=None):
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The security groups that are associated with the endpoint.
        self.security_groups = security_groups  # type: list[ListVpcEndpointSecurityGroupsResponseBodySecurityGroups]

    def validate(self):
        if self.security_groups:
            for k in self.security_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityGroups'] = []
        if self.security_groups is not None:
            for k in self.security_groups:
                result['SecurityGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_groups = []
        if m.get('SecurityGroups') is not None:
            for k in m.get('SecurityGroups'):
                temp_model = ListVpcEndpointSecurityGroupsResponseBodySecurityGroups()
                self.security_groups.append(temp_model.from_map(k))
        return self


class ListVpcEndpointSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointSecurityGroupsResponse, self).to_map()
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
            temp_model = ListVpcEndpointSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServiceResourcesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, service_id=None):
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   If a next request is to be performed, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The region ID of the service resource.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServiceResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class ListVpcEndpointServiceResourcesResponseBodyResources(TeaModel):
    def __init__(self, auto_allocated_enabled=None, ip=None, region_id=None,
                 related_deprecated_endpoint_count=None, related_endpoint_count=None, resource_id=None, resource_support_ipv_6=None,
                 resource_type=None, v_switch_id=None, vpc_id=None, zone_id=None):
        # Indicates whether automatic resource allocation is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_allocated_enabled = auto_allocated_enabled  # type: bool
        # The IP address of the service resource.
        self.ip = ip  # type: str
        # The ID of the region where the service resource is deployed.
        self.region_id = region_id  # type: str
        # The number of endpoints that are associated with the service resource that is smoothly migrated.
        self.related_deprecated_endpoint_count = related_deprecated_endpoint_count  # type: long
        # The number of endpoints that are associated with the service resource.
        self.related_endpoint_count = related_endpoint_count  # type: long
        # The service resource ID.
        self.resource_id = resource_id  # type: str
        # Indicates whether IPv6 is enabled for the endpoint service. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.resource_support_ipv_6 = resource_support_ipv_6  # type: bool
        # The type of the service resource.
        # 
        # Only **slb** is returned. This value indicates a Classic Load Balancer (CLB) instance.
        self.resource_type = resource_type  # type: str
        # The ID of the vSwitch to which the service resource belongs.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the virtual private cloud (VPC) to which the service resource belongs.
        self.vpc_id = vpc_id  # type: str
        # The ID of the zone to which the service resource belongs.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServiceResourcesResponseBodyResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_allocated_enabled is not None:
            result['AutoAllocatedEnabled'] = self.auto_allocated_enabled
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.related_deprecated_endpoint_count is not None:
            result['RelatedDeprecatedEndpointCount'] = self.related_deprecated_endpoint_count
        if self.related_endpoint_count is not None:
            result['RelatedEndpointCount'] = self.related_endpoint_count
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_support_ipv_6 is not None:
            result['ResourceSupportIPv6'] = self.resource_support_ipv_6
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAllocatedEnabled') is not None:
            self.auto_allocated_enabled = m.get('AutoAllocatedEnabled')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelatedDeprecatedEndpointCount') is not None:
            self.related_deprecated_endpoint_count = m.get('RelatedDeprecatedEndpointCount')
        if m.get('RelatedEndpointCount') is not None:
            self.related_endpoint_count = m.get('RelatedEndpointCount')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceSupportIPv6') is not None:
            self.resource_support_ipv_6 = m.get('ResourceSupportIPv6')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListVpcEndpointServiceResourcesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, resources=None):
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The service resources.
        self.resources = resources  # type: list[ListVpcEndpointServiceResourcesResponseBodyResources]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServiceResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = ListVpcEndpointServiceResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServiceResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointServiceResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServiceResourcesResponse, self).to_map()
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
            temp_model = ListVpcEndpointServiceResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServiceUsersRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, service_id=None, user_id=None,
                 user_list_type=None):
        # The number of entries to return on each page. Valid values: **1 to 50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   If a next request is to be performed, set the value to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token  # type: str
        # The region ID of the endpoint service that you want to query.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The ID of the Alibaba Cloud account in the whitelist of the endpoint service.
        self.user_id = user_id  # type: long
        # The type of the user list in the whitelist of the endpoint service.
        self.user_list_type = user_list_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServiceUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_list_type is not None:
            result['UserListType'] = self.user_list_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserListType') is not None:
            self.user_list_type = m.get('UserListType')
        return self


class ListVpcEndpointServiceUsersResponseBodyUserARNs(TeaModel):
    def __init__(self, user_arn=None):
        # The whitelist in the format of ARN.
        self.user_arn = user_arn  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServiceUsersResponseBodyUserARNs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_arn is not None:
            result['UserARN'] = self.user_arn
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserARN') is not None:
            self.user_arn = m.get('UserARN')
        return self


class ListVpcEndpointServiceUsersResponseBodyUsers(TeaModel):
    def __init__(self, user_id=None):
        # The ID of the Alibaba Cloud account in the whitelist of the endpoint service.
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServiceUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListVpcEndpointServiceUsersResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, total_count=None, user_arns=None,
                 users=None):
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: str
        # The whitelists in the format of Aliyun Resource Name (ARN).
        self.user_arns = user_arns  # type: list[ListVpcEndpointServiceUsersResponseBodyUserARNs]
        # The Alibaba Cloud accounts in the whitelist of the endpoint service.
        self.users = users  # type: list[ListVpcEndpointServiceUsersResponseBodyUsers]

    def validate(self):
        if self.user_arns:
            for k in self.user_arns:
                if k:
                    k.validate()
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServiceUsersResponseBody, self).to_map()
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
        result['UserARNs'] = []
        if self.user_arns is not None:
            for k in self.user_arns:
                result['UserARNs'].append(k.to_map() if k else None)
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
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
        self.user_arns = []
        if m.get('UserARNs') is not None:
            for k in m.get('UserARNs'):
                temp_model = ListVpcEndpointServiceUsersResponseBodyUserARNs()
                self.user_arns.append(temp_model.from_map(k))
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListVpcEndpointServiceUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServiceUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointServiceUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServiceUsersResponse, self).to_map()
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
            temp_model = ListVpcEndpointServiceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServicesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServicesRequestTag, self).to_map()
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


class ListVpcEndpointServicesRequest(TeaModel):
    def __init__(self, auto_accept_enabled=None, max_results=None, next_token=None, region_id=None,
                 resource_group_id=None, resource_id=None, service_business_status=None, service_id=None, service_name=None,
                 service_resource_type=None, service_status=None, tag=None, zone_affinity_enabled=None):
        self.auto_accept_enabled = auto_accept_enabled  # type: bool
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
        self.service_business_status = service_business_status  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.service_resource_type = service_resource_type  # type: str
        self.service_status = service_status  # type: str
        self.tag = tag  # type: list[ListVpcEndpointServicesRequestTag]
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVpcEndpointServicesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class ListVpcEndpointServicesResponseBodyServicesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServicesResponseBodyServicesTags, self).to_map()
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


class ListVpcEndpointServicesResponseBodyServices(TeaModel):
    def __init__(self, auto_accept_enabled=None, connect_bandwidth=None, create_time=None, max_bandwidth=None,
                 min_bandwidth=None, payer=None, region_id=None, resource_group_id=None, service_business_status=None,
                 service_description=None, service_domain=None, service_id=None, service_name=None, service_resource_type=None,
                 service_status=None, service_support_ipv_6=None, service_type=None, tags=None, zone_affinity_enabled=None):
        self.auto_accept_enabled = auto_accept_enabled  # type: bool
        self.connect_bandwidth = connect_bandwidth  # type: int
        self.create_time = create_time  # type: str
        self.max_bandwidth = max_bandwidth  # type: int
        self.min_bandwidth = min_bandwidth  # type: int
        self.payer = payer  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_business_status = service_business_status  # type: str
        self.service_description = service_description  # type: str
        self.service_domain = service_domain  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.service_resource_type = service_resource_type  # type: str
        self.service_status = service_status  # type: str
        self.service_support_ipv_6 = service_support_ipv_6  # type: bool
        self.service_type = service_type  # type: str
        self.tags = tags  # type: list[ListVpcEndpointServicesResponseBodyServicesTags]
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth
        if self.min_bandwidth is not None:
            result['MinBandwidth'] = self.min_bandwidth
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_business_status is not None:
            result['ServiceBusinessStatus'] = self.service_business_status
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')
        if m.get('MinBandwidth') is not None:
            self.min_bandwidth = m.get('MinBandwidth')
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceBusinessStatus') is not None:
            self.service_business_status = m.get('ServiceBusinessStatus')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpcEndpointServicesResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class ListVpcEndpointServicesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, services=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.services = services  # type: list[ListVpcEndpointServicesResponseBodyServices]
        self.total_count = total_count  # type: int

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListVpcEndpointServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListVpcEndpointServicesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesResponse, self).to_map()
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
            temp_model = ListVpcEndpointServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointServicesByEndUserRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServicesByEndUserRequestTag, self).to_map()
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


class ListVpcEndpointServicesByEndUserRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_group_id=None, service_id=None,
                 service_name=None, service_type=None, tag=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.service_type = service_type  # type: str
        self.tag = tag  # type: list[ListVpcEndpointServicesByEndUserRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesByEndUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVpcEndpointServicesByEndUserRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListVpcEndpointServicesByEndUserResponseBodyServicesTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointServicesByEndUserResponseBodyServicesTags, self).to_map()
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


class ListVpcEndpointServicesByEndUserResponseBodyServices(TeaModel):
    def __init__(self, payer=None, resource_group_id=None, service_domain=None, service_id=None, service_name=None,
                 service_resource_type=None, service_support_ipv_6=None, service_type=None, tags=None, zones=None):
        self.payer = payer  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_domain = service_domain  # type: str
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.service_resource_type = service_resource_type  # type: str
        self.service_support_ipv_6 = service_support_ipv_6  # type: bool
        self.service_type = service_type  # type: str
        self.tags = tags  # type: list[ListVpcEndpointServicesByEndUserResponseBodyServicesTags]
        self.zones = zones  # type: list[str]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesByEndUserResponseBodyServices, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.payer is not None:
            result['Payer'] = self.payer
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_domain is not None:
            result['ServiceDomain'] = self.service_domain
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.service_resource_type is not None:
            result['ServiceResourceType'] = self.service_resource_type
        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6
        if self.service_type is not None:
            result['ServiceType'] = self.service_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zones is not None:
            result['Zones'] = self.zones
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Payer') is not None:
            self.payer = m.get('Payer')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceDomain') is not None:
            self.service_domain = m.get('ServiceDomain')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('ServiceResourceType') is not None:
            self.service_resource_type = m.get('ServiceResourceType')
        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')
        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpcEndpointServicesByEndUserResponseBodyServicesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('Zones') is not None:
            self.zones = m.get('Zones')
        return self


class ListVpcEndpointServicesByEndUserResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, services=None, total_count=None):
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.services = services  # type: list[ListVpcEndpointServicesByEndUserResponseBodyServices]
        self.total_count = total_count  # type: str

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesByEndUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Services'] = []
        if self.services is not None:
            for k in self.services:
                result['Services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.services = []
        if m.get('Services') is not None:
            for k in m.get('Services'):
                temp_model = ListVpcEndpointServicesByEndUserResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListVpcEndpointServicesByEndUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointServicesByEndUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointServicesByEndUserResponse, self).to_map()
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
            temp_model = ListVpcEndpointServicesByEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointZonesRequest(TeaModel):
    def __init__(self, endpoint_id=None, max_results=None, next_token=None, region_id=None):
        # The ID of the endpoint for which you want to query zones.
        # 
        # After you specify an endpoint ID, the system queries the zones of the specified endpoint.
        self.endpoint_id = endpoint_id  # type: str
        # The number of entries to return on each page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If this is your first request and no next requests are to be performed, you do not need to specify this parameter.
        # *   If a next request is to be performed, set the parameter to the value of **NextToken** that is returned from the last call.
        self.next_token = next_token  # type: str
        # The region ID of the endpoint.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListVpcEndpointZonesResponseBodyZones(TeaModel):
    def __init__(self, eni_id=None, eni_ip=None, region_id=None, v_switch_id=None, zone_domain=None, zone_id=None,
                 zone_ipv_6address=None, zone_status=None):
        # The endpoint ENI ID.
        self.eni_id = eni_id  # type: str
        # The IP address of the endpoint ENI.
        self.eni_ip = eni_ip  # type: str
        # The region ID of the endpoint.
        self.region_id = region_id  # type: str
        # The ID of the vSwitch in the zone. The system automatically creates an endpoint elastic network interface (ENI) in the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # The domain name of the zone.
        # 
        # After the endpoint is connected to the endpoint service, you can access the service resources in the endpoint service by using the domain name of the zone.
        self.zone_domain = zone_domain  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str
        # Indicates whether IPv6 is enabled for the endpoint service. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.zone_ipv_6address = zone_ipv_6address  # type: str
        # The state of the zone. Valid values:
        # 
        # *   **Creating**: The zone is being created.
        # *   **Wait**: The zone is to be connected.
        # *   **Connected**: The zone is connected.
        # *   **Deleting**: The zone is being deleted.
        # *   **Disconnecting**: The zone is being disconnected.
        # *   **Disconnected**: The zone is disconnected.
        # *   **Connecting**: The zone is being connected.
        self.zone_status = zone_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointZonesResponseBodyZones, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.eni_ip is not None:
            result['EniIp'] = self.eni_ip
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_domain is not None:
            result['ZoneDomain'] = self.zone_domain
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        if self.zone_ipv_6address is not None:
            result['ZoneIpv6Address'] = self.zone_ipv_6address
        if self.zone_status is not None:
            result['ZoneStatus'] = self.zone_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('EniIp') is not None:
            self.eni_ip = m.get('EniIp')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneDomain') is not None:
            self.zone_domain = m.get('ZoneDomain')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        if m.get('ZoneIpv6Address') is not None:
            self.zone_ipv_6address = m.get('ZoneIpv6Address')
        if m.get('ZoneStatus') is not None:
            self.zone_status = m.get('ZoneStatus')
        return self


class ListVpcEndpointZonesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, zones=None):
        # The number of entries returned on each page.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next requests are performed.
        # *   If a value is returned for **NextToken**, the value can be used in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The zones.
        self.zones = zones  # type: list[ListVpcEndpointZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = ListVpcEndpointZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class ListVpcEndpointZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointZonesResponse, self).to_map()
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
            temp_model = ListVpcEndpointZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVpcEndpointsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointsRequestTag, self).to_map()
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


class ListVpcEndpointsRequest(TeaModel):
    def __init__(self, connection_status=None, endpoint_id=None, endpoint_name=None, endpoint_status=None,
                 endpoint_type=None, max_results=None, next_token=None, region_id=None, resource_group_id=None, service_name=None,
                 tag=None, vpc_id=None):
        self.connection_status = connection_status  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_name = endpoint_name  # type: str
        self.endpoint_status = endpoint_status  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.service_name = service_name  # type: str
        self.tag = tag  # type: list[ListVpcEndpointsRequestTag]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVpcEndpointsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListVpcEndpointsResponseBodyEndpointsTags(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListVpcEndpointsResponseBodyEndpointsTags, self).to_map()
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


class ListVpcEndpointsResponseBodyEndpoints(TeaModel):
    def __init__(self, bandwidth=None, connection_status=None, create_time=None, endpoint_business_status=None,
                 endpoint_description=None, endpoint_domain=None, endpoint_id=None, endpoint_name=None, endpoint_status=None,
                 endpoint_type=None, region_id=None, resource_group_id=None, resource_owner=None, service_id=None,
                 service_name=None, tags=None, vpc_id=None, zone_affinity_enabled=None):
        self.bandwidth = bandwidth  # type: long
        self.connection_status = connection_status  # type: str
        self.create_time = create_time  # type: str
        self.endpoint_business_status = endpoint_business_status  # type: str
        self.endpoint_description = endpoint_description  # type: str
        self.endpoint_domain = endpoint_domain  # type: str
        self.endpoint_id = endpoint_id  # type: str
        self.endpoint_name = endpoint_name  # type: str
        self.endpoint_status = endpoint_status  # type: str
        self.endpoint_type = endpoint_type  # type: str
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_owner = resource_owner  # type: bool
        self.service_id = service_id  # type: str
        self.service_name = service_name  # type: str
        self.tags = tags  # type: list[ListVpcEndpointsResponseBodyEndpointsTags]
        self.vpc_id = vpc_id  # type: str
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointsResponseBodyEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.connection_status is not None:
            result['ConnectionStatus'] = self.connection_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoint_business_status is not None:
            result['EndpointBusinessStatus'] = self.endpoint_business_status
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_domain is not None:
            result['EndpointDomain'] = self.endpoint_domain
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.endpoint_status is not None:
            result['EndpointStatus'] = self.endpoint_status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ConnectionStatus') is not None:
            self.connection_status = m.get('ConnectionStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndpointBusinessStatus') is not None:
            self.endpoint_business_status = m.get('EndpointBusinessStatus')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointDomain') is not None:
            self.endpoint_domain = m.get('EndpointDomain')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('EndpointStatus') is not None:
            self.endpoint_status = m.get('EndpointStatus')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVpcEndpointsResponseBodyEndpointsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class ListVpcEndpointsResponseBody(TeaModel):
    def __init__(self, endpoints=None, max_results=None, next_token=None, request_id=None, total_count=None):
        self.endpoints = endpoints  # type: list[ListVpcEndpointsResponseBodyEndpoints]
        self.max_results = max_results  # type: int
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListVpcEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
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
                temp_model = ListVpcEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListVpcEndpointsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListVpcEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListVpcEndpointsResponse, self).to_map()
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
            temp_model = ListVpcEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenPrivateLinkServiceRequest(TeaModel):
    def __init__(self, owner_id=None):
        self.owner_id = owner_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenPrivateLinkServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class OpenPrivateLinkServiceResponseBody(TeaModel):
    def __init__(self, order_id=None, request_id=None):
        # The order ID.
        self.order_id = order_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(OpenPrivateLinkServiceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenPrivateLinkServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: OpenPrivateLinkServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(OpenPrivateLinkServiceResponse, self).to_map()
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
            temp_model = OpenPrivateLinkServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserFromVpcEndpointServiceRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, service_id=None, user_arn=None, user_id=None):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the AccessKey pair, the permissions of the RAM user, and the required parameters. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the endpoint service for which you want to remove the account ID from the whitelist. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The whitelist in the format of Aliyun Resource Name (ARN).
        self.user_arn = user_arn  # type: str
        # The account ID that you want to remove from the whitelist.
        self.user_id = user_id  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromVpcEndpointServiceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.user_arn is not None:
            result['UserARN'] = self.user_arn
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('UserARN') is not None:
            self.user_arn = m.get('UserARN')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveUserFromVpcEndpointServiceResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUserFromVpcEndpointServiceResponseBody, self).to_map()
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


class RemoveUserFromVpcEndpointServiceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveUserFromVpcEndpointServiceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUserFromVpcEndpointServiceResponse, self).to_map()
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
            temp_model = RemoveUserFromVpcEndpointServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveZoneFromVpcEndpointRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None, zone_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the endpoint for which you want to delete the zone.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint for which you want to delete the zone. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the zone that you want to delete.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveZoneFromVpcEndpointRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class RemoveZoneFromVpcEndpointResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveZoneFromVpcEndpointResponseBody, self).to_map()
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


class RemoveZoneFromVpcEndpointResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveZoneFromVpcEndpointResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveZoneFromVpcEndpointResponse, self).to_map()
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
            temp_model = RemoveZoneFromVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value must be 1 to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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
    def __init__(self, client_token=None, dry_run=None, region_id=None, resource_id=None, resource_type=None,
                 tag=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the PrivateLink instance.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The resource IDs. You can specify up to 20 resource IDs.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource.
        self.resource_type = resource_type  # type: str
        # The tags that you want to add to the resource.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
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
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
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
        # The request ID.
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


class UpdateVpcEndpointAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_description=None, endpoint_id=None,
                 endpoint_name=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The description of the endpoint.
        # 
        # The description must be 2 to 256 characters in length. It cannot start with `http://` or `https://`.
        self.endpoint_description = endpoint_description  # type: str
        # The endpoint ID whose attributes you want to modify.
        self.endpoint_id = endpoint_id  # type: str
        # The name of the endpoint.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (\_), and hyphens (-). The name must start with a letter.
        self.endpoint_name = endpoint_name  # type: str
        # The region ID of the endpoint whose attributes you want to modify. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_description is not None:
            result['EndpointDescription'] = self.endpoint_description
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.endpoint_name is not None:
            result['EndpointName'] = self.endpoint_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointDescription') is not None:
            self.endpoint_description = m.get('EndpointDescription')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('EndpointName') is not None:
            self.endpoint_name = m.get('EndpointName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateVpcEndpointAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointAttributeResponseBody, self).to_map()
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


class UpdateVpcEndpointAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVpcEndpointAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVpcEndpointAttributeResponse, self).to_map()
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
            temp_model = UpdateVpcEndpointAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointConnectionAttributeRequest(TeaModel):
    def __init__(self, bandwidth=None, client_token=None, dry_run=None, endpoint_id=None, region_id=None,
                 service_id=None):
        # The bandwidth of the endpoint connection that you want to modify. Unit: Mbit/s.
        self.bandwidth = bandwidth  # type: int
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint connection whose bandwidth you want to modify. You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointConnectionAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        return self


class UpdateVpcEndpointConnectionAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointConnectionAttributeResponseBody, self).to_map()
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


class UpdateVpcEndpointConnectionAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVpcEndpointConnectionAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVpcEndpointConnectionAttributeResponse, self).to_map()
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
            temp_model = UpdateVpcEndpointConnectionAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointServiceAttributeRequest(TeaModel):
    def __init__(self, auto_accept_enabled=None, client_token=None, connect_bandwidth=None, dry_run=None,
                 region_id=None, service_description=None, service_id=None, service_support_ipv_6=None,
                 zone_affinity_enabled=None):
        # Specifies whether to automatically accept endpoint connection requests. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_accept_enabled = auto_accept_enabled  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # The default bandwidth of the endpoint connection. Valid values: **100** to **10240**. Unit: Mbit/s.
        self.connect_bandwidth = connect_bandwidth  # type: int
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the endpoint service.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The description of the endpoint service.
        self.service_description = service_description  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # Specifies whether to enable IPv6. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.service_support_ipv_6 = service_support_ipv_6  # type: bool
        # Specifies whether to enable zone affinity. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.zone_affinity_enabled = zone_affinity_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointServiceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_accept_enabled is not None:
            result['AutoAcceptEnabled'] = self.auto_accept_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connect_bandwidth is not None:
            result['ConnectBandwidth'] = self.connect_bandwidth
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_description is not None:
            result['ServiceDescription'] = self.service_description
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.service_support_ipv_6 is not None:
            result['ServiceSupportIPv6'] = self.service_support_ipv_6
        if self.zone_affinity_enabled is not None:
            result['ZoneAffinityEnabled'] = self.zone_affinity_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAcceptEnabled') is not None:
            self.auto_accept_enabled = m.get('AutoAcceptEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectBandwidth') is not None:
            self.connect_bandwidth = m.get('ConnectBandwidth')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceDescription') is not None:
            self.service_description = m.get('ServiceDescription')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ServiceSupportIPv6') is not None:
            self.service_support_ipv_6 = m.get('ServiceSupportIPv6')
        if m.get('ZoneAffinityEnabled') is not None:
            self.zone_affinity_enabled = m.get('ZoneAffinityEnabled')
        return self


class UpdateVpcEndpointServiceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointServiceAttributeResponseBody, self).to_map()
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


class UpdateVpcEndpointServiceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVpcEndpointServiceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVpcEndpointServiceAttributeResponse, self).to_map()
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
            temp_model = UpdateVpcEndpointServiceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointServiceResourceAttributeRequest(TeaModel):
    def __init__(self, auto_allocated_enabled=None, client_token=None, dry_run=None, region_id=None,
                 resource_id=None, service_id=None, zone_id=None):
        # Specifies whether to enable automatic resource allocation. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.auto_allocated_enabled = auto_allocated_enabled  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run  # type: bool
        # The ID of the region where the service resource is deployed.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The service resource ID.
        self.resource_id = resource_id  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The zone ID of the service resource.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointServiceResourceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_allocated_enabled is not None:
            result['AutoAllocatedEnabled'] = self.auto_allocated_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AutoAllocatedEnabled') is not None:
            self.auto_allocated_enabled = m.get('AutoAllocatedEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateVpcEndpointServiceResourceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointServiceResourceAttributeResponseBody, self).to_map()
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


class UpdateVpcEndpointServiceResourceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVpcEndpointServiceResourceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVpcEndpointServiceResourceAttributeResponse, self).to_map()
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
            temp_model = UpdateVpcEndpointServiceResourceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateVpcEndpointZoneConnectionResourceAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, endpoint_id=None, region_id=None,
                 resource_allocate_mode=None, resource_id=None, resource_replace_mode=None, resource_type=None, service_id=None,
                 zone_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The endpoint ID.
        self.endpoint_id = endpoint_id  # type: str
        # The region ID of the endpoint connection whose bandwidth you want to modify.
        # 
        # You can call the [DescribeRegions](~~120468~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The resource allocation mode. You can change the resource allocation mode only if the endpoint connection is in the **Disconnected** state. Valid values:
        # 
        # *   **Auto**: automatically and randomly allocates the service resource. In this mode, the service resource is deleted.
        # *   **Mannual**: manually allocates the service resource. If you set the value to Mannual, you must also specify the **ResourceId** and **ResourceType** parameters.
        self.resource_allocate_mode = resource_allocate_mode  # type: str
        # The ID of the service resource that you want to manually allocate or migrate in the zone where the endpoint connection is deployed.
        # 
        # > If **ResourceAllocateMode** is set to **Mannual**, or **ResourceReplaceMode** is set, this parameter is required.
        self.resource_id = resource_id  # type: str
        # The migration mode of the service resource. Valid values:
        # 
        # *   **Graceful**: smoothly migrates the service resource in the zone.
        # *   **Force**: forcefully migrates the service resource in the zone.
        # 
        # > If you want to migrate the service resource, you need to set this parameter. This parameter is available only if the endpoint connection is in the **Connected** state. If you set this parameter, you must also specify the **ResourceId** and **ResourceType** parameters.
        self.resource_replace_mode = resource_replace_mode  # type: str
        # The type of the service resource. Valid values:
        # 
        # *   **slb**: a CLB instance that supports PrivateLink. In addition, the CLB instance is deployed in a VPC.
        # *   **alb**: an Application Load Balancer (ALB) instance that supports PrivateLink. In addition, the ALB instance is deployed in a VPC.
        # 
        # > If **ResourceAllocateMode** is set to **Mannual**, or **ResourceReplaceMode** is set, this parameter is required.
        self.resource_type = resource_type  # type: str
        # The endpoint service ID.
        self.service_id = service_id  # type: str
        # The zone ID.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointZoneConnectionResourceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_allocate_mode is not None:
            result['ResourceAllocateMode'] = self.resource_allocate_mode
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_replace_mode is not None:
            result['ResourceReplaceMode'] = self.resource_replace_mode
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.service_id is not None:
            result['ServiceId'] = self.service_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceAllocateMode') is not None:
            self.resource_allocate_mode = m.get('ResourceAllocateMode')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceReplaceMode') is not None:
            self.resource_replace_mode = m.get('ResourceReplaceMode')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateVpcEndpointZoneConnectionResourceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateVpcEndpointZoneConnectionResourceAttributeResponseBody, self).to_map()
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


class UpdateVpcEndpointZoneConnectionResourceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateVpcEndpointZoneConnectionResourceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateVpcEndpointZoneConnectionResourceAttributeResponse, self).to_map()
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
            temp_model = UpdateVpcEndpointZoneConnectionResourceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


