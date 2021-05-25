# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class RunDiagnosisRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunDiagnosisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class RunDiagnosisResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RunDiagnosisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class RunDiagnosisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RunDiagnosisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RunDiagnosisResponse, self).to_map()
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
            temp_model = RunDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGuestClusterAccessLogDashboardsRequest(TeaModel):
    def __init__(self, k_8s_cluster_id=None):
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGuestClusterAccessLogDashboardsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards(TeaModel):
    def __init__(self, url=None, title=None):
        self.url = url  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeGuestClusterAccessLogDashboardsResponseBody(TeaModel):
    def __init__(self, request_id=None, dashboards=None, k_8s_cluster_id=None):
        self.request_id = request_id  # type: str
        self.dashboards = dashboards  # type: list[DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards]
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeGuestClusterAccessLogDashboardsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeGuestClusterAccessLogDashboardsResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeGuestClusterAccessLogDashboardsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeGuestClusterAccessLogDashboardsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeGuestClusterAccessLogDashboardsResponse, self).to_map()
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
            temp_model = DescribeGuestClusterAccessLogDashboardsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(self, service_mesh_id=None, id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.id = id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBuiltinEnvoyFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListBuiltinEnvoyFilterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListBuiltinEnvoyFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListBuiltinEnvoyFilterResponse, self).to_map()
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
            temp_model = ListBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesEndpoints(TeaModel):
    def __init__(self, intranet_pilot_endpoint=None, reverse_tunnel_endpoint=None, public_pilot_endpoint=None,
                 intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        self.intranet_pilot_endpoint = intranet_pilot_endpoint  # type: str
        self.reverse_tunnel_endpoint = reverse_tunnel_endpoint  # type: str
        self.public_pilot_endpoint = public_pilot_endpoint  # type: str
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.reverse_tunnel_endpoint is not None:
            result['ReverseTunnelEndpoint'] = self.reverse_tunnel_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('ReverseTunnelEndpoint') is not None:
            self.reverse_tunnel_endpoint = m.get('ReverseTunnelEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo(TeaModel):
    def __init__(self, profile=None, creation_time=None, update_time=None, error_message=None, version=None,
                 state=None, service_mesh_id=None, name=None, region_id=None):
        self.profile = profile  # type: str
        self.creation_time = creation_time  # type: str
        self.update_time = update_time  # type: str
        self.error_message = error_message  # type: str
        self.version = version  # type: str
        self.state = state  # type: str
        self.service_mesh_id = service_mesh_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.version is not None:
            result['Version'] = self.version
        if self.state is not None:
            result['State'] = self.state
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork(TeaModel):
    def __init__(self, vpc_id=None, security_group_id=None, v_switches=None):
        self.vpc_id = vpc_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switches = v_switches  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer(TeaModel):
    def __init__(self, pilot_public_eip=None, pilot_public_loadbalancer_id=None, api_server_loadbalancer_id=None,
                 api_server_public_eip=None):
        self.pilot_public_eip = pilot_public_eip  # type: bool
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id  # type: str
        self.api_server_loadbalancer_id = api_server_loadbalancer_id  # type: str
        self.api_server_public_eip = api_server_public_eip  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot(TeaModel):
    def __init__(self, http_10enabled=None, trace_sampling=None):
        self.http_10enabled = http_10enabled  # type: bool
        self.trace_sampling = trace_sampling  # type: float

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(self, exclude_namespaces=None, enabled=None):
        self.exclude_namespaces = exclude_namespaces  # type: str
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(self, enable_namespaces_by_default=None, auto_injection_policy_enabled=None,
                 init_cniconfiguration=None):
        self.enable_namespaces_by_default = enable_namespaces_by_default  # type: bool
        self.auto_injection_policy_enabled = auto_injection_policy_enabled  # type: bool
        self.init_cniconfiguration = init_cniconfiguration  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig(TeaModel):
    def __init__(self, telemetry=None, outbound_traffic_policy=None, tracing=None, strict_mtls=None, pilot=None,
                 mtls=None, sidecar_injector=None):
        self.telemetry = telemetry  # type: bool
        self.outbound_traffic_policy = outbound_traffic_policy  # type: str
        self.tracing = tracing  # type: bool
        self.strict_mtls = strict_mtls  # type: bool
        self.pilot = pilot  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot
        self.mtls = mtls  # type: bool
        self.sidecar_injector = sidecar_injector  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector

    def validate(self):
        if self.pilot:
            self.pilot.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.strict_mtls is not None:
            result['StrictMtls'] = self.strict_mtls
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.mtls is not None:
            result['Mtls'] = self.mtls
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('StrictMtls') is not None:
            self.strict_mtls = m.get('StrictMtls')
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('Mtls') is not None:
            self.mtls = m.get('Mtls')
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshesSpec(TeaModel):
    def __init__(self, network=None, load_balancer=None, mesh_config=None):
        self.network = network  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork
        self.load_balancer = load_balancer  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer
        self.mesh_config = mesh_config  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig

    def validate(self):
        if self.network:
            self.network.validate()
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshesSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        return self


class DescribeServiceMeshesResponseBodyServiceMeshes(TeaModel):
    def __init__(self, endpoints=None, service_mesh_info=None, spec=None, clusters=None):
        self.endpoints = endpoints  # type: DescribeServiceMeshesResponseBodyServiceMeshesEndpoints
        self.service_mesh_info = service_mesh_info  # type: DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo
        self.spec = spec  # type: DescribeServiceMeshesResponseBodyServiceMeshesSpec
        self.clusters = clusters  # type: list[str]

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBodyServiceMeshes, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshesResponseBodyServiceMeshesSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        return self


class DescribeServiceMeshesResponseBody(TeaModel):
    def __init__(self, request_id=None, service_meshes=None):
        self.request_id = request_id  # type: str
        self.service_meshes = service_meshes  # type: list[DescribeServiceMeshesResponseBodyServiceMeshes]

    def validate(self):
        if self.service_meshes:
            for k in self.service_meshes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ServiceMeshes'] = []
        if self.service_meshes is not None:
            for k in self.service_meshes:
                result['ServiceMeshes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.service_meshes = []
        if m.get('ServiceMeshes') is not None:
            for k in m.get('ServiceMeshes'):
                temp_model = DescribeServiceMeshesResponseBodyServiceMeshes()
                self.service_meshes.append(temp_model.from_map(k))
        return self


class DescribeServiceMeshesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceMeshesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshesResponse, self).to_map()
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
            temp_model = DescribeServiceMeshesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(self, service_mesh_id=None, id=None, name=None, parameters=None, istio_version=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: str
        self.istio_version = istio_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBuiltinEnvoyFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        return self


class ModifyBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyBuiltinEnvoyFilterResponseBody, self).to_map()
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


class ModifyBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyBuiltinEnvoyFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyBuiltinEnvoyFilterResponse, self).to_map()
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
            temp_model = ModifyBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAvailableNacosInstancesRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None):
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableNacosInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeAvailableNacosInstancesResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeAvailableNacosInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class DescribeAvailableNacosInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeAvailableNacosInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeAvailableNacosInstancesResponse, self).to_map()
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
            temp_model = DescribeAvailableNacosInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIngressGatewaysRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIngressGatewaysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeIngressGatewaysResponseBody(TeaModel):
    def __init__(self, request_id=None, ingress_gateways=None):
        self.request_id = request_id  # type: str
        self.ingress_gateways = ingress_gateways  # type: list[dict[str, any]]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeIngressGatewaysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ingress_gateways is not None:
            result['IngressGateways'] = self.ingress_gateways
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IngressGateways') is not None:
            self.ingress_gateways = m.get('IngressGateways')
        return self


class DescribeIngressGatewaysResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeIngressGatewaysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeIngressGatewaysResponse, self).to_map()
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
            temp_model = DescribeIngressGatewaysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshDetailRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints(TeaModel):
    def __init__(self, intranet_pilot_endpoint=None, public_pilot_endpoint=None,
                 intranet_api_server_endpoint=None, public_api_server_endpoint=None):
        self.intranet_pilot_endpoint = intranet_pilot_endpoint  # type: str
        self.public_pilot_endpoint = public_pilot_endpoint  # type: str
        self.intranet_api_server_endpoint = intranet_api_server_endpoint  # type: str
        self.public_api_server_endpoint = public_api_server_endpoint  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intranet_pilot_endpoint is not None:
            result['IntranetPilotEndpoint'] = self.intranet_pilot_endpoint
        if self.public_pilot_endpoint is not None:
            result['PublicPilotEndpoint'] = self.public_pilot_endpoint
        if self.intranet_api_server_endpoint is not None:
            result['IntranetApiServerEndpoint'] = self.intranet_api_server_endpoint
        if self.public_api_server_endpoint is not None:
            result['PublicApiServerEndpoint'] = self.public_api_server_endpoint
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('IntranetPilotEndpoint') is not None:
            self.intranet_pilot_endpoint = m.get('IntranetPilotEndpoint')
        if m.get('PublicPilotEndpoint') is not None:
            self.public_pilot_endpoint = m.get('PublicPilotEndpoint')
        if m.get('IntranetApiServerEndpoint') is not None:
            self.intranet_api_server_endpoint = m.get('IntranetApiServerEndpoint')
        if m.get('PublicApiServerEndpoint') is not None:
            self.public_api_server_endpoint = m.get('PublicApiServerEndpoint')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo(TeaModel):
    def __init__(self, profile=None, creation_time=None, update_time=None, error_message=None, version=None,
                 state=None, service_mesh_id=None, name=None, region_id=None):
        self.profile = profile  # type: str
        self.creation_time = creation_time  # type: str
        self.update_time = update_time  # type: str
        self.error_message = error_message  # type: str
        self.version = version  # type: str
        self.state = state  # type: str
        self.service_mesh_id = service_mesh_id  # type: str
        self.name = name  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.version is not None:
            result['Version'] = self.version
        if self.state is not None:
            result['State'] = self.state
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.name is not None:
            result['Name'] = self.name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork(TeaModel):
    def __init__(self, vpc_id=None, security_group_id=None, v_switches=None):
        self.vpc_id = vpc_id  # type: str
        self.security_group_id = security_group_id  # type: str
        self.v_switches = v_switches  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer(TeaModel):
    def __init__(self, pilot_public_eip=None, pilot_public_loadbalancer_id=None, api_server_loadbalancer_id=None,
                 api_server_public_eip=None):
        self.pilot_public_eip = pilot_public_eip  # type: bool
        self.pilot_public_loadbalancer_id = pilot_public_loadbalancer_id  # type: str
        self.api_server_loadbalancer_id = api_server_loadbalancer_id  # type: str
        self.api_server_public_eip = api_server_public_eip  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.pilot_public_loadbalancer_id is not None:
            result['PilotPublicLoadbalancerId'] = self.pilot_public_loadbalancer_id
        if self.api_server_loadbalancer_id is not None:
            result['ApiServerLoadbalancerId'] = self.api_server_loadbalancer_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('PilotPublicLoadbalancerId') is not None:
            self.pilot_public_loadbalancer_id = m.get('PilotPublicLoadbalancerId')
        if m.get('ApiServerLoadbalancerId') is not None:
            self.api_server_loadbalancer_id = m.get('ApiServerLoadbalancerId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA(TeaModel):
    def __init__(self, request_memory=None, log_level=None, enabled=None, limit_memory=None, request_cpu=None,
                 limit_cpu=None):
        self.request_memory = request_memory  # type: str
        self.log_level = log_level  # type: str
        self.enabled = enabled  # type: bool
        self.limit_memory = limit_memory  # type: str
        self.request_cpu = request_cpu  # type: str
        self.limit_cpu = limit_cpu  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.log_level is not None:
            result['LogLevel'] = self.log_level
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LogLevel') is not None:
            self.log_level = m.get('LogLevel')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus(TeaModel):
    def __init__(self, use_external=None, external_url=None):
        self.use_external = use_external  # type: bool
        self.external_url = external_url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.use_external is not None:
            result['UseExternal'] = self.use_external
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('UseExternal') is not None:
            self.use_external = m.get('UseExternal')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog(TeaModel):
    def __init__(self, enabled=None):
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature(TeaModel):
    def __init__(self, filter_gateway_cluster_config=None, enable_sdsserver=None):
        self.filter_gateway_cluster_config = filter_gateway_cluster_config  # type: bool
        self.enable_sdsserver = enable_sdsserver  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot(TeaModel):
    def __init__(self, http_10enabled=None, trace_sampling=None, feature=None):
        self.http_10enabled = http_10enabled  # type: bool
        self.trace_sampling = trace_sampling  # type: float
        self.feature = feature  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature

    def validate(self):
        if self.feature:
            self.feature.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.feature is not None:
            result['Feature'] = self.feature.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('Feature') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilotFeature()
            self.feature = temp_model.from_map(m['Feature'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE(TeaModel):
    def __init__(self, enabled=None):
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration(TeaModel):
    def __init__(self, exclude_namespaces=None, enabled=None):
        self.exclude_namespaces = exclude_namespaces  # type: str
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_namespaces is not None:
            result['ExcludeNamespaces'] = self.exclude_namespaces
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ExcludeNamespaces') is not None:
            self.exclude_namespaces = m.get('ExcludeNamespaces')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector(TeaModel):
    def __init__(self, enable_namespaces_by_default=None, request_memory=None, limit_memory=None, request_cpu=None,
                 auto_injection_policy_enabled=None, limit_cpu=None, init_cniconfiguration=None, sidecar_injector_webhook_as_yaml=None):
        self.enable_namespaces_by_default = enable_namespaces_by_default  # type: bool
        self.request_memory = request_memory  # type: str
        self.limit_memory = limit_memory  # type: str
        self.request_cpu = request_cpu  # type: str
        self.auto_injection_policy_enabled = auto_injection_policy_enabled  # type: bool
        self.limit_cpu = limit_cpu  # type: str
        self.init_cniconfiguration = init_cniconfiguration  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml  # type: str

    def validate(self):
        if self.init_cniconfiguration:
            self.init_cniconfiguration.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.init_cniconfiguration is not None:
            result['InitCNIConfiguration'] = self.init_cniconfiguration.to_map()
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('InitCNIConfiguration') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjectorInitCNIConfiguration()
            self.init_cniconfiguration = temp_model.from_map(m['InitCNIConfiguration'])
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport(TeaModel):
    def __init__(self, mysql_filter_enabled=None, redis_filter_enabled=None, thrift_filter_enabled=None,
                 dubbo_filter_enabled=None):
        self.mysql_filter_enabled = mysql_filter_enabled  # type: bool
        self.redis_filter_enabled = redis_filter_enabled  # type: bool
        self.thrift_filter_enabled = thrift_filter_enabled  # type: bool
        self.dubbo_filter_enabled = dubbo_filter_enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali(TeaModel):
    def __init__(self, enabled=None, url=None):
        self.enabled = enabled  # type: bool
        self.url = url  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment(TeaModel):
    def __init__(self, enabled=None):
        self.enabled = enabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit(TeaModel):
    def __init__(self, enabled=None, project=None):
        self.enabled = enabled  # type: bool
        self.project = project  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.project is not None:
            result['Project'] = self.project
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('Project') is not None:
            self.project = m.get('Project')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy(TeaModel):
    def __init__(self, request_memory=None, cluster_domain=None, limit_memory=None, request_cpu=None,
                 enable_dnsproxying=None, limit_cpu=None, access_log_service_enabled=None, access_log_service_host=None,
                 access_log_service_port=None):
        self.request_memory = request_memory  # type: str
        self.cluster_domain = cluster_domain  # type: str
        self.limit_memory = limit_memory  # type: str
        self.request_cpu = request_cpu  # type: str
        self.enable_dnsproxying = enable_dnsproxying  # type: bool
        self.limit_cpu = limit_cpu  # type: str
        self.access_log_service_enabled = access_log_service_enabled  # type: bool
        self.access_log_service_host = access_log_service_host  # type: str
        self.access_log_service_port = access_log_service_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory
        if self.request_cpu is not None:
            result['RequestCPU'] = self.request_cpu
        if self.enable_dnsproxying is not None:
            result['EnableDNSProxying'] = self.enable_dnsproxying
        if self.limit_cpu is not None:
            result['LimitCPU'] = self.limit_cpu
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')
        if m.get('RequestCPU') is not None:
            self.request_cpu = m.get('RequestCPU')
        if m.get('EnableDNSProxying') is not None:
            self.enable_dnsproxying = m.get('EnableDNSProxying')
        if m.get('LimitCPU') is not None:
            self.limit_cpu = m.get('LimitCPU')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport(TeaModel):
    def __init__(self, gateway_apienabled=None):
        self.gateway_apienabled = gateway_apienabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig(TeaModel):
    def __init__(self, opa=None, prometheus=None, access_log=None, pilot=None, mse=None, customized_zipkin=None,
                 sidecar_injector=None, include_ipranges=None, exclude_ipranges=None, exclude_outbound_ports=None,
                 exclude_inbound_ports=None, telemetry=None, edition=None, protocol_support=None, outbound_traffic_policy=None,
                 kiali=None, tracing=None, web_assembly_filter_deployment=None, enable_locality_lb=None, audit=None,
                 proxy=None, k_8s_new_apis_support=None):
        self.opa = opa  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA
        self.prometheus = prometheus  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus
        self.access_log = access_log  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog
        self.pilot = pilot  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot
        self.mse = mse  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE
        self.customized_zipkin = customized_zipkin  # type: bool
        self.sidecar_injector = sidecar_injector  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector
        self.include_ipranges = include_ipranges  # type: str
        self.exclude_ipranges = exclude_ipranges  # type: str
        self.exclude_outbound_ports = exclude_outbound_ports  # type: str
        self.exclude_inbound_ports = exclude_inbound_ports  # type: str
        self.telemetry = telemetry  # type: bool
        self.edition = edition  # type: str
        self.protocol_support = protocol_support  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport
        self.outbound_traffic_policy = outbound_traffic_policy  # type: str
        self.kiali = kiali  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali
        self.tracing = tracing  # type: bool
        self.web_assembly_filter_deployment = web_assembly_filter_deployment  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment
        self.enable_locality_lb = enable_locality_lb  # type: bool
        self.audit = audit  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit
        self.proxy = proxy  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy
        self.k_8s_new_apis_support = k_8s_new_apis_support  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport

    def validate(self):
        if self.opa:
            self.opa.validate()
        if self.prometheus:
            self.prometheus.validate()
        if self.access_log:
            self.access_log.validate()
        if self.pilot:
            self.pilot.validate()
        if self.mse:
            self.mse.validate()
        if self.sidecar_injector:
            self.sidecar_injector.validate()
        if self.protocol_support:
            self.protocol_support.validate()
        if self.kiali:
            self.kiali.validate()
        if self.web_assembly_filter_deployment:
            self.web_assembly_filter_deployment.validate()
        if self.audit:
            self.audit.validate()
        if self.proxy:
            self.proxy.validate()
        if self.k_8s_new_apis_support:
            self.k_8s_new_apis_support.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.opa is not None:
            result['OPA'] = self.opa.to_map()
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus.to_map()
        if self.access_log is not None:
            result['AccessLog'] = self.access_log.to_map()
        if self.pilot is not None:
            result['Pilot'] = self.pilot.to_map()
        if self.mse is not None:
            result['MSE'] = self.mse.to_map()
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.sidecar_injector is not None:
            result['SidecarInjector'] = self.sidecar_injector.to_map()
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.protocol_support is not None:
            result['ProtocolSupport'] = self.protocol_support.to_map()
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.kiali is not None:
            result['Kiali'] = self.kiali.to_map()
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.web_assembly_filter_deployment is not None:
            result['WebAssemblyFilterDeployment'] = self.web_assembly_filter_deployment.to_map()
        if self.enable_locality_lb is not None:
            result['EnableLocalityLB'] = self.enable_locality_lb
        if self.audit is not None:
            result['Audit'] = self.audit.to_map()
        if self.proxy is not None:
            result['Proxy'] = self.proxy.to_map()
        if self.k_8s_new_apis_support is not None:
            result['K8sNewAPIsSupport'] = self.k_8s_new_apis_support.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('OPA') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigOPA()
            self.opa = temp_model.from_map(m['OPA'])
        if m.get('Prometheus') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPrometheus()
            self.prometheus = temp_model.from_map(m['Prometheus'])
        if m.get('AccessLog') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAccessLog()
            self.access_log = temp_model.from_map(m['AccessLog'])
        if m.get('Pilot') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigPilot()
            self.pilot = temp_model.from_map(m['Pilot'])
        if m.get('MSE') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigMSE()
            self.mse = temp_model.from_map(m['MSE'])
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('SidecarInjector') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigSidecarInjector()
            self.sidecar_injector = temp_model.from_map(m['SidecarInjector'])
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ProtocolSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProtocolSupport()
            self.protocol_support = temp_model.from_map(m['ProtocolSupport'])
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('Kiali') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigKiali()
            self.kiali = temp_model.from_map(m['Kiali'])
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('WebAssemblyFilterDeployment') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigWebAssemblyFilterDeployment()
            self.web_assembly_filter_deployment = temp_model.from_map(m['WebAssemblyFilterDeployment'])
        if m.get('EnableLocalityLB') is not None:
            self.enable_locality_lb = m.get('EnableLocalityLB')
        if m.get('Audit') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigAudit()
            self.audit = temp_model.from_map(m['Audit'])
        if m.get('Proxy') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigProxy()
            self.proxy = temp_model.from_map(m['Proxy'])
        if m.get('K8sNewAPIsSupport') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfigK8sNewAPIsSupport()
            self.k_8s_new_apis_support = temp_model.from_map(m['K8sNewAPIsSupport'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMeshSpec(TeaModel):
    def __init__(self, network=None, load_balancer=None, mesh_config=None):
        self.network = network  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork
        self.load_balancer = load_balancer  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer
        self.mesh_config = mesh_config  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig

    def validate(self):
        if self.network:
            self.network.validate()
        if self.load_balancer:
            self.load_balancer.validate()
        if self.mesh_config:
            self.mesh_config.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMeshSpec, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.network is not None:
            result['Network'] = self.network.to_map()
        if self.load_balancer is not None:
            result['LoadBalancer'] = self.load_balancer.to_map()
        if self.mesh_config is not None:
            result['MeshConfig'] = self.mesh_config.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Network') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecNetwork()
            self.network = temp_model.from_map(m['Network'])
        if m.get('LoadBalancer') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecLoadBalancer()
            self.load_balancer = temp_model.from_map(m['LoadBalancer'])
        if m.get('MeshConfig') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpecMeshConfig()
            self.mesh_config = temp_model.from_map(m['MeshConfig'])
        return self


class DescribeServiceMeshDetailResponseBodyServiceMesh(TeaModel):
    def __init__(self, endpoints=None, service_mesh_info=None, spec=None, clusters=None):
        self.endpoints = endpoints  # type: DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints
        self.service_mesh_info = service_mesh_info  # type: DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo
        self.spec = spec  # type: DescribeServiceMeshDetailResponseBodyServiceMeshSpec
        self.clusters = clusters  # type: list[str]

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()
        if self.service_mesh_info:
            self.service_mesh_info.validate()
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBodyServiceMesh, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.service_mesh_info is not None:
            result['ServiceMeshInfo'] = self.service_mesh_info.to_map()
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Endpoints') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('ServiceMeshInfo') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshServiceMeshInfo()
            self.service_mesh_info = temp_model.from_map(m['ServiceMeshInfo'])
        if m.get('Spec') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMeshSpec()
            self.spec = temp_model.from_map(m['Spec'])
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        return self


class DescribeServiceMeshDetailResponseBody(TeaModel):
    def __init__(self, request_id=None, service_mesh=None):
        self.request_id = request_id  # type: str
        self.service_mesh = service_mesh  # type: DescribeServiceMeshDetailResponseBodyServiceMesh

    def validate(self):
        if self.service_mesh:
            self.service_mesh.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh is not None:
            result['ServiceMesh'] = self.service_mesh.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceMesh') is not None:
            temp_model = DescribeServiceMeshDetailResponseBodyServiceMesh()
            self.service_mesh = temp_model.from_map(m['ServiceMesh'])
        return self


class DescribeServiceMeshDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceMeshDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshDetailResponse, self).to_map()
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
            temp_model = DescribeServiceMeshDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeMeshVersionRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeMeshVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class UpgradeMeshVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeMeshVersionResponseBody, self).to_map()
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


class UpgradeMeshVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeMeshVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeMeshVersionResponse, self).to_map()
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
            temp_model = UpgradeMeshVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServiceMeshKubeconfigRequest(TeaModel):
    def __init__(self, service_mesh_id=None, private_ip_address=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshKubeconfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeServiceMeshKubeconfigResponseBody(TeaModel):
    def __init__(self, request_id=None, kubeconfig=None):
        self.request_id = request_id  # type: str
        self.kubeconfig = kubeconfig  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeServiceMeshKubeconfigResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.kubeconfig is not None:
            result['Kubeconfig'] = self.kubeconfig
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Kubeconfig') is not None:
            self.kubeconfig = m.get('Kubeconfig')
        return self


class DescribeServiceMeshKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeServiceMeshKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeServiceMeshKubeconfigResponse, self).to_map()
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
            temp_model = DescribeServiceMeshKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCaCertRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCaCertRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetCaCertResponseBody(TeaModel):
    def __init__(self, request_id=None, ca_cert=None):
        self.request_id = request_id  # type: str
        # base64 encode format
        self.ca_cert = ca_cert  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetCaCertResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ca_cert is not None:
            result['CaCert'] = self.ca_cert
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CaCert') is not None:
            self.ca_cert = m.get('CaCert')
        return self


class GetCaCertResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetCaCertResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetCaCertResponse, self).to_map()
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
            temp_model = GetCaCertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceMeshSlbRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceMeshSlbRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetServiceMeshSlbResponseBodyData(TeaModel):
    def __init__(self, status=None, server_health_status=None, load_balancer_id=None):
        self.status = status  # type: str
        self.server_health_status = server_health_status  # type: str
        self.load_balancer_id = load_balancer_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceMeshSlbResponseBodyData, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.server_health_status is not None:
            result['ServerHealthStatus'] = self.server_health_status
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ServerHealthStatus') is not None:
            self.server_health_status = m.get('ServerHealthStatus')
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')
        return self


class GetServiceMeshSlbResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: list[GetServiceMeshSlbResponseBodyData]

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetServiceMeshSlbResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = GetServiceMeshSlbResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class GetServiceMeshSlbResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceMeshSlbResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceMeshSlbResponse, self).to_map()
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
            temp_model = GetServiceMeshSlbResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceEndpointsRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, name=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace  # type: str
        self.name = name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisteredServiceEndpointsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetRegisteredServiceEndpointsResponseBodyServiceEndpoints(TeaModel):
    def __init__(self, address=None, cluster_id=None):
        self.address = address  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisteredServiceEndpointsResponseBodyServiceEndpoints, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['Address'] = self.address
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class GetRegisteredServiceEndpointsResponseBody(TeaModel):
    def __init__(self, service_endpoints=None, request_id=None):
        self.service_endpoints = service_endpoints  # type: list[GetRegisteredServiceEndpointsResponseBodyServiceEndpoints]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.service_endpoints:
            for k in self.service_endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetRegisteredServiceEndpointsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ServiceEndpoints'] = []
        if self.service_endpoints is not None:
            for k in self.service_endpoints:
                result['ServiceEndpoints'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.service_endpoints = []
        if m.get('ServiceEndpoints') is not None:
            for k in m.get('ServiceEndpoints'):
                temp_model = GetRegisteredServiceEndpointsResponseBodyServiceEndpoints()
                self.service_endpoints.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisteredServiceEndpointsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRegisteredServiceEndpointsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegisteredServiceEndpointsResponse, self).to_map()
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
            temp_model = GetRegisteredServiceEndpointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAutoInjectionLabelSyncStatusRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoInjectionLabelSyncStatusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetAutoInjectionLabelSyncStatusResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None):
        self.status = status  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetAutoInjectionLabelSyncStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetAutoInjectionLabelSyncStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetAutoInjectionLabelSyncStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetAutoInjectionLabelSyncStatusResponse, self).to_map()
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
            temp_model = GetAutoInjectionLabelSyncStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServiceNamespacesRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisteredServiceNamespacesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetRegisteredServiceNamespacesResponseBody(TeaModel):
    def __init__(self, namespaces=None, request_id=None):
        self.namespaces = namespaces  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisteredServiceNamespacesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisteredServiceNamespacesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRegisteredServiceNamespacesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegisteredServiceNamespacesResponse, self).to_map()
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
            temp_model = GetRegisteredServiceNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVSwitchesRequest(TeaModel):
    def __init__(self, region_id=None, vpc_id=None):
        self.region_id = region_id  # type: str
        self.vpc_id = vpc_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVSwitchesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeVSwitchesResponseBodyVSwitches(TeaModel):
    def __init__(self, vpc_id=None, v_switch_id=None, status=None, is_default=None, v_switch_name=None):
        self.vpc_id = vpc_id  # type: str
        self.v_switch_id = v_switch_id  # type: str
        self.status = status  # type: str
        self.is_default = is_default  # type: bool
        self.v_switch_name = v_switch_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVSwitchesResponseBodyVSwitches, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id
        if self.status is not None:
            result['Status'] = self.status
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')
        return self


class DescribeVSwitchesResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, next_token=None, max_results=None, v_switches=None):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        # VSwitches
        self.v_switches = v_switches  # type: list[DescribeVSwitchesResponseBodyVSwitches]

    def validate(self):
        if self.v_switches:
            for k in self.v_switches:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVSwitchesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['VSwitches'] = []
        if self.v_switches is not None:
            for k in self.v_switches:
                result['VSwitches'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.v_switches = []
        if m.get('VSwitches') is not None:
            for k in m.get('VSwitches'):
                temp_model = DescribeVSwitchesResponseBodyVSwitches()
                self.v_switches.append(temp_model.from_map(k))
        return self


class DescribeVSwitchesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVSwitchesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVSwitchesResponse, self).to_map()
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
            temp_model = DescribeVSwitchesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeVpcsRequest(TeaModel):
    def __init__(self, region_id=None):
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcsRequest, self).to_map()
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


class DescribeVpcsResponseBodyVpcs(TeaModel):
    def __init__(self, vpc_id=None, vpc_name=None, status=None, is_default=None):
        self.vpc_id = vpc_id  # type: str
        self.vpc_name = vpc_name  # type: str
        self.status = status  # type: str
        self.is_default = is_default  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeVpcsResponseBodyVpcs, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name
        if self.status is not None:
            result['Status'] = self.status
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        return self


