# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddServersToServerGroupRequestServers(TeaModel):
    def __init__(self, description=None, port=None, server_id=None, server_ip=None, server_type=None, weight=None):
        # The description of the servers.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        # 
        # >  You can specify at most 40 servers in each call.
        self.description = description  # type: str
        # The port used by the backend server. Valid values: **1** to **65535**.
        # 
        # >  You can specify at most 40 servers in each call.
        self.port = port  # type: int
        # The ID of the server. You can specify at most 40 server IDs in each call.
        # 
        # *   If the server group type is **Instance**, set the ServerId parameter to the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. These backend servers are specified by **Ecs**, **Eni**, or **Eci**.
        # *   If the server group type is **Ip**, set the ServerId parameter to an IP address.
        self.server_id = server_id  # type: str
        # The IP address of the server. If the server group type is **Ip**, set the ServerId parameter to an IP address.
        # 
        # >  You can specify at most 40 server IP addresses in each call.
        self.server_ip = server_ip  # type: str
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: an ECS instance
        # *   **Eni**: an ENI
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        # 
        # >  You can specify at most 40 servers in each call.
        self.server_type = server_type  # type: str
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the weight of a backend server is set to **0**, no requests are forwarded to the backend server.
        # 
        # >  You can specify at most 40 servers in each call.
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddServersToServerGroupRequestServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class AddServersToServerGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, server_group_id=None, servers=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not add the servers to the server group. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str
        # A list of backend servers.
        self.servers = servers  # type: list[AddServersToServerGroupRequestServers]

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddServersToServerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = AddServersToServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class AddServersToServerGroupResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, server_group_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddServersToServerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class AddServersToServerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddServersToServerGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddServersToServerGroupResponse, self).to_map()
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
            temp_model = AddServersToServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(self, additional_certificate_ids=None, client_token=None, dry_run=None, listener_id=None,
                 region_id=None):
        # The additional certificates. You can associate up to 15 additional certificates with a listener in each request.
        self.additional_certificate_ids = additional_certificate_ids  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The listener ID. You must specify the ID of a listener that uses SSL over TCP.
        self.listener_id = listener_id  # type: str
        # The region ID of the Network Load Balancer (NLB) instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_certificate_ids is not None:
            result['AdditionalCertificateIds'] = self.additional_certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalCertificateIds') is not None:
            self.additional_certificate_ids = m.get('AdditionalCertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AssociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateAdditionalCertificatesWithListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateAdditionalCertificatesWithListenerResponse, self).to_map()
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
            temp_model = AssociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachCommonBandwidthPackageToLoadBalancerRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, client_token=None, dry_run=None, load_balancer_id=None,
                 region_id=None):
        # The ID of the EIP bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not associate the EIP bandwidth plan with the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachCommonBandwidthPackageToLoadBalancerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachCommonBandwidthPackageToLoadBalancerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachCommonBandwidthPackageToLoadBalancerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachCommonBandwidthPackageToLoadBalancerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachCommonBandwidthPackageToLoadBalancerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachCommonBandwidthPackageToLoadBalancerResponse, self).to_map()
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
            temp_model = AttachCommonBandwidthPackageToLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelShiftLoadBalancerZonesRequestZoneMappings(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None):
        # The ID of the vSwitch in the zone. By default, each zone uses one vSwitch and one subnet.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID of the NLB instance.
        # 
        # > You can add at most one zone in each call.
        # 
        # You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelShiftLoadBalancerZonesRequestZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CancelShiftLoadBalancerZonesRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None, zone_mappings=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The mappings between zones and vSwitches.
        # 
        # > You can add at most one zone in each call.
        self.zone_mappings = zone_mappings  # type: list[CancelShiftLoadBalancerZonesRequestZoneMappings]

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CancelShiftLoadBalancerZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = CancelShiftLoadBalancerZonesRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class CancelShiftLoadBalancerZonesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CancelShiftLoadBalancerZonesResponseBody, self).to_map()
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


class CancelShiftLoadBalancerZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CancelShiftLoadBalancerZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CancelShiftLoadBalancerZonesResponse, self).to_map()
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
            temp_model = CancelShiftLoadBalancerZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateListenerRequestProxyProtocolV2Config(TeaModel):
    def __init__(self, ppv_2private_link_ep_id_enabled=None, ppv_2private_link_eps_id_enabled=None,
                 ppv_2vpc_id_enabled=None):
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled  # type: bool
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled  # type: bool
        self.ppv_2vpc_id_enabled = ppv_2vpc_id_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestProxyProtocolV2Config, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ppv_2private_link_ep_id_enabled is not None:
            result['Ppv2PrivateLinkEpIdEnabled'] = self.ppv_2private_link_ep_id_enabled
        if self.ppv_2private_link_eps_id_enabled is not None:
            result['Ppv2PrivateLinkEpsIdEnabled'] = self.ppv_2private_link_eps_id_enabled
        if self.ppv_2vpc_id_enabled is not None:
            result['Ppv2VpcIdEnabled'] = self.ppv_2vpc_id_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ppv2PrivateLinkEpIdEnabled') is not None:
            self.ppv_2private_link_ep_id_enabled = m.get('Ppv2PrivateLinkEpIdEnabled')
        if m.get('Ppv2PrivateLinkEpsIdEnabled') is not None:
            self.ppv_2private_link_eps_id_enabled = m.get('Ppv2PrivateLinkEpsIdEnabled')
        if m.get('Ppv2VpcIdEnabled') is not None:
            self.ppv_2vpc_id_enabled = m.get('Ppv2VpcIdEnabled')
        return self


class CreateListenerRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerRequestTag, self).to_map()
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


class CreateListenerRequest(TeaModel):
    def __init__(self, alpn_enabled=None, alpn_policy=None, ca_certificate_ids=None, ca_enabled=None,
                 certificate_ids=None, client_token=None, cps=None, dry_run=None, end_port=None, idle_timeout=None,
                 listener_description=None, listener_port=None, listener_protocol=None, load_balancer_id=None, mss=None,
                 proxy_protocol_enabled=None, proxy_protocol_v2config=None, region_id=None, sec_sensor_enabled=None,
                 security_policy_id=None, server_group_id=None, start_port=None, tag=None):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.alpn_enabled = alpn_enabled  # type: bool
        # The ALPN policy.
        # 
        # Valid values:
        # 
        # *   HTTP1Only
        # *   HTTP2Only
        # *   HTTP2Preferred
        # *   HTTP2Optional
        self.alpn_policy = alpn_policy  # type: str
        # The certificate authority (CA) certificates. This parameter takes effect only for listeners that use SSL over TCP.
        # 
        # > You can specify only one CA certificate.
        self.ca_certificate_ids = ca_certificate_ids  # type: list[str]
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.ca_enabled = ca_enabled  # type: bool
        # The server certificates. This parameter takes effect only for listeners that use SSL over TCP.
        # 
        # > You can specify only one server certificate.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps  # type: int
        # Specifies whether to perform only a dry run without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The last port in the listener port range. Valid values: **0** to **65535**. The number of the last port must be greater than the number of the first port.
        # 
        # > This parameter is required when **ListenerPort** is set to **0**.
        self.end_port = end_port  # type: int
        # The timeout period of idle connections. Unit: seconds. Valid values: **1** to **900**. Default value: **900**.
        self.idle_timeout = idle_timeout  # type: int
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description  # type: str
        # The listener port. Valid values: **0** to **65535**.
        # 
        # If you set the value to **0**, the listener listens by port range. If you set the value to **0**, you must specify **StartPort** and **EndPort**.
        self.listener_port = listener_port  # type: int
        # The listener protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The ID of the Network Load Balancer (NLB) instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The maximum size of a TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged.
        # 
        # > This parameter is supported only by TCP listeners and listeners that use SSL over TCP.
        self.mss = mss  # type: int
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.proxy_protocol_enabled = proxy_protocol_enabled  # type: bool
        self.proxy_protocol_v2config = proxy_protocol_v2config  # type: CreateListenerRequestProxyProtocolV2Config
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.sec_sensor_enabled = sec_sensor_enabled  # type: bool
        # The security policy ID. System security policies and custom security policies are supported.
        # 
        # Valid values: **tls_cipher_policy\_1\_0** (default), **tls_cipher_policy\_1\_1**, **tls_cipher_policy\_1\_2**, **tls_cipher_policy\_1\_2\_strict**, and **tls_cipher_policy\_1\_2\_strict_with\_1\_3**.
        # 
        # > This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str
        # The first port in the listener port range. Valid values: **0** to **65535**.
        # 
        # > This parameter is required when **ListenerPort** is set to **0**.
        self.start_port = start_port  # type: int
        # The tags.
        self.tag = tag  # type: list[CreateListenerRequestTag]

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.proxy_protocol_v2config is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('ProxyProtocolV2Config') is not None:
            temp_model = CreateListenerRequestProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m['ProxyProtocolV2Config'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateListenerRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateListenerShrinkRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerShrinkRequestTag, self).to_map()
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


class CreateListenerShrinkRequest(TeaModel):
    def __init__(self, alpn_enabled=None, alpn_policy=None, ca_certificate_ids=None, ca_enabled=None,
                 certificate_ids=None, client_token=None, cps=None, dry_run=None, end_port=None, idle_timeout=None,
                 listener_description=None, listener_port=None, listener_protocol=None, load_balancer_id=None, mss=None,
                 proxy_protocol_enabled=None, proxy_protocol_v2config_shrink=None, region_id=None, sec_sensor_enabled=None,
                 security_policy_id=None, server_group_id=None, start_port=None, tag=None):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.alpn_enabled = alpn_enabled  # type: bool
        # The ALPN policy.
        # 
        # Valid values:
        # 
        # *   HTTP1Only
        # *   HTTP2Only
        # *   HTTP2Preferred
        # *   HTTP2Optional
        self.alpn_policy = alpn_policy  # type: str
        # The certificate authority (CA) certificates. This parameter takes effect only for listeners that use SSL over TCP.
        # 
        # > You can specify only one CA certificate.
        self.ca_certificate_ids = ca_certificate_ids  # type: list[str]
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.ca_enabled = ca_enabled  # type: bool
        # The server certificates. This parameter takes effect only for listeners that use SSL over TCP.
        # 
        # > You can specify only one server certificate.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps  # type: int
        # Specifies whether to perform only a dry run without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The last port in the listener port range. Valid values: **0** to **65535**. The number of the last port must be greater than the number of the first port.
        # 
        # > This parameter is required when **ListenerPort** is set to **0**.
        self.end_port = end_port  # type: int
        # The timeout period of idle connections. Unit: seconds. Valid values: **1** to **900**. Default value: **900**.
        self.idle_timeout = idle_timeout  # type: int
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description  # type: str
        # The listener port. Valid values: **0** to **65535**.
        # 
        # If you set the value to **0**, the listener listens by port range. If you set the value to **0**, you must specify **StartPort** and **EndPort**.
        self.listener_port = listener_port  # type: int
        # The listener protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The ID of the Network Load Balancer (NLB) instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The maximum size of a TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged.
        # 
        # > This parameter is supported only by TCP listeners and listeners that use SSL over TCP.
        self.mss = mss  # type: int
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.proxy_protocol_enabled = proxy_protocol_enabled  # type: bool
        self.proxy_protocol_v2config_shrink = proxy_protocol_v2config_shrink  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.sec_sensor_enabled = sec_sensor_enabled  # type: bool
        # The security policy ID. System security policies and custom security policies are supported.
        # 
        # Valid values: **tls_cipher_policy\_1\_0** (default), **tls_cipher_policy\_1\_1**, **tls_cipher_policy\_1\_2**, **tls_cipher_policy\_1\_2\_strict**, and **tls_cipher_policy\_1\_2\_strict_with\_1\_3**.
        # 
        # > This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str
        # The first port in the listener port range. Valid values: **0** to **65535**.
        # 
        # > This parameter is required when **ListenerPort** is set to **0**.
        self.start_port = start_port  # type: int
        # The tags.
        self.tag = tag  # type: list[CreateListenerShrinkRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateListenerShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.proxy_protocol_v2config_shrink is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('ProxyProtocolV2Config') is not None:
            self.proxy_protocol_v2config_shrink = m.get('ProxyProtocolV2Config')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateListenerShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateListenerResponseBody(TeaModel):
    def __init__(self, job_id=None, listener_id=None, request_id=None):
        # The asynchronous task ID.
        self.job_id = job_id  # type: str
        # The listener ID.
        self.listener_id = listener_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateListenerResponse, self).to_map()
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
            temp_model = CreateListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLoadBalancerRequestDeletionProtectionConfig(TeaModel):
    def __init__(self, enabled=None, reason=None):
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.enabled = enabled  # type: bool
        # The reason why the deletion protection feature is enabled or disabled. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoadBalancerRequestDeletionProtectionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class CreateLoadBalancerRequestLoadBalancerBillingConfig(TeaModel):
    def __init__(self, pay_type=None):
        # The billing method of the NLB instance.
        # 
        # Set the value to **PostPay**, which specifies the pay-as-you-go billing method.
        self.pay_type = pay_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoadBalancerRequestLoadBalancerBillingConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class CreateLoadBalancerRequestModificationProtectionConfig(TeaModel):
    def __init__(self, reason=None, status=None):
        # The reason why the configuration read-only mode is enabled. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        # 
        # >  This parameter takes effect only if the **Status** parameter is set to **ConsoleProtection**.
        self.reason = reason  # type: str
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: does not enable the configuration read-only mode. You cannot set the **Reason** parameter. If the **Reason** parameter is set, the value is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode. You can set the **Reason** parameter.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoadBalancerRequestModificationProtectionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class CreateLoadBalancerRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoadBalancerRequestTag, self).to_map()
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


class CreateLoadBalancerRequestZoneMappings(TeaModel):
    def __init__(self, allocation_id=None, private_ipv_4address=None, v_switch_id=None, zone_id=None):
        # The ID of the elastic IP address (EIP) that is associated with the Internet-facing NLB instance. You can specify one EIP for each zone. You must add at least two zones. You can add a maximum of 10 zones.
        self.allocation_id = allocation_id  # type: str
        # The private IP address. You must add at least two zones. You can add a maximum of 10 zones.
        self.private_ipv_4address = private_ipv_4address  # type: str
        # The vSwitch in the zone. You can specify only one vSwitch (subnet) in each zone of an NLB instance. You must add at least two zones. You can add a maximum of 10 zones.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the zone of the NLB instance. You must add at least two zones. You can add a maximum of 10 zones.
        # 
        # You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoadBalancerRequestZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateLoadBalancerRequest(TeaModel):
    def __init__(self, address_ip_version=None, address_type=None, bandwidth_package_id=None, client_token=None,
                 deletion_protection_config=None, dry_run=None, load_balancer_billing_config=None, load_balancer_name=None,
                 load_balancer_type=None, modification_protection_config=None, region_id=None, resource_group_id=None, tag=None,
                 vpc_id=None, zone_mappings=None):
        # The protocol version. Valid values:
        # 
        # *   **ipv4:** IPv4. This is the default value.
        # *   **DualStack:** dual stack.
        self.address_ip_version = address_ip_version  # type: str
        # The type of IPv4 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the virtual private cloud (VPC) where the NLB instance is deployed.
        # 
        # >  To enable a public IPv6 address for an NLB instance, call the [EnableLoadBalancerIpv6Internet](~~445878~~) operation.
        self.address_type = address_type  # type: str
        # The ID of the EIP bandwidth plan that is associated with the Internet-facing NLB instance.
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request is different.
        self.client_token = client_token  # type: str
        # The configuration of the deletion protection feature.
        self.deletion_protection_config = deletion_protection_config  # type: CreateLoadBalancerRequestDeletionProtectionConfig
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. This is the default value. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The billing settings of the NLB instance.
        self.load_balancer_billing_config = load_balancer_billing_config  # type: CreateLoadBalancerRequestLoadBalancerBillingConfig
        # The name of the NLB instance.
        # 
        # The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        self.load_balancer_name = load_balancer_name  # type: str
        # The type of the instance. Set the value to **network**, which specifies an NLB instance.
        self.load_balancer_type = load_balancer_type  # type: str
        # The configuration of the configuration read-only mode.
        self.modification_protection_config = modification_protection_config  # type: CreateLoadBalancerRequestModificationProtectionConfig
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags.
        self.tag = tag  # type: list[CreateLoadBalancerRequestTag]
        # The ID of the VPC where the NLB instance is deployed.
        self.vpc_id = vpc_id  # type: str
        # The mappings between zones and vSwitches. You must add at least two zones. You can add a maximum of 10 zones.
        self.zone_mappings = zone_mappings  # type: list[CreateLoadBalancerRequestZoneMappings]

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateLoadBalancerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = CreateLoadBalancerRequestDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = CreateLoadBalancerRequestLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = CreateLoadBalancerRequestModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateLoadBalancerRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = CreateLoadBalancerRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class CreateLoadBalancerResponseBody(TeaModel):
    def __init__(self, loadbalancer_id=None, order_id=None, request_id=None):
        # The ID of the NLB instance.
        self.loadbalancer_id = loadbalancer_id  # type: str
        # The ID of the order for the NLB instance.
        self.order_id = order_id  # type: long
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateLoadBalancerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.loadbalancer_id is not None:
            result['LoadbalancerId'] = self.loadbalancer_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LoadbalancerId') is not None:
            self.loadbalancer_id = m.get('LoadbalancerId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLoadBalancerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateLoadBalancerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateLoadBalancerResponse, self).to_map()
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
            temp_model = CreateLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSecurityPolicyRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键。最多支持128个字符，不能以`aliyun`或`acs:`开头，不能包含`http://`或`https://`。
        # 
        # 一次调用最多支持添加20个标签。
        self.key = key  # type: str
        # 标签值。最多支持128个字符，不能以`aliyun`或`acs:`开头，不能包含`http://`或`https://`。
        # 
        # 一次调用最多支持添加20个标签。
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecurityPolicyRequestTag, self).to_map()
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


