# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachClusterToHubRequest(TeaModel):
    def __init__(self, attach_to_mesh=None, cluster_id=None, cluster_ids=None):
        # Specifies whether to associate the clusters with Service Mesh (ASM) instances. Valid values:
        self.attach_to_mesh = attach_to_mesh  # type: bool
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # A JSON string that can be parsed into a string array. The string specifies the clusters that you want to associate with the master instance.
        self.cluster_ids = cluster_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachClusterToHubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attach_to_mesh is not None:
            result['AttachToMesh'] = self.attach_to_mesh
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AttachToMesh') is not None:
            self.attach_to_mesh = m.get('AttachToMesh')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        return self


class AttachClusterToHubResponseBody(TeaModel):
    def __init__(self, cluster_id=None, managed_cluster_ids=None, request_id=None, task_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # A list of the IDs of the clusters that you want to associate with the master instance.
        self.managed_cluster_ids = managed_cluster_ids  # type: list[str]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachClusterToHubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.managed_cluster_ids is not None:
            result['ManagedClusterIds'] = self.managed_cluster_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ManagedClusterIds') is not None:
            self.managed_cluster_ids = m.get('ManagedClusterIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AttachClusterToHubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachClusterToHubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachClusterToHubResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachClusterToHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHubClusterRequest(TeaModel):
    def __init__(self, api_server_public_eip=None, audit_log_enabled=None, is_enterprise_security_group=None,
                 name=None, profile=None, region_id=None, v_switches=None, vpc_id=None):
        # Specifies whether to use a public IP address to expose the API server. Valid values: - true: uses a public IP address to expose the API server. - true: uses an internal IP address to expose the API server.
        self.api_server_public_eip = api_server_public_eip  # type: bool
        # Specifies whether to enable audit logs. Valid values: - true: enables audit logs. - false: disables audit logs.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # Specifies whether the security group is an advanced security group.
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # The name of the master instance.
        self.name = name  # type: str
        # Scenario-oriented master control type. The value can be:
        # 
        # - `Default`: Standard scenario Master instance.
        # - `XFlow`: Workflow scenario master instance.
        # 
        # Default Value: `Default`.
        self.profile = profile  # type: str
        # The ID of the region. You can call the DescribeRegions operation to query available regions.
        self.region_id = region_id  # type: str
        # The ID of the vSwitch.
        self.v_switches = v_switches  # type: str
        # The ID of the virtual private cloud (VPC) to which the master instance belongs. You can call the DescribeVpcs operation to query available VPCs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHubClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.is_enterprise_security_group is not None:
            result['IsEnterpriseSecurityGroup'] = self.is_enterprise_security_group
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('IsEnterpriseSecurityGroup') is not None:
            self.is_enterprise_security_group = m.get('IsEnterpriseSecurityGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateHubClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHubClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateHubClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHubClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHubClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateHubClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHubClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, force=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to forcefully delete the master instance. Valid values: - true: forcefully delete the master instance. - false: does not forcefully delete the master instance. Default value: false.
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHubClusterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteHubClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the master instance.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHubClusterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteHubClusterResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHubClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHubClusterResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteHubClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterDetailsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterApiServer(TeaModel):
    def __init__(self, api_server_eip_id=None, enabled_public=None, load_balancer_id=None):
        # The ID of the elastic IP address (EIP).
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Indicates whether a public endpoint is used to expose the API server. Valid values: - true: a public endpoint is used to expose the API server. - false: no public endpoint is used to expose the API server.
        self.enabled_public = enabled_public  # type: bool
        # The ID of the Server Load Balancer (SLB) instance.
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterApiServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.enabled_public is not None:
            result['EnabledPublic'] = self.enabled_public
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('EnabledPublic') is not None:
            self.enabled_public = m.get('EnabledPublic')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, creation_time=None, error_message=None, name=None,
                 profile=None, region_id=None, state=None, update_time=None, version=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The specification of the master instance. Valid values: - ack.pro.small: ACK Pro
        self.cluster_spec = cluster_spec  # type: str
        # The time when the master instance was created.
        self.creation_time = creation_time  # type: str
        # The error message that is returned when the system fails to create the master instance.
        self.error_message = error_message  # type: str
        # The name of the master instance.
        self.name = name  # type: str
        # The configurations of the master instance.
        self.profile = profile  # type: str
        # The ID of the region in which the master instance resides.
        self.region_id = region_id  # type: str
        # The status of the master instance. Valid values: - initial: The master instance is being initialized. - failed: The master instance failed to be created. - running: The master instance is running. - inactive: The master instance is inactive. - deleting: The master instance is being deleted. - delete_failed: The master instance failed to be deleted. - deleted: The master instance is deleted.
        self.state = state  # type: str
        # The time when the master instance was updated.
        self.update_time = update_time  # type: str
        # The Kubernetes version of the master instance.
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeHubClusterDetailsResponseBodyClusterConditions(TeaModel):
    def __init__(self, message=None, reason=None, status=None, type=None):
        # 删除条件错误信息
        self.message = message  # type: str
        # 删除条件原因
        self.reason = reason  # type: str
        # 删除条件状态，取值
        # - True 不能删除
        # - False 允许删除
        # - Unknow 未知
        self.status = status  # type: str
        # 删除条件类型
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeHubClusterDetailsResponseBodyClusterEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        # The internal endpoint of the API server of the master instance.
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        # The public endpoint of the API server of the master instance.
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeHubClusterDetailsResponseBodyClusterLogConfig(TeaModel):
    def __init__(self, enable_log=None, log_project=None, log_store_ttl=None):
        # Indicates whether audit logs are enabled. Valid values: - true: audit logs are enabled. - false: audit logs are disabled.
        self.enable_log = enable_log  # type: bool
        # The name of the Log Service project.
        self.log_project = log_project  # type: str
        # The retention period of the logs.
        self.log_store_ttl = log_store_ttl  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store_ttl is not None:
            result['LogStoreTTL'] = self.log_store_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStoreTTL') is not None:
            self.log_store_ttl = m.get('LogStoreTTL')
        return self


class DescribeHubClusterDetailsResponseBodyClusterMeshConfig(TeaModel):
    def __init__(self, enable_mesh=None, mesh_id=None):
        # Indicates whether ASM is enabled. Valid values: - true: ASM is enabled. - false: ASM is disabled.
        self.enable_mesh = enable_mesh  # type: bool
        # The ID of the ASM instance.
        self.mesh_id = mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterMeshConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.mesh_id is not None:
            result['MeshId'] = self.mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('MeshId') is not None:
            self.mesh_id = m.get('MeshId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterNetwork(TeaModel):
    def __init__(self, cluster_domain=None, ipstack=None, security_group_ids=None, v_switches=None, vpc_id=None):
        # The domain name of the master instance.
        self.cluster_domain = cluster_domain  # type: str
        # The IP version that is supported by the master instance. Valid values: - ipv4: IPv4. - ipv6: IPv6. - dual: IPv4 and IPv6.
        self.ipstack = ipstack  # type: str
        # The ID of the associated security group.
        self.security_group_ids = security_group_ids  # type: list[str]
        # A list of the vSwitches that are used by the master instance.
        self.v_switches = v_switches  # type: list[str]
        # The ID of the virtual private cloud (VPC) in which the master instance resides.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.ipstack is not None:
            result['IPStack'] = self.ipstack
        if self.security_group_ids is not None:
            result['SecurityGroupIDs'] = self.security_group_ids
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('IPStack') is not None:
            self.ipstack = m.get('IPStack')
        if m.get('SecurityGroupIDs') is not None:
            self.security_group_ids = m.get('SecurityGroupIDs')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeHubClusterDetailsResponseBodyCluster(TeaModel):
    def __init__(self, api_server=None, cluster_info=None, conditions=None, endpoints=None, log_config=None,
                 mesh_config=None, network=None):
        # Information about the API server of the master instance.
        self.api_server = api_server  # type: DescribeHubClusterDetailsResponseBodyClusterApiServer
        # The details about the master instance.
        self.cluster_info = cluster_info  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfo
        # 集群删除条件信息列表
        self.conditions = conditions  # type: list[DescribeHubClusterDetailsResponseBodyClusterConditions]
        # The endpoint of the master instance.
        self.endpoints = endpoints  # type: DescribeHubClusterDetailsResponseBodyClusterEndpoints
        # The logging configuration.
        self.log_config = log_config  # type: DescribeHubClusterDetailsResponseBodyClusterLogConfig
        # The Service Mesh (ASM) configurations.
        self.mesh_config = mesh_config  # type: DescribeHubClusterDetailsResponseBodyClusterMeshConfig
        # The network configurations of the master instance.
        self.network = network  # type: DescribeHubClusterDetailsResponseBodyClusterNetwork

    def validate(self):
        if self.api_server:
            self.api_server.validate()
        if self.cluster_info:
            self.cluster_info.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.endpoints:
            self.endpoints.validate()
        if self.log_config:
            self.log_config.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server is not None:
            result['ApiServer'] = self.api_server.to_map()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServer') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterApiServer()
            self.api_server = temp_model.from_map(m['ApiServer'])
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeHubClusterDetailsResponseBodyClusterConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Endpoints') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('LogConfig') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterLogConfig()
            self.log_config = temp_model.from_map(m['LogConfig'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeHubClusterDetailsResponseBody(TeaModel):
    def __init__(self, cluster=None, request_id=None):
        # The details about the master instance.
        self.cluster = cluster  # type: DescribeHubClusterDetailsResponseBodyCluster
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.cluster:
            self.cluster.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClusterDetailsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClusterDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterKubeconfigRequest(TeaModel):
    def __init__(self, cluster_id=None, private_ip_address=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to obtain the credential that is used to connect to the master instance over the internal network. Valid values: - `true`: obtains only the credential that is used to access the master instance over the internal network. - `false`: obtains only the credential that is used to access the master instance over the Internet. Default value: `false`.
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterKubeconfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeHubClusterKubeconfigResponseBody(TeaModel):
    def __init__(self, kubeconfig=None, request_id=None):
        # The content of the kubeconfig file of the master instance.
        self.kubeconfig = kubeconfig  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterKubeconfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClusterKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClusterKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClusterKubeconfigResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterLogsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterLogsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeHubClusterLogsResponseBodyLogs(TeaModel):
    def __init__(self, cluster_id=None, cluster_log=None, creation_time=None, log_level=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # A log of the master instance.
        self.cluster_log = cluster_log  # type: str
        # The time when the log was created. Format: <i>yyyy-mm-dd</i>t<i>hh:mm:ss</i>z (UTC time).
        self.creation_time = creation_time  # type: str
        # The severity level of the log. Valid values: - error: errors. - warn: warnings. - info: information.
        self.log_level = log_level  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterLogsResponseBodyLogs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_log is not None:
            result['ClusterLog'] = self.cluster_log
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterLog') is not None:
            self.cluster_log = m.get('ClusterLog')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        return self


class DescribeHubClusterLogsResponseBody(TeaModel):
    def __init__(self, logs=None, request_id=None):
        # Brief information about operation logs.
        self.logs = logs  # type: list[DescribeHubClusterLogsResponseBodyLogs]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClusterLogsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = DescribeHubClusterLogsResponseBodyLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClusterLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClusterLogsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClustersRequest(TeaModel):
    def __init__(self, profile=None):
        # The scenario where master instances are used. Valid values:
        # 
        # *   `Default`: standard scenarios.
        # *   `XFlow`: workflow scenarios.
        # 
        # Default value: `Default`.
        self.profile = profile  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        return self


class DescribeHubClustersResponseBodyClustersApiServer(TeaModel):
    def __init__(self, api_server_eip_id=None, enabled_public=None, load_balancer_id=None):
        # The ID of the elastic IP address (EIP).
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Indicates whether the API server is accessible over the Internet. Valid values:
        # 
        # *   true: The API server is accessible over the Internet.
        # *   false: The API server is inaccessible over the Internet.
        self.enabled_public = enabled_public  # type: bool
        # The ID of the Server Load Balancer (SLB) instance that is associated with the Kubernetes API server.
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersApiServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.enabled_public is not None:
            result['EnabledPublic'] = self.enabled_public
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('EnabledPublic') is not None:
            self.enabled_public = m.get('EnabledPublic')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeHubClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, creation_time=None, error_message=None, name=None,
                 profile=None, region_id=None, state=None, update_time=None, version=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The specification of the master instance.
        # 
        # *   ack.pro.small: ACK Pro cluster
        self.cluster_spec = cluster_spec  # type: str
        # The time when the master instance was created.
        self.creation_time = creation_time  # type: str
        # The error message returned when the master instance failed to be created.
        self.error_message = error_message  # type: str
        # The name of the master instance.
        self.name = name  # type: str
        # The configurations of the master instance.
        self.profile = profile  # type: str
        # The ID of the region in which the master instance resides.
        self.region_id = region_id  # type: str
        # The status of the master instance. Valid values:
        # 
        # *   initial: The master instance is being initialized.
        # *   failed: The master instance failed to be created.
        # *   running: The master instance is running
        # *   inactive: The master instance is pending.
        # *   deleting: The master instance is being deleted.
        # *   delete_failed: The master instance failed to be deleted.
        # *   deleted: The master instance is deleted.
        self.state = state  # type: str
        # The last time when the master instance was updated.
        self.update_time = update_time  # type: str
        # The Kubernetes version of the master instance.
        self.version = version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersClusterInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.state is not None:
            result['State'] = self.state
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class DescribeHubClustersResponseBodyClustersConditions(TeaModel):
    def __init__(self, message=None, reason=None, status=None, type=None):
        # The error message of the deletion condition.
        self.message = message  # type: str
        # The reason for the deletion condition.
        self.reason = reason  # type: str
        # The status of the deletion condition. Valid values:
        # 
        # *   True: The master instance cannot be deleted.
        # *   False: The master instance can be deleted.
        # *   Unknow: Whether the master instance can be deleted is unknown.
        self.status = status  # type: str
        # The type of deletion condition.
        self.type = type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersConditions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeHubClustersResponseBodyClustersEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        # The internal endpoint of the API server.
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        # The public endpoint of the API server.
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeHubClustersResponseBodyClustersLogConfig(TeaModel):
    def __init__(self, enable_log=None, log_project=None, log_store_ttl=None):
        # Indicates whether audit logging is enabled. Valid values:
        # 
        # *   true: Audit logging is enabled.
        # *   false: Audit logging is disabled.
        self.enable_log = enable_log  # type: bool
        # The name of the project of Log Service.
        self.log_project = log_project  # type: str
        # The number of days that logs are retained by Log Service.
        self.log_store_ttl = log_store_ttl  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersLogConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_log is not None:
            result['EnableLog'] = self.enable_log
        if self.log_project is not None:
            result['LogProject'] = self.log_project
        if self.log_store_ttl is not None:
            result['LogStoreTTL'] = self.log_store_ttl
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableLog') is not None:
            self.enable_log = m.get('EnableLog')
        if m.get('LogProject') is not None:
            self.log_project = m.get('LogProject')
        if m.get('LogStoreTTL') is not None:
            self.log_store_ttl = m.get('LogStoreTTL')
        return self


class DescribeHubClustersResponseBodyClustersMeshConfig(TeaModel):
    def __init__(self, enable_mesh=None, mesh_id=None):
        # Indicates whether ASM is enabled. Valid values:
        # 
        # *   true: ASM is enabled.
        # *   false: ASM is disabled.
        self.enable_mesh = enable_mesh  # type: bool
        # The ID of the ASM instance.
        self.mesh_id = mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersMeshConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.mesh_id is not None:
            result['MeshId'] = self.mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('MeshId') is not None:
            self.mesh_id = m.get('MeshId')
        return self


class DescribeHubClustersResponseBodyClustersNetwork(TeaModel):
    def __init__(self, cluster_domain=None, security_group_ids=None, v_switches=None, vpc_id=None):
        # The domain name of the master instance.
        self.cluster_domain = cluster_domain  # type: str
        # The security group IDs of the master instance.
        self.security_group_ids = security_group_ids  # type: list[str]
        # The IDs of the vSwitches to which the master instance is connected.
        self.v_switches = v_switches  # type: list[str]
        # The ID of the virtual private cloud (VPC) to which the master instance belongs.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.security_group_ids is not None:
            result['SecurityGroupIDs'] = self.security_group_ids
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('SecurityGroupIDs') is not None:
            self.security_group_ids = m.get('SecurityGroupIDs')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeHubClustersResponseBodyClusters(TeaModel):
    def __init__(self, api_server=None, cluster_info=None, conditions=None, endpoints=None, log_config=None,
                 mesh_config=None, network=None):
        # The details of the Kubernetes API server.
        self.api_server = api_server  # type: DescribeHubClustersResponseBodyClustersApiServer
        # The details of the master instance.
        self.cluster_info = cluster_info  # type: DescribeHubClustersResponseBodyClustersClusterInfo
        # The list of the deletion conditions of the master instance.
        self.conditions = conditions  # type: list[DescribeHubClustersResponseBodyClustersConditions]
        # The endpoint of the master instance.
        self.endpoints = endpoints  # type: DescribeHubClustersResponseBodyClustersEndpoints
        # The logging configurations.
        self.log_config = log_config  # type: DescribeHubClustersResponseBodyClustersLogConfig
        # The configurations of Alibaba Cloud Service Mesh (ASM).
        self.mesh_config = mesh_config  # type: DescribeHubClustersResponseBodyClustersMeshConfig
        # The network configurations of the master instance.
        self.network = network  # type: DescribeHubClustersResponseBodyClustersNetwork

    def validate(self):
        if self.api_server:
            self.api_server.validate()
        if self.cluster_info:
            self.cluster_info.validate()
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()
        if self.endpoints:
            self.endpoints.validate()
        if self.log_config:
            self.log_config.validate()
        if self.mesh_config:
            self.mesh_config.validate()
        if self.network:
            self.network.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server is not None:
            result['ApiServer'] = self.api_server.to_map()
        if self.cluster_info is not None:
            result['ClusterInfo'] = self.cluster_info.to_map()
        result['Conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['Conditions'].append(k.to_map() if k else None)
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.log_config is not None:
            result['LogConfig'] = self.log_config.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServer') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersApiServer()
            self.api_server = temp_model.from_map(m['ApiServer'])
        if m.get('ClusterInfo') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersClusterInfo()
            self.cluster_info = temp_model.from_map(m['ClusterInfo'])
        self.conditions = []
        if m.get('Conditions') is not None:
            for k in m.get('Conditions'):
                temp_model = DescribeHubClustersResponseBodyClustersConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('Endpoints') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('LogConfig') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersLogConfig()
            self.log_config = temp_model.from_map(m['LogConfig'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        if m.get('Network') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeHubClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        # The list of the master instances returned.
        self.clusters = clusters  # type: list[DescribeHubClustersResponseBodyClusters]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeHubClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeHubClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeHubClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeHubClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeHubClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManagedClustersRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeManagedClustersResponseBodyClustersCluster(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, cluster_type=None, created=None, current_version=None,
                 init_version=None, name=None, profile=None, region=None, resource_group_id=None, state=None, updated=None,
                 v_switch_id=None, vpc_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The specification of the master instance. Valid values: - ack.pro.small: ACK Pro.
        self.cluster_spec = cluster_spec  # type: str
        # The type of the master instance.
        self.cluster_type = cluster_type  # type: str
        # The time when the master instance was created.
        self.created = created  # type: str
        # The current Kubernetes version of the master instance.
        self.current_version = current_version  # type: str
        # The original Kubernetes version of the master instance.
        self.init_version = init_version  # type: str
        # The name of the master instance.
        self.name = name  # type: str
        # The name of the master instance.
        self.profile = profile  # type: str
        # The region in which the master instance resides.
        self.region = region  # type: str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The status of the associated clusters. Valid values: - initial: The associated clusters are being initialized. - failed: The associated clustersfailed to be created. - running: The associated clusters are running. - inactive: The associated clusters are inactive. - deleting: The associated clusters are being deleted. - deleted: The associated clusters are deleted.
        self.state = state  # type: str
        # The time when the master instance was updated.
        self.updated = updated  # type: str
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id  # type: str
        # VPC ID.
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClustersCluster, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterID'] = self.cluster_id
        if self.cluster_spec is not None:
            result['ClusterSpec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.created is not None:
            result['Created'] = self.created
        if self.current_version is not None:
            result['CurrentVersion'] = self.current_version
        if self.init_version is not None:
            result['InitVersion'] = self.init_version
        if self.name is not None:
            result['Name'] = self.name
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region is not None:
            result['Region'] = self.region
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.state is not None:
            result['State'] = self.state
        if self.updated is not None:
            result['Updated'] = self.updated
        if self.v_switch_id is not None:
            result['VSwitchID'] = self.v_switch_id
        if self.vpc_id is not None:
            result['VpcID'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterID') is not None:
            self.cluster_id = m.get('ClusterID')
        if m.get('ClusterSpec') is not None:
            self.cluster_spec = m.get('ClusterSpec')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Created') is not None:
            self.created = m.get('Created')
        if m.get('CurrentVersion') is not None:
            self.current_version = m.get('CurrentVersion')
        if m.get('InitVersion') is not None:
            self.init_version = m.get('InitVersion')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('Updated') is not None:
            self.updated = m.get('Updated')
        if m.get('VSwitchID') is not None:
            self.v_switch_id = m.get('VSwitchID')
        if m.get('VpcID') is not None:
            self.vpc_id = m.get('VpcID')
        return self


class DescribeManagedClustersResponseBodyClustersMeshStatus(TeaModel):
    def __init__(self, in_mesh=None):
        # Indicates whether the clusters are associated with ASM instances. Valid values: - true: The clusters are associated with ASM instances. - false: The clusters are not associated with ASM instances.
        self.in_mesh = in_mesh  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClustersMeshStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.in_mesh is not None:
            result['InMesh'] = self.in_mesh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InMesh') is not None:
            self.in_mesh = m.get('InMesh')
        return self


class DescribeManagedClustersResponseBodyClustersStatus(TeaModel):
    def __init__(self, message=None, state=None):
        # The status information.
        self.message = message  # type: str
        # The status of the association between the clusters and the master instance. Valid values: - Installing: The clusters are being associated with the master instance. - Successed: The clusters are associated with the master instance. - Failed: The clusters failed to be associated with the master instance. - Deleting: The clusters are being disassociated from the master instance. - Deleted: The clusters are disassociated from the master instance.
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClustersStatus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class DescribeManagedClustersResponseBodyClusters(TeaModel):
    def __init__(self, cluster=None, mesh_status=None, status=None):
        # The name of the master instance.
        self.cluster = cluster  # type: DescribeManagedClustersResponseBodyClustersCluster
        # The status of the association between the clusters and Service Mesh (ASM).
        self.mesh_status = mesh_status  # type: DescribeManagedClustersResponseBodyClustersMeshStatus
        # The status of the association between the clusters and the master instance.
        self.status = status  # type: DescribeManagedClustersResponseBodyClustersStatus

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.mesh_status:
            self.mesh_status.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.mesh_status is not None:
            result['MeshStatus'] = self.mesh_status.to_map()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('MeshStatus') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersMeshStatus()
            self.mesh_status = temp_model.from_map(m['MeshStatus'])
        if m.get('Status') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class DescribeManagedClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        # Information about the master instance.
        self.clusters = clusters  # type: list[DescribeManagedClustersResponseBodyClusters]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeManagedClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeManagedClustersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeManagedClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeManagedClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, language=None):
        # The language. Valid values: zh, en, and jp.
        self.language = language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.language is not None:
            result['Language'] = self.language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # A list of available regions that are returned.
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


class DetachClusterFromHubRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids=None, detach_from_mesh=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # A JSON string that can be parsed into a string array. The string specifies the clusters that you want to disassociate from the master instance.
        self.cluster_ids = cluster_ids  # type: str
        # Specifies whether to only disassociate the clusters from Service Mesh (ASM) instances. Valid values: - true: only disassociates the clusters from ASM instances. - false: disassociates the clusters from the master instance and ASM instances.
        self.detach_from_mesh = detach_from_mesh  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachClusterFromHubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        if self.detach_from_mesh is not None:
            result['DetachFromMesh'] = self.detach_from_mesh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        if m.get('DetachFromMesh') is not None:
            self.detach_from_mesh = m.get('DetachFromMesh')
        return self


class DetachClusterFromHubResponseBody(TeaModel):
    def __init__(self, cluster_id=None, managed_cluster_ids=None, request_id=None, task_id=None):
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # The IDs of the clusters that are disassociated from the master instance.
        self.managed_cluster_ids = managed_cluster_ids  # type: list[str]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The ID of the task.
        self.task_id = task_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachClusterFromHubResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.managed_cluster_ids is not None:
            result['ManagedClusterIds'] = self.managed_cluster_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ManagedClusterIds') is not None:
            self.managed_cluster_ids = m.get('ManagedClusterIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DetachClusterFromHubResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachClusterFromHubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachClusterFromHubResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DetachClusterFromHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHubClusterFeatureRequestUnitsVSwitches(TeaModel):
    def __init__(self, vswitch_id=None, zone_id=None):
        self.vswitch_id = vswitch_id  # type: str
        self.zone_id = zone_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHubClusterFeatureRequestUnitsVSwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class UpdateHubClusterFeatureRequestUnits(TeaModel):
    def __init__(self, region_id=None, v_switches=None, vpc_id=None):
        self.region_id = region_id  # type: str
        self.v_switches = v_switches  # type: list[UpdateHubClusterFeatureRequestUnitsVSwitches]
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateHubClusterFeatureRequestUnits, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = UpdateHubClusterFeatureRequestUnitsVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class UpdateHubClusterFeatureRequest(TeaModel):
    def __init__(self, api_server_eip_id=None, audit_log_enabled=None, cluster_id=None, deletion_protection=None,
                 enable_argo_cd=None, enable_mesh=None, enabled=None, name=None, price_limit=None, public_api_server_enabled=None,
                 schedule_mode=None, server_enabled=None, units=None):
        # The ID of the EIP.
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Specifies whether to enable audit logs. Valid values: - true: enable audit logs. - false: disables audit logs.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to enable deletion protection for the master instance. After you enable deletion protection, you cannot delete the master instance in the console or by calling API operations. Valid values:
        self.deletion_protection = deletion_protection  # type: bool
        # Whether to enable ArgoCD.
        # 
        # - true Enabled
        # - false Disabled
        self.enable_argo_cd = enable_argo_cd  # type: bool
        # Specifies whether to enable Service Mesh (ASM). Valid values: true: enables ASM. false: disables ASM.
        self.enable_mesh = enable_mesh  # type: bool
        self.enabled = enabled  # type: bool
        # The name of the master instance. The name must be 1 to 63 characters in length, and can contain letters and digits. The name must start with a letter. The name can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name  # type: str
        self.price_limit = price_limit  # type: str
        # Specifies whether to associate an elastic IP address (EIP) with the API server. Default value: false. To associate an EIP with the API server, set the value to true. You can use a custom EIP by setting the ApiServerEipId parameter. If you do not set the ApiServerEipId parameter, the system automatically creates an EIP.
        self.public_api_server_enabled = public_api_server_enabled  # type: bool
        self.schedule_mode = schedule_mode  # type: str
        self.server_enabled = server_enabled  # type: bool
        self.units = units  # type: list[UpdateHubClusterFeatureRequestUnits]

    def validate(self):
        if self.units:
            for k in self.units:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UpdateHubClusterFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.enable_argo_cd is not None:
            result['EnableArgoCD'] = self.enable_argo_cd
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.public_api_server_enabled is not None:
            result['PublicApiServerEnabled'] = self.public_api_server_enabled
        if self.schedule_mode is not None:
            result['ScheduleMode'] = self.schedule_mode
        if self.server_enabled is not None:
            result['ServerEnabled'] = self.server_enabled
        result['Units'] = []
        if self.units is not None:
            for k in self.units:
                result['Units'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EnableArgoCD') is not None:
            self.enable_argo_cd = m.get('EnableArgoCD')
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('PublicApiServerEnabled') is not None:
            self.public_api_server_enabled = m.get('PublicApiServerEnabled')
        if m.get('ScheduleMode') is not None:
            self.schedule_mode = m.get('ScheduleMode')
        if m.get('ServerEnabled') is not None:
            self.server_enabled = m.get('ServerEnabled')
        self.units = []
        if m.get('Units') is not None:
            for k in m.get('Units'):
                temp_model = UpdateHubClusterFeatureRequestUnits()
                self.units.append(temp_model.from_map(k))
        return self


class UpdateHubClusterFeatureShrinkRequest(TeaModel):
    def __init__(self, api_server_eip_id=None, audit_log_enabled=None, cluster_id=None, deletion_protection=None,
                 enable_argo_cd=None, enable_mesh=None, enabled=None, name=None, price_limit=None, public_api_server_enabled=None,
                 schedule_mode=None, server_enabled=None, units_shrink=None):
        # The ID of the EIP.
        self.api_server_eip_id = api_server_eip_id  # type: str
        # Specifies whether to enable audit logs. Valid values: - true: enable audit logs. - false: disables audit logs.
        self.audit_log_enabled = audit_log_enabled  # type: bool
        # The ID of the master instance.
        self.cluster_id = cluster_id  # type: str
        # Specifies whether to enable deletion protection for the master instance. After you enable deletion protection, you cannot delete the master instance in the console or by calling API operations. Valid values:
        self.deletion_protection = deletion_protection  # type: bool
        # Whether to enable ArgoCD.
        # 
        # - true Enabled
        # - false Disabled
        self.enable_argo_cd = enable_argo_cd  # type: bool
        # Specifies whether to enable Service Mesh (ASM). Valid values: true: enables ASM. false: disables ASM.
        self.enable_mesh = enable_mesh  # type: bool
        self.enabled = enabled  # type: bool
        # The name of the master instance. The name must be 1 to 63 characters in length, and can contain letters and digits. The name must start with a letter. The name can contain letters, digits, underscores (_), and hyphens (-).
        self.name = name  # type: str
        self.price_limit = price_limit  # type: str
        # Specifies whether to associate an elastic IP address (EIP) with the API server. Default value: false. To associate an EIP with the API server, set the value to true. You can use a custom EIP by setting the ApiServerEipId parameter. If you do not set the ApiServerEipId parameter, the system automatically creates an EIP.
        self.public_api_server_enabled = public_api_server_enabled  # type: bool
        self.schedule_mode = schedule_mode  # type: str
        self.server_enabled = server_enabled  # type: bool
        self.units_shrink = units_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHubClusterFeatureShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip_id is not None:
            result['ApiServerEipId'] = self.api_server_eip_id
        if self.audit_log_enabled is not None:
            result['AuditLogEnabled'] = self.audit_log_enabled
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection
        if self.enable_argo_cd is not None:
            result['EnableArgoCD'] = self.enable_argo_cd
        if self.enable_mesh is not None:
            result['EnableMesh'] = self.enable_mesh
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.name is not None:
            result['Name'] = self.name
        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit
        if self.public_api_server_enabled is not None:
            result['PublicApiServerEnabled'] = self.public_api_server_enabled
        if self.schedule_mode is not None:
            result['ScheduleMode'] = self.schedule_mode
        if self.server_enabled is not None:
            result['ServerEnabled'] = self.server_enabled
        if self.units_shrink is not None:
            result['Units'] = self.units_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApiServerEipId') is not None:
            self.api_server_eip_id = m.get('ApiServerEipId')
        if m.get('AuditLogEnabled') is not None:
            self.audit_log_enabled = m.get('AuditLogEnabled')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')
        if m.get('EnableArgoCD') is not None:
            self.enable_argo_cd = m.get('EnableArgoCD')
        if m.get('EnableMesh') is not None:
            self.enable_mesh = m.get('EnableMesh')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')
        if m.get('PublicApiServerEnabled') is not None:
            self.public_api_server_enabled = m.get('PublicApiServerEnabled')
        if m.get('ScheduleMode') is not None:
            self.schedule_mode = m.get('ScheduleMode')
        if m.get('ServerEnabled') is not None:
            self.server_enabled = m.get('ServerEnabled')
        if m.get('Units') is not None:
            self.units_shrink = m.get('Units')
        return self


class UpdateHubClusterFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateHubClusterFeatureResponseBody, self).to_map()
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


class UpdateHubClusterFeatureResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateHubClusterFeatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateHubClusterFeatureResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateHubClusterFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