class DescribeVpcsResponseBody(TeaModel):
    def __init__(self, total_count=None, request_id=None, next_token=None, max_results=None, vpcs=None):
        # TotalCount本次请求条件下的数据总量，此参数为可选参数，默认可不返回
        self.total_count = total_count  # type: int
        # Id of the request
        self.request_id = request_id  # type: str
        # 表示当前调用返回读取到的位置，空代表数据已经读取完毕
        self.next_token = next_token  # type: str
        # MaxResults本次请求所返回的最大记录条数
        self.max_results = max_results  # type: int
        # Vpcs
        self.vpcs = vpcs  # type: list[DescribeVpcsResponseBodyVpcs]

    def validate(self):
        if self.vpcs:
            for k in self.vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeVpcsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['Vpcs'] = []
        if self.vpcs is not None:
            for k in self.vpcs:
                result['Vpcs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.vpcs = []
        if m.get('Vpcs') is not None:
            for k in m.get('Vpcs'):
                temp_model = DescribeVpcsResponseBodyVpcs()
                self.vpcs.append(temp_model.from_map(k))
        return self


class DescribeVpcsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeVpcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeVpcsResponse, self).to_map()
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
            temp_model = DescribeVpcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveVmAppFromMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_name=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace  # type: str
        self.service_name = service_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveVmAppFromMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class RemoveVmAppFromMeshResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveVmAppFromMeshResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class RemoveVmAppFromMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveVmAppFromMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveVmAppFromMeshResponse, self).to_map()
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
            temp_model = RemoveVmAppFromMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterPrometheusRequest(TeaModel):
    def __init__(self, service_mesh_id=None, k_8s_cluster_id=None, k_8s_cluster_region_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str
        self.k_8s_cluster_region_id = k_8s_cluster_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterPrometheusRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        if self.k_8s_cluster_region_id is not None:
            result['K8sClusterRegionId'] = self.k_8s_cluster_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        if m.get('K8sClusterRegionId') is not None:
            self.k_8s_cluster_region_id = m.get('K8sClusterRegionId')
        return self


class DescribeClusterPrometheusResponseBody(TeaModel):
    def __init__(self, request_id=None, prometheus=None):
        self.request_id = request_id  # type: str
        self.prometheus = prometheus  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterPrometheusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.prometheus is not None:
            result['Prometheus'] = self.prometheus
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Prometheus') is not None:
            self.prometheus = m.get('Prometheus')
        return self


class DescribeClusterPrometheusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterPrometheusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterPrometheusResponse, self).to_map()
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
            temp_model = DescribeClusterPrometheusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIstioInjectionConfigRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, enable_istio_injection=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace  # type: str
        self.enable_istio_injection = enable_istio_injection  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIstioInjectionConfigRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.enable_istio_injection is not None:
            result['EnableIstioInjection'] = self.enable_istio_injection
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('EnableIstioInjection') is not None:
            self.enable_istio_injection = m.get('EnableIstioInjection')
        return self


class UpdateIstioInjectionConfigResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateIstioInjectionConfigResponseBody, self).to_map()
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


class UpdateIstioInjectionConfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateIstioInjectionConfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateIstioInjectionConfigResponse, self).to_map()
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
            temp_model = UpdateIstioInjectionConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmMetaRequest(TeaModel):
    def __init__(self, service_mesh_id=None, trust_domain=None, namespace=None, service_account=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.trust_domain = trust_domain  # type: str
        self.namespace = namespace  # type: str
        self.service_account = service_account  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVmMetaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.trust_domain is not None:
            result['TrustDomain'] = self.trust_domain
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('TrustDomain') is not None:
            self.trust_domain = m.get('TrustDomain')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')
        return self


class GetVmMetaResponseBodyVmMetaInfo(TeaModel):
    def __init__(self, hosts_content=None, token_content=None, envoy_env_content=None):
        self.hosts_content = hosts_content  # type: str
        self.token_content = token_content  # type: str
        self.envoy_env_content = envoy_env_content  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVmMetaResponseBodyVmMetaInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts_content is not None:
            result['HostsContent'] = self.hosts_content
        if self.token_content is not None:
            result['TokenContent'] = self.token_content
        if self.envoy_env_content is not None:
            result['EnvoyEnvContent'] = self.envoy_env_content
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostsContent') is not None:
            self.hosts_content = m.get('HostsContent')
        if m.get('TokenContent') is not None:
            self.token_content = m.get('TokenContent')
        if m.get('EnvoyEnvContent') is not None:
            self.envoy_env_content = m.get('EnvoyEnvContent')
        return self


class GetVmMetaResponseBody(TeaModel):
    def __init__(self, vm_meta_info=None, request_id=None):
        self.vm_meta_info = vm_meta_info  # type: GetVmMetaResponseBodyVmMetaInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.vm_meta_info:
            self.vm_meta_info.validate()

    def to_map(self):
        _map = super(GetVmMetaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vm_meta_info is not None:
            result['VmMetaInfo'] = self.vm_meta_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('VmMetaInfo') is not None:
            temp_model = GetVmMetaResponseBodyVmMetaInfo()
            self.vm_meta_info = temp_model.from_map(m['VmMetaInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetVmMetaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVmMetaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVmMetaResponse, self).to_map()
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
            temp_model = GetVmMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeUpgradeVersionRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUpgradeVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeUpgradeVersionResponseBodyVersion(TeaModel):
    def __init__(self, kubernetes_version=None, istio_operator_version=None, istio_version=None):
        self.kubernetes_version = kubernetes_version  # type: str
        self.istio_operator_version = istio_operator_version  # type: str
        self.istio_version = istio_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeUpgradeVersionResponseBodyVersion, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        if self.istio_operator_version is not None:
            result['IstioOperatorVersion'] = self.istio_operator_version
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        if m.get('IstioOperatorVersion') is not None:
            self.istio_operator_version = m.get('IstioOperatorVersion')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        return self


class DescribeUpgradeVersionResponseBody(TeaModel):
    def __init__(self, request_id=None, version=None):
        self.request_id = request_id  # type: str
        self.version = version  # type: DescribeUpgradeVersionResponseBodyVersion

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super(DescribeUpgradeVersionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.version is not None:
            result['Version'] = self.version.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Version') is not None:
            temp_model = DescribeUpgradeVersionResponseBodyVersion()
            self.version = temp_model.from_map(m['Version'])
        return self


class DescribeUpgradeVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeUpgradeVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeUpgradeVersionResponse, self).to_map()
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
            temp_model = DescribeUpgradeVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersInServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersInServiceMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards(TeaModel):
    def __init__(self, url=None, title=None):
        self.url = url  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeClustersInServiceMeshResponseBodyClusters(TeaModel):
    def __init__(self, sg_id=None, vpc_id=None, creation_time=None, update_time=None, error_message=None, state=None,
                 access_log_dashboards=None, region_id=None, cluster_domain=None, version=None, cluster_type=None, name=None,
                 cluster_id=None):
        self.sg_id = sg_id  # type: str
        self.vpc_id = vpc_id  # type: str
        self.creation_time = creation_time  # type: str
        self.update_time = update_time  # type: str
        self.error_message = error_message  # type: str
        self.state = state  # type: str
        self.access_log_dashboards = access_log_dashboards  # type: list[DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards]
        self.region_id = region_id  # type: str
        self.cluster_domain = cluster_domain  # type: str
        self.version = version  # type: str
        self.cluster_type = cluster_type  # type: str
        self.name = name  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        if self.access_log_dashboards:
            for k in self.access_log_dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersInServiceMeshResponseBodyClusters, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sg_id is not None:
            result['SgId'] = self.sg_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.state is not None:
            result['State'] = self.state
        result['AccessLogDashboards'] = []
        if self.access_log_dashboards is not None:
            for k in self.access_log_dashboards:
                result['AccessLogDashboards'].append(k.to_map() if k else None)
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.version is not None:
            result['Version'] = self.version
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.name is not None:
            result['Name'] = self.name
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('SgId') is not None:
            self.sg_id = m.get('SgId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('State') is not None:
            self.state = m.get('State')
        self.access_log_dashboards = []
        if m.get('AccessLogDashboards') is not None:
            for k in m.get('AccessLogDashboards'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClustersAccessLogDashboards()
                self.access_log_dashboards.append(temp_model.from_map(k))
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClustersInServiceMeshResponseBody(TeaModel):
    def __init__(self, request_id=None, clusters=None):
        self.request_id = request_id  # type: str
        self.clusters = clusters  # type: list[DescribeClustersInServiceMeshResponseBodyClusters]

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClustersInServiceMeshResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = DescribeClustersInServiceMeshResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        return self


class DescribeClustersInServiceMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClustersInServiceMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClustersInServiceMeshResponse, self).to_map()
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
            temp_model = DescribeClustersInServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBuiltinEnvoyFilterCatalogRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBuiltinEnvoyFilterCatalogRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetBuiltinEnvoyFilterCatalogResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBuiltinEnvoyFilterCatalogResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetBuiltinEnvoyFilterCatalogResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBuiltinEnvoyFilterCatalogResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBuiltinEnvoyFilterCatalogResponse, self).to_map()
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
            temp_model = GetBuiltinEnvoyFilterCatalogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterGrafanaRequest(TeaModel):
    def __init__(self, service_mesh_id=None, k_8s_cluster_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.k_8s_cluster_id = k_8s_cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterGrafanaRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.k_8s_cluster_id is not None:
            result['K8sClusterId'] = self.k_8s_cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('K8sClusterId') is not None:
            self.k_8s_cluster_id = m.get('K8sClusterId')
        return self


class DescribeClusterGrafanaResponseBodyDashboards(TeaModel):
    def __init__(self, url=None, title=None):
        self.url = url  # type: str
        self.title = title  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeClusterGrafanaResponseBodyDashboards, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class DescribeClusterGrafanaResponseBody(TeaModel):
    def __init__(self, request_id=None, dashboards=None):
        self.request_id = request_id  # type: str
        self.dashboards = dashboards  # type: list[DescribeClusterGrafanaResponseBodyDashboards]

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeClusterGrafanaResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['Dashboards'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k in m.get('Dashboards'):
                temp_model = DescribeClusterGrafanaResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k))
        return self


class DescribeClusterGrafanaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeClusterGrafanaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeClusterGrafanaResponse, self).to_map()
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
            temp_model = DescribeClusterGrafanaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnosisRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnosisRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetDiagnosisResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, run_at=None, result=None):
        self.status = status  # type: str
        self.request_id = request_id  # type: str
        self.run_at = run_at  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetDiagnosisResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.run_at is not None:
            result['RunAt'] = self.run_at
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RunAt') is not None:
            self.run_at = m.get('RunAt')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetDiagnosisResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetDiagnosisResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetDiagnosisResponse, self).to_map()
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
            temp_model = GetDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegisteredServicesRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisteredServicesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetRegisteredServicesResponseBody(TeaModel):
    def __init__(self, services=None, request_id=None):
        self.services = services  # type: list[str]
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetRegisteredServicesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.services is not None:
            result['Services'] = self.services
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Services') is not None:
            self.services = m.get('Services')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRegisteredServicesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetRegisteredServicesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetRegisteredServicesResponse, self).to_map()
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
            temp_model = GetRegisteredServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeCensRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class DescribeCensResponseBody(TeaModel):
    def __init__(self, request_id=None, clusters=None):
        self.request_id = request_id  # type: str
        self.clusters = clusters  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeCensResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.clusters is not None:
            result['Clusters'] = self.clusters
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Clusters') is not None:
            self.clusters = m.get('Clusters')
        return self


class DescribeCensResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeCensResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeCensResponse, self).to_map()
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
            temp_model = DescribeCensResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, force=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class DeleteServiceMeshResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteServiceMeshResponseBody, self).to_map()
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


class DeleteServiceMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteServiceMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteServiceMeshResponse, self).to_map()
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
            temp_model = DeleteServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSaTokenRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_account_name=None, need_refresh=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace  # type: str
        self.service_account_name = service_account_name  # type: str
        self.need_refresh = need_refresh  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSaTokenRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_account_name is not None:
            result['ServiceAccountName'] = self.service_account_name
        if self.need_refresh is not None:
            result['NeedRefresh'] = self.need_refresh
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceAccountName') is not None:
            self.service_account_name = m.get('ServiceAccountName')
        if m.get('NeedRefresh') is not None:
            self.need_refresh = m.get('NeedRefresh')
        return self


class GetSaTokenResponseBody(TeaModel):
    def __init__(self, request_id=None, token=None):
        self.request_id = request_id  # type: str
        # Token of service account
        self.token = token  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetSaTokenResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class GetSaTokenResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetSaTokenResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetSaTokenResponse, self).to_map()
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
            temp_model = GetSaTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVmAppMeshInfoRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVmAppMeshInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetVmAppMeshInfoResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetVmAppMeshInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class GetVmAppMeshInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetVmAppMeshInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetVmAppMeshInfoResponse, self).to_map()
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
            temp_model = GetVmAppMeshInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveClusterFromServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, cluster_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClusterFromServiceMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class RemoveClusterFromServiceMeshResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveClusterFromServiceMeshResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class RemoveClusterFromServiceMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveClusterFromServiceMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveClusterFromServiceMeshResponse, self).to_map()
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
            temp_model = RemoveClusterFromServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, request_id=None, business_locations=None):
        self.request_id = request_id  # type: str
        self.business_locations = business_locations  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.business_locations is not None:
            result['BusinessLocations'] = self.business_locations
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BusinessLocations') is not None:
            self.business_locations = m.get('BusinessLocations')
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