class CreateSecurityPolicyRequest(TeaModel):
    def __init__(self, ciphers=None, client_token=None, dry_run=None, region_id=None, resource_group_id=None,
                 security_policy_name=None, tag=None, tls_versions=None):
        # The supported cipher suites, which are determined by the TLS protocol version. You can specify at most 32 cipher suites.
        # 
        # TLS 1.0 and TLS 1.1 support the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # 
        # TLS 1.2 supports the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # *   **ECDHE-ECDSA-AES128-GCM-SHA256**\
        # *   **ECDHE-ECDSA-AES256-GCM-SHA384**\
        # *   **ECDHE-ECDSA-AES128-SHA256**\
        # *   **ECDHE-ECDSA-AES256-SHA384**\
        # *   **ECDHE-RSA-AES128-GCM-SHA256**\
        # *   **ECDHE-RSA-AES256-GCM-SHA384**\
        # *   **ECDHE-RSA-AES128-SHA256**\
        # *   **ECDHE-RSA-AES256-SHA384**\
        # *   **AES128-GCM-SHA256**\
        # *   **AES256-GCM-SHA384**\
        # *   **AES128-SHA256**\
        # *   **AES256-SHA256**\
        # 
        # TLS 1.3 supports the following cipher suites:
        # 
        # *   **TLS_AES\_128\_GCM_SHA256**\
        # *   **TLS_AES\_256\_GCM_SHA384**\
        # *   **TLS_CHACHA20\_POLY1305\_SHA256**\
        # *   **TLS_AES\_128\_CCM_SHA256**\
        # *   **TLS_AES\_128\_CCM\_8\_SHA256**\
        self.ciphers = ciphers  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: checks the request but does not create the security policy. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The name of the security policy.
        # 
        # The name must be 1 to 200 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.security_policy_name = security_policy_name  # type: str
        # 标签列表。
        self.tag = tag  # type: list[CreateSecurityPolicyRequestTag]
        # The supported versions of the Transport Layer Security (TLS) protocol. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        self.tls_versions = tls_versions  # type: list[str]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateSecurityPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateSecurityPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')
        return self


class CreateSecurityPolicyResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, security_policy_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateSecurityPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class CreateSecurityPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateSecurityPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateSecurityPolicyResponse, self).to_map()
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
            temp_model = CreateSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServerGroupRequestHealthCheckConfig(TeaModel):
    def __init__(self, health_check_connect_port=None, health_check_connect_timeout=None,
                 health_check_domain=None, health_check_enabled=None, health_check_http_code=None, health_check_interval=None,
                 health_check_type=None, health_check_url=None, healthy_threshold=None, http_check_method=None,
                 unhealthy_threshold=None):
        # The port that you want to use for health checks on backend servers.
        # 
        # Valid values: **0** to **65535**.
        # 
        # Default value: **0**. If you set the value to 0, the port of the backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port  # type: int
        # The maximum timeout period of a health check. Unit: seconds. Valid values: **1** to **300**. Default value: **5**.
        self.health_check_connect_timeout = health_check_connect_timeout  # type: int
        # The domain name that you want to use for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the private IP address of a backend server.
        # *   **domain**: a specified domain name. The domain name must be 1 to 80 characters in length, and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain  # type: str
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true** (default)
        # *   **false**\
        self.health_check_enabled = health_check_enabled  # type: bool
        # The HTTP status codes to return for health checks. Separate multiple HTTP status codes with commas (,). Valid values: **http\_2xx** (default), **http\_3xx**, **http\_4xx**, and **http\_5xx**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code  # type: list[str]
        # The interval at which health checks are performed. Unit: seconds.
        # 
        # Valid values: **5** to **50**.
        # 
        # Default value: **10**.
        self.health_check_interval = health_check_interval  # type: int
        # The protocol that you want to use for health checks. Valid values: **TCP** (default) and **HTTP**.
        self.health_check_type = health_check_type  # type: str
        # The path to which health check requests are sent.
        # 
        # The path must be 1 to 80 characters in length, and can contain letters, digits, and the following special characters: `- / . % ? # &`. It must start with a forward slash (/).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url  # type: str
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.healthy_threshold = healthy_threshold  # type: int
        # The HTTP method that is used for health checks. Valid values: **GET** (default) and **HEAD**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method  # type: str
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.unhealthy_threshold = unhealthy_threshold  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerGroupRequestHealthCheckConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.http_check_method is not None:
            result['HttpCheckMethod'] = self.http_check_method
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('HttpCheckMethod') is not None:
            self.http_check_method = m.get('HttpCheckMethod')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class CreateServerGroupRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key  # type: str
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerGroupRequestTag, self).to_map()
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


class CreateServerGroupRequest(TeaModel):
    def __init__(self, address_ipversion=None, any_port_enabled=None, client_token=None,
                 connection_drain_enabled=None, connection_drain_timeout=None, dry_run=None, health_check_config=None,
                 preserve_client_ip_enabled=None, protocol=None, region_id=None, resource_group_id=None, scheduler=None,
                 server_group_name=None, server_group_type=None, tag=None, vpc_id=None):
        # The protocol version. Valid values:
        # 
        # *   **ipv4** (default): IPv4
        # *   **DualStack**: dual stack
        self.address_ipversion = address_ipversion  # type: str
        # Specifies whether to enable all-port forwarding. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.any_port_enabled = any_port_enabled  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.connection_drain_enabled = connection_drain_enabled  # type: bool
        # The timeout period of connection draining. Unit: seconds. Valid values: **0** to **900**.
        self.connection_drain_timeout = connection_drain_timeout  # type: int
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The configurations of the health check feature.
        self.health_check_config = health_check_config  # type: CreateServerGroupRequestHealthCheckConfig
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # *   **true**\
        # *   **false** (default)
        self.preserve_client_ip_enabled = preserve_client_ip_enabled  # type: bool
        # The protocol used to forward requests to the backend servers. Valid values:
        # 
        # *   **TCP** (default)
        # *   **UDP**\
        # *   **TCPSSL**\
        self.protocol = protocol  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr:** The weighted round-robin algorithm is used. Backend servers with higher weights receive more requests than backend servers with lower weights. This is the default value.
        # *   **rr:** The round-robin algorithm is used. Requests are forwarded to backend servers in sequence.
        # *   **sch:** Source IP hashing is used. Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch:** Four-element hashing is used. It specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hashing. Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler  # type: str
        # The name of the server group.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.server_group_name = server_group_name  # type: str
        # The type of server group. Valid values:
        # 
        # *   **Instance**: allows you to add servers of the **Ecs**, **Ens**, or **Eci** type. This is the default value.
        # *   **Ip**: allows you to add servers by specifying IP addresses.
        self.server_group_type = server_group_type  # type: str
        # The tags.
        self.tag = tag  # type: list[CreateServerGroupRequestTag]
        # The ID of the virtual private cloud (VPC) to which the server group belongs.
        # 
        # > If **ServerGroupType** is set to **Instance**, only servers in the specified VPC can be added to the server group.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateServerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.any_port_enabled is not None:
            result['AnyPortEnabled'] = self.any_port_enabled
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('AnyPortEnabled') is not None:
            self.any_port_enabled = m.get('AnyPortEnabled')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckConfig') is not None:
            temp_model = CreateServerGroupRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateServerGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateServerGroupResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, server_group_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class CreateServerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateServerGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServerGroupResponse, self).to_map()
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
            temp_model = CreateServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteListenerRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, listener_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not delete the listener. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the listener.
        self.listener_id = listener_id  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteListenerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteListenerResponse, self).to_map()
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
            temp_model = DeleteListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLoadBalancerRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to only precheck this request. Valid values:
        # 
        # *   **true**: prechecks the request without deleting the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLoadBalancerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteLoadBalancerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteLoadBalancerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLoadBalancerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteLoadBalancerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteLoadBalancerResponse, self).to_map()
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
            temp_model = DeleteLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSecurityPolicyRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, security_policy_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the available regions.
        self.region_id = region_id  # type: str
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecurityPolicyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class DeleteSecurityPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteSecurityPolicyResponseBody, self).to_map()
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


class DeleteSecurityPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteSecurityPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteSecurityPolicyResponse, self).to_map()
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
            temp_model = DeleteSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServerGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, server_group_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can only contain ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class DeleteServerGroupResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteServerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteServerGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServerGroupResponse, self).to_map()
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
            temp_model = DeleteServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, client_token=None, service_code=None):
        # The supported natural language. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        # *   **ja**: Japanese
        self.accept_language = accept_language  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # The service code. Set the value to **nlb**.
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the region service.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

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


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # A list of regions.
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


class DescribeZonesRequest(TeaModel):
    def __init__(self, accept_language=None, client_token=None, region_id=None, service_code=None):
        # The supported natural language. Valid values:
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US** (default): English
        # *   **ja**: Japanese
        self.accept_language = accept_language  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system uses **RequestId** as **ClientToken**. **RequestId** may be different for each API request.
        self.client_token = client_token  # type: str
        # The ID of the region to which the zone belongs. You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The service code. Set the value to **nlb**.
        self.service_code = service_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.service_code is not None:
            result['ServiceCode'] = self.service_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServiceCode') is not None:
            self.service_code = m.get('ServiceCode')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(self, local_name=None, zone_id=None):
        # The name of the zone.
        self.local_name = local_name  # type: str
        # The ID of the zone.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeZonesResponseBodyZones, self).to_map()
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


class DescribeZonesResponseBody(TeaModel):
    def __init__(self, request_id=None, zones=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The list of zones.
        self.zones = zones  # type: list[DescribeZonesResponseBodyZones]

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
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


class DetachCommonBandwidthPackageFromLoadBalancerRequest(TeaModel):
    def __init__(self, bandwidth_package_id=None, client_token=None, dry_run=None, load_balancer_id=None,
                 region_id=None):
        # The ID of the EIP bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not disassociate the NLB instance from the EIP bandwidth plan. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachCommonBandwidthPackageFromLoadBalancerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachCommonBandwidthPackageFromLoadBalancerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachCommonBandwidthPackageFromLoadBalancerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachCommonBandwidthPackageFromLoadBalancerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachCommonBandwidthPackageFromLoadBalancerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachCommonBandwidthPackageFromLoadBalancerResponse, self).to_map()
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
            temp_model = DetachCommonBandwidthPackageFromLoadBalancerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableLoadBalancerIpv6InternetRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableLoadBalancerIpv6InternetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableLoadBalancerIpv6InternetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableLoadBalancerIpv6InternetResponseBody, self).to_map()
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


class DisableLoadBalancerIpv6InternetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableLoadBalancerIpv6InternetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableLoadBalancerIpv6InternetResponse, self).to_map()
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
            temp_model = DisableLoadBalancerIpv6InternetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateAdditionalCertificatesWithListenerRequest(TeaModel):
    def __init__(self, additional_certificate_ids=None, client_token=None, dry_run=None, listener_id=None,
                 region_id=None):
        # The additional certificates. You can disassociate up to 15 additional certificates from a listener in each request.
        self.additional_certificate_ids = additional_certificate_ids  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The listener ID. You must specify the ID of a listener that uses SSL over TCP.
        self.listener_id = listener_id  # type: str
        # The region ID of the Network Load Balancer (NLB) instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateAdditionalCertificatesWithListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.additional_certificate_ids is not None:
            result['AdditionalCertificateIds'] = self.additional_certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AdditionalCertificateIds') is not None:
            self.additional_certificate_ids = m.get('AdditionalCertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisassociateAdditionalCertificatesWithListenerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateAdditionalCertificatesWithListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateAdditionalCertificatesWithListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisassociateAdditionalCertificatesWithListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisassociateAdditionalCertificatesWithListenerResponse, self).to_map()
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
            temp_model = DisassociateAdditionalCertificatesWithListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableLoadBalancerIpv6InternetRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not change the network type of the NLB instance. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableLoadBalancerIpv6InternetRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableLoadBalancerIpv6InternetResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableLoadBalancerIpv6InternetResponseBody, self).to_map()
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


