# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AttachClusterToHubRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_ids = cluster_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachClusterToHubRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_ids is not None:
            result['ClusterIds'] = self.cluster_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        return self


class AttachClusterToHubResponseBody(TeaModel):
    def __init__(self, cluster_id=None, managed_cluster_ids=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.managed_cluster_ids = managed_cluster_ids  # type: list[str]
        self.request_id = request_id  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ManagedClusterIds') is not None:
            self.managed_cluster_ids = m.get('ManagedClusterIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachClusterToHubResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachClusterToHubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachClusterToHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHubClusterRequest(TeaModel):
    def __init__(self, api_server_public_eip=None, audit_log_enabled=None, audit_log_project=None,
                 audit_log_store_ttl=None, control_plane_log_enabled=None, control_plane_log_project=None, control_plane_log_ttl=None,
                 is_enterprise_security_group=None, name=None, region_id=None, v_switches=None, vpc_id=None):
        self.api_server_public_eip = api_server_public_eip  # type: bool
        self.audit_log_enabled = audit_log_enabled  # type: bool
        self.audit_log_project = audit_log_project  # type: str
        self.audit_log_store_ttl = audit_log_store_ttl  # type: str
        self.control_plane_log_enabled = control_plane_log_enabled  # type: bool
        self.control_plane_log_project = control_plane_log_project  # type: str
        self.control_plane_log_ttl = control_plane_log_ttl  # type: str
        # 是否企业安全组
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # 集群名称
        self.name = name  # type: str
        self.region_id = region_id  # type: str
        self.v_switches = v_switches  # type: str
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
        if self.audit_log_project is not None:
            result['AuditLogProject'] = self.audit_log_project
        if self.audit_log_store_ttl is not None:
            result['AuditLogStoreTTL'] = self.audit_log_store_ttl
        if self.control_plane_log_enabled is not None:
            result['ControlPlaneLogEnabled'] = self.control_plane_log_enabled
        if self.control_plane_log_project is not None:
            result['ControlPlaneLogProject'] = self.control_plane_log_project
        if self.control_plane_log_ttl is not None:
            result['ControlPlaneLogTTL'] = self.control_plane_log_ttl
        if self.is_enterprise_security_group is not None:
            result['IsEnterpriseSecurityGroup'] = self.is_enterprise_security_group
        if self.name is not None:
            result['Name'] = self.name
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
        if m.get('AuditLogProject') is not None:
            self.audit_log_project = m.get('AuditLogProject')
        if m.get('AuditLogStoreTTL') is not None:
            self.audit_log_store_ttl = m.get('AuditLogStoreTTL')
        if m.get('ControlPlaneLogEnabled') is not None:
            self.control_plane_log_enabled = m.get('ControlPlaneLogEnabled')
        if m.get('ControlPlaneLogProject') is not None:
            self.control_plane_log_project = m.get('ControlPlaneLogProject')
        if m.get('ControlPlaneLogTTL') is not None:
            self.control_plane_log_ttl = m.get('ControlPlaneLogTTL')
        if m.get('IsEnterpriseSecurityGroup') is not None:
            self.is_enterprise_security_group = m.get('IsEnterpriseSecurityGroup')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class CreateHubClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHubClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHubClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHubClusterRequest(TeaModel):
    def __init__(self, cluster_id=None, force=None):
        self.cluster_id = cluster_id  # type: str
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
        self.cluster_id = cluster_id  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHubClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHubClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterDetailsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # 集群ID
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
    def __init__(self, enabled_public=None, load_balancer_id=None):
        self.enabled_public = enabled_public  # type: bool
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClusterDetailsResponseBodyClusterApiServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_public is not None:
            result['EnabledPublic'] = self.enabled_public
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnabledPublic') is not None:
            self.enabled_public = m.get('EnabledPublic')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeHubClusterDetailsResponseBodyClusterClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, creation_time=None, error_message=None, name=None,
                 profile=None, region_id=None, state=None, update_time=None, version=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_spec = cluster_spec  # type: str
        self.creation_time = creation_time  # type: str
        self.error_message = error_message  # type: str
        self.name = name  # type: str
        self.profile = profile  # type: str
        self.region_id = region_id  # type: str
        self.state = state  # type: str
        self.update_time = update_time  # type: str
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


class DescribeHubClusterDetailsResponseBodyClusterEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
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


class DescribeHubClusterDetailsResponseBodyClusterNetwork(TeaModel):
    def __init__(self, cluster_domain=None, ipstack=None, security_group_ids=None, v_switches=None, vpc_id=None):
        self.cluster_domain = cluster_domain  # type: str
        self.ipstack = ipstack  # type: str
        self.security_group_ids = security_group_ids  # type: list[str]
        self.v_switches = v_switches  # type: list[str]
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
    def __init__(self, api_server=None, cluster_info=None, endpoints=None, network=None):
        self.api_server = api_server  # type: DescribeHubClusterDetailsResponseBodyClusterApiServer
        self.cluster_info = cluster_info  # type: DescribeHubClusterDetailsResponseBodyClusterClusterInfo
        self.endpoints = endpoints  # type: DescribeHubClusterDetailsResponseBodyClusterEndpoints
        self.network = network  # type: DescribeHubClusterDetailsResponseBodyClusterNetwork

    def validate(self):
        if self.api_server:
            self.api_server.validate()
        if self.cluster_info:
            self.cluster_info.validate()
        if self.endpoints:
            self.endpoints.validate()
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
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
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
        if m.get('Endpoints') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('Network') is not None:
            temp_model = DescribeHubClusterDetailsResponseBodyClusterNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeHubClusterDetailsResponseBody(TeaModel):
    def __init__(self, cluster=None, request_id=None):
        self.cluster = cluster  # type: DescribeHubClusterDetailsResponseBodyCluster
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHubClusterDetailsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterKubeconfigRequest(TeaModel):
    def __init__(self, cluster_id=None, private_ip_address=None):
        self.cluster_id = cluster_id  # type: str
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
        self.kubeconfig = kubeconfig  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHubClusterKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClusterLogsRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # 集群ID
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
        self.cluster_id = cluster_id  # type: str
        self.cluster_log = cluster_log  # type: str
        self.creation_time = creation_time  # type: str
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
        self.logs = logs  # type: list[DescribeHubClusterLogsResponseBodyLogs]
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHubClusterLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHubClusterLogsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHubClustersResponseBodyClustersApiServer(TeaModel):
    def __init__(self, enabled_public=None, load_balancer_id=None):
        self.enabled_public = enabled_public  # type: bool
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeHubClustersResponseBodyClustersApiServer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_public is not None:
            result['EnabledPublic'] = self.enabled_public
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnabledPublic') is not None:
            self.enabled_public = m.get('EnabledPublic')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class DescribeHubClustersResponseBodyClustersClusterInfo(TeaModel):
    def __init__(self, cluster_id=None, cluster_spec=None, creation_time=None, error_message=None, name=None,
                 profile=None, region_id=None, state=None, update_time=None, version=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_spec = cluster_spec  # type: str
        self.creation_time = creation_time  # type: str
        self.error_message = error_message  # type: str
        self.name = name  # type: str
        self.profile = profile  # type: str
        self.region_id = region_id  # type: str
        self.state = state  # type: str
        self.update_time = update_time  # type: str
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


class DescribeHubClustersResponseBodyClustersEndpoints(TeaModel):
    def __init__(self, intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
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


class DescribeHubClustersResponseBodyClustersNetwork(TeaModel):
    def __init__(self, cluster_domain=None, security_group_ids=None, v_switches=None, vpc_id=None):
        self.cluster_domain = cluster_domain  # type: str
        self.security_group_ids = security_group_ids  # type: list[str]
        self.v_switches = v_switches  # type: list[str]
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
    def __init__(self, api_server=None, cluster_info=None, endpoints=None, network=None):
        self.api_server = api_server  # type: DescribeHubClustersResponseBodyClustersApiServer
        self.cluster_info = cluster_info  # type: DescribeHubClustersResponseBodyClustersClusterInfo
        self.endpoints = endpoints  # type: DescribeHubClustersResponseBodyClustersEndpoints
        self.network = network  # type: DescribeHubClustersResponseBodyClustersNetwork

    def validate(self):
        if self.api_server:
            self.api_server.validate()
        if self.cluster_info:
            self.cluster_info.validate()
        if self.endpoints:
            self.endpoints.validate()
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
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
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
        if m.get('Endpoints') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('Network') is not None:
            temp_model = DescribeHubClustersResponseBodyClustersNetwork()
            self.network = temp_model.from_map(m['Network'])
        return self


class DescribeHubClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        self.clusters = clusters  # type: list[DescribeHubClustersResponseBodyClusters]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeHubClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHubClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManagedClustersRequest(TeaModel):
    def __init__(self, cluster_id=None):
        # 集群ID
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
        self.cluster_id = cluster_id  # type: str
        self.cluster_spec = cluster_spec  # type: str
        self.cluster_type = cluster_type  # type: str
        self.created = created  # type: str
        self.current_version = current_version  # type: str
        self.init_version = init_version  # type: str
        self.name = name  # type: str
        self.profile = profile  # type: str
        self.region = region  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.state = state  # type: str
        self.updated = updated  # type: str
        self.v_switch_id = v_switch_id  # type: str
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


class DescribeManagedClustersResponseBodyClustersStatus(TeaModel):
    def __init__(self, message=None, state=None):
        self.message = message  # type: str
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
    def __init__(self, cluster=None, status=None):
        self.cluster = cluster  # type: DescribeManagedClustersResponseBodyClustersCluster
        self.status = status  # type: DescribeManagedClustersResponseBodyClustersStatus

    def validate(self):
        if self.cluster:
            self.cluster.validate()
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super(DescribeManagedClustersResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['Cluster'] = self.cluster.to_map()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Cluster') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersCluster()
            self.cluster = temp_model.from_map(m['Cluster'])
        if m.get('Status') is not None:
            temp_model = DescribeManagedClustersResponseBodyClustersStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class DescribeManagedClustersResponseBody(TeaModel):
    def __init__(self, clusters=None, request_id=None):
        self.clusters = clusters  # type: list[DescribeManagedClustersResponseBodyClusters]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeManagedClustersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeManagedClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None, region_vpc_endpoint=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
        self.region_id = region_id  # type: str
        self.region_vpc_endpoint = region_vpc_endpoint  # type: str

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
        if self.region_vpc_endpoint is not None:
            result['RegionVpcEndpoint'] = self.region_vpc_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RegionVpcEndpoint') is not None:
            self.region_vpc_endpoint = m.get('RegionVpcEndpoint')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachClusterFromHubRequest(TeaModel):
    def __init__(self, cluster_id=None, cluster_ids=None):
        self.cluster_id = cluster_id  # type: str
        self.cluster_ids = cluster_ids  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterIds') is not None:
            self.cluster_ids = m.get('ClusterIds')
        return self


class DetachClusterFromHubResponseBody(TeaModel):
    def __init__(self, cluster_id=None, managed_cluster_ids=None, request_id=None):
        self.cluster_id = cluster_id  # type: str
        self.managed_cluster_ids = managed_cluster_ids  # type: list[str]
        self.request_id = request_id  # type: str

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
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ManagedClusterIds') is not None:
            self.managed_cluster_ids = m.get('ManagedClusterIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DetachClusterFromHubResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachClusterFromHubResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachClusterFromHubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