class SetServiceRegistrySourceRequest(TeaModel):
    def __init__(self, service_mesh_id=None, config=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.config = config  # type: dict[str, any]

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetServiceRegistrySourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.config is not None:
            result['Config'] = self.config
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Config') is not None:
            self.config = m.get('Config')
        return self


class SetServiceRegistrySourceShrinkRequest(TeaModel):
    def __init__(self, service_mesh_id=None, config_shrink=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.config_shrink = config_shrink  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetServiceRegistrySourceShrinkRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.config_shrink is not None:
            result['Config'] = self.config_shrink
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Config') is not None:
            self.config_shrink = m.get('Config')
        return self


class SetServiceRegistrySourceResponseBody(TeaModel):
    def __init__(self, request_id=None, result=None):
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(SetServiceRegistrySourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class SetServiceRegistrySourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: SetServiceRegistrySourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(SetServiceRegistrySourceResponse, self).to_map()
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
            temp_model = SetServiceRegistrySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddClusterIntoServiceMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, cluster_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.cluster_id = cluster_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClusterIntoServiceMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class AddClusterIntoServiceMeshResponseBody(TeaModel):
    def __init__(self, message=None, request_id=None, code=None):
        self.message = message  # type: str
        self.request_id = request_id  # type: str
        self.code = code  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddClusterIntoServiceMeshResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class AddClusterIntoServiceMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddClusterIntoServiceMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddClusterIntoServiceMeshResponse, self).to_map()
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
            temp_model = AddClusterIntoServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(self, service_mesh_id=None, id=None, name=None, parameters=None, istio_version=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.parameters = parameters  # type: str
        self.istio_version = istio_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBuiltinEnvoyFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        return self


class AddBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddBuiltinEnvoyFilterResponseBody, self).to_map()
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


class AddBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddBuiltinEnvoyFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddBuiltinEnvoyFilterResponse, self).to_map()
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
            temp_model = AddBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEcsListRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEcsListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetEcsListResponseBodyEcsInstances(TeaModel):
    def __init__(self, instance_id=None, host_name=None, ip_address=None, status=None, has_tag=None,
                 security_group_ids=None):
        self.instance_id = instance_id  # type: str
        self.host_name = host_name  # type: str
        self.ip_address = ip_address  # type: str
        self.status = status  # type: str
        self.has_tag = has_tag  # type: bool
        self.security_group_ids = security_group_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetEcsListResponseBodyEcsInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.status is not None:
            result['Status'] = self.status
        if self.has_tag is not None:
            result['HasTag'] = self.has_tag
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('HasTag') is not None:
            self.has_tag = m.get('HasTag')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        return self


class GetEcsListResponseBody(TeaModel):
    def __init__(self, ecs_instances=None, request_id=None):
        self.ecs_instances = ecs_instances  # type: list[GetEcsListResponseBodyEcsInstances]
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ecs_instances:
            for k in self.ecs_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetEcsListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['EcsInstances'] = []
        if self.ecs_instances is not None:
            for k in self.ecs_instances:
                result['EcsInstances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.ecs_instances = []
        if m.get('EcsInstances') is not None:
            for k in m.get('EcsInstances'):
                temp_model = GetEcsListResponseBodyEcsInstances()
                self.ecs_instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetEcsListResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetEcsListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetEcsListResponse, self).to_map()
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
            temp_model = GetEcsListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMeshFeatureRequest(TeaModel):
    def __init__(self, service_mesh_id=None, tracing=None, trace_sampling=None, locality_load_balancing=None,
                 telemetry=None, open_agent_policy=None, opalog_level=None, oparequest_cpu=None, oparequest_memory=None,
                 opalimit_cpu=None, opalimit_memory=None, enable_audit=None, audit_project=None, cluster_domain=None,
                 customized_zipkin=None, outbound_traffic_policy=None, proxy_request_cpu=None, proxy_request_memory=None,
                 proxy_limit_cpu=None, proxy_limit_memory=None, include_ipranges=None, exclude_ipranges=None,
                 exclude_outbound_ports=None, exclude_inbound_ports=None, enable_namespaces_by_default=None,
                 auto_injection_policy_enabled=None, sidecar_injector_request_cpu=None, sidecar_injector_request_memory=None,
                 sidecar_injector_limit_cpu=None, sidecar_injector_limit_memory=None, sidecar_injector_webhook_as_yaml=None,
                 cni_enabled=None, cni_exclude_namespaces=None, opa_enabled=None, http_10enabled=None, kiali_enabled=None,
                 customized_prometheus=None, prometheus_url=None, access_log_enabled=None, mseenabled=None, redis_filter_enabled=None,
                 mysql_filter_enabled=None, thrift_filter_enabled=None, web_assembly_filter_enabled=None, dnsproxying_enabled=None,
                 dubbo_filter_enabled=None, filter_gateway_cluster_config=None, enable_sdsserver=None, access_log_service_enabled=None,
                 access_log_service_host=None, access_log_service_port=None, gateway_apienabled=None, config_source_enabled=None,
                 config_source_nacos_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.tracing = tracing  # type: bool
        self.trace_sampling = trace_sampling  # type: float
        self.locality_load_balancing = locality_load_balancing  # type: bool
        self.telemetry = telemetry  # type: bool
        self.open_agent_policy = open_agent_policy  # type: bool
        self.opalog_level = opalog_level  # type: str
        self.oparequest_cpu = oparequest_cpu  # type: str
        self.oparequest_memory = oparequest_memory  # type: str
        self.opalimit_cpu = opalimit_cpu  # type: str
        self.opalimit_memory = opalimit_memory  # type: str
        self.enable_audit = enable_audit  # type: bool
        self.audit_project = audit_project  # type: str
        self.cluster_domain = cluster_domain  # type: str
        self.customized_zipkin = customized_zipkin  # type: bool
        self.outbound_traffic_policy = outbound_traffic_policy  # type: str
        self.proxy_request_cpu = proxy_request_cpu  # type: str
        self.proxy_request_memory = proxy_request_memory  # type: str
        self.proxy_limit_cpu = proxy_limit_cpu  # type: str
        self.proxy_limit_memory = proxy_limit_memory  # type: str
        self.include_ipranges = include_ipranges  # type: str
        self.exclude_ipranges = exclude_ipranges  # type: str
        self.exclude_outbound_ports = exclude_outbound_ports  # type: str
        self.exclude_inbound_ports = exclude_inbound_ports  # type: str
        self.enable_namespaces_by_default = enable_namespaces_by_default  # type: bool
        self.auto_injection_policy_enabled = auto_injection_policy_enabled  # type: bool
        self.sidecar_injector_request_cpu = sidecar_injector_request_cpu  # type: str
        self.sidecar_injector_request_memory = sidecar_injector_request_memory  # type: str
        self.sidecar_injector_limit_cpu = sidecar_injector_limit_cpu  # type: str
        self.sidecar_injector_limit_memory = sidecar_injector_limit_memory  # type: str
        self.sidecar_injector_webhook_as_yaml = sidecar_injector_webhook_as_yaml  # type: str
        self.cni_enabled = cni_enabled  # type: bool
        self.cni_exclude_namespaces = cni_exclude_namespaces  # type: str
        self.opa_enabled = opa_enabled  # type: bool
        self.http_10enabled = http_10enabled  # type: bool
        self.kiali_enabled = kiali_enabled  # type: bool
        self.customized_prometheus = customized_prometheus  # type: bool
        self.prometheus_url = prometheus_url  # type: str
        self.access_log_enabled = access_log_enabled  # type: bool
        self.mseenabled = mseenabled  # type: bool
        self.redis_filter_enabled = redis_filter_enabled  # type: bool
        self.mysql_filter_enabled = mysql_filter_enabled  # type: bool
        self.thrift_filter_enabled = thrift_filter_enabled  # type: bool
        self.web_assembly_filter_enabled = web_assembly_filter_enabled  # type: bool
        self.dnsproxying_enabled = dnsproxying_enabled  # type: bool
        self.dubbo_filter_enabled = dubbo_filter_enabled  # type: bool
        self.filter_gateway_cluster_config = filter_gateway_cluster_config  # type: bool
        self.enable_sdsserver = enable_sdsserver  # type: bool
        self.access_log_service_enabled = access_log_service_enabled  # type: bool
        self.access_log_service_host = access_log_service_host  # type: str
        self.access_log_service_port = access_log_service_port  # type: int
        self.gateway_apienabled = gateway_apienabled  # type: bool
        self.config_source_enabled = config_source_enabled  # type: bool
        self.config_source_nacos_id = config_source_nacos_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMeshFeatureRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.cluster_domain is not None:
            result['ClusterDomain'] = self.cluster_domain
        if self.customized_zipkin is not None:
            result['CustomizedZipkin'] = self.customized_zipkin
        if self.outbound_traffic_policy is not None:
            result['OutboundTrafficPolicy'] = self.outbound_traffic_policy
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.enable_namespaces_by_default is not None:
            result['EnableNamespacesByDefault'] = self.enable_namespaces_by_default
        if self.auto_injection_policy_enabled is not None:
            result['AutoInjectionPolicyEnabled'] = self.auto_injection_policy_enabled
        if self.sidecar_injector_request_cpu is not None:
            result['SidecarInjectorRequestCPU'] = self.sidecar_injector_request_cpu
        if self.sidecar_injector_request_memory is not None:
            result['SidecarInjectorRequestMemory'] = self.sidecar_injector_request_memory
        if self.sidecar_injector_limit_cpu is not None:
            result['SidecarInjectorLimitCPU'] = self.sidecar_injector_limit_cpu
        if self.sidecar_injector_limit_memory is not None:
            result['SidecarInjectorLimitMemory'] = self.sidecar_injector_limit_memory
        if self.sidecar_injector_webhook_as_yaml is not None:
            result['SidecarInjectorWebhookAsYaml'] = self.sidecar_injector_webhook_as_yaml
        if self.cni_enabled is not None:
            result['CniEnabled'] = self.cni_enabled
        if self.cni_exclude_namespaces is not None:
            result['CniExcludeNamespaces'] = self.cni_exclude_namespaces
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.http_10enabled is not None:
            result['Http10Enabled'] = self.http_10enabled
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        if self.config_source_enabled is not None:
            result['ConfigSourceEnabled'] = self.config_source_enabled
        if self.config_source_nacos_id is not None:
            result['ConfigSourceNacosID'] = self.config_source_nacos_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('ClusterDomain') is not None:
            self.cluster_domain = m.get('ClusterDomain')
        if m.get('CustomizedZipkin') is not None:
            self.customized_zipkin = m.get('CustomizedZipkin')
        if m.get('OutboundTrafficPolicy') is not None:
            self.outbound_traffic_policy = m.get('OutboundTrafficPolicy')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('EnableNamespacesByDefault') is not None:
            self.enable_namespaces_by_default = m.get('EnableNamespacesByDefault')
        if m.get('AutoInjectionPolicyEnabled') is not None:
            self.auto_injection_policy_enabled = m.get('AutoInjectionPolicyEnabled')
        if m.get('SidecarInjectorRequestCPU') is not None:
            self.sidecar_injector_request_cpu = m.get('SidecarInjectorRequestCPU')
        if m.get('SidecarInjectorRequestMemory') is not None:
            self.sidecar_injector_request_memory = m.get('SidecarInjectorRequestMemory')
        if m.get('SidecarInjectorLimitCPU') is not None:
            self.sidecar_injector_limit_cpu = m.get('SidecarInjectorLimitCPU')
        if m.get('SidecarInjectorLimitMemory') is not None:
            self.sidecar_injector_limit_memory = m.get('SidecarInjectorLimitMemory')
        if m.get('SidecarInjectorWebhookAsYaml') is not None:
            self.sidecar_injector_webhook_as_yaml = m.get('SidecarInjectorWebhookAsYaml')
        if m.get('CniEnabled') is not None:
            self.cni_enabled = m.get('CniEnabled')
        if m.get('CniExcludeNamespaces') is not None:
            self.cni_exclude_namespaces = m.get('CniExcludeNamespaces')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('Http10Enabled') is not None:
            self.http_10enabled = m.get('Http10Enabled')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        if m.get('ConfigSourceEnabled') is not None:
            self.config_source_enabled = m.get('ConfigSourceEnabled')
        if m.get('ConfigSourceNacosID') is not None:
            self.config_source_nacos_id = m.get('ConfigSourceNacosID')
        return self


class UpdateMeshFeatureResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateMeshFeatureResponseBody, self).to_map()
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


class UpdateMeshFeatureResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpdateMeshFeatureResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateMeshFeatureResponse, self).to_map()
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
            temp_model = UpdateMeshFeatureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddVmAppToMeshRequest(TeaModel):
    def __init__(self, service_mesh_id=None, namespace=None, service_name=None, ips=None, ports=None, labels=None,
                 annotations=None, service_account=None, force=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.namespace = namespace  # type: str
        self.service_name = service_name  # type: str
        self.ips = ips  # type: str
        self.ports = ports  # type: str
        self.labels = labels  # type: str
        self.annotations = annotations  # type: str
        self.service_account = service_account  # type: str
        self.force = force  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVmAppToMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.ips is not None:
            result['Ips'] = self.ips
        if self.ports is not None:
            result['Ports'] = self.ports
        if self.labels is not None:
            result['Labels'] = self.labels
        if self.annotations is not None:
            result['Annotations'] = self.annotations
        if self.service_account is not None:
            result['ServiceAccount'] = self.service_account
        if self.force is not None:
            result['Force'] = self.force
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Ips') is not None:
            self.ips = m.get('Ips')
        if m.get('Ports') is not None:
            self.ports = m.get('Ports')
        if m.get('Labels') is not None:
            self.labels = m.get('Labels')
        if m.get('Annotations') is not None:
            self.annotations = m.get('Annotations')
        if m.get('ServiceAccount') is not None:
            self.service_account = m.get('ServiceAccount')
        if m.get('Force') is not None:
            self.force = m.get('Force')
        return self


class AddVmAppToMeshResponseBody(TeaModel):
    def __init__(self, request_id=None, data=None):
        self.request_id = request_id  # type: str
        self.data = data  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddVmAppToMeshResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class AddVmAppToMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddVmAppToMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddVmAppToMeshResponse, self).to_map()
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
            temp_model = AddVmAppToMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceMeshRequest(TeaModel):
    def __init__(self, region_id=None, istio_version=None, vpc_id=None, api_server_public_eip=None,
                 pilot_public_eip=None, tracing=None, name=None, v_switches=None, trace_sampling=None, locality_load_balancing=None,
                 telemetry=None, open_agent_policy=None, opalog_level=None, oparequest_cpu=None, oparequest_memory=None,
                 opalimit_cpu=None, opalimit_memory=None, enable_audit=None, audit_project=None, proxy_request_cpu=None,
                 proxy_request_memory=None, proxy_limit_cpu=None, proxy_limit_memory=None, include_ipranges=None, exclude_ipranges=None,
                 exclude_outbound_ports=None, exclude_inbound_ports=None, opa_enabled=None, kiali_enabled=None, access_log_enabled=None,
                 customized_prometheus=None, prometheus_url=None, redis_filter_enabled=None, mysql_filter_enabled=None,
                 thrift_filter_enabled=None, web_assembly_filter_enabled=None, mseenabled=None, dnsproxying_enabled=None, edition=None,
                 config_source_enabled=None, config_source_nacos_id=None, dubbo_filter_enabled=None, filter_gateway_cluster_config=None,
                 enable_sdsserver=None, access_log_service_enabled=None, access_log_service_host=None,
                 access_log_service_port=None, gateway_apienabled=None):
        self.region_id = region_id  # type: str
        self.istio_version = istio_version  # type: str
        self.vpc_id = vpc_id  # type: str
        self.api_server_public_eip = api_server_public_eip  # type: bool
        self.pilot_public_eip = pilot_public_eip  # type: bool
        self.tracing = tracing  # type: bool
        self.name = name  # type: str
        self.v_switches = v_switches  # type: str
        self.trace_sampling = trace_sampling  # type: float
        self.locality_load_balancing = locality_load_balancing  # type: bool
        self.telemetry = telemetry  # type: bool
        self.open_agent_policy = open_agent_policy  # type: bool
        self.opalog_level = opalog_level  # type: str
        self.oparequest_cpu = oparequest_cpu  # type: str
        self.oparequest_memory = oparequest_memory  # type: str
        self.opalimit_cpu = opalimit_cpu  # type: str
        self.opalimit_memory = opalimit_memory  # type: str
        self.enable_audit = enable_audit  # type: bool
        self.audit_project = audit_project  # type: str
        self.proxy_request_cpu = proxy_request_cpu  # type: str
        self.proxy_request_memory = proxy_request_memory  # type: str
        self.proxy_limit_cpu = proxy_limit_cpu  # type: str
        self.proxy_limit_memory = proxy_limit_memory  # type: str
        self.include_ipranges = include_ipranges  # type: str
        self.exclude_ipranges = exclude_ipranges  # type: str
        self.exclude_outbound_ports = exclude_outbound_ports  # type: str
        self.exclude_inbound_ports = exclude_inbound_ports  # type: str
        self.opa_enabled = opa_enabled  # type: bool
        self.kiali_enabled = kiali_enabled  # type: bool
        self.access_log_enabled = access_log_enabled  # type: bool
        self.customized_prometheus = customized_prometheus  # type: bool
        self.prometheus_url = prometheus_url  # type: str
        self.redis_filter_enabled = redis_filter_enabled  # type: bool
        self.mysql_filter_enabled = mysql_filter_enabled  # type: bool
        self.thrift_filter_enabled = thrift_filter_enabled  # type: bool
        self.web_assembly_filter_enabled = web_assembly_filter_enabled  # type: bool
        self.mseenabled = mseenabled  # type: bool
        self.dnsproxying_enabled = dnsproxying_enabled  # type: bool
        self.edition = edition  # type: str
        self.config_source_enabled = config_source_enabled  # type: bool
        self.config_source_nacos_id = config_source_nacos_id  # type: str
        self.dubbo_filter_enabled = dubbo_filter_enabled  # type: bool
        self.filter_gateway_cluster_config = filter_gateway_cluster_config  # type: bool
        self.enable_sdsserver = enable_sdsserver  # type: bool
        self.access_log_service_enabled = access_log_service_enabled  # type: bool
        self.access_log_service_host = access_log_service_host  # type: str
        self.access_log_service_port = access_log_service_port  # type: int
        self.gateway_apienabled = gateway_apienabled  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceMeshRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.api_server_public_eip is not None:
            result['ApiServerPublicEip'] = self.api_server_public_eip
        if self.pilot_public_eip is not None:
            result['PilotPublicEip'] = self.pilot_public_eip
        if self.tracing is not None:
            result['Tracing'] = self.tracing
        if self.name is not None:
            result['Name'] = self.name
        if self.v_switches is not None:
            result['VSwitches'] = self.v_switches
        if self.trace_sampling is not None:
            result['TraceSampling'] = self.trace_sampling
        if self.locality_load_balancing is not None:
            result['LocalityLoadBalancing'] = self.locality_load_balancing
        if self.telemetry is not None:
            result['Telemetry'] = self.telemetry
        if self.open_agent_policy is not None:
            result['OpenAgentPolicy'] = self.open_agent_policy
        if self.opalog_level is not None:
            result['OPALogLevel'] = self.opalog_level
        if self.oparequest_cpu is not None:
            result['OPARequestCPU'] = self.oparequest_cpu
        if self.oparequest_memory is not None:
            result['OPARequestMemory'] = self.oparequest_memory
        if self.opalimit_cpu is not None:
            result['OPALimitCPU'] = self.opalimit_cpu
        if self.opalimit_memory is not None:
            result['OPALimitMemory'] = self.opalimit_memory
        if self.enable_audit is not None:
            result['EnableAudit'] = self.enable_audit
        if self.audit_project is not None:
            result['AuditProject'] = self.audit_project
        if self.proxy_request_cpu is not None:
            result['ProxyRequestCPU'] = self.proxy_request_cpu
        if self.proxy_request_memory is not None:
            result['ProxyRequestMemory'] = self.proxy_request_memory
        if self.proxy_limit_cpu is not None:
            result['ProxyLimitCPU'] = self.proxy_limit_cpu
        if self.proxy_limit_memory is not None:
            result['ProxyLimitMemory'] = self.proxy_limit_memory
        if self.include_ipranges is not None:
            result['IncludeIPRanges'] = self.include_ipranges
        if self.exclude_ipranges is not None:
            result['ExcludeIPRanges'] = self.exclude_ipranges
        if self.exclude_outbound_ports is not None:
            result['ExcludeOutboundPorts'] = self.exclude_outbound_ports
        if self.exclude_inbound_ports is not None:
            result['ExcludeInboundPorts'] = self.exclude_inbound_ports
        if self.opa_enabled is not None:
            result['OpaEnabled'] = self.opa_enabled
        if self.kiali_enabled is not None:
            result['KialiEnabled'] = self.kiali_enabled
        if self.access_log_enabled is not None:
            result['AccessLogEnabled'] = self.access_log_enabled
        if self.customized_prometheus is not None:
            result['CustomizedPrometheus'] = self.customized_prometheus
        if self.prometheus_url is not None:
            result['PrometheusUrl'] = self.prometheus_url
        if self.redis_filter_enabled is not None:
            result['RedisFilterEnabled'] = self.redis_filter_enabled
        if self.mysql_filter_enabled is not None:
            result['MysqlFilterEnabled'] = self.mysql_filter_enabled
        if self.thrift_filter_enabled is not None:
            result['ThriftFilterEnabled'] = self.thrift_filter_enabled
        if self.web_assembly_filter_enabled is not None:
            result['WebAssemblyFilterEnabled'] = self.web_assembly_filter_enabled
        if self.mseenabled is not None:
            result['MSEEnabled'] = self.mseenabled
        if self.dnsproxying_enabled is not None:
            result['DNSProxyingEnabled'] = self.dnsproxying_enabled
        if self.edition is not None:
            result['Edition'] = self.edition
        if self.config_source_enabled is not None:
            result['ConfigSourceEnabled'] = self.config_source_enabled
        if self.config_source_nacos_id is not None:
            result['ConfigSourceNacosID'] = self.config_source_nacos_id
        if self.dubbo_filter_enabled is not None:
            result['DubboFilterEnabled'] = self.dubbo_filter_enabled
        if self.filter_gateway_cluster_config is not None:
            result['FilterGatewayClusterConfig'] = self.filter_gateway_cluster_config
        if self.enable_sdsserver is not None:
            result['EnableSDSServer'] = self.enable_sdsserver
        if self.access_log_service_enabled is not None:
            result['AccessLogServiceEnabled'] = self.access_log_service_enabled
        if self.access_log_service_host is not None:
            result['AccessLogServiceHost'] = self.access_log_service_host
        if self.access_log_service_port is not None:
            result['AccessLogServicePort'] = self.access_log_service_port
        if self.gateway_apienabled is not None:
            result['GatewayAPIEnabled'] = self.gateway_apienabled
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('ApiServerPublicEip') is not None:
            self.api_server_public_eip = m.get('ApiServerPublicEip')
        if m.get('PilotPublicEip') is not None:
            self.pilot_public_eip = m.get('PilotPublicEip')
        if m.get('Tracing') is not None:
            self.tracing = m.get('Tracing')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('VSwitches') is not None:
            self.v_switches = m.get('VSwitches')
        if m.get('TraceSampling') is not None:
            self.trace_sampling = m.get('TraceSampling')
        if m.get('LocalityLoadBalancing') is not None:
            self.locality_load_balancing = m.get('LocalityLoadBalancing')
        if m.get('Telemetry') is not None:
            self.telemetry = m.get('Telemetry')
        if m.get('OpenAgentPolicy') is not None:
            self.open_agent_policy = m.get('OpenAgentPolicy')
        if m.get('OPALogLevel') is not None:
            self.opalog_level = m.get('OPALogLevel')
        if m.get('OPARequestCPU') is not None:
            self.oparequest_cpu = m.get('OPARequestCPU')
        if m.get('OPARequestMemory') is not None:
            self.oparequest_memory = m.get('OPARequestMemory')
        if m.get('OPALimitCPU') is not None:
            self.opalimit_cpu = m.get('OPALimitCPU')
        if m.get('OPALimitMemory') is not None:
            self.opalimit_memory = m.get('OPALimitMemory')
        if m.get('EnableAudit') is not None:
            self.enable_audit = m.get('EnableAudit')
        if m.get('AuditProject') is not None:
            self.audit_project = m.get('AuditProject')
        if m.get('ProxyRequestCPU') is not None:
            self.proxy_request_cpu = m.get('ProxyRequestCPU')
        if m.get('ProxyRequestMemory') is not None:
            self.proxy_request_memory = m.get('ProxyRequestMemory')
        if m.get('ProxyLimitCPU') is not None:
            self.proxy_limit_cpu = m.get('ProxyLimitCPU')
        if m.get('ProxyLimitMemory') is not None:
            self.proxy_limit_memory = m.get('ProxyLimitMemory')
        if m.get('IncludeIPRanges') is not None:
            self.include_ipranges = m.get('IncludeIPRanges')
        if m.get('ExcludeIPRanges') is not None:
            self.exclude_ipranges = m.get('ExcludeIPRanges')
        if m.get('ExcludeOutboundPorts') is not None:
            self.exclude_outbound_ports = m.get('ExcludeOutboundPorts')
        if m.get('ExcludeInboundPorts') is not None:
            self.exclude_inbound_ports = m.get('ExcludeInboundPorts')
        if m.get('OpaEnabled') is not None:
            self.opa_enabled = m.get('OpaEnabled')
        if m.get('KialiEnabled') is not None:
            self.kiali_enabled = m.get('KialiEnabled')
        if m.get('AccessLogEnabled') is not None:
            self.access_log_enabled = m.get('AccessLogEnabled')
        if m.get('CustomizedPrometheus') is not None:
            self.customized_prometheus = m.get('CustomizedPrometheus')
        if m.get('PrometheusUrl') is not None:
            self.prometheus_url = m.get('PrometheusUrl')
        if m.get('RedisFilterEnabled') is not None:
            self.redis_filter_enabled = m.get('RedisFilterEnabled')
        if m.get('MysqlFilterEnabled') is not None:
            self.mysql_filter_enabled = m.get('MysqlFilterEnabled')
        if m.get('ThriftFilterEnabled') is not None:
            self.thrift_filter_enabled = m.get('ThriftFilterEnabled')
        if m.get('WebAssemblyFilterEnabled') is not None:
            self.web_assembly_filter_enabled = m.get('WebAssemblyFilterEnabled')
        if m.get('MSEEnabled') is not None:
            self.mseenabled = m.get('MSEEnabled')
        if m.get('DNSProxyingEnabled') is not None:
            self.dnsproxying_enabled = m.get('DNSProxyingEnabled')
        if m.get('Edition') is not None:
            self.edition = m.get('Edition')
        if m.get('ConfigSourceEnabled') is not None:
            self.config_source_enabled = m.get('ConfigSourceEnabled')
        if m.get('ConfigSourceNacosID') is not None:
            self.config_source_nacos_id = m.get('ConfigSourceNacosID')
        if m.get('DubboFilterEnabled') is not None:
            self.dubbo_filter_enabled = m.get('DubboFilterEnabled')
        if m.get('FilterGatewayClusterConfig') is not None:
            self.filter_gateway_cluster_config = m.get('FilterGatewayClusterConfig')
        if m.get('EnableSDSServer') is not None:
            self.enable_sdsserver = m.get('EnableSDSServer')
        if m.get('AccessLogServiceEnabled') is not None:
            self.access_log_service_enabled = m.get('AccessLogServiceEnabled')
        if m.get('AccessLogServiceHost') is not None:
            self.access_log_service_host = m.get('AccessLogServiceHost')
        if m.get('AccessLogServicePort') is not None:
            self.access_log_service_port = m.get('AccessLogServicePort')
        if m.get('GatewayAPIEnabled') is not None:
            self.gateway_apienabled = m.get('GatewayAPIEnabled')
        return self