class EnableLoadBalancerIpv6InternetResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableLoadBalancerIpv6InternetResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableLoadBalancerIpv6InternetResponse, self).to_map()
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
            temp_model = EnableLoadBalancerIpv6InternetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobStatusRequest(TeaModel):
    def __init__(self, client_token=None, job_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class GetJobStatusResponseBody(TeaModel):
    def __init__(self, request_id=None, status=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The state of the task. Valid values:
        # 
        # *   **Succeeded**: The task is successful.
        # *   **processing**: The ticket is being executed.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetJobStatusResponseBody, self).to_map()
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


class GetJobStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetJobStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetJobStatusResponse, self).to_map()
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
            temp_model = GetJobStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListenerAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, listener_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** of each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: checks the request but does not query the listener details. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the listener.
        self.listener_id = listener_id  # type: str
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetListenerAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetListenerAttributeResponseBodyProxyProtocolV2Config(TeaModel):
    def __init__(self, ppv_2private_link_ep_id_enabled=None, ppv_2private_link_eps_id_enabled=None,
                 ppv_2vpc_id_enabled=None):
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled  # type: bool
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled  # type: bool
        self.ppv_2vpc_id_enabled = ppv_2vpc_id_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetListenerAttributeResponseBodyProxyProtocolV2Config, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ppv_2private_link_ep_id_enabled is not None:
            result['Ppv2PrivateLinkEpIdEnabled'] = self.ppv_2private_link_ep_id_enabled
        if self.ppv_2private_link_eps_id_enabled is not None:
            result['Ppv2PrivateLinkEpsIdEnabled'] = self.ppv_2private_link_eps_id_enabled
        if self.ppv_2vpc_id_enabled is not None:
            result['Ppv2VpcIdEnabled'] = self.ppv_2vpc_id_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ppv2PrivateLinkEpIdEnabled') is not None:
            self.ppv_2private_link_ep_id_enabled = m.get('Ppv2PrivateLinkEpIdEnabled')
        if m.get('Ppv2PrivateLinkEpsIdEnabled') is not None:
            self.ppv_2private_link_eps_id_enabled = m.get('Ppv2PrivateLinkEpsIdEnabled')
        if m.get('Ppv2VpcIdEnabled') is not None:
            self.ppv_2vpc_id_enabled = m.get('Ppv2VpcIdEnabled')
        return self


class GetListenerAttributeResponseBodyTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The key of the tag that you want to remove. You can remove up to 20 tags in each call.
        self.tag_key = tag_key  # type: str
        # The value of the tag.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetListenerAttributeResponseBodyTags, self).to_map()
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


class GetListenerAttributeResponseBody(TeaModel):
    def __init__(self, alpn_enabled=None, alpn_policy=None, ca_certificate_ids=None, ca_enabled=None,
                 certificate_ids=None, cps=None, end_port=None, idle_timeout=None, listener_description=None, listener_id=None,
                 listener_port=None, listener_protocol=None, listener_status=None, load_balancer_id=None, mss=None,
                 proxy_protocol_enabled=None, proxy_protocol_v2config=None, region_id=None, request_id=None, sec_sensor_enabled=None,
                 security_policy_id=None, server_group_id=None, start_port=None, tags=None):
        # Indicates whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.alpn_enabled = alpn_enabled  # type: bool
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**\
        # *   **HTTP2Only**\
        # *   **HTTP2Preferred**\
        # *   **HTTP2Optional**\
        self.alpn_policy = alpn_policy  # type: str
        # The CA certificates. Only one CA certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids  # type: list[str]
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ca_enabled = ca_enabled  # type: bool
        # The server certificates. Only one server certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps  # type: int
        # The last port in the listening port range. Valid values: **0** to **65535**. The number of the last port must be smaller than that of the first port.
        self.end_port = end_port  # type: str
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**.
        self.idle_timeout = idle_timeout  # type: int
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description  # type: str
        # The ID of the listener.
        self.listener_id = listener_id  # type: str
        # The listening port. Valid values: **0** to **65535**. A value of **0** specifies all ports. If you set the value to **0**, you must also set the **StartPort** and **EndPort** parameters.
        self.listener_port = listener_port  # type: int
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**: The listener is being created.
        # *   **Running**: The listener is running.
        # *   **Configuring**: The listener is being configured.
        # *   **Stopping**: The listener is being stopped.
        # *   **Stopped**: The listener is stopped.
        # *   **Starting**: The listener is being started.
        # *   **Deleting**: The listener is being deleted.
        # *   **Deleted**: The listener is deleted.
        self.listener_status = listener_status  # type: str
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The size of the largest TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged.
        # 
        # >  This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss  # type: int
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_enabled = proxy_protocol_enabled  # type: bool
        self.proxy_protocol_v2config = proxy_protocol_v2config  # type: GetListenerAttributeResponseBodyProxyProtocolV2Config
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # Indicates whether fine-grained monitoring is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sec_sensor_enabled = sec_sensor_enabled  # type: bool
        # The ID of the security policy. System security policies and custom security policies are supported.
        # 
        # Valid values: **tls_cipher_policy\_1\_0**, **tls_cipher_policy\_1\_1**, **tls_cipher_policy\_1\_2**, **tls_cipher_policy\_1\_2\_strict**, and **tls_cipher_policy\_1\_2\_strict_with\_1\_3**.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str
        # The first port in the listening port range. Valid values: **0** to **65535**.
        self.start_port = start_port  # type: str
        # The tags.
        self.tags = tags  # type: list[GetListenerAttributeResponseBodyTags]

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetListenerAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.proxy_protocol_v2config is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('ProxyProtocolV2Config') is not None:
            temp_model = GetListenerAttributeResponseBodyProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m['ProxyProtocolV2Config'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetListenerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class GetListenerAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetListenerAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetListenerAttributeResponse, self).to_map()
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
            temp_model = GetListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListenerHealthStatusRequest(TeaModel):
    def __init__(self, listener_id=None, max_results=None, next_token=None, region_id=None):
        # The ID of the listener of the NLB instance.
        self.listener_id = listener_id  # type: str
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetListenerHealthStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason(TeaModel):
    def __init__(self, reason_code=None):
        # The reason why the **status** is abnormal. Valid values:
        # 
        # *   **CONNECT_TIMEOUT**: The NLB instance failed to connect to the backend server within the specified period of time.
        # *   **CONNECT_FAILED**: The NLB instance failed to connect to the backend server.
        # *   **RECV_RESPONSE_TIMEOUT**: The NLB instance failed to receive a response from the backend server within the specified period of time.
        # *   **CONNECT_INTERRUPT**: The connection between the health check and the backend servers was interrupted.
        # *   **HTTP_CODE_NOT_MATCH**: The HTTP status code from the backend servers was not the expected one.
        # *   **HTTP_INVALID_HEADER**: The format of the response from the backend servers is invalid.
        self.reason_code = reason_code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reason_code is not None:
            result['ReasonCode'] = self.reason_code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ReasonCode') is not None:
            self.reason_code = m.get('ReasonCode')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers(TeaModel):
    def __init__(self, port=None, reason=None, server_id=None, server_ip=None, status=None):
        # The backend port.
        self.port = port  # type: int
        # The cause of the health check failure.
        self.reason = reason  # type: GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason
        # The ID of the backend server.
        self.server_id = server_id  # type: str
        # The IP address of the backend server.
        self.server_ip = server_ip  # type: str
        # The health check status. Valid values:
        # 
        # *   **Initial**: indicates that health checks are configured for the NLB instance, but no data was found.
        # *   **Unhealthy**: indicates that the backend server consecutively fails health checks.
        # *   **Unused**: indicates that the weight of the backend server is 0.
        # *   **Unavailable**: indicates that health checks are disabled.
        self.status = status  # type: str

    def validate(self):
        if self.reason:
            self.reason.validate()

    def to_map(self):
        _map = super(GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.reason is not None:
            result['Reason'] = self.reason.to_map()
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Reason') is not None:
            temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServersReason()
            self.reason = temp_model.from_map(m['Reason'])
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos(TeaModel):
    def __init__(self, heath_check_enabled=None, non_normal_servers=None, server_group_id=None):
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.heath_check_enabled = heath_check_enabled  # type: bool
        # A list of unhealthy backend servers.
        self.non_normal_servers = non_normal_servers  # type: list[GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers]
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        if self.non_normal_servers:
            for k in self.non_normal_servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.heath_check_enabled is not None:
            result['HeathCheckEnabled'] = self.heath_check_enabled
        result['NonNormalServers'] = []
        if self.non_normal_servers is not None:
            for k in self.non_normal_servers:
                result['NonNormalServers'].append(k.to_map() if k else None)
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HeathCheckEnabled') is not None:
            self.heath_check_enabled = m.get('HeathCheckEnabled')
        self.non_normal_servers = []
        if m.get('NonNormalServers') is not None:
            for k in m.get('NonNormalServers'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfosNonNormalServers()
                self.non_normal_servers.append(temp_model.from_map(k))
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class GetListenerHealthStatusResponseBodyListenerHealthStatus(TeaModel):
    def __init__(self, listener_id=None, listener_port=None, listener_protocol=None, server_group_infos=None):
        # The ID of the listener of the NLB instance.
        self.listener_id = listener_id  # type: str
        # The listening port.
        self.listener_port = listener_port  # type: int
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The information about the server groups.
        self.server_group_infos = server_group_infos  # type: list[GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos]

    def validate(self):
        if self.server_group_infos:
            for k in self.server_group_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetListenerHealthStatusResponseBodyListenerHealthStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        result['ServerGroupInfos'] = []
        if self.server_group_infos is not None:
            for k in self.server_group_infos:
                result['ServerGroupInfos'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        self.server_group_infos = []
        if m.get('ServerGroupInfos') is not None:
            for k in m.get('ServerGroupInfos'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatusServerGroupInfos()
                self.server_group_infos.append(temp_model.from_map(k))
        return self


class GetListenerHealthStatusResponseBody(TeaModel):
    def __init__(self, listener_health_status=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        # The health check status of the server groups that are associated with the listener.
        self.listener_health_status = listener_health_status  # type: list[GetListenerHealthStatusResponseBodyListenerHealthStatus]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # - If **NextToken** is empty, it indicates that no next query is to be sent.
        # - If a value of **NextToken** is returned, the value is the token used for the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.listener_health_status:
            for k in self.listener_health_status:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetListenerHealthStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ListenerHealthStatus'] = []
        if self.listener_health_status is not None:
            for k in self.listener_health_status:
                result['ListenerHealthStatus'].append(k.to_map() if k else None)
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
        self.listener_health_status = []
        if m.get('ListenerHealthStatus') is not None:
            for k in m.get('ListenerHealthStatus'):
                temp_model = GetListenerHealthStatusResponseBodyListenerHealthStatus()
                self.listener_health_status.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetListenerHealthStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetListenerHealthStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetListenerHealthStatusResponse, self).to_map()
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
            temp_model = GetListenerHealthStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoadBalancerAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among all requests. ClientToken can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, **ClientToken** is set to the value of **RequestId**. The value of **RequestId** for each API request may be different.
        self.client_token = client_token  # type: str
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: checks the request but does not query the listener details. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig(TeaModel):
    def __init__(self, enabled=None, enabled_time=None, reason=None):
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.enabled = enabled  # type: bool
        # The time when the deletion protection feature was enabled. The time follows the ISO 8601 standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time is displayed in UTC.
        self.enabled_time = enabled_time  # type: str
        # The reason why the deletion protection feature is enabled or disabled. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig(TeaModel):
    def __init__(self, pay_type=None):
        # The billing method of the NLB instance. Set the value to **PostPay**, which specifies the pay-as-you-go billing method.
        self.pay_type = pay_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class GetLoadBalancerAttributeResponseBodyModificationProtectionConfig(TeaModel):
    def __init__(self, enabled_time=None, reason=None, status=None):
        # The time when the modification protection feature was enabled. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.enabled_time = enabled_time  # type: str
        # The reason why the configuration read-only mode is enabled. The value must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The value must start with a letter.
        # 
        # >  This parameter takes effect only if the **Status** parameter is set to **ConsoleProtection**.
        self.reason = reason  # type: str
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: does not enable the configuration read-only mode. You cannot set the **Reason** parameter. If the **Reason** parameter is set, the value is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode. You can set the **Reason** parameter.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyModificationProtectionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLoadBalancerAttributeResponseBodyOperationLocks(TeaModel):
    def __init__(self, lock_reason=None, lock_type=None):
        # The reason why the NLB instance is locked.
        self.lock_reason = lock_reason  # type: str
        # The type of the lock. Valid values:
        # 
        # *   **SecurityLocked**: The NLB instance is locked due to security reasons.
        # *   **RelatedResourceLocked**: The NLB instance is locked due to other resources associated with the NLB instance.
        # *   **FinancialLocked**: The NLB instance is locked due to overdue payments.
        # *   **ResidualLocked**: The NLB instance is locked because the associated resources have overdue payments and the resources are released.
        self.lock_type = lock_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyOperationLocks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        return self


class GetLoadBalancerAttributeResponseBodyTags(TeaModel):
    def __init__(self, tag_key=None, tag_value=None):
        # The tag key.
        self.tag_key = tag_key  # type: str
        # The tag value.
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyTags, self).to_map()
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


class GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses(TeaModel):
    def __init__(self, allocation_id=None, eni_id=None, ipv_6address=None, private_ipv_4address=None,
                 private_ipv_4hc_status=None, private_ipv_6hc_status=None, public_ipv_4address=None):
        # The ID of the elastic IP address (EIP).
        self.allocation_id = allocation_id  # type: str
        # The ID of the elastic network interface (ENI).
        self.eni_id = eni_id  # type: str
        # The IPv6 address of the NLB instance.
        self.ipv_6address = ipv_6address  # type: str
        # The private IPv4 address of the NLB instance.
        self.private_ipv_4address = private_ipv_4address  # type: str
        # The health status of the private IPv4 address of the NLB instance. Valid values:
        # 
        # *   **Healthy**\
        # *   **Unhealthy**\
        # 
        # > This parameter is returned only when the **Status** of the zone is **Active**.
        self.private_ipv_4hc_status = private_ipv_4hc_status  # type: str
        # The health status of the IPv6 address of the NLB instance. Valid values:
        # 
        # *   **Healthy**\
        # *   **Unhealthy**\
        # 
        # > This parameter is returned only when the **Status** of the zone is **Active**.
        self.private_ipv_6hc_status = private_ipv_6hc_status  # type: str
        # The public IPv4 address of the NLB instance.
        self.public_ipv_4address = public_ipv_4address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.private_ipv_4hc_status is not None:
            result['PrivateIPv4HcStatus'] = self.private_ipv_4hc_status
        if self.private_ipv_6hc_status is not None:
            result['PrivateIPv6HcStatus'] = self.private_ipv_6hc_status
        if self.public_ipv_4address is not None:
            result['PublicIPv4Address'] = self.public_ipv_4address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('PrivateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('PrivateIPv4HcStatus')
        if m.get('PrivateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('PrivateIPv6HcStatus')
        if m.get('PublicIPv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIPv4Address')
        return self


class GetLoadBalancerAttributeResponseBodyZoneMappings(TeaModel):
    def __init__(self, load_balancer_addresses=None, status=None, v_switch_id=None, zone_id=None):
        # The information about the IP addresses used by the NLB instance.
        self.load_balancer_addresses = load_balancer_addresses  # type: list[GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses]
        # The zone status. Valid values:
        # 
        # *   **Active**: The zone is available.
        # *   **Stopped**: The zone is disabled. You can set the zone to this status only by using Cloud Architect Design Tools (CADT).
        # *   **Shifted**: The DNS record is removed.
        # *   **Starting**: The zone is being enabled. You can set the zone to this status only by using CADT.
        # *   **Stopping** You can set the zone to this status only by using CADT.
        self.status = status  # type: str
        # The ID of the vSwitch in the zone. By default, each zone contains one vSwitch and one subnet.
        self.v_switch_id = v_switch_id  # type: str
        # The ID of the zone. You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.load_balancer_addresses:
            for k in self.load_balancer_addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBodyZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k in m.get('LoadBalancerAddresses'):
                temp_model = GetLoadBalancerAttributeResponseBodyZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(self, address_ip_version=None, address_type=None, bandwidth_package_id=None, cps=None,
                 create_time=None, cross_zone_enabled=None, dnsname=None, deletion_protection_config=None,
                 ipv_6address_type=None, load_balancer_billing_config=None, load_balancer_business_status=None,
                 load_balancer_id=None, load_balancer_name=None, load_balancer_status=None, load_balancer_type=None,
                 modification_protection_config=None, operation_locks=None, region_id=None, request_id=None, resource_group_id=None,
                 security_group_ids=None, tags=None, vpc_id=None, zone_mappings=None):
        # The protocol version. Valid values:
        # 
        # *   **ipv4**: IPv4
        # *   **DualStack**: dual stack
        self.address_ip_version = address_ip_version  # type: str
        # The IPv4 network type of the NLB instance. Valid values:
        # 
        # *   **Internet** The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet** The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC in which the NLB instance is deployed.
        self.address_type = address_type  # type: str
        # The ID of the EIP bandwidth plan.
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        # The maximum number of connections per second that can be created on the NLB instance. Valid values: **0** to **1000000**.
        # 
        # **0** indicates that the number of connections is unlimited.
        self.cps = cps  # type: int
        # The time when the NLB instance was created. This value is a UNIX timestamp.
        # 
        # Unit: milliseconds.
        self.create_time = create_time  # type: str
        # Indicates whether the NLB instance is accessible across zones. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.cross_zone_enabled = cross_zone_enabled  # type: bool
        # The domain name of the NLB instance.
        self.dnsname = dnsname  # type: str
        # The configuration of the deletion protection feature.
        self.deletion_protection_config = deletion_protection_config  # type: GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig
        # The IPv6 network type of the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. In this case, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.ipv_6address_type = ipv_6address_type  # type: str
        # The billing information of the NLB instance.
        self.load_balancer_billing_config = load_balancer_billing_config  # type: GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig
        # The status of workloads on the NLB instance. Valid values:
        # 
        # *   **Abnormal**\
        # *   **Normal**\
        self.load_balancer_business_status = load_balancer_business_status  # type: str
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The NLB instance name.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.load_balancer_name = load_balancer_name  # type: str
        # The NLB instance status. Valid values:
        # 
        # *   **Inactive**: The NLB instance is disabled. The listeners of NLB instances in the Inactive state do not forward traffic.
        # *   **Active**: The NLB instance is running.
        # *   **Provisioning**: The NLB instance is being created.
        # *   **Configuring**: The NLB instance is being modified.
        # *   **CreateFailed**: The system failed to create the NLB instance. In this case, you are not charged for the NLB instance. You can only delete the NLB instance.
        self.load_balancer_status = load_balancer_status  # type: str
        # The type of the Server Load Balancer (SLB) instance. Set the value to **network**, which specifies NLB.
        self.load_balancer_type = load_balancer_type  # type: str
        # The configuration of the configuration read-only mode.
        self.modification_protection_config = modification_protection_config  # type: GetLoadBalancerAttributeResponseBodyModificationProtectionConfig
        # The information about the locked NLB instance. This parameter is returned only when `LoadBalancerBussinessStatus` is **Abnormal**.
        self.operation_locks = operation_locks  # type: list[GetLoadBalancerAttributeResponseBodyOperationLocks]
        # The region ID of the NLB instance.
        self.region_id = region_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the security group associated with the NLB instance.
        self.security_group_ids = security_group_ids  # type: list[str]
        # The tags.
        self.tags = tags  # type: list[GetLoadBalancerAttributeResponseBodyTags]
        # The VPC ID of the NLB instance.
        self.vpc_id = vpc_id  # type: str
        # The list of zones and vSwitches in the zones. You must specify 2 to 10 zones.
        self.zone_mappings = zone_mappings  # type: list[GetLoadBalancerAttributeResponseBodyZoneMappings]

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.operation_locks:
            for k in self.operation_locks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        result['OperationLocks'] = []
        if self.operation_locks is not None:
            for k in self.operation_locks:
                result['OperationLocks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = GetLoadBalancerAttributeResponseBodyModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        self.operation_locks = []
        if m.get('OperationLocks') is not None:
            for k in m.get('OperationLocks'):
                temp_model = GetLoadBalancerAttributeResponseBodyOperationLocks()
                self.operation_locks.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetLoadBalancerAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = GetLoadBalancerAttributeResponseBodyZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class GetLoadBalancerAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetLoadBalancerAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetLoadBalancerAttributeResponse, self).to_map()
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
            temp_model = GetLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenerCertificatesRequest(TeaModel):
    def __init__(self, cert_type=None, listener_id=None, max_results=None, next_token=None, region_id=None):
        # The type of the certificate. Valid values:
        # 
        # *   **Server**: a server certificate.
        # *   **Ca**: Certificate Authority Certificate
        self.cert_type = cert_type  # type: str
        # The ID of the listener. Specify the ID of a listener that uses SSL over TCP.
        self.listener_id = listener_id  # type: str
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The ID of the region where the Network Load Balancer (NLB) instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenerCertificatesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListListenerCertificatesResponseBodyCertificates(TeaModel):
    def __init__(self, certificate_id=None, certificate_type=None, is_default=None, status=None):
        # The ID of the certificate.
        self.certificate_id = certificate_id  # type: str
        # The type of the certificate.
        # 
        # -  Server
        # - Ca
        self.certificate_type = certificate_type  # type: str
        # Indicates whether the certificate is the default certificate of the listener. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_default = is_default  # type: bool
        # Indicates whether the certificate is associated with the listener. Valid values:
        # 
        # *   **Associating**\
        # *   **Associated**\
        # *   **Diassociating**\
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenerCertificatesResponseBodyCertificates, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_id is not None:
            result['CertificateId'] = self.certificate_id
        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CertificateId') is not None:
            self.certificate_id = m.get('CertificateId')
        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListListenerCertificatesResponseBody(TeaModel):
    def __init__(self, certificate_ids=None, certificates=None, max_results=None, next_token=None, request_id=None,
                 total_count=None):
        # The server certificates.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The certificates.
        self.certificates = certificates  # type: list[ListListenerCertificatesResponseBodyCertificates]
        # The number of entries returned per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.certificates:
            for k in self.certificates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenerCertificatesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        result['Certificates'] = []
        if self.certificates is not None:
            for k in self.certificates:
                result['Certificates'].append(k.to_map() if k else None)
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
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        self.certificates = []
        if m.get('Certificates') is not None:
            for k in m.get('Certificates'):
                temp_model = ListListenerCertificatesResponseBodyCertificates()
                self.certificates.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenerCertificatesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListListenerCertificatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenerCertificatesResponse, self).to_map()
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
            temp_model = ListListenerCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListListenersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The value of the tag. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersRequestTag, self).to_map()
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


class ListListenersRequest(TeaModel):
    def __init__(self, listener_ids=None, listener_protocol=None, load_balancer_ids=None, max_results=None,
                 next_token=None, region_id=None, tag=None):
        # The listener IDs.
        self.listener_ids = listener_ids  # type: list[str]
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The ID of the NLB instance. You can query up to 20 NLB instances at a time.
        self.load_balancer_ids = load_balancer_ids  # type: list[str]
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The tags.
        self.tag = tag  # type: list[ListListenersRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_ids is not None:
            result['ListenerIds'] = self.listener_ids
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerIds') is not None:
            self.listener_ids = m.get('ListenerIds')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListListenersRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListListenersResponseBodyListenersProxyProtocolV2Config(TeaModel):
    def __init__(self, ppv_2private_link_ep_id_enabled=None, ppv_2private_link_eps_id_enabled=None,
                 ppv_2vpc_id_enabled=None):
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled  # type: bool
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled  # type: bool
        self.ppv_2vpc_id_enabled = ppv_2vpc_id_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersProxyProtocolV2Config, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ppv_2private_link_ep_id_enabled is not None:
            result['Ppv2PrivateLinkEpIdEnabled'] = self.ppv_2private_link_ep_id_enabled
        if self.ppv_2private_link_eps_id_enabled is not None:
            result['Ppv2PrivateLinkEpsIdEnabled'] = self.ppv_2private_link_eps_id_enabled
        if self.ppv_2vpc_id_enabled is not None:
            result['Ppv2VpcIdEnabled'] = self.ppv_2vpc_id_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ppv2PrivateLinkEpIdEnabled') is not None:
            self.ppv_2private_link_ep_id_enabled = m.get('Ppv2PrivateLinkEpIdEnabled')
        if m.get('Ppv2PrivateLinkEpsIdEnabled') is not None:
            self.ppv_2private_link_eps_id_enabled = m.get('Ppv2PrivateLinkEpsIdEnabled')
        if m.get('Ppv2VpcIdEnabled') is not None:
            self.ppv_2vpc_id_enabled = m.get('Ppv2VpcIdEnabled')
        return self


class ListListenersResponseBodyListenersTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag option.
        # 
        # The value can be up to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListListenersResponseBodyListenersTags, self).to_map()
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


class ListListenersResponseBodyListeners(TeaModel):
    def __init__(self, alpn_enabled=None, alpn_policy=None, ca_certificate_ids=None, ca_enabled=None,
                 certificate_ids=None, cps=None, end_port=None, idle_timeout=None, listener_description=None, listener_id=None,
                 listener_port=None, listener_protocol=None, listener_status=None, load_balancer_id=None, mss=None,
                 proxy_protocol_enabled=None, proxy_protocol_v2config=None, region_id=None, sec_sensor_enabled=None,
                 security_policy_id=None, server_group_id=None, start_port=None, tags=None):
        # Indicates whether Application-Layer Protocol Negotiation (ALPN) is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.alpn_enabled = alpn_enabled  # type: bool
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**\
        # *   **HTTP2Only**\
        # *   **HTTP2Preferred**\
        # *   **HTTP2Optional**\
        self.alpn_policy = alpn_policy  # type: str
        # The list of CA certificates.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids  # type: list[str]
        # Indicates whether mutual authentication is enabled. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ca_enabled = ca_enabled  # type: bool
        # The list of server certificates.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** indicates that the number of connections is unlimited.
        self.cps = cps  # type: int
        # The last port in the listening port range.
        self.end_port = end_port  # type: str
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**. Default value: **900**.
        self.idle_timeout = idle_timeout  # type: int
        # The name of the listener.
        # 
        # The name must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description  # type: str
        # The ID of the listener.
        self.listener_id = listener_id  # type: str
        # The listening port.
        self.listener_port = listener_port  # type: int
        # The listening protocol. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The status of the listener. Valid values:
        # 
        # *   **Provisioning**\
        # *   **Running**\
        # *   **Configuring**\
        # *   **Stopping**\
        # *   **Stopped**\
        # *   **Starting**\
        # *   **Deleting**\
        # *   **Deleted**\
        self.listener_status = listener_status  # type: str
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The maximum size of a TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** indicates that the maximum segment size remains unchanged.
        # 
        # >  This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss  # type: int
        # Indicates whether the Proxy protocol is used to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.proxy_protocol_enabled = proxy_protocol_enabled  # type: bool
        self.proxy_protocol_v2config = proxy_protocol_v2config  # type: ListListenersResponseBodyListenersProxyProtocolV2Config
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id  # type: str
        # Indicates whether fine-grained monitoring is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.sec_sensor_enabled = sec_sensor_enabled  # type: bool
        # The ID of the security policy.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str
        # The first port in the listening port range.
        self.start_port = start_port  # type: str
        # The tag key.
        self.tags = tags  # type: list[ListListenersResponseBodyListenersTags]

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersResponseBodyListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.end_port is not None:
            result['EndPort'] = self.end_port
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.listener_status is not None:
            result['ListenerStatus'] = self.listener_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.proxy_protocol_v2config is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.start_port is not None:
            result['StartPort'] = self.start_port
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('EndPort') is not None:
            self.end_port = m.get('EndPort')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('ListenerStatus') is not None:
            self.listener_status = m.get('ListenerStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('ProxyProtocolV2Config') is not None:
            temp_model = ListListenersResponseBodyListenersProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m['ProxyProtocolV2Config'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('StartPort') is not None:
            self.start_port = m.get('StartPort')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListListenersResponseBodyListenersTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListListenersResponseBody(TeaModel):
    def __init__(self, listeners=None, max_results=None, next_token=None, request_id=None, total_count=None):
        # The list of listeners.
        self.listeners = listeners  # type: list[ListListenersResponseBodyListeners]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If **NextToken** is empty, it indicates that no next query is to be sent.
        # *   If a value of **NextToken** is returned, the value is the token used for the next query.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.listeners:
            for k in self.listeners:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListListenersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Listeners'] = []
        if self.listeners is not None:
            for k in self.listeners:
                result['Listeners'].append(k.to_map() if k else None)
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
        self.listeners = []
        if m.get('Listeners') is not None:
            for k in m.get('Listeners'):
                temp_model = ListListenersResponseBodyListeners()
                self.listeners.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListListenersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListListenersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListListenersResponse, self).to_map()
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
            temp_model = ListListenersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLoadBalancersRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The value of the tag. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag value cannot contain `http://` or `https://`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersRequestTag, self).to_map()
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


class ListLoadBalancersRequest(TeaModel):
    def __init__(self, address_ip_version=None, address_type=None, dnsname=None, ipv_6address_type=None,
                 load_balancer_business_status=None, load_balancer_ids=None, load_balancer_names=None, load_balancer_status=None,
                 load_balancer_type=None, max_results=None, next_token=None, region_id=None, resource_group_id=None, tag=None,
                 vpc_ids=None, zone_id=None):
        # The protocol version. Valid values:
        # 
        # *   **ipv4**: IPv4
        # *   **DualStack**: dual stack
        self.address_ip_version = address_ip_version  # type: str
        # The type of IPv4 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.address_type = address_type  # type: str
        # The domain name of the NLB instance.
        self.dnsname = dnsname  # type: str
        # The type of IPv6 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.ipv_6address_type = ipv_6address_type  # type: str
        # The business status of the NLB instance. Valid values:
        # 
        # *   **Abnormal**: The NLB instance is not working as expected.
        # *   **Normal**: The NLB instance is working as expected.
        self.load_balancer_business_status = load_balancer_business_status  # type: str
        # The ID of the NLB instance. You can query up to 20 NLB instances at a time.
        self.load_balancer_ids = load_balancer_ids  # type: list[str]
        # The name of the NLB instance. You can specify up to 20 names at a time.
        self.load_balancer_names = load_balancer_names  # type: list[str]
        # The status of the NLB instance. Valid values:
        # 
        # *   **Inactive**: The NLB instance is disabled. Listeners of NLB instances in the Inactive state do not forward traffic.
        # *   **Active**: The NLB instance is running.
        # *   **Provisioning**: The NLB instance is being created.
        # *   **Configuring**: The NLB instance is being modified.
        # *   **Deleting**: The NLB instance is being deleted.
        # *   **Deleted**: The NLB instance is deleted.
        self.load_balancer_status = load_balancer_status  # type: str
        # The type of the Server Load Balancer (SLB) instance. Set the value to **network**, which specifies NLB.
        self.load_balancer_type = load_balancer_type  # type: str
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If this is your first query and no subsequent queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The tags of the NLB instance.
        self.tag = tag  # type: list[ListLoadBalancersRequestTag]
        # The ID of the virtual private cloud (VPC) where the NLB instance is deployed. You can specify up to 10 VPC IDs at a time.
        self.vpc_ids = vpc_ids  # type: list[str]
        # The name of the zone. You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLoadBalancersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status
        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids
        if self.load_balancer_names is not None:
            result['LoadBalancerNames'] = self.load_balancer_names
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_ids is not None:
            result['VpcIds'] = self.vpc_ids
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')
        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')
        if m.get('LoadBalancerNames') is not None:
            self.load_balancer_names = m.get('LoadBalancerNames')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListLoadBalancersRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcIds') is not None:
            self.vpc_ids = m.get('VpcIds')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig(TeaModel):
    def __init__(self, enabled=None, enabled_time=None, reason=None):
        # Indicates whether deletion protection is enabled. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.enabled = enabled  # type: bool
        # The time when deletion protection was enabled. The time is displayed in UTC in `yyyy-MM-ddTHH:mm:ssZ` format.
        self.enabled_time = enabled_time  # type: str
        # The reason why the deletion protection feature is enabled or disabled. The reason must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The reason must start with a letter.
        self.reason = reason  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        return self


class ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig(TeaModel):
    def __init__(self, pay_type=None):
        # The billing method of the NLB instance. Only **PostPay** is supported, which indicates the pay-as-you-go billing method.
        self.pay_type = pay_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pay_type is not None:
            result['PayType'] = self.pay_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')
        return self


class ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig(TeaModel):
    def __init__(self, enabled_time=None, reason=None, status=None):
        # The time when the configuration read-only mode was enabled. The time is displayed in UTC in `yyyy-MM-ddTHH:mm:ssZ` format.
        self.enabled_time = enabled_time  # type: str
        # The reason why the configuration read-only mode is enabled. The reason must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The reason must start with a letter.
        # 
        # This parameter takes effect only if **Status** is set to **ConsoleProtection**.
        self.reason = reason  # type: str
        # Indicates whether the configuration read-only mode is enabled. Valid values:
        # 
        # *   **NonProtection**: disabled. In this case, **Reason** is not returned. If **Reason** is set, the value is cleared.
        # *   **ConsoleProtection**: enabled. In this case, **Reason** is returned.
        # 
        # >  If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_time is not None:
            result['EnabledTime'] = self.enabled_time
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnabledTime') is not None:
            self.enabled_time = m.get('EnabledTime')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListLoadBalancersResponseBodyLoadBalancersOperationLocks(TeaModel):
    def __init__(self, lock_reason=None, lock_type=None):
        # The reason why the NLB instance is locked.
        self.lock_reason = lock_reason  # type: str
        # The type of lock. Valid values:
        # 
        # *   **SecurityLocked**: The NLB instance is locked due to security reasons.
        # *   **RelatedResourceLocked**: The NLB instance is locked due to association issues.
        # *   **FinancialLocked**: The NLB instance is locked due to overdue payments.
        # *   **ResidualLocked**: The NLB instance is locked because the payments of the associated resources are overdue and the resources are released.
        self.lock_type = lock_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersOperationLocks, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lock_reason is not None:
            result['LockReason'] = self.lock_reason
        if self.lock_type is not None:
            result['LockType'] = self.lock_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LockReason') is not None:
            self.lock_reason = m.get('LockReason')
        if m.get('LockType') is not None:
            self.lock_type = m.get('LockType')
        return self


class ListLoadBalancersResponseBodyLoadBalancersTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key.
        self.key = key  # type: str
        # The tag value.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersTags, self).to_map()
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


class ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses(TeaModel):
    def __init__(self, allocation_id=None, eni_id=None, ipv_6address=None, private_ipv_4address=None,
                 private_ipv_4hc_status=None, private_ipv_6hc_status=None, public_ipv_4address=None):
        # The ID of the elastic IP address (EIP).
        self.allocation_id = allocation_id  # type: str
        # The ID of the elastic network interface (ENI) attached to the NLB instance.
        self.eni_id = eni_id  # type: str
        # The IPv6 address used by the NLB instance.
        self.ipv_6address = ipv_6address  # type: str
        # The private IPv4 address of the NLB instance.
        self.private_ipv_4address = private_ipv_4address  # type: str
        # The health check status of the private IPv4 address.
        self.private_ipv_4hc_status = private_ipv_4hc_status  # type: str
        # The health check status of the private IPv6 address.
        self.private_ipv_6hc_status = private_ipv_6hc_status  # type: str
        # The public IPv4 address of the NLB instance.
        self.public_ipv_4address = public_ipv_4address  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eni_id is not None:
            result['EniId'] = self.eni_id
        if self.ipv_6address is not None:
            result['Ipv6Address'] = self.ipv_6address
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.private_ipv_4hc_status is not None:
            result['PrivateIPv4HcStatus'] = self.private_ipv_4hc_status
        if self.private_ipv_6hc_status is not None:
            result['PrivateIPv6HcStatus'] = self.private_ipv_6hc_status
        if self.public_ipv_4address is not None:
            result['PublicIPv4Address'] = self.public_ipv_4address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')
        if m.get('Ipv6Address') is not None:
            self.ipv_6address = m.get('Ipv6Address')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('PrivateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('PrivateIPv4HcStatus')
        if m.get('PrivateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('PrivateIPv6HcStatus')
        if m.get('PublicIPv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIPv4Address')
        return self


class ListLoadBalancersResponseBodyLoadBalancersZoneMappings(TeaModel):
    def __init__(self, load_balancer_addresses=None, status=None, v_switch_id=None, zone_id=None):
        # The IP addresses that are used by the NLB instance.
        self.load_balancer_addresses = load_balancer_addresses  # type: list[ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses]
        # The state of the task. Valid values:
        # 
        # *   **Succeeded**: The task is successful.
        # *   **processing**: The ticket is being executed.
        self.status = status  # type: str
        # The ID of the vSwitch in the zone. By default, each zone contains one vSwitch and one subnet.
        self.v_switch_id = v_switch_id  # type: str
        # The name of the zone. You can call the [DescribeZones](~~443890~~) operation to query the zones.
        self.zone_id = zone_id  # type: str

    def validate(self):
        if self.load_balancer_addresses:
            for k in self.load_balancer_addresses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancersZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k in self.load_balancer_addresses:
                result['LoadBalancerAddresses'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('LoadBalancerAddresses') is not None:
            for k in m.get('LoadBalancerAddresses'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListLoadBalancersResponseBodyLoadBalancers(TeaModel):
    def __init__(self, address_ip_version=None, address_type=None, bandwidth_package_id=None, create_time=None,
                 cross_zone_enabled=None, dnsname=None, deletion_protection_config=None, ipv_6address_type=None,
                 load_balancer_billing_config=None, load_balancer_business_status=None, load_balancer_id=None, load_balancer_name=None,
                 load_balancer_status=None, load_balancer_type=None, modification_protection_config=None, operation_locks=None,
                 region_id=None, resource_group_id=None, security_group_ids=None, tags=None, vpc_id=None, zone_mappings=None):
        # The IP version. Valid values:
        # 
        # *   **ipv4**: IPv4
        # *   **DualStack**: dual stack
        self.address_ip_version = address_ip_version  # type: str
        # The type of IPv4 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.address_type = address_type  # type: str
        # The ID of the EIP bandwidth plan that is associated with the NLB instance if the NLB instance uses a public IP address.
        self.bandwidth_package_id = bandwidth_package_id  # type: str
        # The time when the resource was created. The time is displayed in UTC in the `yyyy-MM-ddTHH:mm:ssZ` format.
        self.create_time = create_time  # type: str
        # Indicates whether cross-zone load balancing is enabled for the NLB instance. Valid values:
        # 
        # *   **true**: enabled
        # *   **false**: disabled
        self.cross_zone_enabled = cross_zone_enabled  # type: bool
        # The domain name of the NLB instance.
        self.dnsname = dnsname  # type: str
        # The configuration of the deletion protection feature.
        self.deletion_protection_config = deletion_protection_config  # type: ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig
        # The type of IPv6 address used by the NLB instance. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. Therefore, the NLB instance can be accessed over the VPC where the NLB instance is deployed.
        self.ipv_6address_type = ipv_6address_type  # type: str
        # The billing settings of the NLB instance.
        self.load_balancer_billing_config = load_balancer_billing_config  # type: ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig
        # The business status of the NLB instance. Valid values:
        # 
        # *   **Abnormal**: The NLB instance is not working as expected.
        # *   **Normal**: The NLB instance is working as expected.
        self.load_balancer_business_status = load_balancer_business_status  # type: str
        # The ID of the NLB instance.
        self.load_balancer_id = load_balancer_id  # type: str
        # The name of the NLB instance.
        self.load_balancer_name = load_balancer_name  # type: str
        # The status of the NLB instance. Valid values:
        # 
        # *   **Inactive**: The NLB instance is disabled. Listeners of NLB instances in the Inactive state do not forward traffic.
        # *   **Active**: The NLB instance is running.
        # *   **Provisioning**: The NLB instance is being created.
        # *   **Configuring**: The NLB instance is being modified.
        # *   **Deleting**: The NLB instance is being deleted.
        # *   **Deleted**: The NLB instance is deleted.
        self.load_balancer_status = load_balancer_status  # type: str
        # The type of the SLB instance. Only **Network** is returned, which indicates NLB.
        self.load_balancer_type = load_balancer_type  # type: str
        # The configuration of the configuration read-only mode.
        self.modification_protection_config = modification_protection_config  # type: ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig
        # The configuration of the operation lock. This parameter takes effect if the value of `LoadBalancerBussinessStatus` is **Abnormal**.
        self.operation_locks = operation_locks  # type: list[ListLoadBalancersResponseBodyLoadBalancersOperationLocks]
        # The ID of the region where the NLB instance is deployed.
        self.region_id = region_id  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The security group to which the NLB instance is added.
        self.security_group_ids = security_group_ids  # type: list[str]
        # A list of tags.
        self.tags = tags  # type: list[ListLoadBalancersResponseBodyLoadBalancersTags]
        # The ID of the VPC where the NLB instance is deployed.
        self.vpc_id = vpc_id  # type: str
        # The mappings between zones and vSwitches.
        self.zone_mappings = zone_mappings  # type: list[ListLoadBalancersResponseBodyLoadBalancersZoneMappings]

    def validate(self):
        if self.deletion_protection_config:
            self.deletion_protection_config.validate()
        if self.load_balancer_billing_config:
            self.load_balancer_billing_config.validate()
        if self.modification_protection_config:
            self.modification_protection_config.validate()
        if self.operation_locks:
            for k in self.operation_locks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLoadBalancersResponseBodyLoadBalancers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ip_version is not None:
            result['AddressIpVersion'] = self.address_ip_version
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.bandwidth_package_id is not None:
            result['BandwidthPackageId'] = self.bandwidth_package_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled
        if self.dnsname is not None:
            result['DNSName'] = self.dnsname
        if self.deletion_protection_config is not None:
            result['DeletionProtectionConfig'] = self.deletion_protection_config.to_map()
        if self.ipv_6address_type is not None:
            result['Ipv6AddressType'] = self.ipv_6address_type
        if self.load_balancer_billing_config is not None:
            result['LoadBalancerBillingConfig'] = self.load_balancer_billing_config.to_map()
        if self.load_balancer_business_status is not None:
            result['LoadBalancerBusinessStatus'] = self.load_balancer_business_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status
        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type
        if self.modification_protection_config is not None:
            result['ModificationProtectionConfig'] = self.modification_protection_config.to_map()
        result['OperationLocks'] = []
        if self.operation_locks is not None:
            for k in self.operation_locks:
                result['OperationLocks'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressIpVersion') is not None:
            self.address_ip_version = m.get('AddressIpVersion')
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('BandwidthPackageId') is not None:
            self.bandwidth_package_id = m.get('BandwidthPackageId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')
        if m.get('DNSName') is not None:
            self.dnsname = m.get('DNSName')
        if m.get('DeletionProtectionConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersDeletionProtectionConfig()
            self.deletion_protection_config = temp_model.from_map(m['DeletionProtectionConfig'])
        if m.get('Ipv6AddressType') is not None:
            self.ipv_6address_type = m.get('Ipv6AddressType')
        if m.get('LoadBalancerBillingConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersLoadBalancerBillingConfig()
            self.load_balancer_billing_config = temp_model.from_map(m['LoadBalancerBillingConfig'])
        if m.get('LoadBalancerBusinessStatus') is not None:
            self.load_balancer_business_status = m.get('LoadBalancerBusinessStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')
        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')
        if m.get('ModificationProtectionConfig') is not None:
            temp_model = ListLoadBalancersResponseBodyLoadBalancersModificationProtectionConfig()
            self.modification_protection_config = temp_model.from_map(m['ModificationProtectionConfig'])
        self.operation_locks = []
        if m.get('OperationLocks') is not None:
            for k in m.get('OperationLocks'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersOperationLocks()
                self.operation_locks.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancersZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class ListLoadBalancersResponseBody(TeaModel):
    def __init__(self, load_balancers=None, max_results=None, next_token=None, request_id=None, total_count=None):
        # The NLB instances.
        self.load_balancers = load_balancers  # type: list[ListLoadBalancersResponseBodyLoadBalancers]
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that determines the start point of the next query. Valid values:
        # 
        # *   If this is your first query and no subsequent queries are to be sent, ignore this parameter.
        # *   If a subsequent query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.load_balancers:
            for k in self.load_balancers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListLoadBalancersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LoadBalancers'] = []
        if self.load_balancers is not None:
            for k in self.load_balancers:
                result['LoadBalancers'].append(k.to_map() if k else None)
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
        self.load_balancers = []
        if m.get('LoadBalancers') is not None:
            for k in m.get('LoadBalancers'):
                temp_model = ListLoadBalancersResponseBodyLoadBalancers()
                self.load_balancers.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListLoadBalancersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListLoadBalancersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListLoadBalancersResponse, self).to_map()
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
            temp_model = ListLoadBalancersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSecurityPolicyRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. You can specify up to 10 tag keys.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The tag value. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityPolicyRequestTag, self).to_map()
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


class ListSecurityPolicyRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_group_id=None,
                 security_policy_ids=None, security_policy_names=None, tag=None):
        # The number of entries to return per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The IDs of the TLS security policies. You can specify at most 20 policy IDs in each call.
        self.security_policy_ids = security_policy_ids  # type: list[str]
        # The names of the TLS security policies. You can specify at most 20 policy names.
        self.security_policy_names = security_policy_names  # type: list[str]
        # The tags.
        self.tag = tag  # type: list[ListSecurityPolicyRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecurityPolicyRequest, self).to_map()
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
        if self.security_policy_ids is not None:
            result['SecurityPolicyIds'] = self.security_policy_ids
        if self.security_policy_names is not None:
            result['SecurityPolicyNames'] = self.security_policy_names
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
        if m.get('SecurityPolicyIds') is not None:
            self.security_policy_ids = m.get('SecurityPolicyIds')
        if m.get('SecurityPolicyNames') is not None:
            self.security_policy_names = m.get('SecurityPolicyNames')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListSecurityPolicyRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners(TeaModel):
    def __init__(self, listener_id=None, listener_port=None, listener_protocol=None, load_balancer_id=None):
        # The listener ID.
        self.listener_id = listener_id  # type: str
        # The listener port.
        self.listener_port = listener_port  # type: long
        # The listener protocol. Valid value: **TCPSSL**.
        self.listener_protocol = listener_protocol  # type: str
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port
        if self.listener_protocol is not None:
            result['ListenerProtocol'] = self.listener_protocol
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')
        if m.get('ListenerProtocol') is not None:
            self.listener_protocol = m.get('ListenerProtocol')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class ListSecurityPolicyResponseBodySecurityPoliciesTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. You can specify up to 10 tag keys.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The tag value. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSecurityPolicyResponseBodySecurityPoliciesTags, self).to_map()
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


class ListSecurityPolicyResponseBodySecurityPolicies(TeaModel):
    def __init__(self, ciphers=None, region_id=None, related_listeners=None, resource_group_id=None,
                 security_policy_id=None, security_policy_name=None, security_policy_status=None, tags=None, tls_version=None):
        # The supported cipher suites, which are determined by the TLS protocol version. You can specify at most 32 cipher suites.
        # 
        # TLS 1.0 and TLS 1.1 support the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # 
        # TLS 1.2 supports the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # *   **ECDHE-ECDSA-AES128-GCM-SHA256**\
        # *   **ECDHE-ECDSA-AES256-GCM-SHA384**\
        # *   **ECDHE-ECDSA-AES128-SHA256**\
        # *   **ECDHE-ECDSA-AES256-SHA384**\
        # *   **ECDHE-RSA-AES128-GCM-SHA256**\
        # *   **ECDHE-RSA-AES256-GCM-SHA384**\
        # *   **ECDHE-RSA-AES128-SHA256**\
        # *   **ECDHE-RSA-AES256-SHA384**\
        # *   **AES128-GCM-SHA256**\
        # *   **AES256-GCM-SHA384**\
        # *   **AES128-SHA256**\
        # *   **AES256-SHA256**\
        # 
        # TLS 1.3 supports the following cipher suites:
        # 
        # *   **TLS_AES\_128\_GCM_SHA256**\
        # *   **TLS_AES\_256\_GCM_SHA384**\
        # *   **TLS_CHACHA20\_POLY1305\_SHA256**\
        # *   **TLS_AES\_128\_CCM_SHA256**\
        # *   **TLS_AES\_128\_CCM\_8\_SHA256**\
        self.ciphers = ciphers  # type: str
        # The region ID of the NLB instance.
        self.region_id = region_id  # type: str
        # The listeners that are associated with the NLB instance.
        self.related_listeners = related_listeners  # type: list[ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners]
        # The resource group ID.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id  # type: str
        # The name of the TLS security policy.
        self.security_policy_name = security_policy_name  # type: str
        # The status of the TLS security policy. Valid values:
        # 
        # *   **Configuring**\
        # *   **Available**\
        self.security_policy_status = security_policy_status  # type: str
        # The tags.
        self.tags = tags  # type: list[ListSecurityPolicyResponseBodySecurityPoliciesTags]
        # The supported versions of the TLS protocol. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**.
        self.tls_version = tls_version  # type: str

    def validate(self):
        if self.related_listeners:
            for k in self.related_listeners:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecurityPolicyResponseBodySecurityPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RelatedListeners'] = []
        if self.related_listeners is not None:
            for k in self.related_listeners:
                result['RelatedListeners'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.security_policy_status is not None:
            result['SecurityPolicyStatus'] = self.security_policy_status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.related_listeners = []
        if m.get('RelatedListeners') is not None:
            for k in m.get('RelatedListeners'):
                temp_model = ListSecurityPolicyResponseBodySecurityPoliciesRelatedListeners()
                self.related_listeners.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('SecurityPolicyStatus') is not None:
            self.security_policy_status = m.get('SecurityPolicyStatus')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListSecurityPolicyResponseBodySecurityPoliciesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')
        return self


class ListSecurityPolicyResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, security_policies=None, total_count=None):
        # The number of entries per page.
        self.max_results = max_results  # type: int
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If NextToken is empty, no next page exists.
        # *   If a value is returned for NextToken, specify the value in the next request to retrieve a new page of results.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # A list of TLS security policies.
        self.security_policies = security_policies  # type: list[ListSecurityPolicyResponseBodySecurityPolicies]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSecurityPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
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
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSecurityPolicyResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListSecurityPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSecurityPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSecurityPolicyResponse, self).to_map()
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
            temp_model = ListSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerGroupServersRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, server_group_id=None, server_ids=None,
                 server_ips=None):
        # The number of entries to return on each page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str
        # The IDs of the servers.
        self.server_ids = server_ids  # type: list[str]
        # The IP addresses of the servers.
        self.server_ips = server_ips  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerGroupServersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_ids is not None:
            result['ServerIds'] = self.server_ids
        if self.server_ips is not None:
            result['ServerIps'] = self.server_ips
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerIds') is not None:
            self.server_ids = m.get('ServerIds')
        if m.get('ServerIps') is not None:
            self.server_ips = m.get('ServerIps')
        return self


class ListServerGroupServersResponseBodyServers(TeaModel):
    def __init__(self, description=None, port=None, server_group_id=None, server_id=None, server_ip=None,
                 server_type=None, status=None, weight=None, zone_id=None):
        # The description of the backend server.
        self.description = description  # type: str
        # The port used by the backend server. Valid values: **1** to **65535**.
        self.port = port  # type: int
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str
        # The ID of the server.
        self.server_id = server_id  # type: str
        # The IP address of the backend server.
        self.server_ip = server_ip  # type: str
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Eni**: an elastic network interface (ENI)
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        self.server_type = server_type  # type: str
        # Indicates the status of the backend server. Valid values:
        # 
        # *   **Adding**: The backend server is being added.
        # *   **Available**: The backend server is added.
        # *   **Configuring**: The backend server is being configured.
        # *   **Removing**: The backend server is being removed.
        self.status = status  # type: str
        # The weight of the backend server.
        self.weight = weight  # type: int
        # The zone ID of the server.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerGroupServersResponseBodyServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.status is not None:
            result['Status'] = self.status
        if self.weight is not None:
            result['Weight'] = self.weight
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListServerGroupServersResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, servers=None, total_count=None):
        # The number of entries returned per page.
        self.max_results = max_results  # type: int
        # The token that is used for the next query. Valid values:
        # 
        # *   If this is your first query or no next query is to be sent, ignore this parameter.
        # *   If a next query is to be sent, set the parameter to the value of NextToken that is returned from the last call.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # A list of backend servers.
        self.servers = servers  # type: list[ListServerGroupServersResponseBodyServers]
        # The number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServerGroupServersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
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
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = ListServerGroupServersResponseBodyServers()
                self.servers.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServerGroupServersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServerGroupServersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServerGroupServersResponse, self).to_map()
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
            temp_model = ListServerGroupServersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListServerGroupsRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag. You can specify up to 10 tag keys.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The value of the tag. You can specify up to 10 tag values.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerGroupsRequestTag, self).to_map()
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


class ListServerGroupsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, region_id=None, resource_group_id=None,
                 server_group_ids=None, server_group_names=None, server_group_type=None, tag=None, vpc_id=None):
        # The number of entries per page. Valid values: **1** to **100**. Default value: **20**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The server group ID. You can specify up to 20 server group IDs in each call.
        self.server_group_ids = server_group_ids  # type: list[str]
        # The names of the server groups to be queried. You can specify up to 20 names in each call.
        self.server_group_names = server_group_names  # type: list[str]
        # The type of server group. Valid values:
        # 
        # *   **Instance** : allows you to add servers of the **Ecs**, **Ens**, and **Eci** types.
        # *   **Ip**: allows you to add servers by specifying IP addresses.
        self.server_group_type = server_group_type  # type: str
        # The tags.
        self.tag = tag  # type: list[ListServerGroupsRequestTag]
        # The ID of the virtual private cloud (VPC) to which the server group belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServerGroupsRequest, self).to_map()
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
        if self.server_group_ids is not None:
            result['ServerGroupIds'] = self.server_group_ids
        if self.server_group_names is not None:
            result['ServerGroupNames'] = self.server_group_names
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
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
        if m.get('ServerGroupIds') is not None:
            self.server_group_ids = m.get('ServerGroupIds')
        if m.get('ServerGroupNames') is not None:
            self.server_group_names = m.get('ServerGroupNames')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListServerGroupsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListServerGroupsResponseBodyServerGroupsHealthCheck(TeaModel):
    def __init__(self, health_check_connect_port=None, health_check_connect_timeout=None,
                 health_check_domain=None, health_check_enabled=None, health_check_http_code=None, health_check_interval=None,
                 health_check_type=None, health_check_url=None, healthy_threshold=None, http_check_method=None,
                 unhealthy_threshold=None):
        # The backend port that is used for health checks.
        # 
        # Valid values: **0** to **65535**.
        # 
        # A value of **0** indicates that the port on a backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port  # type: int
        # The maximum timeout period of a health check. Unit: seconds. Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout  # type: int
        # The domain name that you want to use for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the private IP address of a backend server.
        # *   **domain**: a specified domain name. The domain name must be 1 to 80 characters in length, and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain  # type: str
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.health_check_enabled = health_check_enabled  # type: bool
        # The HTTP status codes returned for health checks. Multiple HTTP status codes are separated by commas (,). Valid values: **http\_2xx**, **http\_3xx**, **http\_4xx**, and **http\_5xx**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code  # type: list[str]
        # The interval at which health checks are performed. Unit: seconds.
        # 
        # Valid values: **5** to **50**.
        self.health_check_interval = health_check_interval  # type: int
        # The protocol that is used for health checks. Valid values: **TCP** and **HTTP**.
        self.health_check_type = health_check_type  # type: str
        # The path to which health check probes are sent.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url  # type: str
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold  # type: int
        # The HTTP method that is used for health checks. Valid values: **GET** and **HEAD**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method  # type: str
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerGroupsResponseBodyServerGroupsHealthCheck, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.http_check_method is not None:
            result['HttpCheckMethod'] = self.http_check_method
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('HttpCheckMethod') is not None:
            self.http_check_method = m.get('HttpCheckMethod')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class ListServerGroupsResponseBodyServerGroupsTags(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. At most 10 tag keys are returned.
        # 
        # The tag key can be up to 64 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.key = key  # type: str
        # The tag value. At most 10 tag values are returned.
        # 
        # The tag value can be up to 128 characters in length, and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListServerGroupsResponseBodyServerGroupsTags, self).to_map()
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


class ListServerGroupsResponseBodyServerGroups(TeaModel):
    def __init__(self, address_ipversion=None, ali_uid=None, any_port_enabled=None, connection_drain_enabled=None,
                 connection_drain_timeout=None, health_check=None, preserve_client_ip_enabled=None, protocol=None, region_id=None,
                 related_load_balancer_ids=None, resource_group_id=None, scheduler=None, server_count=None, server_group_id=None,
                 server_group_name=None, server_group_status=None, server_group_type=None, tags=None, vpc_id=None):
        # The IP version. Valid values:
        # 
        # *   **ipv4**\
        # *   **DualStack**\
        self.address_ipversion = address_ipversion  # type: str
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid  # type: long
        # Indicates whether the feature of forwarding requests to all ports is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.any_port_enabled = any_port_enabled  # type: bool
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.connection_drain_enabled = connection_drain_enabled  # type: bool
        # The timeout period of connection draining. Unit: seconds. Valid values: **10** to **900**.
        self.connection_drain_timeout = connection_drain_timeout  # type: int
        # The configurations of health checks.
        self.health_check = health_check  # type: ListServerGroupsResponseBodyServerGroupsHealthCheck
        # Indicates whether client IP preservation is enabled. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # > This parameter is set to **true** by default when **AddressIPVersion** is set to **ipv4**. This parameter is set to **false** when **AddressIPVersion** is set to **ipv6**. **true** will be supported by later versions.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled  # type: bool
        # The protocol used to forward requests to the backend servers. Valid values: **TCP**, **UDP**, and **TCPSSL**.
        self.protocol = protocol  # type: str
        # The region ID of the NLB instance.
        self.region_id = region_id  # type: str
        # The NLB instances.
        self.related_load_balancer_ids = related_load_balancer_ids  # type: list[str]
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The routing algorithm. Valid values:
        # 
        # *   **Wrr**: Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are forwarded to the backend servers in sequence. sch: Requests are forwarded to the backend servers based on source IP address hashing.
        # *   **sch**: Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch**: Four-element hashing, which specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hashing. Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler  # type: str
        # The number of server groups associated with the NLB instances.
        self.server_count = server_count  # type: int
        # The server group ID.
        self.server_group_id = server_group_id  # type: str
        # The server group name.
        self.server_group_name = server_group_name  # type: str
        # The status of the server group. Valid values:
        # 
        # *   **Creating**\
        # *   **Available**\
        # *   **Configuring**\
        self.server_group_status = server_group_status  # type: str
        # The type of server group. Valid values:
        # 
        # *   **Instance** : contains servers of the **Ecs**, **Ens**, and **Eci** types.
        # *   **Ip**: contains servers specified by IP addresses.
        self.server_group_type = server_group_type  # type: str
        # The tag.
        self.tags = tags  # type: list[ListServerGroupsResponseBodyServerGroupsTags]
        # The ID of the VPC to which the server group belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.health_check:
            self.health_check.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServerGroupsResponseBodyServerGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.any_port_enabled is not None:
            result['AnyPortEnabled'] = self.any_port_enabled
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        if self.health_check is not None:
            result['HealthCheck'] = self.health_check.to_map()
        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.related_load_balancer_ids is not None:
            result['RelatedLoadBalancerIds'] = self.related_load_balancer_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_count is not None:
            result['ServerCount'] = self.server_count
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        if self.server_group_status is not None:
            result['ServerGroupStatus'] = self.server_group_status
        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('AnyPortEnabled') is not None:
            self.any_port_enabled = m.get('AnyPortEnabled')
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        if m.get('HealthCheck') is not None:
            temp_model = ListServerGroupsResponseBodyServerGroupsHealthCheck()
            self.health_check = temp_model.from_map(m['HealthCheck'])
        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelatedLoadBalancerIds') is not None:
            self.related_load_balancer_ids = m.get('RelatedLoadBalancerIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        if m.get('ServerGroupStatus') is not None:
            self.server_group_status = m.get('ServerGroupStatus')
        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListServerGroupsResponseBodyServerGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListServerGroupsResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, server_groups=None, total_count=None):
        # The number of entries per page. Valid values: **1** to **100**.
        self.max_results = max_results  # type: int
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # A list of server groups.
        self.server_groups = server_groups  # type: list[ListServerGroupsResponseBodyServerGroups]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.server_groups:
            for k in self.server_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListServerGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k in self.server_groups:
                result['ServerGroups'].append(k.to_map() if k else None)
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
        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k in m.get('ServerGroups'):
                temp_model = ListServerGroupsResponseBodyServerGroups()
                self.server_groups.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListServerGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListServerGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListServerGroupsResponse, self).to_map()
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
            temp_model = ListServerGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSystemSecurityPolicyRequest(TeaModel):
    def __init__(self, region_id=None):
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemSecurityPolicyRequest, self).to_map()
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


class ListSystemSecurityPolicyResponseBodySecurityPolicies(TeaModel):
    def __init__(self, ciphers=None, security_policy_id=None, security_policy_name=None, tls_version=None):
        # The cipher suites.
        self.ciphers = ciphers  # type: str
        # The TLS policy ID.
        self.security_policy_id = security_policy_id  # type: str
        # The TLS policy name.
        self.security_policy_name = security_policy_name  # type: str
        # The version of the TLS protocol.
        self.tls_version = tls_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSystemSecurityPolicyResponseBodySecurityPolicies, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.tls_version is not None:
            result['TlsVersion'] = self.tls_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('TlsVersion') is not None:
            self.tls_version = m.get('TlsVersion')
        return self


class ListSystemSecurityPolicyResponseBody(TeaModel):
    def __init__(self, request_id=None, security_policies=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # A list of TLS security policies.
        self.security_policies = security_policies  # type: list[ListSystemSecurityPolicyResponseBodySecurityPolicies]

    def validate(self):
        if self.security_policies:
            for k in self.security_policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSystemSecurityPolicyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecurityPolicies'] = []
        if self.security_policies is not None:
            for k in self.security_policies:
                result['SecurityPolicies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.security_policies = []
        if m.get('SecurityPolicies') is not None:
            for k in m.get('SecurityPolicies'):
                temp_model = ListSystemSecurityPolicyResponseBodySecurityPolicies()
                self.security_policies.append(temp_model.from_map(k))
        return self


class ListSystemSecurityPolicyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSystemSecurityPolicyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSystemSecurityPolicyResponse, self).to_map()
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
            temp_model = ListSystemSecurityPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. The tag key can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.key = key  # type: str
        # The tag value. The tag value can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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
        # The number of entries per page. Valid values: **1** to **50**. Default value: **50**.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   You do not need to specify this parameter for the first request.
        # *   You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token  # type: str
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The resource ID.
        self.resource_id = resource_id  # type: list[str]
        # The type of resource to query. Valid values:
        # 
        # *   **loadbalancer**: a Network Load Balancer (NLB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        # *   **listener**: a listener
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
    def __init__(self, ali_uid=None, category=None, region_no=None, resource_id=None, resource_type=None, scope=None,
                 tag_key=None, tag_value=None):
        # The UID of the Alibaba Cloud account.
        self.ali_uid = ali_uid  # type: long
        # The type of the tag. Valid values:
        # 
        # *   **Custom**\
        # *   **System**\
        # *   **All**\
        self.category = category  # type: str
        # The region information.
        self.region_no = region_no  # type: str
        # The resource ID.
        self.resource_id = resource_id  # type: str
        # The type of resource. Valid values:
        # 
        # *   **loadbalancer**: an NLB instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        self.resource_type = resource_type  # type: str
        # The visible range of the tags.
        self.scope = scope  # type: str
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
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        if self.category is not None:
            result['Category'] = self.category
        if self.region_no is not None:
            result['RegionNo'] = self.region_no
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, max_results=None, next_token=None, request_id=None, tag_resources=None, total_count=None):
        # The number of entries per page.
        self.max_results = max_results  # type: int
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is the token that determines the start point of the next query.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The details about the resource and its tags, including the resource ID, the resource type, and the keys and values of the tags.
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]
        # The total number of entries returned.
        self.total_count = total_count  # type: int

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
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
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


class LoadBalancerJoinSecurityGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None,
                 security_group_ids=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The ID of the NLB instance to be associated with the security group.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The security group ID of the instance.
        self.security_group_ids = security_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoadBalancerJoinSecurityGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class LoadBalancerJoinSecurityGroupResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoadBalancerJoinSecurityGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LoadBalancerJoinSecurityGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LoadBalancerJoinSecurityGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LoadBalancerJoinSecurityGroupResponse, self).to_map()
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
            temp_model = LoadBalancerJoinSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LoadBalancerLeaveSecurityGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None,
                 security_group_ids=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to obtain the region ID.
        self.region_id = region_id  # type: str
        # The ID of the security group to be disassociated.
        self.security_group_ids = security_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoadBalancerLeaveSecurityGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class LoadBalancerLeaveSecurityGroupResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LoadBalancerLeaveSecurityGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LoadBalancerLeaveSecurityGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LoadBalancerLeaveSecurityGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LoadBalancerLeaveSecurityGroupResponse, self).to_map()
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
            temp_model = LoadBalancerLeaveSecurityGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, new_resource_group_id=None, region_id=None, resource_id=None, resource_type=None):
        # The ID of the new resource group.
        # 
        # You can log on to the [Resource Management console](https://resourcemanager.console.aliyun.com/resource-groups) to view resource group IDs.
        self.new_resource_group_id = new_resource_group_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to obtain the region ID.
        self.region_id = region_id  # type: str
        # The ID of the bastion host for which you want to change the resource group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.resource_id = resource_id  # type: str
        # The type of the resource. Valid values:
        # 
        # *   **loadbalancer**: a Network Load Balancer (NLB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
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