class CreateServiceMeshResponseBody(TeaModel):
    def __init__(self, request_id=None, service_mesh_id=None):
        self.request_id = request_id  # type: str
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateServiceMeshResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class CreateServiceMeshResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateServiceMeshResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateServiceMeshResponse, self).to_map()
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
            temp_model = CreateServiceMeshResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceRegistrySourceRequest(TeaModel):
    def __init__(self, service_mesh_id=None):
        self.service_mesh_id = service_mesh_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceRegistrySourceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        return self


class GetServiceRegistrySourceResponseBody(TeaModel):
    def __init__(self, status=None, request_id=None, result=None):
        self.status = status  # type: str
        self.request_id = request_id  # type: str
        self.result = result  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetServiceRegistrySourceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetServiceRegistrySourceResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetServiceRegistrySourceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetServiceRegistrySourceResponse, self).to_map()
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
            temp_model = GetServiceRegistrySourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(self, service_mesh_id=None, id=None, name=None, istio_version=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.istio_version = istio_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveBuiltinEnvoyFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        return self


class RemoveBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveBuiltinEnvoyFilterResponseBody, self).to_map()
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


class RemoveBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveBuiltinEnvoyFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveBuiltinEnvoyFilterResponse, self).to_map()
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
            temp_model = RemoveBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBuiltinEnvoyFilterRequest(TeaModel):
    def __init__(self, service_mesh_id=None, id=None, name=None, istio_version=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.id = id  # type: str
        self.name = name  # type: str
        self.istio_version = istio_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBuiltinEnvoyFilterRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.istio_version is not None:
            result['IstioVersion'] = self.istio_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('IstioVersion') is not None:
            self.istio_version = m.get('IstioVersion')
        return self


class GetBuiltinEnvoyFilterResponseBody(TeaModel):
    def __init__(self, parameters=None, request_id=None):
        self.parameters = parameters  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetBuiltinEnvoyFilterResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetBuiltinEnvoyFilterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetBuiltinEnvoyFilterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetBuiltinEnvoyFilterResponse, self).to_map()
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
            temp_model = GetBuiltinEnvoyFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitializeASMRoleResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(InitializeASMRoleResponseBody, self).to_map()
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


class InitializeASMRoleResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: InitializeASMRoleResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(InitializeASMRoleResponse, self).to_map()
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
            temp_model = InitializeASMRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMeshTagToEcsRequest(TeaModel):
    def __init__(self, service_mesh_id=None, ecs_id=None):
        self.service_mesh_id = service_mesh_id  # type: str
        self.ecs_id = ecs_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMeshTagToEcsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_mesh_id is not None:
            result['ServiceMeshId'] = self.service_mesh_id
        if self.ecs_id is not None:
            result['EcsId'] = self.ecs_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ServiceMeshId') is not None:
            self.service_mesh_id = m.get('ServiceMeshId')
        if m.get('EcsId') is not None:
            self.ecs_id = m.get('EcsId')
        return self


class AddMeshTagToEcsResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddMeshTagToEcsResponseBody, self).to_map()
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


class AddMeshTagToEcsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddMeshTagToEcsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddMeshTagToEcsResponse, self).to_map()
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
            temp_model = AddMeshTagToEcsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