class MoveResourceGroupResponseBodyData(TeaModel):
    def __init__(self, resource_id=None):
        # The ID of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, data=None, http_status_code=None, request_id=None, success=None):
        # The data returned.
        self.data = data  # type: MoveResourceGroupResponseBodyData
        # The HTTP status code returned.
        self.http_status_code = http_status_code  # type: int
        # The request ID.
        self.request_id = request_id  # type: str
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.success = success  # type: bool

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = MoveResourceGroupResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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


class RemoveServersFromServerGroupRequestServers(TeaModel):
    def __init__(self, port=None, server_id=None, server_ip=None, server_type=None):
        # The port that is used by the backend server. Valid values: **1** to **65535**.
        self.port = port  # type: int
        # The backend server ID.
        # 
        # *   If the server group type is **Instance**, set this parameter to the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. The backend servers are specified by **Ecs**, **Eni**, or **Eci**.
        # *   If the server group type is **Ip**, set this parameter to an IP address.
        self.server_id = server_id  # type: str
        # The IP address of the backend server. If the server group type is **Ip**, you must specify an IP address.
        self.server_ip = server_ip  # type: str
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: ECS instance
        # *   **Eni**: ENI
        # *   **Eci**: elastic container instance
        # *   **Ip**: IP address
        self.server_type = server_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveServersFromServerGroupRequestServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        return self


class RemoveServersFromServerGroupRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, server_group_id=None, servers=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str
        # The backend servers that you want to add to the server group. You can specify up to 40 servers in each call.
        self.servers = servers  # type: list[RemoveServersFromServerGroupRequestServers]

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveServersFromServerGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = RemoveServersFromServerGroupRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class RemoveServersFromServerGroupResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, server_group_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveServersFromServerGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class RemoveServersFromServerGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveServersFromServerGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveServersFromServerGroupResponse, self).to_map()
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
            temp_model = RemoveServersFromServerGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartListenerRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, listener_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The listener ID.
        self.listener_id = listener_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StartListenerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartListenerResponse, self).to_map()
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
            temp_model = StartListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartShiftLoadBalancerZonesRequestZoneMappings(TeaModel):
    def __init__(self, v_switch_id=None, zone_id=None):
        # The ID of the vSwitch in the zone. By default, each zone contains one vSwitch and one subnet.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID of the NLB instance.
        # 
        # > You can remove only one zone in each call.
        # 
        # You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartShiftLoadBalancerZonesRequestZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class StartShiftLoadBalancerZonesRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None, zone_mappings=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The mappings between zones and vSwitches.
        # 
        # > You can remove only one zone in each call.
        self.zone_mappings = zone_mappings  # type: list[StartShiftLoadBalancerZonesRequestZoneMappings]

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(StartShiftLoadBalancerZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = StartShiftLoadBalancerZonesRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class StartShiftLoadBalancerZonesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartShiftLoadBalancerZonesResponseBody, self).to_map()
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


class StartShiftLoadBalancerZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartShiftLoadBalancerZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartShiftLoadBalancerZonesResponse, self).to_map()
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
            temp_model = StartShiftLoadBalancerZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopListenerRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, listener_id=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The listener ID.
        self.listener_id = listener_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopListenerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class StopListenerResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StopListenerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopListenerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StopListenerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StopListenerResponse, self).to_map()
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
            temp_model = StopListenerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The tag key. The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
        self.key = key  # type: str
        # The tag value. The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # You can add up to 20 tags in each call.
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
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** is different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run  # type: bool
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource. Valid values:
        # 
        # *   **loadbalancer**: a Network Load Balancer (NLB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
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
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
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
    def __init__(self, all=None, client_token=None, dry_run=None, region_id=None, resource_id=None,
                 resource_type=None, tag_key=None):
        # Specifies whether to remove all tags from the specified resource. Valid values:
        # 
        # *   **true**: removes all tags from the specified resource.
        # *   **false**: does not remove all tags from the specified resource. This is the default value.
        self.all = all  # type: bool
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, the system automatically uses the value of **RequestId** as the value of **ClientToken**. The value of **RequestId** is different for each API request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: performs a dry run and sends the request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run  # type: bool
        # The region ID of the resource.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The ID of the resource. You can specify up to 50 resource IDs in each call.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource from which you want to remove tags. Valid values:
        # 
        # *   **loadbalancer**: a Network Load Balancer (NLB) instance
        # *   **securitypolicy**: a security policy
        # *   **servergroup**: a server group
        self.resource_type = resource_type  # type: str
        # The key of the tag that you want to remove. You can remove up to 20 tags in each call.
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
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
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
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
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
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
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


class UpdateListenerAttributeRequestProxyProtocolV2Config(TeaModel):
    def __init__(self, ppv_2private_link_ep_id_enabled=None, ppv_2private_link_eps_id_enabled=None,
                 ppv_2vpc_id_enabled=None):
        self.ppv_2private_link_ep_id_enabled = ppv_2private_link_ep_id_enabled  # type: bool
        self.ppv_2private_link_eps_id_enabled = ppv_2private_link_eps_id_enabled  # type: bool
        self.ppv_2vpc_id_enabled = ppv_2vpc_id_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerAttributeRequestProxyProtocolV2Config, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ppv_2private_link_ep_id_enabled is not None:
            result['Ppv2PrivateLinkEpIdEnabled'] = self.ppv_2private_link_ep_id_enabled
        if self.ppv_2private_link_eps_id_enabled is not None:
            result['Ppv2PrivateLinkEpsIdEnabled'] = self.ppv_2private_link_eps_id_enabled
        if self.ppv_2vpc_id_enabled is not None:
            result['Ppv2VpcIdEnabled'] = self.ppv_2vpc_id_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ppv2PrivateLinkEpIdEnabled') is not None:
            self.ppv_2private_link_ep_id_enabled = m.get('Ppv2PrivateLinkEpIdEnabled')
        if m.get('Ppv2PrivateLinkEpsIdEnabled') is not None:
            self.ppv_2private_link_eps_id_enabled = m.get('Ppv2PrivateLinkEpsIdEnabled')
        if m.get('Ppv2VpcIdEnabled') is not None:
            self.ppv_2vpc_id_enabled = m.get('Ppv2VpcIdEnabled')
        return self


class UpdateListenerAttributeRequest(TeaModel):
    def __init__(self, alpn_enabled=None, alpn_policy=None, ca_certificate_ids=None, ca_enabled=None,
                 certificate_ids=None, client_token=None, cps=None, dry_run=None, idle_timeout=None, listener_description=None,
                 listener_id=None, mss=None, proxy_protocol_enabled=None, proxy_protocol_v2config=None, region_id=None,
                 sec_sensor_enabled=None, security_policy_id=None, server_group_id=None):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.alpn_enabled = alpn_enabled  # type: bool
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**: uses only HTTP 1.x. The priority of HTTP 1.1 is higher than the priority of HTTP 1.0.
        # *   **HTTP2Only**: uses only HTTP 2.0.
        # *   **HTTP2Optional**: preferentially uses HTTP 1.x over HTTP 2.0. The priority of HTTP 1.1 is higher than the priority of HTTP 1.0, and the priority of HTTP 1.0 is higher than the priority of HTTP 2.0.
        # *   **HTTP2Preferred**: preferentially uses HTTP 2.0 over HTTP 1.x. The priority of HTTP 2.0 is higher than the priority of HTTP 1.1, and the priority of HTTP 1.1 is higher than the priority of HTTP 1.0.
        # 
        # > This parameter is required if AlpnEnabled is set to true.
        self.alpn_policy = alpn_policy  # type: str
        # The CA certificates. Only one CA certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids  # type: list[str]
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.ca_enabled = ca_enabled  # type: bool
        # The server certificates.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps  # type: int
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not update the configurations of the listener. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**.
        self.idle_timeout = idle_timeout  # type: int
        # Enter a name for the listener.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description  # type: str
        # The ID of the listener.
        self.listener_id = listener_id  # type: str
        # The size of the largest TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged. This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss  # type: int
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_enabled = proxy_protocol_enabled  # type: bool
        self.proxy_protocol_v2config = proxy_protocol_v2config  # type: UpdateListenerAttributeRequestProxyProtocolV2Config
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sec_sensor_enabled = sec_sensor_enabled  # type: bool
        # The ID of the security policy.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        if self.proxy_protocol_v2config:
            self.proxy_protocol_v2config.validate()

    def to_map(self):
        _map = super(UpdateListenerAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.proxy_protocol_v2config is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config.to_map()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('ProxyProtocolV2Config') is not None:
            temp_model = UpdateListenerAttributeRequestProxyProtocolV2Config()
            self.proxy_protocol_v2config = temp_model.from_map(m['ProxyProtocolV2Config'])
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateListenerAttributeShrinkRequest(TeaModel):
    def __init__(self, alpn_enabled=None, alpn_policy=None, ca_certificate_ids=None, ca_enabled=None,
                 certificate_ids=None, client_token=None, cps=None, dry_run=None, idle_timeout=None, listener_description=None,
                 listener_id=None, mss=None, proxy_protocol_enabled=None, proxy_protocol_v2config_shrink=None, region_id=None,
                 sec_sensor_enabled=None, security_policy_id=None, server_group_id=None):
        # Specifies whether to enable Application-Layer Protocol Negotiation (ALPN). Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.alpn_enabled = alpn_enabled  # type: bool
        # The ALPN policy. Valid values:
        # 
        # *   **HTTP1Only**: uses only HTTP 1.x. The priority of HTTP 1.1 is higher than the priority of HTTP 1.0.
        # *   **HTTP2Only**: uses only HTTP 2.0.
        # *   **HTTP2Optional**: preferentially uses HTTP 1.x over HTTP 2.0. The priority of HTTP 1.1 is higher than the priority of HTTP 1.0, and the priority of HTTP 1.0 is higher than the priority of HTTP 2.0.
        # *   **HTTP2Preferred**: preferentially uses HTTP 2.0 over HTTP 1.x. The priority of HTTP 2.0 is higher than the priority of HTTP 1.1, and the priority of HTTP 1.1 is higher than the priority of HTTP 1.0.
        # 
        # > This parameter is required if AlpnEnabled is set to true.
        self.alpn_policy = alpn_policy  # type: str
        # The CA certificates. Only one CA certificate is supported.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.ca_certificate_ids = ca_certificate_ids  # type: list[str]
        # Specifies whether to enable mutual authentication. Valid values:
        # 
        # *   **true**: yes
        # *   **false** (default): no
        self.ca_enabled = ca_enabled  # type: bool
        # The server certificates.
        self.certificate_ids = certificate_ids  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **0** to **1000000**. **0** specifies that the number of connections is unlimited.
        self.cps = cps  # type: int
        # Specifies whether only to precheck the request. Valid values:
        # 
        # *   **true**: prechecks the request but does not update the configurations of the listener. The system prechecks the required parameters, request syntax, and limits. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # *   **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The timeout period of an idle connection. Unit: seconds. Valid values: **1** to **900**.
        self.idle_timeout = idle_timeout  # type: int
        # Enter a name for the listener.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.listener_description = listener_description  # type: str
        # The ID of the listener.
        self.listener_id = listener_id  # type: str
        # The size of the largest TCP segment. Unit: bytes. Valid values: **0** to **1500**. **0** specifies that the maximum segment size remains unchanged. This parameter is supported only by listeners that use SSL over TCP.
        self.mss = mss  # type: int
        # Specifies whether to use the Proxy protocol to pass client IP addresses to backend servers. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.proxy_protocol_enabled = proxy_protocol_enabled  # type: bool
        self.proxy_protocol_v2config_shrink = proxy_protocol_v2config_shrink  # type: str
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # Specifies whether to enable fine-grained monitoring. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sec_sensor_enabled = sec_sensor_enabled  # type: bool
        # The ID of the security policy.
        # 
        # >  This parameter takes effect only for listeners that use SSL over TCP.
        self.security_policy_id = security_policy_id  # type: str
        # The ID of the server group.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerAttributeShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alpn_enabled is not None:
            result['AlpnEnabled'] = self.alpn_enabled
        if self.alpn_policy is not None:
            result['AlpnPolicy'] = self.alpn_policy
        if self.ca_certificate_ids is not None:
            result['CaCertificateIds'] = self.ca_certificate_ids
        if self.ca_enabled is not None:
            result['CaEnabled'] = self.ca_enabled
        if self.certificate_ids is not None:
            result['CertificateIds'] = self.certificate_ids
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout
        if self.listener_description is not None:
            result['ListenerDescription'] = self.listener_description
        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id
        if self.mss is not None:
            result['Mss'] = self.mss
        if self.proxy_protocol_enabled is not None:
            result['ProxyProtocolEnabled'] = self.proxy_protocol_enabled
        if self.proxy_protocol_v2config_shrink is not None:
            result['ProxyProtocolV2Config'] = self.proxy_protocol_v2config_shrink
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.sec_sensor_enabled is not None:
            result['SecSensorEnabled'] = self.sec_sensor_enabled
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AlpnEnabled') is not None:
            self.alpn_enabled = m.get('AlpnEnabled')
        if m.get('AlpnPolicy') is not None:
            self.alpn_policy = m.get('AlpnPolicy')
        if m.get('CaCertificateIds') is not None:
            self.ca_certificate_ids = m.get('CaCertificateIds')
        if m.get('CaEnabled') is not None:
            self.ca_enabled = m.get('CaEnabled')
        if m.get('CertificateIds') is not None:
            self.certificate_ids = m.get('CertificateIds')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')
        if m.get('ListenerDescription') is not None:
            self.listener_description = m.get('ListenerDescription')
        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')
        if m.get('Mss') is not None:
            self.mss = m.get('Mss')
        if m.get('ProxyProtocolEnabled') is not None:
            self.proxy_protocol_enabled = m.get('ProxyProtocolEnabled')
        if m.get('ProxyProtocolV2Config') is not None:
            self.proxy_protocol_v2config_shrink = m.get('ProxyProtocolV2Config')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecSensorEnabled') is not None:
            self.sec_sensor_enabled = m.get('SecSensorEnabled')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateListenerAttributeResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateListenerAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateListenerAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateListenerAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateListenerAttributeResponse, self).to_map()
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
            temp_model = UpdateListenerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerAddressTypeConfigRequestZoneMappings(TeaModel):
    def __init__(self, allocation_id=None, eip_type=None, v_switch_id=None, zone_id=None):
        # The ID of the elastic IP address (EIP).
        self.allocation_id = allocation_id  # type: str
        # The type of the EIP. Valid values:
        # 
        # *   **Common**\
        # *   **Anycast**\
        # 
        # > Anycast EIPs are supported only by NLB instances in the China (Hong Kong) region. This parameter is required when **AddressType** is set to **Internet**.
        self.eip_type = eip_type  # type: str
        # The ID of the vSwitch in the zone. Each zone can contain only one vSwitch and one subnet.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID of the NLB instance.
        # 
        # You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerAddressTypeConfigRequestZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eip_type is not None:
            result['EipType'] = self.eip_type
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateLoadBalancerAddressTypeConfigRequest(TeaModel):
    def __init__(self, address_type=None, client_token=None, dry_run=None, load_balancer_id=None, region_id=None,
                 zone_mappings=None):
        # The new network type. Valid values:
        # 
        # *   **Internet**: The NLB instance uses a public IP address. The domain name of the NLB instance is resolved to the public IP address. Therefore, the NLB instance can be accessed over the Internet.
        # *   **Intranet**: The NLB instance uses a private IP address. The domain name of the NLB instance is resolved to the private IP address. In this case, the NLB instance can be accessed over the virtual private cloud (VPC) where the NLB instance is deployed.
        self.address_type = address_type  # type: str
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The mappings between zones and vSwitches. You can specify at most 10 zones in each call.
        self.zone_mappings = zone_mappings  # type: list[UpdateLoadBalancerAddressTypeConfigRequestZoneMappings]

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateLoadBalancerAddressTypeConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_type is not None:
            result['AddressType'] = self.address_type
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = UpdateLoadBalancerAddressTypeConfigRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class UpdateLoadBalancerAddressTypeConfigResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerAddressTypeConfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerAddressTypeConfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLoadBalancerAddressTypeConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLoadBalancerAddressTypeConfigResponse, self).to_map()
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
            temp_model = UpdateLoadBalancerAddressTypeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerAttributeRequest(TeaModel):
    def __init__(self, client_token=None, cps=None, cross_zone_enabled=None, dry_run=None, load_balancer_id=None,
                 load_balancer_name=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # The maximum number of connections that can be created per second on the NLB instance. Valid values: **1** to **1000000**.
        self.cps = cps  # type: int
        # Specifies whether to enable cross-zone load balancing for the NLB instance. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.cross_zone_enabled = cross_zone_enabled  # type: bool
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The NLB instance name.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.load_balancer_name = load_balancer_name  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.cps is not None:
            result['Cps'] = self.cps
        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('Cps') is not None:
            self.cps = m.get('Cps')
        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateLoadBalancerAttributeResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLoadBalancerAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLoadBalancerAttributeResponse, self).to_map()
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
            temp_model = UpdateLoadBalancerAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerProtectionRequest(TeaModel):
    def __init__(self, client_token=None, deletion_protection_enabled=None, deletion_protection_reason=None,
                 dry_run=None, load_balancer_id=None, modification_protection_reason=None,
                 modification_protection_status=None, region_id=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.deletion_protection_enabled = deletion_protection_enabled  # type: bool
        # The reason why deletion protection is enabled. The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The reason must start with a letter.
        # 
        # > This parameter takes effect only when **DeletionProtectionEnabled** is set to **true**.
        self.deletion_protection_reason = deletion_protection_reason  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The reason why the configuration read-only mode is enabled. The reason must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The reason must start with a letter.
        # 
        # > This parameter takes effect only if **Status** is set to **ConsoleProtection**.
        self.modification_protection_reason = modification_protection_reason  # type: str
        # Specifies whether to enable the configuration read-only mode. Valid values:
        # 
        # *   **NonProtection**: disables the configuration read-only mode. In this case, you cannot set the **ModificationProtectionReason** parameter. If you specify **ModificationProtectionReason**, the value is cleared.
        # *   **ConsoleProtection**: enables the configuration read-only mode. In this case, you can specify **ModificationProtectionReason**.
        # 
        # > If you set this parameter to **ConsoleProtection**, you cannot use the NLB console to modify instance configurations. However, you can call API operations to modify instance configurations.
        self.modification_protection_status = modification_protection_status  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerProtectionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.deletion_protection_enabled is not None:
            result['DeletionProtectionEnabled'] = self.deletion_protection_enabled
        if self.deletion_protection_reason is not None:
            result['DeletionProtectionReason'] = self.deletion_protection_reason
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason
        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DeletionProtectionEnabled') is not None:
            self.deletion_protection_enabled = m.get('DeletionProtectionEnabled')
        if m.get('DeletionProtectionReason') is not None:
            self.deletion_protection_reason = m.get('DeletionProtectionReason')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')
        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpdateLoadBalancerProtectionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerProtectionResponseBody, self).to_map()
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


class UpdateLoadBalancerProtectionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLoadBalancerProtectionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLoadBalancerProtectionResponse, self).to_map()
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
            temp_model = UpdateLoadBalancerProtectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLoadBalancerZonesRequestZoneMappings(TeaModel):
    def __init__(self, allocation_id=None, eip_type=None, private_ipv_4address=None, v_switch_id=None, zone_id=None):
        # The ID of the elastic IP address (EIP) or Anycast EIP.
        self.allocation_id = allocation_id  # type: str
        # The type of the EIP. Valid values:
        # 
        # *   **Common**\
        # *   **Anycast**\
        # 
        # > Anycast EIPs are supported only by NLB instances in the China (Hong Kong) region. This parameter is required when **AddressType** is set to **Internet**.
        self.eip_type = eip_type  # type: str
        # The private IP addresses.
        self.private_ipv_4address = private_ipv_4address  # type: str
        # The ID of the vSwitch in the zone. By default, each zone uses one vSwitch and one subnet.
        self.v_switch_id = v_switch_id  # type: str
        # The zone ID. You can call the [DescribeZones](~~443890~~) operation to query the most recent zone list.
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerZonesRequestZoneMappings, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allocation_id is not None:
            result['AllocationId'] = self.allocation_id
        if self.eip_type is not None:
            result['EipType'] = self.eip_type
        if self.private_ipv_4address is not None:
            result['PrivateIPv4Address'] = self.private_ipv_4address
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllocationId') is not None:
            self.allocation_id = m.get('AllocationId')
        if m.get('EipType') is not None:
            self.eip_type = m.get('EipType')
        if m.get('PrivateIPv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIPv4Address')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateLoadBalancerZonesRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, load_balancer_id=None, region_id=None, zone_mappings=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**: sends the request. If the request passes the check, an HTTP 2xx status code is returned and the operation is performed. This is the default value.
        self.dry_run = dry_run  # type: bool
        # The NLB instance ID.
        self.load_balancer_id = load_balancer_id  # type: str
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to obtain the region ID.
        self.region_id = region_id  # type: str
        # The mappings between zones and vSwitches. You can specify at most 10 zones.
        self.zone_mappings = zone_mappings  # type: list[UpdateLoadBalancerZonesRequestZoneMappings]

    def validate(self):
        if self.zone_mappings:
            for k in self.zone_mappings:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateLoadBalancerZonesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k in self.zone_mappings:
                result['ZoneMappings'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k in m.get('ZoneMappings'):
                temp_model = UpdateLoadBalancerZonesRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k))
        return self


class UpdateLoadBalancerZonesResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateLoadBalancerZonesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLoadBalancerZonesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateLoadBalancerZonesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateLoadBalancerZonesResponse, self).to_map()
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
            temp_model = UpdateLoadBalancerZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSecurityPolicyAttributeRequest(TeaModel):
    def __init__(self, ciphers=None, client_token=None, dry_run=None, region_id=None, security_policy_id=None,
                 security_policy_name=None, tls_versions=None):
        # The supported cipher suites, which are determined by the TLS protocol version. You can specify at most 32 cipher suites.
        # 
        # TLS 1.0 and TLS 1.1 support the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # 
        # TLS 1.2 supports the following cipher suites:
        # 
        # *   **ECDHE-ECDSA-AES128-SHA**\
        # *   **ECDHE-ECDSA-AES256-SHA**\
        # *   **ECDHE-RSA-AES128-SHA**\
        # *   **ECDHE-RSA-AES256-SHA**\
        # *   **AES128-SHA**\
        # *   **AES256-SHA**\
        # *   **DES-CBC3-SHA**\
        # *   **ECDHE-ECDSA-AES128-GCM-SHA256**\
        # *   **ECDHE-ECDSA-AES256-GCM-SHA384**\
        # *   **ECDHE-ECDSA-AES128-SHA256**\
        # *   **ECDHE-ECDSA-AES256-SHA384**\
        # *   **ECDHE-RSA-AES128-GCM-SHA256**\
        # *   **ECDHE-RSA-AES256-GCM-SHA384**\
        # *   **ECDHE-RSA-AES128-SHA256**\
        # *   **ECDHE-RSA-AES256-SHA384**\
        # *   **AES128-GCM-SHA256**\
        # *   **AES256-GCM-SHA384**\
        # *   **AES128-SHA256**\
        # *   **AES256-SHA256**\
        # 
        # TLS 1.3 supports the following cipher suites:
        # 
        # *   **TLS_AES\_128\_GCM_SHA256**\
        # *   **TLS_AES\_256\_GCM_SHA384**\
        # *   **TLS_CHACHA20\_POLY1305\_SHA256**\
        # *   **TLS_AES\_128\_CCM_SHA256**\
        # *   **TLS_AES\_128\_CCM\_8\_SHA256**\
        self.ciphers = ciphers  # type: list[str]
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to obtain the region ID.
        self.region_id = region_id  # type: str
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id  # type: str
        # The name of the security policy.
        # 
        # The name must be 1 to 200 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.security_policy_name = security_policy_name  # type: str
        # The supported versions of the Transport Layer Security (TLS) protocol. Valid values: **TLSv1.0**, **TLSv1.1**, **TLSv1.2**, and **TLSv1.3**. You can specify at most four TLS protocol versions.
        self.tls_versions = tls_versions  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecurityPolicyAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ciphers is not None:
            result['Ciphers'] = self.ciphers
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        if self.security_policy_name is not None:
            result['SecurityPolicyName'] = self.security_policy_name
        if self.tls_versions is not None:
            result['TlsVersions'] = self.tls_versions
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Ciphers') is not None:
            self.ciphers = m.get('Ciphers')
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        if m.get('SecurityPolicyName') is not None:
            self.security_policy_name = m.get('SecurityPolicyName')
        if m.get('TlsVersions') is not None:
            self.tls_versions = m.get('TlsVersions')
        return self


class UpdateSecurityPolicyAttributeResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, security_policy_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The ID of the TLS security policy.
        self.security_policy_id = security_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateSecurityPolicyAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.security_policy_id is not None:
            result['SecurityPolicyId'] = self.security_policy_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SecurityPolicyId') is not None:
            self.security_policy_id = m.get('SecurityPolicyId')
        return self


class UpdateSecurityPolicyAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateSecurityPolicyAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateSecurityPolicyAttributeResponse, self).to_map()
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
            temp_model = UpdateSecurityPolicyAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerGroupAttributeRequestHealthCheckConfig(TeaModel):
    def __init__(self, health_check_connect_port=None, health_check_connect_timeout=None,
                 health_check_domain=None, health_check_enabled=None, health_check_http_code=None, health_check_interval=None,
                 health_check_type=None, health_check_url=None, healthy_threshold=None, http_check_method=None,
                 unhealthy_threshold=None):
        # The port that you want to use for health checks on backend servers. Valid values: **0** to **65535**. If you set the value to **0**, the ports of backend servers are used for health checks.
        self.health_check_connect_port = health_check_connect_port  # type: int
        # The maximum timeout period of a health check. Unit: seconds. Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout  # type: int
        # The domain name that you want to use for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the private IP address of a backend server.
        # *   **domain**: a specified domain name. The domain name must be 1 to 80 characters in length, and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain  # type: str
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.health_check_enabled = health_check_enabled  # type: bool
        # The HTTP status codes to return for health checks. Separate multiple HTTP status codes with commas (,). Valid values: **http\_2xx** (default), **http\_3xx**, **http\_4xx**, and **http\_5xx**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code  # type: list[str]
        # The interval at which health checks are performed. Unit: seconds.
        # 
        # Valid values: **5** to **50**.
        self.health_check_interval = health_check_interval  # type: int
        # The protocol that you want to use for health checks. Valid values: **TCP** and **HTTP**.
        self.health_check_type = health_check_type  # type: str
        # The path to which health check requests are sent.
        # 
        # The path must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: `- / . % ? # & =`. It can also contain the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \" , +`. The path must start with a forward slash (/).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url  # type: str
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold  # type: int
        # The HTTP method that is used for health checks. Valid values: **GET** and **HEAD**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method  # type: str
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**. Valid values: **2** to **10**.
        self.unhealthy_threshold = unhealthy_threshold  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServerGroupAttributeRequestHealthCheckConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port
        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout
        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain
        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled
        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code
        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval
        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type
        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url
        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold
        if self.http_check_method is not None:
            result['HttpCheckMethod'] = self.http_check_method
        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')
        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')
        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')
        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')
        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')
        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')
        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')
        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')
        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')
        if m.get('HttpCheckMethod') is not None:
            self.http_check_method = m.get('HttpCheckMethod')
        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')
        return self


class UpdateServerGroupAttributeRequest(TeaModel):
    def __init__(self, client_token=None, connection_drain_enabled=None, connection_drain_timeout=None,
                 dry_run=None, health_check_config=None, preserve_client_ip_enabled=None, region_id=None, scheduler=None,
                 server_group_id=None, server_group_name=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.connection_drain_enabled = connection_drain_enabled  # type: bool
        # The timeout period of connection draining. Unit: seconds. Valid values: **10** to **900**.
        self.connection_drain_timeout = connection_drain_timeout  # type: int
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The configurations of the health check feature.
        self.health_check_config = health_check_config  # type: UpdateServerGroupAttributeRequestHealthCheckConfig
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.preserve_client_ip_enabled = preserve_client_ip_enabled  # type: bool
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to obtain the region ID.
        self.region_id = region_id  # type: str
        # The routing algorithm. Valid values:
        # 
        # *   **Wrr**: Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **rr**: Requests are forwarded to backend servers in sequence.
        # *   **sch:** Source IP hashing is used. Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch:** Four-element hashing is used. It specifies consistent hashing that is based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same information based on the four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hashing. Requests that contain the same QUIC ID are forwarded to the same backend server.
        self.scheduler = scheduler  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str
        # The new name of the server group.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (\_), and hyphens (-). The name must start with a letter.
        self.server_group_name = server_group_name  # type: str

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        _map = super(UpdateServerGroupAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()
        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('HealthCheckConfig') is not None:
            temp_model = UpdateServerGroupAttributeRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m['HealthCheckConfig'])
        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')
        return self


class UpdateServerGroupAttributeResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, server_group_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServerGroupAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateServerGroupAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServerGroupAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServerGroupAttributeResponse, self).to_map()
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
            temp_model = UpdateServerGroupAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServerGroupServersAttributeRequestServers(TeaModel):
    def __init__(self, description=None, port=None, server_id=None, server_ip=None, server_type=None, weight=None):
        # The description of the backend server.
        # 
        # The description must be 2 to 256 characters in length, and can contain letters, digits, commas (,), periods (.), semicolons (;), forward slashes (/), at signs (@), underscores (\_), and hyphens (-).
        self.description = description  # type: str
        # The port that is used by the backend server. Valid values: **1** to **65535**. You can specify at most 40 backend servers in each call.
        # 
        # > This is parameter cannot be modified.
        self.port = port  # type: int
        # The backend server ID. You can specify at most 40 backend servers in each call.
        # 
        # *   If the server group type is **Instance**, set the ServerId parameter to the ID of an Elastic Compute Service (ECS) instance, an elastic network interface (ENI), or an elastic container instance. These backend servers are specified by **Ecs**, **Eni**, or **Eci**.
        # *   If the server group type is **Ip**, set this parameter to an IP address.
        self.server_id = server_id  # type: str
        # The IP address of the backend server. If the server group type is **Ip**, you must specify an IP address.
        # 
        # > You can specify at most 40 backend servers in each call.
        self.server_ip = server_ip  # type: str
        # The type of the backend server. Valid values:
        # 
        # *   **Ecs**: ECS instance
        # *   **Eni**: ENI
        # *   **Eci**: an elastic container instance
        # *   **Ip**: an IP address
        # 
        # > You can specify at most 40 backend servers in each call.
        self.server_type = server_type  # type: str
        # The weight of the backend server. Valid values: **0** to **100**. Default value: **100**. If the weight of a backend server is set to **0**, no requests are forwarded to the backend server.
        # 
        # > You can specify at most 40 backend servers in each call.
        self.weight = weight  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServerGroupServersAttributeRequestServers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.port is not None:
            result['Port'] = self.port
        if self.server_id is not None:
            result['ServerId'] = self.server_id
        if self.server_ip is not None:
            result['ServerIp'] = self.server_ip
        if self.server_type is not None:
            result['ServerType'] = self.server_type
        if self.weight is not None:
            result['Weight'] = self.weight
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')
        if m.get('ServerIp') is not None:
            self.server_ip = m.get('ServerIp')
        if m.get('ServerType') is not None:
            self.server_type = m.get('ServerType')
        if m.get('Weight') is not None:
            self.weight = m.get('Weight')
        return self


class UpdateServerGroupServersAttributeRequest(TeaModel):
    def __init__(self, client_token=None, dry_run=None, region_id=None, server_group_id=None, servers=None):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token  # type: str
        # Specifies whether to perform a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false**(default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run  # type: bool
        # The region ID of the NLB instance.
        # 
        # You can call the [DescribeRegions](~~443657~~) operation to query the most recent region list.
        self.region_id = region_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str
        # The backend servers that you want to modify. You can specify up to 40 servers in each call.
        self.servers = servers  # type: list[UpdateServerGroupServersAttributeRequestServers]

    def validate(self):
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateServerGroupServersAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = UpdateServerGroupServersAttributeRequestServers()
                self.servers.append(temp_model.from_map(k))
        return self


class UpdateServerGroupServersAttributeResponseBody(TeaModel):
    def __init__(self, job_id=None, request_id=None, server_group_id=None):
        # The ID of the asynchronous task.
        self.job_id = job_id  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The server group ID.
        self.server_group_id = server_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateServerGroupServersAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')
        return self


class UpdateServerGroupServersAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateServerGroupServersAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateServerGroupServersAttributeResponse, self).to_map()
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
            temp_model = UpdateServerGroupServersAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


